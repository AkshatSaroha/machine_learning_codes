// using System;
// using System.Security.Cryptography.X509Certificates;

// class Program
// {
//     // main method - entry point of program 
//     static void Main()
//     {
//         var myInteger = 0;
//         var myDouble = 0.0;
//         var myString = "";
//         var myBoolean = false;
//         var myChar = ' ';

//         Console.Write("Enter an integer: ");
//         myInteger = Convert.ToInt32(Console.ReadLine());

//         Console.Write("Enter a double value: ");
//         myDouble = Convert.ToDouble(Console.ReadLine());

//         Console.Write("Enter a string: ");
//         myString = Console.ReadLine();

//         Console.Write("Enter a boolean value(true/false): ");
//         myBoolean = Convert.ToBoolean(Console.ReadLine());

//         Console.Write("Enter a single character: ");
//         myChar = Convert.ToChar(Console.ReadLine());

//         Console.WriteLine("You have entered following data: ");
//         Console.WriteLine($"Integer: {myInteger}");
//         Console.WriteLine($"Double: {myDouble}");
//         Console.WriteLine($"String: {myString}");
//         Console.WriteLine($"Boolean: {myBoolean}");
//         Console.WriteLine($"Character: {myChar}");
//     }

// }

// class Program
// {
//     static void Main()
//     {
//         Console.Write("ENter a number: ");
//         int number = Convert.ToInt32(Console.ReadLine());

//         if (number > 0)
//         {
//             Console.WriteLine("Positive Number");
//         }
//         else if (number < 0)
//         {
//             Console.WriteLine("Negative Number");
//         }
//         else
//         {
//             Console.WriteLine("Zero");
//         }
//     }
// }

// class Program
// {
//     static void Main()
//     {
//         Console.Write("Enter the marks: ");
//         int marks = Convert.ToInt32(Console.ReadLine());

//         if (marks >= 90)
//         {
//             Console.WriteLine('A');
//         }
//         else if (marks >= 80 && marks < 89)
//         {
//             Console.WriteLine('B');
//         }
//         else if (marks >= 70 && marks < 80)
//         {
//             Console.WriteLine('C');
//         }
//         else if (marks > 60 && marks < 69)
//         {
//             Console.WriteLine('D');
//         }
//         else
//         {
//             Console.WriteLine('F');
//         }
//     }
// }


// class Program
// {
//     static void Main()
//     {
//         Console.Write("ENter a letter: ");
//         char input = Char.ToLower(Console.ReadKey().KeyChar);
//         Console.WriteLine();
//         switch (input)
//         {
//             case 'v':
//                 Console.WriteLine("Violet");
//                 break;
//             case 'i':
//                 Console.WriteLine("Indigo");
//                 break;
//             case 'b':
//                 Console.WriteLine("Blue");
//                 break;
//             case 'g':
//                 Console.WriteLine("Green");
//                 break;
//             case 'y':
//                 Console.WriteLine("Yellow");
//                 break;
//             case 'o':
//                 Console.WriteLine("Orange");
//                 break;
//             case 'r':
//                 Console.WriteLine("Red");
//                 break;

//             default:
//                 if (Char.IsLetter(input))
//                 {
//                     Console.WriteLine("the letter is not in VIBGYOR");
//                 }
//                 else
//                 {
//                     Console.WriteLine("Enter a valid letter");
//                 }
//                 break;
//         }
//     }
// }

// class Program
// {
//     static void Main()
//     {
//         // Arithmetic op
//         int a = 10, b = 3;
//         Console.WriteLine("Addition = " + (a + b));
//         Console.WriteLine("Subtraction = " + (a - b));
//         Console.WriteLine("Multiplication = " + (a * b));
//         Console.WriteLine("Division = " + (a / b));
//         Console.WriteLine("Modulo = " + (a % b));

//         // Comparison op
//         Console.WriteLine("Is a Equal to b = " + (a == b));
//         Console.WriteLine("Is a NOT Equal to b = " + (a != b));

//         // Logical operator
//         bool x = true, y = false;
//         Console.WriteLine("Initial values: x = " + x + ", y = " + y);
//         Console.WriteLine("x AND y : " + (x && y));
//         Console.WriteLine("x OR y : " + (x || y));
//         Console.WriteLine("x NOT : " + (!x));
//     }
// }


// ----------------------- OOPS -------------------------

// class BankAccount
// {
//     // Encapsulated private field
//     private double balance;
//     public BankAccount(double initialBalance)
//     {
//         balance = initialBalance;
//     }
//     // Method to deposit amount
//     public void Deposit(double amountToDeposit)
//     {
//         if (amountToDeposit > 0)
//         {
//             balance = balance + amountToDeposit;
//             Console.WriteLine($"Deposited amount: ${amountToDeposit}, New Balance: ${balance}");
//         }
//         else
//         {
//             Console.WriteLine("Deposit amount msut be positive!");
//         }
//     }

//     public void Withdraw(double amountToWithdraw)
//     {
//         if (amountToWithdraw > 0 && amountToWithdraw <= balance)
//         {
//             balance = balance - amountToWithdraw;
//             Console.WriteLine($"Withdrawl Amount: ${amountToWithdraw}, New Balance: ${balance}");
//         }
//         else
//         {
//             Console.WriteLine("Withdraw amount msut be positive!");
//         }
//     }
//     public Double GetAccountBalance()
//     {
//         return balance;
//     }
// }  

// class Program {
//     static void Main()
//     {
//         BankAccount bankAccount = new BankAccount(10000.25);
//         Console.WriteLine($"Initial balance : ${bankAccount.GetAccountBalance()}");
//         bankAccount.Withdraw(500);
//         Console.WriteLine($"After withdrawl : ${bankAccount.GetAccountBalance()}");
//         bankAccount.Deposit(1000);
//         Console.WriteLine($"After Deposit : ${bankAccount.GetAccountBalance()}");
//     }
// }

// class Animal
// {
//     public String name;
//     public Animal(String animalName)
//     {
//         name = animalName;
//     }
//     public void Speak()
//     {
//         Console.WriteLine(name + " makes a sound.");
//     }
// }
// class Dog : Animal // INHERITANCE
// {
//     public Dog(String name) : base(name)
//     {

//     }
//     public void Speak()
//     {
//         Console.WriteLine(name + " bhow bhow");
//     }
// }

// class Program
// {
//     static void Main()
//     {
//         Animal myAnimal = new Animal("Generic Animal");
//         Dog myDog = new Dog("Sheru");

//         myAnimal.Speak();
//         myDog.Speak();
//     }
// }

// using System;

// // Interface for Sports
// interface ISport
// {
//     void PlaySport(string sportName);
// }

// // Interface for Art
// interface IArt
// {
//     void PerformArt(string artType);
// }

// // SIngle Inheritance
// class Person
// {
//     public string Name;
//     public int Age;

//     public void DisplayInfo()
//     {
//         Console.WriteLine($"Name: {Name}, Age: {Age}");
//     }
// }

// class Student : Person
// {
//     public string StudentID;

//     public void DisplayStudentInfo()
//     {
//         DisplayInfo();
//         Console.WriteLine($"Student ID: {StudentID}");
//     }
// }

// // Multilevel Inheritance
// class GraduateStudent : Student
// {
//     public string Degree;

//     public void DisplayGraduateInfo()
//     {
//         DisplayStudentInfo();
//         Console.WriteLine($"Degree: {Degree}");
//     }
// }

// // Hierarchical Inheritance
// class Teacher : Person
// {
//     public string Subject;

//     public void DisplayTeacherInfo()
//     {
//         DisplayInfo();
//         Console.WriteLine($"Subject: {Subject}");
//     }
// }

// class Admin : Person
// {
//     public string Department;

//     public void DisplayAdminInfo()
//     {
//         DisplayInfo();
//         Console.WriteLine($"Department: {Department}");
//     }
// }

// // Multiple Inheritance via Interfaces
// class ExtraCurricularStudent : Student, ISport, IArt
// {
//     private string sport;
//     private string art;

//     public void PlaySport(string sportName)
//     {
//         sport = sportName;
//         Console.WriteLine($"Plays: {sport}");
//     }

//     public void PerformArt(string artType)
//     {
//         art = artType;
//         Console.WriteLine($"Performs: {art}");
//     }

//     public void DisplayExtraCurricularInfo()
//     {
//         DisplayStudentInfo();
//         PlaySport(sport);
//         PerformArt(art);
//     }
//     // Constructor
//     public ExtraCurricularStudent(string name, int age, string id, string sportName, string artType)
//     {
//         Name = name;
//         Age = age;
//         StudentID = id;
//         sport = sportName;
//         art = artType;
//     }
// }

// // Hybrid Inheritance: 
// class ExtraCurricularGraduateStudent : GraduateStudent, ISport, IArt
// {
//     private string sport;
//     private string art;

//     public void PlaySport(string sportName)
//     {
//         sport = sportName;
//         Console.WriteLine($"Plays: {sport}");
//     }

//     public void PerformArt(string artType)
//     {
//         art = artType;
//         Console.WriteLine($"Performs: {art}");
//     }

//     public void DisplayFullProfile()
//     {
//         DisplayGraduateInfo();
//         PlaySport(sport);
//         PerformArt(art);
//     }

//     public ExtraCurricularGraduateStudent(string name, int age, string id, string degree, string sportName, string artType)
//     {
//         Name = name;
//         Age = age;
//         StudentID = id;
//         Degree = degree;
//         sport = sportName;
//         art = artType;
//     }
// }

// class Program
// {
//     static void Main()
//     {
//         // 1. Single Inheritance
//         Console.WriteLine("------------- Single Inheritance --------------");
//         Student s1 = new Student { Name = "Akshat", Age = 20, StudentID = "101" };
//         s1.DisplayStudentInfo();
//         Console.WriteLine();

//         // 2. Multilevel Inheritance
//         Console.WriteLine("------------- Multilevel Inheritance -------------");
//         GraduateStudent g1 = new GraduateStudent
//         {
//             Name = "Saroha",
//             Age = 21,
//             StudentID = "102",
//             Degree = "BTech"
//         };
//         g1.DisplayGraduateInfo();
//         Console.WriteLine();

//         // 3. Hierarchical Inheritance
//         Console.WriteLine("-------------- Hierarchical Inheritance -------------");
//         Teacher t1 = new Teacher { Name = "Ravita", Age = 35, Subject = "Mathematics" };
//         t1.DisplayTeacherInfo();
//         Console.WriteLine();

//         Admin a1 = new Admin { Name = "Ashutosh", Age = 40, Department = "Databases" };
//         a1.DisplayAdminInfo();
//         Console.WriteLine();

//         // 4. Multiple Inheritance via Interfaces
//         Console.WriteLine("--------------- Multiple Inheritance  ------------");
//         ExtraCurricularStudent ecs = new ExtraCurricularStudent("Ravi", 19, "103", "Cricket", "Painting");
//         ecs.DisplayExtraCurricularInfo();
//         Console.WriteLine();

//         // 5. Hybrid Inheritance
//         Console.WriteLine("--------------- Hybrid Inheritance ---------------");
//         ExtraCurricularGraduateStudent ecgs = new ExtraCurricularGraduateStudent("Anmol", 26, "104", "MBA", "Football", "Flute");
//         ecgs.DisplayFullProfile();
//     }
// }


// Polymorphism - overriding
// public abstract class PaymentMethod
// {
//     public abstract void processPayment(decimal amount);
// }

// public class CreditCardPayment : PaymentMethod
// {
//     public override void processPayment(decimal amount)
//     {
//         Console.WriteLine($"Processing Credit Card Payment of ${amount}");
//     }
// }
// public class PayPalPayment : PaymentMethod
// {
//     public override void processPayment(decimal amount)
//     {
//         Console.WriteLine($"Processing PayPal Payment of ${amount}");
//     }
// }
// public class CryptoPayment : PaymentMethod
// {
//     public override void processPayment(decimal amount)
//     {
//         Console.WriteLine($"Processing Crypto Payment of ${amount}");
//     }
// }
// public class PaymentProcessor
// {
//     public void process(PaymentMethod method, decimal amount)
//     {
//         method.processPayment(amount);
//     }
// }

// class Program
// {
//     public static void Main()
//     {
//         var processor = new PaymentProcessor();
//         PaymentMethod paymentMethod1 = new CreditCardPayment();
//         PaymentMethod paymentMethod2 = new PayPalPayment();
//         PaymentMethod paymentMethod3 = new CryptoPayment();

//         processor.process(paymentMethod1, 1000.25m);
//         processor.process(paymentMethod2, 1000.25m);
//         processor.process(paymentMethod3, 1000.25m);
//     }
// }

// Polymorphism - overloading
// class Employee
// {
//     public void PrintDetails()
//     {
//         Console.WriteLine("No employee details provided.");
//     }
//     public void PrintDetails(string name)
//     {
//         Console.WriteLine($"Employee Name: {name}");
//     }
//     public void PrintDetails(string name, int age)
//     {
//         Console.WriteLine($"Employee Name: {name}, Age: {age}");
//     }
//     public void PrintDetails(string name, int age, string department)
//     {
//         Console.WriteLine($"Employee Name: {name}, Age: {age}, Department: {department}");
//     }
// }
// class Program
// {
//     public static void Main()
//     {
//         Employee emp = new Employee();

//         emp.PrintDetails();
//         emp.PrintDetails("Akshat");
//         emp.PrintDetails("Akshat", 21);
//         emp.PrintDetails("Akshat", 21, "CSE");
//     }
// }


// -------------- DATABASE CONNECTION ----------------------------

// using System;
// using System.Linq.Expressions;
// using MySql.Data.MySqlClient;

// class Program
// {
//     static void Main()
//     {
//         // Connection string
//         string connectionString = "Server=localhost;Database=exl;User=root;Password=16122003";

//         using (MySqlConnection conn = new MySqlConnection(connectionString))
//         {
//             try
//             {
//                 conn.Open();
//                 Console.WriteLine("Successfully connected to MYSQL !");

//                 string query = "SELECT * FROM exl.person;";
//                 MySqlCommand cmd = new MySqlCommand(query, conn);

//                 MySqlDataReader reader = cmd.ExecuteReader();

//                 while (reader.Read())
//                 {
//                     Console.WriteLine($"ID: {reader["id"]}, Name: {reader["name"]}, Age: {reader["age"]}");
//                 }
//                 reader.Close();
//             }
//             catch (MySqlException err)
//             {
//                 Console.WriteLine($"Error : could not connect {err}");
//             }
//             finally
//             {
//                 conn.Close();
//                 Console.WriteLine("MySQL coonnection closed");
//             }
//         }
//     }
// }

// ------------------------ CRUD operations --------------------------

// using System;
// using MySql.Data.MySqlClient;

// class Program
// {
//     static string connectionString = "Server=localhost;Database=exl;User=root;Password=16122003";

//     public static void Main()
//     {
//         while (true)
//         {
//             Console.WriteLine("\n Choose your option: ");
//             Console.WriteLine("1. View all people");
//             Console.WriteLine("2. Add a new person ");
//             Console.WriteLine("3. Update an existing person ");
//             Console.WriteLine("4. Delete an existing person ");
//             Console.WriteLine("5. Exit ");

//             Console.Write("Your choice: ");
//             string choice = Console.ReadLine();
//             switch (choice)
//             {
//                 case "1":
//                     GetAllPeople();
//                     break;
//                 case "2":
//                     AddPerson();
//                     break;
//                 case "3":
//                     UpdatePerson();
//                     break;
//                 case "4":
//                     DeletePerson();
//                     break;
//                 case "5":
//                     return;
//                 default:
//                     Console.WriteLine("Error: choose correct option!");
//                     break;
//             }
//         }
//     }

//     public static void GetAllPeople()
//     {
//         using (var conn = new MySqlConnection(connectionString))
//         {
//             conn.Open();
//             string query = "SELECT * FROM exl.person;";
//             var cmd = new MySqlCommand(query, conn);
//             var reader = cmd.ExecuteReader();

//             Console.WriteLine("\nPeople in PERSON Table");
//             Console.WriteLine("ID |\t Age |\t Name");
//             Console.WriteLine("----------------------------");

//             while (reader.Read())
//             {
//                 Console.WriteLine($"{reader["id"]}\t{reader["age"]}\t{reader["name"]}");
//             }
//             reader.Close();
//         }
//     }

//     public static void AddPerson()
//     {
//         Console.Write("Enter your name: ");
//         string name = Console.ReadLine();

//         Console.Write("Enter your age: ");
//         int age = int.Parse(Console.ReadLine());

//         using (MySqlConnection conn = new MySqlConnection(connectionString))
//         {
//             conn.Open();
//             string query = "INSERT INTO exl.person (name, age) VALUES (@name, @age)";
//             var cmd = new MySqlCommand(query, conn);
//             cmd.Parameters.AddWithValue("@name", name);
//             cmd.Parameters.AddWithValue("@age", age);
//             cmd.ExecuteNonQuery();

//             // Get the last inserted ID
//             long insertedId = cmd.LastInsertedId;

//             Console.WriteLine("Person added successfully!");
//             Console.WriteLine();
//             Console.WriteLine($"New Person : ID: {insertedId}, Name: {name}, Age: {age}");
//         }
//     }

//     public static void UpdatePerson()
//     {
//         Console.Write("Enter person ID to update: ");
//         int id = int.Parse(Console.ReadLine());

//         Console.Write("Enter new name: ");
//         string name = Console.ReadLine();

//         Console.Write("Enter new age: ");
//         int age = int.Parse(Console.ReadLine());

//         using (var conn = new MySqlConnection(connectionString))
//         {
//             conn.Open();
//             string query = "UPDATE exl.person SET name = @name, age = @age WHERE id = @id;";
//             var cmd = new MySqlCommand(query, conn);
//             cmd.Parameters.AddWithValue("@name", name);
//             cmd.Parameters.AddWithValue("@id", id);
//             cmd.Parameters.AddWithValue("@age", age);
//             int rows = cmd.ExecuteNonQuery();

//             if (rows > 0)
//             {
//                 Console.WriteLine("Person updated successfully!");
//                 Console.WriteLine();
//                 Console.WriteLine($"Updated Person : ID: {id}, Name: {name}, Age: {age}");
//             }
//             else
//             {
//                 Console.WriteLine("Person NOT FOUND!");
//             }
//         }
//     }

//     public static void DeletePerson()
//     {
//         Console.Write("Enter person ID to delete: ");
//         int id = int.Parse(Console.ReadLine());

//         using (var conn = new MySqlConnection(connectionString))
//         {
//             conn.Open();

//             // First, fetch the person's details before deleting
//             string fetchQuery = "SELECT name, age FROM exl.person WHERE id = @id;";
//             var fetchCmd = new MySqlCommand(fetchQuery, conn);
//             fetchCmd.Parameters.AddWithValue("@id", id);

//             var reader = fetchCmd.ExecuteReader();

//             if (reader.Read())
//             {
//                 string name = reader["name"].ToString();
//                 int age = Convert.ToInt32(reader["age"]);
//                 reader.Close();

//                 // Now delete
//                 string deleteQuery = "DELETE FROM exl.person WHERE id = @id;";
//                 var deleteCmd = new MySqlCommand(deleteQuery, conn);
//                 deleteCmd.Parameters.AddWithValue("@id", id);
//                 deleteCmd.ExecuteNonQuery();

//                 Console.WriteLine("Person has been DELETED successfully!");
//                 Console.WriteLine();
//                 Console.WriteLine($"Deleted Person → ID: {id}, Name: {name}, Age: {age}");
//             }
//             else
//             {
//                 Console.WriteLine("Person NOT FOUND!");
//             }
//         }
//     }
// }

// ------------------------- TASK -------------------------------

// using System;
// using System.Data;
// using MySql.Data.MySqlClient;
// using System.Text.RegularExpressions;

// class Program
// {
//     static string connectionString = "Server=localhost;Database=exl;User=root;Password=16122003";
//     static MySqlConnection conn = new MySqlConnection(connectionString);
//     static string[] validStatuses = { "Pending", "In Progress", "Completed" };

//     static void Main()
//     {
//         while (true)
//         {
//             Console.WriteLine("\n1. Add New Employee");
//             Console.WriteLine("2. View All Employees");
//             Console.WriteLine("3. View by Status");
//             Console.WriteLine("4. View by Department");
//             Console.WriteLine("5. View by Joining Date Range");
//             Console.WriteLine("6. Update Employee");
//             Console.WriteLine("7. Delete Employee");
//             Console.WriteLine("0. Exit");

//             Console.Write("Choose an option: ");
//             string choice = Console.ReadLine();
//             switch (choice)
//             {
//                 case "1":
//                     AddEmployee();
//                     break;
//                 case "2":
//                     ViewAll();
//                     break;
//                 case "3":
//                     ViewByStatus();
//                     break;
//                 case "4":
//                     ViewByDepartment();
//                     break;
//                 case "5":
//                     ViewByDateRange();
//                     break;
//                 case "6":
//                     UpdateEmployee();
//                     break;
//                 case "7":
//                     DeleteEmployee();
//                     break;
//                 case "8":
//                     return;
//                 default:
//                     Console.WriteLine("Invalid choice.");
//                     break;
//             }
//         }
//     }
//     static void AddEmployee()
//     {
//         Console.Write("Full Name: ");
//         string name = Console.ReadLine();

//         string email;
//         while (true)
//         {
//             Console.Write("Email: ");
//             email = Console.ReadLine();
//             if (!Regex.IsMatch(email, @"^[^@\s]+@[^@\s]+\.[^@\s]+$"))
//             {
//                 Console.WriteLine("Invalid email format.");
//                 continue;
//             }
//             if (EmailExists(email))
//             {
//                 Console.WriteLine("Email already exists.");
//                 continue;
//             }
//             break;
//         }

//         Console.Write("Department: ");
//         string dept = Console.ReadLine();

//         DateTime joiningDate;
//         while (true)
//         {
//             Console.Write("Joining Date (yyyy-MM-dd): ");
//             if (DateTime.TryParse(Console.ReadLine(), out joiningDate) && joiningDate >= DateTime.Today)
//                 break;
//             Console.WriteLine("Invalid date. Must be today or later.");
//         }

//         string status;
//         while (true)
//         {
//             Console.Write("Status: (Pending/In Progress/Completed): ");
//             status = Console.ReadLine();
//             if (Array.Exists(validStatuses, s => s.Equals(status)))
//             {
//                 status = status.Trim();
//                 break;
//             }
//             Console.WriteLine("Invalid status.");
//         }

//         string query = "INSERT INTO employee_onboarding (full_name, email, department, joining_date, status) VALUES (@name, @mail, @dept, @joinDate, @status)";
//         using (MySqlCommand cmd = new MySqlCommand(query, conn))
//         {
//             cmd.Parameters.AddWithValue("@name", name);
//             cmd.Parameters.AddWithValue("@mail", email);
//             cmd.Parameters.AddWithValue("@dept", dept);
//             cmd.Parameters.AddWithValue("@joinDate", joiningDate.ToString("yyyy-MM-dd"));
//             cmd.Parameters.AddWithValue("@status", status);
//             conn.Open();
//             cmd.ExecuteNonQuery();
//             conn.Close();
//         }

//         Console.WriteLine("Employee added.");
//     }

//     static void ViewAll()
//     {
//         using (var conn = new MySqlConnection(connectionString))
//         {
//             conn.Open();
//             string query = "SELECT * FROM exl.employee_onboarding;";
//             var cmd = new MySqlCommand(query, conn);
//             var reader = cmd.ExecuteReader();

//             Console.WriteLine("\nPeople in Employee Table");
//             Console.WriteLine("Employee_ID |\t Full Name |\t Email |\t Department |\t Joining Date |\t Status");
//             Console.WriteLine("--------------------------------------------------------------------------------");

//             while (reader.Read())
//             {
//                 Console.WriteLine($"{reader["employee_id"]} | {reader["full_name"]} | {reader["email"]} | {reader["department"]} | {reader["joining_date"]:yyyy-MM-dd} | {reader["status"]}");
//             }
//             reader.Close();
//         }
//     }

//     static bool EmailExists(string email)
//     {
//         string query = "SELECT COUNT(*) FROM employee_onboarding WHERE email = @email";
//         using var cmd = new MySqlCommand(query, conn);
//         cmd.Parameters.AddWithValue("@email", email);
//         conn.Open();
//         long count = (long)cmd.ExecuteScalar();
//         conn.Close();
//         return count > 0;
//     }

//     static void ViewByStatus()
//     {
//         Console.Write("Enter status (Pending/In Progress/Completed): ");
//         string status = Console.ReadLine();
//         string query = "SELECT * FROM employee_onboarding WHERE status = @status";
//         using var cmd = new MySqlCommand(query, conn);
//         cmd.Parameters.AddWithValue("@status", status);
//         conn.Open();
//         using var reader = cmd.ExecuteReader();
//         Console.WriteLine("Employee_ID |\t Full Name |\t Email |\t Department |\t Joining Date |\t Status");
//         Console.WriteLine("--------------------------------------------------------------------------------");

//         while (reader.Read())
//         {
//             Console.WriteLine($"{reader["employee_id"]} | {reader["full_name"]} | {reader["email"]} | {reader["department"]} | {reader["joining_date"]:yyyy-MM-dd} | {reader["status"]}");
//         }
//         conn.Close();
//     }

//     static void ViewByDepartment()
//     {
//         Console.Write("Enter department: ");
//         string dept = Console.ReadLine();
//         string query = "SELECT * FROM employee_onboarding WHERE department = @dept";
//         using var cmd = new MySqlCommand(query, conn);
//         cmd.Parameters.AddWithValue("@dept", dept);
//         conn.Open();
//         using var reader = cmd.ExecuteReader();
//         Console.WriteLine("Employee_ID |\t Full Name |\t Email |\t Department |\t Joining Date |\t Status");
//         Console.WriteLine("--------------------------------------------------------------------------------");

//         while (reader.Read())
//         {
//             Console.WriteLine($"{reader["employee_id"]} | {reader["full_name"]} | {reader["email"]} | {reader["department"]} | {reader["joining_date"]:yyyy-MM-dd} | {reader["status"]}");
//         }
//         conn.Close();
//     }

//     static void ViewByDateRange()
//     {
//         Console.Write("Start date (yyyy-MM-dd): ");
//         string start = Console.ReadLine();
//         Console.Write("End date (yyyy-MM-dd): ");
//         string end = Console.ReadLine();
//         string query = "SELECT * FROM employee_onboarding WHERE joining_date BETWEEN @start AND @end";
//         using var cmd = new MySqlCommand(query, conn);
//         cmd.Parameters.AddWithValue("@start", start);
//         cmd.Parameters.AddWithValue("@end", end);
//         conn.Open();
//         using var reader = cmd.ExecuteReader();
//         Console.WriteLine("Employee_ID |\t Full Name |\t Email |\t Department |\t Joining Date |\t Status");
//         Console.WriteLine("--------------------------------------------------------------------------------");

//         while (reader.Read())
//         {
//             Console.WriteLine($"{reader["employee_id"]} | {reader["full_name"]} | {reader["email"]} | {reader["department"]} | {reader["joining_date"]:yyyy-MM-dd} | {reader["status"]}");
//         }
//         conn.Close();
//     }

//     static void UpdateEmployee()
//     {
//         Console.Write("Enter employee_id to update: ");
//         int employee_id = int.Parse(Console.ReadLine());

//         Console.Write("Update (1) Status (2) Department (3) Email (4) Name :");
//         string option = Console.ReadLine();

//         string column = "";
//         string newValue = "";

//         switch (option)
//         {
//             case "1":
//                 Console.Write("Enter new status: ");
//                 newValue = Console.ReadLine();
//                 if (!Array.Exists(validStatuses, s => s.Equals(newValue)))
//                 {
//                     Console.WriteLine("Invalid status.");
//                     return;
//                 }
//                 column = "status"; break;

//             case "2":
//                 Console.Write("Enter new department: ");
//                 newValue = Console.ReadLine();
//                 column = "department"; break;

//             case "3":
//                 Console.Write("Enter new email: ");
//                 newValue = Console.ReadLine();
//                 if (!Regex.IsMatch(newValue, @"^[^@\s]+@[^@\s]+\.[^@\s]+$"))
//                 {
//                     Console.WriteLine("Invalid email.");
//                     return;
//                 }
//                 if (EmailExists(newValue))
//                 {
//                     Console.WriteLine("Email already exists.");
//                     return;
//                 }
//                 column = "email"; break;

//             case "4":
//                 Console.Write("Enter new name: ");
//                 newValue = Console.ReadLine();
//                 column = "full_name";
//                 break;

//             default:
//                 Console.WriteLine("Invalid option.");
//                 return;
//         }

//         string query = $"UPDATE employee_onboarding SET {column} = @value WHERE employee_id = @employee_id";
//         using var cmd = new MySqlCommand(query, conn);
//         cmd.Parameters.AddWithValue("@value", newValue);
//         cmd.Parameters.AddWithValue("@employee_id", employee_id);
//         conn.Open();
//         int rows = cmd.ExecuteNonQuery();
//         conn.Close();

//         Console.WriteLine(rows > 0 ? "Update successful." : "No matching employee.");
//     }
    
//     static void DeleteEmployee()
//     {
//         Console.Write("Enter employee_id to delete: ");
//         int employee_id = int.Parse(Console.ReadLine());
//         Console.Write("Are you sure? (y/n): ");
//         if (Console.ReadLine() == "n")
//         {
//             Console.WriteLine("Deletion Cancelled.");
//             return;
//         }

//         string query = "DELETE FROM employee_onboarding WHERE employee_id = @employee_id";
//         using var cmd = new MySqlCommand(query, conn);
//         cmd.Parameters.AddWithValue("@employee_id", employee_id);
//         conn.Open();
//         int rows = cmd.ExecuteNonQuery();
//         conn.Close();
//         Console.WriteLine(rows > 0 ? "Deleted successfully." : "Employee not found.");
//     }
// }


// --------------------- HW Task: Product Inventory Tracker-----------------------------------
using System;
using System.Data;
using MySql.Data.MySqlClient;

class Program
{
    static string connStr = "Server=localhost;Database=exl;User=root;Password=16122003";
    static MySqlConnection conn = new MySqlConnection(connStr);

    static void Main()
    {
        while (true)
        {
            Console.WriteLine("\n------------------- Product Inventory Menu -----------------");
            Console.WriteLine("1. Add New Product");
            Console.WriteLine("2. View All Products");
            Console.WriteLine("3. Update Product (Price or Stock)");
            Console.WriteLine("4. Delete Product");
            Console.WriteLine("5. Show Products with Stock < 5");
            Console.WriteLine("6. Search Product by Name");
            Console.WriteLine("0. Exit");

            Console.Write("Choose an option: ");
            string choice = Console.ReadLine();
            switch (choice)
            {
                case "1":
                    AddProduct();
                    break;
                case "2":
                    ViewProducts();
                    break;
                case "3":
                    UpdateProduct();
                    break;
                case "4":
                    DeleteProduct();
                    break;
                case "5":
                    ShowLowStock();
                    break;
                case "6":
                    SearchProduct();
                    break;
                case "0":
                    return;
                default:
                    Console.WriteLine("Invalid choice.");
                    break;
            }
        }
    }

    static void AddProduct()
    {
        Console.Write("Product Name: ");
        string name = Console.ReadLine();

        Console.Write("Category: ");
        string category = Console.ReadLine();

        decimal price;
        while (true)
        {
            Console.Write("Price: ");
            price = decimal.Parse(Console.ReadLine());
            if (price < 0) // price validation
            {
                Console.WriteLine("Price must be a positive number.");
                break;
            }
            break;
        }
        int qty;
        while (true)
        {
            Console.Write("Stock Quantity: ");
            qty = int.Parse(Console.ReadLine());
            if (qty < 0) // qty validation
            {
                Console.WriteLine("Stock quantity cannot be negative.");
                break;
            }
            break;
        }
        string query = "INSERT INTO products (product_name, category, price, stock_qty) VALUES (@name, @cat, @price, @qty)";
        using var cmd = new MySqlCommand(query, conn);
        cmd.Parameters.AddWithValue("@name", name);
        cmd.Parameters.AddWithValue("@cat", category);
        cmd.Parameters.AddWithValue("@price", price);
        cmd.Parameters.AddWithValue("@qty", qty);
        conn.Open();
        cmd.ExecuteNonQuery();
        conn.Close();

        Console.WriteLine("Product added successfully.");
        Console.WriteLine($"{name} | {category} | {price} | {qty}");
    }

    static void ViewProducts()
    {
        string query = "SELECT * FROM products";
        using var cmd = new MySqlCommand(query, conn);
        conn.Open();
        using var reader = cmd.ExecuteReader();

        Console.WriteLine("\nProduct List:");
        Console.WriteLine("ID |\t Name |\t Category |\t Price |\t Stock");

        while (reader.Read())
        {
            Console.WriteLine($"{reader["product_id"]} | {reader["product_name"]} | {reader["category"]} | Rs.{reader["price"]:0.00} | {reader["stock_qty"]}");
        }
        conn.Close();
    }

    static void UpdateProduct()
    {
        Console.Write("Enter Product ID to update: ");
        int id = int.Parse(Console.ReadLine());

        Console.Write("Update (1) Price or (2) Stock? ");
        string option = Console.ReadLine();

        string column = "";
        object newValue = null;

        if (option == "1")
        {
            Console.Write("New Price: ");

            decimal price = decimal.Parse(Console.ReadLine());
            if (price <= 0)
            {
                Console.WriteLine("Invalid price.");
                return;
            }
            column = "price";
            newValue = price;
        }
        else if (option == "2")
        {
            Console.Write("New Stock Quantity: ");

            int qty = int.Parse(Console.ReadLine());
            if (qty < 0)
            {
                Console.WriteLine("Invalid quantity.");
                return;
            }
            column = "stock_qty";
            newValue = qty;
        }
        else
        {
            Console.WriteLine("Invalid option.");
            return;
        }

        string query = $"UPDATE products SET {column} = @value WHERE product_id = @id";
        using var cmd = new MySqlCommand(query, conn);
        cmd.Parameters.AddWithValue("@value", newValue);
        cmd.Parameters.AddWithValue("@id", id);
        conn.Open();
        int rows = cmd.ExecuteNonQuery();
        conn.Close();

        Console.WriteLine(rows > 0 ? "Update successful." : "Product not found.");
    }

    static void DeleteProduct()
    {
        Console.Write("Enter Product ID to delete: ");
        int id = int.Parse(Console.ReadLine());

        Console.Write("Are you sure? (y/n): ");
        if (Console.ReadLine() == "n")
        {
            Console.WriteLine("Deletion cancelled");
            return;
        } 

        string query = "DELETE FROM products WHERE product_id = @id";
        using var cmd = new MySqlCommand(query, conn);
        cmd.Parameters.AddWithValue("@id", id);
        conn.Open();
        int rows = cmd.ExecuteNonQuery();
        conn.Close();

        Console.WriteLine(rows > 0 ? "Product deleted." : "Product not found.");
    }

    static void ShowLowStock()
    {
        string query = "SELECT * FROM products WHERE stock_qty < 5";
        using var cmd = new MySqlCommand(query, conn);
        conn.Open();
        using var reader = cmd.ExecuteReader();

        Console.WriteLine("\nLow Stock Products (<5):");
        Console.WriteLine("ID |\t Name |\t Category |\t Price |\t Stock");

        while (reader.Read())
        {
            Console.WriteLine($"{reader["product_id"]} | {reader["product_name"]} | {reader["category"]} | Rs.{reader["price"]:0.00} | {reader["stock_qty"]}");
        }
        conn.Close();
    }

    static void SearchProduct()
    {
        Console.Write("Enter product name to search: ");
        string name = Console.ReadLine();

        string query = "SELECT * FROM products WHERE product_name LIKE @name";
        using var cmd = new MySqlCommand(query, conn);
        cmd.Parameters.AddWithValue("@name", name);

        conn.Open();
        using var reader = cmd.ExecuteReader();

        Console.WriteLine("\nSearch Results:");
        Console.WriteLine("ID |\t Name |\t Category |\t Price |\t Stock");

        while (reader.Read())
        {
            Console.WriteLine($"{reader["product_id"]} | {reader["product_name"]} | {reader["category"]} | Rs.{reader["price"]:0.00} | {reader["stock_qty"]}");
        }
        conn.Close();
    }
}
