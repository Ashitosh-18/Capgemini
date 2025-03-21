using Microsoft.AspNetCore.Mvc;
using SubjectTopicsApp.Models;
using Microsoft.EntityFrameworkCore;
using System.Linq;

public class SubjectTopicsController : Controller
{
    private readonly SubjectTopicsDbContext _context;

    public SubjectTopicsController(SubjectTopicsDbContext context)
    {
        _context = context;
    }

    public async Task<IActionResult> Index()
    {
        var topics = await _context.SubjectTopics.ToListAsync();
        return View(topics);
    }

    [HttpGet]
    public JsonResult GetAllTopics()
    {
        var topics = _context.SubjectTopics.ToList();
        return Json(topics);
    }

    [HttpPost]
    public JsonResult Create(string TopicName)
    {
        if (!string.IsNullOrWhiteSpace(TopicName))
        {
            var newTopic = new SubjectTopic { TopicName = TopicName };
            _context.SubjectTopics.Add(newTopic);
            _context.SaveChanges();
            return Json(new { success = true, topic = newTopic });
        }
        return Json(new { success = false });
    }

    [HttpPost]
    public JsonResult Edit(int TopicId, string TopicName)
    {
        var topic = _context.SubjectTopics.Find(TopicId);
        if (topic != null)
        {
            topic.TopicName = TopicName;
            _context.SaveChanges();
            return Json(new { success = true });
        }
        return Json(new { success = false });
    }

    [HttpPost]
    public JsonResult Delete(int TopicId)
    {
        var topic = _context.SubjectTopics.Find(TopicId);
        if (topic != null)
        {
            _context.SubjectTopics.Remove(topic);
            _context.SaveChanges();
            return Json(new { success = true });
        }
        return Json(new { success = false });
    }
}
