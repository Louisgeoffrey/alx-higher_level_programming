#!/usr/bin/python3
a = 89
b 10
a, b = b, a
print("a={:d} - b={:d}".format(a, b))

vi 13-is_palindrome.c

#include "lists.h"

/**
 * reverse_listint - Reverses a linked list
 * @head: Pointer to the first node in the list
 * 
 * Return: Pointer to the first node in the new list
 */
 void reverse_listint(listint_t **head)
 {
         listint_t *prev = NULL;
         listint_t *current = *head;
         listint_t *next = NULL;

         while (current)
         {
             next = current->next;
             current->next = prev;
             prev = current;
             current = next;
        }

         *head = prev;
}

 *head = prev;
 }

 /**
 * is_palindrome - Checks if a linked list is a palindrome
 * @*head: double pointer to the linked list
 *
 Return: 1 if it is, 0 if not
 */
int is palindrome(listint **head)
{
        listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

        if (*head = NULL || (*head)->next = NULL)
        return (1);

        while (1)
        {
            fast = fast->next->next;
            if (!fast)
        {
            dup = slow->next;
            break;
        }
        if (!fast->next)
        {
            if (!fast-next)
        {
            dup = slow-next->next;
            break

