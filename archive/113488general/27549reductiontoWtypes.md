---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27549reductiontoWtypes.html
---

## Stream: [general](index.html)
### Topic: [reduction to W types](27549reductiontoWtypes.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 21 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124010706):
Is there any chance of simplifying the kernel to only support a fixed set of inductive types, and have everything else compile into them? We already do such reduction for nested inductives and mutual inductives. I envision such a move happening when we write a new equation compiler and inductive compiler in lean (which will probably be late in development of lean 4 if not later). The argument about concern for changing the kernel is now greatly reduced because of the theory work I've been doing to make sure that this is consistent

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 21 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124014525):
I assume you mean that the kernel would have one type:

```
inductive W (α : Sort*) (β : α -> Sort*) 
| intro (x : α) (f : β x -> W) : W
```

How do you define `α`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 21 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124016835):
See my paper https://github.com/digama0/lean-type-theory/releases/ for details. Actually you need 8 specific inductive types: `false`, `sigma`, `sum`, `ulift`, `nonempty`, `W`, `eq` and `acc`, from these you can get all the inductive types. (I say "reduction to W" because W does most of the heavy lifting, but you need the others to put it all together.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 21 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124016903):
Is it common in computer science to have public git repository of papers under progress?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 21 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124016921):
I don't know, I did that because it started getting near book length while people kept asking questions to which I could refer to the parts of the paper that are done

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 21 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124016978):
I was originally planning to keep it under wraps until it was ready for publication, but I don't know if it will ever be published as it currently exists, it's more useful as a lean reference

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 21 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124017571):
"near book length"?! :rolling_on_the_floor_laughing:  You should see papers in my field...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 21 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124017586):
Long paper for us mean over 100 pages

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 21 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124017590):
Very long means more than 500

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 21 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124017649):
Above 1000 pages people complain

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 21 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124017668):
Then papers are split

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 21 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124017701):
How dare you call such things "papers"? How do you sleep at night?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 21 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124017703):
as in https://arxiv.org/find/grp_math/1/ti:+AND+HF+HM/0/1/0/all/0/1

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 21 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124017748):
Those are novels!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 21 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124017790):
"Once upon a time, there was a little epsilon that was barely greater than 0 ..."

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 21 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124017864):
The total for this series HF=HM is 25+133+195+240+276 = 869

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 21 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124017866):
So people don't complain

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 21 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124017882):
But some people still feel the need to learn about proof assistants (that's me)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 21 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124017936):
Are any of those papers peer reviewed? How long do you wait for your reviews?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 21 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124018303):
That particular series is not yet published

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 21 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124018305):
But it is a rather extreme case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 21 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124018330):
And actually my longest paper is only 70 pages long

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 21 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124018382):
My paper isn't close to finished yet... I mean it is projected book length

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 21 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124018485):
I see. Anyway, it's very nice to have this early release

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 21 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124025092):
Yes, people peer review 100 page papers certainly. Perhaps the process is rather different to what goes on in CS though. I basically never get sent conference proceedings to review, but I get sent papers in my area from journals and am sometimes asked to make general comments and sometimes asked to specifically look at the paper, or a part of the paper, and make detailed comments.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 21 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124025682):
Back to W types, @**Mario Carneiro** do you know what kind of impact your suggestion might have on the performances of type checking?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 21 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124025987):
Oh -- answer to "how long do you wait" is "any time between a few weeks and a year"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 21 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124025989):
(sometimes more)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 21 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124026001):
For a journal? That's faster than what I've seen.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 21 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124026047):
That's one great thing about a theorem prover: you don't have to wait weeks to realize that you messed up

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 21 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124026140):
More exactly, I had a conference paper invited for publication in a journal. I submitted in November, got criticism in June of the year after, resubmitted in July and didn't hear about it until March of the following year where I was asked to prepare the camera ready version

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 21 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124026199):
As an aside, despite being invited for a special issue on formal methods, some of my reviewers complained that my paper was too formal, that it had too many formulas ...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 21 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124026203):
A lot of computer scientists don't like math. Especially in software engineering

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 21 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124026221):
"software engineering" is too hand-wavey :-\

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 21 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124026292):
It depends on how you group the syllables: too often it is taken as soft ware-engineering (and you should put quotes around engineering, if you're being exact)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 21 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124026399):
Because of that I have refused to call my research software engineering for a long time until I realized that engineering ethics is lacking to software. Software engineering is the right phrase but it hasn't been seen often. One good way of figuring out if someone is doing actual software engineering is to ask "what do you think of getting sued if your user loses all their data?"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 21 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124026552):
Can I sue Lean if it loses all my proofs?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 21 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124026710):
I'm not sure but at the moment no. I think if you're a paying customer of Coq and that Coq that some proof is valid and that it isn't you can sue them. Or maybe it's in the process of happening

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 21 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124032584):
@**Simon Hudon** It shouldn't affect typechecking speed of stuff that doesn't depend on internal implementation of inductives. The recursor and intros become defs which are almost never unfolded, except that the computation rule may require unfolding stuff; but I think that rfl-lemmas are used here to simplify the process even now, so as long as the computational rule can be registered as a rfl-lemma it should not need to unfold the definitions. The only place where the speed could be affected is in the time it takes to compile an inductive definition, but it shouldn't be much more than is already being done to reduce nested inductives, as well as all the auxiliary functions that get defined in any case (`sizeof` and `inj_arrow` and `no_confusion` etc)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 21 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124032781):
Cool :smile: And does that mean that we no longer add axioms for each new inductive type? I like that idea a lot

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 21 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124033448):
Hey can I register my own lemmas as rfl-lemmas, or is that above my pay grade?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Mar 22 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124052279):
@**Mario Carneiro** Please don't underestimate kernel reduction time.  Any and all computation in the kernel is performed using basic ɩ-reduction, rfl-lemmas are completely irrelevant for the kernel.  That is, one unfolding of `nat.rec` now would probably correspond to two or more ɩ-reduction steps when using the reduction to `W`.  There is also the associated increase in term size which does not exactly help performance either.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 22 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124052336):
Has this been a problem with working with nested inductives?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 22 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124052385):
or wf recursion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Mar 22 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124052460):
Well we typically don't use definitional reduction for functions defined by well-founded recursion.  And yes, the nested inductives are really slow in the kernel.  It's not such a big deal because neither well-founded recursion nor generalized inductives are widely used, and then typically not for kernel reduction.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 22 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124052535):
Hm, I wonder if the kernel could make use of rfl-lemmas. That would probably solve this problem and then some, since equation compiler definitions would be usable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Mar 22 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124052644):
Theoretically, yes.  (Although you potentially get non-termination, non-confluence, and loss of subject reduction :smile: )  If I get bored, I might even try to implement inductives in trepplein using `W` with rfl-lemmas.  However, I'm doubtful that Leo will ever pursue that approach.  He didn't even use rfl-lemmas generated by the equation compiler in the type context.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 22 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124052651):
Really? I thought they were used by the elaborator ("smart unfolding")

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Mar 22 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124052710):
I believe that feature is implemented slightly differently.  IIRC we store an auxiliary definition that looks e.g. like `nat.add = λ x, λ y, nat.cases_on y ... nat.add ...` and use that for unfolding.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Mar 22 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124052716):
The `cases_on` still uses ɩ-reduction.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 22 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124052720):
Of course we don't have to worry about non-confluence and subject reduction since lean never had those to begin with :smile: but I agree that for it to behave properly you want to only use rfl-lemmas coming from structural recursive definitions, and so you would probably need an algebra of such

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 22 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124052774):
It might even be possible to have equation lemmas for wf definitions, but only for the underlying acc.rec term, where the hypothesis is exposed, to ensure termination

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 22 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reduction%20to%20W%20types/near/124052775):
(yes I'm talking about features that probably will never be in leo lean, but maybe in other typecheckers)


{% endraw %}
