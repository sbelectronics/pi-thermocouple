import spidev
import sys
import time

class Max31855:
    def __init__(self, spi_num, spi_ce):
        self.spi = spidev.SpiDev()
        self.spi.open(spi_num, spi_ce)

    def read32(self):
        bytes = self.spi.readbytes(4)
        v = 0
        for byte in bytes:
           v = (v << 8) | byte
        return v

    def readThermo(self):
        v = self.read32()

        # fault bit is D16, then fault code is in [D2..D0]
        fault_signal = v & 0x1000
        if fault_signal:
            fault = v & 0x07
        else:
            fault = None

        internal_neg = v & 0x8000
        internal = (v>>4) & 0x7FF
        if internal_neg:
            internal -= 4096
        internal = internal * 0.0625

        external_neg = v & 0x80000000
        external = v >> 18
        if external_neg:
            external -= 16384
        external = external * 0.25

        return (fault, internal, external)

    @property
    def fault(self):
        return self.readThermo()[0]


    @property
    def externalC(self):
        (fault, internal, external) = self.readThermo()
        if fault:
           return None
        else:
           return external

    @property
    def internalC(self):
        (fault, internal, external) = self.readThermo()
        if fault:
           return None
        else:
           return internal

    def to_f(self,C):
        if (C == None):
            return None
        else:
            return C * 9.0 / 5.0 + 32.0

    @property
    def externalF(self):
        return self.to_f(self.externalC)

    @property
    def internalF(self):
        return self.to_f(self.internalC)

def usage():
   sys.exit(-1)

def main():
   thermo = Max31855(0,0)

   if thermo.fault:
       print "fault"
   else:
       print "internal=%0.2f F, external=%0.2f F" % (thermo.internalF, thermo.externalF)

if __name__ == "__main__":
    main()
