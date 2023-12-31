#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 *
 * @head: pointer to pointer of first node of listint_t list.
 * @number: integer to be included in new node.
 *
 * Return: address of the new node or NULL if it fails.
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node = NULL;
    listint_t *current = NULL;

    if (!head)
        return (NULL);

    new_node = malloc(sizeof(listint_t));
    if (!new_node)
        return (NULL);

    new_node->n = number;

    if (!*head)
    {
        new_node->next = NULL;
        *head = new_node;
        return (new_node);
    }

    current = *head;

    if (current->n > number)
    {
        new_node->next = current;
        *head = new_node;
        return (new_node);
    }

    while (current->next)
    {
        if (current->next->n > number)
        {
            new_node->next = current->next;
            current->next = new_node;
            return (new_node);
        }
        current = current->next;
    }

    new_node->next = NULL;
    current->next = new_node;

    return (new_node);
}