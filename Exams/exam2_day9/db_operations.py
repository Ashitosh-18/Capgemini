from abc import ABC, abstractmethod

class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

class SQLDatabase(IDatabaseOperations):
    def insert(self):
        print("Inserting data into SQL")

    def update(self):
        print("Updating data in SQL")

    def delete(self):
        print("Deleting data from SQL")

class NoSQLDatabase(IDatabaseOperations):
    def insert(self):
        print("Inserting data into NoSQL")

    def update(self):
        print("Updating data in NoSQL")

    def delete(self):
        print("Deleting data from NoSQL")

sql = SQLDatabase()
nosql = NoSQLDatabase()

sql.insert()
sql.update()
sql.delete()

nosql.insert()
nosql.update()
nosql.delete()
