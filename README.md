# Daily-Problem

This repo contains Python 3.6 solutions to some of the Daily Coding Problem when I manage to get to them. All solution are of my own design and programming, but of course I do not own any of the problems.

## List of Problems Solved

### 1. Problem #27: Well-Formed Brackets

This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.

The solution is available [here](https://github.com/nsadeh/Daily-Problem/blob/master/problem_27.py).

## 2. Problem #28: Justifying Sentences

This problem was asked by Palantir.

Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words `["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]` and `k = `16, you should return the following:

```
["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
```

The solution to this problem is available [here](https://github.com/nsadeh/Daily-Problem/blob/master/problem_28.py). That is my 15-minute solution, I plan to optimize and clean the approach.

The algorithm iterates through each word and appends it to a running `current_word` if the total length is acceptable. If not, it appends the `current_word` to the list to be returned after running `interspace` on it, which disperses spaces according to the instruction inside the phrase.
