using Microsoft.AspNetCore.Mvc;
using WebApplication1.model;


// Web api is stateless
namespace WebApplication1.Controllers
{
    [ApiController]
    [Route("api")]
    public class FirstController : ControllerBase
    {
        [HttpGet]
        public string GetDateTime()
        {
            return System.DateTime.Now.ToString();
        }

        [HttpGet("GetRegionTime")]
        public string GetDateTime(string region)
        {
            return region + System.DateTime.Now.ToString();
        }

        [HttpGet("GetStudent")]
        public Student GetStudent(int rollNo, string name)
        {
            Student student = new Student();
            student.Name = name;
            student.Id = rollNo;
            return student;
        }
    }
}