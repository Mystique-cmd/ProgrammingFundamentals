import java.util.Scanner;
public class ifelseifelse {
	public static void main (String[] args ){
		final double RATE_1 = 15.0, RATE_2 = 18.50, RATE_3 = 24.0, RATE_4 =28.0;
		int first100 = 100, next100 = 100, next300 = 300;
		Scanner input = new Scanner(System.in);
		System.out.print("Enter units consumed:");
		int units = input.nextInt();
		double amount = 0;

		if ( units <= 100) {
			amount = units * RATE_1;
		}else if ( units <=200 ){
			int remaining = units -first100;
			amount = (first100 * RATE_1) + (remaining * RATE_2);
		}else if(units <=500) {
			int remaining = units - (first100 + next100);
			amount = (first100 * RATE_1) + (next100 * RATE_2) + (remaining * RATE_3);
		}else{
			int remaining = units - ( first100 +next100 +next300);
			amount = (first100 * RATE_1) + (next100 * RATE_2) + (next300 * RATE_3) + (remaining * RATE_4);
		}
		System.out.println("Bill Amount: Ksh " + amount);
	}
}

