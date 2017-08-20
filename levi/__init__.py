import turtle

def go_right(step):
     turtle.setheading(0)
     turtle.forward(step)

def go_up(step):
     turtle.setheading(90)
     turtle.forward(step)


def go_left(step):
     turtle.setheading(180)
     turtle.forward(step)

def go_down(step):
     turtle.setheading(270)
     turtle.forward(step)

def levi_draw(step_size,step_number):
    move_dict = {1: go_up,
                 2: go_right,
                 3: go_left,
                 4: go_down
                 }
    for _ in range(step_number):
        move_in_a_direction = move_dict[random.randint(1, 4)]
        move_in_a_direction(step_size)
        
        
        
class Art:
  def __init__(step_size=1,step_number=100):
    levi_draw(step_size,step_number)
  
  def go_up(step=1):
    go_up(step)
    
  def go_down(step=1):
    go_down(step)
  
  def go_right(step=1):
    go_right(step)
    
  def go_left(step=1):
    go_right(step)
     
  def save(fname):
     cv = turtle.getcanvas()
     cv.postscript(file=fname + ".ps", colormode='color')
     turtle.done()
