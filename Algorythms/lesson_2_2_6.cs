using System;

namespace Algorythms
{
    class lesson_2_2_6
    {
        public static void GetFibNum()
        {
            string input = Console.ReadLine();
            long n;
            if (long.TryParse(input.ToString(), out n))
            {
                long[] fibArr = new long[n+1];
                for (int i = 0; i <= n; i++)
                {
                    if (i < 2)
                    {
                        fibArr[i] = i;
                        continue;
                    }
                    fibArr[i] = fibArr[i - 1] + fibArr[i - 2];
                }
                Console.WriteLine(fibArr[n]);
            }
            Console.ReadLine();
        }
    }
}
