// Data/DataSeeder.cs
using Bogus;

public class DataSeeder
{
    public static void SeedData(ApplicationDbContext context)
    {
        // Clear existing data
        context.Database.EnsureDeleted();
        context.Database.EnsureCreated();

        // Create categories
        var categories = new List<Category>();
        var categoryFaker = new Faker<Category>()
            .RuleFor(c => c.Name, f => f.Commerce.Categories(1)[0])
            .RuleFor(c => c.Description, f => f.Lorem.Sentence());

        categories = categoryFaker.Generate(5);
        context.Categories.AddRange(categories);
        context.SaveChanges();

        // Create products
        var products = new List<Product>();
        var productFaker = new Faker<Product>()
            .RuleFor(p => p.Name, f => f.Commerce.ProductName())
            .RuleFor(p => p.Description, f => f.Commerce.ProductDescription())
            .RuleFor(p => p.Price, f => f.Random.Decimal(10, 1000))
            .RuleFor(p => p.StockQuantity, f => f.Random.Int(0, 100))
            .RuleFor(p => p.CategoryId, f => f.PickRandom(categories).Id)
            .RuleFor(p => p.CreatedAt, f => f.Date.Past(1))
            .RuleFor(p => p.IsActive, f => f.Random.Bool(0.8f)); // 80% active

        products = productFaker.Generate(50);
        context.Products.AddRange(products);
        context.SaveChanges();

        // Create customers
        var customers = new List<Customer>();
        var customerFaker = new Faker<Customer>()
            .RuleFor(c => c.FirstName, f => f.Person.FirstName)
            .RuleFor(c => c.LastName, f => f.Person.LastName)
            .RuleFor(c => c.Email, f => f.Person.Email)
            .RuleFor(c => c.Phone, f => f.Phone.PhoneNumber())
            .RuleFor(c => c.RegistrationDate, f => f.Date.Past(2));

        customers = customerFaker.Generate(20);
        context.Customers.AddRange(customers);
        context.SaveChanges();

        // Create orders
        var orders = new List<Order>();
        var orderFaker = new Faker<Order>()
            .RuleFor(o => o.CustomerId, f => f.PickRandom(customers).Id)
            .RuleFor(o => o.OrderDate, f => f.Date.Past(1))
            .RuleFor(o => o.Status, f => f.PickRandom("Pending", "Shipped", "Delivered", "Cancelled"));

        orders = orderFaker.Generate(100);
        context.Orders.AddRange(orders);
        context.SaveChanges();

        // Create order items
        var orderItems = new List<OrderItem>();
        var orderItemFaker = new Faker<OrderItem>()
            .RuleFor(oi => oi.OrderId, f => f.PickRandom(orders).Id)
            .RuleFor(oi => oi.ProductId, f => f.PickRandom(products).Id)
            .RuleFor(oi => oi.Quantity, f => f.Random.Int(1, 5))
            .RuleFor(oi => oi.UnitPrice, (f, oi) => 
                products.First(p => p.Id == oi.ProductId).Price);

        orderItems = orderItemFaker.Generate(300);
        context.OrderItems.AddRange(orderItems);
        context.SaveChanges();

        // Update order total amounts
        foreach (var order in orders)
        {
            order.TotalAmount = context.OrderItems
                .Where(oi => oi.OrderId == order.Id)
                .Sum(oi => oi.Quantity * oi.UnitPrice);
        }
        context.SaveChanges();

        Console.WriteLine("Database seeded successfully!");
        Console.WriteLine($"Categories: {categories.Count}");
        Console.WriteLine($"Products: {products.Count}");
        Console.WriteLine($"Customers: {customers.Count}");
        Console.WriteLine($"Orders: {orders.Count}");
        Console.WriteLine($"Order Items: {orderItems.Count}");
    }
}