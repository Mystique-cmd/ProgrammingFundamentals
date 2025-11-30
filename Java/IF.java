import java.util.Scanner;
public class IF{
	public static void main (String[] args) {
		Scanner input = new Scanner(System.in);
		final int RATE = 15;

		System.out.print("Enter units consumed:");
		int units = input.nextInt();

		double amount = 0;

		if (units <=100) {
			amount = units * RATE;
		}
		System.out.println("Bill Amount: Ksh. " + amount);
	}
}
