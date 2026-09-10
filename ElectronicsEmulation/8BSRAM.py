class SRAM:
    inp_addr_pins = [0,0,0]
    out_addr_pins = [0,0,0]
    inp_dt_pins = [0,0,0,0,0,0,0,0]
    out_dt_pins = [0,0,0,0,0,0,0,0]
    data = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
    ]

    def setWriteAddr(self, newAddr):
        for i in range(0,3,1):
            if newAddr[i] < 1:
                self.out_addr_pins[i] = 0
            else:
                self.out_addr_pins[i] = 1

sram1 = SRAM()
sram1.setWriteAddr([0,40,0])

print(sram1.out_addr_pins)
