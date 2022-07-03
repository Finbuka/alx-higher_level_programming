#include <stddef.h>
#include "lists.h"

/**
 * is_palindrome - checks the list for palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 on True 0 on False
 */
int is_palindrome(listint_t **head)
{
	size_t length = get_list_num(*head);
	size_t store_half[length];
	int i = 0;
	listint_t *h;

	if (*head == NULL)
		return (1);
	if (length % 2 != 0)
		return (0);
	length = (length / 2) - 1;
	while (h)
	{
		if (i <= length)
			store_half[i] = h->n;
		else if (store_half[length--] != h->n)
			return (0);
		h = h->next;
	}
	return (1);

}

/**
 * get_list_num - gets the number of all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t get_list_num(const listint_t *h)
{
	const listint_t *curr;
	unsigned int n;

	curr = h;
	n = 0;
	while (curr != NULL)
	{
		curr = curr->next;
		n++;
	}

	return (n);
}
