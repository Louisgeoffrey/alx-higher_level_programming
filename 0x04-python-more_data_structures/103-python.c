#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - This prints bytes information
 * @p: Python object
 *
 * Return: No return
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, i, limit;

	printf("[.] bytes object info\n");
	if (!pyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((pyVarObject *)(p))->ob_size;
	string = ((pyBytesObject *)p)->ob_sval;

	printf(" size: %ld\n", size);
	printf(" trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf(" first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
		if (string[i] >= 0)
			printf(" %02x", string[i]);
		else
			printf(" %02x", 256 + string[i]);

	printf("\n");
}

/**
 * print_python_list - This prints the list information
 * @p: Python Object
 *
 * Return: No return
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PylistObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PylistObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python list = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PylistObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
