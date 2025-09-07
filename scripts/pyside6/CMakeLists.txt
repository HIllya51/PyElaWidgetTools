
project(my_wrapper)
cmake_minimum_required(VERSION 3.18)

# Main tuning variables:
set(ELA_INCLUDE_PATH "C:/Users/11737/Documents/GitHub/PyElaWidgetTools/ElaWidgetTools/ElaWidgetTools" CACHE STRING "ELA_INCLUDE_PATH")
set(ELA_LIB_PATH "C:/Users/11737/Documents/GitHub/PyElaWidgetTools/ElaWidgetTools/build/ElaWidgetTools/Release/ElaWidgetTools.lib" CACHE STRING "ELA_LIB_PATH")
set(MY_PYTHON_INSTALL_PATH "C:/Users/11737/AppData/Local/Programs/Python/Python312" CACHE STRING "MY_PYTHON_INSTALL_PATH")
set(MY_QT_INSTALL c:/tmp/6.8.3/msvc2022_64 CACHE STRING "MY_QT_INSTALL")

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_PREFIX_PATH ${MY_QT_INSTALL})
set(CMAKE_BUILD_TYPE Release)
set(MY_SITE_PACKAGES_PATH "${MY_PYTHON_INSTALL_PATH}/Lib/site-packages")

message(STATUS "Python3_ROOT_DIR: ${Python3_ROOT_DIR}")
message(STATUS "Python3_EXECUTABLE: ${Python3_EXECUTABLE}")
message(STATUS "Python3_FIND_REGISTRY: ${Python3_FIND_REGISTRY}")
message(STATUS "PY_BUILD_CMAKE_MODULE_NAME: ${PY_BUILD_CMAKE_MODULE_NAME}")

find_package(Qt6 REQUIRED COMPONENTS Core Widgets)

qt_standard_project_setup()

set(SHIBOKEN_OUTPUT_FOLDER "${CMAKE_CURRENT_BINARY_DIR}/OUTPUTDIR")

# Do not use a GLOB here, to allow for usage as OUTPUT in custom command
file(GLOB SHIBOKEN_GENERATED_SOURCES "${SHIBOKEN_OUTPUT_FOLDER}/ElaWidgetTools/*.cpp" "${SHIBOKEN_OUTPUT_FOLDER}/ElaWidgetTools/*.h")


add_custom_command(
    COMMAND shiboken6 
        --generator-set=shiboken
        --output-directory=OUTPUTDIR
        -I${ELA_INCLUDE_PATH}
        -I${MY_QT_INSTALL}/include -I${MY_QT_INSTALL}/include/QtCore
        --typesystem-paths=${MY_SITE_PACKAGES_PATH}/PySide6/typesystems
        --enable-pyside-extensions
        --avoid-protected-hack
        ${CMAKE_CURRENT_SOURCE_DIR}/wrapper.hpp
        ${CMAKE_CURRENT_SOURCE_DIR}/bindings.xml
    DEPENDS bindings.xml wrapper.hpp
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    OUTPUT ${SHIBOKEN_GENERATED_SOURCES}
    COMMENT "Running shiboken6 generator for bindings.xml"
)

add_library(
    ElaWidgetTools
    SHARED
    wrapper.hpp
    ${SHIBOKEN_GENERATED_SOURCES}
)

# A bit ugly:
# - include paths to python installation
# - include paths to pyside and shiboken6_generator in .venv
target_include_directories(
    ElaWidgetTools
    PRIVATE
    "src"
    "${ELA_INCLUDE_PATH}"
    "${MY_PYTHON_INSTALL_PATH}/include"
    "${MY_SITE_PACKAGES_PATH}/PySide6/include"
    "${MY_SITE_PACKAGES_PATH}/PySide6/include/QtWidgets"
    "${MY_SITE_PACKAGES_PATH}/PySide6/include/QtGui"
    "${MY_SITE_PACKAGES_PATH}/PySide6/include/QtCore"
    "${MY_SITE_PACKAGES_PATH}/PySide6/include/QtPrintSupport"
    "${MY_SITE_PACKAGES_PATH}/shiboken6_generator/include"
)

# Use the python stable ABI3:
# See also https://docs.python.org/3/c-api/stable.html
target_compile_definitions(
    ElaWidgetTools    
    PRIVATE
    "-DPy_LIMITED_API=0x03060000"
)

set_target_properties(
    ElaWidgetTools
    PROPERTIES
    SUFFIX ".pyd"
)

target_link_directories(
    ElaWidgetTools
    PRIVATE
    "${MY_PYTHON_INSTALL_PATH}/libs"
    ${MY_SITE_PACKAGES_PATH}/shiboken6
    ${MY_SITE_PACKAGES_PATH}/PySide6
)

target_link_libraries(
    ElaWidgetTools
    PRIVATE
    Qt6::Widgets
    Qt6::Core
    shiboken6.abi3
    pyside6.abi3
    ${ELA_LIB_PATH}
)

install(
    TARGETS ElaWidgetTools
    DESTINATION ${PY_BUILD_CMAKE_MODULE_NAME}
)
