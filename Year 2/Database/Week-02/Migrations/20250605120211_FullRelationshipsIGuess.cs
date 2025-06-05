using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Week_02.Migrations
{
    /// <inheritdoc />
    public partial class FullRelationshipsIGuess : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Employees_Departments_DepartmentManagingNumber",
                table: "Employees");

            migrationBuilder.DropIndex(
                name: "IX_Employees_DepartmentManagingNumber",
                table: "Employees");

            migrationBuilder.DropColumn(
                name: "DepartmentManagingNumber",
                table: "Employees");

            migrationBuilder.CreateIndex(
                name: "IX_Projects_DepartmentNumber",
                table: "Projects",
                column: "DepartmentNumber");

            migrationBuilder.CreateIndex(
                name: "IX_Departments_ManagerSSN",
                table: "Departments",
                column: "ManagerSSN",
                unique: true);

            migrationBuilder.AddForeignKey(
                name: "FK_Departments_Employees_ManagerSSN",
                table: "Departments",
                column: "ManagerSSN",
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

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Departments_Employees_ManagerSSN",
                table: "Departments");

            migrationBuilder.DropForeignKey(
                name: "FK_Projects_Departments_DepartmentNumber",
                table: "Projects");

            migrationBuilder.DropIndex(
                name: "IX_Projects_DepartmentNumber",
                table: "Projects");

            migrationBuilder.DropIndex(
                name: "IX_Departments_ManagerSSN",
                table: "Departments");

            migrationBuilder.AddColumn<string>(
                name: "DepartmentManagingNumber",
                table: "Employees",
                type: "text",
                nullable: false,
                defaultValue: "");

            migrationBuilder.CreateIndex(
                name: "IX_Employees_DepartmentManagingNumber",
                table: "Employees",
                column: "DepartmentManagingNumber",
                unique: true);

            migrationBuilder.AddForeignKey(
                name: "FK_Employees_Departments_DepartmentManagingNumber",
                table: "Employees",
                column: "DepartmentManagingNumber",
                principalTable: "Departments",
                principalColumn: "Number",
                onDelete: ReferentialAction.Cascade);
        }
    }
}
