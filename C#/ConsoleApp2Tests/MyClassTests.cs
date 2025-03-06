using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Tests
{
    [TestClass()]
    public class MyClassTests
    {
        [TestMethod()]
        public void AddTest()
        {
            var myClass = new MyClass();

            // Act
            var result = myClass.Add(2, 3);

            // Assert
            Assert.AreEqual(5, result);
        }
    }
}