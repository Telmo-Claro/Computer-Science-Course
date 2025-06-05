using System.ComponentModel.DataAnnotations;
using System.Security.Cryptography.X509Certificates;
using Microsoft.EntityFrameworkCore;
public class Model
{
    public class MyContext : DbContext
    {
        public DbSet<Employee> Employees { get; set; }
        public DbSet<Dependent> Dependents { get; set; }
        public DbSet<Department> Departments { get; set; }
        public DbSet<DepartmentLocation> Dept_Locations { get; set; }
        public DbSet<Project> Projects { get; set; }
        public DbSet<WorksOn> Works_ons { get; set; }

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
                .HasKey(e => e.SSN);
            modelBuilder.Entity<Dependent>()
                .HasKey(d => new { d.EmployeeSSN, d.FirstName });
            modelBuilder.Entity<WorksOn>()
                .HasKey(wo => new { wo.EmployeeSSN, wo.ProjectNumber });
            modelBuilder.Entity<Project>()
                .HasKey(pr => pr.Number);
            modelBuilder.Entity<DepartmentLocation>()
                .HasKey(ld => new { ld.DepartmentNumber, ld.Location });
            modelBuilder.Entity<Department>()
                .HasKey(d => d.Number);

            modelBuilder.Entity<Employee>()
                .HasOne<Employee>(e => e.Supervisor)
                .WithMany(s => s.Supervisees)
                .HasForeignKey(e => e.Super_SSN);

            modelBuilder.Entity<Employee>()
                .HasOne<Department>(x=>x.DepartmentWorking)
                .WithMany(x => x.Employees)
                .HasForeignKey(f => f.DepartmentNumber);

            modelBuilder.Entity<Employee>()
                .HasOne<Department>(x => x.DepartmentManaging)
                .WithOne(y => y.DepartmentManager)
                .HasForeignKey<Department>(f => f.ManagerSSN);

            modelBuilder.Entity<WorksOn>()
                .HasOne<Employee>(wo => wo.Employee)
                .WithMany(e => e.Projects)
                .HasForeignKey(wo => wo.EmployeeSSN);
            modelBuilder.Entity<WorksOn>()
                .HasOne<Project>(wo => wo.Project)
                .WithMany(p => p.WorksOns)
                .HasForeignKey(wo => wo.ProjectNumber);

            modelBuilder.Entity<Project>()
                .HasOne<Department>(p => p.Department)
                .WithMany(d => d.Projects)
                .HasForeignKey(p => p.DepartmentNumber);
        }
    }
}