"""High-level resume builder combining parsing and generation."""

from .resume_parser import parse_sections, extract_skills
from .resume_generator import generate_docx


def build_resume(text: str, output_path: str) -> str:
    """Parse plain text resume content and generate a .docx file."""
    sections = parse_sections(text)
    skills = extract_skills(text)
    if skills:
        sections["skills"] = skills
    return generate_docx(sections, output_path)