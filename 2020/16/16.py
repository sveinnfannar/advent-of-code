# coding: utf-8
import doctest
import math
import itertools
from collections import Counter, defaultdict
from collections import namedtuple
import re

Rule = namedtuple('Rule', ['name', 'a', 'b'])


def ints(s):
    return list(map(int, re.findall(r"\d+", s)))


def parse_rules(rules_s):
    rules = []
    for rule in rules_s.split('\n'):
        rule = rule.strip()
        name, rest = rule.split(': ')
        range_a, range_b = rest.split(' or ')
        rules.append(Rule(name, ints(range_a), ints(range_b)))
    return rules


def parse_tickets(tickets_s):
    tickets = []
    for line in tickets_s.split('\n')[1:]:
        if line:
            tickets.append([int(x) for x in line.split(',')])
    return tickets


def parse_my_ticket():
    return [int(x) for x in my_ticket_s.split('\n')[1].split(',')]


def column(col, tickets):
    """
    >>> column(1, [[1, 2, 3], [4, 5, 6]])
    [2, 5]
    """
    return [ticket[col] for ticket in tickets]


def is_valid(rule, x):
    return rule.a[0] <= x <= rule.a[1] or rule.b[0] <= x <= rule.b[1]


def is_number_valid(rules, x):
    return any(is_valid(rule, x) for rule in rules)


def is_valid_column(rule, xs):
    """
    >>> is_valid_column(Rule('a', [0, 5], [10, 15]), [0, 1, 11, 15])
    True
    >>> is_valid_column(Rule('a', [0, 5], [10, 15]), [0, 1, 11, 15, 20])
    False
    """
    return all(is_valid(rule, x) for x in xs)


rules_s, my_ticket_s, tickets_s = open('input.txt').read().split('\n\n')
rules = parse_rules(rules_s)
my_ticket = parse_my_ticket()
tickets = parse_tickets(tickets_s)

invalids = [x for ticket in tickets
            for x in ticket
            if not any(is_valid(rule, x) for rule in rules)]
print('part 1:', sum(invalids))

valid_tickets = [ticket for ticket in tickets
                 if all(is_number_valid(rules, x) for x in ticket)]

# For each rule find all columns that match
rule_to_columns = defaultdict(set)
for rule in rules:
    for i in range(len(my_ticket)):
        col = column(i, valid_tickets)
        if is_valid_column(rule, col):
            rule_to_columns[rule.name].add(i)

# Reduce the columns for each rule down to 1 per rule
rule_to_column = {}
while singles := [(r, c) for r, c in rule_to_columns.items() if len(c) == 1]:
    single_rule, single_col = singles[0]
    single_col = single_col.pop()
    del rule_to_columns[single_rule]
    rule_to_column[single_rule] = single_col
    for cols in rule_to_columns.values():
        cols.discard(single_col)

# Multiply departure values
mul = 1
for name, col_id in rule_to_column.items():
    if name.startswith('departure'):
        mul *= my_ticket[col_id]
print('part 2:', mul)

if __name__ == "__main__":
    doctest.testmod()
