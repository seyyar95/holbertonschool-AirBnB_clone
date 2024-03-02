#!/usr/bin/python3
"""
Class console
This class defines an interactive command-line interface (CLI)
for the HBNB application.
It inherits from the `cmd.CMD` class provided by the `cmd` module,
which offers basic functionalities for building command-line interfaces

"""
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
    """
    Prompt displayed before each user input.
    """
    prompt = "(hbnb) "

    @staticmethod
    def split_args(line):
        """
        Splits a user input line into arguments, handling both quoted strings
        and non-whitespace characters.

        Args:
            line (str); The user input line to split.

        Returns:
            list: A list of arguments extracted from the line.
        """

        pattern = r'"[^"]*"|\S+'
        return re.findall(pattern, line)

    def do_EOF(self, line):
        """Exits the program when user enter `EOF`."""
        return True

    def help_quit(self):
        """Prints help message for `quit` command."""
        print("Quit command to exit the program")

    def do_quit(self, line):
        """Exits the program when user enters `quit`."""
        return True

    def emptyline(self):
        """Does nothing when an empty line is entered."""
        pass

    def do_create(self, line):
        """
        Creates a new instance of a class and stores it in the storage.

        Args:
            line (str): The user input line containing the class name.

        Returns:
            None
        """

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
        """
        Prints a specific instance of a class based on
        class name and instance ID

        Args:
            line (str): The user input line containing class name
            and instance ID.

        Returns:
            None
        """

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
        """
        Deletes an instance of a class based on class name
        and instance ID.

        Args:
            line (str): The user input line containing class name
            and instance ID.

        Returns:
            None
        """

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
        """
        prints all objects of a given class
        or all objects in storage.

        Args:
            line (str): The user input line
            containing the class name (optional)

        Returns:
            None
        """

        args = HBNBCommand.split_args(line)
        try:
            if args:
                class_name = args[0]
                if class_name not in globals():
                    raise KeyError("** class doesn't exist **")
                else:
                    for value in storage.all().values():
                        if value.__class__.__name__ == class_name:
                            print(value)
            else:
                for value in storage.all().values():
                    print(value)

        except KeyError as e:
            print(e.args[0])

    def do_update(self, line):
        """
        Updates an attribute of a class instance
        stored in the global storage.

        Args:
            line (str): The user input line containing update arguments
            in format:
            `<class_name> <instance_id> <attribute_name> "<attributae_value>"`

        Returns:
                None
        """

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
