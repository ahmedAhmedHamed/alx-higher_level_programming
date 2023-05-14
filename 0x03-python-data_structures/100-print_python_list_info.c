#include "/usr/include/python3.10/Python.h"
#include "/usr/include/python3.10/listobject.h"
#include "/usr/include/python3.10/object.h"
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	int i = 0;
	int s = Py_SIZE(p);/*list size*/
	int e = PyList_Size(p);
	PyObject *tempObj;

	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", e);
	while (i < s)
	{
		tempObj = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, tempObj->ob_type->tp_name);
		i++;
	}
}

int main (void)
{

    return (0);
}
