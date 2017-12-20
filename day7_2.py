#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import day7

class Tree(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = int(weight)
        self.children = []
        self.parent = None
        self._total_weight = None

    def add_children(self, children):
        self.children.extend(children)
        for child in children:
            assert child.parent is None
            child.parent = self

    def get_root(self):
        if self.parent is None:
            return self
        else:
            return self.parent.get_root()

    def get_wrong_weight(self):
        if len(self.children) <= 1:
            return self
        
        children_weights = [(child,child.total_weight()) for child in self.children]
        children_weights.sort(key=lambda pair: pair[1])
        
        if children_weights[0][1] != children_weights[1][1]:
            return children_weights[0][0].get_wrong_weight()
        elif children_weights[-1][1] != children_weights[-2][1]:
            return children_weights[-1][0].get_wrong_weight()
        else:
            return self

    def total_weight(self):
        if self._total_weight is None:
            self._total_weight = self.weight + sum(child.total_weight() for child in self.children)
        return self._total_weight

class Day(day7.Day):
    def parse(self, input):
        programs = super(Day, self).parse(input)

        # make tree
        
        nodes = {}
    
        for name in programs:
            node = Tree(name, programs[name][1])
            nodes[name] = node
        
        for name in programs:
            children = [nodes[child_name] for child_name in programs[name][0]]
            nodes[name].add_children(children)
            
        return next(iter(nodes.values())).get_root()

    def run(self, tree):
        bad_node = tree.get_wrong_weight()
        sibling_weights = bad_node.parent.children
        children_weights = [child.total_weight() for child in sibling_weights]
        children_weights.sort()
        if children_weights[0] != children_weights[1]:
            difference = children_weights[0] - children_weights[1]
        elif children_weights[-1] != children_weights[-2]:
            difference = children_weights[-1] - children_weights[-2]
        return bad_node.weight - difference

if __name__ == '__main__':
    Day(7).main()
