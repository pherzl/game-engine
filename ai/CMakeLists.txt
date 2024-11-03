cmake_minimum_required(VERSION 3.15)
project(ai CXX)

add_library(ai src/ai.cpp)

target_include_directories(ai PUBLIC include)
target_link_libraries(ai algorithms)
install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/
        DESTINATION include
)

install(TARGETS ai)
