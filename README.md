# HeartDiseaseAI
Predict whether a patient has heart disease using medical attributes
Performed data preprocessing,EDA Visualization and dataset spliting.

Focused on machine learning model training using cross-validation. Due to execution time limitations in the Codespace environment, full model comparison could not be completed. Logistic Regression was successfully implemented as the baseline model, achieving 88.3% accuracy** for heart disease prediction. Further model comparison and deep learning implementation will continue in the next stage.

## Machine Learning Phase

Implemented disease prediction using Machine Learning models.

### Models Used
- Logistic Regression (baseline)
- Random Forest Classifier

### Improvements
- Applied GridSearchCV for hyperparameter tuning
- Selected best Random Forest model based on performance

### Evaluation
- Accuracy score
- Confusion Matrix
- Feature Importance analysis

### Model Saving
Final optimized model saved using pickle:
random_forest_model.pkl

Random Forest achieved better performance compared to Logistic Regression.

### Deep Learning – Artificial Neural Network (ANN)
Deep Learning – Artificial Neural Network (ANN)

An Artificial Neural Network (ANN) was implemented to perform heart disease prediction and to compare deep learning performance with the machine learning model.

### ANN Workflow

- Data preprocessing and feature scaling

- Train–test split

- ANN model creation using TensorFlow/Keras

- Model training and evaluation

- Model saving for deployment

### Model Performance

- ANN Accuracy: 0.8844 (88.44%)

### Model Accuracy Comparison

Random Forest (Machine Learning): 0.8847

ANN (Deep Learning): 0.8844

Although ANN achieved comparable performance, the Random Forest model provided slightly better accuracy and was selected as the final model for deployment.

The Random Forest model slightly outperformed the ANN model, therefore it is selected as the final model for deployment, while ANN serves as a deep learning benchmark.

### Model Saving

The trained ANN model was saved using:

model.save("ann_model.keras")
