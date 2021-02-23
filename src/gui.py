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
        self.listbox = Gtk.ListBox()
        self.list_of_goals = []
        self.add(self.main_box)
        self.main_box.add(self.listbox)


        self.delete_button = Gtk.Button("Delete Goal")
        self.delete_button.connect("clicked", self.delete_goal_handler)

        self.main_box.pack_end(self.add_goal_widget, True, True, 0)
        self.main_box.pack_end(self.delete_button, False, False, 10)
        self.goals_repo = repo
        self.show_all()

    def add_goal_callback(self, goal):
        self.add_to_goal_list(goal)
        self.show_all()
        self.goals_repo.save(goal)

    def add_to_goal_list(self, goal):
        self.list_of_goals.append(goal)
        row = Gtk.ListBoxRow()
        label = Gtk.Label(f"{goal}", xalign=0)
        label.set_justify(Gtk.Justification.LEFT)
        row.add(label)
        self.listbox.add(row)

    def delete_goal_handler(self, btn):
        row = self.listbox.get_selected_row()
        goal = self.list_of_goals[row.get_index()]
        del self.list_of_goals[row.get_index()]
        print(f"goal: {goal.id}")
        self.goals_repo.delete(goal)
        self.listbox.remove(row)
