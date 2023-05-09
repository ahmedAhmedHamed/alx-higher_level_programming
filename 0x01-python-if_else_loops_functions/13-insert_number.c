#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newList = malloc(sizeof(listint_t *));
	listint_t *temp = *head;

	if (head == NULL || newList == NULL)
	{
		free(newList);
		return (NULL);
	}
	newList->next = NULL;
	newList->n = number;
	if (*head == NULL)
	{
		*head = newList;
		return (newList);
	}

	while (temp->next != NULL)
	{
		if (temp->next->n > number)
			break;
		temp = (temp)->next;
	}
	if (temp != *head)
	{
		newList->next = temp->next;
		temp->next = newList;
		return (temp->next);
	}
	else
	{
		newList->next = *head;
		*head = newList;
		return (newList);
	}
}
