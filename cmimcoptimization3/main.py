# from ast import literal_eval
# edit to the name of the input file
task = "4"

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
rot = {"U":"R","D":"L","L":"U","R":"D"}
dirs = {"U":[-1,0],"D":[1,0],"L":[0,-1],"R":[0,1]}

# switch the direction of a path
def reverse(s):
  new_s = ""
  for char in s:
    new_s = rev[char] + new_s
  return new_s

# unstick the robots??
def rotate(s):
  new_s = ""
  for char in s:
    new_s = rot[char] + new_s
  return new_s

# is there a robot at this location
def is_robot_at(loc):
  for rob in robots:
    if rob[0] == loc[0] and rob[1] == loc[1]:
      return True
  return False

def num_robots_at(loc):
  num = 0
  for rob in robots:
    if rob[0] == loc[0] and rob[1] == loc[1]:
      num += 1
  return num

def get_path_to_closest(loc1):
  # bfs search
  q = []
  visited = [[False for i in range(c)] for j in range(r)]
  path_to = [["" for i in range(c)] for j in range(r)]
  x = loc1

  visited[x[0]][x[1]] = True
  path_to[x[0]][x[1]] = ""
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
        continue
      #print("appended")
      path_to[new[0]][new[1]] = path_to[s[0]][s[1]] + key
      if is_robot_at(new):
        return [path_to[new[0]][new[1]], new[0],new[1]]
      q.append(new)
  return [False]#raise Exception("wtf where is it")
      
# find the shortest path from every point to the entrance
# BFS lmao
q = []
visited = [[False for i in range(c)] for j in range(r)]
shortestpath = [["" for i in range(c)] for j in range(r)]
x = entrance[0]

visited[x[0]][x[1]] = True
shortestpath[x[0]][x[1]] = ""
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
      continue
    #print("appended")
    shortestpath[new[0]][new[1]] = shortestpath[s[0]][s[1]] + key
    q.append(new)

#path_options = get_all_paths(8)
total = []
total_str = ""
next_path = ""
counter = 0

def move_robots():
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

# current_rob = []
# current_count = 1
while len(robots) > 0:
  print("turn",counter,"robots left",len(robots), "current len",len(total_str))
  # move all the robots first
  move_robots()
  
  #print(robots)

  # start testing for best possible move
  min_score = -1
  # next_path = "not found yet"

  farthest_robs = []
  farthest_rob = entrance[0]
  
  # we're done with the current robot, do this
  current_longest = ""
  for rob in robots:
    # possibility = reverse(shortestpath[rob[0]][rob[1]])
    # path_options.append(possibility[:len(possibility) // 4]) # 7 works the best for task 2???
    # path_options.append(possibility[:len(possibility) // 2 + 1])
    # path_options.append(possibility)
    #print(rob,len(possibility))
    info = get_path_to_closest(rob)
    if len(info[0]) > len(current_longest):
      current_longest = info[0]
    else:
      continue
    if len(shortestpath[info[1]][info[2]]) > len(shortestpath[rob[0]][rob[1]]):
      current_longest = reverse(info[0])
    # if len(possibility) > len(shortestpath[farthest_rob[0]][farthest_rob[1]]):
    #   farthest_robs.append([rob[0],rob[1]])
    #   farthest_rob = farthest_robs[-1]
  next_path = current_longest
  print(next_path)
  total.append(next_path)
  total_str += next_path
  counter += 1
  continue

  if task == "2" and counter <= 2:
    farthest_rob = [robots[2][0],robots[2][1]]
  #print(farthest_rob)
  closest_info = get_path_to_closest(farthest_rob)
  maybe_path = closest_info[0]
  if maybe_path == False:
    next_path = reverse(shortestpath[farthest_rob[0]][farthest_rob[1]])
  else:
    # current_rob = closest_info[1:3]
    # current_count = num_robots_at(current_rob)
    if counter > 3 and ((maybe_path == total[counter - 2] and total[counter - 1] == total[counter - 3]) or total[counter - 1] == maybe_path): #maybe_path == reverse(next_path): (for task 3)
      print("stuck?")
      next_path = reverse(maybe_path)
      #next_path = reverse(shortestpath[farthest_rob[0]][farthest_rob[1]])
      #next_path = next_path[:2] # just head in the entrance direction? len // 4 + 1 works well for 4,5,6
      # 8 for t3 and t4, 6 for t6, and 7 for t5
      #next_path = reverse(shortestpath[farthest_rob[0]][farthest_rob[1]])[:6]
      #next_path = reverse(get_path_to_closest(entrance[0])[0])
      # if len(farthest_robs) >= 2:
      #   info = get_path_to_closest(farthest_robs[-2])
      #   if len(shortestpath[info[1]][info[2]]) > len(shortestpath[farthest_robs[-2][0]][farthest_robs[-2][1]]):
      #     next_path = reverse(info[0])
      #   else:
      #     next_path = info[0]
      # else:
      #   next_path = reverse(maybe_path)
    else:
      next_path = maybe_path

  # if task == "2" and (counter >= 3 and counter <= 3):
  #   next_path = reverse(shortestpath[robots[1][0]][robots[1][1]])
  if task == "2": 
    if counter == 6:
      # next_path = next_path[:140]
      next_path = reverse(shortestpath[robots[1][0]][robots[1][1]])
    if counter >= 4 and counter <= 5:
      next_path = reverse(shortestpath[robots[0][0]][robots[0][1]])
    if counter >= 3 and counter <= 5:
    # print(65 * len(next_path) // 128 + 1)
    # next_path = next_path[:65 * len(next_path) // 128 + 1]
      next_path = next_path[:65 * len(next_path) // 128 + 1]
  

  print(next_path)
  total.append(next_path)
  total_str += next_path
  counter += 1

print(total_str)
print(len(total_str))

# change to whatever you want your output file to be called
out = open('output' + task + '.txt', 'w')
out.write(total_str)
out.close()