def validate_text(value: str, field_name: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string.")

    cleaned = value.strip()

    if not cleaned:
        raise ValueError(f"{field_name} cannot be empty.")

    if len(cleaned) < 20:
        raise ValueError(f"{field_name} must contain at least 20 characters.")

    return cleaned


if __name__ == "__main__":
    resume = "I am a Python developer with four years of experience."
    print(validate_text(resume, "resume"))