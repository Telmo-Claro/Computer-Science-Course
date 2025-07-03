using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Security.Cryptography.X509Certificates;
using Microsoft.EntityFrameworkCore;
using Week_02.Models;

namespace Week_02;

/*
 * The goal of this week:
 * Make a new DB using the one from week01 but this time with Entity Framework
 */

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
            string DBName = "Week02"; //change it accordingly
            string Host = "localhost";//127.0.0.1
            string Port = "5432";
            optionsBuilder.UseNpgsql($"User ID={UserID};Host={Host};Port={Port};Database={DBName};Pooling=true;");
            optionsBuilder.LogTo(Console.WriteLine, Microsoft.Extensions.Logging.LogLevel.Debug);
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Employee>()
                .HasKey(e => e.SSN);

            modelBuilder.Entity<Department>()
                .HasKey(d => d.Number);

            modelBuilder.Entity<DepartmentLocation>()
                .HasKey(ld => new { ld.DepartmentNumber, ld.Location });

            modelBuilder.Entity<Project>()
                .HasKey(pr => pr.Number);

            modelBuilder.Entity<WorksOn>()
                .HasKey(wo => new { wo.EmployeeSSN, wo.ProjectNumber });

            modelBuilder.Entity<Dependent>()
                .HasKey(d => new { d.EmployeeSSN, d.FirstName });

            // one-to-one with Department
            modelBuilder.Entity<Employee>()
                .HasOne<Department>()
                .WithMany()
                .HasForeignKey(d => d.DepartmentNumber);

            modelBuilder.Entity<Employee>()
                .HasOne<Employee>()
                .WithMany()
                .HasForeignKey(e => e.Super_SSN);

            modelBuilder.Entity<DepartmentLocation>()
                .HasOne<Department>()
                .WithMany()
                .HasForeignKey(d => d.DepartmentNumber);

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

            modelBuilder.Entity<Dependent>()
                .HasOne<Employee>()
                .WithMany()
                .HasForeignKey(d => d.EmployeeSSN);
        }
    }
}