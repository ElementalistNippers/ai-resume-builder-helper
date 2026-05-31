#include <iostream>
#include "resume_builder.h"
#include "ai_processor.h"

int main() {
    std::cout << "AI Resume Builder Helper\n";
    std::cout << "Enter your skills (comma separated): ";

    std::string skills;
    std::getline(std::cin, skills);

    AIProcessor ai;
    ResumeBuilder builder;

    std::string optimizedSkills = ai.optimizeSkills(skills);
    std::string resume = builder.generateResume(optimizedSkills);

    std::cout << "\nGenerated Resume:\n" << resume << "\n";
    return 0;
}