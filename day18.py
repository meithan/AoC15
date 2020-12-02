# Advent of Code: Day 18
import sys

#fname = sys.argv[1]
fname = "input18.txt"
N = 100
num_steps = 100
part2 = True

#fname = "test18.txt"
#num_steps = 4
#N = 6

# ===================

def update_grid(old, new, N):
    if part2:
        new[0][0] = 1
        new[0][N-1] = 1
        new[N-1][0] = 1
        new[N-1][N-1] = 1
    for i in range(N):
        for j in range(N):
            if part2 and (i,j) in [(0,0),(N-1,0),(0,N-1),(N-1,N-1)]:
                continue
            neighs_on = -old[i][j]  # bias count
            imin = max(i-1, 0)
            imax = min(i+1, N-1)
            jmin = max(j-1, 0)
            jmax = min(j+1, N-1)
            for ip in range(imin,imax+1):
                for jp in range(jmin,jmax+1):
                    if old[ip][jp] == 1:
                        neighs_on += 1
            if old[i][j] == 1:
                if neighs_on == 2 or neighs_on == 3:
                    new[i][j] = 1
                else:
                    new[i][j] = 0
            else:
                if neighs_on == 3:
                    new[i][j] = 1
                else:
                    new[i][j] = 0

# ===================

def count_on(grid, N):
    count = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1: count += 1
    return count
    
# ===================

def print_grid(grid, N):
    for i in range(N):
        buf = []
        for j in range(N):
            if grid[i][j] == 1: buf.append("#")
            else: buf.append(".")
        print " ".join(buf)
    print

# ===================

grid1 = []
grid2 = []
for i in range(N):
    grid1.append([0]*N)
    grid2.append([0]*N)
    
f = open(fname)
for i in range(N):
    line = f.readline()
    for j in range(N):
        if line[j] == "#": grid1[i][j] = 1
        else: grid1[i][j] = 0
f.close()
if part2:
    grid1[0][0] = 1
    grid1[0][N-1] = 1
    grid1[N-1][0] = 1
    grid1[N-1][N-1] = 1    

for step in range(num_steps):
    if step % 2 == 0:
        old = grid1
        new = grid2
    else:
        old = grid2
        new = grid1
    update_grid(old, new, N)
    print step+1
    #print_grid(new, N)
                
print "%i lights are on after %i steps" % (count_on(new, N), num_steps)
