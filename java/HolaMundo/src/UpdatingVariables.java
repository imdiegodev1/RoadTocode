public class UpdatingVariables {
    public static void main(String[] args) {
        //Salario de un empleado
        int salary = 1000;

        //Recibe bono de 200
        salary += 200;
        System.out.println(salary);

        //aportes a pension: descuento de 50
        salary = salary - 50;
        System.out.println(salary);

        //horas extra 30 c/u
        //uso cupon 45

        salary = salary + (2*30) - 45;
        System.out.println(salary);

        //Manejo cadenas de texto
        String employeeName = "Diego";
        employeeName = employeeName + " Naranjo";
        System.out.println(employeeName);

        System.out.println("Tu nombre es: " + employeeName);
    }
}
