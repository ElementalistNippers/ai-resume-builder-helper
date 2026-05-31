"""Tests for resume parser and builder."""

from src.resume_parser import parse_sections, extract_skills
from src.builder import build_resume
import os
import tempfile


def test_parse_sections():
    text = """Summary line here.
Experience
Software Engineer at Corp
Education
MIT
Skills
Python, Docker"""
    sections = parse_sections(text)
    assert "Summary line here." in sections["summary"]
    assert "Software Engineer at Corp" in sections["experience"]
    assert "MIT" in sections["education"]
    assert "Python, Docker" in sections["skills"]


def test_extract_skills():
    text = "I know Python, Java, and AWS."
    skills = extract_skills(text)
    assert "python" in skills
    assert "java" in skills
    assert "aws" in skills
    assert "go" not in skills


def test_build_resume_creates_file():
    text = "Summary\nExperience\nDev at ACME\nEducation\nUCLA\nSkills\nPython"
    with tempfile.NamedTemporaryFile(suffix=".docx", delete=False) as tmp:
        path = build_resume(text, tmp.name)
        assert os.path.exists(path)
        os.unlink(path)