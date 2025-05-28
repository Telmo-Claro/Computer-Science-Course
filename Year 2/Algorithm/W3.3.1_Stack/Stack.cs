namespace Solution;

public class Stack<T> : IStack<T>
{
    private T[] array;
    private int top;
    private int usage;

    public bool Empty => top == -1;

    public bool Full => top == Size - 1;

    public int Count => usage;

    public int Size => array.Length;

    public Stack(int size = 4)
    {
        array = new T[size];
        top = -1;
        usage = 0;
    }

    public T? Peek()
    {
        return !Empty ? array[top] : default(T);
    }

    public T? Pop()
    {
        if (!Empty)
        {

        }
        return default(T);
    }


    public void Push(T Item)
    {
        if (Full)
        {
            T[] newArray = new T[array.Length * 2];
            for (int i = 0; i < array.Length; i++)
            {
                newArray[i] = array[i];
            }
            array = newArray;
        }

        array[++top] = Item;
        usage++;
    }
}