import datetime

import gi

from gui import GoalsWindow
from goal import Goal

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


def start():
    win = GoalsWindow()

    tmp_list_of_goals = [
        Goal("Do thing A", datetime.datetime(2021, 2, 15)),
        Goal("Do thing B", datetime.datetime(2021, 1, 15)), 
        Goal("Do this much longer thing named C", datetime.datetime(2021, 3, 20))
    ]
    for _, goal in enumerate(tmp_list_of_goals):
        win.add_to_goal_list(goal)

    win.show_all()

    Gtk.main()

start()

