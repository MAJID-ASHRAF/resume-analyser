import re

from validators.input_validator import validate_text


SKILLS = [
    "Python",
    "JavaScript",
    "Java",
    "React",
    "React Native",
    "Next.js",
    "TypeScript",
    "Redux",
    "FastAPI",
    "PostgreSQL",
    "AWS",
    "REST APIs",
    "Node.js",
    "Express.js",
    "MongoDB",
    "MySQL",
    "Docker",
    "Kubernetes",
    "HTML",
    "CSS",
    "Tailwind CSS",
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
]


# Compile patterns once, prioritizing longer skill names.
SKILL_PATTERNS = [
    (
        skill,
        re.compile(
            r"(?<!\w)"
            + r"\s+".join(
                re.escape(word) for word in skill.split()
            )
            + r"(?!\w)",
            re.IGNORECASE,
        ),
    )
    for skill in sorted(SKILLS, key=len, reverse=True)
]


def extract_skills(text: str) -> list[str]:
    """
    Extract skills using case-insensitive regex matching.

    Features:
    - Longest-match-first strategy
    - Word boundary protection
    - Multi-word skill support
    - Duplicate prevention
    - Overlapping match resolution
    - Input validation
    """

    cleaned = validate_text(text, "resume")

    extracted = []
    extracted_set = set()
    occupied_positions = []

    for skill, pattern in SKILL_PATTERNS:

        for match in pattern.finditer(cleaned):

            start, end = match.span()

            # Check overlap with previously matched skills.
            overlaps = any(
                start < occupied_end and end > occupied_start
                for occupied_start, occupied_end in occupied_positions
            )

            if overlaps:
                continue

            occupied_positions.append((start, end))

            if skill not in extracted_set:
                extracted.append(skill)
                extracted_set.add(skill)

    return extracted


if __name__ == "__main__":
    print(extract_skills("I have worked with React Native and React for four years."))