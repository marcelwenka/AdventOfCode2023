
from collections import namedtuple
from functools import reduce
import operator

Rule = namedtuple("Rule", ["mode", "dest", "var", "bound"])

class Bound:
    __slots__ = ["min", "max"]
    def __init__(self, min, max):
        self.min = min
        self.max = max
    def copy(self):
        return Bound(self.min, self.max)
    def __str__(self):
        return f"({self.min},{self.max})"
    def __repr__(self):
        return f"({self.min},{self.max})"

workflows = { }
s = 0

with open("19/data") as file:
    for line in file:
        line = line.strip()
        if not line:
            break
        line = line.strip("}")
        name, rules = line.split("{")
        workflow = []
        for rule in rules.split(","):
            if ":" in rule:
                cond, dest = rule.split(":")
                if "<" in cond:
                    var, bound = cond.split("<")
                    workflow.append(Rule("less", dest, var, int(bound)))
                elif ">" in cond:
                    var, bound = cond.split(">")
                    workflow.append(Rule("great", dest, var, int(bound)))
                else:
                    raise Exception("Unknown rule condition!")
            else:
                workflow.append(Rule("send", rule, None, None))
        workflows[name] = workflow

def getCombinations(wfname, initb):
    if wfname == "R":
        return 0
    if any(b.max < b.min for b in initb.values()):
        return 0
    if wfname == "A":
        # print(init)
        return reduce(operator.mul, [b.max - b.min + 1 for b in initb.values()], 1)
    combs = 0
    workflow = workflows[wfname]
    bounds = { name: bound.copy() for name, bound in initb.items() }
    for rule in workflow:
        if rule.mode == "send":
            combs += getCombinations(rule.dest, bounds)
        else:
            bound = bounds[rule.var]
            prev = bound.copy()
            if rule.mode == "less":
                bound.max = min(bound.max, rule.bound - 1)
                combs += getCombinations(rule.dest, bounds)
                prev.min = max(rule.bound, bound.min)
            if rule.mode == "great":
                bound.min = max(bound.min, rule.bound + 1)
                combs += getCombinations(rule.dest, bounds)
                prev.max = min(rule.bound, bounds[rule.var].max)
            bounds[rule.var] = prev
    return combs

bounds = { key: Bound(1, 4000) for key in "xmas" }
print(getCombinations("in", bounds))
