// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");


//As in other languages, C# has the following logic operators:
//AND &&
//OR ||
//NOT !
//XOR ^
//AND binary logic &
//OR binary logic |


bool value1 = true;
bool value2 = true;
bool value3 = false;

//AND
bool resultAnd = value1 && value2;
Console.WriteLine("The result of true && true is: " + resultAnd);

//OR
bool resultOr = value1 || value2;
Console.WriteLine("The result of true || true is: " + resultOr);

bool resultOr2 = value1 || value3;
Console.WriteLine("The result of true || false is: " + resultOr2);

//NOT
bool resultNot = !value1;
bool resultNot2 = !value3;
Console.WriteLine("The result of !true: " + resultNot);
Console.WriteLine("The result of !false: " + resultNot2);

//XOR
bool resultXor = value1 ^ value2;
Console.WriteLine("The result of true ^ true is: " + resultXor);

bool resultXor2 = value1 ^ value3;
Console.WriteLine("The result of true ^ false is: " + resultXor2);