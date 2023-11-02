pip install streamlit sympy
import streamlit as st
import pandas as pd
from sympy import *

st.title("Algebraic Expressions and Equations Solver")

# Load data from CSV files
expressions_df = pd.read_csv('expressions.csv')
equations_df = pd.read_csv('equations.csv')

st.header("Algebraic Expressions")
st.table(expressions_df)

st.header("Algebraic Equations")
st.table(equations_df)

# Function to solve algebraic expressions and equations
def solve_expression(expression_str):
    x = symbols('x')
    expression = sympify(expression_str)
    result = simplify(expression)
    return result

def solve_equation(equation_str):
    x = symbols('x')
    equation = Eq(sympify(equation_str), 0)
    solution = solve(equation, x)
    return solution

# User input for solving expressions and equations
expression_input = st.text_input("Enter an expression:")
if st.button("Solve Expression"):
    if expression_input:
        try:
            result = solve_expression(expression_input)
            st.write(f"Simplified Expression: {result}")
        except Exception as e:
            st.error("Invalid Expression")

equation_input = st.text_input("Enter an equation:")
if st.button("Solve Equation"):
    if equation_input:
        try:
            solution = solve_equation(equation_input)
            st.write(f"Solutions for x: {solution}")
        except Exception as e:
            st.error("Invalid Equation")

st.sidebar.markdown("Note: Use 'x' as the variable in expressions and equations.")

st.write("Feel free to enter your own expressions and equations and click the buttons to solve them.")
