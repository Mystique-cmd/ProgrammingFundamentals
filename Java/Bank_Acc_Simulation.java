public class Account {
	//encapsulated fields (private)
	private String accountNumber;
	private double balance;
	//constructor - its a special type of method that is used to initialize objects. 
	//It is called automatically when an obect of a class is created
	public Account ( String accountNumber, double balance){
		this.accountNumber = accountNumber;
		this.balance = initialBalance;
	}
	
	public void deposit( double amount){
		if (amount > 0 ) {
			balance += amount;
			System.out.println("Deposited : $" + amount);
		}else{
			System.out.println("Deposited amount must be positive");
		}
	}
	
	public void withdraw ( double amount ){
		if ( amount > 0 && amount <= balance){
			balance -= amount;
			System.out.println("Withdrawn : $" + amount);
		}else{
			System.out.println("Insufficient funds or Invalid amount");
		}
	}
	
	public double getBalance(){
		return balance;
	}
	
	public String getAccountNumber(){
		return accountNumber;
	}
}

public class Customer{
	private String name;
	private Account account;
	
	public Customer(String name, Account account){
		this.name = name;
		this.account = account;	
	}
	
	public void displayCustomerInfo(){
		System.out.println("Customer: " + name);
		System.out.println("Account Number: " + account.getAccountNumber());
		System.out.println("Balance: $" + account.getBalance());
	}
	
	public void deposit (double amount){
		account.deposit(amount);
	}
	
	public void withdraw(double amount){
		account.withdraw(amount);
	}
	
	public void checkBalance(){
		System.out.println("Current Balance : $" + account.getBalance());
	}
}

public class Main {
	public static void main(String[] args){
		Account acc1 = new Account ("ACC123", 500.0);
		Customer cust1 = new Customer("Alice", acc1);
		
		cust1.displayCustomerInfo();
		cust1.deposit(200);
		cust1.withdraw(100);
		cust1.checkBalance();
	}
}
