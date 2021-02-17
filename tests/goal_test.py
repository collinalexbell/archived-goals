import datetime
import unittest
import pprint

from goal import Goal

class TestGoal(unittest.TestCase):
    def test_add_tag(self):
        Goal.init_repo()
        mongo_goal = Goal("get mongodb working", datetime.datetime(2021, 2, 15))
        mongo_goal.save()

        goals = Goal.get_all()
        self.assertEqual(goals[0]['name'], 'get mongodb working')
        self.assertEqual(len(goals[0]['tags']), 0)

        mongo_goal.add_tag("test")
        goals = Goal.get_all()
        self.assertEqual(len(goals[0]['tags']), 1)
        self.assertEqual(goals[0]['tags'][0], 'test')

        mongo_goal.delete()

if __name__ == '__main__':
    unittest.main()
