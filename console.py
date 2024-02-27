#!/usr/bin/python3
"""Class console"""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
