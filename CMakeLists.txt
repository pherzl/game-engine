cmake_minimum_required(VERSION 3.15)
project(game-engine CXX)

# Set the install prefix
set(CMAKE_INSTALL_PREFIX "${CMAKE_BINARY_DIR}/install")

add_subdirectory(network)
add_subdirectory(algorithms)
add_subdirectory(ai)
add_subdirectory(rendering)
