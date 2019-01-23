---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/96566BeginnerQuestions.html
---

## Stream: [general](index.html)
### Topic: [Beginner Questions](96566BeginnerQuestions.html)

---


{% raw %}
#### [ Clyde Watson (Jun 28 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128751244):
I'm really new to LEAN (and anything like it), and I've had some problems that might be considered a little too simple.

#### [ Clyde Watson (Jun 28 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128751249):
Questions answered so far:

Let's say that I declared a variable a of type int. How do I attribute a value to it (let's say, 3)?

How would I define a function that searches for a given object in a list?

How do I know that I've reached the end of a list? I want to know this in order to compare if two strings have the same characters at the same positions.

Is there a document where I can check all the avaliable commands for Lean?

How would I declare a local variable inside a function?

New Questions:

Do string and list char represent the same type?

That's it, for now. Thank you all for your time and patience :)

#### [ Simon Hudon (Jun 28 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128751446):
First question: you want a definition. You do it with `def my_def : int := 7`

#### [ Clyde Watson (Jun 28 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128751738):
Thank you for that, Simon!

#### [ Simon Hudon (Jun 28 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128751894):
Second question: 

```lean
def find (x : nat) : list nat -> option nat 
| [] := none
| (y :: ys) := 
if x = y then some 0
         else do r <- find ys
                 return (r + 1)
```

#### [ Clyde Watson (Jun 28 2018 at 05:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128752529):
Thanks again! :simple_smile: I will try to understand the code.

#### [ Simon Hudon (Jun 28 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128752644):
Don't hesitate to ask more questions. I tried to put as little mysterious stuff as possible but I think if you're not a Haskell adept, `do`, `<-`  and `return` are not obvious.

#### [ Mario Carneiro (Jun 28 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128754968):
> First one: Let's say that I declared a variable a of type int. How do I attribute a value to it (let's say, 3)?

The first thing to understand about lean is that it is a *functional programming language*. If you are used to a more traditional imperative programming language, like C, Java, Python, etc, then there is a bit of culture shock to be had. The big thing to know is that there are no "variables* in lean in the sense meant by this word in imperative languages. (My professor always said this was a bad name for them and preferred the term "assignable" for C/Java style mutable memory locations.) In lean, variables are things that you can substitute values for, but their values never change from the time they are declared. In an imperative language you would call these immutable variables, but there are no mutable variables in lean.

To declare a variable and give it a value, you can use `let`:
```
def f (x : nat) : nat :=
let y := 3 in ...
```
Here `f` is a function with an input variable of type `nat`, and inside the body of the function I've declared a variable `y` (also of type `nat`) with value `3`.

#### [ Mario Carneiro (Jun 28 2018 at 07:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128755050):
> Second one: How would I define a function that searches for a given object in a list?
> 
> Third, that's related to the second one: How do I know that I've reached the end of a list? I want to know this in order to compare if two strings have the same characters at the same positions.

Usually, a function which is defined on lists will be done by pattern matching, as in Simon's code. This is done in the first two lines, with `| [] :=` and `| (y :: ys) :=`. This says what to do if the list is empty, and what to do if it is nonempty with head `y` and tail `ys`. Defining the function this way automatically takes care of "knowing when I've reached the end of a list", because you can't even get the value from a list unless you are already in the nonempty case - the nonempty check and value retrieval happen at the same time.

#### [ Mario Carneiro (Jun 28 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128755147):
Here's a function that compares two strings and returns true iff they are equal:
```
def is_equal : list char → list char → bool
| []        []        := tt
| (x :: xs) []        := ff
| []        (y :: ys) := ff
| (x :: xs) (y :: ys) := (x = y) && is_equal xs ys
```

#### [ Mario Carneiro (Jun 28 2018 at 07:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128755265):
> Fourth: Is there a document where I can check all the avaliable commands for Lean?

This depends on what you mean by "command". There are relatively few actual keywords recognized by the lean language, and you can find a relatively complete list in chapters 4 and 5 of the [lean reference manual](https://leanprover.github.io/reference/).

#### [ Mario Carneiro (Jun 28 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128755374):
> Fifth: How would I declare a local variable inside a function? I tried doing the following:
```
def example_def (a : int) : int :=
variable k : int
```
> I have a feeling that I might have to use let k := int in ..., but I'm not really sure.

Since as mentioned there is no such thing as a local assignable in lean, the best you can do is to have a `let` declaration, which also requires that you provide the local variable with a value. This is because unlike most pointer based languages, there is no "universal null" value in all types - the values of a type are all explicitly determined by the type. So if you define a variable of type `int`, then it must contain an integer value, maybe `0` or `42` or something but "unassigned" is not an option. `let k := int` actually declares `k` to be a variable of type `Type` with value `int`, which is probably not what you want.

#### [ Clyde Watson (Jun 29 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128804676):
```quote
Don't hesitate to ask more questions. I tried to put as little mysterious stuff as possible but I think if you're not a Haskell adept, `do`, `<-`  and `return` are not obvious.
```
You are right, it isn't that obvious. What does "some 0" mean?
I'm having some trouble understand the "do r <- find ys return (r +1)" part.  Isn't find missing one argument, that is, the x that it's searching? Also, for some reason, Lean considers ys to have the type "option nat".

#### [ Clyde Watson (Jun 29 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128804735):
Thanks a lot for all the explanations, Mario! It really is a shock. It's the first time I'm seeing a functional programming language.

#### [ Clyde Watson (Jun 29 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128804790):
```quote
Here's a function that compares two strings and returns true iff they are equal:
```
def is_equal : list char → list char → bool
| []        []        := tt
| (x :: xs) []        := ff
| []        (y :: ys) := ff
| (x :: xs) (y :: ys) := (x = y) && is_equal xs ys
```
```
So, according to the piece of code you sent, whenever I want to compare two kinds of lists, I only have to "place them" side by side?

#### [ Clyde Watson (Jun 29 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128805114):
One new quesion: In Lean, are there any differences between string and list char?

#### [ Simon Hudon (Jun 29 2018 at 03:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128805586):
```quote
You are right, it isn't that obvious. What does "some 0" mean?
```

`some 0` could also be written `return 0`. Both are expressions of type `option nat`. `option nat` has two kinds of values `none` or `some n` where `n` is a natural number. That means `option nat` either contains a single natural number or nothing. `return 0` comes in handy when you think of `option nat` as a sequential program that may fail or return a natural number. This leads us to your second question:

```quote
I'm having some trouble understand the "do r <- find ys return (r +1)" part. Isn't find missing one argument, that is, the x that it's searching? Also, for some reason, Lean considers ys to have the type "option nat".
```

I apologize, the expression has a syntax error in it. It should be `do r <- find ys, return (r +1)` (notice the comma in the middle). You can read it as "call `find ys` then, if it doesn't fail (i.e. produce the value `none`) take the result (a natural number), call it `r` and return from the sequence of two instructions with the value of `r+1`"

#### [ Sean Leather (Jun 29 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128813110):
```quote
One new quesion: In Lean, are there any differences between string and list char?
```
This is extracted from the core library ([`init/data/string/basic.lean`](https://github.com/leanprover/lean/blob/master/library/init/data/string/basic.lean#L10-L18)):

```lean
/- In the VM, strings are implemented using a dynamic array and UTF-8 encoding. -/
structure string_imp := (data : list char)
def string := string_imp
```

#### [ Mario Carneiro (Jun 29 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128814743):
> So, according to the piece of code you sent, whenever I want to compare two kinds of lists, I only have to "place them" side by side?

That's the way pattern match syntax works. In this case, since the type of the function is `is_equal : list char → list char → bool`, there are two arguments, both lists of chars, and so each case should include two variables, possibly broken into cases. In my code snippet I broke into all four cases, but you can combine some of them with wildcards `_`, depending on the function you are defining. You should read the second case `| (x :: xs) [] := ff` as being shorthand for the partial specification `is_equal (x :: xs) [] = ff` of the function `is_equal`.

#### [ Mario Carneiro (Jun 29 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128814833):
> One new quesion: In Lean, are there any differences between string and list char?

Just to unpack Sean's answer a bit: In lean, a string is a wrapper around a `list char`. The wrapper is there because there is a change of underlying data representation - I believe `string` is stored as an array of bytes, while `list char` is a linked list, like all `list` structures.

In fact, the whole function `is_equal` already exists in lean so you don't need to define it - it's just `a = b` where `a b : string`. Pretty much all data types defined in lean have an equality test implemented, and you can write equality tests for your own data structures easily as well.

#### [ Mario Carneiro (Jun 29 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128815011):
Here's another way to write Simon's `find` function using pattern matching instead of monad notation:
```
def find (x : nat) : list nat -> option nat
| [] := none
| (y :: ys) :=
  if x = y then some 0 else
  match find ys with
  | none := none
  | some r := some (r + 1)
  end
```
The `match` acts just like the top level pattern match - it takes the result of `find ys`, which is an `option nat`, and breaks into cases depending on if it is `none` or `some r` for some `r`. I mentioned before that lean has no "universal null" value, but when you explicitly want to indicate a "null" value, you do it with the `option` type. Essentially, this function either returns a result, wrapped in `some`, or it returns failure to find the value, encoded as `none` here (you might use "null" for this in other languages).

#### [ Kevin Buzzard (Jun 29 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128816419):
@**Clyde Watson** I started with Lean after very little functional programming experience (I knew some python / java but only as a hobbyist; I am a professional mathematician). I found http://learnyouahaskell.com/ extremely helpful. Your questions about basic pattern matching seem to indicate that you might be able to learn a lot from this resource (or from some other Haskell learning resources, if the informality of this one is not to your taste). Basically the rule is that if you're defining functions on, or proving things about, so-called "inductive types" like the natural numbers or lists, then you use induction (or recursion), and a syntax which is a completely basic part of functional programming with these "|"s.

#### [ Mario Carneiro (Jun 29 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128816592):
terminology note: In Haskell, what we call "inductive types" are called (generalized) algebraic data types or GADTs

#### [ Sean Leather (Jun 29 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128823178):
```quote
I started with Lean after very little functional programming experience (I knew some python / java but only as a hobbyist; I am a professional mathematician). I found http://learnyouahaskell.com/ extremely helpful.
```

@**Kevin Buzzard** That's pretty cool that you used Learn You a Haskell for Great Good. Did you learn Haskell first and then move to Lean or use it as a tutorial about the related concepts in Lean?

#### [ Kevin Buzzard (Jun 29 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128823396):
I am not sure I have learnt Haskell in any real sense. The reason I mentioned it was that the website I mentioned showed me how to define functions on lists by recursion using exactly the notation that the OP was originally asking about. Basically my history was: hobbyist programmer (written simple Android apps in java etc), then in 2016 I attempted to read learnyouahaskell just because (a) I knew the people on our joint maths and computing degree had to learn it in their first term and (b) I'd had an undergraduate doing a maths project with me on elliptic curves and they'd used Haskell to write their code, and then later in 2016 I tried reading it again, and then in 2017 I started trying to code in Lean and then I went back to it for a third time and this time it all made sense. But the concept of defining a function on lists by defining it on the constructors was something which dawned on me on the first reading.

#### [ Reid Barton (Jun 29 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128845444):
```quote
Isn't find missing one argument
```
This is a syntactic oddity of lean--when referring to the thing currently being defined (here `find`) inside its own definition, parameters to the left of the colon (here `(x : nat)`) are fixed, and you don't even write them.

#### [ Reid Barton (Jun 29 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128845733):
So `find ys` inside the definition of `find` means the same as `find x ys` outside it

#### [ Kevin Buzzard (Jun 30 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128853494):
```quote
What does "some 0" mean?
```
I'll show you how to figure this out yourself!

One really important thing to learn in Lean is that every question of this form is a question which you can begin to investigate yourself, and the sooner you learn how to do this the sooner you can figure out what you need to learn next; you can ask really targetted questions which in general receive better answers. 

Here's how you can use Lean to answer your own question, in VS Code. First open a completely new file called scratch.lean and let's see if we can isolate your question. Make this as the only line:

`definition X := some 0`

It works! 

[technical note: This isn't always the case -- sometimes the thing you're trying to understand might rely on some file being imported or some namespace being open and you'll have to resort to right-clicking -- see later.]

Now we have `X` we can see what this `some` command really is -- it's defined in the root namespace and is in core lean, so it's probably important. 

Now we can write stuff like

`#check X`

to see that `X` is a term of type `option ℕ`. So it looks like `option` is a function which eats `ℕ`. What is the type of `ℕ`? We just check with

`#check ℕ`

and we see that `ℕ` has type `Type`. So `option` is a function which eats something of type `Type`. We can look at what `option` is with

`#check option `

and we see it's a function from `Type` to `Type` (just ignore the universes, you can worry about these later). So `some 0` is a term of type `option ℕ`which has type `Type`. So that's where `some 0` lives in the tree of terms, types and universes.

[Pro tip: always be checking there are no red underlines in your code. Sometimes random typos which you don't bother to fix can have weird consequences later on. Learn how to use `sorry` to fix red errors in half-written code]

We didn't look at any definitions yet, we just looked at the types of everything in sight. Everything has a type, and `#check x` tells you the type of `x`. Here is a simple picture of the entire type theory of Lean. There are six kinds of things. There are two universes, `Type` and `Prop`. A type is something of type `Type`, and a term is something of type `α` for `α` a type. A proposition is something of type `Prop`, and a proof is something of type `H` for `H` a proposition. That's it. The `Type` stuff is where computer programs live. `Prop` is where theorems and proofs live. So `some 0` is a computable thing, it's a term of type `option ℕ : Type`. 

Next let's actually unravel the definitions. Right-click on `some` in VS Code and select `Go to definition` (or left-click and press F12). A new file will open called `core.lean` and you'll be taken to about line 279 where you'll see that `option α` is an inductive type with two constructors: `none` and `some val` with `val : α`. So in abstracta your question is answered -- `some` is a constructor which takes `n : ℕ` and returns `some n : option ℕ`. We can just check that with 

`#check some`

and the answer...looks a bit messy. It's clearly some kind of function, but there are question marks. If you don't like those `?M_1` things, you could use the following trick:

`#check @some`

which works with functions and which might produce nicer output. Now we see that `some` is actually a Pi type.

Here's a gist with all those commands in. One of the fiddly little VS Code options on the right is "show the output of all the `#check`s at once"; that might be the one you want here.

https://gist.github.com/kbuzzard/455709bfd5d8fed57f5e4321481adf5b

If you get stuck at some point, send the entire file as a gist (just google for how to do it) or, if it's got quite big, just a minimal working example of your question. It's much easier for experts to answer questions with the full file in front of them. Even experts make silly mistakes sometimes, which others can spot instantly. Actually, sometimes I find my own silly mistakes when I am making the minimal working example. And did I mention to make sure there are no errors in your file?

So that's `option`, and how to ask if you get stuck along the way. But if you want some more insight as to what the point of this type is, or perhaps want to know more about what an inductive type is or a Pi type, or what the different kinds of brackets all mean (round, squiggly, square), now is the time to go to the docs -- Theorem Proving In Lean is a really good place to look for basic stuff. It's here:

https://leanprover.github.io/theorem_proving_in_lean/

 I find the web search functionality really hard to use though; there's a pdf download and I usually search with my pdf viewer and then maybe switch to the html manual later because it looks nicer, if I want to know more. If you want to know more about `option` then the fourth occurrence of " option " in the pdf is the one you want; it's on p101. There you can see a brief description of the point of `option` and examples of other inductive types which have similar structures. I wish I had learnt this method earlier -- it took a while to dawn on me that you could just work everything out by right clicking and figuring out if you were a term or a type, a proof or a proposition.

 You also need to learn a kind of filter -- stuff you can just ignore for the time being.  Stuff like typeclasses, `opt_param`/`out_param`, `[stuff in brackets]` and universes, you can start to worry about them later. Universes are to do with subtle set-theoretic issues like avoiding Russell's Paradox, and the other stuff is technical computer science stuff which you can just treat as magic for the time being. [Typeclasses are some crazy computer science generalisation of notation overloading]

#### [ Amin Bandali (Jun 30 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128879959):
Another beginner question here: Is it possible to "overload" an instance?

`format` has an instance for `list α`:
https://github.com/leanprover/lean/blob/e53f8021ec3bd8b6c7c2eb998932ec79cb941b18/library/init/meta/format.lean#L87-L92
And I'd like to customize that in various places. For instance, say, I'd want to drop the outer square brackets, or another time make the items semicolon-separated rather than comma-separated

#### [ Simon Hudon (Jun 30 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128884679):
It is possible but I wouldn't advise using it that way. Instead, you should explicitly invoke the formatting code that you're interested in. Just to be sure, can you show an example where that would be handy?

#### [ Amin Bandali (Jun 30 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128884895):
I see. The example I was aiming to use that for was a `structure` with a `(exts : list string)` field, which I wanted format using `format!"EXTENDS {my_struct.exts}"`

#### [ Simon Hudon (Jun 30 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128885052):
Yes, that's what I thought. If you replace `format!"EXTENDS {my_struct.exts}"` with `format!"EXTENDS {my_to_fmt my_struct.exts}" you should get the same result. Unlike in Haskell, Lean doesn't guarantee global uniqueness of instances so you have to be vigilant not to make the instance search more difficult

#### [ Amin Bandali (Jun 30 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/128885421):
Thanks for the explanations :simple_smile:  makes sense

#### [ Guy Leroy (Jul 03 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129013476):
Hi, I'm following a simple tutorial for Lean and an exercice is to define a curry function and an uncurry function.
Could anyone help me with this please?

def curry (α β γ : Type) (f : α × β → γ) : α → β → γ := sorry
def uncurry (α β γ : Type) (f : α → β → γ) : α × β → γ := sorry

#### [ Chris Hughes (Jul 03 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129013840):
If you have `a : α` and `b : β` then I can make an element of type `α × β` by writing `⟨a, b⟩`. The pointy bracket is written with `\<`. If I have `x : α × β`, then `x.1` is the first element of the pair and `x.2` is the second element.

#### [ Guy Leroy (Jul 03 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129014538):
Oh thank you. I am still struggling though, the best I came up with is:

def curry (α β γ : Type) (f : α × β → γ) : α → β → γ := λ f x, f x.1 x.2 
def uncurry (α β γ : Type) (f : α → β → γ) : α × β → γ := λ f a b, f ⟨a, b⟩  

which is obvisouly wrong  as the types don't match but I can't figure out how to make it work

#### [ Guy Leroy (Jul 03 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129014608):
Any other hint?

#### [ Mario Carneiro (Jul 03 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129014636):
Your answers are perfect, except they are swapped

#### [ Sean Leather (Jul 03 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129014639):
To add to Chris's answer, there are a couple of things you can do to learn what you need to do.

* `×` is notation for `prod`. How would you know this? You can do `#print ×` in a file and see `_ `×`:35 _:34 := prod #1 #0`.
* Want to find out more about `prod`, use `#print prod`.

```lean
@[derive list.cons.{0} pexpr ``(has_reflect) (list.nil.{0} pexpr)]
structure prod : Type u → Type v → Type (max u v)
fields:
prod.fst : Π {α : Type u} {β : Type v}, α × β → α
prod.snd : Π {α : Type u} {β : Type v}, α × β → β
```

* `structure`s have a default constructor `mk`. Try `#print prod.mk`.
* Lastly, `⟨a, ..., z⟩` is the anonymous constructor that works for many structures and types.

#### [ Chris Hughes (Jul 03 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129014717):
They're not quite perfect. You need to get rid of the `f`s in the lambdas. In lean syntax anything before the colon doesn't need to be introduced with a lambda.

#### [ Chris Hughes (Jul 03 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129014776):
This is correct.
```lean
def curry (α β γ : Type) (f : α × β → γ) : α → β → γ := λ a b, f ⟨a, b⟩
def uncurry (α β γ : Type) (f : α → β → γ) : α × β → γ := λ x, f x.1 x.2 
```

#### [ Sean Leather (Jul 03 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129014805):
Just to help you see, these are also possible:

```lean
def curry (α β γ : Type) : (α × β → γ) → α → β → γ := λ f a b, f ⟨a, b⟩
def uncurry (α β γ : Type) : (α → β → γ) → α × β → γ := λ f x, f x.1 x.2
```

#### [ Guy Leroy (Jul 03 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129014848):
Thank you all for the detailed answers! Greatly appreciate it

#### [ Kevin Buzzard (Jul 03 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129015912):
@**Guy Leroy** Everything is completely logical and you have a logical brain; I remember being confused about all of this a year ago. You came to my talk yesterday, right? `alpha -> beta -> gamma` is a type, and you make terms of that type using `lambda`. After the `lambda` you'd better take a term of type alpha and then a term of type beta, and then you need to return a term of type gamma. So now hopefully you can get your terms sorted out. For products however, you need to learn the notation. The type is `\alpha \times \beta` so now you need to know the constructor and the eliminators, which is a fancy way of saying that you need to know how to get something of type `alpha x beta` from `a : alpha` and `b : beta` (that's the constructor for the product) and then you also need to know how to get the things of type alpha and beta from the thing of type `alpha x beta` -- those are the eliminators. So that's three different pieces of notation -- one for making the product type (that's \times), one for the constructor (that's pointy brackets) and one for the elminators (that's the `.1` and `.2` notation). A year ago all of these were floating around in my head and I'd just try any of them until something worked. But now I realise that if you keep everything straight then it all starts fitting into place. The pointy brackets are often used for constructors, the dots are often used for eliminators (I hope they are called eliminators, I'm no expert) and the notation for the types depends on the type but is something you pick up as you go along.

#### [ Kevin Buzzard (Jul 03 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129015940):
As for the stuff before or after the colon, I've realised that this trips mathematicians up. I need to write something about functions. There's so much functiony stuff which CS people do which is very cool but which we don't see in maths at all! Even using functions as maps from props to props is new to mathematicians.

#### [ Mario Carneiro (Jul 03 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016068):
Actually `.1` is called a projection

#### [ Mario Carneiro (Jul 03 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016073):
an eliminator is `prod.rec` for example

#### [ Guy Leroy (Jul 03 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016118):
Thank you for the explanation. Yes I came yesterday. The syntax is slowly starting to make sense, I'm a bit confused at first as we were taught Haskell in first year and it has some similar features.

#### [ Guy Leroy (Jul 03 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016126):
But I understand the curry/uncurry functions and their syntax now I think

#### [ Kevin Buzzard (Jul 03 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016361):
```quote
an eliminator is `prod.rec` for example
```
Technical interlude: are the projections defined using `prod.rec` or are they inbuilt and appear like axioms when the product type is defined? I don't know how to figure this out. I guess they would be easy to define using `prod.rec`.

#### [ Kevin Buzzard (Jul 03 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016391):
```quote
But I understand the curry/uncurry functions and their syntax now I think
```
When I did that exercise last year, the first thing I wanted to prove was that if you curried and then uncurried, you got back to where you started! But at that point in TPIL you don't have enough tools to do that.

#### [ Kevin Buzzard (Jul 03 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016497):
"The dot operator is how you access the members of an object" I think I once read in a book on Java. Is this not the appropriate language in Lean? It feels like the same sort of thing.

#### [ Mario Carneiro (Jul 03 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016598):
It's a bit hard to tell just by looking at the definition, but projections are defined using the recursor/eliminator

#### [ Sean Leather (Jul 03 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016607):
[In type theory, what is an eliminator, and what is its opposite?](https://www.quora.com/In-type-theory-what-is-an-eliminator-and-what-is-its-opposite)

#### [ Sean Leather (Jul 03 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016667):
Conclusion: a projection is an eliminator.

#### [ Mario Carneiro (Jul 03 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016806):
In lean, projections are a limited version of the `cases_on` eliminator

#### [ Mario Carneiro (Jul 03 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016815):
They only work when the inductive only has one constructor (which is why they are only generated for `structure`s)

#### [ Mario Carneiro (Jul 03 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129016862):
and they are obviously nonrecursive (in programming languages with a fixpoint operator this is not as important as it is in lean)

#### [ Mario Carneiro (Jul 03 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129017129):
The projections are even harder to unfold than I remember... Even `#reduce` doesn't unfold them, I have to unfold first to the underlying projection macro (printed as `[prod.fst c]`), and then force that to expand through a `change`:
```
#print prod.fst
-- @[reducible]
-- def prod.fst : Π {α : Type u} {β : Type v}, prod α β → α :=
-- λ (α : Type u) (β : Type v) (c : prod α β), [prod.fst c]
example {α β} (a : α × β) : prod.fst.{0 0} a = sorry :=
begin 
  delta prod.fst,
  change @prod.cases_on _ _ _ _ _ = _,
  -- prod.cases_on a (λ (fst : α) (snd : β), fst) = sorry
end
```

#### [ Sean Leather (Jul 03 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129017389):
I tend to do `cases a, dsimp` while writing a proof, though I can usually remove the `dsimp` before I'm done.

#### [ Kevin Buzzard (Jul 03 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033519):
Rohan Mitta has just asked me how to formalise an exercise on the topological spaces example sheet: prove that if T1 and T2 are topologies on X (i.e. T1 and T2 are sets of subsets of X) then their intersection is a topology.

#### [ Mario Carneiro (Jul 03 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033547):
this is in lean already

#### [ Kevin Buzzard (Jul 03 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033550):
That sounds like a question to me, but somehow when you formalise it in Lean it becomes more like a construction. I figured that he needed some predicate `is_open_sets` and I just glanced through the topological space lean file and didn't spot it

#### [ Kevin Buzzard (Jul 03 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033562):
I'm sure it's in Lean already, they form some complete semilattice or whatever

#### [ Mario Carneiro (Jul 03 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033572):
it's part of the construction of the complete lattice

#### [ Kevin Buzzard (Jul 03 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033578):
I just saw that. But Rohan is trying to learn how to use Lean so I am happy to encourage him to figure this exercise out himself!

#### [ Kevin Buzzard (Jul 03 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033592):
It's in Lean but it doesn't look like a proposition, it looks like a construction

#### [ Kevin Buzzard (Jul 03 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033642):
Is `is_open_sets` in Lean? I couldn't find it

#### [ Mario Carneiro (Jul 03 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033644):
it is a construction

#### [ Kevin Buzzard (Jul 03 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033659):
It looks like an exercise

#### [ Mario Carneiro (Jul 03 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033665):
what does `is_open_sets` mean?

#### [ Kevin Buzzard (Jul 03 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033700):
`is_open_sets` is a map from set (set X) to Prop and it's the conjunction of the axioms saying that the sets are the opens in a topology. Am I not thinking straight?

#### [ Kevin Buzzard (Jul 03 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033765):
And he wants to prove is_open_sets A and is_open_sets B implies is_open_sets (A intersect B)

#### [ Kevin Buzzard (Jul 03 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033773):
Am I making sense?

#### [ Kevin Buzzard (Jul 03 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033890):
```lean
definition is_open_sets {α : Type u} (is_open : set α → Prop) := 
  is_open univ ∧ (∀s t, is_open s → is_open t → is_open (s ∩ t)) ∧ (∀s, (∀t∈s, is_open t) → is_open (⋃₀ s))
```

#### [ Kevin Buzzard (Jul 03 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129033894):
I think it's that

#### [ Kevin Buzzard (Jul 03 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129034040):
Now I can make the example sheet question into a proposition.

#### [ Kevin Buzzard (Jul 03 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129034141):
Is this some equivalent way of formalising the notion of a topological space? Why did we choose the other way?

#### [ Kevin Buzzard (Jul 03 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129034388):
```lean
definition is_to_top {α : Type u} (is_open : set α → Prop) (H : is_open_sets (is_open)) : topological_space α :=
{ is_open := is_open,
  is_open_univ := H.left,
  is_open_inter := H.right.left,
  is_open_sUnion := H.right.right
}

definition top_to_is {α : Type u} (T : topological_space α) : is_open_sets (T.is_open) :=
⟨T.is_open_univ,T.is_open_inter,T.is_open_sUnion⟩
```

#### [ Kevin Buzzard (Jul 03 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129034394):
They're kind of the same

#### [ Mario Carneiro (Jul 03 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129034413):
yes, it is equivalent to unbundling the set (set A) part of topological_space

#### [ Reid Barton (Jul 03 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129034414):
The difference is just that the mathlib definition does not have the properties split off together into a separate structure/definition

#### [ Kevin Buzzard (Jul 03 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129035139):
So what I find myself wondering again and again is what the best way is. A year ago there were plenty of things I could formalise in 0 ways; now I find there are plenty of things I can formalise in two ways, and I really struggle to know the right way. What I have now understood is that in some sense it doesn't matter, because if I write a good enough API then probably any one of my choices will be fine. But I am beginning to realise that there's more at stake than this.

#### [ Mario Carneiro (Jul 03 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129035491):
particularly in view of the complete lattice structure, the intersection theorem is only one part of bigger structure, and using it as such makes  sense of the whole finer/coarser thing in a more disciplined way

#### [ Sjoerd de Vries (Jul 04 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129076394):
I really am a beginner, so forgive me if I sound incredibly stupid.
I'm trying to define a function which can add vectors with entries in `ℕ`.
I tried something like this:
`namespace vectest
    universe u
    constant vec : Type u → ℕ → Type u
    def vec_add (n : ℕ) : vec (list ℕ) n → vec (list ℕ) n → vec (list ℕ) n := sorry
end vectest `
I don't see how I could specify the desired function like this - of course I intend my input to be a vector of length `n` with entries in `ℕ`, but Lean just sees (as far as I can tell) something of Type `list ℕ` which happens to depend on `n`. I can't really expect to be able to extract values from the list and add them, then put them back into a new list of length `n`, if Lean doesn't know that's what I'm talking about, right?

#### [ Kevin Buzzard (Jul 04 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129076676):
Hi Sjoerd. I would generally discourage the use of `constant`. Is the idea that you want to model vectors of length `n` with entries in `nat`?

#### [ Sjoerd de Vries (Jul 04 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129076678):
Yes, that's the idea.

#### [ Chris Hughes (Jul 04 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129076726):
The best way to do that is a function `fin n → nat`. `fin n` is a type with `n` elements.

#### [ Sjoerd de Vries (Jul 04 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129076959):
So I can think of `fin n` as being a discrete set with `n` elements and of vectors as functions. Is there a pre-defined way of adding functions that I can then use to add vectors? And how would I find out if this thing exists without asking any of you?

#### [ Kevin Buzzard (Jul 04 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129077522):
I think it's not so hard to write these functions yourself and it would probably be a good exercise.

#### [ Chris Hughes (Jul 04 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129077578):
`algebra/pi_instances` contains all of these for `add`, `mul` etc

#### [ Kevin Buzzard (Jul 04 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129077664):
Sjoerd -- feel free to send me a private message if you don't want to spam the chat. `fin n` is a type which has exactly `n` terms, which you can think of as 0,1,...,n-1.

#### [ Sebastian Ullrich (Jul 04 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129077943):
Defining `vector` as a function is quite unusual because of the resulting runtime complexity (which you may not be interested in). The common definitions are as an inductive type ([e.g.](https://github.com/leanprover/lean/blob/a4aae537fe771ee92d746d4a2be1e73c543e48b9/tests/lean/run/smt_ematch3.lean#L5-L7)) or as a subtype of `list` ([`data.vector`](https://github.com/leanprover/lean/blob/master/library/data/vector.lean)).

#### [ Zak (Jul 09 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129318433):
Hey, would anyone mind explaining how to prove `A ∨ B` given two propositions `A` and `B` and a proof of A?

#### [ Zak (Jul 09 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129318435):
I think the question looks a bit like this; 
```lean
theorem prove_or (A B : Prop) (proof_A : A) : A ∨ B
```

#### [ Simon Hudon (Jul 09 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129318792):
You can prove it as:

```lean
theorem prove_or (A B : Prop) (proof_A : A) : A ∨ B :=
or.inl proof_A
```

or 

```lean
theorem prove_or (A B : Prop) (proof_A : A) : A ∨ B :=
by { left, exact proof_A }
```

#### [ Zak (Jul 09 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129318803):
Thank you :D `left` will be very useful

#### [ Simon Hudon (Jul 09 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129320318):
Fun fact: `left` works with any inductive type. It applies the first constructor while `right` applies the second constructor.

#### [ Patrick Massot (Jul 09 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129329261):
https://leanprover.github.io/theorem_proving_in_lean/tactics.html#more-tactics

#### [ Kevin Buzzard (Jul 09 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334456):
I was mulling over `∨` as a result of this question, thinking how one could explain to a beginner how to work this out, and as a result I ran into something which I myself didn't understand. Is `∨` left associative or right associative? If you can't remember then I figured that one way of finding out was just checking for yourself:

```lean
example (P Q R : Prop) : P ∨ Q ∨ R = P ∨ (Q ∨ R) := rfl
example (P Q R : Prop) : P ∨ Q ∨ R = (P ∨ Q) ∨ R := rfl
```

I was expecting precisely one of these to work. But neither does! The first one (which is the right answer) gives the error

```
type mismatch, term
  rfl
has type
  ?m_2 = ?m_2
but is expected to have type
  P ∨ Q ∨ R = P ∨ Q ∨ R
```

#### [ Kevin Buzzard (Jul 09 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334461):
Why does `rfl` not prove that?

#### [ Kenny Lau (Jul 09 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334482):
because `=` is less important than `∨`

#### [ Kenny Lau (Jul 09 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334521):
think about what a = b or c = d means

#### [ Kenny Lau (Jul 09 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334533):
(pp.all would have shown you the problem)

#### [ Kenny Lau (Jul 09 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334550):
```lean
example (P Q R : Prop) : (P ∨ Q ∨ R) = (P ∨ (Q ∨ R)) := rfl
example (P Q R : Prop) : (P ∨ Q ∨ R) = ((P ∨ Q) ∨ R) := rfl
```

#### [ Sebastien Gouezel (Jul 09 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334753):
Another beginner question: I would like to understand why `apply` is failing in the following example:
```lean
import analysis.real order.filter
open filter

lemma test (a b c : real) : tendsto (λx, a * x) (nhds c) (nhds (a * c)) :=
begin
  apply tendsto_mul,   -- this line fails
  apply_instance,
  exact tendsto_const_nhds,
  exact tendsto_id
end
```
I know how to work it out with `apply tendsto_mul _ _` or `refine tendsto_mul _ _` or a direct term proof, but with the above it fails with the error message
```
invalid apply tactic, failed to unify
  tendsto (λ (x : ℝ), a * x) (nhds c) (nhds (a * c))
with
  tendsto ?m_3 ?m_4 (nhds ?m_6) → tendsto ?m_7 ?m_4 (nhds ?m_8) → tendsto (λ (x : ?m_1), ?m_3 x * ?m_7 x) ?m_4 (nhds (?m_6 * ?m_8))
```
What I don't get is why this unification problem is hard. Any hint?

#### [ Patrick Massot (Jul 09 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334812):
This is higher order unification

#### [ Patrick Massot (Jul 09 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334820):
You want Lean to recognize a product of functions

#### [ Kenny Lau (Jul 09 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334825):
no that isn't it

#### [ Patrick Massot (Jul 09 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334826):
But it could be a product in many ways, in principle

#### [ Kenny Lau (Jul 09 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334884):
I suspect it's `apply` not knowing which term is the last thing

#### [ Patrick Massot (Jul 09 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334905):
Hum, it's weird that `apply tendsto_mul _ _` works

#### [ Mario Carneiro (Jul 09 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334982):
note that `tendsto` is itself defined as a pi

#### [ Mario Carneiro (Jul 09 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129334989):
this has been known to confuse `apply` in the past

#### [ Kevin Buzzard (Jul 09 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129335071):
```quote
because `=` is less important than `∨`
```
How ironic that the reason the question came up was that the output of `#print notation ∨` was what inspired me to ask the question, so I already knew that `∨` was unimportant. Thanks Kenny. It's not the first time I've been done over by binding powers -- I get caught out by `∃` occasionally too.

#### [ Sebastien Gouezel (Jul 09 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129335914):
```quote
note that `tendsto` is itself defined as a pi
```
You mean `apply` unfolds the definition of `tendsto` all the way up to the filter inclusion, which is indeed a pi? And then I am not surprised it is confused. Is there a way to tell lean that is should never unfold by itself the definition of `tendsto`, to avoid the problem?

#### [ Mario Carneiro (Jul 09 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129336027):
these instructions are already in place

#### [ Mario Carneiro (Jul 09 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129336028):
`apply` is not supposed to look that deep, but it does

#### [ Mario Carneiro (Jul 09 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129336037):
it will even look through `@[irreducible]` definitions, unlike almost anything else

#### [ Sebastien Gouezel (Jul 09 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129336172):
Yes, I can see that the definition of subset is protected... Do you know if this behavior of `apply`is by design, and for what reason? This is a real pain for what I would like to do.

#### [ Mario Carneiro (Jul 09 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129336641):
It's certainly a bug, but we've got to live with it until lean 4 comes around. It only concerns the calculation of how many underscores to insert, and only then in limited circumstances (I'm not sure Patrick was that far off the mark with the note about higher order unification)

#### [ Mario Carneiro (Jul 09 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129336770):
I think, after you unfold EVERYTHING, the tendsto becomes a bunch of pis applied to a metavariable (the unknown target topology set), which may unfold to still more pis but lean can't be sure

#### [ Sebastien Gouezel (Jul 09 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129338353):
Thanks for your explanations. Indeed, for proofs written by hand, adding some underscores is not a problem. 

I wanted to try my hand at automation, adding `@[tendsto_rules]` before `tendsto` lemmas. With the aim that writing `applys [tendsto_rules]` would try to `apply`successively all the tagged rules, to prove convergence statements. Since `apply` does not work well in this context, I will have to find another exercise to learn tactics.

For fun, an even "better" example: in my example above, if you try to replace the line `exact tendsto_const_nhds` with `apply tendsto_const_nhds` it fails (while the unification looks even easier as there are no premises in `tendsto_const_nhds`), but it works with `apply @tendsto_const_nhds _ _ _ _ _` (I agree, it is only a matter of getting the right number of underscores :)

#### [ Kevin Buzzard (Jul 09 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129339844):
You could write a tactic which is `apply` but which works the way you want it to ;-) I have no idea how hard that would be!

#### [ Patrick Massot (Jul 09 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129342154):
It looks like `apply` is written in C, not Lean

#### [ Sebastien Gouezel (Jul 09 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beginner%20Questions/near/129343466):
I probably speak C++ better than lean, but still I will rather find another exercise, this one is not for me!


{% endraw %}
