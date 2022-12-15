#!/usr/bin/env python3
"""Bloco de notas

$ notes_v010.py new "Minha Nota"
tag: tech
text: 
Anotação geral sobre carreira de tecnologia

$ notes_v010.py read --tag=tech
...
...
"""
__version__ = "0.1.0"

import os
import sys

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage.")
    print(f"You must specify subcommand {cmds}.")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}.")
    
if arguments[0] == "read":
    # leitura das notas
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"title: {title}")
            print(f"text: {text}")
            print("-" * 30)

# Validação
if arguments[0] == "new":
    # criação da nota
    try:
        title = arguments[1]
        text = [
            f"{title}",
            input("tag:").strip(),
            input("text:\n").strip(),
        ]
        # \t - tsv
        try:
            with open(filepath, "a") as file_:
                file_.write("\t".join(text) + "\n")
        except PermissionError as e:
            print(str(e))
    except IndexError as e:
        # TODO: Logging
        print(f"[Error] {str(e)}.")
        print(f"Insert a title for the note as an argument.")
        print(f"Format: new 'title'.")
        
