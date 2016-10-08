using System;

namespace Algorythms
{
    public static class lesson_1_1_4
    {
        public static void test()
        {
            string input = Console.ReadLine();
            int x1;
            int y1;
            if (int.TryParse(input[0].ToString(), out x1) && int.TryParse(input[2].ToString(), out y1))
            {
                int result = x1 + y1;
                Console.WriteLine(result);
            }
            Console.ReadLine();
        }
    }
}
