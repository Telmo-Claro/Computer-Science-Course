using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
namespace Week_03.Models;

public class WorksOn
{
    public string EmployeeSSN { get; set; }
    public int ProjectNumber { get; set; }
    public int? Hours { get; set; }
    
    public WorksOn(string Essn, int Pno, int Hours)
    { 
        this.EmployeeSSN = Essn;
        this.ProjectNumber = Pno;
        this.Hours = Hours;    
    }

}