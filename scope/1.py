# username = "chaiourcode"

# def func():
#    username="chai"

#    print(username)
# func()
# print(username)




def chaiourcode(num):
   def actual(x):
      return x**num
   return actual

f = chaiourcode(2)
g = chaiourcode(3)

print(f(2))
print(g(3))
