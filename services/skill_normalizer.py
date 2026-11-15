import re
from collections.abc import Iterable


SKILL_ALIASES = {
    "JavaScript": ["JS", "Javascript"],
    "PostgreSQL": ["Postgres", "Postgre"],
    "React": ["ReactJS"],
    "Node.js": ["Node", "NodeJS"],
    "Python": [],
    "TypeScript": ["TS"],
}

_ALIAS_LOOKUP = {
    re.sub(r"\s+", " ", name.strip()).casefold(): canonical
    for canonical, aliases in SKILL_ALIASES.items()
    for name in (canonical, *aliases)
}


def normalize_skills(skills: Iterable[str]) -> list[str]:
    """Convert known skill aliases to canonical names, retaining unique unknowns."""
    if isinstance(skills, str):
        raise TypeError("skills must be an iterable of strings, not a string.")

    normalized = []
    seen = set()

    for skill in skills:
        if not isinstance(skill, str):
            raise TypeError("each skill must be a string.")

        cleaned = re.sub(r"\s+", " ", skill.strip())
        if not cleaned:
            continue

        canonical = _ALIAS_LOOKUP.get(cleaned.casefold(), cleaned)
        if canonical not in seen:
            normalized.append(canonical)
            seen.add(canonical)

    return normalized
