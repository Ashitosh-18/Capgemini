using Microsoft.AspNetCore.Mvc;
using WebApplication1.model;

namespace WebApplication1.Controllers
{
    //[ApiController]
    //[Route("api")]
    //public class FirstController : ControllerBase

    [ApiController]
    [Route("api/[Controller]")]
    public class StudentController : ControllerBase
    {
        public static List<Student> students = new List<Student>();
        public static List<Account> accounts = new List<Account>();

        public static List<StudentAccount> studentAccounts = new List<StudentAccount>();

        [HttpPost("AddStudentAccount")]
        public IActionResult AddStudentAccount(StudentAccount studentAccount)
        {
            if (studentAccount == null)
                return BadRequest("Invalid student account data.");

            studentAccounts.Add(studentAccount);
            return Ok($"{studentAccount.StudentId} - Account linked successfully.");
        }


        [HttpGet]
        public ActionResult<List<Student>> GetStudents()
        {
            return Ok(students);
        }

        [HttpPost]
        public string AddStudent(Student student)
        {
            students.Add(student);
            return $"{student.Id} - {student.Name} Record inserted successfully";
        }

        [HttpPost("Account")]
        public string AddAccount(Account account)
        {
            accounts.Add(account);
            return $"{account.Id} - {account.AccountName} Record inserted successfully";
        }

        [HttpPut]
        public string UpdateStudent(Student student)
        {
            Student studentToUpdate = students.Find(s => s.Id == student.Id);
            studentToUpdate.Name = student.Name;
            return $"{student.Id} - {student.Name} Record updated successfully";
        }

        [HttpDelete]
        public string DeleteStudent(int id)
        {
            Student studentToDelete = students.Find(s => s.Id == id);
            students.Remove(studentToDelete);
            return $"{studentToDelete.Id} - {studentToDelete.Name} Record deleted successfully";
        }
    }
}
