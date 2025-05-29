using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/*
 * One department -> many locations
 * One department -> many projects
 * One employee -> One department
 * One employee -> Many projects
 * One employee -> one supervisor (employee)
 * One employee -> many supervisee
 * One employee -> Many dependents
 * Many employee -> works for -> One department
 * Many employees -> works_on -> many projects
 * One employee -> Manages -> One department
 */

public class Employee
{
    public string SSN { get; set; } // Primary Key
    public string FirstName { get; set; }
    public string MiddleInitials { get; set; }
    public string LastName { get; set; }
    public DateTime BirthDate { get; set; }
    public string Address { get; set; }
    public string Sex { get; set; }
    public int Salary { get; set; }

    public Employee Supervisor { get; set; }
    public IEnumerable<Employee> Supervisees { get; set; }

    public string DepartmentNumber { get; set; }
    public Department Department { get; set; }

    public Object DependentKey {  get; set; }
    public Dependent Dependent { get; set; }
}
