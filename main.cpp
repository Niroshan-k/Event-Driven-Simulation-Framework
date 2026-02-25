#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

namespace py = pybind11;

// check the high performance
double batch_process(py::array_t<double> prices, py::array_t<int> quantities) {
    py::buffer_info price_buf = prices.request();
    py::buffer_info quant_buf = quantities.request();

    double *p_ptr = static_cast<double *>(price_buf.ptr);
    int *q_ptr = static_cast<int *>(quant_buf.ptr);
    size_t n = price_buf.size;

    double total = 0;
    for (size_t i = 0; i < n; i++) {
        total += p_ptr[i] * q_ptr[i];
    }
    return total;
}

PYBIND11_MODULE(simcore, m) {
    m.def("batch_process", &batch_process, "Processes 1M+ rows with zero-copy");
}