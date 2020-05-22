# Minimal working examples

A minimum working example is a code snippet that can be copied-and-pasted into an empty Lean file and still have the same features (working) and that does not include unnecessary details (minimum).

[Here](https://stackoverflow.com/help/minimal-reproducible-example) is the stackoverflow guide to making MWEs.

Please make sure that your code snippet has:

- correct imports; and
- all the relevant definitions / theorems.

It is fine for your example to throw compiler errors or warnings. In particular, it is fine for your code to contain the keyword `sorry`. The point of MWE is that your code should *throw the same errors in a blank file as it does for you*, that way people can help you with exactly the error you are confused about.

## How do I know if my code is a MWE?

You can *test* this by making a new Lean file, pasting your code snippet into it, and seeing if you get the expected behavior. This is exactly what people who try to help you will do!
 

## What if I'm asking about the [Natural Number Game](https://wwwf.imperial.ac.uk/~buzzard/xena/natural_number_game/)?
If your example comes from the natural number game or any such browser-based lean demo, then you can add a link to the webpage instead of finding the correct imports. So for example it would be much more useful to say "I am on [this level](https://wwwf.imperial.ac.uk/~buzzard/xena/natural_number_game/?world=9&level=4) of the Natural Number Game and my proof script is _blah_", rather than "I am on Advanced Multiplication World Level 4 of the Natural Number Game and my proof script is _blah_".)

If you post a code snippet on Zulip, please make sure it is surrounded in triple backticks.

````text
```
def my_nat : nat := 5
```
````
