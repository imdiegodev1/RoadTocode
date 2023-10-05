// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

//Explicit variable declaration.
int variableInt;
string variableString;
float variableFloat;
double variableDouble;
bool variableBoolean;

//This variables can be declared and in the future can be initialized

variableInt = 30;
variableString = "Hola mundo";
variableFloat = 30.5f;
variableDouble = 30.5;
variableBoolean = true;

Console.WriteLine("Variable Integer: "+ variableInt+ " and its type is: "+ variableInt.GetType());
Console.WriteLine("Variable String: " + variableString + " and its type is: " + variableString.GetType());
Console.WriteLine("Variable Float: " + variableFloat + " and its type is: " + variableFloat.GetType());
Console.WriteLine("Variable Double: " + variableDouble + " and its type is: " + variableDouble.GetType());
Console.WriteLine("Variable Boolean: " + variableBoolean + " and its type is: " + variableBoolean.GetType());

//Implicit variable declaration.
//In case of implicit variable declaration you must initialice the variable when you declare it
var variableInt2 = 0;
var variableString2 = "variable";
var variableFloat2 = 1.1f;
var variableDouble2 = 1.1d;
var variableBoolean2 = true;

Console.WriteLine("Variable Integer: " + variableInt2 + " and its type is: " + variableInt2.GetType());
Console.WriteLine("Variable String: " + variableString2 + " and its type is: " + variableString2.GetType());
Console.WriteLine("Variable Float: " + variableFloat2 + " and its type is: " + variableFloat2.GetType());
Console.WriteLine("Variable Double: " + variableDouble2 + " and its type is: " + variableDouble2.GetType());
Console.WriteLine("Variable Boolean: " + variableBoolean2 + " and its type is: " + variableBoolean2.GetType());

//Constant declaration.
//When you declare a constant you use the reserved word const
//Is better if you initialice the constant and declare its value in the same line
const double Pi = 3.141516;

Console.WriteLine("My constant is: " + Pi);
