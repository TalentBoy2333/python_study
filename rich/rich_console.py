import sys
import datetime
from rich.console import Console

console = Console()

console.print("Hello", "World!")
console.print("Hello", "World!", style="bold red")
console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")

'''
'''
def my_log(msg): 
    timestamp = 'timestamp {}'.format(datetime.datetime.now().strftime('%Y%m%d-%H-%M-%S'))
    filename = __file__
    line = str(sys._getframe().f_lineno)
    
    log_msg = '{} {}-line {}: {}'.format(timestamp, filename, line, msg)
    console.print('[bold red]Error[/bold red]', log_msg)
my_log('hello world')

'''
'''
console = Console()
test_data = [
    {"jsonrpc": "2.0", "method": "sum", "params": [None, 1, 2, 4, False, True], "id": "1",},
    {"jsonrpc": "2.0", "method": "notify_hello", "params": [7]},
    {"jsonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": "2"},
]

def test_log():
    enabled = False
    context = {
        "foo": "bar",
    }
    movies = ["Deadpool", "Rise of the Skywalker"]
    console.log("Hello from", console, "!")
    console.log(test_data, log_locals=True)


test_log()