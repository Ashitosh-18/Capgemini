using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using TopicApplication.Models;


namespace TopicApplication.Models
{
    public class SubTopics
    {
        [Key]
        public int SubtopicID { get; set; }

        [Required]
        public string Subtopic { get; set; }

        [Required]
        public int TopicID { get; set; }
        [ForeignKey("TopicID")]
        public Topics Topic { get; set; }
    }
}
