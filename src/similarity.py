from sentence_transformers import SentenceTransformer, util

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def calculate_similarity(resumes, job_description):
    resume_embeddings = model.encode(resumes, convert_to_tensor=True)
    job_embedding = model.encode(job_description, convert_to_tensor=True)

    scores = util.cos_sim(resume_embeddings, job_embedding)
    return scores
