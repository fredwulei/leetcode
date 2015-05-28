Ideas
=====

This question is easier than Integer to Roman.

Read every symbols in a Roman number, then add up all of them. The only exception is when smaller symbols appear before larger ones, such as "IX", "IV". And since there cannot be more than one smaller symbol at one time, i.e. "IIV" is impossible, so we just store the last symbol we read, and if we meet larger symbol later, we just need to substract twice of the amount of smaller symbol. For example, when processing "IX", we get an "I" first, `res = 1`, then we find a "X", which is greater than "I", so `res = res - 2*1 + 10`, thus we get 9.