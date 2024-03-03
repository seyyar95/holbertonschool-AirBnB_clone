#!/usr/bin/python3
"""
This is just a copy of `console.py` where I handled all errors by using only one function in order to avoid to use the same statements whithin different methods.

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
    
    @staticmethod
    def error_handler(args, method):
        if not args and method != "all":
            print("** class name missing **")
        elif not args and method == "all":
            return False
        elif args[0] not in globals() or type(globals()[args[0]]) is not type:
            print("** class doesn't exist **")
        elif len(args) == 1 and method != "create" and method != "all":
            print("** instance id missing **")
        elif method != "create" and method != "all" and f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        elif method == "update" and len(args) == 2:
            print("** attribute name missing **")
        elif method == "update" and len(args) == 3:
            print("** value missing **")
        else:
            return True

        
        

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
        no_error_found = HBNBCommand.error_handler(args, "create")
        try:
            if no_error_found:
                class_name = globals()[args[0]]
                b = class_name()
                b.save()
                print(b.id)
        except Exception as e:
            print(e)


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
        no_error_found = HBNBCommand.error_handler(args, "show")
        try:
            if no_error_found:
                class_name = args[0]
                instance_id = args[1]
                key = f"{class_name}.{instance_id}"
                print(storage.all()[key])
        except Exception as e:
            print(e)

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

        args = HBNBCommand.split_rgs(line)
        no_error_found = HBNBCommand.error_handler(args, "destroy")
        try:
            if no_error_found:
                class_name = args[0]
                instance_id = args[1]
                key = f"{class_name}.{instance_id}"
                del storage.all()[key]
                storage.save()
        except Exception as e:
            print(e)

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
        no_error_found = HBNBCommand.error_handler(args, "all")
        try:
            if no_error_found:
                class_name = args[0]
                for value in storage.all().values():
                    if value.__class__.__name__ == class_name:
                        print(value)
            elif len(args) == 0:
                for value in storage.all().values():
                    print(value)

        except Exception as e:
            print(e)

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
        no_error_found = HBNBCommand.error_handler(args, "update")
        try:
            if no_error_found:
                class_name = args[0]
                instance_id = args[1]
                key = f"{class_name}.{instance_id}"
                instance = storage.all()[key]
                attribute_name = args[2]
                attribute_value = args[3]
                setattr(instance, attribute_name, attribute_value)
                storage.save
        except Exception as e:
            print(e)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
