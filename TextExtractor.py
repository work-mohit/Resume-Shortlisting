from pdfminer.high_level import extract_text
import os
import re
import pandas as pd
DATA_DIR = './Resume/data/'
resume_dfs = []

for job_type in os.listdir(DATA_DIR):
    resume_path = os.path.join(DATA_DIR, job_type)
    for resume in os.listdir(resume_path):
        text = extract_text(os.path.join(resume_path, resume))

        category_match = re.search(r'^(.+?)\n', text, re.MULTILINE)
        skills_match = re.search(r'skills\n(.+?)\n\n', text, re.DOTALL | re.IGNORECASE)
        education_match = re.search(r'Education(?: and Training|al Background)?\n(.+?)\n\n', text, re.DOTALL | re.IGNORECASE)

        category = job_type + ','
        skills = ''
        education = ''
        id = resume[:-4]

        if category_match:
            category += category_match.group(1).strip()
        if skills_match:
            skills = skills_match.group(1).strip().replace('\n', ' ')
        if education_match:
            education = education_match.group(1).strip().replace('\n', ' ')


        resume_df = pd.DataFrame({'resume_id':[id],'Category': [category], 'Skills': [skills], 'Education': [education]})
        resume_dfs.append(resume_df)

resume_dfs = pd.concat(resume_dfs, ignore_index=True)
resume_dfs.to_csv('resume_details.csv', index=False)