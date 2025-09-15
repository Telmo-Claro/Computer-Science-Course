using System;
using Microsoft.EntityFrameworkCore.Migrations;
using Npgsql.EntityFrameworkCore.PostgreSQL.Metadata;

#nullable disable

namespace Practicum_5.Migrations
{
    /// <inheritdoc />
    public partial class Initial : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "departments",
                columns: table => new
                {
                    Dnumber = table.Column<int>(type: "integer", nullable: false)
                        .Annotation("Npgsql:ValueGenerationStrategy", NpgsqlValueGenerationStrategy.IdentityByDefaultColumn),
                    Dname = table.Column<string>(type: "text", nullable: false),
                    Mgr_ssn = table.Column<string>(type: "varchar(9)", nullable: true),
                    Mgr_start_date = table.Column<DateOnly>(type: "date", nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_departments", x => x.Dnumber);
                });

            migrationBuilder.CreateTable(
                name: "dept_Locations",
                columns: table => new
                {
                    Dno = table.Column<int>(type: "integer", nullable: false),
                    Dlocation = table.Column<string>(type: "varchar(50)", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_dept_Locations", x => new { x.Dno, x.Dlocation });
                    table.ForeignKey(
                        name: "FK_dept_Locations_departments_Dno",
                        column: x => x.Dno,
                        principalTable: "departments",
                        principalColumn: "Dnumber",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateTable(
                name: "employees",
                columns: table => new
                {
                    SSN = table.Column<string>(type: "varchar(9)", nullable: false),
                    fName = table.Column<string>(type: "text", nullable: false),
                    lName = table.Column<string>(type: "text", nullable: false),
                    Bdate = table.Column<DateOnly>(type: "date", nullable: true),
                    Address = table.Column<string>(type: "text", nullable: true),
                    Sex = table.Column<char>(type: "character(1)", nullable: true),
                    Salary = table.Column<decimal>(type: "numeric", nullable: false),
                    Super_ssn = table.Column<string>(type: "varchar(9)", nullable: true),
                    DNo = table.Column<int>(type: "integer", nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_employees", x => x.SSN);
                    table.ForeignKey(
                        name: "FK_employees_departments_DNo",
                        column: x => x.DNo,
                        principalTable: "departments",
                        principalColumn: "Dnumber");
                    table.ForeignKey(
                        name: "FK_employees_employees_Super_ssn",
                        column: x => x.Super_ssn,
                        principalTable: "employees",
                        principalColumn: "SSN");
                });

            migrationBuilder.CreateTable(
                name: "projects",
                columns: table => new
                {
                    Pnumber = table.Column<int>(type: "integer", nullable: false)
                        .Annotation("Npgsql:ValueGenerationStrategy", NpgsqlValueGenerationStrategy.IdentityByDefaultColumn),
                    Pname = table.Column<string>(type: "text", nullable: false),
                    Plocation = table.Column<string>(type: "text", nullable: true),
                    DNo = table.Column<int>(type: "integer", nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_projects", x => x.Pnumber);
                    table.ForeignKey(
                        name: "FK_projects_departments_DNo",
                        column: x => x.DNo,
                        principalTable: "departments",
                        principalColumn: "Dnumber");
                });

            migrationBuilder.CreateTable(
                name: "dependents",
                columns: table => new
                {
                    Essn = table.Column<string>(type: "varchar(9)", nullable: false),
                    Dependent_name = table.Column<string>(type: "text", nullable: false),
                    Sex = table.Column<char>(type: "character(1)", nullable: false),
                    Bdate = table.Column<DateOnly>(type: "date", nullable: false),
                    Relationship = table.Column<string>(type: "text", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_dependents", x => new { x.Essn, x.Dependent_name });
                    table.ForeignKey(
                        name: "FK_dependents_employees_Essn",
                        column: x => x.Essn,
                        principalTable: "employees",
                        principalColumn: "SSN",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateTable(
                name: "worksOn",
                columns: table => new
                {
                    Essn = table.Column<string>(type: "varchar(9)", nullable: false),
                    Pno = table.Column<int>(type: "integer", nullable: false),
                    Hours = table.Column<int>(type: "integer", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_worksOn", x => new { x.Pno, x.Essn });
                    table.ForeignKey(
                        name: "FK_worksOn_employees_Essn",
                        column: x => x.Essn,
                        principalTable: "employees",
                        principalColumn: "SSN",
                        onDelete: ReferentialAction.Cascade);
                    table.ForeignKey(
                        name: "FK_worksOn_projects_Pno",
                        column: x => x.Pno,
                        principalTable: "projects",
                        principalColumn: "Pnumber",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateIndex(
                name: "IX_departments_Mgr_ssn",
                table: "departments",
                column: "Mgr_ssn",
                unique: true);

            migrationBuilder.CreateIndex(
                name: "IX_employees_DNo",
                table: "employees",
                column: "DNo");

            migrationBuilder.CreateIndex(
                name: "IX_employees_Super_ssn",
                table: "employees",
                column: "Super_ssn");

            migrationBuilder.CreateIndex(
                name: "IX_projects_DNo",
                table: "projects",
                column: "DNo");

            migrationBuilder.CreateIndex(
                name: "IX_worksOn_Essn",
                table: "worksOn",
                column: "Essn");

            migrationBuilder.AddForeignKey(
                name: "FK_departments_employees_Mgr_ssn",
                table: "departments",
                column: "Mgr_ssn",
                principalTable: "employees",
                principalColumn: "SSN");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_departments_employees_Mgr_ssn",
                table: "departments");

            migrationBuilder.DropTable(
                name: "dependents");

            migrationBuilder.DropTable(
                name: "dept_Locations");

            migrationBuilder.DropTable(
                name: "worksOn");

            migrationBuilder.DropTable(
                name: "projects");

            migrationBuilder.DropTable(
                name: "employees");

            migrationBuilder.DropTable(
                name: "departments");
        }
    }
}
