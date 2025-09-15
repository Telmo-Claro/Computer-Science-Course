using Microsoft.EntityFrameworkCore;
using Week_03.Models;

namespace Week_03;

public class CompanyContext : DbContext
{
    public DbSet<Employee> employees { get; set; }
    public DbSet<Department> departments { get; set; }
    public DbSet<Project> projects { get; set; }
    public DbSet<WorksOn> worksOn { get; set; }
    public DbSet<Dependent> dependents { get; set; }
    public DbSet<DepartmentLocation> dept_Locations { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        string UserID = "postgres";
        string DBName = "Week03"; //change it accordingly
        string Host = "localhost";//127.0.0.1
        string Port = "5432";
        optionsBuilder.UseNpgsql($"User ID={UserID};Host={Host};Port={Port};Database={DBName};Pooling=true;");
        optionsBuilder.LogTo(Console.WriteLine, Microsoft.Extensions.Logging.LogLevel.Debug);
    }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Employee>()
            .HasKey(x => x.SSN);

        modelBuilder.Entity<Department>()
            .HasKey(x => x.Number);



        modelBuilder.Entity<Project>()
            .HasKey(x => x.Number);

        modelBuilder.Entity<WorksOn>()
            .HasKey(x => new { x.EmployeeSSN, x.ProjectNumber });

        modelBuilder.Entity<Dependent>()
            .HasKey(x => new { x.EmployeeSSN, x.FirstName });
        
        
        // Builds one-to-one Department Manager
        modelBuilder.Entity<Department>()
            .HasOne<Employee>()
            .WithOne()
            .HasForeignKey<Department>(d => d.ManagerSSN);
        
        // Builds one-to-many Department Employee
        modelBuilder.Entity<Employee>()
            .HasOne<Department>()
            .WithMany()
            .HasForeignKey(d => d.DepartmentNumber);

        // One-to-many Supervisee Supervisor 
        modelBuilder.Entity<Employee>()
            .HasOne<Employee>()
            .WithMany()
            .HasForeignKey(e => e.Super_SSN);
        
        // One to many Dependee Dependents (employee)
        modelBuilder.Entity<Dependent>()
            .HasOne<Employee>()
            .WithMany()
            .HasForeignKey(d => d.EmployeeSSN);
        
        // One to many Project Departments
        modelBuilder.Entity<Project>()
            .HasOne<Department>()
            .WithMany()
            .HasForeignKey(d => d.DepartmentNumber);
        
        // many-to-many
        modelBuilder.Entity<WorksOn>()
            .HasOne<Employee>()
            .WithMany()
            .HasForeignKey(e => e.EmployeeSSN);
        modelBuilder.Entity<WorksOn>()
            .HasOne<Project>()
            .WithMany()
            
            .HasForeignKey(p => p.ProjectNumber);
        // One to many Location to Departments
        modelBuilder.Entity<DepartmentLocation>()
            .HasOne<Department>()
            .WithMany()
            .HasForeignKey(d => d.DepartmentNumber);
        
        modelBuilder.Entity<DepartmentLocation>()
            .HasKey(x => new { x.DepartmentNumber, x.Location });

    }
}
