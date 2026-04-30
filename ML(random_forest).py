import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.utils import resample

# -----------------------------
# LOAD MAPREDUCE FEATURES
# -----------------------------
features = pd.read_csv("features.csv")

# fix column name
features.rename(columns={"window": "window_id"}, inplace=True)

# -----------------------------
# CREATE ANOMALY LABELS (same logic)
# -----------------------------
df = pd.read_csv("HDFS_100k.log_structured.csv")

df['window_id'] = df.index // 50

# event rarity
event_freq = df['EventId'].value_counts(normalize=True)
df['inv_weight'] = df['EventId'].map(lambda x: 1.0 / (event_freq.get(x, 1e-9)))

agg = df.groupby('window_id').agg(
    unique_events=('EventId', 'nunique'),
    rare_score=('inv_weight', 'sum')
).reset_index()

# normalize
agg['z_unique'] = (agg['unique_events'] - agg['unique_events'].mean()) / (agg['unique_events'].std() + 1e-9)
agg['z_rare'] = (agg['rare_score'] - agg['rare_score'].mean()) / (agg['rare_score'].std() + 1e-9)

agg['score'] = 0.6 * agg['z_rare'] + 0.4 * agg['z_unique']

# top 15% anomalies
threshold = agg['score'].quantile(0.85)
agg['label'] = (agg['score'] >= threshold).astype(int)

print("\nClass distribution:")
print(agg['label'].value_counts())

# -----------------------------
# MERGE
# -----------------------------
data = features.merge(agg[['window_id', 'label']], on='window_id')

# -----------------------------
# TRAIN TEST SPLIT
# -----------------------------
X = data.drop(columns=['window_id', 'label'])
y = data['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# -----------------------------
# BALANCE TRAIN DATA
# -----------------------------
train_df = pd.concat([X_train, y_train], axis=1)

normal = train_df[train_df.label == 0]
anomaly = train_df[train_df.label == 1]

anomaly_up = resample(anomaly, replace=True, n_samples=int(len(normal)*0.7), random_state=42)

train_bal = pd.concat([normal, anomaly_up])

X_train_bal = train_bal.drop(columns=['label'])
y_train_bal = train_bal['label']

# -----------------------------
# TRAIN MODEL
# -----------------------------
model = RandomForestClassifier(n_estimators=200, max_depth=12, class_weight='balanced')
model.fit(X_train_bal, y_train_bal)

# -----------------------------
# PREDICTION
# -----------------------------
proba = model.predict_proba(X_test)[:, 1]
y_pred = (proba >= 0.3).astype(int)

# -----------------------------
# RESULTS
# -----------------------------
print("\nCONFUSION MATRIX:")
print(confusion_matrix(y_test, y_pred))

print("\nCLASSIFICATION REPORT:")
print(classification_report(y_test, y_pred, zero_division=0))

# -----------------------------
# GRAPH
# -----------------------------
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.title("Confusion Matrix (MapReduce + ML)")
plt.show()