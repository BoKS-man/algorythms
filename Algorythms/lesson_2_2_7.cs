using System;

namespace Algorythms
{
    /*Дано число 1≤n≤10^7, необходимо найти последнюю цифру n-го числа Фибоначчи.
    Как мы помним, числа Фибоначчи растут очень быстро, поэтому при их вычислении
    нужно быть аккуратным с переполнением.В данной задаче, впрочем,
    этой проблемы можно избежать, поскольку нас интересует только
    последняя цифра числа Фибоначчи: если 0≤a,b≤9 — последние цифры чисел Fi и Fi+1
    соответственно, то (a+b)mod10 — последняя цифра числа Fi+2.*/
    class lesson_2_2_7
    {
        public static void Main()
        {
            string input = Console.ReadLine();
            long n;
            if (long.TryParse(input.ToString(), out n))
            {
                long[] fibArr = new long[n + 1];
                for (int i = 0; i <= n; i++)
                {
                    if (i < 2)
                    {
                        fibArr[i] = i;
                        continue;
                    }
                    fibArr[i] = (fibArr[i - 1] + fibArr[i - 2]) % 10;
                }
                Console.WriteLine(fibArr[n]);
            }
            Console.ReadLine();
        }
    }
}