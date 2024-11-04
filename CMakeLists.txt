cmake_minimum_required(VERSION 3.15)
project(game-engine CXX)
set(CMAKE_CXX_STANDARD 20)

# Set the install prefix
set(CMAKE_INSTALL_PREFIX "${CMAKE_BINARY_DIR}/install")

add_subdirectory(network)
add_subdirectory(algorithms)
add_subdirectory(ai)
add_subdirectory(rendering)
