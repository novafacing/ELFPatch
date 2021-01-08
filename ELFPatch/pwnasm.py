from __future__ import absolute_import
from keystone import *
from capstone import *

class PwnAssembler(object):
    def __init__(self, arch, mode):
        self.arch = arch
        self.mode = mode

        self.assembler = Ks(arch, mode)

    def assemble(self, data, offset=0):
        return str(self.assembler.asm(data, offset)[0])

class PwnDisassembler(object):
    def __init__(self, arch, mode):
        self.arch = arch
        self.mode = mode

        self.disassembler = Cs(arch, mode)

    def disassemble(self, data, offset=0x0):
        return self.disassembler.disasm(data, offset)

