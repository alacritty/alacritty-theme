# Interactive program for show and change color themes of alcritty configuration
from pathlib import Path
import os
import sys
import argparse

#env variables
# Absolut paths
HOME_PATH = os.environ.get("HOME")
CONFIG_PATH =  HOME_PATH+"/.config/alacritty/"
CONFIG_FILE = "alacritty.toml"
CONFIG_FILE_PATH = CONFIG_PATH + CONFIG_FILE
THEMES_PATH = CONFIG_PATH+"themes/themes/"
THEMES_EXTENSION = ".toml"
#  Marks of where is the import of color theme
MARK_INIT_THEME_CONFIG = "#init_theme"
MARK_END_THEME_CONFIG = "#end_theme"



"""
Returns all the files with a specified extension in the specified path
"""
def get_files_with_extension(path: str, extension: str) -> list[str]:
    files = []
    for file in os.listdir(path):
        if file.endswith(extension):
            files.append(file)
    return files

"""
Extract from the string the substring at the end, if the strings contains it
and return the string without the subtring
"""
def extract_final_substring(string: str, substring: str):
    index = string.find(substring)
    return string[0:index] if index != -1 else None
    
"""
Truns the given iterable into a columnify representable, by sorting the objects 
insede by lenght of its string representation, so it can be pretty divided in
'equal' colums
"""
def columnify(iterable):
    # First convert everything to its repr
    strings = [repr(x) for x in iterable]
    # Now pad all the strings to match the widest
    widest = max(len(x) for x in strings)
    padded = [x.ljust(widest) for x in strings]
    return padded

"""
Print into the standard output the contains of the iterable in a 'preatty' way, print 
the elements by columns with the same length
"""
def colprint(iterable):
    size = os.get_terminal_size()
    width = size.columns
    columns = columnify(iterable)
    colwidth = len(columns[0])+2
    perline = (width-4) // colwidth
    print("  ",end="")
    for i, column in enumerate(columns):
        print(str(column), end='  ')
        if i % perline == perline-1:
            print('\n  ', end='')
    print("")

"""
Show the themes in the alacritty themes path

Raises:
    FileNotFoundError: If the new theme or config file or themes path dosent exits
"""
def show_themes(path:str = THEMES_PATH, extension: str=THEMES_EXTENSION, initial_name: str=""):

    themes_path_check = Path(path)
    if not themes_path_check.exists():
        raise FileNotFoundError("Error: Theme path didnt exist: "+path)
    
    themes = get_files_with_extension(path, extension)
    if initial_name != "":
        themes = list(filter(lambda x: x.startswith(initial_name), themes))
    if len(themes) == 0: return
    #take the extension out
    themes = list(map(lambda x: extract_final_substring(x, extension), themes))

    colprint(themes)

"""
Returns a tuple with the first index and the last index of the elements 
of list in between the given marks

    init_mark = index of initial element mark
    end_mark = index of last element mark
"""
def get_lines_between_marks(list_lines: list, init_mark, end_mark) -> tuple[int, int]:
    
    init: int = None
    end: int = None
    #search fo the marks in the list
    for i, line in enumerate(list_lines):
        if init_mark in line:
            init = i
        elif end_mark in line:
            end = i
    return (init, end)

"""
Repalce the color theme of the alactritty configuration with the provided one
Args:
    new_theme: str  
        String name of the new theme to set (without the extension).
    config_file_path: str, default=CONFIG_FILE_PATH 
        Path of the config file of alacritty.
    themes_path: str, default=THEMES_PATH 
        Path o the directory with the file.
    init_mark: str, default=MARK_INIT_THEME_CONFIG 
        Initial mark of the theme import in configuration file.
    end_mark: str, default=MARK_END_THEME_CONFIG 
        Last mark of the theme import in configuration file.
    extension: str, default=THEMES_EXTENSION
        Extension that should have the theme file
Raises:
    FileNotFoundError: If the new theme or config file or themes path dosent exits
    LookupError: If the init and end marks arent in the file
"""
def replace_theme(new_theme: str, config_file_path: str=CONFIG_FILE_PATH
                  , themes_path: str=THEMES_PATH
                  , init_mark: str=MARK_INIT_THEME_CONFIG, end_mark:str =MARK_END_THEME_CONFIG
                  , extension: str=THEMES_EXTENSION):

    with open(config_file_path, 'r') as file:
        lines = file.readlines()

    theme_file: str = themes_path + new_theme + extension
    theme_file_path_check = Path(theme_file)
    themes_path_check = Path(themes_path)
    config_file_path_check =  Path(config_file_path)
    
    if not config_file_path_check.exists():
        raise FileNotFoundError("Error: Not found config file: "+config_file_path)
    
    elif not themes_path_check.exists():
        raise FileNotFoundError("Error: Not found directory of themes: "+themes_path)

    elif not theme_file_path_check.exists():
        raise FileNotFoundError('Error: Not found theme: '+new_theme+ " in path " +themes_path)

    new_lines: str = ["import = [\n", '\t"' +theme_file+ '"\n', "]\n"]

    init, end = get_lines_between_marks(lines, init_mark=init_mark, end_mark=end_mark)

    if init is not None and end is not None:
        # Replace the line
        lines[init + 1:end] = new_lines
        # print the result
        with open(config_file_path, 'w') as file:
            file.writelines(lines)
        return new_theme

    else:
        raise LookupError("Error: Didnt found the initial and en mark lines for import color theme \n Initial mark before import: " + init_mark
                          + "\n End mark after the import: " + end_mark)

"""
Return the actual the of colors in the config file
Args:
    config_file_path: str, default=CONFIG_FILE_PATH 
        Path of the config file of alacritty.
    themes_path: str, default=THEMES_PATH 
        Path o the directory with the file.
    init_mark: str, default=MARK_INIT_THEME_CONFIG 
        Initial mark of the theme import in configuration file.
    end_mark: str, default=MARK_END_THEME_CONFIG 
        Last mark of the theme import in configuration file.
    extension: str, default=THEMES_EXTENSION
        Extension that should have the theme file
Raises:
    FileNotFoundError: If the new theme or config file or themes path dosent exits
    LookupError: If the init and end marks arent in the file
"""
def get_actual_theme(config_file_path: str=CONFIG_FILE_PATH, themes_path: str=THEMES_PATH
                     , init_mark: str=MARK_INIT_THEME_CONFIG, end_mark:str =MARK_END_THEME_CONFIG
                     , extension=THEMES_EXTENSION) -> str:

    with open(config_file_path, 'r') as file:
        lines: list[str] = file.readlines()

    themes_path_check = Path(themes_path)
    config_file_path_check =  Path(config_file_path)
    
    if not config_file_path_check.exists():
        raise FileNotFoundError("Error: Not found config file: "+config_file_path)
    
    elif not themes_path_check.exists():
        raise FileNotFoundError("Error: Not found directory of themes: "+themes_path)
    
    init, end = get_lines_between_marks(lines, init_mark=MARK_INIT_THEME_CONFIG, end_mark=MARK_END_THEME_CONFIG)

    if init == None or end == None:
        raise LookupError("Error: Didnt found the initial and en mark lines for import color theme \n Initial mark before import: " 
                            + init_mark 
                            + "\n End mark after the import: " 
                            + end_mark)

    import_lines: list[str] = list(map(lambda x: x.strip().strip('"'), lines[init + 1:end]))
    path_line = list(filter(lambda x: x.startswith(themes_path), import_lines))[0]
    path_list = path_line.split("/")
    return extract_final_substring(path_list[len(path_list)-1], extension)


"""
Interactive window for show and change of themes of alacritty
"""
def interactive_window():
    print("=================================================")
    print("Alacritty color theme selector")
    print("=================================================")
    print("Option (1): Show themes in config path")
    print("Option (2): Change theme")
    print("Option (3): Get name of actual theme")
    print("Other = exit")
    print("=================================================")
    election: str = input("Enter option: ")

    if election == "1":
        name: str = input("Enter init name of search (default all): ")
        show_themes(initial_name=name)
    elif election == "2":
        name_theme: str = input("Enter the name of the new theme: ")
        theme = replace_theme(name_theme,  init_mark=MARK_INIT_THEME_CONFIG, end_mark=MARK_END_THEME_CONFIG)
        print(f'Changed theme to {theme}')
    elif election == "3":
        print(f"Actual theme: "+get_actual_theme())
    else: return

"""
Fuction in charge of command execute
"""
def main():

    all_str_op_show_themes = "all"

    # parser for user interact in command line
    parser = argparse.ArgumentParser(description="Script for fast alacritty color theme selector using imports. Alacritty config file should content (init) and (end) mark before and after the import of theme.")
    
    parser.add_argument("--actual"
                        , dest='actual_theme'
                        , action="store_true"
                        , default=""
                        , help="Show the actual color theme used in config file.")

    parser.add_argument("--set"
                        , dest='change_theme'
                        , nargs=1
                        , type=str
                        , metavar="theme_name"
                        , help="Change the theme to the provided one (dont put extension to the theme name).")

    parser.add_argument("--showthemes"
                        , dest="show_in_path"
                        , action="store"
                        , default=''
                        , nargs='?'
                        , type=str
                        , metavar='"init_name"'
                        , help='Shows the themes with a given initial name, to show all use [--showthemes '+all_str_op_show_themes+']')

    parser.add_argument("--configfile"
                        , dest="config_file_path"
                        , action="store"
                        , default=CONFIG_FILE_PATH
                        , nargs= 1
                        , type=str
                        , metavar="config_file_path"
                        , help="Change the path of config file of alacritty, default='"+CONFIG_FILE_PATH+"'.")

    parser.add_argument("--themespath"
                        , dest="themes_path"
                        , action="store"
                        , default=THEMES_PATH
                        , nargs=1
                        , type=str
                        , metavar="themes_path"
                        , help="Change the path of were are the themes, default='"+THEMES_PATH+"'.")

    parser.add_argument("--themesextension"
                        , dest="themes_extension"
                        , action="store"
                        , default=THEMES_EXTENSION
                        , nargs=1
                        , type=str
                        , metavar=".ext"
                        , help="Change the extension of themes files, default='"+THEMES_EXTENSION+"'.")

    parser.add_argument("--initmark"
                        , dest="init_mark"
                        , action="store"
                        , default=MARK_INIT_THEME_CONFIG
                        , nargs=1
                        , type=str
                        , metavar="#init_theme"
                        , help="Set the inital mark of importation theme in config file, default='"+MARK_INIT_THEME_CONFIG+"'.")

    parser.add_argument("--endmark"
                        , dest="end_mark"
                        , action="store"
                        , default=MARK_END_THEME_CONFIG
                        , nargs=1
                        , type=str
                        , metavar="#end_theme"
                        , help="Set the last mark of importation theme in config file, default='"+MARK_END_THEME_CONFIG+"'.")


    args = parser.parse_args()
    
    call_get_actual_theme = args.actual_theme

    change_theme = args.change_theme
    if type(change_theme) is list: change_theme = change_theme[0]

    show_in_path = args.show_in_path

    config_file_path = args.config_file_path
    if type(config_file_path) is list: config_file_path = config_file_path[0]

    themes_path = args.themes_path
    if type(themes_path) is list: themes_path = themes_path[0]

    themes_extension = args.themes_extension
    if type(themes_extension) is list: themes_extension = themes_extension[0]

    init_mark = args.init_mark
    if type(init_mark) is list: init_mark = init_mark[0]

    end_mark = args.end_mark
    if type(end_mark) is list: end_mark = end_mark[0]

    """print(change_theme)
    print(show_in_path)
    print(config_file_path)
    print(themes_path)
    print(themes_extension)
    print(init_mark)
    print(end_mark)"""

    if call_get_actual_theme:
        try:
            actual = get_actual_theme(config_file_path=config_file_path, themes_path=themes_path, init_mark=init_mark, end_mark=end_mark, extension=themes_extension)
            print(f"Actual theme => [{actual}]")
        except Exception as e:
            print(e)
            return 1 
        return 0

    elif show_in_path:
        try:
            if show_in_path == all_str_op_show_themes: 
                show_in_path = ""
            show_themes(initial_name=show_in_path, path=themes_path, extension=themes_extension)
        except Exception as e:
            print(e)
            return 1 
        return 0
    
    elif change_theme:
        try:
            theme = replace_theme(change_theme, config_file_path=config_file_path, themes_path=themes_path, init_mark=init_mark, end_mark=end_mark, extension=themes_extension)
            print(f'Changed theme to {theme}')
        except Exception as e:
            print(e)
            return 1
        return 0
    else:
        parser.print_help()


if __name__ == "__main__": 
     exit(main())
