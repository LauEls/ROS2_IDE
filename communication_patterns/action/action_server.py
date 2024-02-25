from communication_patterns.action.action import Action

class ActionServer(Action):
    def __init__(self, action_type, raw_action_name):
        super().__init__(action_type, raw_action_name)
        print("Action Server Name: ", self.action_name)

    