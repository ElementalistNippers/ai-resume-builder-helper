cmake_minimum_required(VERSION 3.10)
project(ai_resume_builder_helper)

set(CMAKE_CXX_STANDARD 17)

add_executable(ai_resume_builder_helper
    src/main.cpp
    src/resume_builder.cpp
    src/ai_processor.cpp
)

target_include_directories(ai_resume_builder_helper PRIVATE src)
target_link_libraries(ai_resume_builder_helper PRIVATE nlohmann_json)