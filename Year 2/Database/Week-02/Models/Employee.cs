using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
namespace Week_02.Models;
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
    public string Super_SSN { get; set; }
    public string DepartmentNumber { get; set; }
}
