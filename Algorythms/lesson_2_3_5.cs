using System;

namespace Algorythms
{
    /*По данным двум числам 1≤a,b≤2⋅10^9 найдите их наибольший общий делитель.*/
    class lesson_2_3_5
    {
        public static void GetGCD()
        {
            string input = Console.ReadLine();
            string[] parameters = input.Split(' ');
            int n;
            int m;
            int.TryParse(parameters[0], out n);
            int.TryParse(parameters[1], out m);
            Console.WriteLine(EuAlg(n, m));
        }
        private static int EuAlg(int a, int b)
        {
            if (a == 0) return b;
            if (b == 0) return a;
            if (a >= b) return EuAlg(a % b, b);
            if (b >= a) return EuAlg(a, b % a);
            return -1;//тут костыль.
        }
    }
}
