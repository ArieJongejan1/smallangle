import click
import numpy as np
import pandas as pd
from numpy import pi


@click.group()
def cmd_group():
    """
    smallangle gives results of sinus and tangent of a number of function arguments
    equally devide over the interval 0 to 2pi 
    """
    pass

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=5,
    help = "provides a number of results"
)
def sin(number):
    """ 
    Provides sinus for a given value on the interval 0 to  2 pi. 
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=5,
    help = "provides a given number of results"
)
def tan(number):
    """ 
    Provides tangent for a given value between 0 and 2 pi.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)

if __name__ == "__main__":
    cmd_group()

