#include <Python.h>

void print_python_list(PyObject *p) {
    // Check if the object is a valid PyListObject.
    if (!PyList_Check(p)) {
        printf("Not a valid PyListObject.\n");
        return;
    }

    // Get the size of the list.
    int size = PyList_Size(p);

    // Print the list information.
    printf("List size: %d\n", size);
    printf("List items:\n");
    for (int i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        printf("  * %s\n", PyUnicode_AsUTF8(item));
    }
}

void print_python_bytes(PyObject *p) {
    // Check if the object is a valid PyBytesObject.
    if (!PyBytes_Check(p)) {
        printf("Not a valid PyBytesObject.\n");
        return;
    }

    // Get the size of the bytes object.
    int size = PyBytes_GET_SIZE(p);

    // Print the bytes object information.
    printf("Bytes size: %d\n", size);
    printf("First %d bytes: ", 10);
    for (int i = 0; i < 10 && i < size; i++) {
        printf("%02x ", PyBytes_AS_STRING(p)[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    // Check if the object is a valid PyFloatObject.
    if (!PyFloat_Check(p)) {
        printf("Not a valid PyFloatObject.\n");
        return;
    }

    // Get the value of the float object.
    double value = PyFloat_AS_DOUBLE(p);

    // Print the float object information.
    printf("Float value: %g\n", value);
}

