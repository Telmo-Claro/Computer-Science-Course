using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Week_03.Models;

namespace Week_03.Models;

public class Employee
{
    
    public string SSN { get; set; } // Primary Key
    public string FirstName { get; set; }
    public char MiddleInitials { get; set; }
    public string LastName { get; set; }
    public DateOnly BirthDate { get; set; }
    public string Address { get; set; }
    public char Sex { get; set; }
    public decimal Salary { get; set; }
    public string? Super_SSN { get; set; }
    public int DepartmentNumber { get; set; }
}
