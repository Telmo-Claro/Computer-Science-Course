using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class Dependent
{
    public string FirstName { get; set; }
    public string Sex { get; set; }
    public DateTime BirthDate { get; set; }
    public string Relationship { get; set; }
    public string EmployeeSSN { get; set; }

    public IEnumerable<Employee> Employees { get; set; }
}
