from conans import ConanFile, CMake, tools, errors
import os

class ConanHelloWorld(ConanFile):
    version = "0.0.1"
    name = "conan-hello-world"

    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = ["CMakeLists.txt", "*.cpp", "*.h"]

    def requirements(self):
        pass
        # self.requires("benchmark/1.5.2")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
