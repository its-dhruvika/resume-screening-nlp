from src.text_processing import load_text
from src.similarity import calculate_similarity

resumes_text = load_text("data/resumes.txt")
job_desc = load_text("data/job_description.txt")

resumes = resumes_text.split("\n\n")
scores = calculate_similarity(resumes, job_desc)

ranked = sorted(
    [(i+1, score[0]) for i, score in enumerate(scores)],
    key=lambda x: x[1],
    reverse=True
)

for rank, (resume_no, score) in enumerate(ranked, start=1):
    print(f"Rank {rank}: Resume {resume_no} - {score*100:.2f}% match")


