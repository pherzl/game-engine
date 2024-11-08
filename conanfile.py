from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class game_engineRecipe(ConanFile):
    name = "game-engine"
    version = "1.0"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    generators = "CMakeDeps"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*", "network/*", "algorithms/*", "ai/*", "rendering/*"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.user_presets_path = False
        tc.generate()

    def requirements(self):
        requirements = self.conan_data.get('requirements', [])
        for requirement in requirements:
            self.requires(requirement)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.components["algorithms"].libs = ["algorithms"]
        self.cpp_info.components["algorithms"].set_property("cmake_target_name", "game-engine::algorithms")
        self.cpp_info.components["algorithms"].requires = ["fmt::fmt", "zlib::zlib"]

        self.cpp_info.components["network"].libs = ["network"]
        self.cpp_info.components["network"].set_property("cmake_target_name", "game-engine::network")

        self.cpp_info.components["ai"].libs = ["ai"]
        self.cpp_info.components["ai"].requires = ["algorithms"]
        self.cpp_info.components["ai"].set_property("cmake_target_name", "game-engine::ai")

        self.cpp_info.components["rendering"].libs = ["rendering"]
        self.cpp_info.components["rendering"].requires = ["algorithms"]
        self.cpp_info.components["rendering"].set_property("cmake_target_name", "game-engine::rendering")
