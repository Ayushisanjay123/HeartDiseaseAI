#  HeartDiseaseAI

##  Project Overview

**HeartDiseaseAI** is an end-to-end machine learning and deep learning project that predicts the presence of heart disease based on patient health attributes. The project covers data preprocessing, exploratory data analysis, machine learning model development, hyperparameter tuning, deep learning comparison, Streamlit deployment, and Power BI dashboard development.

---

##  Project Workflow
**Train-test data splitting**

* Data preprocessing and cleaning
* Exploratory Data Analysis (EDA) & visualization
* Dataset splitting (train–test)
* Machine Learning model training
* Hyperparameter tuning
* Deep Learning comparison
* Model deployment
* Power BI dashboard visualization

---

##  Machine Learning Phase

### Models Used

* Logistic Regression (Baseline)
* Random Forest Classifier

### Improvements

* Hyperparameter tuning using **GridSearchCV**
* Model selection based on performance metrics

### Evaluation Metrics

* Accuracy
* Confusion Matrix
* Feature Importance

### Results

* Logistic Regression Accuracy: **88.3%**
* Random Forest Accuracy: **88.47%**

Random Forest achieved the highest accuracy among the evaluated models and was selected for deployment.

### Model Saving

```
random_forest_model.pkl
```

---

##  Deep Learning – Artificial Neural Network (ANN)

An ANN model was implemented using TensorFlow/Keras to compare deep learning performance with machine learning models.

### ANN Workflow

* Data preprocessing & feature scaling
* Train–test split
* ANN model creation
* Model training and evaluation

### Performance

* ANN Accuracy: **88.44%**
* Random Forest Accuracy: **88.47%**

The ANN and Random Forest models achieved comparable accuracy. Random Forest performed marginally better and was therefore selected for deployment.
### Model Saving

```
model.save("ann_model.keras")
```

---

##  Deployment (Streamlit App)

The `deployment.py` file implements a Streamlit web application for heart disease prediction.

### Features

* User medical input interface
* Data preprocessing
* Prediction using trained Random Forest model
* Real-time prediction output based on user-provided input features
  > **Disclaimer:** This project is developed for educational and demonstration purposes only. It is not intended to provide medical diagnosis or replace professional medical advice.

### Run Application

```bash
streamlit run deployment.py
```

---

##  Power BI Dashboard

The Power BI dashboard uses a dataset containing patient attributes, actual heart disease labels, and model predictions to analyze prediction results and explore patterns within the dataset.

### Dataset Includes

* Patient features
* Actual labels
* Model predictions

### Output File

```
heart_disease_dashboard.csv
```

### Dashboard Features

### Dashboard Features

* KPI cards for patient and prediction statistics
* Interactive slicers for filtering
* Analysis of heart disease distribution
* Visualization of patient risk factors
* Comparison of actual and predicted outcomes
---

##  Tools & Technologies

* Python
* Scikit-learn
* TensorFlow / Keras
* Streamlit
* Power BI
* Pandas & NumPy

---

## Key Findings

* Random Forest achieved the highest accuracy among the evaluated models at 88.47%.
* ANN achieved a comparable accuracy of 88.44%.
* Hyperparameter tuning was used to improve the Random Forest model.
* Feature importance analysis was used to understand the contribution of input features to model predictions.
* The final Random Forest model was integrated into a Streamlit application for interactive prediction.

