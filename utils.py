import json
from datetime import datetime
from pathlib import Path
import DataStructure


#load config.json and return a dictionary
def read_config() -> dict:
    with open('config.json', 'r', encoding='utf-8') as f:
        internal_config_file = json.load(f)
    return internal_config_file

def convert_custom_time_stamp(time_stamp:str) -> str:
    time_stamp_raw = datetime.strptime(time_stamp, '%Y_%m_%d_%H_%M_%S')
    return time_stamp_raw.strftime('%Y/%m/%d %H:%M:%S')

def get_json_path(opt:str,current_experiment:DataStructure.CurrentExperiment)->str:
    relative_file_path = "Datas/default/" + current_experiment.created_time + ".json"
    relative_path_path = Path(relative_file_path)
    relative_path_path.parent.mkdir(parents=True, exist_ok=True)
    if opt == "absolute":
        return relative_path_path.absolute().as_posix()
    elif opt == "relative":
        return relative_file_path
if __name__ == '__main__':
    config_file = read_config()
