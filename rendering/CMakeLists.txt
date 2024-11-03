cmake_minimum_required(VERSION 3.15)
project(rendering CXX)

add_library(rendering src/rendering.cpp)

target_include_directories(rendering PUBLIC include)
target_link_libraries(rendering algorithms)
install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/
        DESTINATION include
)

install(TARGETS rendering)
