//using Solution;
using ToDo;

class MainClass
{
    static void Main()
    {
        DebugArray();
    }
  
    static void DebugArray()
    {
        var data = new int[,] { { 1, 2, 3, 4 }, { 5, 6, 7, -8 }, { 9, 10, 11, 12 } };
        var actualValue = MultiArray.RowSum(data);
        var expectedValue = new int[] { 10, 10, 42 };
        int count = 0;
        foreach (var i in actualValue)
        {
            Console.WriteLine("Actual: " + actualValue[count]);
            Console.WriteLine("Expected: " + expectedValue[count]);
            count++;
        }
        int[][] arr = new int[3][];

        // Initializing each row of the jagged array

        // First row
        arr[0] = new int[] { 1, 2, 3, 4};
        // Second row
        arr[1] = new int[] { 4, 5, 6 };
        // Third row (only two elements)
        arr[2] = new int[] { 7, 8 };

        var maxRowIndex = MultiArray.MaxRowIndexSum(arr);
        Console.WriteLine(maxRowIndex);

        var newArr = new int[][]{
            new int[] {3, 21, 34, 34},
            new int[] {21, 0, 34},
            new int[] {3, 21, 34, 34, 45, -12, 11},
            null,
            new int[0],
            new int[] {3, 21}
        };

        var maxCol = MultiArray.MaxCol(newArr);
        Console.WriteLine(maxCol);
    }
}