// Remove more superfluous code

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

//int a = 1; // unused
int b = 0;
int c = 0;
int d = 0;
int e = 0;
int f = 0;
int g = 0;
int h = 0;

void run(void) {
    //b = 81;                 //set b 81
    //c = b;                  //set c b
    c = 81;
    //b += 100000;            //sub b -100000
    b = 100081; //81 + 100000; 
    //c = b;                  //set c b
    //c = 100081;
    //c += 17000;             //sub c -17000
    //c = 100081 + 17000;
    c = 117081;
    
j1: f = 1;                    //set f 1
    d = 2;                    //set d 2
j4: e = 2;                    //set e 2
j3: g = d;                    //set g d
    g *= e;                   //mul g e
    g -= b;                   //sub g b
    if (g == 0) {             //jnz g 2
      f = 0;                  //set f 0
    }
    e++;                      //sub e -1
    g = e;                    //set g e
    g -= b;                   //sub g b
    if (g != 0) goto j3;      //jnz g -8
    d++;                      //sub d -1
    g = d;                    //set g d
    g -= b;                   //sub g b
    if (g != 0) goto j4;      //jnz g -13
    if (f == 0) {             //jnz f 2
      h++;                    //sub h -1
    }
j5: g = b;                    //set g b
    g -= c;                   //sub g c
    if (g == 0) {             //jnz g 2
      //goto j7;              //jnz 1 3
      return;
    }
    b += 17;                  //sub b -17
    goto j1;                  //jnz 1 -23
}

int main(void) {
    run();
    printf("%d\n", h);
    return EXIT_SUCCESS;
}
