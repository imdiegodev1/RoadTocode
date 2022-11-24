public class Casting {

    public static void main(String[] args) {

        double monthly = 30.0/12.0;
        System.out.println(monthly);

        //Estimacion
        int estimateMonthly = (int) monthly;
        System.out.println(estimateMonthly);

        //Exactitud
        int a = 30;
        int b = 12;

        System.out.println((double) a/b);
    }
}