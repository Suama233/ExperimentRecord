import json

#load config.json and return a dictionary
def read_config() -> dict:
    with open('config.json', 'r', encoding='utf-8') as f:
        internal_config_file = json.load(f)
    return internal_config_file



if __name__ == '__main__':
    config_file = read_config()
