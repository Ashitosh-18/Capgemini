using System;
using System.Collections.Generic;
using System.IO;

class Program
{
    // Class and Object (OOP)
    class Person
    {
        public string Name { get; set; }
        public int Age { get; set; }

        // Constructor
        public Person(string name, int age)
        {
            Name = name;
            Age = age;
        }

        // Method to display details
        public void Display()
        {
            Console.WriteLine($"Name: {Name}, Age: {Age}");
        }
    }

    // Function with parameters and return type
    static int AddNumbers(int a, int b)
    {
        return a + b;
    }

    static void Main()
    {
        // 1️⃣ Taking Runtime Input
        Console.Write("Enter your name: ");
        string name = Console.ReadLine();

        Console.Write("Enter your age: ");
        int age = Convert.ToInt32(Console.ReadLine());

        // 2️⃣ Creating an Object
        Person person = new Person(name, age);
        Console.WriteLine("\nPerson Details:");
        person.Display();

        // 3️⃣ Conditional Statement
        if (age >= 18)
        {
            Console.WriteLine("You are an adult.");
        }
        else
        {
            Console.WriteLine("You are a minor.");
        }

        // 4️⃣ Looping (For Loop)
        Console.WriteLine("\nCounting from 1 to 5:");
        for (int i = 1; i <= 5; i++)
        {
            Console.Write(i + " ");
        }
        Console.WriteLine();

        // 5️⃣ Using Arrays
        int[] numbers = { 10, 20, 30, 40, 50 };
        Console.WriteLine("\nArray Elements:");
        foreach (var num in numbers)
        {
            Console.Write(num + " ");
        }
        Console.WriteLine();

        // 6️⃣ Using Lists
        List<string> colors = new List<string> { "Red", "Blue", "Green" };
        colors.Add("Yellow");
        Console.WriteLine("\nList of Colors:");
        foreach (var color in colors)
        {
            Console.Write(color + " ");
        }
        Console.WriteLine();

        // 7️⃣ Using Dictionary
        Dictionary<string, int> studentMarks = new Dictionary<string, int>
        {
            { "Alice", 85 },
            { "Bob", 90 },
            { "Charlie", 78 }
        };
        Console.WriteLine("\nStudent Marks:");
        foreach (var kvp in studentMarks)
        {
            Console.WriteLine($"{kvp.Key}: {kvp.Value}");
        }

        // 8️⃣ Exception Handling
        try
        {
            Console.Write("\nEnter a number to divide 100 by: ");
            int divisor = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine($"Result: {100 / divisor}");
        }
        catch (DivideByZeroException)
        {
            Console.WriteLine("Error: Cannot divide by zero!");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Unexpected error: {ex.Message}");
        }

        // 9️⃣ File Handling (Writing and Reading a File)
        string filePath = "data.txt";
        File.WriteAllText(filePath, "Hello, this is a test file!");
        Console.WriteLine($"\nFile Created: {filePath}");

        string fileContent = File.ReadAllText(filePath);
        Console.WriteLine($"File Content: {fileContent}");

        // 🔟 Using Functions
        int sum = AddNumbers(10, 20);
        Console.WriteLine($"\nSum of 10 and 20: {sum}");

        Console.WriteLine("\nProgram Completed Successfully!");
    }
}
