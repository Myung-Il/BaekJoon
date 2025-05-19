from sys import stdin
input = lambda:stdin.readline().rstrip()
def multi():
    s1, s2, i = input().split()
    return s1, s2, int(i)


class Pipe:
    def __init__(self, source):
        self.source = source
        self.sinks = dict()
    
    def sinkAdd(self, sink, capacity):self.sinks[sink] = capacity


n = int(input())
pipes = dict()

for _ in range(n):
    source, sink, capacity = multi()
    if pipes.get(source):pipes[source].append(capacity)
    else:
        pipes[source] = Pipe(source)
    pipes[source].sinkAdd(sink, capacity)