using System.Numerics;

namespace ToDo;

public class MultiArray : IMultiArray
{
    public static T[]? RowSum<T>(T[,] arr2D) where T : INumber<T>
    {        
        var toReturn = new T[arr2D.GetLength(0)];

        for(int i = 0; i < arr2D.GetLength(0); i++)
        {
            T count = default;
            for(int j = 0; j < arr2D.GetLength(1); j++)
            {
                count += arr2D[i, j];
            }
            toReturn[i] = count;
        }
        return toReturn;
    }

    public static T[]? ColSum<T>(T[,] arr2D) where T : INumber<T>
    {        
        T[] toReturn = new T[arr2D.GetLength(1)];

        for(int i = 0; i < arr2D.GetLength(1); i++)
        {
            T count = default;
            for(int j = 0; j < arr2D.GetLength(0); j++)
            {
                count += arr2D[j, i];
            }
            toReturn[i] = count;
        }
        return toReturn;
    }

    public static Tuple<int, T>? MaxRowIndexSum<T>(T[][] arrJagged) where T : INumber<T>
    { 
        int indexToReturn = 0;
        T tToReturn = default;

        for(int i = 0; i < arrJagged.Length; ++i)
        {
            int tempMaxIndex = 0;
            T rowSum = default;
            for(int j = 0; j < arrJagged[i].Length; ++j)
            {
                rowSum += arrJagged[i][j];
            }
            if(rowSum > tToReturn)
            {
                indexToReturn = i;
                tToReturn = rowSum;
            }
        }

        return new Tuple<int,T>(indexToReturn,tToReturn);
    }

    public static T?[] MaxCol<T>(T[][] arrJagged) where T : INumber<T>
    {        
        //ToDo
        T[] arrToReturn = new T[arrJagged.Length];
        int intOfHighestCol = 0;
        T totalOfCol = default;
        
        // Finding the index with the highest sum
        for(int i = 0; i < arrJagged.Length; i++)
        {
            T tempTotalOfCol = default;
            for(int j = 0; j < arrJagged[i].Length; i++)
            {
                tempTotalOfCol += arrJagged[j][i];
            }
            intOfHighestCol = tempTotalOfCol > totalOfCol ? i : intOfHighestCol;
        }

        for(int i = 0; i < arrJagged.Length; i++)
        {
            if(arrJagged[i][intOfHighestCol] is null || arrJagged[i].Length < intOfHighestCol)
            {
                arrToReturn[i] = default;
            }
            else
            {
                arrToReturn[i] = arrJagged[i][intOfHighestCol];
            }
        }
        return arrToReturn;
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