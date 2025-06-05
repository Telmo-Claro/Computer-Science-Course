using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Week_02.Migrations
{
    /// <inheritdoc />
    public partial class WorksOnsEmployees : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateIndex(
                name: "IX_Works_ons_ProjectNumber",
                table: "Works_ons",
                column: "ProjectNumber");

            migrationBuilder.AddForeignKey(
                name: "FK_Works_ons_Employees_EmployeeSSN",
                table: "Works_ons",
                column: "EmployeeSSN",
                principalTable: "Employees",
                principalColumn: "SSN",
                onDelete: ReferentialAction.Cascade);

            migrationBuilder.AddForeignKey(
                name: "FK_Works_ons_Projects_ProjectNumber",
                table: "Works_ons",
                column: "ProjectNumber",
                principalTable: "Projects",
                principalColumn: "Number",
                onDelete: ReferentialAction.Cascade);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Works_ons_Employees_EmployeeSSN",
                table: "Works_ons");

            migrationBuilder.DropForeignKey(
                name: "FK_Works_ons_Projects_ProjectNumber",
                table: "Works_ons");

            migrationBuilder.DropIndex(
                name: "IX_Works_ons_ProjectNumber",
                table: "Works_ons");
        }
    }
}
