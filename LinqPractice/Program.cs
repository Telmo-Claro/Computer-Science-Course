// Program.cs
using System;
using Microsoft.EntityFrameworkCore;

class Program
{
    static void Main()
    {
        try
        {
            Console.WriteLine("Ensuring database exists and is ready...");

            using (var db = new ApplicationDbContext())
            {
                // Ensure the database file and schema are created from the model
                db.Database.EnsureCreated();

                Console.WriteLine("Seeding database with fake data (this will recreate data)...");
                // SeedData currently calls EnsureDeleted/EnsureCreated internally
                DataSeeder.SeedData(db);

                Console.WriteLine("Database setup complete! Ready for LINQ practice.");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
            Console.WriteLine("If this persists, run `dotnet restore` and ensure the SQLite provider package is installed.");
        }
    }
}