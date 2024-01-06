
from collections import namedtuple

Signal = namedtuple("Signal", ["sender", "dest", "signal"])

class Module:
    def __init__(self, name, dests):
        self.name = name
        self.dests = dests

class Transmitter(Module):
    def __init__(self, name, dests):
        super().__init__(name, dests)
    def send(self, _, input):
        return [Signal(self.name, dest, input) for dest in self.dests]
    def copy(self):
        return self

class Inverter(Module):
    def __init__(self, name, dests):
        super().__init__(name, dests)
        self.state = False
    def send(self, _, input):
        if input:
            return []
        self.state = not self.state
        return [Signal(self.name, dest, self.state) for dest in self.dests]
    def copy(self):
        return Inverter(self.name, self.dests, self.state)

class Conjunction(Module):
    def __init__(self, name, dests):
        super().__init__(name, dests)
        self.ins = { }
    def addInput(self, input):
        self.ins[input] = False
    def send(self, sender, input):
        self.ins[sender] = input
        output = not all(self.ins.values())
        return [Signal(self.name, dest, output) for dest in self.dests]

modules = { }

with open("20/data") as file:
    for line in file:
        line = line.strip()
        name, dests = line.split(" -> ")
        dests = dests.split(", ")
        if name == "broadcaster":
            modules[name] = Transmitter(name, dests)
        elif name[0] == "%":
            modules[name[1:]] = Inverter(name[1:], dests)
        elif name[0] == "&":
            modules[name[1:]] = Conjunction(name[1:], dests)

for module in modules.values():
    for dest in module.dests:
        destmod = modules.get(dest, None)
        if type(destmod) is Conjunction:
            destmod.addInput(module.name)

highs, downs = 0, 0

for _ in range(1000):
    signals = [Signal("button", "broadcaster", False)]
    while signals:
        # for signal in signals:
        #     print(f"{signal.sender} -{'high' if signal.signal else 'low'}-> {signal.dest}")
        highs += sum(s.signal for s in signals)
        downs += sum(not s.signal for s in signals)
        nexts = []
        for sender, dest, signal in signals:
            module = modules.get(dest, None)
            if not module:
                continue
            nexts.extend(module.send(sender, signal))
        signals = nexts

print(f"{highs} * {downs} = {highs * downs}")
