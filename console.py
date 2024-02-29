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
        args = HBNBCommand.split_args(line)
        try:
            class_name = args[0]
            if class_name not in globals():
                raise KeyError("** class doesn't exist **")
            else:
                class_name = globals()[args[0]]
                b = class_name()
                b.save()
                print(b.id)
        except KeyError as e:
            print(e.args[0])
        except IndexError:
            if len(args) < 1:
                print("** class name missing **")

    def do_show(self, line):
        args = HBNBCommand.split_args(line)
        try:
            class_name = args[0]
            if class_name not in globals():
                raise KeyError("** class doesn't exist **")
            else:
                instance_id = args[1]
                key = f"{class_name}.{instance_id}"
                if key not in storage.all():
                    raise KeyError("** no instance found **")
                print(storage.all()[key])
        except KeyError as e:
            print(e.args[0])
        except IndexError:
            if len(args) < 1:
                print("** class name missing **")
            elif len(args) < 2:
                print("** instance id missing **")
        
    def do_destroy(self, line):
        args = HBNBCommand.split_args(line)
        try:
            class_name = args[0]
            if class_name not in globals():
                raise KeyError("** class doesn't exist **")
            else:
                instance_id = args[1]
                key = f"{class_name}.{instance_id}"
                if key not in storage.all():
                    raise KeyError("** no instance found **")
                del storage.all()[key]
                storage.save()
        except KeyError as e:
            print(e.args[0])
        except IndexError:
            if len(args) < 1:
                print("** class name missing **")
            elif len(args) < 2:
                print("** instance id missing **")

    def do_all(self, line):
        args = HBNBCommand.split_args(line)
        if args:
            try:
                class_name = args[0]
                if class_name not in globals():
                    raise KeyError("** class doesn't exist **")
                else:
                    for v in storage.all().values():
                        if v.__class__.__name__ == class_name:
                            print(v)
            except KeyError as e:
                print(e.args[0])
        else:
            for v in storage.all().values():
                print(v)

    def do_update(self, line):
        """
        Updates an attribute of a class instance
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
            print(e.args[0])
        except IndexError:
            if len(args) < 1:
                print("** class name missing **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
