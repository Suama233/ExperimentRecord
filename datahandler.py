import DataStructure
import io_layer
import time
import json
from pathlib import Path

import utils


def set_experiment_created_time(current_experiment: DataStructure.CurrentExperiment) -> None:
    current_time = time.time()
    time_array = time.localtime(current_time)
    time_style_changed = time.strftime("%Y_%m_%d_%H_%M_%S", time_array)
    current_experiment.created_time = time_style_changed

def save_current_experiment(current_experiment: DataStructure.CurrentExperiment) -> None:
    file_path = utils.get_json_path(opt='relative',current_experiment=current_experiment)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(current_experiment.__dict__, f, ensure_ascii=False, indent=4)
    io_layer.print_experiment_saved(current_experiment,utils.get_json_path(opt="absolute",current_experiment=current_experiment))

#input_list be like: ['attr1','attr2',...]
def remove_attributes(current_experiment: DataStructure.CurrentExperiment,input_list: list) -> None:
    for attribute_to_remove in input_list:
        if attribute_to_remove in current_experiment:
            io_layer.report_attribute_not_found(attribute_to_remove)
        current_experiment.attributes.pop(attribute_to_remove)
        io_layer.print_remove_attribute_finished(attribute_to_remove)

#input_list be like: ['name',...],['draft','...'],['attribute','attr1','value1']
def set_variables(current_experiment: DataStructure.CurrentExperiment,input_list: list) -> None:
    if input_list[0] not in ['name','remark','draft','attribute']:
        io_layer.report_command_invalid()
    elif input_list[0] in ['name','remark','draft']:
        value_before = getattr(current_experiment,input_list[0])
        setattr(current_experiment,input_list[0],input_list[1])
        io_layer.print_set_variable_finished(case_type = "change" ,variable_changed = input_list[0],value_before = value_before,value_after = input_list[1])
    elif input_list[0] == 'attribute':
        if input_list[1] in current_experiment.attributes:
            value_before = current_experiment.attributes[input_list[1]]
            current_experiment.attributes[input_list[1]] = input_list[2]
            io_layer.print_set_variable_finished(case_type="change",variable_changed = input_list[0], value_before=value_before,value_after=input_list[2])
        else:
            current_experiment.attributes[input_list[1]] = input_list[2]
            io_layer.print_set_variable_finished(case_type="new",key_new = input_list[1], value_new=input_list[2])
