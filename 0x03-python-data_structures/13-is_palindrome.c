#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/* Function to reverse a linked list */
listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL;
    listint_t *current = head;
    listint_t *next = NULL;

    /* Traverse the list and reverse links */
    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}

/* Function to check if a linked list is a palindrome */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *second_half, *prev_of_slow = NULL;
    int is_palindrome = 1;

    /* Handle edge case: empty list or single node list */
    if (*head == NULL || (*head)->next == NULL)
        return 1;

    /* Find the middle of the list */
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_of_slow = slow;
        slow = slow->next;
    }

    /* If the list has an odd number of elements, move slow one step further */
    second_half = slow;
    prev_of_slow->next = NULL; /* Terminate the first half */
    second_half = reverse_list(second_half); /* Reverse the second half */

    /* Compare the first half and the reversed second half */
    listint_t *first_half = *head;
    while (second_half != NULL)
    {
        if (first_half->n != second_half->n)
        {
            is_palindrome = 0;
            break;
        }
        first_half = first_half->next;
        second_half = second_half->next;
    }

    /* Restore the original list (optional) */
    second_half = reverse_list(second_half);
    if (prev_of_slow != NULL)
        prev_of_slow->next = second_half;

    return is_palindrome;
}
