#!/usr/bin/env python3

from loguru import logger
from simple_term_menu import TerminalMenu


from dict_decomp_words import dict_decomposition

options = [(f"[{x[0]}] {x[1]}") for x in enumerate(dict_decomposition)]

logger.add(
    "log/ddm.log",
    format="{time}, {level}, {message}",
    level="INFO",
    rotation="00:00",
    compression="zip",
)

main_menu = TerminalMenu(options)

@logger.catch
def ddm(options):
    quitting = False

    while quitting == False:
        print("Data Scientist\n(с)Яндекс.Практикум\nДекомпозиция:")
        options_index = main_menu.show()
        options_choice = options[options_index]
        dict_value = (f"{options_choice.split('] ')[1]}")

        if options_choice == '[9] выход':
            quitting = True
        else:
            dict_meaning = dict_decomposition[dict_value]
            print(f"{options_choice.split('] ')[1]:*^80}")

            for i in dict_meaning:
                print(f'\t{i}')

            print('*' * 80)

ddm(options)
