import sys
import itertools

# Weighted undirected graph
class WeightedGraph:

  def __init__(self):
    self.V = 0
    self.E = 0
    self.edges = []
    self.names = []
    
  # Adds an undirected weighted edge to the graph
  # Source and dest can b
  def add_edge(self, src, dst, weight):
    srcidx = None
    dstidx = None
    # Look for node names, get their nodes indices
    for i,name in enumerate(self.names):
      if name == src:
        srcidx = i
      elif name == dst:
        dstidx = i
      if srcidx != None and dstidx != None:
        break
    # Add nodes if not already in names list
    if srcidx == None:
      self.names.append(src)
      srcidx = self.V
      self.V += 1
      self.edges.append({})
    if dstidx == None:
      self.names.append(dst)
      dstidx = self.V
      self.V += 1
      self.edges.append({})      
    # Adds the edge to source and destination lists
    if dstidx not in self.edges[srcidx]:
      print "Added edge %s <-> %s, weight %f" % (src, dst, weight)
      self.edges[srcidx][dstidx] = weight
      self.edges[dstidx][srcidx] = weight
      self.E += 1

  # Returns the weight of the (src,dst) edge, or -1 if no edge exists
  def edge_weight(self, src, dst):
    if dst in self.edges[src]:
      return self.edges[src][dst]
    else:
      return -1

# ============

if __name__ == "__main__":

  # Load graph
  G = WeightedGraph()  
  infname = sys.argv[1]
  f = open(infname, "r")
  for line in f:
    data = line.split()
    src = data[0]
    dst = data[2]
    weight = float(data[4])
    G.add_edge(src, dst, weight)
  f.close()
  print "%i vertices, %i edges" % (G.V, G.E)
  for e in G.edges:
    print e
  
  # Brute force solution: try all possible permutations
  shortest_dist = None
  shortest_paths = []
  longest_dist = None
  longest_paths = []  
  for path in itertools.permutations(range(G.V)):
    if path[0] > path[-1]: continue   # skip reverse permutations
    length = 0.0
    ruledout = False
    # Check if the path is valid, recording its length
    for i in range(len(path)-1):
      weight = G.edge_weight(path[i],path[i+1])
      if weight != -1:
        length += weight
      else:
        ruledout = True
        break
    # If the path is valid, check if it's as good or better
    if not ruledout:
      if shortest_dist == None or length == shortest_dist:
        shortest_dist = length
        shortest_paths.append(path)
      elif length < shortest_dist:
        shortest_dist = length
        shortest_paths = [path]
      if longest_dist == None or length == longest_dist:
        longest_dist = length
        longest_paths.append(path)
      elif length > longest_dist:
        longest_dist = length
        longest_paths = [path]
        
  print "\nShortest path length:", shortest_dist
  shortest_paths = map(lambda path: map(lambda x: G.names[x], path), shortest_paths)
  print "Shortest paths:"
  for path in shortest_paths: print path
  
  print "\nLongest path length:", longest_dist
  longest_paths = map(lambda path: map(lambda x: G.names[x], path), longest_paths)
  print "Longest paths:"
  for path in longest_paths: print path  
