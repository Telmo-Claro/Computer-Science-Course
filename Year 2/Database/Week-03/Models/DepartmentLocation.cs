using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
namespace Week_03.Models;

public class DepartmentLocation
{
    // Parameterless constructor required by EF Core
    public DepartmentLocation() { }
    public DepartmentLocation(int Dno, string Dlocation) {
        this.DepartmentNumber = Dno;
        this.Location = Dlocation;
    }
    
    public int DepartmentNumber { get; set; }
    public string Location { get; set; }
    

    

}
