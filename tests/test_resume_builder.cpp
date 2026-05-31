#include "../src/resume_builder.h"
#include <cassert>

void testGenerateResume() {
    ResumeBuilder builder;
    std::string resume = builder.generateResume("C++, Python");
    assert(resume.find("C++, Python") != std::string::npos);
    assert(resume.find("Experience") != std::string::npos);
}

int main() {
    testGenerateResume();
    return 0;
}