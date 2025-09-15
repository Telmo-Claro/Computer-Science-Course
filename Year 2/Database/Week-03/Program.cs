using Bogus;

using Week_03.Models;

namespace Week_03;

class Program
{
    static CompanyContext db = new CompanyContext();

    static void Main(string[] args)
    {
        Seed();

    }

    static void Seed()
    {
        // Deletes and builds it again
        db.Database.EnsureDeleted();
        db.Database.EnsureCreated();
        
        var faker = new Faker("en");
        
        // Seed Departments
        var departments = new List<Department>();
        for (int i = 1; i < 11; i++)
        {
            var dept = new Department
            {
                Number = i,
                Name = faker.Commerce.Department(),
                ManagerSSN = null, // added later
                ManagerStartDate = DateOnly.FromDateTime(faker.Date.Past(5))
            };
            departments.Add(dept);
            db.departments.Add(dept);
        }
        
        // Managers
        var managers = new List<Employee>();
        foreach (var dept in departments)
        {
            var manager = new Employee
            {
                SSN = faker.Random.Replace("#########"),
                FirstName = faker.Name.FirstName(),
                MiddleInitials = faker.Random.Char('A', 'Z'),
                LastName = faker.Name.LastName(),
                BirthDate = DateOnly.FromDateTime(faker.Date.Past(30, DateTime.Today.AddYears(-25))),
                Address = faker.Address.FullAddress(),
                Sex = faker.PickRandom('M', 'F'),
                Salary = faker.Random.Decimal(70000, 120000),
                Super_SSN = null, // top-level managers have no supervisor
                DepartmentNumber = dept.Number
            };

            managers.Add(manager);
            db.employees.Add(manager);
        }
        db.SaveChanges();
        
        // Assign managers to departments now (after saving their SSNs)
        for (int i = 0; i < departments.Count; i++)
        {
            departments[i].ManagerSSN = managers[i].SSN;
        }
        db.SaveChanges();
        
        // Seed employees (with managers as supervisors)
        // 3. Seed Employees (with managers as supervisors)
        var employees = new List<Employee>();
        for (int i = 0; i < 90; i++)
        {
            var dept = faker.PickRandom(departments);
            var manager = managers.First(m => m.DepartmentNumber == dept.Number);

            var emp = new Employee
            {
                SSN = faker.Random.Replace("#########"),
                FirstName = faker.Name.FirstName(),
                MiddleInitials = faker.Random.Char('A', 'Z'),
                LastName = faker.Name.LastName(),
                BirthDate = DateOnly.FromDateTime(faker.Date.Past(30, DateTime.Today.AddYears(-22))),
                Address = faker.Address.FullAddress(),
                Sex = faker.PickRandom('M', 'F'),
                Salary = faker.Random.Decimal(40000, 100000),
                Super_SSN = manager.SSN,
                DepartmentNumber = dept.Number
            };
            employees.Add(emp);
            db.employees.Add(emp);
        }
        
        var dept_bob = faker.PickRandom(departments);
        var manager_bob = managers.First(m => m.DepartmentNumber == dept_bob.Number);
        var bob = new Employee
        {
            SSN = faker.Random.Replace("#########"),
            FirstName = "Bob",
            MiddleInitials = faker.Random.Char('A', 'Z'),
            LastName = faker.Name.LastName(),
            BirthDate = DateOnly.FromDateTime(faker.Date.Past(30, DateTime.Today.AddYears(-22))),
            Address = faker.Address.FullAddress(),
            Sex = faker.PickRandom('M', 'F'),
            Salary = faker.Random.Decimal(40000, 100000),
            Super_SSN = manager_bob.SSN,
            DepartmentNumber = dept_bob.Number
        };
        employees.Add(bob);
        db.employees.Add(bob);

        db.SaveChanges();
        
        // Projects
        // 4. Seed Projects
        var projects = new List<Project>();
        for (int i = 1; i <= 20; i++)
        {
            var dept = faker.PickRandom(departments);
            var proj = new Project
            {
                Number = i,
                Name = faker.Commerce.ProductName(),
                Location = faker.Address.City(),
                DepartmentNumber = dept.Number
            };
            projects.Add(proj);
            db.projects.Add(proj);
        }
        db.SaveChanges();
        
        // 5. Seed WorksOn
        var allEmployees = managers.Concat(employees).ToList();
        var worksOn = new List<WorksOn>();
        foreach (var emp in allEmployees)
        {
            var assignedProjects = faker.Random.ListItems(projects, faker.Random.Int(1, 3));
            foreach (var proj in assignedProjects)
            {
                var w = new WorksOn(emp.SSN, proj.Number, faker.Random.Int(5, 40));
                worksOn.Add(w);
                db.worksOn.Add(w);
            }
        }
        db.SaveChanges();
        
        // 6. Seed Dependents
        foreach (var emp in allEmployees)
        {
            int count = faker.Random.Int(0, 2);
            for (int i = 0; i < count; i++)
            {
                var dep = new Dependent(
                    emp.SSN,
                    faker.Name.FirstName(),
                    faker.PickRandom('M', 'F'),
                    DateOnly.FromDateTime(faker.Date.Past(20, DateTime.Today.AddYears(-5))),
                    faker.PickRandom("Son", "Daughter", "Spouse")
                );
                db.dependents.Add(dep);
            }
        }
        db.SaveChanges();
        
        // 7. Seed Dept_Locations
        foreach (var dept in departments)
        {
            var locationCount = faker.Random.Int(1, 2);
            for (int i = 0; i < locationCount; i++)
            {
                var loc = new DepartmentLocation(dept.Number, faker.Address.City());
                db.dept_Locations.Add(loc);
            }
        }
        db.SaveChanges();

        Console.WriteLine("✔ Test data populated.");
    }
}