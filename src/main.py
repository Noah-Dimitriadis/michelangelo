import typer
from quotes import get_quote
import shutil


app = typer.Typer()

ascii_map = {
            50: "../creation_of_ascii/50.txt",
            75: "../creation_of_ascii/75.txt",
            100: "../creation_of_ascii/100.txt",
            125: "../creation_of_ascii/125.txt",
            150: "../creation_of_ascii/150.txt",
            175: "../creation_of_ascii/175.txt",
            200: "../creation_of_ascii/200.txt",
            225: "../creation_of_ascii/225.txt",
            250: "../creation_of_ascii/250.txt",
            275: "../creation_of_ascii/275.txt",
            300: "../creation_of_ascii/300.txt",
            325: "../creation_of_ascii/325.txt",
            350: "../creation_of_ascii/350.txt",
            375: "../creation_of_ascii/375.txt",
            400: "../creation_of_ascii/400.txt",
        }


@app.command()
def main():
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
    quote = get_quote()
    print(quote)

if __name__ == "__main__":
    app()