from __future__ import absolute_import
from construct import Array

#The parsing of the ELF with the specific sized structs
class ELFParse(object):
    def __init__(self, elf_structs, data):

        self.ehdr = elf_structs.Elf_ehdr.parse(data)
        self.phdr_table = Array(self.ehdr.e_phnum, elf_structs.Elf_phdr).parse(data[self.ehdr.e_phoff:])






