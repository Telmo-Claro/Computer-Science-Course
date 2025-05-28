namespace Solution;

public class FloydWarshall
{
    public static Tuple<double[,], int[,]> Init(double[,] graph)
    {
        //ToDo 1.1 Initialize the distance and next matrix
        var inf = double.PositiveInfinity;
        var totalNodes = graph.GetLength(0);
        double[,] dist = new double[totalNodes, totalNodes]; // Make the matrix of the distance between each node
        int[,] next = new int[totalNodes, totalNodes]; // Predecessor matrix, it points to the previous node

        for (int i = 0; i < graph.GetLength(0); i++)
        {
            for (int j = 0; j < graph.GetLength(1); j++)
            {
                if (i == j)
                {
                    dist[i, j] = 0;
                }
                else
                {
                    dist[i, j] = graph[i, j];
                }

                if (graph[i, j] != inf)
                {
                    next[i, j] = j;
                }
                else
                {
                    next[i, j] = -1;
                }
            }
        }

        for (int k = 0; k < totalNodes; k++)
        {
            for (int i = 0; i < totalNodes; i++)
            {
                for (int j = 0; j < totalNodes; j++)
                {
                    if (dist[i, j] > dist[i, k] + dist[k, j])
                    {
                        dist[i, j] = dist[i, k] + dist[k, j];
                        next[i, j] = next[i, k];
                    }
                }
            }
        }


        return new Tuple<double[,], int[,]>(dist, next);
    }
    
    public static Tuple<double[,], int[,]> AllPairShortestPath(double[,] graph)
    {
        return Init(graph);
    }
}