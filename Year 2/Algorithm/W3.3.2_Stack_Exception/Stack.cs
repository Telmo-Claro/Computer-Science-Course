//-----This file HAS to be modified----

public class Stack<T> : SimpleStack<T>
{
    public Stack() : base()
    {
    }

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