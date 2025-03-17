using System;

interface ILogger
{
    void Save();
}

interface IDatabaseSaver
{
    void Save();
}

class DataManager : ILogger, IDatabaseSaver
{
    void ILogger.Save()
    {
        Console.WriteLine("Logging data...");
    }

    void IDatabaseSaver.Save()
    {
        Console.WriteLine("Saving data to database...");
    }
}