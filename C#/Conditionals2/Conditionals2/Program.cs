// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

int totalJugador = 21;
int totalDealer = 15;
string message = "";
string switchControl = "menu";

//Blackjack, play to get 21 with 2 or more cards
//if you got more than 21 you lose

switch (switchControl)
{
    case "menu":
        Console.WriteLine("I wanna play a game");
        Console.WriteLine("Type 21 to start the game:");
        switchControl = Console.ReadLine();
        break;

    case "21":

        if (totalJugador > totalDealer && totalJugador < 22)
        {
            message = "You win!";
        }
        else if (totalJugador >= 22)
        {
            message = "You lose";
        }
        else if (totalJugador <= totalDealer)
        {
            message = "You lose";
        }
        else
        {
            message = "Not a valid result";
        }

        Console.WriteLine(message);
        break;
    default:
        Console.WriteLine("It is not a valid value");
        break;
}