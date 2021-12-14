import random
from myhdl import block, instance, Signal, intbv, delay
from mux import mux

random.seed(9)
randrange = random.randrange

@block
def test_mux():

    z, a, b, sel = [Signal(intbv(0)) for i in range(4)]

    mux_1 = mux(z, a, b, sel)

    @instance
    def stimulus():
        print("z a b sel")
        for i in range(15):
            a.next, b.next, sel.next = randrange(9), randrange(9), randrange(3)
            yield delay(10)
            print("%s %s %s %s" % (z, a, b, sel))

    return mux_1, stimulus

tb = test_mux()
tb.run_sim()