namespace Week_03.Models;

public class Department
{
    public string Name { get; set; }
    public int Number { get; set; }
    public string? ManagerSSN { get; set; }
    public  DateOnly ManagerStartDate { get; set; }
}