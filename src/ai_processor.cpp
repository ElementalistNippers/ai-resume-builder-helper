#include "ai_processor.h"
#include <algorithm>
#include <sstream>
#include <vector>

std::string AIProcessor::optimizeSkills(const std::string& skills) {
    std::istringstream iss(skills);
    std::vector<std::string> skillList;
    std::string skill;

    while (std::getline(iss, skill, ',')) {
        skill.erase(0, skill.find_first_not_of(" \t"));
        skill.erase(skill.find_last_not_of(" \t") + 1);
        if (!skill.empty()) {
            skillList.push_back(skill);
        }
    }

    if (skillList.empty()) {
        return "No skills provided";
    }

    std::ostringstream optimized;
    for (size_t i = 0; i < skillList.size(); ++i) {
        if (i != 0) optimized << ", ";
        optimized << skillList[i];
    }

    return optimized.str();
}