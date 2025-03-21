using Microsoft.AspNetCore.Mvc;
using SubjectTopicsApp.Models;
using System.Linq;

namespace SubjectTopicsApp.Controllers
{
    public class SubtopicsController : Controller
    {
        private readonly SubjectTopicsDbContext _context;

        public SubtopicsController(SubjectTopicsDbContext context)
        {
            _context = context;
        }

        [HttpGet]
        public JsonResult GetByTopic(int topicId)
        {
            var subtopics = _context.Subtopics.Where(s => s.TopicId == topicId).ToList();
            return Json(subtopics);
        }

        [HttpPost]
        public JsonResult Create(int TopicId, string SubtopicName)
        {
            if (!string.IsNullOrEmpty(SubtopicName))
            {
                var newSubtopic = new Subtopic { TopicId = TopicId, SubtopicName = SubtopicName };
                _context.Subtopics.Add(newSubtopic);
                _context.SaveChanges();
                return Json(newSubtopic);
            }
            return Json(null);
        }

        [HttpPost]
        public JsonResult Edit(int SubtopicId, string SubtopicName)
        {
            var subtopic = _context.Subtopics.Find(SubtopicId);
            if (subtopic != null)
            {
                subtopic.SubtopicName = SubtopicName;
                _context.SaveChanges();
                return Json(subtopic);
            }
            return Json(null);
        }

        [HttpPost]
        public JsonResult Delete(int SubtopicId)
        {
            var subtopic = _context.Subtopics.Find(SubtopicId);
            if (subtopic != null)
            {
                _context.Subtopics.Remove(subtopic);
                _context.SaveChanges();
                return Json(new { success = true });
            }
            return Json(new { success = false });
        }
    }
}
