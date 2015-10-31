import redis

class Client(object):
    """description of class"""

    def __init__(self):
        #constructor
        #connect to Redis
        self.__r = redis.StrictRedis('localhost',port=6379,db=0,charset="utf-8",decode_responses=True)

    def saveQuestion(self,title,question,answer):
        #Store data in database
        #Key name will be the title they type in :question
        self.__r.set(title + ':question', question)
        self.__r.set(title + ':answer',answer)

    def getQuestion(self,title):
        #send the user the form        
        #Read question from Database
        question = self.r.get(title+':question')
        return question
    
    def getAnswer(self,title):
        #Read answer from DB
        answer = self.r.get(title + ':answer')
        return answer


