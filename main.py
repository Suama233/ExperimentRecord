import logic
import io_layer
import DataStructure

def main_loop() -> None:
    io_layer.print_start_menu()
    general_info = DataStructure.GeneralInfo(current_stage="main")

    debug_stage_swift = [general_info.current_stage]

    while True:
        str_input = input()
        logic.receive_input(general_info, str_input)

        debug_stage_swift.append(general_info.current_stage)

if __name__ == '__main__':
    main_loop()