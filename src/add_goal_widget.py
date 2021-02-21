import gi

from gi.repository import Gtk

class AddGoalWidget(Gtk.Frame):
    def __init__(self):
        Gtk.Frame.__init__(self, label="Add Goal")
        self.init_widget_content()

    def init_widget_content(self):
        self.content = Gtk.VBox()
        self.name_row = NameRow()
        self.date_row = DateRow()
        self.add_button = Gtk.Button(label="Add Goal")
        self.add_button.set_size_request(50, 20)

        self.content.add(self.name_row)
        self.content.add(self.date_row)
        self.content.pack_end(self.add_button, False, False, 10)
        self.add(self.content)

class DateRow(Gtk.HBox):
    def __init__(self):
        Gtk.HBox.__init__(self)
        self.calendar = Gtk.Calendar()
        self.add(self.calendar)

class NameRow(Gtk.HBox):
    def __init__(self):
        Gtk.HBox.__init__(self)
        self.add(Gtk.Label("Goal Name:"))
        self.name_input = Gtk.Entry()
        self.add(self.name_input)

