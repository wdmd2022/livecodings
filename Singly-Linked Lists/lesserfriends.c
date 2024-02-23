#include "headers.h"

/**
 * add_worst_friend - add a new node at the end of a friend_t list
 *
 * @head: double pointer to the head of the list
 * @name: string, value for the new node
 * @phone: int, phone number for new node
 *
 * Return: the address of the new element, or NULL if failed
 */
friend_t *add_worst_friend(friend_t **head, char *name, int phonenum)
{
	friend_t *oldworst;
	friend_t *newworst;

	newworst = malloc(sizeof(friend_t));
	if (!newworst)
	{
		return (NULL);
	}
	newworst->name = strdup(name);
	newworst->phone = phonenum;
	newworst->next = NULL;
	if (*head == NULL)
	{
		*head = newworst;
		return (newworst);
	}
	oldworst = *head;
	while (oldworst->next != NULL)
	{
		oldworst = oldworst->next;
	}
	oldworst->next = newworst;
	return (newworst);
}