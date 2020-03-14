"""
functions mfffff 

Background Knowledge

- Why do we use them? 
> execute code more than once and possiblity in differnt places in a program without having to write it more than once
> organize code so it's more readable and easier to reason about
> make programming easier to debug
> #dontrepeatyourself

-How do they work? 
> the def statement 
> def is an executable statement that tells python to create a function object and assign it a name. 
> bundles all the statements in the function body into a function object, and assigns to that object a name. 
ex: def multiply ():
5 * 5 

-Calling a function
> the def statement makes a function obj, but it doesn't call the function. you have to add () after the function's name to call it. 
> calling a function executes the statements that make up its body. 

Scopes/namespaces
>  global variables and local variables don't clash into each other. 
> global variables, everything outside of the function. Globally available to the program. 
> local variables, inside the function, beneath the def statement. Python creates a whole new scope for the function. Are not available to the global scope. 
> Python will use variables in the local scope before global scope. 

LEGB Rule
> Local, names assigned in any way within a function, and not declared global in that function
> Enclosing function locals, names in the local scope of any and all enclosing functions, from inner to outers. 
> Global (module): names assigned at the top-level of a module file, or declared global in a def within the file.
> Built-in (Python): names preassigned in the built-in names module; open, range .. 

Passing/Returing values to/from functions

> have to figure out if the value is passed by refernece or by value in order to reason about what code is doing. 

Pass by reference
-Python does three things:
> 1. creates an object to represent the value
> 2. creates the variable/name if it doesn't exist already
> 3. links  the variable to the new object



"""
slicing

nums = [4, 56, 73, 12, 17, 99, 42, 87]



print(nums[::]) whole string

print(nums[3::]) starts the count at the 4th element

print(nums[2:6:]) start at position 2 and then end at position before the 6th position

print(nums[2:6:2]) start at 2, end before 6th position and skips by 2

print(nums[::2]) skip by 2

print(nums[-1::]) going backwards

 """