public class SwitchStatement {
    public static void main(String[] args) {

        //ejemplo de seleccion de modo light, dark o blue dark
        //de una app

        String colorModeSelected = "Dark";

        switch (colorModeSelected){
            case "Light":
                System.out.println("Seleccionaste Light Mode");
                break;
            case "Night":
                System.out.println("Seleccionaste Blue Dark Mode");
                break;
            case "Dark":
                System.out.println("Seleccionaste Light Mode");
                break;
            default:
                System.out.println("Selecciona una opcion correcta");

        }
    }
}
