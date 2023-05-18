#include "/usr/include/python3.10/Python.h"
#include "/usr/include/python3.10/listobject.h"
#include "/usr/include/python3.10/object.h"
#include <stdio.h>

void hexPrint(const char *myString, Py_ssize_t size)
{
	Py_ssize_t i = 0;

	while (i < size)
	{
		printf("%02x ", (unsigned char) myString[i]);
		i++;
	}
}

void print_python_bytes(PyObject *p)
{
	Py_ssize_t _size;
	char *s = NULL;
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	_size = PyBytes_GET_SIZE(p);
	s = PyBytes_AS_STRING(p);
	printf("  size: %ld\n", _size);
	if (_size > 10)
		_size = 10;
	else
		_size++;

	printf("  trying string: %s\n", s);

	printf("  first %ld bytes: ", _size);

	hexPrint(s, _size);
	printf("\n");
}

void print_python_list(PyObject *p)
{
	int i = 0;
	const char *bytes = "bytes";
	const char *pointer = NULL;
	PyListObject *casted = (PyListObject *) p;
	Py_ssize_t s = (((PyVarObject *) (casted))->ob_size);/*list size*/
	Py_ssize_t e = PyList_Size(p);
	PyObject *tempObj;

	printf("[*] Python list info");
	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", e);
	while (i < s)
	{
		tempObj = PyList_GET_ITEM(casted, i);
		printf("[*] size of the Python List: %ld\n", e);
		pointer = tempObj->ob_type->tp_name;
		printf("[*] Element : %s\n", pointer);
		if (strcmp(pointer, bytes) == 0)
		{
			Py_ssize_t _size;
			char *s = NULL;
			printf("[.] bytes object info\n");
			if (!PyBytes_Check(tempObj))
			{
				printf("  [ERROR] Invalid Bytes Object\n");
				return;
			}
			_size = PyBytes_GET_SIZE(tempObj);
			s = PyBytes_AS_STRING(tempObj);
			printf("  size: %ld\n", _size);
			if (_size > 10)
				_size = 10;
			else
				_size++;

			printf("  trying string: %s\n", s);

			printf("  first %ld bytes: ", _size);

			hexPrint(s, _size);
			printf("\n");
		}
		i++;
	}
}

