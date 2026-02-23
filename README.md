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
