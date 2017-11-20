#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class HttpParserConan(ConanFile):
    name = "http_parser"
    version = "2.7.1"
    year = "2017"
    url = "https://github.com/bincrafters/conan-http-parser"
    description = "Keep it short"
    license = "https://github.com/nodejs/http-parser/blob/master/LICENSE-MIT"
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake"
    exports = ["CMakeLists.txt"]
    options = {"shared": [True, False], "strict": [True, False]}
    default_options = "shared=False", "strict=False"

    def source(self):
        source_url = "https://github.com/nodejs/http-parser"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name.replace("_", "-") + "-" + self.version
        os.rename(extracted_dir, "sources")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["HTTP_PARSER_STRICT"] = self.options.strict
        cmake.configure()
        cmake.build()

    def package(self):
        with tools.chdir("sources"):
            self.copy(pattern="LICENSE")
            self.copy(pattern="*", dst="include", src="sources")
            self.copy(pattern="*.dll", dst="bin", src="bin", keep_path=False)
            self.copy(pattern="*.lib", dst="lib", src="lib", keep_path=False)
            self.copy(pattern="*.a", dst="lib", src="lib", keep_path=False)
            self.copy(pattern="*.so*", dst="lib", src="lib", keep_path=False)
            self.copy(pattern="*.dylib", dst="lib", src="lib", keep_path=False)
            self.copy(pattern="*.pdb", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
