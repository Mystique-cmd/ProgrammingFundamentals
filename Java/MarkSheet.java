import java.util.Scanner;
public class MarkSheet {
    public static void main(String[] args) {


        //Title
        System.out.println("                                                                                                       Dedan Kimathi University of Technology              ");
        System.out.println("                                                                                                         School of Computer Science and IT                 ");
        System.out.println("                                                                                                           Department of Computer Science                  ");
        System.out.println("                                                                                                               Academic Year: 2024/2025                     ");
        System.out.println("                                                                                                        STUDENT MARKSHEET ( SECOND YEAR RESULTS )            ");

        Scanner input=new Scanner(System.in);
        String fullName_1,fullName_2,fullName_3,fullName_4,fullName_5,regNo_1,regNo_2,regNo_3,regNo_4,regNo_5,Status;
        int  ccs2211_1,ccs2211_2,ccs2211_3,ccs2211_4,ccs2211_5,igs2202_1,igs2202_2,igs2202_3,igs2202_4,igs2202_5,ccs2208_1,ccs2208_2,ccs2208_3,ccs2208_4,ccs2208_5,sma2215_1,sma2215_2,sma2215_3,sma2215_4,sma2215_5,ccs2207_1,ccs2207_2,ccs2207_3,ccs2207_4,ccs2207_5,ccs2209_1,ccs2209_2,ccs2209_3,ccs2209_4,ccs2209_5,ccs2210_1,ccs2210_2,ccs2210_3,ccs2210_4,ccs2210_5;
        float AVERAGE_1,AVERAGE_2,AVERAGE_3,AVERAGE_4,AVERAGE_5,TOTALS_1,TOTALS_2,TOTALS_3,TOTALS_4,TOTALS_5;

        System.out.print("Enter Full Name:");
        fullName_1=input.nextLine();
        System.out.print("Enter Your Reg No.:");
        regNo_1=input.nextLine();
        System.out.print("Enter Your CCS2211 :");
        ccs2211_1=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your IGS2202:");
        igs2202_1=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your CCS2208:");
        ccs2208_1=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your SMA2215:");
        sma2215_1=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your CCS2207:");
        ccs2207_1=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your CCS2209:");
        ccs2209_1=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your CCS2210:");
        ccs2210_1=Integer.parseInt(input.nextLine());

        System.out.print("Enter Full Name:");
        fullName_2=input.nextLine();
        System.out.print("Enter Your Reg No.:");
        regNo_2=input.nextLine();
        System.out.print("Enter Your CCS2211:");
        ccs2211_2=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your IGS2202:");
        igs2202_2=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your CCS2208:");
        ccs2208_2=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your SMA2215:");
        sma2215_2=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your CSS2207:");
        ccs2207_2=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your CCS2209:");
        ccs2209_2=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your CCS2210:");
        ccs2210_2=Integer.parseInt(input.nextLine());

        System.out.print("Enter Full Name:");
        fullName_3=input.nextLine();
        System.out.print("Enter Your Reg No.:");
        regNo_3=input.nextLine();
        System.out.print("Enter Your CCS2211:");
        ccs2211_3=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your IGS2202:");
        igs2202_3=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your CCS2208:");
        ccs2208_3=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your SMA2215:");
        sma2215_3=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your CCS2207:");
        ccs2207_3=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your CCS2209:");
        ccs2209_3=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your CCS2210:");
        ccs2210_3=Integer.parseInt(input.nextLine());

        System.out.print("Enter Full Name:");
        fullName_4=input.nextLine();
        System.out.print("Enter Your Reg No.:");
        regNo_4=input.nextLine();
        System.out.print("Enter Your CCS2211:");
        ccs2211_4=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your IGS2202:");
        igs2202_4=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your CCS2208:");
        ccs2208_4=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your SMA2215:");
        sma2215_4=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your CCS2207:");
        ccs2207_4=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your CCS2209:");
        ccs2209_4=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your CCS2210:");
        ccs2210_4=Integer.parseInt(input.nextLine());


        System.out.print("Enter Full Name:");
        fullName_5=input.nextLine();
        System.out.print("Enter Your Reg No.:");
        regNo_5=input.nextLine();
        System.out.print("Enter Your CCS2211:");
        ccs2211_5=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your IGS2202:");
        igs2202_5=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your CCS2208:");
        ccs2208_5=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your SMA2215:");
        sma2215_5=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your CCS2207:");
        ccs2207_5=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your CCS2209:");
        ccs2209_5=Integer.parseInt(input.nextLine());
        System.out.print("Enter Your CCS2210:");
        ccs2210_5=Integer.parseInt(input.nextLine());

        input.close();
        
        TOTALS_1=ccs2211_1+igs2202_1+ccs2208_1+sma2215_1+ccs2207_1+ ccs2209_1+ccs2210_1;
        TOTALS_2=ccs2211_2+igs2202_2+ccs2208_2+sma2215_2+ccs2207_2+ ccs2209_2+ccs2210_2;
        TOTALS_3=ccs2211_3+igs2202_3+ccs2208_3+sma2215_3+ccs2207_3+ ccs2209_3+ccs2210_3;
        TOTALS_4=ccs2211_4+igs2202_4+ccs2208_4+sma2215_4+ccs2207_4+ ccs2209_4+ccs2210_4;
        TOTALS_5=ccs2211_5+igs2202_5+ccs2208_5+sma2215_5+ccs2207_5+ ccs2209_5+ccs2210_5;

        AVERAGE_1=TOTALS_1/7;
        AVERAGE_2=TOTALS_2/7;
        AVERAGE_3=TOTALS_3/7;
        AVERAGE_4=TOTALS_4/7;
        AVERAGE_5=TOTALS_5/7;

        System.out.println("Student Score Sheet");
        System.out.println("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------");
        System.out.println("Reg No. \t\tFull Name\t\tCSS 2211\tIGS 2202\tCCS 2208\tSMA 2215\tCCS 2207\tCCS 2209\tCCS 2210\tTOTALS\t\tAVERAGE\t\tSTATUS\t\tGRADE");
        System.out.println("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------");
        System.out.println(regNo_1 + "\t" + fullName_1 + "\t\t" + ccs2211_1 + "\t\t" + igs2202_1 + "\t\t" + ccs2208_1 + "\t\t" + sma2215_1 + "\t\t" + ccs2207_1 + "\t\t" + ccs2209_1 + "\t\t" + ccs2210_1 + "\t\t" + TOTALS_1 + "\t\t" + AVERAGE_1);
        System.out.println(regNo_2 + "\t" + fullName_2 + "\t\t" + ccs2211_2 + "\t\t" + igs2202_2 + "\t\t" + ccs2208_2 + "\t\t" + sma2215_2 + "\t\t" + ccs2207_2 + "\t\t" + ccs2209_2 + "\t\t" + ccs2210_2 + "\t\t" + TOTALS_2 + "\t\t" + AVERAGE_2);
        System.out.println(regNo_3 + "\t" + fullName_3 + "\t\t" + ccs2211_3 + "\t\t" + igs2202_3 + "\t\t" + ccs2208_3 + "\t\t" + sma2215_3 + "\t\t" + ccs2207_3 + "\t\t" + ccs2209_3 + "\t\t" + ccs2210_3 + "\t\t" + TOTALS_3 + "\t\t" + AVERAGE_3);
        System.out.println(regNo_4 + "\t" + fullName_4 + "\t\t" + ccs2211_4 + "\t\t" + igs2202_4 + "\t\t" + ccs2208_4 + "\t\t" + sma2215_4 + "\t\t" + ccs2207_4 + "\t\t" + ccs2209_4 + "\t\t" + ccs2210_4 + "\t\t" + TOTALS_4 + "\t\t" + AVERAGE_4);
        System.out.println(regNo_5 + "\t" + fullName_5 + "\t\t" + ccs2211_5 + "\t\t" + igs2202_5 + "\t\t" + ccs2208_5 + "\t\t" + sma2215_5 + "\t\t" + ccs2207_5 + "\t\t" + ccs2209_5 + "\t\t" + ccs2210_5 + "\t\t" + TOTALS_5 + "\t\t" + AVERAGE_5);
        }
    }
