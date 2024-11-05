#include <iostream>
#include <fmt/format.h>
#include <algorithms/algorithms.h>

void ai(){
    std::cout << "I am the ai component!\n";
    fmt::println("I am the {} component!", "ai");
    algorithms();
}
