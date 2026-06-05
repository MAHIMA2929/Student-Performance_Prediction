import streamlit as st
import pickle

# Page Configuration
st.set_page_config(
    page_title="🎓 Student Performance Prediction",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 Student Performance Prediction System")
st.markdown("### 📊 Predict whether a student will PASS or FAIL")

st.markdown("---")

# Load Model
with open("student_pass_fail_model.pkl", "rb") as file:
    model = pickle.load(file)

# Inputs
st.subheader("Enter Student Details")

study_hours = st.number_input(
    "Study Hours Per Day",
    min_value=0.0,
    max_value=15.0,
    step=0.5
)

attendance = st.number_input(
    "Attendance Percentage (%)",
    min_value=0,
    max_value=100
)

previous_score = st.number_input(
    "Previous Exam Score",
    min_value=0,
    max_value=100
)

# Prediction Button
if st.button("Predict Result"):

    prediction = model.predict(
        [[study_hours, attendance, previous_score]]
    )

    st.markdown("---")
    st.subheader("📈 Prediction Result")

    if prediction[0] == 1:
        st.success("Congratulations! Student is likely to PASS ")
        st.balloons()
        st.write("Keep up the good work!")
    else:
        st.error("Student is likely to FAIL")
        st.write("More study and better attendance may help improve performance.")