#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stddef.h>

static PyObject *
matrix_multiply(PyObject *m1, PyObject *m2)
{
	Py_ssize_t i, j, k, n;
	double sum;
	PyObject *result, *row, *item;

	n = PyList_Size(m1);
	if (n == 0 || n != PyList_Size(m2)) {
		return NULL;
	}

	result = PyList_New(n);
	if (!result) {
		return NULL;
	}

	for (i = 0; i < n; i++) {
		row = PyList_New(n);
		if (!row) {
			return NULL;
		}

		for (j = 0; j < n; j++) {
			sum = 0.0;
			for (k = 0; k < n; k++) {
				double a = PyFloat_AsDouble(PyList_GetItem(
					PyList_GetItem(m1, i), k));
				double b = PyFloat_AsDouble(PyList_GetItem(
					PyList_GetItem(m2, k), j));
				sum += a * b;
			}
			item = PyFloat_FromDouble(sum);
			if (!item) {
				return NULL;
			}

			PyList_SetItem(row, j, item);
		}
		PyList_SetItem(result, i, row);
	}
	return result;
}

static PyObject *
create_identity_matrix(Py_ssize_t n)
{
	Py_ssize_t i, j;
	PyObject *identity, *row, *item;

	identity = PyList_New(n);
	if (!identity) {
		return NULL;
	}

	for (i = 0; i < n; i++) {
		row = PyList_New(n);
		if (!row) {
			return NULL;
		}

		for (j = 0; j < n; j++) {
			item = PyFloat_FromDouble(i == j ? 1.0 : 0.0);
			if (!item) {
				return NULL;
			}

			PyList_SetItem(row, j, item);
		}
		PyList_SetItem(identity, i, row);
	}
	return identity;
}

static PyObject *
foreign_matrix_power(PyObject *self, PyObject *args)
{
	PyObject *matrix, *result, *temp;
	Py_ssize_t n, exp, i;

	if (!PyArg_ParseTuple(args, "O!n", &PyList_Type, &matrix, &exp)) {
		return NULL;
	}

	n = PyList_Size(matrix);
	result = create_identity_matrix(n);
	if (!result) {
		return NULL;
	}

	for (i = 0; i < exp; i++) {
		temp = matrix_multiply(result, matrix);
		Py_DECREF(result);
		if (!temp) {
			return NULL;
		}

		result = temp;
	}
	return result;
}

static PyMethodDef Methods[] = { { "foreign_matrix_power", foreign_matrix_power,
	                           METH_VARARGS, "Raise a matrix to a power" },
	                         { NULL, NULL, 0, NULL } };

static struct PyModuleDef module = { PyModuleDef_HEAD_INIT, "foreign", NULL, -1,
	                             Methods };

PyMODINIT_FUNC
PyInit_foreign(void)
{
	return PyModule_Create(&module);
}
