import io_layer
import utils
import datahandler
import debugger
import DataStructure
import shlex

#change stage
def stage_change(general_info: DataStructure.GeneralInfo,next_stage: str) -> None:
    general_info.current_stage = next_stage

def receive_input(general_info: DataStructure.GeneralInfo, str_input: str) -> None:
    state_handler[general_info.current_stage](general_info,shlex.split(str_input))

#handle state
# ---------------------------------------
def handle_state_main(general_info: DataStructure.GeneralInfo,input_list: list) -> None:
    try:
        commands_main[input_list[0]](general_info, input_list[1:])
    except KeyError:
        io_layer.report_command_not_find(input_list[0])


def handle_state_create_experiment(general_info: DataStructure.GeneralInfo,input_list: list) -> None:
    if not input_list:
        io_layer.report_command_invalid()
    else:
        try:
            commands_creat_experiment[input_list[0]](general_info, input_list[1:])
        except KeyError:
            io_layer.report_command_not_find(input_list[0])


def handle_state_show_experiment(general_info: DataStructure.GeneralInfo,input_list: list) -> None:
    try:
        commands_show_experiment[input_list[0]](general_info, input_list[1:])
    except KeyError:
        io_layer.report_command_not_find(input_list[0])

# ---------------------------------------

#handle commands in main stage
#Unified input: general_info: DataStructure,input_list: list
# ---------------------------------------
def create_experiment_general(general_info: DataStructure.GeneralInfo,input_list) -> None:
    if not input_list:
        io_layer.report_command_invalid()
    else:
        stage_change(general_info,"create_experiment")
        general_info.current_experiment = DataStructure.CurrentExperiment(' '.join(input_list),general_info.current_project.name)
        io_layer.print_experiment_created(general_info.current_experiment)

# ---------------------------------------

#handle commands in create_experiment stage
#Unified input: general_info: DataStructure,input_list: list
# ---------------------------------------
def ce_set(general_info: DataStructure,input_list: list) -> None:
    pass

def ce_show(general_info:DataStructure,input_list: list) -> None:
    if input_list:
        io_layer.report_command_invalid()
    io_layer.print_current_experiment(general_info.current_experiment)

def ce_save(general_info: DataStructure,input_list: list) -> None:
    pass
# ---------------------------------------




def debug(general_info: DataStructure.GeneralInfo,input_list) -> None:
    try:
        commands_debug[input_list[0]](general_info, input_list[1:])
    except KeyError:
        io_layer.report_command_not_find(input_list[0])


commands_debug = {
    "current_stage":io_layer.debug_print_current_stage,
    "switch_stage": stage_change,
}

#to handle current_state
# ---------------------------------------
state_handler = {
    "main": handle_state_main,
    "create_experiment": handle_state_create_experiment,
    "show_experiment": handle_state_show_experiment,
}
# ---------------------------------------

#to direct commands
# ---------------------------------------
commands_universal = {
    "/help": io_layer.print_help,
    "/debug": debug,
}
commands_main = {
    **commands_universal,
    "/create": create_experiment_general,
}
commands_creat_experiment = {
    **commands_universal,
    "/set": ce_set,
    "/show": ce_show,
}
commands_show_experiment = {
    **commands_universal,
    "/commands": print("/commands called")
}
# ---------------------------------------
