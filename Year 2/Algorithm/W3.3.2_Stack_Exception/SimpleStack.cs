//-----This file HAS to be modified----

using System.Drawing;

public class SimpleStack<T>
{
    protected T?[] arr;
    protected int top;
    protected int usage;
    public int Capacity { get; protected set; }
    
    public SimpleStack()
    {
        Capacity = 4;
        arr = new T[Capacity];
        top = -1;
    }
    public bool IsEmpty() => top == -1;
    public bool IsFull() => top == Capacity - 1;
    
    public void Push(T item) //change something here
    {
        if (IsFull())
        {
            T[] newArray = new T[arr.Length * 2];
            for (int i = 0; i < arr.Length; i++)
            {
                newArray[i] = arr[i];
            }
            arr = newArray;
        }

        arr[++top] = item;
        usage++;
    }
    public T? Peek()        //change something here
    {
        return !IsEmpty() ? arr[top] : throw new StackEmptyException("The Stack is empty.");

    }

    public T? Pop() //change something here
    {
        if (!IsEmpty())
        {
            usage--;
            return arr[top--];
        }

        throw new StackEmptyException("The Stack is empty.");
    }
}