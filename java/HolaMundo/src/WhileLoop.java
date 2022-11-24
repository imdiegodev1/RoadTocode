public class WhileLoop {

    static boolean isTurnOnLight = false;

    public static void main(String[] args) {

        turnOnOffLight();

        int i = 1;
        while (isTurnOnLight && i<=10){
            printSOS();
            i++;
        }
    }

    public static void printSOS(){
        System.out.println(". . . _ _ _ . . . ");
    }

    public static boolean turnOnOffLight() {

        //Esto es equivalente al if comentado mas abajo
        //a esto se le llama operador ternareo
        isTurnOnLight = (isTurnOnLight)?false:true;

        //if reemplazado por operador ternareo
        //if (isTurnOnLight){
        //    isTurnOnLight = false;
        //} else {
        //    isTurnOnLight = true;
        //}

        return isTurnOnLight;
    }
}
