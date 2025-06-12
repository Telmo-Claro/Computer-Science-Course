using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class Department
{
    public required string Name { get; set; }
    public required string Number { get; set; }
    public string? ManagerSSN { get; set; }
    public DateTime? ManagerStartDate { get; set; }

    public Employee? DepartmentManager { get; set; }
    public IEnumerable<Employee>? Employees { get; set; }
    public IEnumerable<Project>? Projects { get; set; }
}
