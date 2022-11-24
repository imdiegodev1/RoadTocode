public class ForLoop {

    static boolean isTurnOnLight = false;

    public static void main(String[] args) {

        turnOnOffLight();

        for (int i = 1; i < 10; i++) {
            printSOS();

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
