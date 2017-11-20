project(cmake_wrapper)

include(conanbuildinfo.cmake)
conan_basic_setup()

add_library(http_parser sources/http_parser.c)

# Defined in original build system https://github.com/nodejs/http-parser/blob/master/Makefile
option(HTTP_PARSER_STRICT "Use strict HTTP parser")
if(HTTP_PARSER_STRICT)
    target_compile_definitions(http_parser PRIVATE HTTP_PARSER_STRICT=1)
else()
    target_compile_definitions(http_parser PRIVATE HTTP_PARSER_STRICT=0)
endif()
