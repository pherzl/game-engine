cmake_minimum_required(VERSION 3.15)
project(algorithms CXX)

add_library(algorithms src/algorithms.cpp)

find_package(fmt REQUIRED)
target_link_libraries(algorithms PUBLIC fmt::fmt)

find_package(ZLIB)
target_link_libraries(algorithms PUBLIC ZLIB::ZLIB)

target_include_directories(algorithms PUBLIC include)

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/
        DESTINATION include
)

install(TARGETS algorithms)
