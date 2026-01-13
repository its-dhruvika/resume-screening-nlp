from src.text_processing import load_text
from src.similarity import calculate_similarity

resumes_text = load_text("data/resumes.txt")
job_desc = load_text("data/job_description.txt")

resumes = resumes_text.split("\n\n")
scores = calculate_similarity(resumes, job_desc)

for i, score in enumerate(scores):
    print(f"Resume {i+1} Match Score: {score[0] * 100:.2f}%")
