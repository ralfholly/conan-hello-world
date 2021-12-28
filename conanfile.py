from conans import ConanFile, CMake, tools, errors
import os

class ConanHelloWorld(ConanFile):
    name = "conan-hello-world"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def requirements(self):
        pass
        # self.requires("benchmark/1.5.2")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
