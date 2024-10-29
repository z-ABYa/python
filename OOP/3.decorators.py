def greet(fx):
  def mfx(*args, **kwargs):
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")
  return mfx

@greet # or greet(hello)() -> [after defining hello fn]
def hello():
  print("Hello world")

hello()


@greet
def add(a, b):
  print(a+b)
  
add(1, 2)
# greet(add)(1, 2)