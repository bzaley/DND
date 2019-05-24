#include <stdio.h>
//#include "methods.h" //All called methods for diceRoller are accessible here
#include <string.h>
//Executable program, hosts just main function
int main(){
  char* token;
  printf("Enter amount of dice type (XdY)[Enter]");
  char diceRoll[11];
  char delim[2] ="d";
  //Need to limit dice to positive numbers
  scanf("%s", diceRoll);
  token = strtok(diceRoll, delim);
  while(token!=NULL){
    printf("%s\n", token);
    token = strtok(NULL, delim);
  }
  return 0;
}
