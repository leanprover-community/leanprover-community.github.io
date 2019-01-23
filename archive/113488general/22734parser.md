---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/22734parser.html
---

## Stream: [general](index.html)
### Topic: [parser](22734parser.html)

---

#### [Kevin Buzzard (Mar 13 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123663841):
Mario once told me that Lean's parser was an Operator-precedence parser. The manual tells me it's a Pratt-style parser. Is it a top down parser? Furthermore, will the Lean 4 Parser be all of these things, or is this not yet known? I have some very primitive notes on parsers but they are so full of questions that I thought I'd better answer some of them before I started making it public.

#### [Sebastian Ullrich (Mar 13 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123664075):
For notation parsing, the new parser will be all of these things as well. The title of Pratt's original paper is "Top down operator precedence".

#### [Simon Hudon (Mar 13 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123664965):
Any chance that the new parser will have a literate mode like in Haskell?

#### [Andrew Ashworth (Mar 13 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123665065):
my understanding is the parser will be completely extendable in lean, which means a user could implement their own literate mode if they wanted. am i wrong?

#### [Andrew Ashworth (Mar 13 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123665138):
about a year ago i looked into extending asciidoc with lean support in vscode, i really wanted inline TeX rendering and lean code cells in the same document

#### [Andrew Ashworth (Mar 13 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123665235):
but apparently i didn't want it badly enough to finish it :)

#### [Simon Hudon (Mar 13 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123666238):
That would be one way to do it. I would still prefer native support so that everything can be treated as snippets but, more importantly, so that you can have a mean to weaken the strict declaration order. For example, I would like to see something like this:

```
<<aux-decl>>

> def my_fun := -- uses aux declaration

Here I explain my_fun. And now I explain how I construct everything in <<<aux-decl>>> that I haven't shown yet:

<<begin aux-decl>>
> def my_fun_aux1 := -- some of the magic

Explain, explain, now one more decl:

> def my_fun_aux2 := -- the rest of the magic

Tada!
<<end aux-decl>>
```

#### [Andrew Ashworth (Mar 13 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123668193):
that's... a lot of lookahead

#### [Moses Schönfinkel (Mar 13 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123668249):
For not much gain IMHO :).

#### [Simon Hudon (Mar 13 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123670070):
@**Moses Schönfinkel** I disagree. This will help write live documentation. What is worse than no documentation is having documentation that is wrong. I want to write documentation and have it part of the test suites so that we're forced to upgrade it as we move forward with the development

#### [Simon Hudon (Mar 13 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123670177):
But maybe what you mean is that breaking the flow is not worth all that. Again, I disagree. When you write a tutorial, you have to adapt your narrative to follow a realistic sequence of inventions. Often, the first code I write ends up at the end of a file. I think that's the best code to start an explanation with because it justifies all the other inventions in the file

#### [Kevin Buzzard (Mar 13 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123670255):
Let's face it, if Lean or Mathlib were written in this way then it would be a darn sight easier to learn.

#### [Simon Hudon (Mar 13 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123670256):
@**Andrew Ashworth** It is a lot of look ahead but this is not C. When C was invented, they had to arrange the syntax so that they would store as little of a program's syntax tree in memory at any time which is why you need a function's declaration before its definition if you want to call it before it's declared. In our situation, the main reason for forcing the order of declaration is to force a topological order in the between the proofs that refer to each other. I'm not sure if Lean keeps a file's whole syntax tree in memory at any one time but it doesn't strike me as the main design criterion

#### [Andrew Ashworth (Mar 13 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123671350):
yes, but i feel like one of the main design criterions is to make lean performant

#### [Andrew Ashworth (Mar 13 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123671378):
i only made that observation because I doubt Leo will get on board with having that be part of core lean since it slows down parsing and compilation, when the process is already fairly slow

#### [Andrew Ashworth (Mar 13 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123671562):
you can always port cweave and ctangle to lean :) if it was good enough for knuth, it might be good enough for simon, haha

#### [Simon Hudon (Mar 13 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123671567):
I think the question is: is this the slow part of the process?

#### [Simon Hudon (Mar 13 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123671611):
What if Simon is more demanding? :stuck_out_tongue_closed_eyes:

#### [Simon Hudon (Mar 13 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123671633):
The other benefit of having it in Lean itself is that you could benefit from the Lean server while writing Lean documentation

#### [Andrew Ashworth (Mar 13 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123671651):
```quote
I think the question is: is this the slow part of the process?
```
as a mere user, i have no idea, but i'm always interested in being educated

#### [Simon Hudon (Mar 13 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123671652):
On performance again: if it can be disabled for most files it shouldn't slow anything down

#### [Simon Hudon (Mar 13 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123671666):
I have no idea either. I was hoping to get enlightened

#### [Moses Schönfinkel (Mar 13 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123671729):
Perhaps a compromise. Pull the C trick - have a prototype to have the declaration beforehand and then put the proof + explanation + documentation wherever you want?

#### [Simon Hudon (Mar 13 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123671764):
I feel like I shouldn't like your idea but I really do

#### [Simon Hudon (Mar 13 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123671797):
It could be something like:

```
forward my_fun_aux1, my_fun_aux2 
```

where the order matters

#### [Moses Schönfinkel (Mar 13 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123671813):
exactly

#### [Simon Hudon (Mar 13 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123671899):
This is really cool actually :) and can be completely separate from any literate mode

#### [Simon Hudon (Mar 13 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123672096):
Now I'm wondering how that should interact with other features:

```
forward something.my_fun_aux

def my_fun := my_fun_aux foo

namespace something 
variable x : int
def my_fun_aux := x + 3
end something
```

#### [Moses Schönfinkel (Mar 13 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123672449):
Damn I really want to do this now ^^.

#### [Simon Hudon (Mar 13 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parser/near/123672464):
Maybe I should work in advertisement :P

