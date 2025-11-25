import java.util.Scanner;
public class StudentManagementSystem {
    class Student {
        String name;
        int age;
        String studentId;
    }
    class Course {
        String courseName;
        String courseCode;
        int credits;
    }
    class Instructor {
        String name;
        String employeeId;
        String department;
    }

public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Welcome to the Student Management System!");
    
    System.out.print("Enter your name: ");
    String name = scanner.nextLine();
    System.out.print("Enter your age: ");
    int age = scanner.nextInt();
    scanner.nextLine(); // Consume newline
    System.out.print("Enter your student ID: ");
    String studentId = scanner.nextLine();

    System.out.print("Enter course name: ");
    String courseName = scanner.nextLine();
    System.out.print("Enter course code: ");
    String courseCode = scanner.nextLine();
    System.out.print("Enter course credits: ");
    int credits = scanner.nextInt();

    System.out.print("Enter instructor name: ");
    scanner.nextLine(); // Consume newline
    String instructorName = scanner.nextLine();
    System.out.print("Enter instructor employee ID: ");
    String employeeId = scanner.nextLine(); 

    scanner.close();

    // Display the entered information
    System.out.println("\nStudent Information:");
    System.out.println("Name: " + name);
    System.out.println("Age: " + age);
    System.out.println("Student ID: " + studentId);
    System.out.println("\nCourse Information:");
    System.out.println("Course Name: " + courseName);
    System.out.println("Course Code: " + courseCode);
    System.out.println("Credits: " + credits);
    System.out.println("\nInstructor Information:");
    System.out.println("Name: " + instructorName);
    System.out.println("Employee ID: " + employeeId);
}
}