<img width="2752" height="1536" alt="Gemini_Generated_Image_75bmtx75bmtx75bm" src="https://github.com/user-attachments/assets/c9a0d9fc-eeac-43d4-a484-fb05b4f6c2a5" /># HDFS Log Anomaly Detection using MapReduce and Machine Learning
Scalable anomaly detection system for HDFS logs using Hadoop MapReduce for feature extraction and Random Forest for classification.

## Overview
This project implements a scalable anomaly detection system for distributed system logs using Hadoop MapReduce and Machine Learning.

Problem Statement
Detect anomalous behavior in HDFS logs using distributed processing and predictive modeling.

## Dataset
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

<img width="2752" height="1536" alt="Gemini_Generated_Image_75bmtx75bmtx75bm" src="https://github.com/user-attachments/assets/98ac0e98-836d-4619-9ef7-d572c1db563b" />



## Results

Confusion Matrix:
<img width="507" height="455" alt="image" src="https://github.com/user-attachments/assets/b5f3673a-3758-4c29-9f23-61adb8cb494d" />


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
