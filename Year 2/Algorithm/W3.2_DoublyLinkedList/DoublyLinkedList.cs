using System.Collections;

namespace Solution;

public class DoublyLinkedList<T> : IDoublyLinkedList<T> where T : IComparable<T>
{
    public DoubleNode<T>? First, Last;
    public DoublyLinkedList() => First = Last = null;
    
    public void Clear() => First = Last = null;

    //Search
    public DoubleNode<T>? Search(T value)
    {
        var newNode = new DoubleNode<T>(value);
        if (First.Value.CompareTo(newNode.Value) == 0)
        {
            return First;
        }

        var current = First;
        while (current.Next != null && current.Value.CompareTo(value) != 0)
        {
            current = current.Next;
        }
        
        return current;
    }

    #region "addNode=> first, last, sorted" 

    public void AddFirst(T value)
    {
        DoubleNode<T> newNode = new DoubleNode<T>(value);
        if (First == null)
        {
            First = newNode;
            Last = newNode;
        }
        else
        {
            First.Previous = newNode;
            newNode.Next = First;
            First = newNode;
        }
    }

    public void AddLast(T value)
    {
        DoubleNode<T> newNode = new DoubleNode<T>(value);
        if (Last == null)
        {
            Last = newNode;
            if(First is null)
            {
                First = newNode;
            }
        }
        else
        {
            newNode.Previous = Last;
            Last.Next = newNode;
            Last = newNode;
        }
    }

    public void AddSorted(T value)
    {
        DoubleNode<T> newNode = new DoubleNode<T>(value);

        if (First == null || First.Value.CompareTo(value) >= 0)
        {
            if (First is null)
            {
                First = newNode;
                Last = newNode;
            }
            else
            {
                First.Previous = newNode;
                newNode.Next = First;
                First = newNode;
            }
        }
        else
        {
            var current = First;
            while (current.Next != null && current.Next.Value.CompareTo(value) <= 0)
            {
                current = current.Next;
            }
            if(current.Next == null)
            {
                newNode.Previous = Last;
                Last.Next = newNode;
                Last = newNode;
            }
            else
            {
                newNode.Previous = current;
                newNode.Next = current.Next;
                current.Next.Previous = newNode;
                current.Next = newNode; 
            }
        }
    }
    #endregion

    public bool Remove(T value)
    {
        if (First == null)
        {
            return false;
        }

        var current = First;
        while (current != null && current.Value.CompareTo(value) != 0)
        {
            current = current.Next;
        }

        if (current == null)
        {
            return false;
        }

        if (current == First)
        {
            First = First.Next;
            if (First != null)
            {
                First.Previous = null;
            }
            else
            {
                Last = null;
            }
            return true;
        }

        if (current == Last)
        {
            Last = Last.Previous;
            if (Last != null)
            {
                Last.Next = null;
            }
            else
            {
                First = null;
            }
            return true;
        }

        current.Previous.Next = current.Next;
        current.Next.Previous = current.Previous;
        return true;
    }

    public void Delete(DoubleNode<T> node)
    {
        // check Prev
        // check Next
        // check First
        // check Last
        throw new NotImplementedException();
     
    }

    public IEnumerator<T> GetEnumerator()
    {
        var current = First;
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