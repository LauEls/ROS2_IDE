from communication_patterns.action.action import Action

class ActionClient(Action):
    def __init__(self, action_type, raw_action_name):
        super().__init__(action_type, raw_action_name)
        print("Action Client Name: ", self.action_name)

    