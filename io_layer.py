import utils
import DataStructure

#print welcome text
def print_welcome() -> None:
    print(r"              _                           ")
    print(r"__      _____| | ___ ___  _ __ ___   ___  ")
    print(r"\ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ ")
    print(r" \ V  V /  __/ | (_| (_) | | | | | |  __/ ")
    print(r"  \_/\_/ \___|_|\___\___/|_| |_| |_|\___| ")

#print basic texts WHEN the program starts
def print_start_menu() -> None:
    print_welcome()
    print('-'*50)
    print("Type /help to get help")
    print('-'*50)

#print all commands when input is identified as "/help"
def print_help(current_stage,*args,**kwargs) -> None:
    print("""
    /help\t\t\t\t\t\t\t\tTo show all commands
    /info\t\t\t\t\t\t\t\tTo get info about the program #Not implemented yet
    /create experiment\t\t\t\t\tTo create a new experiment (and load into Create Experiment area)
    /new project\t\t\t\t\t\tTo create a new project #Not implemented yet
    /load project <name>\t\t\t\tTo (re)load a project #Not implemented yet
    /show experiment list <name>\t\tTo show current project's all experiments #Not implemented yet
    /load experiment <name>\t\t\t\tTo load a specific experiment #Not implemented yet
    
    ---Create Experiment Area---
    /show\t\t\t\t\t\t\t\t\t\tTo show current information of the experiment
    /set <variable> <value>\t\t\t\t\t\tTo create or change a variable
    \t/set name <new_name>\t\t\t\t\tTo change the name of the experiment
    \t/set <remark>/<draft> <new_content>\t\tTo change the content of the remark/draft of the experiment
    \t/set attribute <key> <value>\t\t\tTo create or change a attribute
    /save\t\t\t\t\t\t\t\t\t\tTo save the experiment
    ----------------------------  
    """)

#print the program's information
def print_info() -> None:
    configs = utils.read_config()
    print(f"Current version: {configs["program_info"]["version"]}")
    print(f"Last update: {configs["program_info"]["latest_update_time"]}")

def print_experiment_created(current_experiment: DataStructure.CurrentExperiment) -> None:
    print(f"The experiment '{current_experiment.name}' has been created successfully.")

def print_experiment_saved(current_experiment: DataStructure.CurrentExperiment,file_path:str) -> None:
    print(f"The experiment '{current_experiment.name}' has been saved in '{file_path}'.")

def print_current_experiment(current_experiment: DataStructure.CurrentExperiment,*args,**kwargs) -> None:
    print("*"*20)
    print("Information about current experiment:")
    print(f"Name: {current_experiment.name}")
    print(f"Created time: {utils.convert_custom_time_stamp(current_experiment.created_time)}")
    print("Remark: None" if current_experiment.remark is "" else f"Remark: {current_experiment.remark}")
    print(f"Belongs to '{current_experiment.parent_project}'")
    print("Attributes: None" if current_experiment.attributes is None else f"Attributes: {current_experiment.attributes.__len__()} in total")
    if current_experiment.attributes is not None:
        for attribute in current_experiment.attributes:
            print(f"\t{attribute}: {current_experiment.attributes[attribute]}")
    print("Draft: None" if current_experiment.draft is "" else f"Draft: {current_experiment.draft}")
    print("*"*20)

def print_set_variable_finished(case_type:str,**kwargs) -> None:
    if case_type == "change":
        print(f"{kwargs.get("variable_changed")} has been changed from {kwargs.get("value_before")} to {kwargs.get("value_after")}")
    elif case_type == "new":
        print(f"A new attribute {kwargs.get("key_new")} has been created with value {kwargs.get("value_new")}")

def print_remove_attribute_finished(attribute_to_remove: str) -> None:
    print(f"Attribute '{attribute_to_remove}' removed successfully.")

def report_attribute_not_found(attribute_to_remove: str) -> None:
    print(f"Attribute '{attribute_to_remove}' not found.")

def report_command_not_find(unfounded_command) -> None:
    print(f"'{unfounded_command}' not found.")

def report_command_invalid() -> None:
    print("Command used incorrectly.")

def debug_print_current_stage(general_info: DataStructure.GeneralInfo,*args,**kwargs) -> None:
    print(f"Current stage: {general_info.current_stage}")

#debug area
#----------------------
_io_layer_set={
    "print_welcome":print_welcome,
    "print_start_menu":print_start_menu,
    "print_help":print_help,
    "print_info":print_info
}
if __name__ == "__main__":
    while True:
        func = input()
        if func in _io_layer_set:
            _io_layer_set[func]()
        elif func == "exit":
            break
#----------------------
