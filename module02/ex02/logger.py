import time
from random import randint

def log(func):
    def wrap_fun(*args, **kwargs):
        t1 = time.time()
        f = open("machine.log", "a")
        result = func(*args, **kwargs)
        t2 = time.time()
        str = "(cmaxtime)Running: {:20}".format(func.__name__)
        r_t = (t2 - t1)
        if r_t > 1:
            str += "[ exec-time = {:.3f} s ]".format(r_t)
        else:
            str += "[ exec-time = {:.3f} ms ]".format(r_t * 1000)
        f.write(str)
        f.write("\n")
        f.close()
        return result
    return wrap_fun 

class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
      if self.water_level > 20:
          return True
      else:
          print("Please add water!")
          return False

    @log
    def boil_water(self):
        return "boiling...."
    
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)