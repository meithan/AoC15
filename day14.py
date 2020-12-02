# Advent of Code: Day 14
import sys

#fname = sys.argv[1]
#total_time = int(sys.argv[2])
fname = "input14.txt"
race_time = 2503

class Reindeer:
    def __init__(self, name, speed, fly_time, rest_time):
        self.name = name
        self.speed = int(speed)
        self.fly_time = int(fly_time)
        self.rest_time = int(rest_time)
        self.cycle_time = self.fly_time + self.rest_time
    def distanceAfterTime(self, time):
        cycles = time // self.cycle_time
        distance = cycles*self.fly_time*self.speed
        time = time % self.cycle_time
        distance += min(time, self.fly_time)*self.speed
        return distance
    def __repr__(self):
        return "%s, fly at %i km/s for %i s then rest for %i s" % (self.name, self.speed, self.fly_time, self.rest_time)

f = open(fname)
deers = []
for line in f:
    line = line.split()
    deers.append(Reindeer(line[0], line[3], line[6], line[13]))
f.close()

# Part 1
print "== Part 1 =="
farthest_dist = None
farthest_deer = None
for deer in deers:
    print deer
    dist = deer.distanceAfterTime(race_time)
    print "%i km" % dist
    if farthest_deer == None or dist > farthest_dist:
        farthest_dist = dist
        farthest_deer = deer
print "Winner: %s at %i km" % (farthest_deer.name, farthest_dist)

# Part 2 -- simulate race
print "== Part 2 =="
for deer in deers:
    deer.points = 0
    deer.curdist = 0
time = 0
while time < race_time:
    time += 1
    lead_dist = None
    leaders = []
    for deer in deers:
        deer.curdist = deer.distanceAfterTime(time)
        if lead_dist == None or deer.curdist == lead_dist:
            lead_dist = deer.curdist
            leaders.append(deer)
        elif deer.curdist > lead_dist:
            lead_dist = deer.curdist
            leaders = [deer]
    for deer in leaders:
        deer.points += 1
deers.sort(key=lambda x: x.points, reverse=True)
print "Points after %i seconds" % race_time
for deer in deers:
    print "%s: %i" % (deer.name, deer.points)
