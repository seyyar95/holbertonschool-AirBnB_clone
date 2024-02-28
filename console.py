#!/usr/bin/python3
"""Class console"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Class"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """do_EOF"""
        return True

    def help_quit(self):
        """help"""
        print("Quit command to exit the program")

    def do_quit(self, line):
        """do_quit"""
        return True

    def help_EOF(self):
        """help EOF"""
        print("EOF command to exit the program")

    def emptyline(self):
        """empty"""
        return ""

    def do_create(self, line):
        args = line.split()
        if not args:
            print("*** class name missing ***")
            return

        try:
            class_name = globals()[args[0]]
        except KeyError:
            print("*** class doesn't exist ***")
            return

        b = class_name()
        b.save()
        print(b.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
