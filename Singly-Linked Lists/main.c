#include "headers.h"

int main(void)
{
    friend_t *head;
    friend_t *newbestie;
    friend_t bob = {"Bob", 8675309, NULL};

    head = &bob;
    newbestie = malloc(sizeof(friend_t));
    if (newbestie == NULL)
    {
        printf("Worst malloc ever\n");
        return (1);
    }
    newbestie->name = "Tony";
    newbestie->phone = 5552211;
    newbestie->next = head;
    head = newbestie;
    print_friends(head);
    return;
}