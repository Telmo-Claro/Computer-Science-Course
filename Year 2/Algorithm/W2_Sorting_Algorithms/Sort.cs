namespace ToDo;

public class Sort<T> : ISort<T> where T : IComparable<T>
{
    public static void InsertionSort(T[] data)
    {
        for(int i = 1; i < data.Length; i++)
        {
            T temp = data[i];
            int j = i - 1; // keeps track of the value on the left of temp
            while (j >= 0 && data[j].CompareTo(temp) > 0)
            {
                data[j + 1] = data[j];
                j--;
            }
            data[j + 1] = temp;
        }
    }

    public static void BubbleSort(T[] data)
    {
        for(int i = 0; i < data.Length - 1; i++)
        {
            for(int j = 0; j < data.Length - i - 1; j++)
            {
                if(data[j].CompareTo(data[j + 1]) > 0)
                {
                    T temp = data[j];
                    data[j] = data[j + 1];
                    data[j + 1] = temp;
                }
            }
        }
    }

    public static void MergeSort(T[] array, int left, int right)
    {
        if (left < right)
        {
            int middle = left + (right - left) / 2;

            MergeSort(array, left, middle);
            MergeSort(array, middle + 1, right);

            Merge(array, left, middle, right);
        }
    }

    public static void Merge(T[] array, int left, int middle, int right)
    {
        var leftSize = middle - left + 1;
        var rightSize = right - middle;
        var arrayLeft = new T[leftSize];
        var arrayRight = new T[rightSize];

        int i = 0;
        int j = 0;

        for (i = 0; i < leftSize; ++i) 
        {
            arrayLeft[i] = array[left + i];
        }
        for (j = 0; j < rightSize; ++j)
        {
            arrayRight[j] = array[middle + 1 + j];
        }

        i = 0;
        j = 0;
        int k = left;

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