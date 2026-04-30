# -HDFS-log-anomaly-detection-Map-Reduce-
Scalable anomaly detection system for HDFS logs using Hadoop MapReduce for feature extraction and Random Forest for classification.



# HDFS Log Anomaly Detection using MapReduce and Machine Learning

##  Overview
This project implements a scalable anomaly detection system for distributed system logs using Hadoop MapReduce and Machine Learning.

##  Problem Statement
Detect anomalous behavior in HDFS logs using distributed processing and predictive modeling.

##  Dataset
- HDFS structured log dataset (100k logs)
- Key columns:
  - LineId
  - EventId
  - Component
  - Log Level

##  Methodology

1. MapReduce (Feature Extraction)
- Mapper extracts (window_id, EventId)
- Reducer aggregates event frequencies

2. Feature Engineering
- Convert logs into window-based feature matrix

 3. Machine Learning
- Model: Random Forest Classifier
- Task: Binary classification (Normal / Anomaly)

## Pipeline

HDFS Logs → MapReduce → Feature Matrix → ML Model → Prediction

## Results

Confusion Matrix:
[[340 17]
 [2 61]]

- Accuracy: 95%
- Recall (Anomaly): 97%
- Precision: 78%

## Visualizations

Include:
- Confusion Matrix
- Feature Importance

## Technologies Used
- Python
- Hadoop Streaming (simulated in Colab)
- Scikit-learn
- Pandas

## Key Highlights
- Scalable log processing using MapReduce
- High anomaly detection recall
- Hybrid Big Data + ML pipeline

## References
- https://github.com/logpai/loghub
- https://hadoop.apache.org/
- https://scikit-learn.org/
