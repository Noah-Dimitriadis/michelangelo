import sys
import os
import typer
import shutil
from quotes import get_quote
from typing import Annotated

def resource_path(relative_path):
    base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, relative_path)

app = typer.Typer()

ascii_map = {
            50: resource_path("creation_of_ascii/50.txt"),
            75: resource_path("creation_of_ascii/75.txt"),
            100: resource_path("creation_of_ascii/100.txt"),
            125: resource_path("creation_of_ascii/125.txt"),
            150: resource_path("creation_of_ascii/150.txt"),
            175: resource_path("creation_of_ascii/175.txt"),
            200: resource_path("creation_of_ascii/200.txt"),
            225: resource_path("creation_of_ascii/225.txt"),
            250: resource_path("creation_of_ascii/250.txt"),
            275: resource_path("creation_of_ascii/275.txt"),
            300: resource_path("creation_of_ascii/300.txt"),
            325: resource_path("creation_of_ascii/325.txt"),
            350: resource_path("creation_of_ascii/350.txt"),
            375: resource_path("creation_of_ascii/375.txt"),
            400: resource_path("creation_of_ascii/400.txt"),
        }

@app.command()
def main(quote: Annotated[
    bool, typer.Option()
] = False):
    try:
        while True:
            size = shutil.get_terminal_size()
            width = size.columns
            step = 25
            min_width = 50
            max_width = 400
            size_key = min((max(width, min_width) - min_width) // step * step + min_width, max_width)
            file_path = ascii_map.get(size_key)

            try:
                with open(file_path, 'r') as file:
                    file_content = file.read()
                    print(file_content)
            except FileNotFoundError:
                print(f"Error: File '{file_path}' not found.")
            except Exception as e:
                print(f"An error occurred: {e}")

            if quote:
                print(get_quote())

            input()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    app()