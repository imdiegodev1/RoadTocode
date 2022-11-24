public class IncrementDecrement {

    public static void main(String[] args) {
        int lives = 5;
        lives = lives -1;

        System.out.println(lives); //4

        //posfijo
        lives--; //Decremento
        System.out.println(lives); //3

        lives++; //Incremento
        System.out.println(lives); //4

        //prefijo
        int gift = 100 + ++lives;
        System.out.println(gift);
    }
}
