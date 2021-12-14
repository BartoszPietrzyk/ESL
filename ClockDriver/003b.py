from myhdl import block, Signal

from ClockDriver import ClockDriver
from Hi import Hi

@block
def Greetings():

    clk1 = Signal(0)
    clk2 = Signal(0)

    clkdriver_1 = ClockDriver(clk1)  # positional and default association
    clkdriver_2 = ClockDriver(clk=clk2, period=21)  # named association
    hello_1 = Hi(clk=clk1)  # named and default association
    hello_2 = Hi(to="MyHDL", clk=clk2)  # named association

    return clkdriver_1, clkdriver_2, hello_1, hello_2


inst = Greetings()
inst.run_sim(50)