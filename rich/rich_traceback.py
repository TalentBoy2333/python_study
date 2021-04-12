from rich.console import Console

console = Console()

try:
    a = 1 / 0
except:
    console.print_exception()