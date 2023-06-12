#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * is_palindrome - checks if the single linked list is palindrome
 * @head:  is the begining single linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	/* Findd the length of linked list */
	int length, i = 0;
	listint_t *rev, *temp = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	length = listLength(head);

	for (; i < (length - 1) / 2; i++)
		temp = temp->next;

	if ((length % 2) == 0 && temp->n != temp->next->n)
		return (0);
	temp = temp->next->next;

	/* create a reversed copy of original*/
	rev = reverse(&temp);

	temp = *head;
	/* compare the values of original and reversed copy*/
	while (rev)
	{
		if (temp->n == rev->n)
		{
			temp = temp->next;
			rev = rev->next;
		}
		else
			return (0);
	}
	reverse(&rev);

	return (1);
}

/**
 * reverse - reverses a linked list
 * @head: is the beginning of the node provided.
 *
 * Return: reveresed linked list
 */
listint_t *reverse(listint_t **head)
{
	listint_t *prev = NULL, *next, *node = *head;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;

	return (*head);
}

/**
 * listLength - finds the length of t linked list
 * @head: is the begining of the node
 *
 * Return:  the length of the linked list
 */
int listLength(listint_t **head)
{
	listint_t *temp = *head;
	int len = 0;

	while (temp)
	{
		len++;
		temp = temp->next;
	}

	return (len);
}
