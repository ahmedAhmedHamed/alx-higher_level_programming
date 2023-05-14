#include "lists.h"

int wrapper(listint_t *head, listint_t *headTwo, int depth) {
    listint_t *p1;
    int reverseDepth;

    if (headTwo != NULL && headTwo->next == NULL) {
        if (head->n == headTwo->n)
        {
            return (1);
        }
        return (-1);
    }
    if (headTwo != NULL)
        p1 = headTwo->next;
    else if (headTwo == NULL)
        p1 = head->next;

    else {

        reverseDepth = wrapper(head, p1, depth + 1);
        if (reverseDepth == -1)
            return (-1);
        if (reverseDepth == -5)
            return (-5);
        if (reverseDepth <= depth)
            return (-5);
        while (head != NULL && reverseDepth--)
            head = head->next;
        if (head->n != headTwo->n)
            return (-1);

        return (1 + reverseDepth);
    }
}

int is_palindrome(listint_t **head)
{
    if (head == NULL || *head == NULL || (*head)->next == NULL)
        return (1);
    if (wrapper(*head, NULL, 0) != -1)
        return (1);
    return (0);
}