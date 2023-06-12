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
	int length, m, i = 0;
	listint_t *newLinked_list, *temp = *head;

	length = listLength(head);

	newLinked_list = malloc(sizeof(listint_t));
	newLinked_list->next = NULL;
	/* create a reversed copy of original*/
	while (i < length)
	{
		m = temp->n;
		insert_begin(&newLinked_list, m);
		temp = temp->next;
		i++;
	}

	temp = *head;
	/* compare the values of original and reversed copy*/
	while (i < length)
	{
		if (temp->n == newLinked_list->n)
		{
			temp = temp->next;
			newLinked_list = newLinked_list->next;
			i++;
		}
		else
			return (0);
	}
	return (1);
}

/**
 * insert_begin - inserts a node at the beginning.
 * @head: is the beginning of the node provided.
 * @k:is the value to be inserted.
 */
void insert_begin(listint_t **head, int k)
{
	listint_t *newNode = malloc(sizeof(listint_t));

	if (!newNode)
		return;
	newNode->n = k;
	newNode->next = NULL;

	newNode->next = *head;
	*head = newNode;
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
