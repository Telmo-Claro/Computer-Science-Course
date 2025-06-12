/*
 * The goal of this week:
 * Insert, Delete, Update
 */

class Program
{
    static void Main(string[] args)
    {
        using (var context = new Model.MyContext())
        {
            context.Departments.Add(new Department() { Number = "1", Name = "Education Department" });
            var n = context.SaveChanges();
            Console.WriteLine($"{n} entries written in database");
            context.Employees.Add(
                new Employee()
                {
                    SSN = "12345678",
                    FirstName = "John",
                    LastName = "Doe",
                    BirthDate = DateTime.Parse("01/01/1999"),
                    Address = "John Pork Street",
                    Sex = "M",
                    Salary = 9000,
                }
            );
            context.SaveChanges();
        }
    }
}