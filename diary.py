__author__ = 'Oliver'

import datetime
import os
import sys
from collections import OrderedDict

from peewee import *

db = SqliteDatabase('diary.db')


class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def initialize():
    """Create the database and the table if they don't exist."""
    db.connect()
    db.create_tables([Entry], safe=True)


def menu_loop():
    """Show the menu"""
    choice = None

    while choice != 'q':
        clear()
        print ('Enter "q" to quit.')
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = raw_input('Action: ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()


def add_entry():
    """Add an entry"""
    print("Enter your entry. Press <Ctrl> + D when finished.")
    data = sys.stdin.read().strip()

    if data:
        if raw_input("Save entry? [y\\n]: ").lower() != 'n':
            Entry.create(content=data)
            print("Saved successfully!")


def view_entries(search_query=None):
    """View previous entries.

    >>> a = [1, 2, 3]
    >>> print a
    [1, 2, 4]

    """
    entries = Entry.select().order_by(Entry.timestamp.desc())
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))

    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        clear()
        print(timestamp)
        print('=' * len(timestamp))
        print(entry.content)
        print("\n\n" + "-" * len(timestamp))
        print('Press [n] for next entry')
        print('Press [d] to delete current entry')
        print('Press [q] to quit and return to main menu')

        next_action = raw_input('Action: [N\\D\\Q] ').lower().strip()
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)


def search_entries():
    """Search entries for a string"""
    view_entries(raw_input("Search query: "))

def delete_entry(entry):
    """Delete an entry"""
    if raw_input("Are you sure you want to delete this entry? [y\\n]: ").lower() == 'y':
        entry.delete_instance()
        print("Entry was successfully deleted!")


def clear():

    os.system('cls' if os.name == 'nt' else 'clear')
menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries)
])

if __name__ == "__main__":
    initialize()
    menu_loop()
