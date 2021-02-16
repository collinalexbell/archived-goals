import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class GoalsWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Goals")
        pass

    def init_window(self):
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

