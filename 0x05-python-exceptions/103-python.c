#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "Invalid PyListObject\n");
        return;
    }

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", ((PyVarObject *)p)->ob_size);

    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < ((PyVarObject *)p)->ob_size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "Invalid PyBytesObject\n");
        return;
    }

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", ((PyVarObject *)p)->ob_size);
    printf("  trying string: %s\n", PyBytes_AS_STRING(p));
    printf("  first %zd bytes: ", ((PyVarObject *)p)->ob_size < 10 ? ((PyVarObject *)p)->ob_size : 10);
    for (Py_ssize_t i = 0; i < ((PyVarObject *)p)->ob_size && i < 10; i++) {
        printf("%02x", (unsigned char)PyBytes_AS_STRING(p)[i]);
        if (i < 9 && i < ((PyVarObject *)p)->ob_size - 1)
            printf(" ");
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "Invalid PyFloatObject\n");
        return;
    }

    printf("[.] float object info\n");
    printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}


