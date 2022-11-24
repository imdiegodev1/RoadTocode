public class Funciones {

    public static void main(String[] args) {

        int y = 3;

        //area de un circulo de radio y
        double area_circulo = circleArea(y);
        System.out.println(area_circulo);

        //area superficial de la esfera de radio y
        double sphere_area = sphereArea(y);
        System.out.println(sphere_area);

        //Volumen de una esfera de radio y
        double sphere_volume = sphereVolume(y);
        System.out.println(sphere_volume);

        //Valor moneda
        double quantity;
        String currency;

        System.out.println("MXP a USD: "+convertToDolar(quantity = 200, currency = "MXN"));
        System.out.println("COP a USD: "+convertToDolar(quantity = 5000, currency = "COP"));

    }

    public static double circleArea(double radius) {

        return Math.PI * Math.pow(radius, 2);
    }

    public static double sphereArea(double radius) {

        return 4 * Math.PI * Math.pow(radius, 2);
    }

    public static double sphereVolume (double radius) {

        return (4/3) * Math.PI * Math.pow(radius, 3);
    }

    /**
     *Descripcion: Funcion que especificando su moneda convierte una cantidad
     * de dinero a dolares
     *
     * @param quantity Cantidad de dinero
     * @param currency Tipo de moneda: solo acepta MXNo COP
     * @return quantity Devuelve la cantidad actualizada en Dolares
     *
     **/
    public static double convertToDolar (double quantity, String currency) {
        //MXN COP

        switch (currency){
            case "MXN":
                quantity = quantity * 0.052;
                break;
            case "COP":
                quantity = quantity * 0.00031;
                break;
        }

        return quantity;
    }
}
