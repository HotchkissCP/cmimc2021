# from ast import literal_eval
# edit to the name of the input file
task = "2"

f = open('robotrecovery' + task + '.txt', 'r')
# change this function however you want: it takes in a character representing a cell 
# of the maze and x/y coordinates and returns whatever representation you want
def rep(c,x,y):
    if c == '.':
        return c
    elif c == 'X':
        return c
    elif c == 'R':
        robots.append([y,x]) # this needed to be flipped wtf cmimc
        return c
    elif c == 'E':
        entrance.append([y,x]) # same here
        return c
# you shouldn't need to edit lines 18-25
r,c,n = map(int, f.readline().strip().split())
robots = []
entrance = []
maze = []
instructions = []
for y in range(r):
    s = f.readline().strip()
    maze.append([rep(s[x],x,y) for x in range(c)])

# replace from here to line 30 with your own logic

rev = {"U":"D","D":"U","L":"R","R":"L"}
dirs = {"U":[-1,0],"D":[1,0],"L":[0,-1],"R":[0,1]}

# switch the direction of a path
def reverse(s):
  new_s = ""
  for char in s:
    new_s = rev[char] + new_s
  return new_s

# get all possible paths of length n
def get_all_paths(n):
  if n == 0:
    return [""]
  else:
    prev = get_all_paths(n - 1)
    new = []
    for i in prev:
      for d in dirs:
        new.append(i + d)
    return new

# find the shortest path from every point to the entrance
# BFS lmao
q = []
visited = [[False for i in range(c)] for j in range(r)]
shortestpath = [["" for i in range(c)] for j in range(r)]
x = entrance[0]

visited[x[0]][x[1]] = True
shortestpath[x[0]][x[1]] = ""
reached = 0
walls = 0
q.append(x)
while len(q) != 0:
  s = q[0]
  q.pop(0)
  # process node s
  # print(s)
  for key in dirs:
    d = dirs[key]
    new = [s[0] + d[0],s[1] + d[1]]
    #print(new)
    #print(d)
    
    if new[0] < 0 or new[1] < 0 or new[0]>=r or new[1]>=c:
      # out of bounds
      continue
    if visited[new[0]][new[1]]: 
      continue
    # is it a wall?
    visited[new[0]][new[1]] = True
    if maze[new[0]][new[1]] == "X":
      #print("hit a wall")
      walls += 1
      continue
    #print("appended")
    shortestpath[new[0]][new[1]] = shortestpath[s[0]][s[1]] + key
    q.append(new)
    reached += 1

# score the location of the robots (lower/higher is better)
def get_score(rob_locations):
  score = 0
  for i in range(len(rob_locations)):
    rob = rob_locations[i]
    #print(rob,len(shortestpath[rob[0]][rob[1]]))
    # penalty for staying in the same place
    # if robots[i][0] == rob[0] and robots[i][1] == rob[1]:
    #   continue
    dist = len(shortestpath[rob[0]][rob[1]])
    if dist == 0:
      return "INF"
      # score += 2 # add two??
      # continue
    score += 1/dist
    
  return score

#path_options = get_all_paths(8)
total = ""
next_path = ""
counter = 0
while len(robots) > 0:
  print("turn",counter,"robots left",len(robots), "current len",len(total))
  counter += 1
  # move all the robots first
  for move in next_path:
    d = dirs[move]
    to_remove = []
    for i in range(len(robots)):
      rob = robots[i]
      # print("rob is",rob)
      
      new = [rob[0] + d[0],rob[1] + d[1]]
      if new[0] < 0 or new[1] < 0 or new[0]>=r or new[1]>=c:
        # out of bounds
        # print("tried to go out of bounds")
        continue
      if maze[new[0]][new[1]] == "X":
        # print("hit a wall")
        # it's a wall
        continue
      robots[i] = [new[0],new[1]]
      if new[0] == entrance[0][0] and new[1] == entrance[0][1]:
        # made it to the entrance
        # remove it?
        to_remove.append(i)
        print(i,"made it to the entrance")
        continue
    
    for i in range(len(to_remove) - 1, -1, -1):
      print(to_remove[i], "is being removed now")
      del robots[to_remove[i]]
  #print(robots)

  # start testing for best possible move
  min_score = -1
  next_path = "not found yet"

  path_options = []
  for rob in robots:
    possibility = reverse(shortestpath[rob[0]][rob[1]])
    path_options.append(possibility[:len(possibility) // 4]) # 7 works the best for task 2???
    path_options.append(possibility[:len(possibility) // 2 + 1])
    path_options.append(possibility)

  for path in path_options:
    temp_robots = []
    # go through each robot and move it
    for i in range(len(robots)):
      rob = robots[i]
      temp_robots.append([rob[0],rob[1]])
      for move in path:
        d = dirs[move]
        new = [rob[0] + d[0],rob[1] + d[1]]
        if new[0] < 0 or new[1] < 0 or new[0]>=r or new[1]>=c:
          # out of bounds
          # print("tried to go out of bounds")
          continue
        if maze[new[0]][new[1]] == "X":
          # print("hit a wall")
          # it's a wall
          continue
        temp_robots[i] = [new[0],new[1]]
        if new[0] == entrance[0][0] and new[1] == entrance[0][1]:
          # made it to the entrance
          # remove it?
          #print(i,"made it to the entrance")
          break
    score = get_score(temp_robots)
    #print(temp_robots)
    if score == "INF":
      min_score = score
      next_path = path
      print("going to entrance")
      break
    if min_score == -1 or score > min_score: # change this based on score method
      min_score = score
      next_path = path
      #print("new min",score)
  print(min_score,next_path)
  if next_path == "not found yet":
      next_path = ""
  total += next_path
    
print(total)
print(len(total))

# change to whatever you want your output file to be called
out = open('output' + task + '.txt', 'w')
out.write(total)
out.close()