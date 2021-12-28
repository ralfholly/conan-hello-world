cmake_minimum_required(VERSION 3.18)
project(wheel-rotation VERSION 1.0 LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra")
set(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/helperScripts/cmake/modules)
include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

set(TARGET conan-hello-world)

add_executable(${TARGET}
    ${TARGET}.cpp
)

target_link_libraries(${TARGET}
    # CONAN_PKG::benchmark
)
