#!/usr/bin/python3
"""HBNB Console: Entry point for the AirBnB clone command interpreter."""

import cmd
import shlex
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


# Dictionary of available model classes
classes = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User,
}


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""

    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Exit the console with EOF (Ctrl+D)."""
        return True

    def do_quit(self, arg):
        """Quit command to exit the console."""
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        return False

    # -------------------------------
    # Helpers
    # -------------------------------

    def _key_value_parser(self, args):
        """Convert key=value strings into a dictionary."""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                key, value = arg.split("=", 1)
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace("_", " ")
                else:
                    try:
                        value = int(value)
                    except Exception:
                        try:
                            value = float(value)
                        except Exception:
                            continue
                new_dict[key] = value
        return new_dict

    # -------------------------------
    # Console commands
    # -------------------------------

    def do_create(self, arg):
        """Create a new instance of a class, save it, and print its id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
            print(instance.id)
            instance.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print an instance based on the class and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = f"{args[0]}.{args[1]}"
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Delete an instance based on the class and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = f"{args[0]}.{args[1]}"
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Print all instances, or all instances of a class if specified."""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print(obj_list)

    def do_update(self, arg):
        """Update an instance based on class, id, attribute, and value."""
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        if key not in models.storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        # Cast attribute types if necessary
        if args[0] == "Place":
            if args[2] in integers:
                try:
                    args[3] = int(args[3])
                except Exception:
                    args[3] = 0
            elif args[2] in floats:
                try:
                    args[3] = float(args[3])
                except Exception:
                    args[3] = 0.0

        setattr(models.storage.all()[key], args[2], args[3])
        models.storage.all()[key].save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
