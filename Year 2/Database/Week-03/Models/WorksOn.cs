using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class WorksOn
{
    public required string EmployeeSSN { get; set; }
    public required string ProjectNumber { get; set; }
    public int? Hours { get; set; }

    public Employee? Employee { get; set; }
    public Project? Project { get; set; }
}