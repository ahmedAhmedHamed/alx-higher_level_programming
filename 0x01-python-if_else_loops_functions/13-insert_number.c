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

	while (temp != NULL)
		temp = (temp)->next;
	temp = newList;
	temp->n = number;

	return (temp);
}
