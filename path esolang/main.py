"""Path is an esolang created by Gaham where multiple brackets are used as a part of a code
(...) pushes the length of the contents surrounded by curly brackets
[...] comments
<...> manages the program execution state"""
m="";s=[];l=[]
def code(i):
  global m
  for c in i:
    if c=="<":m="Y"
    elif c==">":break
    elif c=="(" and m=="Y":m="a"
    elif c==")" and m=="a":
      m="Y"
      s.append(len(l))
      while len(l)>0:l.pop()
    elif m=="a":l.append(c)
    elif c=="[" and m=="Y":m="i"
    elif c=="]" and m=="i":m="Y"
    elif m=="i":continue
    else:print("UNKNOWN COMMAND. HALT");break
  print(f"stack:{s}")
code("")