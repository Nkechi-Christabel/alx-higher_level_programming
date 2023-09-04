#include "lists.h"

/**
 * check_cycle - Check if a singly linked list has a cycle.
 * @list: Pointer to the head of the linked list.
 *
 * Return: 1 if there is a cycle, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *one_step, *two_steps;

	if (list == NULL || list->next == NULL)
		return (0);

	one_step = list;
	two_steps = list;

	while (two_steps != NULL && two_steps->next != NULL)
	{
		one_step = one_step->next;
		two_steps = two_steps->next->next;

		if (one_step == two_steps)
			return (1);
	}

    return (0);
}

