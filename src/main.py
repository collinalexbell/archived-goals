import datetime

import gi

from gui import GoalsWindow
from goal import Goal
from goal import Repo as GoalRepo
from time import time as utc

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def log(what):
    time = utc()
    item = f"{{\"time\":{time}, \"event\":\"{what}\"}}\n"
    with open("log", "a") as log:
        log.write(item)

def log_start():
    log("start")

def log_end():
    log("end")


def start():
    log_start()
    repo = GoalRepo()
    win = GoalsWindow(repo)
    win.show_all()
    Gtk.main()
    log_end()
start()

