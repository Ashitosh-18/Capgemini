using SubjectTopicsApp.Models;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace SubjectTopicsApp.Models
{
    public class SubTopics
    {
        [Key]
        public int SubtopicID { get; set; }

        [Required]
        public string SubtopicName { get; set; }

        [Required]
        public int TopicID { get; set; }
        [ForeignKey("TopicID")]
        public Topics TopicName { get; set; }
    }
}