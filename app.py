import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image

# Load the trained Random Forest Classifier model
pickle_in = open("RandomClassifier.pkl", "rb")
RFC = pickle.load(pickle_in)

# Welcome function
def welcome():
    return "Welcome All"

# Prediction function
def predict_note_authentication(Gender, Age, Smoking, Yellow_fingers, Anxiety, PeerPressure, Chronic_disease, Fatigue, Allergy, Wheezing, Alcohal, Coughing, Breadth_shortness, Swallowing_diff, Chest_pain):
    prediction = RFC.predict([[Gender, Age, Smoking, Yellow_fingers, Anxiety, PeerPressure, Chronic_disease,
                             Fatigue, Allergy, Wheezing, Alcohal, Coughing, Breadth_shortness, Swallowing_diff, Chest_pain]])
    return 'You May have Cancer' if prediction[0] == 1 else 'You  May Do not have Cancer'

# Main function for the Streamlit app
def main():
    html_temp = """
    <div style="background-color:black;padding:10px">
    <h2 style="color:white;text-align:center;">Lung Cancer App: Detecting the Signs Early </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Input fields for user to enter data
    Gender = st.selectbox("Gender", options=["Female", "Male"], index=0)
    Gender = 0 if Gender == "Female" else 1
    
    Age = st.text_input("Age", placeholder="Enter Your Age")
    
    Smoking = st.selectbox("Smoking", options=["No", "Yes"], index=0)
    Smoking = 1 if Smoking == "No" else 2

    Yellow_fingers = st.selectbox("Yellow_fingers", options=["No", "Yes"], index=0)
    Yellow_fingers = 1 if Yellow_fingers == "No" else 2
    
    Anxiety = st.selectbox("Anxiety", options=["No", "Yes"], index=0)
    Anxiety = 1 if Anxiety == "No" else 2
    
    PeerPressure = st.selectbox("PeerPressure", options=["No", "Yes"], index=0)
    PeerPressure = 1 if PeerPressure == "No" else 2
    
    Chronic_disease = st.selectbox("Chronic_disease", options=["No", "Yes"], index=0)
    Chronic_disease = 1 if Chronic_disease == "No" else 2
    
    Fatigue = st.selectbox("Fatigue", options=["No", "Yes"], index=0)
    Fatigue = 1 if Fatigue == "No" else 2
    
    Allergy = st.selectbox("Allergy", options=["No", "Yes"], index=0)
    Allergy = 1 if Allergy == "No" else 2
    
    Wheezing = st.selectbox("Wheezing", options=["No", "Yes"], index=0)
    Wheezing = 1 if Wheezing == "No" else 2
    
    Alcohal = st.selectbox("Alcohal", options=["No", "Yes"], index=0)
    Alcohal = 1 if Alcohal == "No" else 2
    
    Coughing = st.selectbox("Coughing", options=["No", "Yes"], index=0)
    Coughing = 1 if Coughing == "No" else 2
    
    Breadth_shortness = st.selectbox("Breadth_shortness", options=["No", "Yes"], index=0)
    Breadth_shortness = 1 if Breadth_shortness == "No" else 2
    
    Swallowing_diff = st.selectbox("Swallowing_diff", options=["No", "Yes"], index=0)
    Swallowing_diff = 1 if Swallowing_diff == "No" else 2
    
    Chest_pain = st.selectbox("Chest_pain", options=["No", "Yes"], index=0)
    Chest_pain = 1 if Chest_pain == "No" else 2

    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(Gender, Age, Smoking, Yellow_fingers, Anxiety, PeerPressure, Chronic_disease,
                                             Fatigue, Allergy, Wheezing, Alcohal, Coughing, Breadth_shortness, Swallowing_diff, Chest_pain)
    st.success('Output: {}'.format(result))

    # Sidebar options
    st.sidebar.title("Cancer Symptoms")
    st.sidebar.image("image.png")

    # About Tab
    about_expander = st.sidebar.expander("About")
    with about_expander:
        st.write(
            "This is a Lung Cancer Detection ML App built using Streamlit.")
        st.write(
            "It predicts the likelihood of lung cancer based on various factors.")
        st.write("Built by LTCE TEAM")
        #st.write("Github Repo Here for Future")

    # Help Tab
    help_expander = st.sidebar.expander("How to Give Inputs")
    with help_expander:
        st.write("This app helps in predicting lung cancer.")
        st.write(
            "Enter the required information in the main section and click 'Predict' to get the result.")
        st.write("Input for the Gender:")
        st.write("Female = 0")
        st.write("Male = 1")
        st.write("Input for the Symptom Features:")
        st.write("No = 1")
        st.write("Yes = 2")

if __name__ == '__main__':
    main()
