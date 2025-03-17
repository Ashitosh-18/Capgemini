using System;
using System.Collections.Generic;
using System.Linq;
abstract class AbstractLogger
{
    public abstract void Log(string message);
    public virtual void LogWarning(string message)
    {
        Console.WriteLine("Warning: " + message);
    }
}

interface ILoggerInterface
{
    void Log(string message);
}

class FileLogger : AbstractLogger
{
    public override void Log(string message)
    {
        Console.WriteLine("Logging to file: " + message);
    }
}
