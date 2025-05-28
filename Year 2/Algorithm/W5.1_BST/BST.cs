
using System.Xml.Schema;
using Microsoft.VisualBasic;

namespace Solution;

public class BST<T> : IBST<T> where T : IComparable<T>
{
    public TreeNode<T>? Root { get; set; }

    public void Insert(T value) => Insert(value, Root);
    public void InsertIterative(T value)
    {
        // case Root is null
        if (Root == null)
        {
            Root = new TreeNode<T>(value);
            return;
        }
        
        var currentNode = Root;
        while(currentNode != null)
        {
            if(value.CompareTo(currentNode.Value) == 0)
            {
                return;
            }
            else if(value.CompareTo(currentNode.Value) < 0)
            {
                if (currentNode is not null)
                {
                    if (currentNode.Left is null)
                    {
                        currentNode.Left = new TreeNode<T>(value, currentNode);
                        break;
                    }
                }
                currentNode = currentNode.Left;
            }
            else // the value is greater than the current node's value
            {
                if (currentNode is not null)
                {
                    if (currentNode.Right is null)
                    {
                        currentNode.Right = new TreeNode<T>(value, currentNode);
                        break;
                    }
                }
                currentNode = currentNode.Right;
            }
        }
    }

    private void Insert(T value, TreeNode<T>? node)
    {
        // case Root is null
        if (Root is null)
        {
            Root = new TreeNode<T>(value);
        }
        else if (value.CompareTo(node.Value) == 0)
        {
            return;
        }
        else if(node.Value.CompareTo(value) > 0)
        {
            if(node.Left is not null)
            {
                Insert(value, node.Left);
            }
            else
            {
                node.Left = new TreeNode<T>(value, node);
            }
        }
        else if (node.Value.CompareTo(value) < 0)
        {
            if(node.Right is not null)
            {
                Insert(value, node.Right);
            }
            else
            {
                node.Right = new TreeNode<T>(value, node);
            }
        }
    }

    #region Traversal

    public string PreOrderTraversal() => PreOrderTraversal(Root);
    private string PreOrderTraversal(TreeNode<T>? currNode)
    {
        var toReturn = "";
        if (currNode is not null)
        {
            toReturn += currNode.Value + " ";
            toReturn += PreOrderTraversal(currNode.Left);
            toReturn += PreOrderTraversal(currNode.Right);
        }

        return toReturn;
    }

    public string InOrderTraversal() => InOrderTraversal(Root);
    private string InOrderTraversal(TreeNode<T>? currNode)
    {
        var toReturn = "";
        if (currNode is not null)
        {
            toReturn += InOrderTraversal(currNode.Left); // Add space after each node
            toReturn += currNode.Value + " ";
            toReturn += InOrderTraversal(currNode.Right);
        }
        return toReturn;    
}

    public string PostOrderTraversal() => PostOrderTraversal(Root);
    private string PostOrderTraversal(TreeNode<T>? currNode)
    {
        var toReturn = "";
        if (currNode is not null)
        {
            toReturn += PostOrderTraversal(currNode.Left);
            toReturn += PostOrderTraversal(currNode.Right);
            toReturn += currNode.Value + " ";
        }

        return toReturn;
    }
    #endregion

    public bool Contains(T value) => Search(Root, value) != null; 

    private TreeNode<T> Search(TreeNode<T>? node, T value)
    {
        // node does not exist
        if(node is null)
        {
            return null;
        }
        // value in the node is the same we are looking for
        if(value.CompareTo(node.Value) == 0)
        {
            return node;
        }
        
        // value in the node is smaller than the one we are looking for
        if(value.CompareTo(node.Value) < 0)
        {
            return Search(node.Left, value);
        }
        // value in the node is bigger than the one we are looking for
        else if(value.CompareTo(node.Value) > 0)
        {
            return Search(node.Right, value);
        }
        return null;
    }

    #region  Remove Delete

    public bool Remove(T value) => DeleteValue(this, value);

    private bool DeleteValue(BST<T>? tree, T value)
    {
        if (tree is null || value is null)
            return false;
        
        // special case if the value to delete is in the root (and the root has 0 children or 1 child)  
        if (value.CompareTo(tree.Root.Value) == 0)
        {
            // there are no children:
            if (tree.Root.Left == null && tree.Root.Right == null)
            {
                tree.Root = null;
            }
            // there is only left child, the right does not exist
            else if (tree.Root.Left != null && tree.Root.Right == null)
            {
                tree.Root = tree.Root.Left;
                tree.Root.Parent = null;
            }
            // there is only right child, the left does not exist 
            else if (tree.Root.Left == null && tree.Root.Right != null)
            {
                tree.Root = tree.Root.Right;
                tree.Root.Parent = null;
            }
            else
            {
                return delete(tree.Root);
            }
            
            return true;
        }
        
        return delete(Search(tree.Root, value));
    }

    private bool delete(TreeNode<T> nodeToDelete)
    {
        if (nodeToDelete is null)
            return false;
        
        // CASE 1 : LEAF
        if (nodeToDelete.Left == null && nodeToDelete.Right == null)
        {
            if (isLeft(nodeToDelete, nodeToDelete.Parent))
            {
                nodeToDelete.Parent.Left = null; 
            } else
            {
                nodeToDelete.Parent.Right = null; 
            }
            return true;
        }

        // CASE 2 : ONE CHILD
        if (nodeToDelete.Left != null && nodeToDelete.Right == null)
        {
            if (isLeft(nodeToDelete, nodeToDelete.Parent))
                nodeToDelete.Parent.Left = nodeToDelete.Left;
            else
                nodeToDelete.Parent.Left = nodeToDelete.Right;
            nodeToDelete.Left.Parent = nodeToDelete.Parent;
            return true;
        }
        else if (nodeToDelete.Left == null && nodeToDelete.Right != null)
        {
            if (isLeft(nodeToDelete, nodeToDelete.Parent))
                nodeToDelete.Parent.Left = nodeToDelete.Right;
            else
                nodeToDelete.Parent.Right = nodeToDelete.Right;
            nodeToDelete.Right.Parent = nodeToDelete.Parent;
            return true;
        }
        
        // CASE 3 : TWO CHILDREN
        var inordersucc = findInOrderSucc(nodeToDelete);
        nodeToDelete.Value = inordersucc.Value;
        return delete(inordersucc);
    }
    

    // This methods finds the in order successor of the node given as parameter
    private TreeNode<T>? findInOrderSucc(TreeNode<T> node)
    {
        var currNode = node.Right;
        while (currNode != null && currNode.Left != null)
            currNode = currNode.Left;

        return currNode;
    }
 
    // This methods checks if the node given as first parameter is the left child of the node given as second parameter ("parent"). 
    // The comparison is based on the values of the nodes.
    private bool isLeft(TreeNode<T> node, TreeNode<T> parent)
    {
        return parent.Left != null && parent.Left.Value.CompareTo(node.Value) == 0;
    }

    public List<T> Traversal(TraversalOrder traversalOrder) //Optional
    {
        throw new NotImplementedException();
    }
    #endregion
}

