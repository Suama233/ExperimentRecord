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
    /new experiment\t\t\t\t\t\tTo create a new experiment
    /new project\t\t\t\t\t\tTo create a new project
    /load project <name>\t\t\t\tTo (re)load a project
    /show experiment list <name>\t\tTo show current project's all experiments
    /load experiment <name>\t\t\t\tTo load a specific experiment
    /info\t\t\t\t\t\t\t\tTo get info about the program
    """)

#print the program's information
def print_info() -> None:
    configs = utils.read_config()
    print(f"Current version: {configs["program_info"]["version"]}")
    print(f"Last update: {configs["program_info"]["latest_update_time"]}")

def print_experiment_created(current_experiment: DataStructure.CurrentExperiment) -> None:
    print(f"The experiment {current_experiment.name} has been created successfully.")

def print_current_experiment(current_experiment: DataStructure.CurrentExperiment,*args,**kwargs) -> None:
    print("*"*20)
    print("Information about current experiment:")
    print(f"Name: {current_experiment.name}")
    print("Remark: None" if current_experiment.remark is "" else f"Remark: {current_experiment.remark}")
    print(f"Belongs to '{current_experiment.parent_project}'")
    print("Attributes: None" if current_experiment.attributes is None else f"Attributes: {current_experiment.attributes.__len__()} in total")
    if current_experiment.attributes is not None:
        for attribute in current_experiment.attributes:
            print(f"\t{attribute}: {current_experiment.attributes[attribute]}")
    print("Draft: None" if current_experiment.draft is "" else f"Draft: {current_experiment.draft}")
    print("*"*20)

def debug_print_current_stage(general_info: DataStructure.GeneralInfo,*args,**kwargs) -> None:
    print(f"Current stage: {general_info.current_stage}")

def report_command_not_find(unfound_command) -> None:
    print(f"'{unfound_command}' not found.")

def report_command_invalid() -> None:
    print("Command used incorrectly.")

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
