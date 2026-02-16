## Midterm Review Activity

### Question 1
Suppose you wish to write a function named
`get_longest_lens`
that takes in a lists of
lists of strings and for returns a list of containing the length
of the longest string in each inner list.

As an example, consider the list of lists:
```
words_lsts = [['cat','dog','mouse'],
              ['elephant','giraffe','hippo'],
              ['sheep','seal','shark','aardvark']]
```
The function would return the following list:
```
[5,8,8]
```

Write this function:
<br><br><br><br><br><br><br><br><br><br><br><br>

### Question 2
```
def transform(list1, list2):
    print("transform: start")

    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both inputs must be lists")

    if len(list1) != len(list2):
        raise ValueError("Lists must be the same length")

    result = []
    for i in range(len(list1)):
        result.append(a / b)
    
    return result


def analyze(a, b):
    print("analyze: start")
    try:
        result = transform(a, b)
        print("analyze: transform worked")
    except ValueError:
        print("analyze: caught ValueError")
    except ArithmeticError:
        print("analyze: caught ArithmeticError")
    except ZeroDivisionError:
        print("analyze: caught ZeroDivisionError")
        return []
    else:
        return result
    finally:
        print('analyze done')


if __name__ == '__main__':
    x = analyze([10, 20, 30], [2, 4, 5])
    print("Result X:", x)

    y = analyze([5, 10], [1, 0])
    print("Result Y:", y)

    z = analyze([1, 2, 3], [1, 2])
    print("Result Z:", z)

    w = analyze("not a list", [1, 2, 3])
    print("Result W:", w)
```

What is the output of the above code?
