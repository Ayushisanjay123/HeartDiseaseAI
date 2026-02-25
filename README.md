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

## Deployment Implementation (deployment.py)

The `deployment.py` file implements the Streamlit web application for Heart Disease Prediction.

The trained Random Forest model is loaded using `pickle`, allowing predictions without retraining the model. Users enter medical details such as age, blood pressure, cholesterol level, ECG results, and other health parameters through an interactive interface.

The application:
- Collects user input using Streamlit fields
- Converts inputs into numerical format
- Sends data to the trained model
- Displays whether the person has heart disease or not

###  Run the App
streamlit run deployment.py

### Power BI Dashboard Data Preparation

A CSV file was generated to support Power BI dashboard visualization using the best-performing Machine Learning model (Random Forest Classifier).

The trained model was used to predict heart disease outcomes, and a new dataset was created containing:

- Patient feature data

- Actual heart disease labels

- Model predicted results

This dataset enables performance comparison and interactive visualization in Power BI.

### Process:

- Loaded processed dataset

- Generated predictions using the tuned Random Forest model

- Combined features, actual values, and predictions

Exported final dataset as CSV

### Output File

heart_disease_dashboard.csv

This file is used to build the Heart Disease Prediction Dashboard for model analysis and accuracy visualization.
