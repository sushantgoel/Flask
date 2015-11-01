import pypyodbc;

class Client(object):
    """description of class"""

    def __init__(self):
        __connectionString = 'Driver={SQL Server Native Client 11.0};Server=localhost;Database=QuizDB;uid=sa;pwd=Tit@nium1591'
        self.connection = pypyodbc.connect(__connectionString)
        self.cursor = self.connection.cursor()
        return

    def saveQuestion(self,title,question,answer):
        sql = ("insert into questions (questionname,description,correctanswer,categoryid) values (?,?,?,?)")
        values=[title,question,answer,1]
        self.cursor.execute(sql,values)
        self.connection.commit()
        self.connection.close()
        return

    def getQuestion(self,title):
        sql = ("select description from questions where questionname=?")
        values=[title]
        self.cursor.execute(sql,values)
        result = self.cursor.fetchone()
        question = result[0]
        self.connection.close()
        return question;

    def getAnswer(self,title):
        sql = ("select correctanswer from questions where questionname=?")
        values=[title]
        self.cursor.execute(sql,values)
        result = self.cursor.fetchone()
        answer = result[0]
        self.connection.close()
        return answer;