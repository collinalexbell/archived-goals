import datetime

import gi

from gui import GoalsWindow
from goal import Goal
from goal import Repo as GoalRepo

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


def start():
    repo = GoalRepo()
    win = GoalsWindow(repo)

    tmp_list_of_goals = [
        Goal("Do thing A", datetime.datetime(2021, 2, 15)),
        Goal("Do thing B", datetime.datetime(2021, 1, 15)), 
        Goal("Do this much longer thing named C", datetime.datetime(2021, 3, 20))
    ]

    goals_from_repo = repo.get_all()

    goals = tmp_list_of_goals + goals_from_repo

    for _, goal in enumerate(goals):
        win.add_to_goal_list(goal)

    win.show_all()

    Gtk.main()

start()

