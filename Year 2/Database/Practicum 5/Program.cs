using Bogus;

namespace Practicum_5;

class Program {

    static CompanyContext db = new CompanyContext();

    static void PopulateDB()
    {

        // Optional: Reset database (only in development)
        db.Database.EnsureDeleted();
        db.Database.EnsureCreated();

        var faker = new Faker("en");

        // 1. Seed Departments
        var departments = new List<Department>();
        for (int i = 1; i <= 10; i++)
        {
            var dept = new Department
            {
                Dnumber = i,
                Dname = faker.Commerce.Department(),
                Mgr_ssn = null, // assign later
                Mgr_start_date = DateOnly.FromDateTime(faker.Date.Past(5))
            };
            departments.Add(dept);
            db.departments.Add(dept);
        }
        db.SaveChanges();

        // 2. Seed Managers (one per department)
        var managers = new List<Employee>();
        foreach (var dept in departments)
        {
            var manager = new Employee
            {
                SSN = faker.Random.Replace("#########"),
                fName = faker.Name.FirstName(),
                Minit = faker.Random.Char('A', 'Z'),
                lName = faker.Name.LastName(),
                Bdate = DateOnly.FromDateTime(faker.Date.Past(30, DateTime.Today.AddYears(-25))),
                Address = faker.Address.FullAddress(),
                Sex = faker.PickRandom('M', 'F'),
                Salary = faker.Random.Decimal(70000, 120000),
                Super_ssn = null, // top-level managers have no supervisor
                DNo = dept.Dnumber
            };

            managers.Add(manager);
            db.employees.Add(manager);
        }
        db.SaveChanges();

        // Assign managers to departments now (after saving their SSNs)
        for (int i = 0; i < departments.Count; i++)
        {
            departments[i].Mgr_ssn = managers[i].SSN;
        }
        db.SaveChanges();

        // 3. Seed Employees (with managers as supervisors)
        var employees = new List<Employee>();
        for (int i = 0; i < 90; i++)
        {
            var dept = faker.PickRandom(departments);
            var manager = managers.First(m => m.DNo == dept.Dnumber);

            var emp = new Employee
            {
                SSN = faker.Random.Replace("#########"),
                fName = faker.Name.FirstName(),
                Minit = faker.Random.Char('A', 'Z'),
                lName = faker.Name.LastName(),
                Bdate = DateOnly.FromDateTime(faker.Date.Past(30, DateTime.Today.AddYears(-22))),
                Address = faker.Address.FullAddress(),
                Sex = faker.PickRandom('M', 'F'),
                Salary = faker.Random.Decimal(40000, 100000),
                Super_ssn = manager.SSN,
                DNo = dept.Dnumber
            };
            employees.Add(emp);
            db.employees.Add(emp);
        }

        var dept_bob = faker.PickRandom(departments);
        var manager_bob = managers.First(m => m.DNo == dept_bob.Dnumber);
        var bob = new Employee
        {
            SSN = faker.Random.Replace("#########"),
            fName = "Bob",
            Minit = faker.Random.Char('A', 'Z'),
            lName = faker.Name.LastName(),
            Bdate = DateOnly.FromDateTime(faker.Date.Past(30, DateTime.Today.AddYears(-22))),
            Address = faker.Address.FullAddress(),
            Sex = faker.PickRandom('M', 'F'),
            Salary = faker.Random.Decimal(40000, 100000),
            Super_ssn = manager_bob.SSN,
            DNo = dept_bob.Dnumber
        };
        employees.Add(bob);
        db.employees.Add(bob);

        db.SaveChanges();

        // 4. Seed Projects
        var projects = new List<Project>();
        for (int i = 1; i <= 20; i++)
        {
            var dept = faker.PickRandom(departments);
            var proj = new Project
            {
                Pnumber = i,
                Pname = faker.Commerce.ProductName(),
                Plocation = faker.Address.City(),
                DNo = dept.Dnumber
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
                var w = new WorksOn(emp.SSN, proj.Pnumber, faker.Random.Int(5, 40));
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
                var loc = new Dept_Location(dept.Dnumber, faker.Address.City());
                db.dept_Locations.Add(loc);
            }
        }
        db.SaveChanges();

        Console.WriteLine("✔ Test data populated.");
    }


    static void FindAnEmployee(string name)
    {

        
        // Find employee with name
        Employee found_emp = db.employees
            .Where(e => e.fName == name)
            .FirstOrDefault();

        if (found_emp == null) {
            Console.WriteLine("❌ No employee found.");
            return;
        }

        // 1. Department he manages
        // var managedDept = db.departments
        //     .Where(d => d.Mgr_ssn == found_emp.SSN)
        //     .FirstOrDefault();

        var managedDept = (from emp in db.employees
            join dept in db.departments
                on emp.SSN equals dept.Mgr_ssn
            where emp.fName == name
            select dept).FirstOrDefault();

        //    // Department Bob he works on
        //     var workingDept = db.departments
        //         .Where(d => d.Dnumber == found_emp.DNo)
        //         .FirstOrDefault();
        var workingDept = ( from e in db.employees
            join d in db.departments
                on e.DNo equals d.Dnumber
            where e.fName == name
            select d).FirstOrDefault();

        // 2. Projects he works on
        // var worksOnProjects = db.worksOn
        //     .Where(w => w.Essn == found_emp.SSN)
        //     .Select(w => w.Project)
        //     .ToList();
        var worksOnProjects = (from w in db.worksOn
            where w.Essn == found_emp.SSN
            select w.Project).ToList();

        // 3. Projects managed by his department
        // var departmentProjects = db.projects
        //     .Where(p => p.DNo == found_emp.DNo)
        //     .ToList();
        var departmentProjects = (from p in db.projects
            where p.DNo == found_emp.DNo
            select p).ToList();

        // OUTPUT
        Console.WriteLine();
        Console.WriteLine($"👤 Employee: {found_emp.fName} {found_emp.lName}, SSN: {found_emp.SSN}");
        Console.WriteLine($"📂 Department He Manages: {managedDept?.Dname ?? "None"}");

        Console.WriteLine("\n🛠 Projects Bob Works On:");
        foreach (var proj in worksOnProjects)
            Console.WriteLine($"- {proj.Pname} ({proj.Pnumber})");

        Console.WriteLine("\n🏗 Projects Managed by Bob's Department:");
        foreach (var proj in departmentProjects)
            Console.WriteLine($"- {proj.Pname} ({proj.Pnumber})");
    }


    static void GroupEmployeesPerDept()
    {
        var num_of_Dept = db.departments.Count();
        var total_salaries_paid = db.employees.Sum(e => e.Salary);

        Console.WriteLine();

        Console.WriteLine($"Number of Departments : {num_of_Dept }");
        Console.WriteLine($"Total amount of Salaries: {total_salaries_paid }");

        var r = from emp in db.employees
            group emp by emp.DNo into EmpsPerDept  //groups all employee records by the department number (DNo).
                //The group is named EmpsPerDept for reference in the next step.
            select new { GroupKey = EmpsPerDept.Key, //The Key of each group is the DNo (the value we grouped by).
                GroupCount = EmpsPerDept.Count() };

        var R = db.employees.ToList()
            .GroupBy(x=>x.DNo, x=>x, (k,v)=> new {GroupKey= k, GroupCount =v.Count() });

        var justforexecution = r.ToList();
        Console.WriteLine();
        foreach (var x in r) //use r or R for same output
            Console.WriteLine($"Department Nr.: {x.GroupKey}, Employees Count:{x.GroupCount}");
    }

    static void GroupEmployeesByTheirHoursofWork()
    {
        var q = from e in db.employees
            join w in db.worksOn on e.SSN equals w.Essn //Join the worksOn table on employee SSN (e.SSN) matching with the Essn field in worksOn.
            join p in db.projects on w.Pno equals p.Pnumber //Join the projects table to associate the project details using the project number (w.Pno = p.Pnumber).
            group new { e, w, p } by e.fName into ewp //Group these joined records by the employee's first name (e.fName).
            orderby ewp.Key 
            select new
            {
                ewp.Key, // The key of the group
                Values = from proj in ewp
                    select new { proj.p.Pname, proj.w.Hours }
            };

        // foreach (var x in q)
        // {
        //     Console.WriteLine(x.Key);
        //     foreach (var v in x.Values)
        //         Console.WriteLine($"-- {v.Pname}, {v.Hours}");
        //     Console.WriteLine($"================={x.Values.Sum(a => a.Hours)}");
        // }
        
        // Table header
        Console.WriteLine($"{"Employee Name",-15} {"Project Name",-25} {"Hours Worked",20} {"Total Hours",15}");
        Console.WriteLine(new string('-', 75));

        // Table rows
        foreach (var x in q)
        {
            var totalHours = x.Values.Sum(a => a.Hours);

            foreach (var v in x.Values)
            {
                Console.WriteLine($"{x.Key,-15} {v.Pname,-25} {v.Hours,20} {totalHours,15}");
            }

            Console.WriteLine(new string('-', 80));
        }

    }

    static void GroupDependentsperEmployee()
    {
        var dependentsOver18 = from e in db.employees
            join d in db.dependents on e.SSN equals d.Essn
            let age = DateTime.Today.Year - d.Bdate.Year
            where age > 18
            group d by new { e.fName, e.lName } into g
            select new
            {
                EmpName = g.Key.fName + " " + g.Key.lName,
                NrDependents = g.Count()
            };
                             
        Console.WriteLine($"{"EmpName",-25} {"NrDependents",15}");


        Console.WriteLine(new string('-', 42));

        foreach (var x in dependentsOver18)
        {
            Console.WriteLine($"{x.EmpName,-25} {x.NrDependents,15}");
        }
    }

    static void Main()
    {
        // PopulateDB();

        var selectResult = 
            from emp in db.employees
            select emp;
        
        foreach (var item in selectResult)
            Console.WriteLine($"{item.SSN}, {item.fName}, {item.Salary}");

        // FindAnEmployee("Bob");
        //GroupEmployeesPerDept();
        //GroupEmployeesByTheirHoursofWork();
        // GroupDependentsperEmployee();
    }
}