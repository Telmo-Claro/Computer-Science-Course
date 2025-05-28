using System.Collections.ObjectModel;

namespace Solution;

public class HashTable<K, V> : IHashTable<K, V>
{
    Entry<K, V>[]? buckets { get; set;}

    public ReadOnlyCollection<Entry<K, V>> data => buckets == null? null : buckets.AsReadOnly();

    public HashTable() { buckets = null; }

    public HashTable(Entry<K, V>[]? input) { importData(input);}

    public HashTable(int capacity)
    {
        buckets = new Entry<K, V>[capacity];
    }

    protected int getIndex(K key)
    {
        int hashCode = Math.Abs(key.GetHashCode());
        return hashCode % buckets.Length;
    }

    public bool Add(K key, V value)
    {
        int index = getIndex(key);
        int originalIndex = index;

        do
        {
            if (buckets[index] != null && buckets[index].Key.Equals(key)) 
                return false;

            if (buckets[index] == null || buckets[index].Key.Equals(key))
            {
                buckets[index] = new Entry<K, V>(key, value);
                return true;
            }

            index = (index + 1) % buckets.Length;
        } while (index != originalIndex);

        return false;
    }

    public V? Find(K key)
    {
        int index = getIndex(key);
        int originalIndex = index;
        
        do
        {
            if(buckets[index] == null)
                return default;
            
            if (buckets[index].Key.Equals(key))
            {
                return buckets[index].Value;
            }
            
            index = (index + 1) % buckets.Length;
        } while (index != originalIndex);

        return default;
    }

    public bool Delete(K key)
    {
        int index = getIndex(key);
        int originalIndex = index;
        
        do
        {
            if(buckets[index] == null)
                return false;
            
            if (buckets[index].Key.Equals(key))
            {
                buckets[index] = default;
                return true;
            }
            
            index = (index + 1) % buckets.Length;
        } while (index != originalIndex);
        
        return false;
    }
    
    
    //DO NOT REMOVE the following method:
    private void importData(Entry<K, V>[]? inputData)
    {
        if(inputData != null) 
        {
            buckets = new Entry<K, V>[inputData.Length];
            for (int i = 0; i < inputData.Length; ++i) 
                buckets[i] = inputData[i];
        }
    }
}