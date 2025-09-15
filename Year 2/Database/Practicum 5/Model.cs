using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using Microsoft.EntityFrameworkCore;

namespace Practicum_5;

class CompanyContext : DbContext {
    public DbSet<Employee> employees { get; set; }
    public DbSet<Department> departments { get; set; }
    public DbSet<Project> projects { get; set; }
    public DbSet<WorksOn> worksOn { get; set; }
    public DbSet<Dependent> dependents { get; set; }
    public DbSet<Dept_Location> dept_Locations { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        string UserID = "practice";
        string DBName = "Week03"; //change it accordingly
        string Host = "localhost";//127.0.0.1
        string Port = "5432";
        optionsBuilder.UseNpgsql($"User ID={UserID};Host={Host};Port={Port};Database={DBName};Pooling=true;");
        optionsBuilder.LogTo(Console.WriteLine, Microsoft.Extensions.Logging.LogLevel.Debug);
    }
            
    protected override void OnModelCreating(ModelBuilder modelBuilder) {
        modelBuilder.Entity<Department>().HasOne(x => x.Manager).WithOne().HasForeignKey<Department>(z => z.Mgr_ssn);
        modelBuilder.Entity<Department>().HasMany(x => x.EmpInDept).WithOne(y => y.Department);
        modelBuilder.Entity<Dependent>().HasKey(x => new { x.Essn, x.Dependent_name });

        modelBuilder.Entity<Project>().HasOne(x=>x.Department).WithMany(y=>y.Projects).HasForeignKey(z => z.DNo);

        modelBuilder.Entity<WorksOn>().HasOne(x => x.Project).WithMany().HasForeignKey(z => z.Pno);
        modelBuilder.Entity<WorksOn>().HasOne(x => x.Employee).WithMany().HasForeignKey(z => z.Essn);

        modelBuilder.Entity<WorksOn>().HasKey(x => new { x.Pno, x.Essn });

        modelBuilder.Entity<Dept_Location>().HasOne<Department>(x => x.Dept).WithMany().HasForeignKey(z => z.Dno);
        modelBuilder.Entity<Dept_Location>().HasKey(x => new { x.Dno, x.Dlocation });

    }
}

class Employee {

    [Required]
    public string fName { get; set; }
    public char? Minit;
    [Required]
    public string lName { get; set; }
    
    [Key, Column(TypeName ="varchar(9)")]
    public string SSN { get; set; }

    public DateOnly? Bdate { get; set; }
    public string? Address { get; set; }

    public char? Sex { get; set; }    //'M', 'F', null
    public decimal Salary { get; set; }
    
    [ForeignKey ("Super_ssn"), Column(TypeName ="varchar(9)")]
    public Employee? Supervisor { get; set; } //Referecnce nevigation property without collection property self
    public string? Super_ssn { get; set; } //Self FK
     
    [ForeignKey("DNo")]
    public Department? Department { get; set; } //Referecnce nevigation property
    public int? DNo { get; set; } //FK

    public virtual ICollection<Dependent>? Dependents { get; set; }  
    
}

class Department {
    public string Dname { get; set; }
    [Key]
    public int Dnumber { get; set; }   
    
    public Employee? Manager { get; set; }     //Reference Navigation property
    public string? Mgr_ssn { get; set; } //FK

    public DateOnly? Mgr_start_date { get; set; }
    public virtual ICollection<Employee>? EmpInDept { get; set; } 
    public virtual ICollection<Project>? Projects { get; set; }
}


class Project {
    public string Pname { get; set; }
    [Key]
    public int Pnumber { get; set; }
    public string?  Plocation { get; set; } 
    public Department? Department { get; set; }// Ref nav property
    public int? DNo { get; set; }    //FK 

    public Project() { }
    public Project(string Pname, int Pnumber, string Plocation, int Dno) { 
        this.Pname = Pname;
        this.Pnumber = Pnumber;
        this.Plocation = Plocation;
        this.DNo = Dno;
    }
}

class WorksOn {
    public Employee Employee { get; set; }
    public string Essn { get; set; }//FK //cPK

    public Project Project { get; set; } 
    public int Pno { get; set; } //FK //CPK
    
    public int Hours { get; set;}

    public WorksOn(string Essn, int Pno, int Hours) { 
        this.Essn = Essn;
        this.Pno = Pno;
        this.Hours = Hours;    
    }
}


class Dependent { 
    [ForeignKey ("Essn")]
    public Employee? Employee { get; set; }
    public string Essn { get; set; }
    public string Dependent_name { get; set; }
    public char Sex { get; set; }
    public DateOnly Bdate { get; set; }
    public string Relationship { get; set; }

    public Dependent(string Essn, string Dependent_name, char Sex, DateOnly Bdate, string Relationship) {
        this.Essn = Essn;
        this.Dependent_name = Dependent_name;
        this .Sex = Sex;
        this .Bdate = Bdate;
        this .Relationship = Relationship;
    }
}

class Dept_Location
{
    public Dept_Location(int Dno, string Dlocation) {
        this.Dno = Dno;
        this.Dlocation = Dlocation;
    }
    public Department? Dept { get; set; }
    public int Dno { get; set; }
    [Column(TypeName = "varchar(50)")]
    public string Dlocation { get; set; }
}