from services.skill_extractor import extract_skills
from services.skill_normalizer import normalize_skills
from validators.input_validator import validate_text


def analyze_resume(resume_text: str) -> dict:

    validated_text = validate_text(resume_text, "resume")

    extracted_skills = extract_skills(validated_text)

    normalized_skills = normalize_skills(extracted_skills)

    return {"skills": normalized_skills}