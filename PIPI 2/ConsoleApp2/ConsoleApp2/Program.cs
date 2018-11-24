using System;

class MainClass
{
    public static void Main(string[] args)
    {
        Random nume = new Random();
        int num01 = nume.Next(1, 11);
        int num02 = nume.Next(1, 11);

        Console.WriteLine("What is " + num01 + " times " + num02 + "?");
        int answer = Convert.ToInt32(Console.ReadLine());
        if (answer == num01 * num02)
        {

            Console.WriteLine("ESTI DESTEP COAIEMIU");

        }
        else
        {
            int response = nume.Next(1, 4);

            Console.WriteLine("BA DA PROSET ESTI");

        }
        Console.ReadKey();




    }
}