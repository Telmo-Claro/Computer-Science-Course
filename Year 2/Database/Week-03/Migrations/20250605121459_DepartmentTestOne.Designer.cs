﻿// <auto-generated />
using System;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Migrations;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;
using Npgsql.EntityFrameworkCore.PostgreSQL.Metadata;

#nullable disable

namespace Week_03.Migrations
{
    [DbContext(typeof(Model.MyContext))]
    [Migration("20250605121459_DepartmentTestOne")]
    partial class DepartmentTestOne
    {
        /// <inheritdoc />
        protected override void BuildTargetModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder
                .HasAnnotation("ProductVersion", "9.0.5")
                .HasAnnotation("Relational:MaxIdentifierLength", 63);

            NpgsqlModelBuilderExtensions.UseIdentityByDefaultColumns(modelBuilder);

            modelBuilder.Entity("Department", b =>
                {
                    b.Property<string>("Number")
                        .HasColumnType("text");

                    b.Property<string>("ManagerSSN")
                        .IsRequired()
                        .HasColumnType("text");

                    b.Property<DateTime>("ManagerStartDate")
                        .HasColumnType("timestamp with time zone");

                    b.Property<string>("Name")
                        .IsRequired()
                        .HasColumnType("text");

                    b.HasKey("Number");

                    b.HasIndex("ManagerSSN")
                        .IsUnique();

                    b.ToTable("Departments");
                });

            modelBuilder.Entity("DepartmentLocation", b =>
                {
                    b.Property<string>("DepartmentNumber")
                        .HasColumnType("text");

                    b.Property<string>("Location")
                        .HasColumnType("text");

                    b.HasKey("DepartmentNumber", "Location");

                    b.ToTable("Dept_Locations");
                });

            modelBuilder.Entity("Dependent", b =>
                {
                    b.Property<string>("EmployeeSSN")
                        .HasColumnType("text");

                    b.Property<string>("FirstName")
                        .HasColumnType("text");

                    b.Property<DateTime>("BirthDate")
                        .HasColumnType("timestamp with time zone");

                    b.Property<string>("Relationship")
                        .IsRequired()
                        .HasColumnType("text");

                    b.Property<string>("Sex")
                        .IsRequired()
                        .HasColumnType("text");

                    b.HasKey("EmployeeSSN", "FirstName");

                    b.ToTable("Dependents");
                });

            modelBuilder.Entity("Employee", b =>
                {
                    b.Property<string>("SSN")
                        .HasColumnType("text");

                    b.Property<string>("Address")
                        .IsRequired()
                        .HasColumnType("text");

                    b.Property<DateTime>("BirthDate")
                        .HasColumnType("timestamp with time zone");

                    b.Property<string>("DepartmentNumber")
                        .IsRequired()
                        .HasColumnType("text");

                    b.Property<string>("DependentEmployeeSSN")
                        .IsRequired()
                        .HasColumnType("text");

                    b.Property<string>("DependentFirstName")
                        .IsRequired()
                        .HasColumnType("text");

                    b.Property<string>("FirstName")
                        .IsRequired()
                        .HasColumnType("text");

                    b.Property<string>("LastName")
                        .IsRequired()
                        .HasColumnType("text");

                    b.Property<string>("MiddleInitials")
                        .IsRequired()
                        .HasColumnType("text");

                    b.Property<int>("Salary")
                        .HasColumnType("integer");

                    b.Property<string>("Sex")
                        .IsRequired()
                        .HasColumnType("text");

                    b.Property<string>("Super_SSN")
                        .IsRequired()
                        .HasColumnType("text");

                    b.HasKey("SSN");

                    b.HasIndex("DepartmentNumber");

                    b.HasIndex("Super_SSN");

                    b.HasIndex("DependentEmployeeSSN", "DependentFirstName");

                    b.ToTable("Employees");
                });

            modelBuilder.Entity("Project", b =>
                {
                    b.Property<string>("Number")
                        .HasColumnType("text");

                    b.Property<string>("DepartmentNumber")
                        .IsRequired()
                        .HasColumnType("text");

                    b.Property<string>("Location")
                        .IsRequired()
                        .HasColumnType("text");

                    b.Property<string>("Name")
                        .IsRequired()
                        .HasColumnType("text");

                    b.HasKey("Number");

                    b.HasIndex("DepartmentNumber");

                    b.ToTable("Projects");
                });

            modelBuilder.Entity("WorksOn", b =>
                {
                    b.Property<string>("EmployeeSSN")
                        .HasColumnType("text");

                    b.Property<string>("ProjectNumber")
                        .HasColumnType("text");

                    b.Property<int>("Hours")
                        .HasColumnType("integer");

                    b.HasKey("EmployeeSSN", "ProjectNumber");

                    b.HasIndex("ProjectNumber");

                    b.ToTable("Works_ons");
                });

            modelBuilder.Entity("Department", b =>
                {
                    b.HasOne("Employee", "DepartmentManager")
                        .WithOne("DepartmentManaging")
                        .HasForeignKey("Department", "ManagerSSN")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.Navigation("DepartmentManager");
                });

            modelBuilder.Entity("Employee", b =>
                {
                    b.HasOne("Department", "DepartmentWorking")
                        .WithMany("Employees")
                        .HasForeignKey("DepartmentNumber")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.HasOne("Employee", "Supervisor")
                        .WithMany("Supervisees")
                        .HasForeignKey("Super_SSN")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.HasOne("Dependent", "Dependent")
                        .WithMany("Dependees")
                        .HasForeignKey("DependentEmployeeSSN", "DependentFirstName")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.Navigation("DepartmentWorking");

                    b.Navigation("Dependent");

                    b.Navigation("Supervisor");
                });

            modelBuilder.Entity("Project", b =>
                {
                    b.HasOne("Department", "Department")
                        .WithMany("Projects")
                        .HasForeignKey("DepartmentNumber")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.Navigation("Department");
                });

            modelBuilder.Entity("WorksOn", b =>
                {
                    b.HasOne("Employee", "Employee")
                        .WithMany("Projects")
                        .HasForeignKey("EmployeeSSN")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.HasOne("Project", "Project")
                        .WithMany("WorksOns")
                        .HasForeignKey("ProjectNumber")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.Navigation("Employee");

                    b.Navigation("Project");
                });

            modelBuilder.Entity("Department", b =>
                {
                    b.Navigation("Employees");

                    b.Navigation("Projects");
                });

            modelBuilder.Entity("Dependent", b =>
                {
                    b.Navigation("Dependees");
                });

            modelBuilder.Entity("Employee", b =>
                {
                    b.Navigation("DepartmentManaging")
                        .IsRequired();

                    b.Navigation("Projects");

                    b.Navigation("Supervisees");
                });

            modelBuilder.Entity("Project", b =>
                {
                    b.Navigation("WorksOns");
                });
#pragma warning restore 612, 618
        }
    }
}
