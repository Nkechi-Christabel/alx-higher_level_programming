#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * push - Push an element onto the stack.
 * @stack: Pointer to the stack (array).
 * @top: Pointer to the top index of the stack.
 * @value: Value to push onto the stack.
 */
void push(int *stack, int *top, int value)
{
	stack[++(*top)] = value;
}

/**
 * pop - Pop an element from the stack.
 * @stack: Pointer to the stack (array).
 * @top: Pointer to the top index of the stack.
 * Return: The popped value.
 */
int pop(int *stack, int *top)
{
	return (stack[(*top)--]);
}

/**
 * is_palindrome - Check if a singly linked list is a palindrome.
 * @head: Pointer to a pointer to the head of the linked list.
 *
 * Return: 1 if it is a palindrome, 0 if it is not.
 */
int is_palindrome(listint_t **head)
{
	int stack[1000], top = -1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head, *fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		push(stack, &top, slow->n);
		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast != NULL)
		slow = slow->next;

	while (slow != NULL)
	{
		if (slow->n != pop(stack, &top))
			return (0);
		slow = slow->next;
	}

	return (1);
}
