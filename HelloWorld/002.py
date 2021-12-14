from myhdl import block, Signal, delay, always, now

@block
def SayHi():

    clk = Signal(0)

    @always(delay(5))
    def drive_clk():
        clk.next = not clk

    @always(clk.posedge)
    def say_hello():
        print("%s Hello World!" % now())

    return drive_clk, say_hello


inst = SayHi()
inst.run_sim(50)