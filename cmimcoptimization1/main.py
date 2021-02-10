import math

task = "6"

# edit to the name of the input file
f = open('uniqueproducts'+ task + '.txt', 'r')
n,m = map(int, f.readline().strip().split())
subsets = []
# replace from here to line 10 with your own logic
# variables available are just n and m, which are as described in the problem

all_primes = set([2,3])
all_not_primes = set([])

def is_prime(n):
  if n in all_primes: return True
  if n in all_not_primes: return False
  if n < 2 or n%2 == 0: 
    all_not_primes.add(n)
    return False
  if n < 9: 
    all_primes.add(n)
    return True
  if n%3 == 0: 
    all_not_primes.add(n)
    return False
  r = int(n**0.5)
  # since all primes > 3 are of the form 6n ± 1
  # start with f=5 (which is prime)
  # and test f, f+2 for being prime
  # then loop by 6. 
  f = 5
  while f <= r:
    #print('\t',f)
    if n % f == 0: 
      all_not_primes.add(n)
      return False
    if n % (f+2) == 0: 
      all_not_primes.add(n)
      return False
    f += 6
  all_primes.add(n)
  return True   

# https://stackoverflow.com/questions/16007204/factorizing-a-number-in-python
# f = lambda n: (p:=[next(i for i in range(2, n+1) if n % i == 0)] if n>1 else [])+(f(n//p[0]) if p else [])

def f(n):
  if n <= 1:
    return []
  p = []
  i = 2
  while n > 1:
    if n % i == 0 and is_prime(i):
      p.append(i)
      n = n // i
    else:
      if i == 2:
        i += 1
      else:
        i += 2
  return p 

# get prime numbers
primes = []
not_primes = []
for i in range(2, m):
  if is_prime(i):
    primes.append(i)
  else:
    not_primes.append(i)
print(primes)
num_primes = len(primes)
print("there are",num_primes,"primes")

# start by adding 1 to each set

counter = 0

# FIXME: it's just broken lol
# if task == "4":
#   subsets.append([1,2,61,67,71,73,79,83,89])
#   subsets.append([1,3,13,17,29,31,41,47,59])
#   subsets.append([1,5,7 ,11,19,23,37,43,53]) #41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89
#   counter = 8
# elif task == "5":
#   subsets.append([1,2,101,103,107,109,113,127,131])
#   subsets.append([1,3,47 ,53 ,59 ,61 ,67 ,79 ,89])
#   subsets.append([1,5,29 ,31 ,37 ,41 ,23 ,71 ,83])
#   subsets.append([1,7,11 ,13 ,17 ,19 ,43 ,73 ,97]) #97, 101, 103, 107, 109, 113, 127, 131
#   counter = 8
# elif task == "1" or task == "2" or task == "3":
#   # subsets.append([1,2,19,13,17])
#   # subsets.append([1,3,5 ,7 ,11])
#   # subsets.append([1,2,3,73,79,83,89,97,101,103,107,109,113,127,131,133,137,139,149])
#   # subsets.append([1,5,7,11,13,17,19,23,29 ,31 ,37 ,41 ,43 ,47 ,53 ,59 ,61 ,67 ,71])
#   subsets.append([1,2,5])
#   subsets.append([1,3,7])
#   start = 12 #task 2: 35
#   subsets[0] = subsets[0] + primes[4+start:4+2*start]
#   subsets[1] = subsets[1] + primes[4:4+start]
#   #print(len(subsets[0]), (len(subsets[1])))
#   counter = len(subsets[0]) - 1

# for i in range(n):
#   subsets.append([1])
# subsets.append([1,2,5,7,11,13,17,19]) 
# subsets.append([1,3,23,29,31,37,41,43,47,53]) 
# subsets.append([1,2,5,7,11,13]) 
# subsets.append([1,3,17,19,23,29,31,37,41,43,47,53])  

if task == "1":
  subsets.append([1,2, 53,59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397]) 
  subsets.append([1,3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
if task == "2":
  start = 38
  subsets.append([1,2] + primes[start:])
  subsets.append([1] + primes[1:start])
if task == "3":
  start = 83
  subsets.append([1,2] + primes[start:])
  subsets.append([1] + primes[1:start])
if task == "4":
  pre = 3
  start = 211
  pre_start = 26
  subsets.append([1,2] + primes[start:])
  subsets.append([1,3] + primes[pre_start:start])
  subsets.append([1,5] + primes[pre:pre_start])
if task == "5":
  pre = 4
  pre_start = 15
  pre_start2 = 53
  start = 105
  
  subsets.append([1,2] + primes[start:])
  subsets.append([1,3] + primes[pre_start2:start])
  subsets.append([1,5] + primes[pre_start:pre_start2])
  subsets.append([1,7] + primes[pre:pre_start])
  # del primes[0]
  # step = 2
  # counter = 0
  # while (counter + 1) * (step) <= start:
  #   j = 0
  #   # alternate the direction we add the numbers
  #   if counter % 4 == 0 or counter % 4 == 3:
  #     r = range(1,3)
  #   else:
  #     r = range(2, 0, -1)
  #   for i in r:
  #     # print(counter * step + j)
  #     subsets[i].append(primes[counter * step + j])
  #     j += 1
  #   counter += 1

#primes = sorted(primes, reverse=True)

# add prime numbers intelligently
# p_i = 16
# while p_i < len(primes) - 0:
#   p = primes[p_i]
#   #print("old")
#   composites = []
#   for s in subsets:
#     current_composites = 0
#     for c in not_primes:
#       factors = f(c)
#       unique = True
#       located = False
#       first = factors[0]
#       if first in s:
#         located = s
#       else:
#         continue
#       #print(first,located)
#       for k in range(1,len(factors)):
#         if not factors[k] in s:
#           #print(k,"not in",located)
#           unique = False
#           break
#       if unique:
#         current_composites += 1
#         #print(c)
#     composites.append(len(s) + current_composites)
#   #print("new")
#   new_composites = []
#   for s_i in range(len(subsets)):
#     subsets[s_i].append(p)
#     #print(s_i,p)
#     current_composites = 0
#     for c in not_primes:
#       factors = f(c)
#       unique = True
#       first = factors[0]
#       if not first in subsets[s_i]:
#         continue
#       #print(first,located)
#       for k in range(1,len(factors)):
#         if not factors[k] in subsets[s_i]:
#           #print(k,"not in",located)
#           unique = False
#           break
#       if unique:
#         current_composites += 1
#         #print(c)
#     #print(current_composites)
#     new_composites.append(len(subsets[s_i]) + current_composites)
#     del subsets[s_i][-1]
  
#   # for task 1,2,3 only for now
#   # if p_i < 5:
#   #   if (abs(composites[0] - new_composites[1]) > abs(composites[1] - new_composites[0])):
#   #     subsets[1].append(p)
#   #   else:
#   #     subsets[0].append(p)
#   if (abs(composites[0] - new_composites[1]) < abs(composites[1] - new_composites[0])):
#     subsets[1].append(p)
#   else:
#     subsets[0].append(p)
#   print(p,composites,new_composites)
#   p_i += 1
  # p_i += 2
  # if p_i >= len(primes):
  #   if p_i % 2 == 0:
  #     p_i = 1
  #   else:
  #     break


# add prime numbers
# step = n
# while (counter + 1) * (step) <= num_primes:
#   j = 0
#   # alternate the direction we add the numbers
#   if counter == 0 or ((task == "1" or task == "2" or task == "3") and (counter % 4 == 0 or counter % 4 == 3)):
#     r = range(len(subsets))
#   else:
#     r = range(len(subsets) - 1, -1, -1)
#   for i in r:
#     # print(counter * step + j)
#     subsets[i].append(primes[counter * step + j])
#     j += 1
#   counter += 1

for i in subsets:
  print("len",len(i))

leftovers = []

# add composite numbers to subsets
for i in not_primes:
  factors = f(i)
  unique = True
  located = []
  first = factors[0]
  for j in range(len(subsets)):
    if first in subsets[j]:
      located = j
  #print(first,located)
  for k in range(1,len(factors)):
    if not factors[k] in subsets[located]:
      #print(k,"not in",located)
      unique = False
      leftovers.append(i)
      break
  if unique:
    subsets[located].append(i)
    #print("unique")

#print(leftovers)

# def get_products(subs):
#   if len(subs) == 2:
#     products = []
#     for i in subs[0]:
#       for j in subs[1]:
#         products.append(i * j)
#     return products
#   else:
#     prev_products = get_products(subs[1:])
#     new_products = []
#     for i in subs[0]:
#       for j in prev_products:
#         new_products.append(i * j)
#     return new_products


# for i in leftovers:
#   for sub_i in range(len(subsets)):
#     subsets[sub_i].append(i)
#     p = get_products(subsets)
#     p_set = set(p)
#     if len(p) != len(p_set):
#       del subsets[sub_i][-1] # contains duplicates
#       print(i,"contains duplicates")

min_len = m
total_len = 0
for i in subsets:
  print("len",len(i))
  total_len += len(i)
  if len(i) < min_len:
    min_len = len(i)
print(total_len)

for i in range(len(subsets)):
  subsets[i] = subsets[i][:min_len]

# print()
# assert len({len(i) for i in subsets}) == 1, "Subsets are not of equal size"

#delete the last number in the output

# change to whatever you want your output file to be called
out = open('output'+ task + '.txt', 'w')
for s in subsets:
    for i in range(len(s)):
        out.write(str(s[i])+" ")
    out.write("\n")
out.close()