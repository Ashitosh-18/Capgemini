using System;
using System.Collections.Generic;

namespace SubjectTopicsApp.Models;

public partial class Subtopic
{
    public int SubtopicId { get; set; }

    public int? TopicId { get; set; }

    public string SubtopicName { get; set; } = null!;

    public virtual SubjectTopic? Topic { get; set; }
}
