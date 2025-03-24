using System.ComponentModel.DataAnnotations;

namespace SubjectTopicsApp.Models
{
    public class Topics
    {
        [Key]
        public int TopicID { get; set; }

        [Required]
        public string TopicName { get; set; }
    }
}