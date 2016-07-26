Ideas
=====

There are two kinds of palindromic substring patterns:

1. Even String (abccba)
2. Odd String (abcba)

The algo splits from the middle of the whole string, until reaches the two ends of it.

In every positions, compares two slices from middle to ends.

Keeps the longest substring, skips when one of the slices is shorter than the already known longest palindromic substring.
