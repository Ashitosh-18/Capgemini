using System;
using System.Collections.Generic;

namespace SubjectTopicsApp.Models;

public partial class SubjectTopic
{
    public int TopicId { get; set; }

    public string TopicName { get; set; } = null!;

    public virtual ICollection<Subtopic> Subtopics { get; set; } = new List<Subtopic>();
}
