#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: the head of the linked list.
 * @number: the number that is insert.
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *c = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (*head);
	new->n = number;
	if (c == NULL)
	{
		new->next = c;
		c = new;
		return (c);
	}
	while (c->next != NULL && c->next->n < number)
	{
		c = c->next;
	}
	new->next = c->next;
	c->next = new;
	return (c);
}
