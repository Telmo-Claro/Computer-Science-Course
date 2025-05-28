namespace ToDo;
public class Sort<T> : ISort<T> where T : IComparable<T>
{
    public static void BubbleSort(T[] data)
    {
        var n = data.Length;
        for(int i = 0; i < n - 1; i++)
        {
            for(int j = 0; j < n - i - 1; j++)
            {
                if(data[j].CompareTo(data[j + 1]) > 0)
                {
                    (data[j], data[j + 1]) = (data[j + 1], data[j]);
                }
            }
        }
    }

    public static void InsertionSort(T[] data)
    {
        for(int i = 1; i < data.Length; i++)
        {
            var key = data[i];
            var flag = 0;
            for(int j = i - 1; j >= 0 && flag != 1;)
            {
                if(key.CompareTo(data[j]) < 0)
                {
                    data[j + 1] = data[j];
                    j--;
                    data[j + 1] = key;
                }
                else
                {
                    flag = 1;
                }
            }
        }
    }

    public static void MergeSort(T[] array, int low, int high)
    {
        if (low < high)
        {
            int middle = low + (high - low) / 2;

            MergeSort(array, low, middle);
            MergeSort(array, middle + 1, high);

            Merge(array, low, middle, high);
        }
    }

    public static void Merge(T[] array, int low, int middle, int high) // q p r
    {
        var leftSize = middle - low + 1;
        var rightSize = high - middle;
        var arrayLeft = new T[leftSize];
        var arrayRight = new T[rightSize];

        int i = 0;
        int j = 0;

        for (i = 0; i < leftSize; ++i) 
        {
            arrayLeft[i] = array[low + i];
        }
        for (j = 0; j < rightSize; ++j)
        {
            arrayRight[j] = array[middle + 1 + j];
        }

        i = 0;
        j = 0;
        int k = low;

        while(i < leftSize && j < rightSize)
        {
            if(arrayLeft[i].CompareTo(arrayRight[j]) <= 0)
            {
                array[k++] = arrayLeft[i++];
            }
            else
            {
                array[k++] = arrayRight[j++];
            }
        }

        while (i < leftSize)
        {
            array[k++] = arrayLeft[i++];
        }

        while (j < rightSize)
        {
            array[k++] = arrayRight[j++];
        }
    }
}