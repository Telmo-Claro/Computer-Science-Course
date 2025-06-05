using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Week_02.Migrations
{
    /// <inheritdoc />
    public partial class EmployeeSuperSSN : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<string>(
                name: "Super_SSN",
                table: "Employees",
                type: "text",
                nullable: false,
                defaultValue: "");

            migrationBuilder.CreateIndex(
                name: "IX_Employees_Super_SSN",
                table: "Employees",
                column: "Super_SSN");

            migrationBuilder.AddForeignKey(
                name: "FK_Employees_Employees_Super_SSN",
                table: "Employees",
                column: "Super_SSN",
                principalTable: "Employees",
                principalColumn: "SSN",
                onDelete: ReferentialAction.Cascade);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Employees_Employees_Super_SSN",
                table: "Employees");

            migrationBuilder.DropIndex(
                name: "IX_Employees_Super_SSN",
                table: "Employees");

            migrationBuilder.DropColumn(
                name: "Super_SSN",
                table: "Employees");
        }
    }
}
