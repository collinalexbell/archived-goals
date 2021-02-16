import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class GoalsWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Goals")
        self.connect("destroy", Gtk.main_quit)
        self.list_of_goals = Gtk.ListBox()
        self.add(self.list_of_goals)
        self.show_all()

    def add_to_goal_list(self, goal):
        row = Gtk.ListBoxRow()
        label = Gtk.Label(f"{goal}", xalign=0)
        label.set_justify(Gtk.Justification.LEFT)
        row.add(label)
        self.list_of_goals.add(row)
