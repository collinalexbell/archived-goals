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
        self.tags = []

    def __str__(self):
        return f"{self.name} with deadline: {self.deadline}"

    def add_tag(self, tag):
        if type(tag) is str:
            self.tags.append(tag)
            self.replace()
        else:
            raise Exception('tag must be a string')

    def to_doc(self):
        return {"name": self.name, "deadline": self.deadline, "tags": self.tags}

    def replace(self):
        update_result = self.repo.replace_one(
            {"_id": self.doc_id}, self.to_doc())
        return update_result.matched_count


    def save(self):
        doc = self.to_doc()
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
    mongo_goal.add_tag("test")
    goals = Goal.get_all()
    for goal in goals:
        pprint.pprint(goal)

    mongo_goal.delete()
    
