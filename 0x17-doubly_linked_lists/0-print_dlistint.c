#include <stdio.h>
#include "lists.h"
/**
 * print_dlistint - prints all the elements of a dlistint_t list.
 * @h: head of the linked list.
 * Return: the number of nodes.
 */
size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *node = h;
	int i = 0;

	if (h == NULL)
		return (0);
	while (node != NULL)
	{
		printf("%d\n", node->n);
		node = node->next;
		i++;
	}
	return (i);
}
