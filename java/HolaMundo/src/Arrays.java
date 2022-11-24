public class Arrays {

    public static void main(String[] args) {

        //Array de una dimension
        String[] androidVersion = new String[17];
        int days[] = new int[7];

        //Array de dos dimensiones (equivalentes a tablas)
        String[][] cities = new String [4][2];

        //Array de 3 dimensiones (en este caso es mejor
        //usar una base de datos
        //Son utiles cuando trabajamos con calculos
        int [][][] numbers = new int [2][2][2];

        //arreglos de 4 o mas dimensiones son posibles
        int [][][][] numbers4 = new int [2][2][2][2];

        //ingresar objetos en un indice especifico
        //en este caso al array androidVersion
        androidVersion[0] = "Apple pie";
        androidVersion[1] = "Bannana Bread";
        androidVersion[2] = "Cupcake";
        androidVersion[3] = "Donut";

        System.out.println(androidVersion[1]);

        //Si quiero imprimir todos los valores sin necesidad de
        //hacerlo uno por uno puedo entonces usar un ciclo for

        for (int i = 0; i < androidVersion.length; i++) {
            System.out.println(androidVersion[i]);
        }
        //Los elementos sin un valor tendran valor null
        //esto depende de como definamos el array

        //Si hacemos lo mismo con el arreglo days obtendremos 0
        for (int i = 0; i < days.length; i++) {
            System.out.println(days[i]);
        }

        //Ingreso de informacion al array cities
        cities[0][0] = "Colombia";
        cities[0][1] = "Medellin";
        cities[1][0] = "Colombia";
        cities[1][1] = "Bogota";
        cities[2][0] = "Mexico";
        cities[2][1] = "Guadalajara";
        cities[3][0] = "Mexico";
        cities[3][1] = "CDMX";

        //para obtener la informacion de un array de 2 dimensiones
        for (int i = 0; i < cities.length; i++) {
            for (int j = 0; j < cities[i].length; j++) {
                System.out.println(cities[i][j]);
            }
        }

        //System.out.println(cities[0][0]);
        //System.out.println(cities[0][1]);
        //System.out.println(cities[1][0]);
        //System.out.println(cities[1][1]);

        int i = 7; char c = 'w';
        System.out.println((i >= 6) && (c == 'w'));
    }
}
