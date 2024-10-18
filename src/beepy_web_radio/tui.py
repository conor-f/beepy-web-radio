from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer, Label


class BeepyWebRadioApp(App):
    BINDINGS = [
        Binding("q", "quit", "Quit", show=True),
    ]

    def compose(self) -> ComposeResult:
        yield Label("Beepy Web Radio")
        yield Footer()

    def on_mount(self) -> None:
        pass
