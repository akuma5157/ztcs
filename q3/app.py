#!/usr/bin/env python
# based on prompt example at https://typer.tiangolo.com/tutorial/prompt/

from os.path import isfile

import typer
from ssh_handler import execute

def main(hosts_file: str = typer.Argument("hosts")):
    if not isfile(hosts_file):
        typer.echo(f"Inventory file not found at {hosts_file}!")
        typer.Abort()
    else:
        while True:
            next = typer.confirm("Would you like to run a command(y/N)?", abort=True)
            command = typer.prompt("$")

            execute(hosts_file, command)

if __name__ == "__main__":
    typer.run(main)
