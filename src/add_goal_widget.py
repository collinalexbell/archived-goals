import datetime

import gi
from gi.repository import Gtk

from goal import Goal

class AddGoalWidget(Gtk.Frame):
    def __init__(self, callback):
        Gtk.Frame.__init__(self, label="Add Goal")
        self.callback = callback
        self.init_widget_content()

    def init_widget_content(self):
        self.content = Gtk.VBox()
        self.name_row = NameRow()
        self.date_row = DateRow()
        self.add_button = Gtk.Button(label="Add Goal")
        self.add_button.connect("clicked", self.action_handler)

        self.content.add(self.name_row)
        self.content.add(self.date_row)
        self.content.pack_end(self.add_button, False, False, 10)
        self.add(self.content)

    def action_handler(self, btn):
        name = self.name_row.get_value()
        date = self.date_row.get_value()
        goal = Goal(name, datetime.datetime(date[0], date[1]+1, date[2]))
        self.callback(goal)

class DateRow(Gtk.HBox):
    def __init__(self):
        Gtk.HBox.__init__(self)
        self.calendar = Gtk.Calendar()
        self.add(self.calendar)

    def get_value(self):
        return self.calendar.get_date()

class NameRow(Gtk.HBox):
    def __init__(self):
        Gtk.HBox.__init__(self)
        self.add(Gtk.Label("Goal Name:"))
        self.name_input = Gtk.Entry()
        self.add(self.name_input)
    
    def get_value(self):
        return self.name_input.get_text()

