# Tracing Exceptions 

Consider the following code:

```
class BadPaintException(ValueError):
    pass

class ExceptionFun:
  
    def __init__(self, nums):
        self.lst = []
        for n in range(len(nums)):
            try:
                self.lst.append(Car())
                self.lst[-1].repaint(nums[n])
            except ValueError:
                continue
            except BadPaintException:
                raise ValueError("something bad happened in constructor")

    def crash(self, indices):
        try:
            for idx in indices:
                self.lst[idx].damaged = True
                self.lst[idx].color = 'mixed'
class Car:
    def __init__(self):
        self.color = 'blue'
        self.doors = 4
        self.damaged = False

    def repaint(self, num):
        if num == 5:
            self.color = 'green'
        elif num == 4:
            self.color = 'yellow'
        elif num == 3:
            self.color = 'black'
        elif num == 2:
            self.color = 'silver'
        elif num == 1:
            self.color = 'blue'
        else:
            raise BadPaintException



if __name__ == '__main__':
    try:
        print('starting')
        ef = ExceptionFun([5, 1, 4, 3, 2, 1, 4, 3, 3, 5, 6])
        print('done calling constructor')
        #ef.crash([5, 11, 1, 3])
        ef.crash([5, 2, 1, 3])
        print('done calling crash')
    except ValueError:
        print('bad value')
    except IndexError:
        print('bad index')
    except BadPaintException as e:
        print('oops')
        print(e)
    else:
        print('all good')
    finally:
        print('done')

```

What is the output of the code?


<br><br><br><br><br><br>



