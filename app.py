import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
st.title("Advertisement Prediction Model")


def advertisement_prediction(input_data: list):
    scaled_data = scaler.transform([input_data])
    prediction = model.predict(scaled_data)
    print(prediction)
    if prediction[0]:
        return "The Advertisement will be clicked."
    else:
        return "The Advertisement will not be clicked."


def main():
    st.subheader("Enter the details")
    daily_time_spent = st.number_input("Daily Time Spent on the Site")
    age = st.number_input("Age")
    area_income = st.number_input("Area Income")
    daily_internet_usage = st.number_input("Daily Internet Usage")
    gender = st.selectbox("Gender", ("Male", "Female"))
    gender = ["Female", "Male"].index(gender)

    prediction = ""

    if st.button("Predict"):
        prediction = advertisement_prediction([daily_time_spent, int(age), area_income,
                                               daily_internet_usage, int(gender)])

    st.success(prediction)


if __name__ == "__main__":
    main()
