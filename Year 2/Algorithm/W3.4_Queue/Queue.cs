namespace Solution;

public class Queue<T> : IQueue<T>
{
    private int front;
    private int back;
    private T[] data;
    private int _count = 0;

    public bool Empty => _count == 0;
    public bool Full => _count == Size - 1;
    public int Count => _count;
    public int Size => data.Length;

    public Queue(int capacity = 5)
    {
        data = new T[capacity];
    }

    public void Enqueue(T element)
    {
        if (Empty)
        {
            front = back = 0;
            data[back] = element;
            _count++;
            return;
        }
        if (Full)
        {
            T[] newArray = new T[data.Length * 2];
            for (int i = 0; i < data.Length; i++)
            {
                newArray[i] = data[i];
            }
            data = newArray;
            data[back + 1] = element;
            back++;
            _count++;
            return;
        }
        
        data[back + 1] = element;
        back++;
    }

    public T? Dequeue()
    {
        if (Empty)
        {
            return default;
        }
        
        T element = data[front];
        for (int i = 0; i < Size - 1; i++)
        {
            data[i] = data[i + 1];
        }

        if (data[back] != null || back > 0)
        {
            data[back] = default;
            back--; 
        }

        return element;
    }

}