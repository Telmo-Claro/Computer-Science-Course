using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
namespace Week_03.Models;

public class Dependent
{
    public string EmployeeSSN { get; set; }
    public string FirstName { get; set; }
    public char Sex { get; set; }
    public DateOnly BirthDate { get; set; }
    public string Relationship { get; set; }
    
    public Dependent(string Essn, string Dependent_name, char Sex, DateOnly Bdate, string Relationship) {
        this.EmployeeSSN = Essn;
        this.FirstName = Dependent_name;
        this.Sex = Sex;
        this.BirthDate = Bdate;
        this.Relationship = Relationship;
    }
}
