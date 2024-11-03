cmake_minimum_required(VERSION 3.15)
project(network CXX)

add_library(network src/network.cpp)

target_include_directories(network PUBLIC include)

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/
        DESTINATION include
)

install(TARGETS network)
