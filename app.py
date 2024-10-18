import streamlit as st

# Set up the Streamlit app
st.title("Simple Calculator")

# User input for numbers
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Dropdown for selecting the operation
operation = st.selectbox("Select the operation", ("Addition", "Subtraction", "Multiplication", "Division"))

# Calculate the result based on the selected operation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.write(f"The result of addition is: {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.write(f"The result of subtraction is: {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.write(f"The result of multiplication is: {result}")
    elif operation == "Division":
        if num2 == 0:
            st.write("Division by zero is not allowed.")
        else:
            result = num1 / num2
            st.write(f"The result of division is: {result}")
