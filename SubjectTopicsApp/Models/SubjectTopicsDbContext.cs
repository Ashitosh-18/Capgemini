using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;

namespace SubjectTopicsApp.Models;

public partial class SubjectTopicsDbContext : DbContext
{
    public SubjectTopicsDbContext(DbContextOptions<SubjectTopicsDbContext> options)
        : base(options)
    {
    }

    public DbSet<SubjectTopic> SubjectTopics { get; set; }
    public DbSet<Subtopic> Subtopics { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<SubjectTopic>(entity =>
        {
            entity.HasKey(e => e.TopicId).HasName("PK__SubjectT__022E0F5D271ADA1F");
            entity.Property(e => e.TopicName).HasMaxLength(255);
        });

        modelBuilder.Entity<Subtopic>(entity =>
        {
            entity.HasKey(e => e.SubtopicId).HasName("PK__Subtopic__C73C3606EDBD622A");
            entity.Property(e => e.SubtopicName).HasMaxLength(255);
            entity.HasOne(d => d.Topic)
                .WithMany(p => p.Subtopics)
                .HasForeignKey(d => d.TopicId)
                .OnDelete(DeleteBehavior.Cascade)
                .HasConstraintName("FK__Subtopics__Topic__38996AB5");
        });

        // ✅ Seed data after defining models
        modelBuilder.Entity<SubjectTopic>().HasData(
            new SubjectTopic { TopicId = 1, TopicName = "JavaScript" },
            new SubjectTopic { TopicId = 2, TopicName = "C#" }
        );

        OnModelCreatingPartial(modelBuilder);
    }

    partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
}
