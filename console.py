#!/usr/bin/python3
"""Console"""


import cmd


class HBNBCommand(cmd.Cmd):
    """class called HBNB wich creates custom prompt for the interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """exits the program when EOF is executed"""
        print()
        return True

    def emptyline(self):
        """do nothing when empty line + ENTER are executed"""
        pass

    def help_quit(self):
        """Print help message for quit command"""
        print("Quit command to exit the program.")
        print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
