from __future__ import division
from __future__ import absolute_import
from construct import *
from .types import *

#32 bit header struct

Elf32_Ehdr = Struct(
        u'e_ident' / Struct(
            u"MAGIC"/Const("\x7fELF"), #ELF Header
            u'EI_CLASS'/ Int8ul,
            u"OTHER_STUFF"/ Array(11, Int8ul)
            ),
        u'e_type' / Elf32_Half,
        u'e_machine' / Elf32_Half,
        u'e_version' / Elf32_Word,
        u'e_entry' / Elf32_Addr,  
        u'e_phoff' / Elf32_Off,
        u'e_shoff' / Elf32_Off,
        u'e_flags' / Elf32_Word,
        u'e_ehsize' / Elf32_Half,
        u'e_phentsize' / Elf32_Half,
        u'e_phnum' / Elf32_Half,
        u'e_shentsize' / Elf32_Half,
        u'e_shnum' / Elf32_Half,
        u'e_shstrndx' / Elf32_Half
        )
#32 bit Segment (program) header struct
Elf32_Phdr = Struct(
        u'p_type' / Elf32_Word,
        u'p_offset' / Elf32_Off,
        u'p_vaddr' / Elf32_Addr,
        u'p_paddr' / Elf32_Addr,
        u'p_filesz' / Elf32_Word,
        u'p_memsz' / Elf32_Word,
        u'p_flags' / Elf32_Word,
        u'p_align' / Elf32_Word
        )


Elf64_Ehdr = Struct(
        u'e_ident' / Struct(
            u"MAGIC"/Const("\x7fELF"), #ELF Header
            u'EI_CLASS'/ Int8ul,
            u"OTHER_STUFF"/ Array(11, Int8ul)
            ),
        u'e_type' / Elf64_Half,
        u'e_machine' / Elf64_Half,
        u'e_version' / Elf64_Word,
        u'e_entry' / Elf64_Addr,
        u'e_phoff' / Elf64_Off,	
        u'e_shoff' / Elf64_Off,	
        u'e_flags' / Elf64_Word,
        u'e_ehsize' / Elf64_Half,
        u'e_phentsize' / Elf64_Half,
        u'e_phnum' / Elf64_Half,
        u'e_shentsize' / Elf64_Half,
        u'e_shnum' / Elf64_Half,
        u'e_shstrndx' / Elf64_Half
        )


Elf64_Phdr = Struct(
        u'p_type' / Elf64_Word,
        u'p_flags' / Elf64_Word,
        u'p_offset' / Elf64_Off,
        u'p_vaddr' / Elf64_Addr,
        u'p_paddr' / Elf64_Addr,
        u'p_filesz' / Elf64_Xword,
        u'p_memsz' / Elf64_Xword,
        u'p_align' / Elf64_Xword
        )


