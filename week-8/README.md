https://replit.com/@NathanE2/week-8-exercise-1

We're going cap off chapter 7 (functions) with one of its programming exercises (7.7 programming exercise 6)

How do we break this problem apart? Visualize as a tree of decisions (google slides?)

q: is speeding?
     yes           no
is over 90mph?
yes         no


Before we start writing code, how will we know if we've solved the problem correctly?

Ex. hacker whitelist, run the program and see if it gave you an "A"
Ex. build a pizza, if it's tasty, great. if its not, tweak the ingredients and try again

But what if we were building cars? There's less room for error. Example https://en.wikipedia.org/wiki/Mars_Climate_Orbiter

In our program, instead of $200, we accidentally type an extra zero ($2,000) in this program?

  We need a way to prove correctness of our programs, especially if our lives, money, etc depend on the program being correct (no bugs)

Going to show you a fast, easy way to prove correctness before we code the function

## Intro to Unit Testing / Test-Driven Development

start with if statements

can be shortened to assertions

Its okay for these to fail (for now)!

Now we can jump in (make sure to run these periodically!)

## Time left?

Fibonacci (or fizzbuzz (https://www.interviewbit.com/problems/fizzbuzz/, https://www.hackerrank.com/challenges/fizzbuzz/problem))

```
# find the nth number in the fibonacci sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

# ^  ^  ^  ^  ^  ^  ^  ^   ^   ^   ^   ^
# 1  2  3  4  5  7  8  9   10  11  12  13


def find_fib(n):
  pass

```

Start with writing unit tests / assertions, write code later

## Next

Depending on how far we get, git & classes might be best next

# Part 2: Wednesday

Fizzbuzz (what is the modulo?)

For homework, going to do 8.8 programming exercise 1

----

Recap: we're nearing the end of the book

Test-driven development

Object Oriented Programming

----

Show slides about python classes
