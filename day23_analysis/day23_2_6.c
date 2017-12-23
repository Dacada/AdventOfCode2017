// Try to give names to variables according to what they seem to be doing

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

//set b 81
//set c b
//jnz a 2
//jnz 1 5 // never reached
//mul b 100
//sub b -100000
//set c b
//sub c -17000

int b = 100081;
int c = 117081;
int d = 0;
int e = 0;
int flag = 0;
int tmp = 0;
int count = 0;

void run(void) {
  while (1) {
    flag = 1;                 //set f 1
    d = 2;                    //set d 2
    
    do {
      e = 2;                  //set e 2
      do {
	tmp = d;              //set g d
	tmp *= e;             //mul g e
	tmp -= b;             //sub g b
	if (tmp == 0) {       //jnz g 2
	  flag = 0;           //set f 0
	}
	e++;                  //sub e -1
	tmp = e;              //set g e
	tmp -= b;             //sub g b
      } while (tmp != 0);     //jnz g -8
      d++;                    //sub d -1
      tmp = d;                //set g d
      tmp -= b;               //sub g b
    } while (tmp != 0);       //jnz g -13
    
    if (flag == 0) {          //jnz f 2
      count++;                //sub h -1
    }
    
    tmp = b;                  //set g b
    tmp -= c;                 //sub g c
    
    if (tmp == 0) {           //jnz g 2
      return;                 //jnz 1 3
    }
    
    b += 17;                  //sub b -17
  }                           //jnz 1 -23
}

int main(void) {
    run();
    printf("%d\n", count);
    return EXIT_SUCCESS;
}
