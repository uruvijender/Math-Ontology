import streamlit as st
from owlready2 import get_ontology, Thing, DataProperty
from pathlib import Path

# Load the ontology
ontology_path = "math_operations_ontology.owl"
onto = get_ontology(ontology_path).load()

# Function to perform operations
def perform_operation(operation, operand1, operand2):
    if operation == "Addition":
        return operand1 + operand2
    elif operation == "Subtraction":
        return operand1 - operand2
    elif operation == "Multiplication":
        return operand1 * operand2
    elif operation == "Division":
        return operand1 / operand2 if operand2 != 0 else "Error: Division by zero"

# Streamlit UI
st.title("Math Operations Using OWL Ontology")
st.write("Perform basic math operations using data from an OWL ontology.")

# Input fields
operation = st.selectbox("Select an operation:", ["Addition", "Subtraction", "Multiplication", "Division"])
operand1 = st.number_input("Enter the first operand:", value=0.0)
operand2 = st.number_input("Enter the second operand:", value=0.0)

# Perform calculation
if st.button("Calculate"):
    result = perform_operation(operation, operand1, operand2)
    st.write(f"Result of {operation}: {result}")

    # Save result in ontology
    with onto:
        # Search for the class dynamically
        operation_class = onto[operation]
        
        # Create a new instance of that class
        operation_instance = operation_class()
        
        # Set the data properties using the append method or direct assignment
        operation_instance.hasOperand1 = [operand1]  # Use a list to assign value
        operation_instance.hasOperand2 = [operand2]  # Use a list to assign value
        operation_instance.hasResult = [result]  # Use a list to assign value
        
        st.write(f"Data saved to ontology: {operation_instance}")

# Save updated ontology (optional)
if st.button("Save Ontology"):
    output_path = Path("updated_math_operations_ontology.owl")
    onto.save(file=str(output_path))
    st.write(f"Ontology saved to {output_path.resolve()}")
