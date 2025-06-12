using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class Project
{
    public required string Name { get; set; }
    public required string Number { get; set; }
    public required string Location { get; set; }
    public string? DepartmentNumber { get; set; }

    public IEnumerable<WorksOn>? WorksOns { get; set; }
    public Department? Department { get; set; }
}
