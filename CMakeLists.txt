cmake_minimum_required(VERSION 3.12)
project(SME_Simulator)

# Find Python first
find_package(Python COMPONENTS Interpreter Development REQUIRED)

# Manually point to the pybind11 folder
# Replace THE_PATH_BELOW with the "Location" you got from 'pip show pybind11'
# IMPORTANT: Use forward slashes / even on Windows!
set(pybind11_DIR "C:/Users/laksh/AppData/Roaming/Python/Python312/site-packages/pybind11/share/cmake/pybind11")

find_package(pybind11 REQUIRED)

pybind11_add_module(simcore main.cpp)


