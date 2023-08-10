#!/usr/bin/python3
"""
Module console.py - a command interpreter using cmd module
"""

import cmd
import json
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models import storage
from models.review import Review
from datetime import datetime

class HBNBCommand(cmd.Cmd):
    ''' Command interpreter class '''

    prompt = "(hbnb)"
    
    All_class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_EOF(self, arg):
        '''Quit command - Use CTRL+D to exit the program'''
        print("")
        return True

    def do_quit(self, arg):
        ''' Quit command to exit the program '''
        return True

    def do_nothing(self, arg):
        ''' No-op command '''
        pass

    def emptyline(self):
        ''' Empty line shouldn't execute anything '''
        pass

    def do_create(self, args):
        ''' Creates a new instance of the specified class and prints its id '''
        if args == "":
            print("** class name missing **")
            return
        arg = shlex.split(args)
        if arg[0] not in HBNBCommand.All_class_dict:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.All_class_dict[arg[0]]()
        new_instance.save()
        print(new_instance.id)

    # Other command methods (do_show, do_destroy, etc.) ...

    def default(self, args):
        '''
        Executes actions on objects based on syntax like {<>}.all(), {<>}.count(),
        {<>}.show(), {<>}.destroy(), {<>}.update()
        '''
        cmd_dict = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
        }
        arg = args.strip()
        val = arg.split(".")
        if len(val) != 2:
            cmd.Cmd.default(self, arg)
            return
        class_name = val[0]
        command = val[1].split("(")[0]
        line = ""
        if (command == "update" and val[1].split("(")[1][-2] == "}"):
            # Handle update with dictionary input
            inputs = val[1].split("(")[1].split(",", 1)
            inputs[0] = shlex.split(inputs[0])[0]
            line = "".join(inputs)[0:-1]
            line = class_name + " " + line
            self.do_update2(line.strip())
            return
        try:
            inputs = val[1].split("(")[1].split(",")
            for num in range(len(inputs)):
                if (num != len(inputs) - 1):
                    line = line + " " + shlex.split(inputs[num])[0]
                else:
                    line = line + " " + shlex.split(inputs[num][0:-1])[0]
        except IndexError:
            inputs = ""
            line = ""
        line = class_name + line
        if (command in cmd_dict.keys()):
            cmd_dict[command](line.strip())

if __name__ == '__main__':
    HBNBCommand().cmdloop()
