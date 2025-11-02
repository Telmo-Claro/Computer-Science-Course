public class Order
{
    public int Id { get; set; }
    public int CustomerId { get; set; }
    public DateTime OrderDate { get; set; }
    public decimal TotalAmount { get; set; }
    public string Status { get; set; } // "Pending", "Shipped", "Delivered", "Cancelled"
    
    // Navigation properties
    public Customer Customer { get; set; }
    public ICollection<OrderItem> OrderItems { get; set; }
}