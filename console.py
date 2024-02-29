#!/usr/bin/python3
"""Class console"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """Class"""
    prompt = "(hbnb) "

    @staticmethod
    def split_args(line):
        # Regex pattern to match quoted strings or non-whitespace characters
        pattern = r'"[^"]*"|\S+'
        return re.findall(pattern, line)

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
            print("** class name missing **")
            return
        try:
            class_name = globals()[args[0]]
        except KeyError:
            print("** class doesn't exist **")
            return

        b = class_name()
        b.save()
        print(b.id)

    def do_show(self, line):
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            if class_name not in globals():
                raise KeyError
            else:
                key = class_name
        except KeyError:
            print("** class doesn't exist **")
            return
        try:
            instance_id = args[1]
            key += '.' + instance_id
        except IndexError:
            print("** instance id missing **")
            return
        try:
            print(storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            if class_name not in globals():
                raise KeyError
            else:
                key = class_name
        except KeyError:
            print("** class doesn't exist **")
            return

        try:
            instance_id = args[1]
            key += '.' + instance_id
        except IndexError:
            print("** instance id missing **")
            return

        try:
            if key not in storage.all():
                raise KeyError
            else:
                del storage.all()[key]
                storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        args = line.split()
        if args:
            try:
                class_name = args[0]
                if class_name not in globals():
                    raise KeyError
                else:
                    for k, v in storage.all().items():
                        print(v)
            except KeyError:
                print("** class doesn't exist **")
                return
        else:
            for k, v in storage.all().items():
                print(v)

    def do_update(self, line):
        """
        Updates an attributae of a class instance
        stored in the global storage.

        Args:
            line (str): The user input line containing update arguments.

        Returns:
                None
        """

        args = HBNBCommand.split_args(line)

        """
        Error Handling
        """

        try:
            class_name = args[0]
            if class_name not in globals():
                raise KeyError("** class doesn't exist **")
            else:
                instance_id = args[1]
                key = f"{class_name}.{instance_id}"
                if key not in storage.all():
                    raise KeyError("** no instance found **")

            instance = storage.all()[key]
            attribute_name = args[2]
            attribute_value = args[3]
            setattr(instance, attribute_name, attribute_value)
            storage.save
        except KeyError as e:
            print(e)
        except IndexError:
            if len(args) < 1:
                print("** class name missing **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif len(args) < 3:
                print("** attributae name missing **")
            elif len(args) < 4:
                print("** value missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
