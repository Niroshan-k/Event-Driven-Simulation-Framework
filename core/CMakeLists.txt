# Create the module using the file in the current (src) directory
pybind11_add_module(simcore main.cpp)

# Link the pybind11 headers found by the root
target_link_libraries(simcore PRIVATE pybind11::module)

# Set output to build/Release for easy testing
set_target_properties(simcore PROPERTIES PREFIX "" SUFFIX ".pyd")