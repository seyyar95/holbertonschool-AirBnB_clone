#!/usr/bin/python3
"""Class console"""
import cmd
from models.base_model import BaseModel
from models import storage


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
            attribute_name = args[2]
        except IndexError:
            print("** attribute name missing **")

        try:
            attribute_value = args[3]
        except IndexError:
            print("** value missing **")

        try:
            if key not in storage.all():
                raise KeyError
            else:
                attribute_name = args[2]
                attribute_value = args[3]
                instance = storage.all()[key]
                setattr(instance, attribute_name, attribute_value)
                storage.save()
        except KeyError:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
