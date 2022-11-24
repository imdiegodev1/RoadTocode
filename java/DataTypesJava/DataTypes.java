public class DataTypes {
    public static void main(String[] args) {

        int n = 1234567890;
        //Para definir un long debo agregar L al final
        long nL = 1234567890L;

        double nD = 123.456;
        //Para definir un float debo agregar F al final
        float nF = 123.456F;

        //A partir de Java 0 puedo crear variables
        //sin definir explicitamente el tipo

        var salary = 1000;
        var pension = salary*0.3; //Resultado double
        System.out.println(salary);
        System.out.println(pension);

        var employeeName = "Diego Naranjo";
        System.out.println("Employee: "+employeeName+" Salary: "+salary)
    }
}
