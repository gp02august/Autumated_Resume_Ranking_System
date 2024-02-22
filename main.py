import os
import fitz 
import docx2txt
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer




# 1. List all files in the specified directory

files_in_directory = os.listdir('resumes/')

# 2. Filter the files with different extensions

docx_files = [file for file in files_in_directory if file.endswith('.docx')]
pdf_files = [file for file in files_in_directory if file.endswith('.pdf')]

# 3. Converting JD to text.
# 3.1 getting all files in the job-desc folder.

cwd = os.getcwd()
path = os.path.join(cwd, "job-desc")
files_in_jobdesc = os.listdir(path)
jd = ''

# 3.1 Confirming job-description only contains one file.

if len(files_in_jobdesc) == 1:
    
    file_name = files_in_jobdesc[0]

    # Check the file extension
    _, file_extension = os.path.splitext(file_name)

    # if file is pdf
    if (file_extension == '.pdf'):
        doc = fitz.open(files_in_jobdesc[0]) 
        for page in doc: 
            jd+=page.get_text() 
        
    elif (file_extension == '.docx'):
        file_path = os.path.join(path, file_name)
        jd = docx2txt.process(file_path) 

    else: 
        print('Invalid File Type')
        
   
else:
    print(f'There are {len(files_in_directory)} files in the directory. Expected only one.')


res_dict = {}
  


for i in docx_files:
    
    # Joining paths
    full_path = os.path.join('resumes', i)
    resume = docx2txt.process(full_path)
    content = [jd, resume]
    
    cv = CountVectorizer()
    matrix = cv.fit_transform(content)
    
    similarity_matrix = cosine_similarity(matrix)
    
    s = similarity_matrix[1][0] * 100

    res_dict.update({i:s})

# 4. for pdf files.

for i in pdf_files:
    
    # Joining paths
    full_path = os.path.join('resumes', i)
    resume = ''

    doc = fitz.open(full_path) 
    for page in doc: 
        resume+=page.get_text()
    content = [jd, resume]
    
    cv = CountVectorizer()
    matrix = cv.fit_transform(content)
    
    similarity_matrix = cosine_similarity(matrix)
    
    s = similarity_matrix[1][0] * 100

    res_dict.update({i:s})



# Sorting the list we get on the basis of values in the res_dict.

sorted_res_dict = dict(sorted(res_dict.items(), key=lambda item: item[1], reverse=True))

# finally storing the ranks with the resume file names and similarity.
final = {}

for rank, (similarity, res) in enumerate(sorted_res_dict.items(), start=1):
    final[rank] = [similarity, res]

print("\nHere is the final List. Rank, Resume, Similarity\n")

for i, j in final.items():
    print(i,j,"\n")
