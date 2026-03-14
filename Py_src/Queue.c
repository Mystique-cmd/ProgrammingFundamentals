#include <stdio.h> // allows input and output operations
#define SIZE 5     // define the maximum size of the queue
// This program implements a simple queue using an array in C.
// It allows enqueueing and dequeueing of elements, and displays the queue contents.
// The queue is implemented using a struct that contains an array, front, and rear indices.

struct Queue
{
    int items[SIZE]; // Array to hold the queue elements
    // front points to the first element in the queue
    // rear points to the last element in the queue
    int front;
    int rear;
};

void enqueue(struct Queue *q, int value)
{ // Function to add an element to the queue
    // Check if the queue is full
    if (q->rear == SIZE - 1)
    {
        printf("Queue is full\n");
    }
    else
    { // If not full, add the element
        if (q->front == -1)
        {
            q->front = 0; // Initialize front if it is the first element being added
        }
        q->rear++;                 // Increment rear to point to the next position
        q->items[q->rear] = value; //    Add the new element to the queue
    }
}
int dequeue(struct Queue *q)
{   //    Function to remove an element from the queue
    // Check if the queue is empty
    // If front is -1 or front is greater than rear, the queue is empty
    // Return -1 to indicate an error
    // If the queue is empty, return -1
    // If the queue is not empty, remove the element at the front
    // and adjust the front index accordingly
    if (q->front == -1 || q->front > q->rear)
    {
        printf("Queue is empty\n");
        return -1; // Indicate error
    }
    int item = q->items[q->front];
    q->front++;
    if (q->front > q->rear)
    {
        // Reset the queue after last element is dequeued
        q->front = -1;
        q->rear = -1;
    }
    return item;
}
void display(struct Queue q)
{   // Function to display the elements in the queue
    // Check if the queue is empty
    // If the queue is empty, print a message
    // If the queue is not empty, print all elements from front to rear
    // If front is -1 or front is greater than rear, the queue is empty
    // Print the elements in the queue
    if (q.front == -1 || q.front > q.rear)
    {
        printf("Queue is empty\n");
        return;
    }
    printf("Queue elements: ");
    for (int i = q.front; i <= q.rear; i++)
    {
        printf("%d ", q.items[i]);
    }
    printf("\n");
}
int main()
{ // Main function to demonstrate the queue operations
    // Declare and initialize a queue
    // Create a queue with front and rear initialized to -1
    // This indicates that the queue is empty initially
    printf("Queue Implementation in C\n");
    printf("Maximum size of the queue: %d\n", SIZE);
    struct Queue q = {.front = -1, .rear = -1};
    // Initialize the queue
    printf("Enter the elements to enqueue:\n");
    for (int i = 0; i < SIZE; i++)
    {
        int value;
        printf("Element %d: ", i + 1);
        scanf("%d", &value);
        enqueue(&q, value);
    }
    display(q);
    // Dequeue elements
    printf("Dequeueing elements:\n");
    for (int i = 0; i < SIZE; i++)
    {
        int item = dequeue(&q);
        if (item != -1)
        {
            printf("Dequeued: %d\n", item);
        }
    }
    display(q);
    // Attempt to dequeue from an empty queue
    printf("Attempting to dequeue from an empty queue:\n");
    int item = dequeue(&q);
    if (item == -1)
    {
        printf("No items to dequeue.\n");
    }
    // Final display of the queue
    display(q);
    return 0;
}