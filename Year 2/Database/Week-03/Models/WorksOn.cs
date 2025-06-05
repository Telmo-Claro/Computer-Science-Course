using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class WorksOn
{
    public string EmployeeSSN { get; set; }
    public string ProjectNumber { get; set; }
    public int Hours { get; set; }

    public Employee Employee { get; set; }
    public Project Project { get; set; }
}