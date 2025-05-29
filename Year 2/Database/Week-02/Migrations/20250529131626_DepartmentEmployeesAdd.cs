using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Week_02.Migrations
{
    /// <inheritdoc />
    public partial class DepartmentEmployeesAdd : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<string>(
                name: "DepartmentNumber",
                table: "Employees",
                type: "text",
                nullable: false,
                defaultValue: "");

            migrationBuilder.CreateIndex(
                name: "IX_Employees_DepartmentNumber",
                table: "Employees",
                column: "DepartmentNumber");

            migrationBuilder.AddForeignKey(
                name: "FK_Employees_Departments_DepartmentNumber",
                table: "Employees",
                column: "DepartmentNumber",
                principalTable: "Departments",
                principalColumn: "Number",
                onDelete: ReferentialAction.Cascade);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Employees_Departments_DepartmentNumber",
                table: "Employees");

            migrationBuilder.DropIndex(
                name: "IX_Employees_DepartmentNumber",
                table: "Employees");

            migrationBuilder.DropColumn(
                name: "DepartmentNumber",
                table: "Employees");
        }
    }
}
