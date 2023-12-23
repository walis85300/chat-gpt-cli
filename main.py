import typer
from rich.prompt import Confirm, Prompt
from rich.markdown import Markdown
from rich.console import Console


from chat import build_chat


app = typer.Typer()


@app.command()
def talk():
    chat = build_chat()
    console = Console()
    while True:
        input = Prompt.ask(">>")
        if input in ["exit", "q", "chao"]:
            confirm_exit = Confirm.ask("Are you sure you want to exit?")
            if confirm_exit:
                print("Good bye")
                raise typer.Exit()

        response = chat.complete(input)
        console.print(Markdown(response or ""))


if __name__ == "__main__":
    app()
