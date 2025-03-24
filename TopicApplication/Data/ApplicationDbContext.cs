using Microsoft.EntityFrameworkCore;
using System.Collections.Generic;
using TopicApplication.Models;

namespace TopicApplication.Data
{
    public class ApplicationDbContext : DbContext
    {

        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options)
        {
        }
        public DbSet<Topics> Topics { get; set; }
        public DbSet<SubTopics> SubTopics { get; set; }
    }
}
