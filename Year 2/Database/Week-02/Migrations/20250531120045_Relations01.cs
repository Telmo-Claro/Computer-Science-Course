using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Week_02.Migrations
{
    /// <inheritdoc />
    public partial class Relations01 : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<string>(
                name: "DepartmentManagingNumber",
                table: "Employees",
                type: "text",
                nullable: false,
                defaultValue: "");

            migrationBuilder.AddColumn<string>(
                name: "DependentEmployeeSSN",
                table: "Employees",
                type: "text",
                nullable: false,
                defaultValue: "");

            migrationBuilder.AddColumn<string>(
                name: "DependentFirstName",
                table: "Employees",
                type: "text",
                nullable: false,
                defaultValue: "");

            migrationBuilder.CreateIndex(
                name: "IX_Employees_DepartmentManagingNumber",
                table: "Employees",
                column: "DepartmentManagingNumber",
                unique: true);

            migrationBuilder.CreateIndex(
                name: "IX_Employees_DependentEmployeeSSN_DependentFirstName",
                table: "Employees",
                columns: new[] { "DependentEmployeeSSN", "DependentFirstName" });

            migrationBuilder.AddForeignKey(
                name: "FK_Employees_Departments_DepartmentManagingNumber",
                table: "Employees",
                column: "DepartmentManagingNumber",
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
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Employees_Departments_DepartmentManagingNumber",
                table: "Employees");

            migrationBuilder.DropForeignKey(
                name: "FK_Employees_Dependents_DependentEmployeeSSN_DependentFirstName",
                table: "Employees");

            migrationBuilder.DropIndex(
                name: "IX_Employees_DepartmentManagingNumber",
                table: "Employees");

            migrationBuilder.DropIndex(
                name: "IX_Employees_DependentEmployeeSSN_DependentFirstName",
                table: "Employees");

            migrationBuilder.DropColumn(
                name: "DepartmentManagingNumber",
                table: "Employees");

            migrationBuilder.DropColumn(
                name: "DependentEmployeeSSN",
                table: "Employees");

            migrationBuilder.DropColumn(
                name: "DependentFirstName",
                table: "Employees");
        }
    }
}
