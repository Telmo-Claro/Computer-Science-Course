using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class Department
{
    public string Dname { get; set; }
    public string Dnumber { get; set; }
    public Employee Mgr_ssn { get; set; }
    public DateTime Mgr_start_date { get; set; }

    public Employee Manager  { get; set; }
    public ICollection<Dept_Location> Dept_Locations { get; set; }
    public ICollection<Employee> EmployeesInDepartment { get; set; }
    public ICollection<Project> ProjectsInDepartment { get; set; }
}
