import click
import webbrowser

#Main is your cli entry point so this cannot be changed without updating your setup.py file.
@click.group()
def main():
    print("Your application {{cookiecutter.cli_name}} is working perfectly.")

#This is a subcommand within your command group and you can add an arbitrary number of these.
@main.command()
def printer(print_it):
    click.echo("You requested a print: {}".format(print_it))
#This is another subcommand within your command group.  You can change/add/or delete this.
@main.command()
def click_docs():
    url = ''
    webbrowser.open_new("https://click.palletsprojects.com/en/7.x/")

