
class Patch(object):
    u"""
    The class which manages the patch
    By the time this is called, the jmp to the virtual address would already have been added in rawelf
    """

    def __init__(self, chunk, virtual_address, patched_jump, assembler=None, append_jump_back=True, append_original_instructions=True, original_instructions=""):
        self.chunk = chunk #The chunk for the patch
        self._virtual_address = virtual_address #The virtual address of where we are patching
        self.patched_jump = patched_jump #The jump instruction which will overwrite the instructions at the patch, Padded to NOPs to make sure we don't have invalid instructions
        self.append_jump_back = append_jump_back
        self.append_original_instructions = append_original_instructions
        self.original_instructions = original_instructions #The original instructions being overwritten
        self.assembler = assembler #The asembler for current architecture

    #@ property's just to stay up to date with new python features
    @property 
    def content(self):
        return self.chunk.content

    @content.setter
    def content(self, new_content):
        self.update_patch(new_content)

    @property
    def virtual_address(self):
        return self._virtual_address

    def update_patch(self, content=""):
        #If we have to append the original instructions we overwrote
        if self.append_original_instructions:
            content += self.original_instructions

        #If we have to append a jump back to the original code
        if self.append_jump_back:
            executing_virtual_address = self.chunk.virtual_address + len(content)
            #We want to jmp back to after the jump
            jump_back_address = self.virtual_address + len(self.patched_jump)
            content += self.assembler.assemble(u"jmp {}".format(jump_back_address), offset=executing_virtual_address)

        self.chunk.update_data(content)

