#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p);
/**
 * print_python_list_info -  prints some basic info about Python lists.
 *
 * @p: Python list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size = PyList_Size(p);

	if (PyList_Check(p))
	{
		printf("[*] Size of the Python List = %ld\n", list_size);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

		for (Py_ssize_t i = 0; i < list_size; i++)
		{
			PyObject *item = PyList_GetItem(p, i);
			printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		}
	}
	else
	{
		printf("  [ERROR] Invalid List Object\n");
	}
}
