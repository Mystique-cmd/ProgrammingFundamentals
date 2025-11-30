import java.util.Scanner;
public class ifelse {
	public static void main ( String[] args ){
		Scanner input = new Scanner(System.in);
		final double RATE_1 = 15.0, RATE_2 = 18.50;
		System.out.print("Enter units consumed:");
		int units = input.nextInt();

		double amount = 0;
		if ( units <= 100) {
			amount = units * RATE_1;
		}else{
			int remaining = units -100;
			amount = (100 * RATE_1) + (remaining * RATE_2);
		}
		System.out.println( "Bill Amount: Ksh " + amount);
	}
}
