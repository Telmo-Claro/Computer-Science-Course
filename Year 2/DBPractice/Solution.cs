using System;
using System.Linq;

class Solution
{
    public static void Q1(ExamContext db, string Name)
    {
        var result = from c in db.Customers
                     where c.FirstName.Contains(Name) || c.LastName.Contains(Name)
                     select c;

        foreach (var r in result)
            Console.WriteLine($"ID: {r.ID}, FirstName: {r.FirstName}, LastName:{r.LastName}");
    }

    public static void Q2(ExamContext db, int ProductID)
    {
        var result = from p in db.Products
                     where p.ID == ProductID
                     select p;

        foreach (var r in result)
            Console.WriteLine($"Company: {r._Company?.Name ?? "(none)"}, Product: {r.Name}, Price: {r.Price}");
    }

    public static void Q3(ExamContext db)
    {
        var result = from c in db.Companies
                     group c by c.Country != null ? c.Country.ToUpper() : "NULL" into g
                     select new
                     {
                         Country = g.Key,
                         Count = g.Count(),
                         Companies = g.ToList()
                     };

        foreach (var r in result)
        {
            Console.WriteLine($"{r.Country}, {r.Count}");
            foreach (var c in r.Companies)
            {
                Console.WriteLine($"{c.ID}, {c.Name}, {c.Country}");
            }
        }

    }

    public static void Q4(ExamContext db, int OrderID)
    {
        // Find order items and related data for the given OrderID
        var items = (from o in db.Orders
                     join c in db.Customers on o.CustomerID equals c.ID
                     join sc in db.ShoppingCarts on o.ID equals sc.OrderID
                     join p in db.Products on sc.ProductID equals p.ID
                     where o.ID == OrderID
                     select new
                     {
                         CustomerName = $"{c.FirstName} {c.LastName}",
                         OrderDate = o.dateTime,
                         ProductName = p.Name,
                         Quantity = sc.Quantity,
                         UnitPrice = p.Price,
                         TotalPrice = sc.Quantity * p.Price
                     }).ToList();

        if (!items.Any())
        {
            Console.WriteLine($"No order found with ID {OrderID}");
            return;
        }

        var first = items.First();
        Console.WriteLine($"Customer: {first.CustomerName}");
        Console.WriteLine($"Order ID: {OrderID}, Date: {first.OrderDate}");

        decimal grandTotal = 0m;
        foreach (var item in items)
        {
            Console.WriteLine($"{item.ProductName}, {item.UnitPrice} x {item.Quantity} = {item.TotalPrice}");
            grandTotal += item.TotalPrice;
        }

        Console.WriteLine($"Grand total: {grandTotal}");

    }

    public static void Q5(ExamContext db)
    {

    }

    public static void Q6(ExamContext db)
    {

    }

    public static void Q7(ExamContext db, string Country, decimal fraction)
    {


    }

    public static void Q8(ExamContext db, int OrderID)
    {

    }

}