import streamlit as st
import pandas as pd
import math

def main():
    st.set_page_config(page_title="All-in-One Professional Tools", page_icon="🛠", layout="wide")
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f2f6;
        }
        .stApp {
            background: linear-gradient(to right, #ff9966, #ff5e62);
        }
        .title {
            text-align: center;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True
    )
    
    st.title("🛠 All-in-One Professional Tools Suite")
    st.markdown("---")
    st.write("Enhance your productivity with essential tools for everyday calculations and conversions.")
    
    # Sidebar Navigation
    tool = st.sidebar.radio("Select a Tool", ["Calculator", "Unit Converter", "BMI Calculator"], index=0)
    
    if tool == "Calculator":
        calculator()
    elif tool == "Unit Converter":
        unit_converter()
    elif tool == "BMI Calculator":
        bmi_calculator()

def calculator():
    st.subheader("🧮 Advanced Calculator")
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number", value=, format="%.2f")
    with col2:
        num2 = st.number_input("Enter second number", value=, format="%.2f")
    
    operation = st.selectbox("Choose an operation", ["Addition", "Subtraction", "Multiplication", "Division"], index=0)
    
    if st.button("Compute", use_container_width=True):
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            result = num1 / num2 if num2 != 0 else "Error: Cannot divide by zero"
        
        st.success(f"Result: {result:.2f}")

def unit_converter():
    st.subheader("📏 Universal Unit Converter")
    unit_type = st.radio("Select Unit Type", ["Length", "Weight", "Temperature"], index=0)
    
    if unit_type == "Length":
        length_converter()
    elif unit_type == "Weight":
        weight_converter()
    elif unit_type == "Temperature":
        temperature_converter()

def length_converter():
    st.write("Convert between meters and kilometers.")
    value = st.number_input("Enter length (meters)", value=, format="%.2f")
    st.success(f"{value} meters = {value / 1000:.4f} kilometers")

def weight_converter():
    st.write("Convert between grams and kilograms.")
    value = st.number_input("Enter weight (grams)", value=, format="%.2f")
    st.success(f"{value} grams = {value / 1000:.4f} kilograms")

def temperature_converter():
    st.write("Convert between Celsius and Fahrenheit.")
    value = st.number_input("Enter temperature (°C)", value=, format="%.2f")
    st.success(f"{value}°C = {(value * 9/5) + 32:.2f}°F")

def bmi_calculator():
    st.subheader("⚖️ Body Mass Index (BMI) Calculator")
    weight = st.number_input("Enter your weight (kg)", value=, format="%.2f")
    height = st.number_input("Enter your height (m)", value=0.0, format="%.2f")
    
    if st.button("Calculate BMI", use_container_width=True):
        if height > 0:
            bmi = weight / (height ** 2)
            df = pd.DataFrame({"Category": ["Underweight", "Normal Weight", "Overweight", "Obese"],
                               "BMI Range": ["<18.5", "18.5 - 24.9", "25 - 29.9", ">=30"]})
            st.success(f"Your BMI is: {bmi:.2f}")
            st.dataframe(df)
            if bmi < 18.5:
                st.info("You are underweight. Consider a balanced diet.")
            elif 18.5 <= bmi < 24.9:
                st.success("You have a healthy weight. Keep it up!")
            elif 25 <= bmi < 29.9:
                st.warning("You are overweight. Consider a healthy lifestyle.")
            else:
                st.error("You are obese. Consult a healthcare provider.")
        else:
            st.error("Height must be greater than zero")
    
if __name__ == "__main__":
    main()


