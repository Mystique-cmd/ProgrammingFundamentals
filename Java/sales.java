import java.util.Scanner;
public class sales{
    public static void main(String[] args){
        Scanner input=new Scanner(System.in);

        System.out.println("Enter Bill to information:");
        System.out.print("Bill to Name:");
        String billName=input.nextLine();
        System.out.println("Enter Bill Address1:");
        String billAddress1=input.nextLine();
        System.out.println("Enter Bill Address2:");
        String billAddress2=input.nextLine();
        System.out.println("Enter Bill GSTIN:");
        String billGSTIN=input.nextLine();
        System.out.println("Enter Bill Contact:");
        String billContact=input.nextLine();
        System.out.println("Enter Bill Email:");
        String billEmail=input.nextLine();

        System.out.println("Enter Shipping Information:");
        System.out.println("Ship to Name:");
        String shipName=input.nextLine();
        System.out.println("Enter Ship Address1:");
        String shipAddress1=input.nextLine();
        System.out.println("Enter Ship Address2:");
        String shipAddress2=input.nextLine();
        System.out.println("Enter Ship GSTIN:");
        String shipGSTIN=input.nextLine();
        System.out.println("Enter Ship Contact:");
        String shipContact=input.nextLine();
        System.out.println("Enter Ship Email:");
        String shipEmail=input.nextLine();

        //product 1
        System.out.println("Enter Product1 info:");
        System.out.print("Enter Product1 Serial No:");
        String p1SNo=input.nextLine();
        System.out.print("Product Code:");
        String p1Code=input.nextLine();
        System.out.print("Enter Product1 Name:");
        String p1Name=input.nextLine();
        System.out.print("Enter Product1 HNS CODE:");
        String p1HSN=input.nextLine();
        System.out.print(" Enter Product1 Quantity : ");
        double p1Qty = Double.parseDouble(input.nextLine());
        System.out.print("Enter Product1 Units:");
        String p1Units=input.nextLine();
        System.out.print("Enter Product1 Rate: ");
        double p1Rate=Double.parseDouble(input.nextLine());
        System.out.print("Enter Product1 Tax:");
        double p1Tax=Double.parseDouble(input.nextLine());
        System.out.println();

        //Product 2
        System.out.println("Enter Product2 info:");
        System.out.print("Enter Product2 Serial No:");
        String p2SNo=input.nextLine();
        System.out.print("Enter Product Code");
        String p2Code=input.nextLine();
        System.out.print("Enter Product2 Name:");
        String p2Name=input.nextLine();
        System.out.print("Enter Product2 HSN code:");
        String p2HSN=input.nextLine();
        System.out.print(" Enter Product2 Quantity : ");
        double p2Qty = Double.parseDouble(input.nextLine());
        System.out.print("Enter Product2 Units:");
        String p2Units=input.nextLine();
        System.out.print("Enter Product2 Rate:");
        double p2Rate=Double.parseDouble(input.nextLine());
        System.out.print("Enter Product2 Tax:");
        double p2Tax=Double.parseDouble(input.nextLine());

        //product 3
        System.out.println("Enter Product3 info:");
        System.out.print("Enter Product3 Serial No:");
        String p3SNo=input.nextLine();
        System.out.print("Product3 Code:");
        String p3Code=input.nextLine();
        System.out.print("Enter Product3 Name:");
        String p3Name=input.nextLine();
        System.out.print("Enter Product3 HNS CODE:");
        String p3HSN=input.nextLine();
        System.out.print(" Enter Product3 Quantity : ");
        double p3Qty = Double.parseDouble(input.nextLine());
        System.out.print("Enter Product3 Units:");
        String p3Units=input.nextLine();
        System.out.print("Enter Product3 Rate: ");
        double p3Rate=Double.parseDouble(input.nextLine());
        System.out.print("Enter Product3 Tax:");
        double p3Tax=Double.parseDouble(input.nextLine());
        System.out.println();

        //product 4
        System.out.println("Enter Product4 info:");
        System.out.print("Enter Product4 Serial No:");
        String p4SNo=input.nextLine();
        System.out.print("Product Code:");
        String p4Code=input.nextLine();
        System.out.print("Enter Product4 Name:");
        String p4Name=input.nextLine();
        System.out.print("Enter Product4 HNS CODE:");
        String p4HSN=input.nextLine();
        System.out.print(" Enter Product4 Quantity : ");
        double p4Qty = Double.parseDouble(input.nextLine());
        System.out.print("Enter Product4 Units:");
        String p4Units=input.nextLine();
        System.out.print("Enter Product4 Rate: ");
        double p4Rate=Double.parseDouble(input.nextLine());
        System.out.print("Enter Product4 Tax:");
        double p4Tax=Double.parseDouble(input.nextLine());
        System.out.println();


        //product 5
        System.out.println("Enter Product5 info:");
        System.out.print("Enter Product5 Serial No:");
        String p5SNo=input.nextLine();
        System.out.print("Product Code:");
        String p5Code=input.nextLine();
        System.out.print("Enter Product5 Name:");
        String p5Name=input.nextLine();
        System.out.print("Enter Product5 HNS CODE:");
        String p5HSN=input.nextLine();
        System.out.print(" Enter Product5 Quantity : ");
        double p5Qty = Double.parseDouble(input.nextLine());
        System.out.print("Enter Product5 Units:");
        String p5Units=input.nextLine();
        System.out.print("Enter Product5 Rate: ");
        double p5Rate=Double.parseDouble(input.nextLine());
        System.out.print("Enter Product5 Tax:");
        double p5Tax=Double.parseDouble(input.nextLine());
        System.out.println();

        //product 6
        System.out.println("Enter Product6 info:");
        System.out.print("Enter Product6 Serial No:");
        String p6SNo=input.nextLine();
        System.out.print("Product Code:");
        String p6Code=input.nextLine();
        System.out.print("Enter Product6 Name:");
        String p6Name=input.nextLine();
        System.out.print("Enter Product6 HNS CODE:");
        String p6HSN=input.nextLine();
        System.out.print(" Enter Product6 Quantity : ");
        double p6Qty = Double.parseDouble(input.nextLine());
        System.out.print("Enter Product6 Units:");
        String p6Units=input.nextLine();
        System.out.print("Enter Product6 Rate: ");
        double p6Rate=Double.parseDouble(input.nextLine());
        System.out.print("Enter Product6 Tax:");
        double p6Tax=Double.parseDouble(input.nextLine());
        System.out.println();

        //product 7

        System.out.println("Enter Product7 info:");
        System.out.print("Enter Product7 Serial No:");
        String p7SNo=input.nextLine();
        System.out.print("Product Code:");
        String p7Code=input.nextLine();
        System.out.print("Enter Product7 Name:");
        String p7Name=input.nextLine();
        System.out.print("Enter Product7 HNS CODE:");
        String p7HSN=input.nextLine();
        System.out.print(" Enter Product7 Quantity : ");
        double p7Qty = Double.parseDouble(input.nextLine());
        System.out.print("Enter Product7 Units:");
        String p7Units=input.nextLine();
        System.out.print("Enter Product7 Rate: ");
        double p7Rate=Double.parseDouble(input.nextLine());
        System.out.print("Enter Product7 Tax:");
        double p7Tax=Double.parseDouble(input.nextLine());
        System.out.println();
        //closing Scanner


        //calculations
        //totals
        double p1amount = p1Qty * p1Rate;
        double p1TaxF=p1amount*(p1Tax/100);
        double finalAmount1=p1amount+p1TaxF;

        double p2amount = p2Qty * p2Rate;
        double p2TaxF=p2amount*(p2Tax/100);
        double finalAmount2=p2amount+p2TaxF;

        double p3amount = p3Qty * p3Rate;
        double p3TaxF=p3amount*(p3Tax/100);
        double finalAmount3=p3amount+p3TaxF;

        double p4amount = p4Qty * p4Rate;
        double p4TaxF=p4amount*(p4Tax/100);
        double finalAmount4=p4amount+p4TaxF;

        double p5amount = p5Qty * p5Rate;
        double p5TaxF=p5amount*(p5Tax/100);
        double finalAmount5=p5amount+p5TaxF;

        double p6amount = p6Qty * p6Rate;
        double p6TaxF=p6amount*(p6Tax/100);
        double finalAmount6=p6amount+p6TaxF;


        double p7amount = p7Qty * p7Rate;
        double p7TaxF=p7amount*(p7Tax/100);
        double finalAmount7=p1amount+p7TaxF;

        //SUM OF TOTALS
        double subTotal=finalAmount1+finalAmount2+finalAmount3+finalAmount4+finalAmount5+finalAmount6+finalAmount7;
        double discountRate = 0.6368/100;
        double discountValue = subTotal * discountRate;

        // Grand total
        double grandTotal = subTotal - discountValue;



        // Bill To and Ship To block
        System.out.println("Bill To:                          \t\tShip To:");
        System.out.println(billName + "\t\t\t\t" + shipName);
        System.out.println(billAddress1 + ", " + billAddress2 + "\t\t" + shipAddress1 + ", " + shipAddress2);
        System.out.println("GSTIN: " + billGSTIN + "\t\t\t\tGSTIN: " + shipGSTIN);
        System.out.println("Contact: " + billContact + "\t\t\tContact: " + shipContact);
        System.out.println("Email: " + billEmail + "\t\tEmail: " + shipEmail);

        System.out.println();
        System.out.println("Payment Date: 7 days from date of delivery\tPayment Terms: 100% against invoice");
        System.out.println();

        // Products
        System.out.println(p1SNo + "\t" + p1Code + "\t" + p1Name + "\t" + p1HSN + "\t" + p1Qty + "\t" + p1Units + "\t" + p1Rate + "\t" + p1Tax + "%\t" + finalAmount1);
        System.out.println(p2SNo + "\t" + p2Code + "\t" + p2Name + "\t" + p2HSN + "\t" + p2Qty + "\t" + p2Units + "\t" + p2Rate + "\t" + p2Tax + "%\t" + finalAmount2);
        System.out.println(p3SNo + "\t" + p3Code + "\t" + p3Name + "\t" + p3HSN + "\t" + p3Qty + "\t" + p3Units + "\t" + p3Rate + "\t" + p3Tax + "%\t" + finalAmount3);
        System.out.println(p4SNo + "\t" + p4Code + "\t" + p4Name + "\t" + p4HSN + "\t" + p4Qty + "\t" + p4Units + "\t" + p4Rate + "\t" + p4Tax + "%\t" + finalAmount4);
        System.out.println(p5SNo + "\t" + p5Code + "\t" + p5Name + "\t" + p5HSN + "\t" + p5Qty + "\t" + p5Units + "\t" + p5Rate + "\t" + p5Tax + "%\t" + finalAmount5);
        System.out.println(p6SNo + "\t" + p6Code + "\t" + p6Name + "\t" + p6HSN + "\t" + p6Qty + "\t" + p6Units + "\t" + p6Rate + "\t" + p6Tax + "%\t" + finalAmount6);
        System.out.println(p7SNo + "\t" + p7Code + "\t" + p7Name + "\t" + p7HSN + "\t" + p7Qty + "\t" + p7Units + "\t" + p7Rate + "\t" + p7Tax + "%\t" + finalAmount7);

        System.out.println("-------------------------------------------------------------------------------------------");
        System.out.println("\t\t\t\t\t\t\tTotal:\t" + subTotal);
        System.out.println("\t\t\t\t\t\t\tDiscount:\t" + discountValue);
        System.out.println("\t\t\t\t\t\t\tGrand Total:\t" + grandTotal);
        System.out.println("-------------------------------------------------------------------------------------------");

        input.close();







    }
}
