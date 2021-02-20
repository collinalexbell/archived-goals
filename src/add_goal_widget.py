import gi

from gi.repository import Gtk

class AddGoalWidget(Gtk.Frame):
    def __init__(self):
        Gtk.Frame.__init__(self, label="Add Goal")
