# ATS Resume Expert

ATS Resume Expert is a Streamlit web application designed to assist job seekers in optimizing their resumes to align with specific job descriptions. The app integrates Google Generative AI to provide professional evaluations and suggestions, enhancing the chances of passing Applicant Tracking System (ATS) screenings.

---

## Features

1. **Job Description Analysis**: Analyze a provided resume against a job description and generate a professional evaluation of strengths and weaknesses.
2. **Skill Improvement Suggestions**: Provide actionable insights on improving skills based on the job description and resume.
3. **Percentage Match**: Evaluate the alignment of the resume with the job description and provide a percentage match, along with keywords present and missing.

---

## Prerequisites

### Software Requirements

- Python 3.8+
- Streamlit
- Poppler (for PDF processing)

### Python Libraries

Install the required libraries using pip:
```bash
pip install -r requirements.txt
```

### Environment Variables

Set up a `.env` file in the project root directory with the following variable:
```
GOOGLE_API_KEY=your_google_api_key_here
```

Replace `your_google_api_key_here` with your actual Google API key.

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd ats-resume-expert
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure Poppler is installed on your system:
   - **Windows**: Download and install Poppler from [Poppler Windows](http://blog.alivate.com.au/poppler-windows/).
   - **macOS/Linux**: Install via Homebrew or your package manager:
     ```bash
     brew install poppler
     ```

5. Update the `poppler_path` in the code if required (Windows users).

---

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open the app in your browser (default: `http://localhost:8501`).

3. Interact with the app:
   - Provide a job description in the text area.
   - Upload a resume in PDF format.
   - Use the buttons to:
     - **Tell me About the Resume**: Receive a professional evaluation.
     - **Percentage match**: Get the percentage match and keywords analysis.

---

## Project Structure

```
ats-resume-expert/
├── app.py               # Main application script
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables
├── README.md            # Project documentation
```

---

## Functions Overview

### 1. `get_gemini_response`
- **Description**: Sends input to Google Generative AI and retrieves the response.
- **Parameters**:
  - `input_text`: Text input from the user (job description).
  - `pdf_parts`: Processed PDF data.
  - `prompt`: Specific AI prompt to guide the response.
- **Returns**: AI-generated content.

### 2. `input_pdf_setup`
- **Description**: Processes the uploaded PDF, converts the first page to an image, and prepares it for API input.
- **Parameters**:
  - `uploaded_file`: The uploaded PDF file.
  - `poppler_path`: Optional path to Poppler installation.
- **Returns**: A list containing processed PDF parts.

---

## Prompts for AI Model

### Evaluation Prompt
```
You are an experienced HR with tech experience in the field of Data Science, Full Stack Web Development, 
Big Data Engineering, DevOps, and Data Analysis. Your task is to review the provided resume against the job description for these profiles.
Please share your professional evaluation on whether the candidate's profile aligns with the role.
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
```

### Percentage Match Prompt
```
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of Data Science, Full Stack Web Development, 
Big Data Engineering, DevOps, and Data Analysis. Your task is to evaluate the resume against the provided job description.
Give me the percentage match if the resume matches the job description. 
First, the output should include the percentage match, followed by keywords missing and present in the resume.
```

---

## Troubleshooting

1. **PDF Processing Errors**:
   - Ensure Poppler is installed and correctly configured.
   - Verify that the uploaded file is a valid PDF.

2. **Google API Errors**:
   - Check the API key in the `.env` file.
   - Ensure the Google API quota is not exceeded.

3. **Streamlit Issues**:
   - Update Streamlit to the latest version:
     ```bash
     pip install --upgrade streamlit
     ```

---

## Future Enhancements

- Add support for multi-page PDF processing.
- Improve AI prompts for better evaluations.
- Include a feature to download the evaluation report.
- Expand to support additional file formats (e.g., DOCX).

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.
