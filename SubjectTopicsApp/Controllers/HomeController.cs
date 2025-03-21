using Microsoft.AspNetCore.Mvc;
using SubjectTopicsApp.Models;
using System.Linq;

public class HomeController : Controller
{
    private readonly SubjectTopicsDbContext _context;

    public HomeController(SubjectTopicsDbContext context)
    {
        _context = context; // Inject the database context
    }

    public IActionResult Index()
    {
        var topics = _context.SubjectTopics.ToList(); // Fetch topics from DB
        return View(topics);
    }

    [HttpPost]
    public IActionResult Create(SubjectTopic topic)
    {
        if (ModelState.IsValid)
        {
            _context.SubjectTopics.Add(topic);
            _context.SaveChanges(); // Save to database
            return Json(new { success = true, topic }); // Return JSON response
        }
        return Json(new { success = false });
    }
}
