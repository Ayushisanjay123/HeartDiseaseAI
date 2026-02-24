import pickle 
import numpy as np
import streamlit as st


loaded_model = pickle.load(open(r'/workspaces/HeartDiseaseAI/random_forest_model.pkl', 'rb'))


def heart_disease_prediction(input_data):

    input_data_as_numpy_array = np.asarray(input_data, dtype=float)

    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return " The person does NOT have Heart Disease"
    else:
        return " The person HAS Heart Disease"


def main():

    st.title("❤️ Heart Disease Prediction Web App")

    st.write("Enter patient medical details below:")

    Age = st.text_input("Age")
    Sex = st.text_input("Sex (0 = Female, 1 = Male)")
    ChestPainType = st.text_input("Chest Pain Type")
    BP = st.text_input("Resting Blood Pressure")
    Cholesterol = st.text_input("Cholesterol")
    FBS = st.text_input("Fasting Blood Sugar > 120 (1 = True, 0 = False)")
    EKG = st.text_input("EKG Results")
    MaxHR = st.text_input("Maximum Heart Rate")
    ExerciseAngina = st.text_input("Exercise Induced Angina (1 = Yes, 0 = No)")
    STdepression = st.text_input("ST Depression")
    SlopeST = st.text_input("Slope of ST Segment")
    Vessels = st.text_input("Number of Major Vessels")
    Thallium = st.text_input("Thallium Test Result")

    diagnosis = ""

    if st.button("Heart Disease Test Result"):

        input_data = [
            Age, Sex, ChestPainType, BP, Cholesterol,
            FBS, EKG, MaxHR, ExerciseAngina,
            STdepression, SlopeST, Vessels, Thallium
        ]

        diagnosis = heart_disease_prediction(input_data)

    st.success(diagnosis)


if __name__ == '__main__':
    main()