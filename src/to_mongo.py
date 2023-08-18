from base import Base
from dotenv import load_dotenv
import pymongo
import os


class ToMongo(Base):

    def __init__(self, user=os.getenv('USERNAME'), password=os.getenv('PASSWORD')):
        Base.__init__(self)
        load_dotenv()
        self.user = user
        self.password = password
        self.mongo_url = os.getenv('MONGO_URL')
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client.db
        self.student = self.db.student
        self.df.reset_index(inplace=True)
    
    def upload_one_by_one(self):
        for i in self.df.index:
            self.student.insert_one(self.df.loc[i].to_dict())


if __name__ == '__main__':
    c = ToMongo()
    print('Successful Connection to Client Object')
    c.upload_one_by_one()
    print('Successfully Uploaded all student Info to Mongo')