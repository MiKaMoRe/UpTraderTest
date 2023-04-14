#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import re
import sys


def main():
    activate_env() # Set all environment variables
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tree_menu.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def activate_env():
    env = open('.env')
    for row in env:
        var_name = re.search(r'\w+=', row)[0][:-1]
        value = re.search(r'=[\w\W]+', row)[0][1:-1]
        os.environ.setdefault(var_name, value)


if __name__ == '__main__':
    main()
