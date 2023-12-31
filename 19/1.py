
from collections import namedtuple
import re

Rule = namedtuple("Rule", ["mode", "dest", "var", "bound"])

state = "rules"
workflows = { }

s = 0

with open("19/data") as file:
    for line in file:
        line = line.strip()
        if not line:
            state = "parts"
            continue
        if state == "rules":
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
        else:
            part = { }
            for assign in re.findall("[xmas]=\d+", line):
                var, val = assign.split("=")
                part[var] = int(val)
            wfname = "in"
            # print(f"x:{part['x']},m:{part['m']},a:{part['a']},s:{part['s']}")
            while wfname not in ["A", "R"]:
                rules = workflows[wfname]
                # print(wfname)
                for rule in rules:
                    # print(rule)
                    if rule.mode == "send":
                        wfname = rule.dest
                        break
                    if rule.mode == "less" and part[rule.var] < rule.bound:
                        wfname = rule.dest
                        break
                    if rule.mode == "great" and part[rule.var] > rule.bound:
                        wfname = rule.dest
                        break
            # print()
            if wfname == "A":
                s += part["x"] + part["m"] + part["a"] + part["s"]

print(s)
