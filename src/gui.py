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

        self.main_box = Gtk.VBox()
        self.add(self.main_box)

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
        self.main_box.add(self.objectives_widget)

        self.manage_existing_goals_widget = ManageExistingGoalsWidget(self.delete_goal_callback)
        for goal in self.goals_from_repo:
            self.manage_existing_goals_widget.add_to_goal_list(goal)
        self.main_box.add(self.manage_existing_goals_widget)

        self.add_goal_widget = AddGoalWidget(self.add_goal_callback)
        self.main_box.pack_end(self.add_goal_widget, True, True, 0)

        self.show_all()

    def select_objective_callback(self):
        pass

    def add_goal_callback(self, goal):
        self.manage_existing_goals_widget.add_to_goal_list(goal)
        self.show_all()
        self.goals_repo.save(goal)

    def delete_goal_callback(self, btn):
        goal = self.manage_existing_goals_widget.get_selected_goal()
        self.goals_repo.delete(goal)

        self.manage_existing_goals_widget.delete_selected_goal()