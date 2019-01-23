---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/67415mathlibfileorganization.html
---

## Stream: [general](index.html)
### Topic: [mathlib file organization](67415mathlibfileorganization.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 01 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406142):
For those interested in the file organization of mathlib, I've written up a [proposal](https://github.com/leanprover/mathlib/issues/148) for a small change that, I think, will improve things a bit. Feedback welcome!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 01 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406319):
Interesting proposal. I have also noticed myself getting lost in the long files...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 01 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406367):
I would also like to separate the "interface lemma's" from the "real beef", although maybe there is not always a clear line between them.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 01 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406374):
```quote
I have also noticed myself getting lost in the long files...
```
I'm glad I'm not the only one. I think this is a first logical step to reducing the size of files. There are other steps that can be taken later, of course.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 01 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406415):
Also, I have never read what the purpose of `default.lean` is. But if I inferred it correctly, then I think we should make more use of it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 01 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406421):
And then using more files will not increase the length of `import` lines.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406424):
I've been deliberately avoiding the use of `default.lean` within mathlib, and I think it's good practice without as well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 01 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406464):
AFAIK, the file `data/list/default.lean` allows you to write `import data.list` instead of `import data.list.default`. So, the `default.lean` file generally `import`s everything in the directory.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 01 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406466):
exactly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406467):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406472):
and that's exactly what I don't want

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 01 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406479):
Why not?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406482):
that adds a bunch of spurious dependencies in an already delicate graph

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406493):
remember that circular dependencies are bad but there isn't an obvious linear order of files

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 01 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406494):
Sure, but there is a partial order, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jun 01 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406536):
It should be a DAG

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 01 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406537):
Do we already have a script that generates a graphviz visualisation?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406586):
[mathlib.gif](/user_uploads/3121/Xpw3mSr_YxZO2VxAF_owodVt/mathlib.gif)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 01 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406596):
Right, I had a similar graph on the level of theorems and proofs for my thesis.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 01 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406643):
But why are you scared that the graph becomes to delicate for Lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 01 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406644):
I don't quite see the problem with `default.lean`. Nonetheless, I see it as just an extra and there's no actual need to have one.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 01 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406646):
Well, we need it to keep imports manageable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 01 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406647):
Already it is common to have files with >8 imports

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 01 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406652):
If you want to split a 3000-line file into 5 files

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406653):
Currently, folders are organized by topic, and files are organized by dependency units

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406661):
so if there is no dependency issue and the topic is still the same, it all goes in one file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 01 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406705):
At least with my proposal, once you split a file into one for definitions and one for theorems, the theorems file imports the definitions file, and you just import the theorems file. The `default.lean` just allows you to leave off one part of the hierarchy.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 01 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406706):
What is a "dependency issue"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406712):
A is used by B, which is used by A'

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406718):
and A' wants to be in the same file as A

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 01 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406727):
Ok, and there is a reason (I guess the topic) that B should not be in that file as well.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406731):
I've thought many times about separating out definitions. But I'm not sure it's as easy as that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406774):
in lean, definitions and theorems are all mixed up thanks to curry howard

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 01 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406781):
As I said, there may be exceptions, but I think there are many obvious easy examples.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 01 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406790):
And I'm happy to give it a try myself.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406793):
If you are using `list` as your test bed it's not representative

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 01 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406794):
If other people think this is a good thing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406797):
programming stuff in general tends to be less dependent

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 01 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406841):
Perhaps. But there is a lot of programming stuff in mathlib. :simple_smile:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 01 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406844):
And what's the harm with doing it there?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406906):
also, how is theorem organization handled? What to do if a definition depends on a theorem?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 01 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406916):
It probably depends on the example.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406972):
What about instances? are they definitions or theorems?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 01 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406983):
To keep the proposal minimal, I don't say anything about that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 01 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127406990):
This is where concrete examples help.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407044):
`rat` is a field

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 01 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407045):
What I really want to know is whether people are, *in general*, in favor of having definitions separated from theorems. From my experience using mathlib, I believe I am. There are certainly wrinkles to be ironed out.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407050):
I am worried about losing topicality

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407061):
particularly for smaller definitions that are more auxiliary or only used in a few theorems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 01 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407063):
Isn't `rat` a `structure`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407070):
I mean a mathematical field

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407078):
That's an instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407113):
in rat.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 01 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407115):
You mean `instance field_rat : discrete_field ℚ`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407119):
yeah

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407194):
@**Jeremy Avigad** may want to chip in on this topic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 01 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407199):
It seems to me that `data/rat.lean` would also benefit from extracting the `def`s.

```
$ grep '^def' data/rat.lean | wc -l
       7
$ grep '^theorem' data/rat.lean | wc -l
      44
$ grep '^instance' data/rat.lean | wc -l
      16
```

 Whether you put instances in with theorems or not is a secondary question. Since I'm not familiar with it, I don't have the answer for you.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407246):
You can't just count them, theorems will almost always outnumber defs by a large margin

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 01 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407248):
That's kind of the point. :wink:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407255):
But there is often def -> theorem -> def -> theorem dependencies that will be messed up with such a reorganization

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 01 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407258):
Indeed! So it needs a concrete attempt.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jun 01 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407260):
and the instances and theorems are very interdependent

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407328):
By the way, one downside of the partial order structure of files is that it's not exactly a lattice, so it's not clear where to put cross cutting theorems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 01 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407335):
With my current PR on algebraic topology, I split it up in 3 files... in this example, would you have rather had 1 file? (Question is for mathlib maintainers.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407344):
like if you have incomparable files A and B and you have a theorem about AB which is used by C

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 01 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407391):
```quote
By the way, one downside of the partial order structure of files is that it's not exactly a lattice, so it's not clear where to put cross cutting theorems
```
Which is one of the reasons I left that concern out of the proposal.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 01 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407469):
(Mario, in my thesis I had one theorem/def per file -- this is all LaTeX --, and it worked quite nicely. I had some LaTeX macros that hyperlinked all references to theorems and definitions. And then with a bit of bash-fu I got PDF's for every theorem/def. I wanted an HTML realisation, but it never became nice enough...)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 01 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407481):
So... that was the other end of the spectrum (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 01 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407488):
And it was on a smaller scale, and not formalised.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 01 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407537):
Yeah, that could make sense for a thesis, but it's probably too far for a library. :wink:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407608):
By the way, metamath is organized as set.mm, a single 20MB text file with lots of ascii headers of various levels to give it a book-like structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407619):
so I guess that's the extreme opposite

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 01 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407624):
[OMG](https://github.com/metamath/set.mm/blob/master/set.mm) :bomb:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407674):
One thing that I like about that is it enforces a linear dependency structure, which makes the dependency question trivial

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407738):
the downside is that it (apparently) adds a lot of spurious dependencies, more than are truly needed by the theorems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407749):
But that's less of a problem when the entire file can be verified in less than 10 seconds

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407823):
Also metamath has a separate html view so you aren't completely reliant on text navigation, you can look at abridged views and high level views of the theorems so that you can skip over the boring stuff... Maybe something like this in lean could be helpful for you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 01 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127407889):
It's still useful to browse code, and I still think good code organization is a worthy goal.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jeremy Avigad (Jun 01 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127427222):
I think it generally makes it easier to read theory files when the definitions are an integral part of theory. The definitions are needed to understand the theorems and the theorems illustrate the intended usage of the definitions. It would be annoying to have to flip back and forth between files.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 01 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127429035):
How about just listing all the definitions in a comment at the top of the file?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 01 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127429473):
And while we're at it how about listing what goes on in the file in another comment at the top of the file?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 01 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127429501):
@**Mario Carneiro** what would you make of such PRs? Someone adding definitions and comments explaining what is going in various files in mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127429555):
Absolutely go ahead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127429564):
I do my best but I also have a lot of theorems I want to prove

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 01 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127429571):
theorems are overrated

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 02 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127442021):
@**Kevin Buzzard**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127442371):
I'm into definitions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127475414):
```quote
theorems are overrated — @**Kevin Buzzard** 
```
I just read the following blogpost of M. Harris: https://mathematicswithoutapologies.wordpress.com/2018/06/02/is-the-tone-appropriate-is-the-mathematics-at-the-right-level/
It contains the following quote of Scholze:
```quote
“What I care most about are definitions. For one thing, humans describe mathematics through language, and, as always, we need sharp words in order to articulate our ideas clearly. (For example, for a long time, I had some idea of the concept of diamonds. But only when I came up with a good name could I really start to think about it, let alone communicate it to others. Finding the name took several months (or even a year?). Then it took another two or three years to finally write down the correct definition (among many close variants). The essential difficulty in writing “Etale cohomology of diamonds” was (by far) not giving the proofs, but finding the definitions.) But even beyond mere language, we perceive mathematical nature through the lenses given by definitions, and it is critical that the definitions put the essential points into focus.

Unfortunately, it is impossible to find the right definitions by pure thought; one needs to detect the correct problems where progress will require the isolation of a new key concept.”
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127475754):
I think this is an over-mature view though; it is only in the context where theorems are commonplace that you can advocate a return to focus on definitions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127475755):
it's too easy to abuse this view to focus only on definitions at the expense of theorems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127475795):
On the other hand there are some definitions which are much more important than theorems.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127475853):
I don't argue that definitions aren't important, essential even. They are the core of the theory, the things that theorems relate

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127475888):
but to take one without the other is to see only half the picture

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127475898):
Maybe I like the fact that DTT muddles the distinction between the two.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127476060):
That's right, so we should take the most important of both :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127476065):
and there is surely ample evidence out there now in blogland and mathoverflow and whatever

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127476066):
that perfectoid spaces are a supremely important definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 04 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127534230):
```quote
I think it generally makes it easier to read theory files when the definitions are an integral part of theory. The definitions are needed to understand the theorems and the theorems illustrate the intended usage of the definitions. It would be annoying to have to flip back and forth between files.
```
@**Jeremy Avigad** Thanks for your thoughts.

I agree with you that it is useful to see definitions and theorems together, but I find that most theorems beyond the simplest `rfl` involve more than one definition. Thus, when the definitions are interleaved with large chunks of theorems, I'm either flipping back and forth or viewing different parts of the same file in a split screen. Whereas with all (or as many as is reasonable) of the definitions in one file, I can view two files side-by-side, one with definitions and one with theorems involving those definitions.

To summarize, while I think it would be nice to have a definition with a nearby associated group of theorems, I think that that is already problematic in mathlib in a very practical sense because the number of theorems generally surpasses the number of definitions and makes it difficult to find them. In addition to that, I think definition discovery is a useful part of learning a theory topic and would be aided by putting the definitions in one place.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 04 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127534547):
```quote
How about just listing all the definitions in a comment at the top of the file?
```

@**Chris Hughes**: By “definition,” are you referring to either (a) the entire declaration (i.e. `def name := term`) or (b) only the name?

(a) While I grant you that we are not engaging in (“full-blown”) software engineering when writing mathlib, this is one of those big no-no's in practice. Duplication in comments is notorious for getting out of sync with code. I would strongly recommend against doing this.

(b) Listing the names may provide a minor benefit for reference. But, since theorems generally use the unfolded definition in some form, this won't be helpful when trying to understand a theorem that uses multiple definitions, because you will end up trying to find the declarations themselves. It won't solve the problem I'm trying to solve.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 04 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127536279):
I think what you really want to do is write a doxygen extension for lean :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 04 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127536339):
not like other programming files don't have the same problem with separation of data structures / classes and methods...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 04 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127536412):
```quote
not like other programming files don't have the same problem with separation of data structures / classes and methods...
```
Certainly! My proposal is actually similar to a common pattern in Haskell package development: putting types in a file of their own.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 04 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127536545):
that's a big pain in lean though since circular dependencies are hard to handle

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 04 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127536546):
https://www.stack.nl/~dimitri/doxygen/manual/faq.html#faq_pgm_X
Seems like Lean falls in the 3rd category...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 04 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127536710):
it wouldn't be so bad if you wanted something quick and dirty - you just want to grab things in between def | definition, lemma, theorem, :, :=, and a newline

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 04 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127536771):
but I am not volunteering to do this :) however it seems more likely to happen than changing how mathlib is organized

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 04 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127536844):
it seems straightfoward - famous last words of every project I've ever estimated ever

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 04 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127540033):
I know I'm always writing the same thing, but I think we shouldn't forget that some people already developed huge libraries in a language very close to Lean, and have a look at how they handle this. For the comments at top of files see https://github.com/math-comp/math-comp/blob/master/mathcomp/algebra/vector.v (this is random file from math-comp, they all look the same)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 04 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127540045):
It also seems they keep the definitions and lemmas in the same file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 04 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127540048):
@**Assia Mahboubi** will probably tell us much more

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Assia Mahboubi (Jun 04 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127540809):
Hi @**Patrick Massot** . I read the thread briefly, so I might have missed the point of the debate. I do not see the advantage of having definitions and theorems in separated files. Sometimes, the difference between a definition and a theorem is quite thin. Also, what makes me believe that an object in the library is what I am looking for is not only its name (and not even only its definition) but also the companion lemmas, examples, etc.  So it would not ease my inspection. Last, the definition of a list in Lean is probably no going to change, but for more complex objects, definitions often evolve during the course of the development. "Testing" the subsequent impact of the changes on notations, lemmas, theorem, etc. is easier if this content is not too far I would say. However, part of the answer might be of a technological nature. Even if I am flatted that people like @**Patrick Massot** want to hear from my experience, you Lean people might benefit from tools that change the game.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jun 04 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127543190):
One more argument in favor of not separating definitions and lemmas: You can make uninteresting helper definitions `private`and still prove things about them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 04 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20file%20organization/near/127543249):
That's really only an argument for not separating *those* definitions. :wink: (But it is a fine argument in any case.)

