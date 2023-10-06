// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

//the relational values in C# are:
//EQUALS ==
//DIFFERENT !=
//LESS THAN <
//HIGHER THAN >
//LESS OR EQUAL THAN <=
///HIGHER OR EQUAL THAN >=

var (value1, value2, value3) = (10, 2, 5);

//EQUALS
bool result1 = value1 == value2;

Console.WriteLine("The result of compare 10 == 2 is: " + result1);

//DIFFERENT
bool result2 = value1 != value2;

Console.WriteLine("The result of compare 10 != 2 is: " + result2);

//HIGHER THAN
bool result3 = value1  > value2;
Console.WriteLine("The result of comparer 10 > 2 is: " + result3);

bool result4 = value2 > value3;
Console.WriteLine("The result of comparer 2 > 5 is: " + result4);

//LESS THAN
bool result5 = value1 < value2;
Console.WriteLine("The result of comparer 10 < 2 is: " + result5);

bool result6 = value2 < value3;
Console.WriteLine("The result of comparer 2 < 5 is: " + result6);