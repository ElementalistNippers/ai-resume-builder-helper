#include "../src/ai_processor.h"
#include <cassert>

void testOptimizeSkills() {
    AIProcessor ai;
    std::string optimized = ai.optimizeSkills("  C++ , Python ,  AI  ");
    assert(optimized == "C++, Python, AI");
}

int main() {
    testOptimizeSkills();
    return 0;
}