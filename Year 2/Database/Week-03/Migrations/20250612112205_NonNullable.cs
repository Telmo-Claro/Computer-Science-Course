using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Week_03.Migrations
{
    /// <inheritdoc />
    public partial class NonNullable : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Employees_Departments_DepartmentNumber",
                table: "Employees");

            migrationBuilder.DropForeignKey(
                name: "FK_Employees_Dependents_DependentEmployeeSSN_DependentFirstName",
                table: "Employees");

            migrationBuilder.DropForeignKey(
                name: "FK_Employees_Employees_Super_SSN",
                table: "Employees");

            migrationBuilder.DropForeignKey(
                name: "FK_Projects_Departments_DepartmentNumber",
                table: "Projects");

            migrationBuilder.AlterColumn<int>(
                name: "Hours",
                table: "Works_ons",
                type: "integer",
                nullable: true,
                oldClrType: typeof(int),
                oldType: "integer");

            migrationBuilder.AlterColumn<string>(
                name: "DepartmentNumber",
                table: "Projects",
                type: "text",
                nullable: true,
                oldClrType: typeof(string),
                oldType: "text");

            migrationBuilder.AlterColumn<string>(
                name: "Super_SSN",
                table: "Employees",
                type: "text",
                nullable: true,
                oldClrType: typeof(string),
                oldType: "text");

            migrationBuilder.AlterColumn<string>(
                name: "MiddleInitials",
                table: "Employees",
                type: "text",
                nullable: true,
                oldClrType: typeof(string),
                oldType: "text");

            migrationBuilder.AlterColumn<string>(
                name: "DependentFirstName",
                table: "Employees",
                type: "text",
                nullable: true,
                oldClrType: typeof(string),
                oldType: "text");

            migrationBuilder.AlterColumn<string>(
                name: "DependentEmployeeSSN",
                table: "Employees",
                type: "text",
                nullable: true,
                oldClrType: typeof(string),
                oldType: "text");

            migrationBuilder.AlterColumn<string>(
                name: "DepartmentNumber",
                table: "Employees",
                type: "text",
                nullable: true,
                oldClrType: typeof(string),
                oldType: "text");

            migrationBuilder.AlterColumn<string>(
                name: "Relationship",
                table: "Dependents",
                type: "text",
                nullable: true,
                oldClrType: typeof(string),
                oldType: "text");

            migrationBuilder.AddForeignKey(
                name: "FK_Employees_Departments_DepartmentNumber",
                table: "Employees",
                column: "DepartmentNumber",
                principalTable: "Departments",
                principalColumn: "Number");

            migrationBuilder.AddForeignKey(
                name: "FK_Employees_Dependents_DependentEmployeeSSN_DependentFirstName",
                table: "Employees",
                columns: new[] { "DependentEmployeeSSN", "DependentFirstName" },
                principalTable: "Dependents",
                principalColumns: new[] { "EmployeeSSN", "FirstName" });

            migrationBuilder.AddForeignKey(
                name: "FK_Employees_Employees_Super_SSN",
                table: "Employees",
                column: "Super_SSN",
                principalTable: "Employees",
                principalColumn: "SSN");

            migrationBuilder.AddForeignKey(
                name: "FK_Projects_Departments_DepartmentNumber",
                table: "Projects",
                column: "DepartmentNumber",
                principalTable: "Departments",
                principalColumn: "Number");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Employees_Departments_DepartmentNumber",
                table: "Employees");

            migrationBuilder.DropForeignKey(
                name: "FK_Employees_Dependents_DependentEmployeeSSN_DependentFirstName",
                table: "Employees");

            migrationBuilder.DropForeignKey(
                name: "FK_Employees_Employees_Super_SSN",
                table: "Employees");

            migrationBuilder.DropForeignKey(
                name: "FK_Projects_Departments_DepartmentNumber",
                table: "Projects");

            migrationBuilder.AlterColumn<int>(
                name: "Hours",
                table: "Works_ons",
                type: "integer",
                nullable: false,
                defaultValue: 0,
                oldClrType: typeof(int),
                oldType: "integer",
                oldNullable: true);

            migrationBuilder.AlterColumn<string>(
                name: "DepartmentNumber",
                table: "Projects",
                type: "text",
                nullable: false,
                defaultValue: "",
                oldClrType: typeof(string),
                oldType: "text",
                oldNullable: true);

            migrationBuilder.AlterColumn<string>(
                name: "Super_SSN",
                table: "Employees",
                type: "text",
                nullable: false,
                defaultValue: "",
                oldClrType: typeof(string),
                oldType: "text",
                oldNullable: true);

            migrationBuilder.AlterColumn<string>(
                name: "MiddleInitials",
                table: "Employees",
                type: "text",
                nullable: false,
                defaultValue: "",
                oldClrType: typeof(string),
                oldType: "text",
                oldNullable: true);

            migrationBuilder.AlterColumn<string>(
                name: "DependentFirstName",
                table: "Employees",
                type: "text",
                nullable: false,
                defaultValue: "",
                oldClrType: typeof(string),
                oldType: "text",
                oldNullable: true);

            migrationBuilder.AlterColumn<string>(
                name: "DependentEmployeeSSN",
                table: "Employees",
                type: "text",
                nullable: false,
                defaultValue: "",
                oldClrType: typeof(string),
                oldType: "text",
                oldNullable: true);

            migrationBuilder.AlterColumn<string>(
                name: "DepartmentNumber",
                table: "Employees",
                type: "text",
                nullable: false,
                defaultValue: "",
                oldClrType: typeof(string),
                oldType: "text",
                oldNullable: true);

            migrationBuilder.AlterColumn<string>(
                name: "Relationship",
                table: "Dependents",
                type: "text",
                nullable: false,
                defaultValue: "",
                oldClrType: typeof(string),
                oldType: "text",
                oldNullable: true);

            migrationBuilder.AddForeignKey(
                name: "FK_Employees_Departments_DepartmentNumber",
                table: "Employees",
                column: "DepartmentNumber",
                principalTable: "Departments",
                principalColumn: "Number",
                onDelete: ReferentialAction.Cascade);

            migrationBuilder.AddForeignKey(
                name: "FK_Employees_Dependents_DependentEmployeeSSN_DependentFirstName",
                table: "Employees",
                columns: new[] { "DependentEmployeeSSN", "DependentFirstName" },
                principalTable: "Dependents",
                principalColumns: new[] { "EmployeeSSN", "FirstName" },
                onDelete: ReferentialAction.Cascade);

            migrationBuilder.AddForeignKey(
                name: "FK_Employees_Employees_Super_SSN",
                table: "Employees",
                column: "Super_SSN",
                principalTable: "Employees",
                principalColumn: "SSN",
                onDelete: ReferentialAction.Cascade);

            migrationBuilder.AddForeignKey(
                name: "FK_Projects_Departments_DepartmentNumber",
                table: "Projects",
                column: "DepartmentNumber",
                principalTable: "Departments",
                principalColumn: "Number",
                onDelete: ReferentialAction.Cascade);
        }
    }
}
