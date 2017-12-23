// Replaced inequalities, different than for greater than or smaller than, as appropriate

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

int product = 100081;
int mult1 = 0;
int mult2 = 0;
int flag = 0;
int count = 0;

void run(void) {
  while (product < 117081) {
    flag = 1;
    mult1 = 2;
    
    while (mult1 < product) {
      mult2 = 2;
      
      while (mult2 < product) {
	if (mult1*mult2 == product) {
	  flag = 0;
	  break;
	}
	
	mult2++;
      }
      
      if (flag == 0) {
	break;
      }
      
      mult1++;
    }

    if (flag == 0) {
      count++;
    }
    
    product += 17;
  }
}

int main(void) {
    run();
    printf("%d\n", count);
    return EXIT_SUCCESS;
}
