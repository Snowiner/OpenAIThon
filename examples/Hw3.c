#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node
{
	int data[9];
	struct Node *next;
}Node;

typedef struct queue
{
	Node *front;
	Node *rear;
}Queue;

int IsEmpty(Queue *queue);
void Enqueue(Queue *queue, int data[9]);

void ArrayCopy(int a[9], int b[9]);
int ArrayComp(int a[9], int b[9]);
void ArrayPrint(int a[9]);
void ArraySwap(int array[9], int a, int b);


int QueueCompHead(Queue *queue,int a[9]);
int QueueComp(Node *node, int a[9]);

void QueuePrintHead(Queue *queue);
void QueuePrint(Node *node);


void DFS(Queue *queue, int input[9], int ans[9], int paper[9]);
void SwapLeft(Queue *queue, int input[9], int ans[9], int paper[9]);
void SwapRight(Queue *queue, int input[9], int ans[9], int paper[9]);
void SwapUp(Queue *queue, int input[9], int ans[9], int paper[9]);
void SwapDown(Queue *queue, int input[9], int ans[9], int paper[9]);

int main(void)
{
	int ans[9] = {1,2,3,8,0,4,7,6,5};
	int input[9] = {1, 3, 2, 0, 7, 8, 5, 6, 4};
	int paper[9] = {9,9,9,9,9,9,9,9,9};

	Queue queue;

	(&queue)->front = NULL;

	DFS(&queue,input,ans,paper);

	QueuePrintHead(&queue);
	return 0;
}

void DFS(Queue *queue, int input[9], int ans[9], int paper[9])
{
	
	if(IsEmpty(queue)){}
	else
	{
		if(ArrayComp(queue->rear->data,ans))
		{	printf("Answer Found!");
			return;}
	}
	
	if(QueueCompHead(queue,input))
	{
		printf("\nDepth covered\n");
		return;
	}/*
	else
	if(ArrayComp(queue->rear->data,input))
	{
		return;
	}
	else if(input[0] == ans[0])
		{
			paper[0] = ans[0];
			if(input[1] == ans[1])
			{
				paper[1] = ans[1];
				if(input [2] == ans[2])
				{
					paper[2] = ans[2];
					if(input[5] == ans[5])
					{
						paper[5] = ans[5];
					}
				}
			}
		
		*/




		

		ArrayPrint(input);
		ArrayPrint(paper);
		Enqueue(queue,input);

		SwapUp(queue,input,ans,paper);
		SwapLeft(queue,input,ans,paper);
		SwapDown(queue,input,ans,paper);
		SwapRight(queue,input,ans,paper);
	/*}*/
}

void ArraySwap(int array[9], int a, int b)
{
	int temp = array[a];
	array[a] = array[b];
	array[b] = temp;
}

void SwapLeft(Queue *queue, int input[9], int ans[9],int paper[9])
{
	int newInput[9];
	ArrayCopy(newInput,input);

	int pos=0;
	for(int i=0; i<9; i++)
	{
		if(newInput[i] == 0)
			break;
		else
		{
			pos++;
		}
	}

	if(pos%3 != 0)
	{
		if(paper[pos-1] == 9)
		{
			ArraySwap(newInput,pos,pos-1);
			DFS(queue,newInput,ans,paper);
		}
		else
			return;
	}

}
void SwapRight(Queue *queue, int input[9], int ans[9], int paper[9])
{
	int newInput[9];
	ArrayCopy(newInput,input);

	int pos=0;
	for(int i=0; i<9; i++)
	{
		if(newInput[i] == 0)
			break;
		else
		{
			pos++;
		}
	}

	if(pos%3 != 2)
	{
		if(paper[pos+1] == 9)
		{
			ArraySwap(newInput,pos,pos+1);
			DFS(queue,newInput,ans,paper);
		}
		else
			return;
	}
}
void SwapUp(Queue *queue, int input[9], int ans[9],int paper[9])
{
	int newInput[9];
	ArrayCopy(newInput,input);

	int pos=0;
	for(int i=0; i<9; i++)
	{
		if(newInput[i] == 0)
			break;
		else
		{
			pos++;
		}
	}

	if(pos/3 != 0)
	{
		if(paper[pos-3] == 9)
		{
			ArraySwap(newInput,pos,pos-3);
			DFS(queue,newInput,ans,paper);
		}
		else
			return;
	}
}
void SwapDown(Queue *queue, int input[9], int ans[9], int paper[9])
{
	int newInput[9];
	ArrayCopy(newInput,input);

	int pos=0;
	for(int i=0; i<9; i++)
	{
		if(newInput[i] == 0)
			break;
		else
		{
			pos++;
		}
	}

	if(pos/3 != 2)
	{
		if(paper[pos+3] == 9)
		{
			ArraySwap(newInput,pos,pos+3);
			DFS(queue,newInput,ans,paper);
		}
		else
			return;
	}
}

int IsEmpty(Queue *queue)
{
	if(queue->front == NULL)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

void Enqueue(Queue *queue, int data[9])
{
	Node *now = (Node*)malloc(sizeof(Node));
	ArrayCopy(now->data,data);
	now->next = NULL;

	if(IsEmpty(queue))
	{
		queue->front = now;
		//printf("\nenqueue in new");
	}
	else
	{
		//printf("\nenqueue in old");
		queue -> rear -> next = now;
	}
	queue -> rear = now;

	//printf("\nenqueue done");
}



void ArrayCopy(int a[9], int b[9])
{
	for(int i = 0; i<9; i++)
	{
		a[i] = b[i];
	}
}

int ArrayComp(int a[9], int b[9])
{
	for(int i = 0; i<9; i++)
	{
		if(a[i] != b[i])
			return 0;
	}
	return 1;
}

void ArrayPrint(int a[9])
{
	for(int i = 0; i<9; i++)
	{
		if(i%3 == 0)
			printf("\n");
		printf("%d",a[i]);

	}
	printf("\n");
}

int QueueCompHead(Queue *queue,int a[9])
{
	if(IsEmpty(queue))
	{
		printf("\nQueue Empty\n");
		return 0;
	}
	else
	{
		return QueueComp(queue->front,a);
	}
}

int QueueComp(Node *node, int a[9])
{
	if(node->data != NULL)
	{
		if(ArrayComp(node->data, a))
		{
			return 1;
		}
		else
		{
			if(node->next != NULL)
			{
				return QueueComp(node->next,a);
			}
			else
			{
				return 0;
			}
		}
	}
	else
	{
		printf("\nNode Data Empty Error\n");
		return 0;
	}
}

void QueuePrintHead(Queue *queue)
{
	if(IsEmpty(queue))
	{
		printf("\nQueue Empty Error\n");
		return ;
	}
	else
	{
		QueuePrint(queue->front);
	}
}

void QueuePrint(Node *node)
{
	if(node->data != NULL)
	{
		ArrayPrint(node->data);
		
		if(node->next != NULL)
		{
			QueuePrint(node->next);
		}
		else
		{
			return;
		}
	}
	else
	{
		printf("\nNode Data Empty Error\n");
		return ;
	}

}