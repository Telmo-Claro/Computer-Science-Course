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
    // Scalar Properties
    public string Fname { get; set; }
    public string Minit { get; set; }
    public string Lname { get; set; }
    public string Ssn { get; set; } // Primary Key
    public DateTime Bday { get; set; }
    public string Address { get; set; }
    public char Sex { get; set; }
    public int Salary { get; set; }
    public string Super_ssn { get; set; }
    public string Dno { get; set; }

    // Navigation Properties
    public Employee Supervisor { get; set; } // Done
    public ICollection<Employee> Supervisees { get; set; } // Done
    public Dependent Dependent { get; set; } // Done
    public Department ManagesDept { get; set; }
    public Department Department { get; set; } // Done
    public ICollection<Works_on> Works_on_Projects { get; set; }


}
