
class CurrentProject:
    def __init__(self,name):
        self.name = name
        self.created_time = 'Haven\'t implement project part yet.'
    def to_json(self):
        return {
            "name": self.name,
        }

class CurrentExperiment:
    def __init__(self,name,project):
        self.parent_project = project
        self.name = name
        self.created_time = ""
        self.remark = ""
        self.draft = ""
        self.attributes = {}

    def to_json(self):
        return {
            "parent_project": self.parent_project.to_json(),
            "name": self.name,
            "remark": self.remark,
            "draft": self.draft,
            "attributes": self.attributes
        }



class GeneralInfo:
    def __init__(self,current_stage):
        self.current_stage = current_stage
        #now only support one default project
        self.current_project = CurrentProject("default")
        self.current_experiment = 0