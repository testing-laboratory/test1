cmake_minimum_required(VERSION 3.2)

include("HunterGate.cmake")

HunterGate(
    URL "https://github.com/cpp-pm/hunter/archive/v0.24.2.tar.gz"
    SHA1 "17fd3b9f0b8c271eac9b71e30a6aa1b9fecab299"
    LOCAL # load cmake/Hunter/config.cmake
)

project(Project1)

hunter_add_package(Boost COMPONENTS system date_time)
message(STATUS "HUNTER_Boost_VERSION: ${HUNTER_Boost_VERSION}")

find_package(Boost COMPONENTS system date_time REQUIRED)
message(STATUS "Boost_VERSION: ${Boost_VERSION}")

add_executable(program1 main.cpp)

target_link_libraries(program1 PRIVATE Boost::boost Boost::system Boost::date_time)
