#!/usr/bin/python3
import cmd
"""Class console"""


class HBNBCommand(cmd.Cmd):
    """Class"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_quit(self, line):
        return True

    def help_EOF(self):
        print("EOF command to exit the program")

    def emptyline(self):
        return ""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
