# Autumated_Resume_Ranking_System

Readme for Resume Matching Tool
This Python script is designed to compare resumes against a job description (JD) and rank them based on similarity using cosine similarity scores. The tool supports both DOCX and PDF file formats.

# Code Editor : 
VsCode

# Prerequisites
Make sure to have the required libraries installed before running the script. You can install them using the following:
* 'pip install PyMuPDF docx2txt scikit-learn'

# Usage
Directory Structure:
Place the job description file in the job-desc directory.
Resumes should be in the resumes directory.

Supported File Formats:
Resumes: Supports both DOCX and PDF formats.
Job Description: Supports both DOCX and PDF formats.
Running the Script:

Execute the script in a Python environment.
* 'python main.py'

# Important Notes
* Ensure there is only one file in the job-desc directory.
  The script uses cosine similarity scores for comparison.
Resumes are ranked in descending order of similarity.


# Output
The output includes the rank, resume file name, and similarity percentage. Output is a dictionary of rank(integer) as key and list having resume name(str) and similarity percentage(float) as value, based on their similarity to the job description.
