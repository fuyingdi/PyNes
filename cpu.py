from memory import Memory


class InstructionSet6502:
    def brk(self):
        # force break
        pass

    def bit(self):
        # test a bit in memory
        pass

    def jmp(self):
        # jump to a new location
        pass

    def jsr(self):
        # jump to a new location and save return address
        pass

    def nop(self):
        # no operation
        pass

    def rti(self):
        # return from interrupt
        pass

    def rts(self):
        # return from subroutine
        pass

    def dey(self):
        # y--
        pass

    def dex(self):
        # x--
        pass

    def iny(self):
        # y++
        pass

    def inx(self):
        # x++
        pass

    def txa(self):
        # transfer x to accumulator
        pass

    def tax(self):
        # transfer accumulator to x
        pass

    def tya(self):
        # transfer y to accumulator
        pass

    def tay(self):
        # transfer accumulator to y
        pass

    def txs(self):
        # transfer x to stack register
        pass

    def tsx(self):
        # transfer stack register to x
        pass

    def php(self):
        pass

    def plp(self):
        pass

    def pla(self):
        # pull accumulator from stack
        pass

    def pha(self):
        # push accumulator on stack
        pass


class CpuRegister:
    stack_register = 0
    pc_register = 0
    accumulator = 0
    x = 0
    y = 0
    
    def get_pc(self):
        pass


class CPU(InstructionSet6502):
    register = CpuRegister()
    memory = Memory()

    def execute_instruction(self, op_code):
        pass

    def execute_pc(self, pc):
        pass

    def reset(self):
        pass

    def get_pc(self):
        pass

    def nmi(self, vector):
        # nmi中断
        pass

    def irq(self, vector):
        # irq中断
        pass
