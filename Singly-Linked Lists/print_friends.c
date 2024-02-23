#include "headers.h"

/**
 * print_friends - prints all the elements of a list_t list
 *
 * @h: pointer to the head of the list
 *
 * Return: nothing
 */
void print_friends(const friend_t *h)
{
	while (h != NULL)
	{
		printf("friend: %s - phone: %d\n", h->name, h->phone);
		h = h->next;
	}
	return;
}