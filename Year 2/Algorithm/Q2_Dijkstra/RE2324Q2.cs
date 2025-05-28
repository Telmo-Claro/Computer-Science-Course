namespace Solution;

public class Q2
{   
    public static Tuple<double[], int[]> Initialize(double[,] graph, int source, List<int> unvisitedNodes){
        //ToDo 2.0: Initialize distance, previous nodes array and unvisitedNodes list 
        //          for Dijkstra (single source shortest path)
        double[] distance = new double[graph.GetLength(0)];
        int[] previous = new int[graph.GetLength(0)];
        unvisitedNodes.Add(source);
        for (int i = 0; i < distance.Length; i++)
        {
            distance[i] = double.PositiveInfinity;
            previous[i] = -1;
            if (i != source)
            {
                unvisitedNodes.Add(i);
            }
        }

        distance[source] = 0;
        return new Tuple<double[], int[]>(distance, previous);
    }

    public static Tuple<double[], int[]> Dijkstra(double[,] graph, 
                                                        int source, 
                                                        Func<double[,], int, List<int>, Tuple<double[], int[]>> initializeFunc, 
                                                        Func<double[,],int, List<int>> neighborsFunc)
    {
        //ToDo 2.1: Dijkstra for single source shortest path
        
        int Count = graph.GetLength(0);
        double[] distance; // this is an array representing the distance of the SOURCE to each NODE.
        int[] prev;
        List<int> unvisitedNodes = new List<int>(Count);
        
        // initialization of distance, prev and unvisitedNodes
        // here the provided method initialize is used:
        (distance, prev) =  initializeFunc(graph, source, unvisitedNodes);
        
        //until unvisitedNodes is empty
        while (unvisitedNodes.Count > 0)
        {
            var closestDistance = double.PositiveInfinity;
            var closestNode = 0;
            
            foreach (var unvisitedNode in unvisitedNodes) // it checks for the next smallest weight.
            {
                // find closest node in unvisitedNodes
                if (distance[unvisitedNode] < closestDistance)
                {
                    closestDistance = distance[unvisitedNode];
                    closestNode = unvisitedNode;
                }
            }
            // remove the closest node from unvisitedNodes
            unvisitedNodes.Remove(closestNode);
            // considering all neighboring (unvisited) nodes 
            // (method: neighborsFunc can be used here)
            foreach (var neighbor in Neighbors(graph, closestNode))
            {
                // update distance and prev arrays when needed
                if (distance[closestNode] + graph[closestNode, neighbor] < distance[neighbor])
                {
                    distance[neighbor] = distance[closestNode] + graph[closestNode, neighbor];
                    prev[neighbor] = closestNode;
                }
            }
        }
        
        return new Tuple<double[], int[]>(distance, prev);
    }

    public static Tuple<double[][], int[][]> DijkstraForAll(double[,] graph, 
                                                          Func<double[,], 
                                                          int, 
                                                          Tuple<double[], int[]>> dijkstraFunc)
    {
        //ToDo 2.2: Dijkstra for all Pairs
        throw new NotImplementedException();
    }
    
    public static List<int> Neighbors(double[,] graph, int node)
    { 
        //ToDo 2.3: Neighbours of given node
        var neighbors = new List<int>();
        for (int i = 0; i < graph.GetLength(0); i++)
        {
            if (!double.IsPositiveInfinity(graph[node, i]))
            {
                neighbors.Add(i);
            }
        }
        return neighbors;
    }
}
