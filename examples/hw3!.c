#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define IDEAL 123456789

//only minor math functions(not important)
int getDigit(int a,int n);
int square(int a);
int power(int a,int n);

// only minor graph search and move functions (not important)
int search9(int a);	//searches where 9 is.
int swap(int input,int a);	//swaps values

// random dice roller
int decision(int a);

// target graph evaluater
int evaluate(int a);

	int map[9][4] = {
		{1, 3, 5, 7},
		{0, 2, 8, 9},
		{1, 3, 9, 9},
		{0, 2, 4, 9},
		{3, 5, 9, 9},
		{0, 4, 6, 9},
		{5, 7, 9, 9},
		{0, 8, 6, 9},
		{1, 7, 9, 9}
	};

	int global_dice = 11;

int main(void)
{
	int input = 756289134;
	int start_value = input;
	time_t seconds = clock();

	while(input != IDEAL)
	{
		
		input = decision(input);
		//printf("\n%d %d %d",input,search9(input),map[search9(input)][0]);
	}

	printf("\n%d milliseconds spent",clock()-seconds);
	printf("\nDONE : %d (from %d)",input,start_value);

	return 0;
}

int decision(int a)
{
	srand(time(NULL));
	int dice = 0;
	int dice_total = 0;
	int next = 987654321;
	int random = square((rand()*global_dice)%1777);	// just to make sure random work
	printf("\n%d",a);

	// let random not to go minus value or overflow
	if(global_dice<10000 || global_dice>10)
	{
		global_dice++;
	}
	else
	{
		global_dice--;
	}
	

	for(int i=0; i<4; i++)
	{
		if(map[search9(a)][i] >8)
		{

		}
		else
		{
			dice += evaluate(swap(a,map[search9(a)][i]));
		}
	}

	dice_total = dice;

	for(int i = 0; i<4; i++)
	{
		if(map[search9(a)][i] >8)
		{

		}
		else
		{
			if( random%dice < evaluate(swap(a,map[search9(a)][i])))
			{
				printf(" %d %d %d", random%dice ,dice_total,evaluate(swap(a,map[search9(a)][i])));
				// to see how random works
				return swap(a,map[search9(a)][i]);
			}
			else
			{
				dice -= evaluate(swap(a,map[search9(a)][i]));
			}
		}
	}

	return next;	// insurance(never happens in usual)
}

int swap(int input,int a)
{
	if(a>8)
	{
		return power(10,10);
	}
	else
	{
		int result = input;
		result += power(10,a)*9;
		result += power(10,search9(input))*getDigit(input,a);
		result -= power(10,a)*getDigit(input,a);
		result -= power(10,search9(input))*9;
		

		return result;
	}
}

int search9(int a)
{
	int digit = 0;
	while(getDigit(a,digit) != 9)
	{
		digit++;
	}

	return digit;
}
int square(int a)
{
	return a*a;
}
int power(int a,int n)
{
	int result=1;
	for(int i=0; i<n; i++)
	{
		result = result*a;
	}

	return result;
}

int getDigit(int a, int n)
{
	for(int i=0; i<n; i++)
	{
		a = a/10;
	}

	return a%10;
}
int evaluate(int a)
{
	int controller = 0;
	int value = 0;
	for(int i = 0; i<9; i++)
	{
		if(getDigit(a,i) == getDigit(IDEAL,i))
		{
			value += 1000;
			// give high value to correct match
		}
		else
		{
			if(i%2 == 1)
			{
				controller =2;	// giving value to sides 
			}
			else if(i == 8)
			{
				controller = 4;	// giving value to center
			}
			else
			{
				controller = 1;	// giving value to edges

			}
			value += controller*10;	// basic value
		}
	}

	return value;
}