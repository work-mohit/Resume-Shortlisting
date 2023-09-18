from datasets import load_dataset
dataset = load_dataset("jacob-hugging-face/job-descriptions", split="train")

import random
num_rows = len(dataset["job_description"])

# Specify the number of random samples you want to extract
num_samples_to_extract = 15

# Create a list of unique random indices
random_indices = random.sample(range(num_rows), num_samples_to_extract)

# Extract random job descriptions and position titles
random_job_descriptions = pd.Series([dataset["job_description"][idx] for idx in random_indices])
random_position_titles = pd.Series([dataset["position_title"][idx] for idx in random_indices])

dataframe_jd = pd.concat([random_position_titles,random_job_descriptions],axis=1).rename(columns={0:'position',1:'job_description'})
dataframe_jd.to_csv('random_job_description.csv', index=False)