import streamlit as st
import pandas as pd

def main():
    st.set_page_config(page_title="All-in-One Professional Tools", page_icon="🛠", layout="wide")
    st.markdown(
        """
        <style>
        .stApp {background: linear-gradient(to right, #ff9966, #ff5e62);}
        .title {text-align: center; color: white;}
        .result-box {background-color:#d4edda; padding:10px; border-radius:5px;}
        </style>
        """, unsafe_allow_html=True
    )
    
    st.title("🛠 All-in-One Professional Tools Suite")
    st.markdown("---")
    st.write("Enhance your productivity with essential tools for everyday calculations and conversions.")
    
    tool = st.sidebar.radio("Select a Tool", ["Calculator", "Unit Converter", "BMI Calculator"], index=1)
    
    if tool == "Calculator":
        calculator()
    elif tool == "Unit Converter":
        unit_converter()
    elif tool == "BMI Calculator":
        bmi_calculator()

def calculator():
    st.subheader("🧮 Advanced Calculator")
    num1 = st.text_input("Enter first number", "", placeholder="Enter a value")
    num2 = st.text_input("Enter second number", "", placeholder="Enter a value")
    operation = st.selectbox("Choose an operation", ["Addition", "Subtraction", "Multiplication", "Division"], index=0)
    
    if st.button("Compute", use_container_width=True):
        try:
            num1, num2 = float(num1), float(num2)
            if operation == "Addition":
                result = num1 + num2
            elif operation == "Subtraction":
                result = num1 - num2
            elif operation == "Multiplication":
                result = num1 * num2
            elif operation == "Division":
                result = num1 / num2 if num2 != 0 else "Error: Cannot divide by zero"
            st.markdown(f"<div class='result-box'><b>Result:</b> {result:.2f}</div>", unsafe_allow_html=True)
        except ValueError:
            st.error("Please enter valid numbers.")

def unit_converter():
    st.subheader("📏 Universal Unit Converter")
    unit_type = st.radio("Select Unit Type", ["Length", "Weight", "Temperature", "Speed", "Volume"], index=0)
    
    units = {
        "Length": ["Meters", "Kilometers", "Miles", "Yards", "Feet"],
        "Weight": ["Grams", "Kilograms", "Pounds", "Ounces"],
        "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
        "Speed": ["Meters/Second", "Kilometers/Hour", "Miles/Hour"],
        "Volume": ["Liters", "Milliliters", "Cubic Meters", "Gallons"]
    }
    
    value = st.text_input("Enter value", "", placeholder="Enter a value")
    from_unit = st.selectbox("From", units[unit_type])
    to_unit = st.selectbox("To", units[unit_type])
    
    if st.button("Convert", use_container_width=True):
        try:
            value = float(value)
            converted_value = convert_units(value, from_unit, to_unit)
            st.markdown(f"<div class='result-box'><b>Converted Value:</b> {converted_value}</div>", unsafe_allow_html=True)
        except ValueError:
            st.error("Please enter a valid numeric value.")

def convert_units(value, from_unit, to_unit):
    conversions = {
        "Meters": {"Kilometers": 0.001, "Miles": 0.000621371, "Yards": 1.09361, "Feet": 3.28084},
        "Kilometers": {"Meters": 1000, "Miles": 0.621371, "Yards": 1093.61, "Feet": 3280.84},
        "Grams": {"Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274},
        "Kilograms": {"Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274},
        "Celsius": {"Fahrenheit": lambda c: (c * 9/5) + 32, "Kelvin": lambda c: c + 273.15},
        "Fahrenheit": {"Celsius": lambda f: (f - 32) * 5/9, "Kelvin": lambda f: ((f - 32) * 5/9) + 273.15},
        "Kelvin": {"Celsius": lambda k: k - 273.15, "Fahrenheit": lambda k: ((k - 273.15) * 9/5) + 32},
    }
    
    if from_unit == to_unit:
        return value
    
    if from_unit in conversions and to_unit in conversions[from_unit]:
        conversion = conversions[from_unit][to_unit]
        return conversion(value) if callable(conversion) else value * conversion
    else:
        return "Conversion not available"

def bmi_calculator():
    st.subheader("⚖️ Body Mass Index (BMI) Calculator")
    weight = st.text_input("Enter your weight (kg)", "", placeholder="Enter weight")
    height = st.text_input("Enter your height (m)", "", placeholder="Enter height")
    
    if st.button("Calculate BMI", use_container_width=True):
        try:
            weight, height = float(weight), float(height)
            if height > 0:
                bmi = weight / (height ** 2)
                df = pd.DataFrame({"Category": ["Underweight", "Normal", "Overweight", "Obese"],
                                   "BMI Range": ["<18.5", "18.5 - 24.9", "25 - 29.9", ">=30"]})
                st.markdown(f"<div class='result-box'><b>Your BMI:</b> {bmi:.2f}</div>", unsafe_allow_html=True)
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
                st.error("Please enter a valid height.")
        except ValueError:
            st.error("Please enter valid numeric values.")

if __name__ == "__main__":
    main()
