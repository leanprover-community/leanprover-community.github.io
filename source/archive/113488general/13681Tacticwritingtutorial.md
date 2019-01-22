---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/13681Tacticwritingtutorial.html
---

## [general](index.html)
### [Tactic writing tutorial](13681Tacticwritingtutorial.html)

#### [Patrick Massot (Dec 03 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150758082):
More and more people are writing tactics, and providing bits of explanations here, but I never remember. So I decided to use my last hope option: I tried to teach it. The result is at https://github.com/leanprover-community/mathlib/blob/tactic_tutorial/docs/extras/tactic_writing.md Not only I hope this will help me remember this stuff, but also I hope it will allow experts to clear my misconceptions. And of course it would be a nice extra if it could teach someone something useful, so I'd be interested to know if any tactic writing newbie can read it (I know Johan already read it, because he carefully monitors our community repository).

#### [Patrick Massot (Dec 03 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150758135):
Of course I also hope more stuff will be added here, by me or others. Don't hesitate to contribute, it's in the community repository.

#### [Mario Carneiro (Dec 03 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150758907):
This is a really nice writeup. A comment: the "pseudo-python" syntax
```python
t = infer_type(H)
return H if unify(e, t) else find_matching_type(e, HS)
```
was a bit confusing for me due to the infix conditional. Is this really how they do it in python? How about something a bit more C-like:
```python
t = infer_type(H)
if unify(e, t):
  return H
else:
  find_matching_type(e, HS)
```

#### [Mario Carneiro (Dec 03 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150758978):
although it occurs to me that what lean is doing with `unify` is more like a try catch than a conditional:
```python
t = infer_type(H)
try:
  unify(e, t)
  return H
catch:
  find_matching_type(e, HS)
```

#### [Patrick Massot (Dec 03 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150758996):
What I wrote is indeed valid python

#### [Johan Commelin (Dec 03 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759013):
Yes, I thought so as well. So why did you call it pseudo-python?

#### [Patrick Massot (Dec 03 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759019):
But I agree the `try`/`except` (not catch) version is closer to what is happening in Lean. But I didn't want to include too much python...

#### [Patrick Massot (Dec 03 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759058):
You guys need to learn more python

#### [Mario Carneiro (Dec 03 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759063):
(NB: I don't know python, I'm inventing pythonic syntax on the fly. code highlighting says the word isn't `catch`)

#### [Mario Carneiro (Dec 03 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759064):
ah

#### [Patrick Massot (Dec 03 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759076):
Maybe I should switch to a more generic imperative pseudo-code

#### [Mario Carneiro (Dec 03 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759091):
the funny thing is I've written several complete programs in python, but some of the syntax differences are meh

#### [Mario Carneiro (Dec 03 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759560):
@**Jeremy Avigad** you should take a look at this

#### [Mario Carneiro (Dec 03 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759657):
>  Parsing a token is introduced by `lean.parser.tk` followed by a string which must be taken from a predetermined list (the initial value of this list seems to be hardwired into Lean source code, in `frontends/lean/token_table.cpp`). 

This list is added to when you use literals in `notation`, `infix`, or `precedence`.

#### [Mario Carneiro (Dec 03 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759735):
Importantly, marking something as a token causes it to no longer be a valid name, just like `have`

#### [Mario Carneiro (Dec 03 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759767):
which is why so many interactive tactics use the same few tokens `:` `using` `generalizing` `with` for separators

#### [Patrick Massot (Dec 03 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759857):
Thanks Mario, this is one of the places where I hoped there would be clarifications

#### [Patrick Massot (Dec 03 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759997):
Jeremy, I hope you don't mind I'm invading PIL's territory, but this tutorial is written from a different perspective, more hands-on and shallow. And of course you can contribute too!

#### [Patrick Massot (Dec 03 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150760035):
Note to myself: I should replace paths to the core library or Lean source code with actual http links

#### [Mario Carneiro (Dec 03 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150760593):
For the monad cheat sheet:
* `return`: produce a value in the monad (type: `A -> m A`)
* `ma >>= f`: get the value of type `A` from `ma : m A` and pass it to `f : A -> m B`. Alternate syntax: `do a <- ma, f a`
* `f <$> ma`: apply the function `f : A -> B` to the value in `ma : m A` to get a `m B`. Same as `do a <- ma, return (f a)`
* `ma >> mb`: same as `do a <- ma, mb`; here the return value of `ma` is ignored and then `mb` is called. Alternate syntax: `do ma, mb`
* `mf <*> ma`: same as `do f <- mf, f <$> ma`, or `do f <- mf, a <- ma, return (f a)`.
* `ma <* mb`: same as `do a <- ma, mb, return a`
* `ma *> mb`: same as `do ma, mb`, or `ma >> mb`. Why two notations for the same thing? Historical reasons
* `pure`: same as `return`. Again, historical reasons

#### [Mario Carneiro (Dec 03 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150760832):
* `failure`: failed value (specific monads usually have a more useful form of this, like `fail` and `failed` for tactics)
* `ma <|> ma'` recover from failure: runs `ma` and if it fails then runs `ma'`.
* `a $> mb`: same as `const a <$> mb` or `do mb, return a`
* `ma <$ b`: same as `const b <$> ma` or `do ma, return b`

#### [Scott Morrison (Dec 03 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150761418):
oof `<*` and `<$` are so confusing... "return the value on the ???"

#### [Patrick Massot (Dec 03 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150797886):
Does anyone know how to print the list of currently registered tokens?

#### [Mario Carneiro (Dec 03 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150797962):
`#print notation`

#### [Mario Carneiro (Dec 03 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150798018):
hm, `generalizing` isn't on that list

#### [Patrick Massot (Dec 03 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150798100):
with and using are not there either

#### [Mario Carneiro (Dec 03 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150798650):
Reading the code, I don't see any other way of listing all tokens, although you can test if a name is a token easily enough

#### [Mario Carneiro (Dec 03 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150798684):
i.e. `#print wit` and `#print with` give different errors

#### [Kenny Lau (Dec 03 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150798705):
so... it is a Δ1 set

#### [Patrick Massot (Dec 03 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799491):
```quote
* `a $> mb`: same as `const a <$> mb` or `do mb, return a`
* `ma <$ b`: same as `const b <$> ma` or `do ma, return b`
```
Are these `const` descriptions really correct? It looks like `const` is missing its type argument

#### [Mario Carneiro (Dec 03 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799644):
it's implicit

#### [Mario Carneiro (Dec 03 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799649):
`const a := λ_, a`

#### [Mario Carneiro (Dec 03 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799732):
Actually most of these are actually defined using `const`, many more than I used, but it's not a very transparent way to write it

#### [Mario Carneiro (Dec 03 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799786):
`map_const α β := map ∘ const β`

#### [Mario Carneiro (Dec 03 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799793):
crystal clear

#### [Mario Carneiro (Dec 03 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799857):
`map_const` is `<$` btw

#### [Mario Carneiro (Dec 03 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799885):
oops, it's not implicit

#### [Patrick Massot (Dec 03 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799889):
Here I see `function.const : Π {α : Sort u_1} (β : Sort u_2), α → β → α`

#### [Patrick Massot (Dec 03 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799899):
And I don't see how it would make sense to have it implicit

#### [Patrick Massot (Dec 03 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799903):
how would you infer it?

#### [Mario Carneiro (Dec 03 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799923):
you would normally write that with B implicit

#### [Mario Carneiro (Dec 03 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799939):
because it's inferrable from the last argument

#### [Patrick Massot (Dec 03 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150800016):
when you apply the constant function yes, but not when talking about the function

#### [Mario Carneiro (Dec 03 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150800017):
but `const` is often used partially applied, and in that case having it implicit can be problematic

#### [Patrick Massot (Dec 03 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150800035):
we're almost synchronous

#### [Patrick Massot (Dec 03 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150804993):
So, should I open a PR, or are there more suggestions, contributions, or questions?

#### [Rob Lewis (Dec 03 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150806366):
This looks really nice, Patrick, thanks! I see a few small mistakes/typos. I can make adjustments myself or comment on a PR, either way is no problem. But it's bedtime now, so tomorrow.

#### [Jeremy Avigad (Dec 04 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150814115):
@**Patrick Massot** Indeed, this is very nice. Do you want to consider becoming one of the authors of Programming in Lean? For personal reasons, I'd like to maintain tight control over TPiL (because it has been a labor of love for a number of years), but we never got very far with PiL, and I'd be happy to have collaborators for that. (We added Jared Roesch to the list of authors early on, because he intended to work on it, but in the end he never did, so his name should be removed.) In Amsterdam, I can show you how to set up and maintain the Sphinx repository (but maybe you are already comfortable doing that).  A caveat: the repository is set up for a Linux installation of Sphinx, and I don't know if it is possible to get it running on Windows. (I know that Rob Lewis has had trouble getting our Logic and Proof running on Windows.)

#### [Patrick Massot (Dec 04 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150833320):
@**Jeremy Avigad** Thanks for the kind words and your trust. I think there is room for both an informal tutorial and PIL. But I'd love to help with any documentation project. I've already compiled TPIL, so I guess I could handle compiling PIL as well.  I'm tempted to write we can discuss all this in Amsterdam, but unfortunately I'll be extremely busy after the Amsterdam workshop, so maybe we should start now, especially if you have something specific in mind (not that I really have time, but it will be much worse after Christmas).

#### [Patrick Massot (Dec 04 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150833394):
@**Rob Lewis** please feel free to correct typos and mistakes directly. The community repository is dedicated to that. I think you can even do the correction from github, without pulling the branch. And pulling the branch won't be a problem either, there is nothing to compile, it's all markdown.

#### [Patrick Massot (Dec 04 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150833417):
Actually maybe we should consider including a Lean file gathering all examples from the tutorial. I have it on my computer of course, but I wouldn't know where to put it in the repository

