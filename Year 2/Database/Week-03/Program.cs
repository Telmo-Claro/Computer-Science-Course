/*
 * The goal of this week:
 * Insert, Delete, Update
 */

class Program
{
    static void Main(string[] args)
    {
        using (var db = new Model.MyContext())
        {
            db.Departments.Add(new Department() { Name = "Education Department"});
            var n = db.SaveChanges();
            Console.WriteLine($"{n} entries written in database");
        }
    }
}