#ifndef HEADERS_H
#define HEADERS_H
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>
#include <string.h>

/**
 * struct friend_s - singly linked list of friends
 * @name: string
 * @phone: phone number of friend
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct friend_s
{
	char *name;
	int phone;
	struct friend_s *next;
} friend_t;

void print_friends(const friend_t *h);
friend_t *add_worst_friend(friend_t **head, char *name, int phonenum);
void ruin_friendships(friend_t *head);

#endif