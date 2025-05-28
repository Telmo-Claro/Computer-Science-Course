using System.Collections;

namespace Solution;

public class SinglyLinkedList<T> : ILinkedList<T> where T : IComparable<T>
{
    public SingleNode<T>? Head;
    private int count;

    public SinglyLinkedList()
    {
        Head = null;
        count = 0;
    }

    public int Count => count;

    public void AddFirst(T value)
    {
        SingleNode<T>? newNode = new SingleNode<T>(value);
        if (Head == null)
        {
            Head = newNode;
        }
        else
        {
            var current = Head;
            Head = newNode;
            Head.Next = current;
        }
        count++;
    }

    public void AddLast(T value)
    {
        SingleNode<T>? newNode = new SingleNode<T>(value);

        if (Head == null)
        {
            Head = newNode;
        }
        else
        {
            var current = Head;
            while (current.Next != null)
            {
                current = current.Next;
            }
            current.Next = newNode;   
        }

        count++;
    }

    public bool Remove(T value)
    {
        if (Head == null || Head.Value.CompareTo(value) > 0)
        {
            return false;
        }

        if (Head.Value.CompareTo(value) == 0)
        {
            Head = Head.Next;
            count--;
            return true;
        }
        
        var current = Head;
        while (current.Next != null && current.Next.Value.CompareTo(value) <= 0)
        {
            if (current.Next.Value.CompareTo(value) == 0)
            {
                current.Next = current.Next.Next;
                count--;
                return true;
            }
            current = current.Next;
        }
        return false;
    }

    public SingleNode<T>? Search(T value)
    {
        var current = Head;
        while (current != null && current.Value.CompareTo(value) != 0)
        {
            current = current.Next;
        }
        return current;
    }

    public bool Contains(T value)
    {
        if (Head == null)
        {
            return false;
        }

        if (Head.Value.CompareTo(value) == 0)
        {
            return true;
        }
        
        var current = Head;
        while (current != null)
        {
            if (current.Value.CompareTo(value) == 0)
            {
                return true;
            }
            current = current.Next;
        }
        return false;
    }

    public void AddSorted(T value)
    {
        var newNode = new SingleNode<T>(value);
        if (Head == null || Head.Value.CompareTo(value) >= 0)
        {
            if (Head == null)
            {
                Head = newNode;
            }
            else
            {
                var current = Head;
                Head = newNode;
                Head.Next = current;
            }
        }
        else
        {
            var current = Head;
            while (current.Next != null && current.Next.Value.CompareTo(value) < 0)
            {
                current = current.Next;
            }
            current.Next = new SingleNode<T>(value, current.Next);
        }
        
        count++;
    }

    public void Clear()
    {
        Head = null;
    }

    public IEnumerator<T> GetEnumerator()
    {
        SingleNode<T>? current = Head;
        while (current != null)
        {
            yield return current.Value;
            current = current.Next;
        }
    }

    IEnumerator IEnumerable.GetEnumerator()
    {
        return GetEnumerator();
    }

}