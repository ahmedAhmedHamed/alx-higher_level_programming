#include "lists.h"

/**
 * check_cycle - checks if a cycle is in the list
 * @head: the head of the linked list
 * Return: 1 if there is a cycle, 0 if there is not
 */
int check_cycle(listint_t *head)
{
	int i = 0;
	int j;
	listint_t *list[1000];
	while (head != NULL)
	{
		list[i] = head;
		for (j = 0; j < i; j++)
			if (head == list[j])
				return (1);
		i++;
		head = head->next;
	}
	return (0);
}


