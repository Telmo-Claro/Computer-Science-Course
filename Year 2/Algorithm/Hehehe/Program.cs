// public int SequentialSearch(T[] array, T target)
// {
//     if(array is null || array.Length <= 0)
//     {
//         return -1;
//     }
//     for(int i = 0; i < array.Length; i++)
//     {
//         if(array[i].CompareTo(target) == 0)
//         {
//             return 1;
//         }\
//     }
//     return -1;
// }
//
// public int BinarySearch(T[] array, T target)
// {
//     int left = 0;
//     int right = array.Length - 1;
// 	
//     while(left <= right)
//     {
//         int mid = (left + right) / 2;
// 		
//         if(arr[mid].CompareTo(target) )
//             return mid;
// 		
//         if(arr[mid] < target)
//             left = mid + 1;
//         else
//             right = mid - 1;
//     }
//     return -1;
// }
//
// public void InsertionSort(T[] array)
// {
//     for(int i = 0; i < array.Length; i++)
//     {
//         T key = array[i];
//         j = i - 1;
// 		
//         while(j >= 0 && array[j] > key) // While the value being compared is larger than 0 and larger than the temp key.
//         {
//             array[j + 1] = array[j]; // Shift the elements to the right.
//             j--; // goes left of the array!
//         }
//         array[j + 1] = key; // puts the temp value in its place.
//     }
// }
//
// public void BubbleSort(T[] array)
// {
//     int n = array.Length
//     bool swapped = false;
//     for(int i = 0; i < n; i++)
//     {
//         for(int j = 0; j < n - i - 1; j++)
//         {
//             if(array[j] > arr[j + 1])
//             {
//                 var temp = arr[j];
//                 array[j] = array[j + 1];
//                 array[j + 1] = temp;
//                 swapped = true;
//             }
//         }
//         if(!swapped)
//             break;
//     }
// }
//
// public void MergeSort(T[] array)
// {
//     if (arr.Length <= 1)
//         return;
//
//     // Creates arrays for left and right.
//     int mid = array.Lenght / 2;
//     T[] left = new T[mid];
//     T[] right = new T[array.Lenght - mid];
//
//     // Copy elements
//     for(int i = 0; i < mid; i++)
//     {
//         left[i] = array[i];
//     }
//     for(int i = mid; i < arr.Length; i++)
//     {
//         right[i - mid] = array[i];
//     }
//
//     // Recursively sorting halves
//     MergeSort(left);
//     MergeSort(right);
//
//     Merge(array, left, right);
// }
//
// public void Merge(T[] array, T[] left, T[]  right)
// {
//     int i = 0;
//     int j = 0;
//     int k = 0;
//
//     // Merging happens here
//     while(i < left.Length && right.Length)
//     {
//         if(left[i] <= right[j])
//             arr(k++) = left[i++];
//         else
//             arr[k++] = right[j++];
//     }
//
//     // Copy elements from left and right.
//     while (i < left.Length)
//         arr[k++] = left[i++];
//     while (j < right.Length)
//         arr[k++] = right[j++];
// }
//
// public class SingleList
// {
// 	public Node? Head;
// 	private int count;
//
// 	public SingleList
// 	public void AddFirst(T value){
// 		Node<T>? newNode = new Node<T>(value);
// 		if(Head is null)
// 		{
// 			Head = newNode;
// 		}
// 		else
// 		{
// 			var current = Head;
// 			Head = newNode;
// 			Head.Next = current;
// 		}
// 		count++;
// 	}
// 	public void AddLast(T value) {
// 		Node<T>? newNode = new Node<T>(value);
// 		if(Head is null)
// 		{
// 			Head = newNode;
// 		}
// 		else
// 		{
// 			var current = Head;
// 			while(current.Next != null)
// 			{
// 				current = current.Next;
// 			}
// 			current.Next = newNode;
// 		}
// 		count++;
// 	}
// 	public bool Remove(T value){
// 		// The value is lower than Head, so we assume the value is not in the list
// 		if(Head is null || Head.Value.CompareTo(value) > 0)
// 		{
// 			return false;
// 		}
// 		// If the value is the Head
// 		if(Head.Value.CompareTo(value) == 0)
// 		{
// 			Head = Head.Next;
// 			count--;
// 			return true;
// 		}
// 		var current = Head;
// 		while(current.Next != null && current.Next.Value.CompareTo(value) <= 0)
// 		{
// 			if(current.Next.Value.CompareTo(value) == 0){
// 				current.Next = current.Next.Next;
// 				count--;
// 				return true;
// 			}
// 			current = current.Next;
// 		}
// 		return false;
// 	}
// 	public Node<T> Search(T value){
// 		var current = Head;
// 		while(current != null && current.Value.CompareTo(value) != 0)
// 		{
// 			current = current.Next;
// 		}
// 		return current;
// 	}
// 	public bool Contains(T value){
// 		if(Head is null)
// 			return false;
// 		if(Head.Value.CompareTo(value) == 0){
// 			return true;
// 		}
// 		var current = Head;
// 		while(current != null)
// 		{
// 			if(current.Value.CompareTo(value) == 0)
// 			{
// 				return true;
// 			}
// 			current = current.Next;
// 		}
// 		return false;
// 	}
// 	public void AddSorted(){
// 		var newNode = new Node<T>(value);
// 		if(Head is null || Head.Value.CompareTo(value) >= 0){
// 			if(Head is null)
// 			{
// 				Head = newNode;
// 			}
// 			else 
// 			{
// 				var current = Head;
// 				Head = newNode;
// 				Head.Next = current;
// 			}
// 		}
// 		else
// 		{
// 			var current = Head;
// 			while(current.Next != null && current.Next.Value.CompareTo(value) < 0)
// 			{
// 				current = current.Next;
// 			}
// 			current.Next = new Node(value, current.Next);
// 		}
// 		count++;
// 	}
// }
//
// public class DoubleList
// {
//     public DoubleNode<T>? First, Last;
//     public DoublyLinkedList() => First = Last = null;
// 	private int count;
//
// 	public DoubleNode<T>? Search(T value)
//     {
//
//         var newNode = new DoubleNode<T>(value);
//         if (First.Value.CompareTo(newNode.Value) == 0)
//             return First;
//
//         var current = First;
//         while (current.Next != null && current.Value.CompareTo(value) != 0)
//         {
//             current = current.Next;
//         }
//         
//         return current;
//     }
//
// 	public void AddFirst(T value)
// 	{
// 		var newNode = new DoubleNode<T>(value);
// 		if(First is null)
// 			First = Last = newNode;
// 		else
// 		{
// 			First.Previous = newNode;
// 			newNode.Next = First;
// 			First = newNode;
// 		}
// 	}
//
// 	public void AddLast(T value)
// 	{
// 		var newNode = new DoubleNode<T>(value)
// 		{
// 			if(Last is null)
// 			{
// 				Last = newNode;
// 				if(First is null)
// 					First = newNode;
// 			}
// 			else
// 			{
// 				newNode.Previous = Last;
// 				Last.Next = newNode;
// 				Last = newNode;
// 			}
// 		}
// 	}
//
// 	public void AddSorted(T value)
// 	{
// 		var newNode = new DoubleNode<T>(value);
// 		if(First is null || value.CompareTo(First.Value) <= 0)
// 		{
// 			newNode.Next = First;
// 			if(First != null)
// 				First.Previous = newNode;
// 			else
// 				Last = newNode;
// 			First = newNode;
// 		}
// 		else
// 		{
// 			var current = First;
// 			while(current.Next != null && value.CompareTo(current.Next.Value) > 0)
// 				current = current.Next;
// 			newNode.Next = current.Next;
// 			newNode.Previous = current;
//
// 			if(current.Next != null)
// 				current.Next.Previous = newNode;
// 			else
// 				Last = newNode; //it's the tail
// 			current.Next = newNode;
// 		}
// 	}
//
// 	public bool Remove(T value)
// 	{
// 		if(First is null) return false;
//
// 		var current = First;
// 		while(current != null && current.Value.CompareTo(value) != 0)
// 		{
// 			current = current.Next;
// 		}
// 		if (current == null)
// 			return false;
// 		
// 		if(current == First)
// 		{
// 			First = First.Next;
// 			if(First != null)
// 				First.Previous = null;
// 			else
// 				Last = null;
// 			return true;
// 		}
// 		
// 		if(current == Last)
// 		{
// 			Last = Last.Previous;
// 			if(Last != null)
// 				Last.Next = null;
// 			else
// 				First = null;
// 			return true;
// 		}
// 		
// 		current.Previous.Next = current.Next;
// 		current.Next.Previous = current.Previous;
// 		return true;
// 	}
// }
//
// ``` C#
// public class Stack<T>
// {
// 	private T[] array;
// 	private int top;
// 	private int usage;
//
// 	public bool Empty => top == -1;
// 	public bool Full => top == Size - 1;
// 	public int Count => usage;
// 	public int Size => array.Length;
//
// 	public Stack(int size = 4)
// 	{
// 		array = new T[size];
// 		top = -1;
// 		usage = 0;
// 	}
//
// 	public void Push(T item)
// 	{
// 		if (Full)
// 		{
// 			T[] newArray = new T[Size * 2 + 1];
// 			for(int i = 0; i < Size; i++)
// 			{
// 				newArray[i] = array[i];
// 			}
// 			array = newArray;
// 		}
// 		array[++top] = item;
// 		usage++;
// 	}
//
// 	public T Pop()
// 	{
// 		if (_top == -1)
// 			throw new InvalidOperationException("Stack is empty!");
// 		return _items[_top--];
// 	}
//
// 	public T Peek()
// 	{
// 		if (_top == -1)
// 			throw new InvalidOperationException("Stack is empty!");
// 		return _items[_top];
// 	}
//
// 	public bool IsEmpty => _top == -1;
// }
//
// public class Queue<T>
// {
// 	private T[] array;
// 	private int front;
// 	private int back;
// 	private int count;
//     
// 	public Queue(int size = 4)
// 	{
// 		data = new T[size];
// 		count = 0;
// 		front = back = -1;
// 	}
// 	private int GetNextIndex(int index)
// 	{
// 		return (index + 1) % array.Length;
// 	}
//
// 	public void Enqueue(T item)
// 	{
// 		if(Full)
// 		{
// 			var newArray = new T[Size * 2];
// 			for(int i = 0; i < Size; i++)
// 			{
// 				newArray[i] = array[i];
// 			}
// 			array = newArray;
// 		}
// 		back = GetNextIndex(back);
// 		count++;
// 		array[back] = item;
// 	}
//
// 	public T Dequeue()
// 	{
// 		if (Empty)
// 		{
// 			return default;
// 		}
// 		front = GetNextIndex(front);
// 		count--;
// 		return array[front];
// 	}
// }
//
// public class Entry<K, V>
//
// {
// 	public K Key { get; set; }
// 	public V Value { get; set; }
// 	public Entry(K key, V value)
// 	{
// 		Key = key;
// 		Value = value;
// 	}
// }
//
// public interface IHashTable<K, V>
// {
// 	bool Add(K key, V value);
// 	V? Find(K key);
// 	bool Delete(K key);
// }
//
// public class HashTable<K, V> : IHashTable<K, V>
//
// {
// 	Entry<K, V>[]? buckets { get; set;}
// 	public ReadOnlyCollection<Entry<K, V>> data => buckets == null? null : buckets.AsReadOnly();
//
// 	public HashTable() { buckets = null; }
// 	public HashTable(Entry<K, V>[]? input) { importData(input);}
// 	public HashTable(int capacity)
// 	{
// 		buckets = new Entry<K, V>[capacity];
// 	}
//
// 	protected int getIndex(K key)
// 	{
// 		int hashCode = Math.Abs(key.GetHashCode());
// 		return hashCode % buckets.Length;
// 	}
//
// 	public bool Add(K key, V value)
// 	{
// 		int index = getIndex(key);
// 		int originalIndex = index;
// 		do
// 		{
// 			if (buckets[index] != null && buckets[index].Key.Equals(key))
// 				return false;
//
// 			if (buckets[index] == null || buckets[index].Key.Equals(key))
// 			{
// 				buckets[index] = new Entry<K, V>(key, value);
// 				return true;
// 			}
// 			
// 			index = (index + 1) % buckets.Length;
// 		} while (index != originalIndex);
// 		return false;
// 	}
//
//
// 	public V? Find(K key)
// 	{
// 		int index = getIndex(key);
// 		int originalIndex = index;
//
// 		do
// 		{
// 			if(buckets[index] == null)
// 				return default;
//
// 			if (buckets[index].Key.Equals(key))
// 			{
// 				return buckets[index].Value;
// 			}
//
// 			index = (index + 1) % buckets.Length;
// 		} while (index != originalIndex);
//
// 		return default;
// 	}
//
// 	public bool Delete(K key)
// 	{
// 		int index = getIndex(key);
// 		int originalIndex = index;
//
// 		do
// 		{
// 			if(buckets[index] == null)
// 				return false;
//
// 			if (buckets[index].Key.Equals(key))
// 			{
// 				buckets[index] = default;
// 				return true;
// 			}
//
// 			index = (index + 1) % buckets.Length;
//
// 		} while (index != originalIndex);
//
// 		return false;
// 	}
//
// 	//DO NOT REMOVE the following method:
// 	private void importData(Entry<K, V>[]? inputData)
// 	{
// 		if(inputData != null)
// 		{
// 			buckets = new Entry<K, V>[inputData.Length];
// 			for (int i = 0; i < inputData.Length; ++i)
// 				buckets[i] = inputData[i];
// 		}
// 	}
// }
//
// public string BFT(int root)
// {
// 	// Create string to return later
// 	string toReturn = "";
// 	// Create queue and array of visited nodes
// 	var queue = new Queue<int>();
// 	var visited = new bool[Count];
// 	// Initialize the Root
// 	queue.Enqueue(start);
// 	visited[root] = true;
//
// 	while (queue.Count > 0)
// 	{
// 		// dequeue a node
// 		var current = queue.Dequeue();
// 		toReturn += current + " "; // Adds the node to the string
//
// 		var neighbors = Neighbors(current); // Gets all neighbors
// 		foreach (var neighbor in neighbors)
// 		{
// 			if (!visited[neighbor])
// 			{
// 				visited[neighbor] = True;
// 				queue.Enqueue(neighbor);
// 			}
// 		}
// 	}
// 	return toReturn;
// }
//
// public string DFT(int root)
// {
// 	string toReturn = " ";
//
// 	// Empty stack
// 	Stack<int> stack = new Stack<int>();
// 	var visited = new bool[Count]; // size of the graph
// 	
// 	while (stack.Count < 0)
// 	{
// 		var node = stack.Pop(); // pop a node from the stack
// 		
// 		if(visited[node] == false)
// 		{
// 			visited[node] = true;
// 			toReturn += node + " ";
// 			var neighbors = NeighborsReversed(node);
// 			foreach(var neighbor in neighbors)
// 			{
// 				stack.Push(neighbor);
// 			}
// 		}
// 	}
// 	return toReturn;
// }
//
// public Tuple<double[], int[]> SingleSourceShortestPath(int source)
// {
// 	// init distance, prev and unvisitedNodes
// 	double[] distance = new double[Count];
// 	int[] prev = new int[Count];
// 	List<int> unvisitedNodes = new();
// 	
// 	for(int i = 0; i < Count; i++)
// 	{
// 		// the default distance: double.PositiveInfinity;
// 		// the default previous node: -1;
// 		distance[i] = double.PositiveInfinity;
// 		prev[i] = -1;
// 		unvisitedNodes.Add(i);
// 	}
// 	
// 	// sets the distance of source
// 	distance[source] = 0;
// 	
// 	while(unvisitedNodes.Count > 0)
// 	{
// 		int closestNode = 0;
// 		double closestDistance = double.PositiveInfinity;
// 		foreach(var node in unvisitedNodes)
// 		{
// 			if(distance[node] < closestDistance)
// 			{
// 				closestNode = node;
// 				closestDistance = distance[node];
// 			}
// 		}
// 		
// 		// remove the closest node from unvisitedNodes;
// 		unvisitedNodes.Remove(closestNode);
// 		
// 		foreach(var neighbor in Neighbors(closestNode))
// 		{
// 			// calculate the distance and updates it if smaller\
// 			double alt = distance[closestNode]
// 			             + AdjacencyMatrix[closestNode, neighbor];
// 			if(alt < distance[neighbor])
// 			{
// 				distance[neighbor] = alt;
// 				prev[neighbor] = closestNode; 
// 			}
// 		}
// 	}
// 	
// 	return new Tuple<double[], int[]>(distance, prev);
// }
//
// public static long FibonacciDynamic(long n, long[] storedResults)
// {
// 	if(storedResults[n] != 0) 
// 	{
// 		return storedResults[n];
// 	}
// 	if(n is 0 or 1)
// 		return n;
// 		
// 	storedResults[n] = FibonacciDynamic(n - 1, storedResults) 
// 	                   +  FibonacciDynamic(n - 2, storedResults);
// 	return storedResults[n];
// }
//
// public class FloydWarshall {
// 	public static Tuple<double[,], int[,]> Init(double[,] graph) {
// 		int n = graph.GetLength(0);
// 		double[,] distance = new double[n, n];
// 		int[,] next = new int[n, n];
//
// 		for (int i = 0; i < n; i++) {
// 			for (int j = 0; j < n; j++) {
// 				if (i == j) {
// 					distance[i, j] = 0;
// 				} else {
// 					distance[i, j] = graph[i, j];
// 				}
// 				if (i != j && !double.IsPositiveInfinity(graph[i, j])) {
// 					next[i, j] = j;
// 				} else {
// 					next[i, j] = -1;
// 				}
// 			}
// 		}
//
// 		return new Tuple<double[,], int[,]>(distance, next);
// 	}
//
// 	public static Tuple<double[,], int[,]> AllPairShortestPath(double[,] graph) {
// 		var (dist, next) = Init(graph);
//
// 		for (int k = 0; k < graph.GetLength(0); k++) {
// 			for (int i = 0; i < graph.GetLength(0); i++) {
// 				for (int j = 0; j < graph.GetLength(0); j++) {
// 					if (dist[i, k] + dist[k, j] < dist[i, j]) {
// 						dist[i, j] = dist[i, k] + dist[k, j];
// 						next[i, j] = next[i, k];
// 					}
// 				}
// 			}
// 		}
//
// 		return new Tuple<double[,], int[,]>(dist, next);
// 	}
// }