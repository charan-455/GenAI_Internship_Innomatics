# GenAI App - AI Code Reviewer

GenAI App is a Python-based web application that allows users to submit their code for review. The application provides feedback on potential bugs, errors, and areas for improvement, along with suggestions for fixing the issues. Powered by Google Gen AI models and built with Streamlit, this app offers a user-friendly interface for seamless code review.

## Table of Contents
- [Objective](#objective)
- [Requirements](#requirements)
- [Key Features](#key-features)
- [Detailed Workflow](#detailed-workflow)
- [Streamlit Interface Example](#streamlit-interface-example)
- [Future Enhancements](#future-enhancements)
- [Deployment](#deployment)

---

## Objective

The goal of this project is to develop an application that:
- Allows users to submit your code for review.
- Analyzes the code for bugs, errors, and optimization opportunities.
- Provides suggestions for fixing issues.
- Displays the fixed code snippets for the user.

The application is designed to be user-friendly, efficient, and provide accurate feedback for improving code quality.

---

## Requirements

### **Python Libraries**
- **Streamlit**: To create the interactive, user-friendly web interface.
- **Google Generative AI**: For utilizing OpenAI's models to analyze and review the code.


### **Google Generative AI**
- Use **gemini-1.5-flash** model to analyze and review the submitted code.
- Provide recommendations for improvements, bug fixes, and optimized code snippets.

---

## Key Features

### **User Interface**
- **Code Input**: Users can input their code by either typing directly into a text box .
- **Submit Button**: After the user inputs their code, they can click a button to submit it for review.
- **Code Review Output**: After submission, the application will display:
  - A list of potential bugs and issues.
  - Suggestions for improvements and optimization.
  - A fixed version of the code.

### **Code Review Functionality**
- **Bug Detection**: The app will identify syntax errors, exceptions, and other potential bugs.
- **Code Optimization**: The app will provide recommendations for improving the performance and readability of the code.
- **Code Fixes**: The app will suggest and display corrected versions of the code.

---

## Detailed Workflow

### **Step 1: User Submits Code**
1. **Input Code**: 
   - Users can paste their Python code directly into a Streamlit text area or upload a `.py` file.
   
2. **Submit for Review**: 
   - When the user clicks the "Submit" button, the code is sent to the backend for analysis.

### **Step 2: Backend Processing**
   
1. **Send Code to OpenAI API**: 
   - The code is sent to google generative AI model to identify bugs, errors, and areas for improvement.
   
2. **Generate Review and Fixes**:
   - The model will return feedback with:
     - Identified issues or bugs.
     - Suggestions for code improvements.
     - A fixed version of the code.

### **Step 3: Display Results**
1. **Display the Review**:
   - The Streamlit app will display:
     - The original code.
     - The review feedback (bugs, suggestions, improvements).
     - The fixed code.

2. **User Feedback** (optional):
   - Provide users with the option to rate the quality of the code review or flag issues.
---