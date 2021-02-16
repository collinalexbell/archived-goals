import pprint
import pymongo
import datetime

class Goal:
    @classmethod
    def init_repo(cls):
        client = pymongo.MongoClient()
        cls.repo = client.holon.goals

    @classmethod
    def get_all(cls):
        return cls.repo.find()

    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline
        self.doc_id = None

    def __str__(self):
        return f"{self.name} with deadline: {self.deadline}"
    
    def save(self):
        doc = {"name": self.name, "deadline": self.deadline}
        self.doc_id = self.repo.insert_one(doc).inserted_id
        return self.doc_id

    def delete(self):
        if self.doc_id is not None:
            self.repo.delete_one({"_id": self.doc_id})


if __name__ == "__main__":
    Goal.init_repo()
    mongo_goal = Goal("get mongodb working", datetime.datetime(2021, 2, 15))
    mongo_goal.save()
    goals = Goal.get_all()
    for goal in goals:
        pprint.pprint(goal)
    mongo_goal.delete()
    
