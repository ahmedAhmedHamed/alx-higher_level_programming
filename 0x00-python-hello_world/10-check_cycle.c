#include "lists.h"

/**
 * check_cycle - checks if a cycle is in the list
 * @head: the head of the linked list
 * Return: 1 if there is a cycle, 0 if there is not
 */
int check_cycle(listint_t *head)
{
	listint_t *temp;

	if (head != NULL)
		temp = head->next;
	while (temp != NULL)
	{
		if (head == temp)
			return (1);
		temp = temp->next;
	}
	return (0);
}


