"""Parse resume text into structured sections."""

import re
from typing import Dict, List


def parse_sections(text: str) -> Dict[str, List[str]]:
    """Split plain text resume into basic sections."""
    sections = {
        "summary": [],
        "experience": [],
        "education": [],
        "skills": [],
    }
    current_key = "summary"

    for line in text.strip().splitlines():
        line = line.strip()
        lower = line.lower()
        if "experience" in lower:
            current_key = "experience"
        elif "education" in lower:
            current_key = "education"
        elif "skills" in lower:
            current_key = "skills"
        elif line and current_key in sections:
            sections[current_key].append(line)

    return sections


def extract_skills(text: str) -> List[str]:
    """Return a simple list of known tech skills found in text."""
    known = {
        "python", "java", "javascript", "typescript", "react", "flask",
        "docker", "kubernetes", "sql", "aws", "git", "machine learning",
    }
    words = re.findall(r"[a-zA-Z#+]+", text.lower())
    return sorted(set(w for w in words if w in known))