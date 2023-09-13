#include <Python.h>

void print_python_list(PyObject *p) {
    PyObject *item;
    Py_ssize_t size, i;

    if (!PyList_Check(p)) {
        fprintf(stderr, "Invalid PyListObject\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *bytes;

    if (!PyBytes_Check(p)) {
        fprintf(stderr, "Invalid PyBytesObject\n");
        return;
    }

    size = PyBytes_Size(p);
    bytes = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", bytes);

    printf("  first 10 bytes:");
    for (i = 0; i < size && i < 10; i++) {
        printf(" %02x", bytes[i] & 0xff);
    }
    printf("\n");
}

