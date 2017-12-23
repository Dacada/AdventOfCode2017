// Rewritten code - replaced do...while for while and some obvious optimizations. Removed original ASM instructions and superflous variables. Renamed the rest of variables.

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

int product = 100081;
int mult1 = 0;
int mult2 = 0;
int flag = 0;
int count = 0;

void run(void) {
  while (1) {
    flag = 1;
    mult1 = 2;
    
    while (mult1 != product) {
      mult2 = 2;
      
      while (mult2 != product) {
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
    
    if (product == 117081) {
      return;
    }
    
    product += 17;
  }
}

int main(void) {
    run();
    printf("%d\n", count);
    return EXIT_SUCCESS;
}
