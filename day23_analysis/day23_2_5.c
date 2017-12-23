// Replace back goto with do...while

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
int f = 0;
int g = 0;
int h = 0;

void run(void) {
  while (1) {
    f = 1;                    //set f 1
    d = 2;                    //set d 2
    do {
      e = 2;                  //set e 2
      do {
	g = d;                //set g d
	g *= e;               //mul g e
	g -= b;               //sub g b
	if (g == 0) {         //jnz g 2
	  f = 0;              //set f 0
	}
	e++;                  //sub e -1
	g = e;                //set g e
	g -= b;               //sub g b
      } while (g != 0);       //jnz g -8
      d++;                    //sub d -1
      g = d;                  //set g d
      g -= b;                 //sub g b
    } while (g != 0);         //jnz g -13
    if (f == 0) {             //jnz f 2
      h++;                    //sub h -1
    }
    g = b;                    //set g b
    g -= c;                   //sub g c
    if (g == 0) {             //jnz g 2
      return;                 //jnz 1 3
    }
    b += 17;                  //sub b -17
  }                           //jnz 1 -23
}

int main(void) {
    run();
    printf("%d\n", h);
    return EXIT_SUCCESS;
}
