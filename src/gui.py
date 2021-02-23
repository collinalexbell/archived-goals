import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from add_goal_widget import AddGoalWidget

class GoalsWindow(Gtk.Window):
    def __init__(self, repo):
        Gtk.Window.__init__(self, title="Goals")
        self.main_box = Gtk.VBox()
        self.add_goal_widget = AddGoalWidget(self.add_goal_callback)
        self.connect("destroy", Gtk.main_quit)
        self.list_of_goals = Gtk.ListBox()
        self.add(self.main_box)
        self.main_box.add(self.list_of_goals)
        self.main_box.add(self.add_goal_widget)
        self.goals_repo = repo
        self.show_all()

    def add_goal_callback(self, goal):
        self.add_to_goal_list(goal)
        self.show_all()
        self.goals_repo.save(goal)

    def add_to_goal_list(self, goal):
        row = Gtk.ListBoxRow()
        label = Gtk.Label(f"{goal}", xalign=0)
        label.set_justify(Gtk.Justification.LEFT)
        row.add(label)
        self.list_of_goals.add(row)
