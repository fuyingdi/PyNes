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
    stack_register = 0xfd
    pc_register = 0
    accumulator = 0
    flags = 0x34
    x = 0
    y = 0

    MASK_NEGATIVE = 0x80
    MASK_OVERFLOW = 0x40
    MASK_BREAK = 0x10
    MASK_DECIMAL = 0x8
    MASK_INTERUPT = 0x4
    MASK_ZERO = 0x2
    MASK_CARRAY = 0x1

    
    def get_pc(self):
        pass

    def get_carry(self):
        if (self.flags & self.MASK_CARRAY) != 0:
            return 1
        elif (self.flags & self.MASK_CARRAY) == 0:
            return 0

    def get_zero(self):
        return (self.flags & self.MASK_ZERO)

    """
    set method
    """
    def _set_carry(self):
        self.flags |= self.MASK_CARRAY

    def _set_zero(self):
        self.flags |= self.MASK_ZERO

    def _set_decimal(self):
        self.flags |= self.MASK_DECIMAL

    def _set_disable_interupt(self):
        self.flags |= self.MASK_INTERUPT

    def _set_break(self):
        self.flags |= self.MASK_BREAK

    def _set_negative(self):
        self.flags &= ~self.MASK_ZERO

    def _set_overflow(self):
        self.flags |= self.MASK_OVERFLOW

    
    """
    get method
    """
    def is_negative(self):
        pass

    def is_overflow(self):
        pass

    def is_break(self):
        pass

    def is_decimal(self):
        pass

    def is_zero(self):
        pass

    def is_carry(self):
        pass

    def is_disable_interupt(self):
        pass

    """
    set flag regiser
    """

    def set_a(self, value):
        self.a = self.a & 0xff

    def set_x(self, value):
        self.x = self.x & 0xff

    def set_y(self, value):
        self.y = self.y & 0xff

    def set_stack(self, value):
        self.stack_register = value & 0xffff

    def set_pc(self, value):
        self.pc_register = value & 0xff
    

    
    




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
