#  HeartDiseaseAI

##  Project Overview

**HeartDiseaseAI** is a machine learning and deep learning project that predicts whether a patient has heart disease using medical attributes.
The project includes data preprocessing, exploratory data analysis (EDA), model training, deployment using Streamlit, and an interactive Power BI analytics dashboard.

---

##  Project Workflow

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

* Accuracy Score
* Confusion Matrix
* Feature Importance Analysis

### Results

* Logistic Regression Accuracy: **88.3%**
* Random Forest Accuracy: **88.47%**

✅Random Forest achieved better performance and was selected as the final model.

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

Although performance was comparable, Random Forest slightly outperformed ANN and was chosen for deployment.

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
* Instant disease prediction output

### Run Application

streamlit run deployment.py
```

---

##  Power BI Dashboard

A dataset was generated using the best-performing Random Forest model to enable interactive visualization.

### Dataset Includes

* Patient features
* Actual labels
* Model predictions

### Output File

```
heart_disease_dashboard.csv
```

### Dashboard Features

* KPI cards for patient statistics and model accuracy
* Interactive slicers for filtering
* Visual analysis of disease distribution and risk factors

---

## 🛠 Tools & Technologies

* Python
* Scikit-learn
* TensorFlow / Keras
* Streamlit
* Power BI
* Pandas & NumPy

---

## 📈 Key Insights

* Elevated fasting blood sugar increases diabetes-related risk.
* Cholesterol and blood pressure strongly influence heart disease prediction.
* Random Forest provided the most stable performance.


