using System.Numerics;

namespace ToDo;

public class MultiArray : IMultiArray
{
    public static T[]? RowSum<T>(T[,] arr2D) where T : INumber<T>
    {
        T[] results = new T[arr2D.GetLength(0)];
        for(int i = 0; i < arr2D.GetLength(0); i++)
        {
            for (int j = 0; j < arr2D.GetLength(1); j++)
            {
                results[i] += arr2D[i, j];
            }
        }
        return results;
    }
    public static T[]? ColSum<T>(T[,] arr2D) where T : INumber<T>
    {
        T[] results = new T[arr2D.GetLength(0)];
        for(int i = 0; i < arr2D.GetLength(0); i++)
        {
            for (int j = 0; j < arr2D.GetLength(i); j++)
            {
                results[i] += arr2D[j, i];
            }
        }
        return results;
    }

    public static Tuple<int, T>? MaxRowIndexSum<T>(T[][] arrJagged) where T : INumber<T>
    {
        //MaxRowIndexSum finds the index of the row with the maximum sum in a jagged array.
        //returns a Tuple<int, T> where: the first item is the index of the row with the maximum sum and the second item is the sum of that row.
        int maxIndex = 0;
        T maxSum = default;
        for (int i = 0; i < arrJagged.Length; i++)
        {
            T rowSum = default;
            for (int j = 0; j < arrJagged[i].Length; j++)
            {
                rowSum += arrJagged[i][j];
            }
            if (rowSum > maxSum)
            {
                maxSum = rowSum;
                maxIndex = i;
            }
        }
        return new Tuple<int, T>(maxIndex, maxSum);
    }

    public static T?[] MaxCol<T>(T[][] arrJagged) where T : INumber<T>
    {
        // Get the highest index of the inner arrays
        int highestIndex = 0;
        for (int i = 0; i < arrJagged.Length; i++)
        {
            if (arrJagged[i] != null)
            {
                highestIndex = arrJagged[i].Length > highestIndex ? arrJagged[i].Length : highestIndex;
            }
        }

        T[] arrMaxCol = new T[arrJagged.Length]; // Creates the return array with the highest index
        T maxColSum = default; // the total sum of the highest column
        int indexTracker = -1; // tracks the index of which column has the highest sum

        for (int i = 0; i < highestIndex; i++)
        {
            T tempSum = default;
            for (int j = 0; j < arrJagged.Length; j++)
            {
                if (arrJagged[j] != null && arrJagged[j].Length > 0 && arrJagged[j].Length > i)
                {
                    tempSum += arrJagged[j][i];
                }
            }

            if (tempSum > maxColSum)
            {
                maxColSum = tempSum;
                indexTracker = i;
            }
        }

        for (int i = 0; i < highestIndex; i++)
        {
            if (arrJagged[i] != null && arrJagged[i].Length > 0 && arrJagged[i].Length > indexTracker)
            {
                arrMaxCol[i] = arrJagged[i][indexTracker];
            }
            else
            {
                arrMaxCol[i] = default;
            }
        }

        return arrMaxCol;
    }

    public static T[][]? Split<T>(Tuple<T, T, T>[] input)
    {
        //ToDo
        throw new NotImplementedException();
    }

    public static T[,]? Zip<T>(T[] a, T[] b)
    {
        //ToDo
        throw new NotImplementedException();
    }
}