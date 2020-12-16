import enum

from collections import namedtuple
from dataclasses import dataclass, field
from typing import List

from chalicelib.challenge import ChallengeSolver


class LoopDetectedError(Exception):
    def __init__(self, system_state, boot_code):
        acc = system_state.acc
        prog_counter = system_state.prog_counter
        instruction = boot_code[system_state.prog_counter]
        super().__init__(f"Loop detected at {acc=} {prog_counter=}: {instruction}")
        
        self.system_state = system_state
        self.boot_code = boot_code


class InstructionType(enum.Enum):
    ACC = "acc"
    JMP = "jmp"
    NOP = "nop"


Instruction = namedtuple('Instruction', ('type', 'argument'))
BootCode = List[Instruction]

@dataclass
class SystemState:
    prog_counter: int = 0
    acc: int = 0
    pc_history: List[int] = field(default_factory=list)

    def execute(self, boot_code: BootCode):
        while self.prog_counter < len(boot_code):
            if self.prog_counter in self.pc_history:
                raise LoopDetectedError(self, boot_code)
            self.pc_history.append(self.prog_counter)
            instruction = boot_code[self.prog_counter]
            if instruction.type == InstructionType.NOP:
                self.prog_counter += 1
            elif instruction.type == InstructionType.ACC:
                self.prog_counter += 1
                self.acc += instruction.argument
            elif instruction.type == InstructionType.JMP:
                self.prog_counter += instruction.argument


class HandheldHalting(ChallengeSolver):
    day = 8
    boot_code: BootCode

    def __init__(self, input):
        lines = input.decode('utf-8').splitlines()
        instrs = []
        for line in lines:
            instr, arg = line.split()
            instrs.append(Instruction(InstructionType(instr), int(arg)))
        self.boot_code = instrs

    def solve_a(self):
        system_state = SystemState()
        try:
            system_state.execute(self.boot_code)
        except LoopDetectedError:
            return system_state.acc
        return -1
    
    def solve_b(self):
        for idx, instruction in enumerate(self.boot_code):
            boot_code_copy = list(self.boot_code)
            if instruction.type == InstructionType.ACC:
                continue
            if instruction.type == InstructionType.JMP:
                boot_code_copy[idx] = Instruction(InstructionType.NOP, instruction.argument)
            if instruction.type == InstructionType.NOP:
                boot_code_copy[idx] = Instruction(InstructionType.JMP, instruction.argument)
            
            system_state = SystemState()
            try:
                system_state.execute(boot_code_copy)
            except LoopDetectedError:
                continue
            return system_state.acc
        return -1