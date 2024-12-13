import random as r
from math import sqrt
import time
from rich import print as rprint

list_ = list(range(1, 1001))
rprint("For the equation :- [bold red]√((a*a)+(b*b)+(c*c))[/bold red]")
while True:
    a= r.randint(1, 100)
    b= r.randint(1, 100)
    c= r.randint(1, 100)
    x = sqrt((a*a)+(b*b)+(c*c))
    for item in list_:
        if x == float(item):
            rprint(f"⊗ Numbers :- [bold green]{a}[/bold green], [bold green]{b}[/bold green] and \
[bold green]{c} [/bold green]\n —> Answer :-  [bold blue]{x}[/bold blue]")
            time.sleep(1)