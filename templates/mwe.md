# Minimal working examples

## tl;dr

When posting code on Zulip, please include all `import`s and `open`s and `universe`s and `variable`s, so others can simply just cut and paste what you post, and see the same issue that you are seeing. The best way to ensure you have done this is to make a completely new Lean file containing only what you are proposing to post, and checking that it compiles.

Bad example:

```
#check (univ : set X)
```

Good example:

```
import data.set.basic

universe u

variable (X : Type u)

open set

#check (univ : set X)
```

Tip: If you are using [Mathlib](https://github.com/leanprover-community/mathlib) and have `import tactic` in your file, there's a tactic called [`extract_goal`](https://leanprover-community.github.io/mathlib_docs/tactics.html#extract_goal) that can help you format the current goal as a stand-alone example.
Note you still need to include the corresponding `import`s and `open`s and `universe`s and `variable`s as mentioned above.

## Formal Definition

A **minimal working example** is a code snippet that can be copied-and-pasted into an empty Lean file and still have the same features (working) and that does not include unnecessary details (minimal).

[Here](https://stackoverflow.com/help/minimal-reproducible-example) is the StackOverflow guide to making MWEs.

Please make sure that your code snippet has:

- correct imports; and
- all the relevant definitions / theorems.

It is fine for your example to throw compiler errors or warnings. In particular, it is fine for your code to contain the keyword `sorry` (and indeed, replacing irrelevant proofs with `sorry` is a good way of minimizing your example). The point of MWE is that your code should *throw the same errors in a blank file as it does for you*, that way people can help you with exactly the error you are confused about.

## How do I know if my code is a MWE?

You should *test* this by making a new Lean file, pasting your code snippet into it, and seeing if you get the expected behavior. This is exactly what people who try to help you will do!

## What if I'm asking about the [Natural Number Game](https://wwwf.imperial.ac.uk/~buzzard/xena/natural_number_game/)?

If your example comes from the Natural Number Game or any such browser-based Lean demo, then you can add a link to the webpage instead of finding the correct imports. So for example it would be much more useful to say "I am on [this level](https://wwwf.imperial.ac.uk/~buzzard/xena/natural_number_game/?world=9&level=4) of the Natural Number Game and my proof script is _blah_", rather than "I am on Advanced Multiplication World Level 4 of the Natural Number Game and my proof script is _blah_".

If you post a code snippet on Zulip, please make sure it is surrounded in triple backticks.

````text
```
def my_nat : nat := 5
```
````

## Tips for minimizing code

- For the purposes of making a MWE, you can replace all proofs of `theorem`s and `lemma`s (outside of the one you're working on) with `sorry`. Lean will give you extra warnings, but these are harmless.

- Remove all declarations (`def`s, `theorem`s, `lemma`s, `example`s, etc.) that are irrelevant to the issue you're seeing. In general, if you can comment out some code without throwing errors, then it can be removed.

- After deleting some code, you can then delete all the declarations that were only referenced there. By repeating this process a few times, you may be able to shorten a long file to just a few lines.
