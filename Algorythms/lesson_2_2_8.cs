﻿using System;
using System.Collections.Generic;

namespace Algorythms
{
    /*Даны целые числа 1≤n≤10^18 и 2≤m≤10^5, необходимо найти остаток от деления 
    n-го числа Фибоначчи на m.*/
    class lesson_2_2_8
    {
        public static void GetFibMod()
        {
            string input = Console.ReadLine();
            string[] parameters = input.Split(' ');
            long n;
            long m;
            if (parameters.Length == 2 &&
                long.TryParse(parameters[0], out n) &&
                long.TryParse(parameters[1], out m))
            {
                long fib0 = 0;
                long fib1 = 1;
                var fibArr = new List<long> { fib0, fib1 };
                do
                {

                    long fibOld = fib1;
                    fib1 = (fib1 + fib0) % m;
                    fib0 = fibOld;
                    fibArr.Add(fib1);
                }
                while ((fib0 != 0 || fib1 != 1));
                int offset = int.Parse((n % (fibArr.Count - 2)).ToString());
                Console.WriteLine(fibArr[offset]);
            }
            Console.ReadLine();
        }
    }
}