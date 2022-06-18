import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from add_goal_widget import AddGoalWidget
from manage_existing_goals_widget import ManageExistingGoalsWidget
from objective_widget import ObjectiveWidget

class GoalsWindow(Gtk.Window):
    def __init__(self, repo):
        self.goals_repo = repo
        self.goals_from_repo = repo.get_all()

        Gtk.Window.__init__(self, title="Goals")
        self.connect("destroy", Gtk.main_quit)

        self.main_box = Gtk.HBox()
        self.notes_frame = Gtk.Frame(label="Notes")
        self.notes_window = Gtk.ScrolledWindow()
        self.notes_text = Gtk.TextView()
        self.notes_text.get_buffer().connect("changed", self.update_notes)
        self.notes_window.add(self.notes_text)
        self.goal_box = Gtk.VBox()
        self.add(self.main_box)
        self.main_box.add(self.goal_box)
        self.notes_frame.add(self.notes_window)
        self.main_box.add(self.notes_frame)

        self.objectives_widget = ObjectiveWidget(
            [
            "Determination",
            "Cybernetics",
            "Business",
            "Finance",
            "Health",
            "Lifestyle",
            "Politics",
            "Reading",
            "Social"
            ], 
            self.select_objective_callback)
        self.goal_box.add(self.objectives_widget)

        self.manage_existing_goals_widget = ManageExistingGoalsWidget(self.delete_goal_callback, self.select_goal_callback)
        for goal in self.goals_from_repo:
            self.manage_existing_goals_widget.add_to_goal_list(goal)
        self.goal_box.add(self.manage_existing_goals_widget)

        self.add_goal_widget = AddGoalWidget(self.add_goal_callback)
        self.goal_box.pack_end(self.add_goal_widget, True, True, 0)

        self.show_all()

    def select_objective_callback(self):
        pass

    def select_goal_callback(self,list_box,list_box_row):
        selected_goal = self.manage_existing_goals_widget.get_selected_goal()
        buffer = self.notes_text.get_buffer()
        if selected_goal != None:
            notes = selected_goal.get_notes()
            if notes != None:
                buffer.set_text(notes)
            else:
                buffer.set_text("")
        else:
            buffer.set_text("")

    def update_notes(self, buffer):
        selected_goal = self.manage_existing_goals_widget.get_selected_goal()
        if selected_goal != None:
            new_notes = buffer.get_text(buffer.get_start_iter(), buffer.get_end_iter(), True)
            if(selected_goal.get_notes() != new_notes):
                selected_goal.update_notes(new_notes)
                self.goals_repo.replace(selected_goal)

    def add_goal_callback(self, goal):
        self.manage_existing_goals_widget.add_to_goal_list(goal)
        self.show_all()
        self.goals_repo.save(goal)

    def delete_goal_callback(self, btn):
        goal = self.manage_existing_goals_widget.get_selected_goal()
        self.goals_repo.delete(goal)

        self.manage_existing_goals_widget.delete_selected_goal()
