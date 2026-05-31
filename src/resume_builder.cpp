#include "resume_builder.h"
#include <sstream>

std::string ResumeBuilder::generateResume(const std::string& skills) {
    std::ostringstream resume;
    resume << "=== Professional Resume ===\n";
    resume << "Skills: " << skills << "\n";
    resume << "Experience: 5 years in software development\n";
    resume << "Education: Bachelor's in Computer Science\n";
    return resume.str();
}