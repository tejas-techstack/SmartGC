#include <stdio.h>
#include <stdlib.h>

int fibonacci(int n) {

    if (n <= 1) {
        return n;
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

int main() {
    int random = 5;
    int num = 10;
    int *n = (int *)malloc(sizeof(int));
    int *x = (int *)malloc(sizeof(int));
    
    *x = random;
    *n = num;

    printf("Fibonacci sequence up to %d:\n", *n);
    for (int i = 0; i < *n; i++) {
        printf("%d\n", fibonacci(i));
	printf("----\n");
    }



    printf("\n");
    return 0;
}
