using Microsoft.EntityFrameworkCore;
using SubjectTopicsApp.Models;
using System.Collections.Generic;

namespace SubjectTopicsApp.Data
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
