import datetime
import unittest
import pprint

import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))


from goal import Goal
from goal import Repo as GoalRepo

class TestGoal(unittest.TestCase):
    def test_add_tag(self):
        repo = GoalRepo()
        mongo_goal = Goal("get mongodb working", datetime.datetime(2021, 2, 15))
        repo.save(mongo_goal)

        goals = repo.get_all()
        self.assertEqual(goals[0]['name'], 'get mongodb working')
        self.assertEqual(len(goals[0]['tags']), 0)

        mongo_goal.add_tag("test")
        repo.replace(mongo_goal)
        goals = repo.get_all()
        self.assertEqual(len(goals[0]['tags']), 1)
        self.assertEqual(goals[0]['tags'][0], 'test')

        repo.delete(mongo_goal)

if __name__ == '__main__':
    unittest.main()
