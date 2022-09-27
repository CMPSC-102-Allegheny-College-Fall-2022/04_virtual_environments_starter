#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Your code will appear in this file."""

from rich.console import Console

import typer

# create a Typer object to support the command-line interface
cli = typer.Typer()


@cli.command()
def main():
    """driver function of the project"""
    console = Console()
    console.print("Hello! Welcome to my project!")
# TODO

# end of main()
