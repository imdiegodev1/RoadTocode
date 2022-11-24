public class MathematicOperations {
    public static void main(String[] args) {
        double x = 2.1;
        double y = 3;

        //uso de la clase Math que Java tiene por defecto
        System.out.println(Math.PI);
        System.out.println(Math.E);

        //funcion CEIL para redondear siempre hacia el numero mayor
        System.out.println(Math.ceil(x));

        //funcion FlOOR redondea hacia el numero menor
        System.out.println(Math.floor(x));

        //Funcion exponencial primer numero entero
        //segundo numero la potencia
        System.out.println(Math.pow(x, y));

        //valor mayor entre dos datos
        System.out.println(Math.max(x, y));

        //Raiz cuadrada
        System.out.println(Math.sqrt(y));

        //area de un circulo de radio y
        System.out.println(Math.PI * Math.pow(y, 2));

        //area superficial de la esfera de radio y
        System.out.println(4 * Math.PI * Math.pow(y, 2));

        //Volumen de una esfera de radio y
        System.out.println((4/3) * Math.PI * Math.pow(y, 3));
    }
}
