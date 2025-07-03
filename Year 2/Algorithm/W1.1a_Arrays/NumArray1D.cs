using System.Numerics;

namespace ToDo;
public class NumArray1D<T> : Array1D<T>, INumArray1D<T> where T : IComparable<T>, INumber<T>
{
    public NumArray1D(int size = 10):base(size) {  }
    public NumArray1D(T[] data):base(data) { }

    public T? Aggregate(Func<T, T, T> fx)
    {
        var result = fx(_data[0], _data[1]);
        for(int i = 2; i < _data.Length; i ++)
        {
            result = fx(result, _data[i]);
        }
        return result;
    }

    public T? Sum()
    {
        Func<T, T, T> fx = (a, b) => a + b;
        return Aggregate(fx);
    }

    public T? Min()
    {
        Func<T, T, T> fx = (a, b) => a < b ? a : b;
        return Aggregate(fx);
    }

    public T? Max()
    {
        Func<T, T, T> fx = (a, b) => a > b ? a : b;
        return Aggregate(fx);
    }

    public T? Product(bool IgnoreZeros = true)
    {
        if (IgnoreZeros)
        {
            Func<T, T, T> fx = (a, b) =>
            {
                if (b.Equals(0))
                {
                    return a;
                }
                return a * b;
            };
            return Aggregate(fx);
        }
        else
        {
            Func<T, T, T> fx = (a, b) => a * b;
            return Aggregate(fx);
        }
    }
}