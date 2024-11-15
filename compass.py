# streamlit_app.py

import streamlit as st

def main():
    # Set page configuration
    st.set_page_config(page_title="Compass LLM Instruction Generator", layout="wide")

    # Header Section
    st.title("Compass LLM Instruction Generator")
    st.subheader("Create and Fine-Tune LLM Instructions for NCEA Achievement Standards")
    st.markdown("---")

    # Sidebar Navigation
    st.sidebar.title("Navigation")
    sections = ["Home", "Static Instructions", "Achievement Standard", "Clarifications", "Fine-Tuning", "Final Preview", "Settings"]
    selection = st.sidebar.radio("Go to", sections)

    if selection == "Home":
        home()
    elif selection == "Static Instructions":
        static_instructions()
    elif selection == "Achievement Standard":
        achievement_standard()
    elif selection == "Clarifications":
        clarifications()
    elif selection == "Fine-Tuning":
        fine_tuning()
    elif selection == "Final Preview":
        final_preview()
    elif selection == "Settings":
        settings()

def home():
    st.header("Welcome to the Compass LLM Instruction Generator")
    st.write("""
    This application helps you create and fine-tune language model instructions for NCEA Achievement Standards.
    Use the navigation menu on the left to get started.
    """)
    st.image("https://via.placeholder.com/800x400.png?text=Compass+LLM", use_column_width=True)

def static_instructions():
    st.header("Static Component of LLM Instructions")
    st.write("Generate the foundational instructions that define the AI assistant's identity, purpose, and general communication guidelines.")

    default_static_instructions = """
### IDENTITY AND PURPOSE
You are an AI teaching assistant specializing in New Zealand's Achievement Standards at the high school level. Your role is to assist students and teachers in understanding and applying concepts within their subject areas. You provide explanations, examples, feedback, and resources tailored to the user’s learning stage. You adapt your communication style and guidance level to support diverse learners.
"""
    static_instructions = st.text_area("Edit Static Instructions", default_static_instructions, height=300)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Save Static Instructions"):
            st.success("Static instructions saved.")
    with col2:
        if st.button("Reset to Default"):
            static_instructions = default_static_instructions
            st.success("Static instructions reset to default.")

def achievement_standard():
    st.header("Enter NCEA Achievement Standard URL")
    st.write("Input the URL of the NCEA Achievement Standard PDF. The app will parse the document to extract the title, purpose, credits, key terms, and achievement criteria.")

    achievement_standard_url = st.text_input("Enter the URL of the NCEA Achievement Standard PDF", "")
    if st.button("Parse Achievement Standard"):
        if achievement_standard_url:
            # Placeholder for parsing logic
            st.success("Parsing complete.")
            # Display extracted data for editing (placeholders)
            st.subheader("Extracted Details")
            title = st.text_input("Title", "Sample Achievement Standard Title")
            purpose = st.text_area("Purpose", "Sample purpose of the achievement standard.")
            credits = st.number_input("Credits", min_value=0, max_value=10, value=4)
            key_terms = st.text_area("Key Terms", "List of key terms...")
            achievement_criteria = st.text_area("Achievement Criteria", "Details of achievement criteria...")
        else:
            st.error("Please enter a valid URL.")

def clarifications():
    st.header("Generate Grading Clarifications")
    st.write("Automatically generate detailed grading clarifications for Not Achieved, Achieved, Merit, and Excellence levels using AI.")

    api_key = st.text_input("Enter OpenAI API Key", type="password")
    if st.button("Generate Clarifications"):
        if api_key:
            st.success("Clarifications generated.")
            st.write("Review and edit the generated clarifications below.")
            for level in ['Not Achieved', 'Achieved', 'Merit', 'Excellence']:
                with st.expander(level):
                    clarification_text = f"Sample clarification text for {level}."
                    st.text_area(f"{level} Clarifications", clarification_text, height=150)
            if st.button("Save Clarifications"):
                st.success("Clarifications saved.")
        else:
            st.error("Please enter your OpenAI API key.")

def fine_tuning():
    st.header("Adjust Grading Criteria")
    st.write("Customize the grading criteria to better align with specific teaching objectives or student needs.")

    for level in ['Not Achieved', 'Achieved', 'Merit', 'Excellence']:
        st.subheader(level)
        key_indicators = st.text_area(f"{level} Key Indicators", "", height=100)
        approach = st.text_area(f"{level} Approach", "", height=100)
        st.write("---")
    if st.button("Save Fine-Tuning Adjustments"):
        st.success("Fine-tuning adjustments saved.")

def final_preview():
    st.header("Final LLM Instruction Set")
    st.write("Review the complete AI assistant instructions before exporting or deploying.")

    final_instruction_set = "Compiled instruction set will appear here..."
    st.text_area("Final Instruction Set", final_instruction_set, height=500)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Download Instruction Set"):
            st.success("Instruction set downloaded.")
    with col2:
        if st.button("Copy to Clipboard"):
            st.success("Instruction set copied to clipboard.")
    with col3:
         if st.button("Deploy Instruction Set"):
            st.success("Instruction set deployed.")

def settings():
    st.header("Settings")
    st.write("Manage application settings and preferences.")

    st.subheader("API Key Management")
    st.write("Store, update, or remove your OpenAI API key.")
    api_key = st.text_input("OpenAI API Key", type="password")
    if st.button("Save API Key"):
        st.success("API key saved.")

    st.subheader("Default Values")
    if st.button("Reset All to Default"):
        st.success("All settings reset to default.")

    st.subheader("Privacy Settings")
    st.write("Information on how your data is handled.")

    st.subheader("About")
    st.write("Version 1.0.0")
    st.write("© 2023 Compass Education")

if __name__ == "__main__":
    main()
