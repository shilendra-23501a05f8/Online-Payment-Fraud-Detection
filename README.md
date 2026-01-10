💳 **Online Payment Fraud Detection System**

A machine learning–based web application that classifies online payment transactions as fraudulent or legitimate, trained on real-world transaction data and deployed as an interactive web app.

🚀 **Live Demo**<br>
👉 Live Application: [online-payment-fraud-detection.app](https://online-payment-fraud-detection-ml.streamlit.app/)<br>
📂 **Source Code**<br>
👉 GitHub Repository: https://github.com/shilendra-23501a05f8/Online-Payment-Fraud-Detection

📌**Problem Statement**<br>
Online payment systems face severe challenges due to extreme class imbalance, where fraudulent transactions are very rare but highly costly if missed.
This project focuses on detecting fraudulent transactions while prioritizing recall to minimize false negatives.

🧠 **Approach**<br>
Used PCA-transformed features (V1–V28) to preserve sensitive transaction information<br>
Trained a Decision Tree classifier on an imbalanced dataset<br>
Optimized the model to achieve high recall, which is critical in fraud detection<br>
Deployed the trained model as a real-time web application using Streamlit<br>

📊**Dataset Overview**<br>
Total transactions: 56,961<br>
Fraud cases: 98<br>
Fraud prevalence: 0.17%<br>
Features: 29 numerical features (V1–V28, normAmount)<br>

🧪 **Model Comparison**<br>
Three machine learning models were trained and evaluated on the same test set to compare performance on an extremely imbalanced fraud detection dataset.<br>
| Model               | Accuracy | Precision (Fraud) | Recall (Fraud) | F1 Score | ROC-AUC |
| ------------------- | -------- | ----------------- | -------------- | -------- | ------- |
| Logistic Regression | 97.40%   | 5.77%             | 90%            | 0.11     | 0.94    |
| Decision Tree       | 97.83%   | 7.17%             | 95%            | 0.13     | 0.96    |
| Random Forest       | 99.82%   | 48.65%            | 90%            | 0.63     | 0.95    |

**Confusion Matrices**<br>
The confusion matrices below provide a visual comparison of how each model handles legitimate and fraudulent transactions.<br>
🔹 Logistic Regression: [confusion_matrix_logistic_regression.png](https://github.com/shilendra-23501a05f8/Online-Payment-Fraud-Detection/blob/main/assets/confusion_matrix_lr.png)<br>
🔹 Decision Tree: [confusion_matrix_decision_tree.png](https://github.com/shilendra-23501a05f8/Online-Payment-Fraud-Detection/blob/main/assets/confusion_matrix_dt.png)<br>
🔹 Random Forest: [confusion_matrix_random_forest.png](https://github.com/shilendra-23501a05f8/Online-Payment-Fraud-Detection/blob/main/assets/confusion_matrix_rf.png)<br>

🏆 **Model Selection Rationale**<br>
Although Random Forest achieved the highest overall accuracy and precision, the Decision Tree model was selected for deployment due to the following reasons:<br>
Highest recall (95%), minimizing missed fraudulent transactions<br>
Strong ROC-AUC (0.96), indicating good class separability<br>
Very low inference latency (~1.3 ms), suitable for real-time prediction<br>
Better interpretability compared to ensemble models<br>
This choice reflects a practical trade-off between performance, interpretability, and deployment efficiency.<br>

📈 **Model Performance** (Test Set)<br>
Metric	Value<br>
Accuracy	97.83%<br>
Precision	7.17%<br>
Recall	95%<br>
F1 Score	0.13<br>
ROC-AUC	0.97<br>

⚠️ Note: Precision is low due to extreme class imbalance.<br>
High recall is intentionally prioritized to reduce missed fraudulent transactions, which are more costly than false positives in real-world systems.

⏱️ **Inference Performance**<br>
Average prediction latency: ~1.3 ms per request<br>
Model is loaded once at startup to ensure fast, real-time predictions<br>

⚙️ **Tech Stack**<br>
Language: Python<br>
Libraries: Pandas, NumPy, Scikit-learn<br>
Deployment: Streamlit Cloud<br>

📂**Project Structure**<br>
├── app.py<br>
├── fraud_model.pkl<br>
├── model_metrics.pkl<br>
├── requirements.txt<br>
├── Online_Payment_Fraud_Detection.ipynb<br>
└── README.md<br>

🛠️**Run Locally**<br>
pip install -r requirements.txt<br>
streamlit run app.py<br>




