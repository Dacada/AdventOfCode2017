// Remove auxiliar register used to calculate intermediary values for comparisons

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
int count = 0;

void run(void) {
  while (1) {
    flag = 1;                 //set f 1
    d = 2;                    //set d 2
    
    do {
      e = 2;                  //set e 2
      do {
	//set g d
	//mul g e
	//sub g b
	if (d*e == b) {       //jnz g 2
	  flag = 0;           //set f 0
	}
	e++;                  //sub e -1
        //set g e
	//sub g b
      } while (e != b);       //jnz g -8
      d++;                    //sub d -1
      //set g d
      //sub g b
    } while (d != b);         //jnz g -13
    
    if (flag == 0) {          //jnz f 2
      count++;                //sub h -1
    }
    
    //set g b
    //sub g c
    if (b == c) {             //jnz g 2
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
