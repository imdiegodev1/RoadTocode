public class IfStement {
    public static void main(String[] args) {
        boolean isBluetoorhEnable = false;
        int fileSended= 3;

        if (isBluetoorhEnable) {
            //send file
            fileSended++;
            System.out.println("Archivo enviado");
        } else {
            fileSended--;
            System.out.println("Por favor encender Bluetooth");
        }

        System.out.println(isBluetoorhEnable);
        System.out.println(fileSended);
    }
}
