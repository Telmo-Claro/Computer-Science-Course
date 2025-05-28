namespace Solution;

public class Q1
{
    public static long Tribonacci(long n, long[] mem){
        Utils.ShowCallStack(false); //DO NOT comment this line of code
        //ToDo 1: Tribonacci via Dynamic programming
        if(mem is null || mem.Length <= n)
        {
            mem = new long[n + 1];
            mem[0] = 0;
            mem[1] = 0;
            mem[2] = 1;
        }
        if(mem[n] != 0)
            return mem[n];
        
        if(n is 0 or 1)
            return 0;

        mem[n] = Tribonacci(n - 1, mem) + Tribonacci(n - 2, mem) + Tribonacci(n - 3, mem);
        return mem[n];
    }
}