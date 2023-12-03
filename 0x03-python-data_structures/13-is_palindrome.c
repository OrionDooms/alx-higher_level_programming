#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head of a linked list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow, *A_Half, *B_Half;

	if (*head == NULL)
		return (0);
	fast = *head;
	slow = *head;
	A_Half = *head;
	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	B_Half = rev_list(slow->next);
	while (B_Half != NULL)
	{
		if (A_Half->n != B_Half->n)
			return (0);
		A_Half = A_Half->next;
		B_Half = B_Half->next;
	}
	return (1);
}
/**
 * rev_list - reverse the linked list.
 * @head: head of a linked list.
 * Return: the listed list in reverse.
 */
listint_t *rev_list(listint_t *head)
{
	listint_t *prev = NULL, *nxt = NULL, *current = head;

	while (current != NULL)
	{
		nxt = current->next;
		current->next = prev;
		prev = current;
		current = nxt;
	}
	return (prev);
}
