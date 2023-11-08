#include <python.h>

/**
 * print_python_list_info - This prints basic info about python lists.
 * @p: PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	pyObject *obj;

	size = py_SIZE(p);
	alloc = ((pyListobject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = Pylist_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
