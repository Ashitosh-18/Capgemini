﻿using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using SubjectTopicsApp.Models;
using SubjectTopicsApp.Data;

namespace SubjectTopicsApp.Controllers
{
    public class SubjectTopicsController : Controller
    {
        private ApplicationDbContext dbContext;

        public SubjectTopicsController(ApplicationDbContext dbContext)
        {
            this.dbContext = dbContext;
        }
        public async Task<IActionResult> Index()
        {
            var topics = await dbContext.Topics.ToListAsync();
            return View(topics);
        }

        public async Task<IActionResult> GetSubtopics(int topicId)
        {
            var subtopics = await dbContext.SubTopics
                                           .Where(s => s.TopicID == topicId)
                                           .ToListAsync();
            ViewData["TopicID"] = topicId;
            return PartialView("_SubtopicsPartial", subtopics);
        }

        [HttpPost]
        public async Task<IActionResult> AddTopic(string topic)
        {
            if (string.IsNullOrWhiteSpace(topic))
            {
                return BadRequest("Topic name cannot be empty.");
            }

            var newTopic = new Topics { TopicName = topic };
            dbContext.Topics.Add(newTopic);
            await dbContext.SaveChangesAsync();

            return Ok(); // Sends a success response (200)
        }

        [HttpPost]
        public async Task<IActionResult> DeleteTopic(int topicId)
        {
            var subtopics = dbContext.SubTopics.Where(s => s.TopicID == topicId);
            dbContext.SubTopics.RemoveRange(subtopics); // Delete related subtopics

            var topic = await dbContext.Topics.FindAsync(topicId);
            if (topic == null)
            {
                return NotFound();
            }

            dbContext.Topics.Remove(topic); // Delete the topic itself
            await dbContext.SaveChangesAsync();

            return Ok(); // Return success response
        }

        [HttpPut]
        public async Task<IActionResult> UpdateTopic([FromBody] TopicUpdateRequest request)
        {
            if (string.IsNullOrWhiteSpace(request.TopicName))
            {
                return BadRequest("Topic name cannot be empty.");
            }

            var topic = await dbContext.Topics.FindAsync(request.TopicId);
            if (topic == null)
            {
                return NotFound();
            }

            topic.TopicName = request.TopicName;
            await dbContext.SaveChangesAsync();

            return Ok();
        }

        // Create a DTO (Data Transfer Object) for updating topics
        public class TopicUpdateRequest
        {
            public int TopicId { get; set; }
            public string TopicName { get; set; }
        }


        [HttpPost]
        public async Task<IActionResult> AddSubtopic(int topicId, string subtopic)
        {
            Console.WriteLine($"the Topic id is :{topicId}");
            if (string.IsNullOrWhiteSpace(subtopic))
            {
                return BadRequest("Subtopic name cannot be empty.");
            }

            var newSubtopic = new SubTopics { SubtopicName = subtopic, TopicID = topicId };
            dbContext.SubTopics.Add(newSubtopic);
            await dbContext.SaveChangesAsync();

            // Return the updated subtopics partial view
            var subtopics = await dbContext.SubTopics.Where(s => s.TopicID == topicId).ToListAsync();
            return PartialView("_SubtopicsPartial", subtopics);
        }


        [HttpPut]
        public async Task<IActionResult> UpdateSubtopic([FromBody] SubtopicUpdateRequest request)
        {
            if (string.IsNullOrWhiteSpace(request.SubtopicName))
            {
                return BadRequest("Subtopic name cannot be empty.");
            }

            var subtopic = await dbContext.SubTopics.FindAsync(request.SubtopicID);
            if (subtopic == null)
            {
                return NotFound();
            }

            subtopic.SubtopicName = request.SubtopicName;
            await dbContext.SaveChangesAsync();

            var subtopics = await dbContext.SubTopics.Where(s => s.TopicID == request.TopicID).ToListAsync();
            return PartialView("_SubtopicsPartial", subtopics);
        }

        [HttpPost]
        public async Task<IActionResult> DeleteSubtopic(int subtopicId)
        {
            var subtopic = await dbContext.SubTopics.FindAsync(subtopicId);
            if (subtopic == null)
            {
                return NotFound();
            }

            var topicId = subtopic.TopicID; // Get the topic ID before deletion
            dbContext.SubTopics.Remove(subtopic);
            await dbContext.SaveChangesAsync();

            var subtopics = await dbContext.SubTopics.Where(s => s.TopicID == topicId).ToListAsync();
            return PartialView("_SubtopicsPartial", subtopics);
        } 

        // DTO for updating subtopics
        public class SubtopicUpdateRequest
        {
            public int SubtopicID { get; set; }
            public string SubtopicName { get; set; }
            public int TopicID { get; set; } // Keeps track of the selected topic
        }




    }
}