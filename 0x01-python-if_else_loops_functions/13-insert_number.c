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

	while (temp->next != NULL)
	{
		if (temp->next->n > number)
			break;
		temp = (temp)->next;
	}

	newList->next = temp->next;

	temp->next = newList;
	temp->next->n = number;

	return (temp->next);
}
