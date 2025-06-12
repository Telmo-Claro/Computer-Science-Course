using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class Dependent
{
    public required string FirstName { get; set; }
    public required string Sex { get; set; }
    public DateTime BirthDate { get; set; }
    public string? Relationship { get; set; }
    public string? EmployeeSSN { get; set; }

    public IEnumerable<Employee>? Dependees { get; set; }
}
