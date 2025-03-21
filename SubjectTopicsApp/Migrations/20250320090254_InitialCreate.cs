using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace SubjectTopicsApp.Migrations
{
    /// <inheritdoc />
    public partial class InitialCreate : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "SubjectTopics",
                columns: table => new
                {
                    TopicId = table.Column<int>(type: "int", nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    TopicName = table.Column<string>(type: "nvarchar(255)", maxLength: 255, nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK__SubjectT__022E0F5D271ADA1F", x => x.TopicId);
                });

            migrationBuilder.CreateTable(
                name: "Subtopics",
                columns: table => new
                {
                    SubtopicId = table.Column<int>(type: "int", nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    TopicId = table.Column<int>(type: "int", nullable: true),
                    SubtopicName = table.Column<string>(type: "nvarchar(255)", maxLength: 255, nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK__Subtopic__C73C3606EDBD622A", x => x.SubtopicId);
                    table.ForeignKey(
                        name: "FK__Subtopics__Topic__38996AB5",
                        column: x => x.TopicId,
                        principalTable: "SubjectTopics",
                        principalColumn: "TopicId",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateIndex(
                name: "IX_Subtopics_TopicId",
                table: "Subtopics",
                column: "TopicId");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "Subtopics");

            migrationBuilder.DropTable(
                name: "SubjectTopics");
        }
    }
}
