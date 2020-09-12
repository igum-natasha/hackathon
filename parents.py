class Human:
    def __init__(self, name: str, human_id: int):
        self.name = name
        self.id = human_id

    def get_schedule(self, human_id: int = None, subject_name: str = None):
        pass

    def get_marks(self):
        pass


class Teacher(Human):
    def __init__(self, name: str, human_id: int):
        super(Teacher, self).__init__(name, human_id)

    def set_schedule(self):
        pass

    def get_marks(self):
        pass


class Child(Human):
    def __init__(self, name: str, human_id: int, group_id):
        super(Child, self).__init__(name, human_id)
        self._group_id = group_id

    def set_goal(self):
        pass

    def get_goals(self):
        pass

    def choose_lessons(self):
        pass

    def get_marks(self):
        pass


class Parents(Human):
    def __init__(self, name: str, human_id: int, *child: Child):
        super(Parents, self).__init__(name, human_id)
        self.child = child

    def get_child_info(self, child_id: int):
        pass

    def get_marks(self):
        pass
