import gi
from gi.repository import Gtk

class ManageExistingGoalsWidget(Gtk.Frame):
    def __init__(self, delete_button_callback, select_goal_callback):
        Gtk.Frame.__init__(self, label="Manage Existing Goals")
        self.delete_button_callback = delete_button_callback
        self.select_goal_callback = select_goal_callback
        self.init_widget_content()

    def init_widget_content(self):
        self.content = Gtk.VBox()
        self.add(self.content)

        self.scrolled_window = Gtk.ScrolledWindow()
        self.content.add(self.scrolled_window)


        self.listbox = Gtk.ListBox()
        self.listbox.connect("row-selected", self.select_goal_callback)
        self.list_of_goals = []
        self.scrolled_window.add(self.listbox)


        self.delete_button = Gtk.Button("Delete Goal")
        self.delete_button.connect("clicked", self.delete_button_callback)
        self.content.pack_end(self.delete_button, False, False, 10)


    def add_to_goal_list(self, goal):
        self.list_of_goals.append(goal)
        row = Gtk.ListBoxRow()
        label = Gtk.Label(f"{goal}", xalign=0)
        label.set_justify(Gtk.Justification.LEFT)
        row.add(label)
        self.listbox.add(row)

    def get_selected_goal(self):
        row = self.listbox.get_selected_row()
        if row != None:
            return self.list_of_goals[row.get_index()]
        else:
            return None

    def delete_selected_goal(self):
        row = self.listbox.get_selected_row()
        if(row != None):
            del self.list_of_goals[row.get_index()]
            self.listbox.remove(row)
        else:
            print("row didn't exist")

