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
    win.show_all()
    Gtk.main()
start()

