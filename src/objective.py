import pprint
import pymongo
import datetime

class Objective:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.id = None

    def set_id(self, id: str):
        self.id = id


class Repo:
    @classmethod
    def to_doc(cls, objective):
        return {"title": objective.title, "description": objective.description}
    
    @classmethod
    def from_doc(cls, doc):
        objective = Objective(doc['title'], doc['description'])
        objective.set_id(goal_doc['_id'])
        return objective

    def __init__(self):
        client = pymongo.MongoClient()
        self.db = client.holon.objectives

    def get_all(self):
        docs = self.db.find()
        rv = []
        for doc in docs:
            rv.append(Repo.from_doc(doc))
        return rv

    def replace(self, obj):
        update_result = self.db.replace_one(
            {"_id": obj.id}, Repo.to_doc(obj))
        return update_result.matched_count

    def save(self, obj):
        doc = Repo.to_doc(obj)
        obj.id = self.db.insert_one(doc).inserted_id
        return obj.id


    def delete(self, obj):
        if obj.id is not None:
            self.db.delete_one({"_id": obj.id})



