// See https://aka.ms/new-console-template for more information
Console.WriteLine("Arithmetic operations");

var variableInt = 5;

//Single sum
variableInt++;
Console.WriteLine("The result for variableInt++: " + variableInt);

Console.WriteLine("If we do the same operation but just when printing: " + variableInt++);

Console.WriteLine("Where is the increment? it has to wait: " + variableInt);

Console.WriteLine("If we cange the order and use ++variableInt: " + ++variableInt);

//As we can see when I printed the variable with single sum the value does not change
//However when I print again the variable i get the increment. It is because in this case
//the order of the factors change the result.

//The single sum operator at the end first call the variable and then add a unit while
//the single sum operator at the beggining first sum and then call the variable

//The same behavior can be seen with single substraction


//Single substraction
var variableInt2 = 5;
variableInt2 --;
Console.WriteLine("The result for variableInt--: " + variableInt2);

Console.WriteLine("If we do the same operation but just when printing: " + variableInt2--);

Console.WriteLine("Where is the increment? it has to wait: " + variableInt2);

Console.WriteLine("If we cange the order and use --variableInt: " + --variableInt2);

//Multiply
var variableInt3 = 5;
var variableInt4 = 2;
int variableInt5;

variableInt5 = variableInt3 * variableInt4;

Console.WriteLine("The result of 5 * 2: " + variableInt5);

//But what if i multiply and integer with a double

var variabledouble0 = 1.5;

double variableCombination;

variableCombination = variableInt3 * variabledouble0;

Console.WriteLine("The result of 5 * 1.5: " + variableCombination);

//To get the result it should be stored in a double variable orr
//declare a implicit variable and initialize it with the operation

//Division
var variableInt6 = 5;
var variableInt7 = 2;
int variableInt8;

variableInt8 = variableInt6 / variableInt7;

Console.WriteLine("The result of 5 / 2: " + variableInt8);

//As you can see if we devide 2 integers and safe the result in an integer value it will
//store just the integer part of the number and ignore the decimal part

double variabledouble;

variabledouble = variableInt6 / variableInt7;

Console.WriteLine("The result of 5 / 2 stored in a double variable is: " + variabledouble);

//As you can see it does not change anything if we store the result in a double variable.
//then to get the decimal part you should:

double variabledouble2;

variabledouble2 = (double) variableInt6 / variableInt7;

Console.WriteLine("The result of 5 / 2 stored in a double variable is: " + variabledouble2);

Console.WriteLine("It is neccesary to explain how to use x and - operator?");