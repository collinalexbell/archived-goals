import pprint
import pymongo
import datetime

class Goal:
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline
        self.id = None
        self.tags = []

    def __str__(self):
        return f"{self.name} with deadline: {self.deadline}"

    def add_tag(self, tag):
        if type(tag) is str:
            self.tags.append(tag)
        else:
            raise Exception('tag must be a string')


class Repo:
    @classmethod
    def to_doc(cls, goal):
        return {"name": goal.name, "deadline": goal.deadline, "tags": goal.tags}

    def __init__(self):
        client = pymongo.MongoClient()
        self.db = client.holon.goals

    def get_all(self):
        return self.db.find()

    def replace(self, goal):
        update_result = self.db.replace_one(
            {"_id": goal.id}, Repo.to_doc(goal))
        return update_result.matched_count


    def save(self, goal):
        doc = Repo.to_doc(goal)
        goal.id = self.db.insert_one(doc).inserted_id
        return goal.id


    def delete(self, goal):
        if goal.id is not None:
            self.db.delete_one({"_id": goal.id})



