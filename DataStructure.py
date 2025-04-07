
class CurrentProject:
    def __init__(self,name):
        self.name = name

class CurrentExperiment:
    def __init__(self,name,project):
        self.parent_project = project
        self.name = name
        self.remark = ""
        self.draft = ""
        self.attributes = {}

class GeneralInfo:
    def __init__(self,current_stage):
        self.current_stage = current_stage
        #now only support one default project
        self.current_project = CurrentProject("default")
        self.current_experiment = 0