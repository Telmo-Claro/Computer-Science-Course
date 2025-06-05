using System;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Week_03.Migrations
{
    /// <inheritdoc />
    public partial class FirstMigration : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "Dependents",
                columns: table => new
                {
                    FirstName = table.Column<string>(type: "text", nullable: false),
                    EmployeeSSN = table.Column<string>(type: "text", nullable: false),
                    Sex = table.Column<string>(type: "text", nullable: false),
                    BirthDate = table.Column<DateTime>(type: "timestamp with time zone", nullable: false),
                    Relationship = table.Column<string>(type: "text", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Dependents", x => new { x.EmployeeSSN, x.FirstName });
                });

            migrationBuilder.CreateTable(
                name: "Dept_Locations",
                columns: table => new
                {
                    DepartmentNumber = table.Column<string>(type: "text", nullable: false),
                    Location = table.Column<string>(type: "text", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Dept_Locations", x => new { x.DepartmentNumber, x.Location });
                });

            migrationBuilder.CreateTable(
                name: "Departments",
                columns: table => new
                {
                    Number = table.Column<string>(type: "text", nullable: false),
                    Name = table.Column<string>(type: "text", nullable: false),
                    ManagerSSN = table.Column<string>(type: "text", nullable: false),
                    ManagerStartDate = table.Column<DateTime>(type: "timestamp with time zone", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Departments", x => x.Number);
                });

            migrationBuilder.CreateTable(
                name: "Employees",
                columns: table => new
                {
                    SSN = table.Column<string>(type: "text", nullable: false),
                    FirstName = table.Column<string>(type: "text", nullable: false),
                    MiddleInitials = table.Column<string>(type: "text", nullable: false),
                    LastName = table.Column<string>(type: "text", nullable: false),
                    BirthDate = table.Column<DateTime>(type: "timestamp with time zone", nullable: false),
                    Address = table.Column<string>(type: "text", nullable: false),
                    Sex = table.Column<string>(type: "text", nullable: false),
                    Salary = table.Column<int>(type: "integer", nullable: false),
                    Super_SSN = table.Column<string>(type: "text", nullable: false),
                    DepartmentNumber = table.Column<string>(type: "text", nullable: false),
                    DependentEmployeeSSN = table.Column<string>(type: "text", nullable: false),
                    DependentFirstName = table.Column<string>(type: "text", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Employees", x => x.SSN);
                    table.ForeignKey(
                        name: "FK_Employees_Departments_DepartmentNumber",
                        column: x => x.DepartmentNumber,
                        principalTable: "Departments",
                        principalColumn: "Number",
                        onDelete: ReferentialAction.Cascade);
                    table.ForeignKey(
                        name: "FK_Employees_Dependents_DependentEmployeeSSN_DependentFirstName",
                        columns: x => new { x.DependentEmployeeSSN, x.DependentFirstName },
                        principalTable: "Dependents",
                        principalColumns: new[] { "EmployeeSSN", "FirstName" },
                        onDelete: ReferentialAction.Cascade);
                    table.ForeignKey(
                        name: "FK_Employees_Employees_Super_SSN",
                        column: x => x.Super_SSN,
                        principalTable: "Employees",
                        principalColumn: "SSN",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateTable(
                name: "Projects",
                columns: table => new
                {
                    Number = table.Column<string>(type: "text", nullable: false),
                    Name = table.Column<string>(type: "text", nullable: false),
                    Location = table.Column<string>(type: "text", nullable: false),
                    DepartmentNumber = table.Column<string>(type: "text", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Projects", x => x.Number);
                    table.ForeignKey(
                        name: "FK_Projects_Departments_DepartmentNumber",
                        column: x => x.DepartmentNumber,
                        principalTable: "Departments",
                        principalColumn: "Number",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateTable(
                name: "Works_ons",
                columns: table => new
                {
                    EmployeeSSN = table.Column<string>(type: "text", nullable: false),
                    ProjectNumber = table.Column<string>(type: "text", nullable: false),
                    Hours = table.Column<int>(type: "integer", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Works_ons", x => new { x.EmployeeSSN, x.ProjectNumber });
                    table.ForeignKey(
                        name: "FK_Works_ons_Employees_EmployeeSSN",
                        column: x => x.EmployeeSSN,
                        principalTable: "Employees",
                        principalColumn: "SSN",
                        onDelete: ReferentialAction.Cascade);
                    table.ForeignKey(
                        name: "FK_Works_ons_Projects_ProjectNumber",
                        column: x => x.ProjectNumber,
                        principalTable: "Projects",
                        principalColumn: "Number",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateIndex(
                name: "IX_Departments_ManagerSSN",
                table: "Departments",
                column: "ManagerSSN",
                unique: true);

            migrationBuilder.CreateIndex(
                name: "IX_Employees_DepartmentNumber",
                table: "Employees",
                column: "DepartmentNumber");

            migrationBuilder.CreateIndex(
                name: "IX_Employees_DependentEmployeeSSN_DependentFirstName",
                table: "Employees",
                columns: new[] { "DependentEmployeeSSN", "DependentFirstName" });

            migrationBuilder.CreateIndex(
                name: "IX_Employees_Super_SSN",
                table: "Employees",
                column: "Super_SSN");

            migrationBuilder.CreateIndex(
                name: "IX_Projects_DepartmentNumber",
                table: "Projects",
                column: "DepartmentNumber");

            migrationBuilder.CreateIndex(
                name: "IX_Works_ons_ProjectNumber",
                table: "Works_ons",
                column: "ProjectNumber");

            migrationBuilder.AddForeignKey(
                name: "FK_Departments_Employees_ManagerSSN",
                table: "Departments",
                column: "ManagerSSN",
                principalTable: "Employees",
                principalColumn: "SSN",
                onDelete: ReferentialAction.Cascade);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Departments_Employees_ManagerSSN",
                table: "Departments");

            migrationBuilder.DropTable(
                name: "Dept_Locations");

            migrationBuilder.DropTable(
                name: "Works_ons");

            migrationBuilder.DropTable(
                name: "Projects");

            migrationBuilder.DropTable(
                name: "Employees");

            migrationBuilder.DropTable(
                name: "Departments");

            migrationBuilder.DropTable(
                name: "Dependents");
        }
    }
}
