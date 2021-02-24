import gi
from gi.repository import Gtk

class ObjectiveWidget(Gtk.Frame):
    def __init__(self, objectives, select_objective_callback):
        Gtk.Frame.__init__(self, label="Objectives")
        self.objectives = objectives
        self.init_widget_content()

    def init_widget_content(self):
        self.content = Gtk.VBox()
        self.add(self.content)

        self.listbox = Gtk.ListBox()

        for objective in self.objectives:
            row = Gtk.ListBoxRow()
            label = Gtk.Label(f"{objective}", xalign=0)
            label.set_justify(Gtk.Justification.LEFT)
            row.add(label)
            self.listbox.add(row)
        self.content.pack_start(self.listbox, False, False, 10)