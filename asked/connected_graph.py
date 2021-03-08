#!/bin/python3

import math
import os
import random
import re
import sys


class Graph:

    def __init__(self, vertex):
        self.vertex = vertex
        self.adjacent_mat = [[] for i in range(vertex)]

    def add_edge(self, v1, v2):
        self.adjacent_mat[v1].append(v2)
        self.adjacent_mat[v2].append(v1)

    def ans(self):
        visited = []
        groups = []
        for i in range(self.vertex):
            visited.append(False)
        for j in range(self.vertex):
            if visited[j] == False:
                ls = []
                groups.append(self.dfs(ls, j, visited))
        return groups

    def dfs(self, temp, v, visited):
        visited[v] = True
        temp.append(v)
        for i in self.adjacent_mat[v]:
            if visited[i] == False:
                temp = self.dfs(temp, i, visited)
        return temp


def get_edges(related):
    ls = []
    for i in range(len(related)):
        for j in range(len(related)):
            if related[i][j] == '1':
                ls.append((i, j))
    return ls


def countGroups(related):
    ls = get_edges(related)
    g = Graph(len(related))
    for i, j in ls:
        g.add_edge(i, j)
    cc = g.ans()
    return len(cc)
