from dotenv import load_dotenv
import base64
import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get Gemini response
def get_gemini_response(input_text, pdf_parts, prompt):
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    response = model.generate_content([input_text, pdf_parts, prompt])
    return response.text

# Function to process uploaded PDF
def input_pdf_setup(uploaded_file, poppler_path=None):
    if uploaded_file is not None:
        try:
            # Convert the PDF to images
            images = pdf2image.convert_from_bytes(
                uploaded_file.read(),
                poppler_path=poppler_path  # Specify poppler path if needed
            )

            # Extract the first page as an image
            first_page = images[0]

            # Convert image to bytes
            img_byte_arr = io.BytesIO()
            first_page.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()

            # Create PDF parts for API
            pdf_parts = [
                {
                    "mime_type": "image/jpeg",
                    "data": base64.b64encode(img_byte_arr).decode()
                }
            ]
            return pdf_parts
        except Exception as e:
            raise ValueError(f"Error converting PDF: {str(e)}")
    else:
        raise ValueError("No file uploaded")

# Streamlit App Configuration
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")

# Input fields
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

# Buttons for different actions
submit1 = st.button("Tell me About the Resume")
submit2 = st.button("How can I improve my Skills")
submit3 = st.button("Percentage match")

# Prompts for AI model
input_prompt1 = """
You are an experienced HR with tech experience in the field of Data Science, Full Stack Web Development, 
Big Data Engineering, DevOps, and Data Analysis. Your task is to review the provided resume against the job description for these profiles.
Please share your professional evaluation on whether the candidate's profile aligns with the role.
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of Data Science, Full Stack Web Development, 
Big Data Engineering, DevOps, and Data Analysis. Your task is to evaluate the resume against the provided job description.
Give me the percentage match if the resume matches the job description. 
First, the output should include the percentage match, followed by keywords missing and present in the resume.
"""

# Path to Poppler (for Windows users, update this path if needed)
poppler_path = r"C:\Program Files (x86)\poppler\Library\bin"  # Adjust based on your system, or set to None for default.

# Functionality for "Tell me About the Resume"
if submit1:
    if uploaded_file is not None:
        try:
            pdf_parts = input_pdf_setup(uploaded_file, poppler_path)
            response = get_gemini_response(input_prompt1, pdf_parts[0], input_text)  # Pass the first element of the list
            st.subheader("The Response is:")
            st.write(response)
        except ValueError as e:
            st.error(f"Error processing the PDF: {str(e)}")
    else:
        st.write("please upload the resume")

# Functionality for "Percentage match"
elif submit3:
    if uploaded_file is not None:
        try:
            pdf_parts = input_pdf_setup(uploaded_file, poppler_path)
            response = get_gemini_response(input_prompt3, pdf_parts[0], input_text)  # Pass the first element of the list
            st.subheader("The Response is:")
            st.write(response)
        except ValueError as e:
            st.error(f"Error processing the PDF: {str(e)}")
    else:
        st.write("please upload the resume")
