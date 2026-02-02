## Review Activity

### Question 1:  Tracing Code
Consider the following code:

```
modnum = 5
x = 10
counter = 0
while x > 0:
    counter += 1
    if x % 2 == 0 or counter % modnum == 0:
        x += 1
    else:
        x -= 2
    print(f'counter = {counter}, x = {x}')

```
What is the output of the code?
<br><br><br><br><br><br><br><br><br><br><br><br><br>



Can you come up with a nontrivial value for `modnum`
(e.g. not 1, -1, or 0) that causes the code to loop
infinitely (without changing any of the other code)?
If so, what is it and explain why that causes an infinite loop.
If not, explain why.
<br><br><br><br><br><br><br><br><br>


### Question 1:  Loops / Lists
Suppose you have a list of lists representing
shopping carts of customers in line at a store.
Each inner list represents
one shopping cart, specifically the prices
of all of the items in the shopping cart
(we are pretending we don't care what they are).

Your store wants to award a prize to the first 
customer with a shopping cart with a total of
at least $100.

Write Python code to accomplish this task.

<br><br><br><br><br><br><br><br><br><br>



### Classes
1. What is a class?
<br><br>
2. What is the name of one method you are likely to see in any class definition?
<br><br>
3. What is an instance variable?
<br><br>
4. What does it mean to instantiate a class?
<br><br>
5. Suppose you want to implement code to represent a vending machine.
   What seems like the best choice to do so:  a list, a dictionary, or a class?
   Why?
