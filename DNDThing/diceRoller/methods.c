#include <stdio.h>
#include <methods.h>

char[] rollDice(int numRolls, int numSides){
  int result=0;
  int[numrolls] individualRolls;
  int roll;

  for(int i=0; i<numRolls, i++){
    roll=(rand()%(numSides - 1)) + 1;
    individualRolls[i]=roll;
    result+=roll;
  }
}
