#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: that is the begining on the linked list
 * @number: is the position to add the node
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;

	listint_t *newnode = malloc(sizeof(listint_t));

	if (newnode == NULL)
		return (NULL);

	newnode->n = number;
	newnode->next = NULL;

	if (!head || !number)
		return (NULL);
	if (*head == NULL)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}

	temp = *head;
	while (temp && temp->n < number)
	{
		temp = temp->next;
	}

	newnode->next = temp->next;
	temp->next = newnode;

	return (newnode);
}
