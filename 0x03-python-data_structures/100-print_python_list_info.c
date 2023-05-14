#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	int i = 0;
	PyListObject *casted = (PyListObject *) p;
	int s = Py_SIZE(casted);/*list size*/
	int e = PyList_Size(p);
	PyObject *tempObj;

	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", e);
	while (i < s)
	{
		tempObj = PyList_GET_ITEM(casted, i);
		printf("Element %d: %s\n", i, tempObj->ob_type->tp_name);
		i++;
	}
}
