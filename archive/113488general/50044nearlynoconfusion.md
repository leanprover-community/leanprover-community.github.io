---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/50044nearlynoconfusion.html
---

## Stream: [general](index.html)
### Topic: [nearly no_confusion](50044nearlynoconfusion.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124130895):
I spent some time with Chris at Xena last night trying to get to the bottom of `no_confusion`.  I seem to have a slightly simpler approach which gives what looks to me like everything we need for a proof of the idea that two nats are equal iff they were constructed using the same constructors in the same order.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124130903):
```
inductive  xnat
| zero : xnat
| succ : xnat → xnat

open xnat

def  xnat_no_confusion_prop (s : xnat) (t : xnat) : Prop  :=
xnat.rec (xnat.rec true (λ _ _,false) t) (λ m _,(xnat.rec false (λ n _,(m=n)) t)) s

variables m n : xnat
#reduce xnat_no_confusion_prop zero zero -- true
#reduce xnat_no_confusion_prop (succ m) zero -- false
#reduce xnat_no_confusion_prop zero (succ n) -- false
#reduce xnat_no_confusion_prop (succ m) (succ n) -- (m = n)

def  xnat_no_confusion' (s t : xnat) (H : s = t) : xnat_no_confusion_prop s t :=
begin
rw H,
cases t with n,
exact trivial, -- t = 0
show (n=n), -- t = succ n
refl,
end

example : succ m = succ n → m = n :=  λ H, xnat_no_confusion' _ _ H
example : ¬ succ m = zero :=  λ H, xnat_no_confusion' _ _ H
 ```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124130959):
Here I prove injectivity of `xnat.succ` and also that `zero` is not a `succ` using an easier variant of the `no_confusion` / `no_confusion_type` strategy, where instead of carrying round a general sort `P` I just use the relevant props.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124130970):
Are there other applications of `no_confusion_type` lemmas which go beyond this sort of "instance of inductive type is uniquely determined by how it was constructed" sort of thing? Or am I missing something else? Why is this sort `P` used?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124131025):
I'm writing a blog post about all this `no_confusion` stuff and I was somehow expecting for this to come out in the wash but it didn't, so I need to think of something coherent to say about why the general sort P is involved before I post.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124131971):
was mcbride's paper on `no confusion` not helpful?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124132023):
I either don't know this paper, or I looked at it before and at the time it was too much for me. Having actually spent some time thinking about no_confusion_type now perhaps I can ask you for a link to this paper in the hope that I can get something from it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124132027):
https://pdfs.semanticscholar.org/d224/e96c59a81a471625faf87118b6299094e1e4.pdf section 7.3

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124132032):
http://strictlypositive.org/thesis.pdf page 136

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124132207):
mcbride's phd thesis is definitely hard going

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124132233):
i had to sit and stare at it for awhile, and i still don't fully understand it :sweat_smile:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124132336):
Well I am not an expert but it seems to me that what McBride is defining on p136ff is what is implemented in Lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124132337):
Maybe I should just post my blog post. Hang on.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 24 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124132589):
I think the reason `no_confusion` uses a general sort instead of using the consequent `m = n` directly is because the number of conclusions varies with the constructors, so that for `list` it would be something like `cons a l = cons a' l' -> a = a' /\ l = l'`, which is a bit less natural to define inductively since the 0-ary case gets special consideration, and it also relies on the definition `and` which may not be available yet. As it is defined normally `no_confusion` for an arbitrary type needs nothing except the basics of DTT, plus `eq` and `heq` (which comes up when there are dependencies, for example `sigma.mk a b = sigma.mk a' b' -> a = a' /\ b == b'` where the latter equality involves `b : B a` and `b' : B a'` which are different types.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124132771):
https://xenaproject.wordpress.com/2018/03/24/no-confusion-over-no_confusion/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124132788):
I'll perhaps add some comments about what you said above, later.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 24 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124133073):
Here's another interesting story to do with no_confusion:
```

inductive {u} mystery : Sort u
| A : mystery
| B : mystery

def confused : Type := mystery
def confused.A : confused := mystery.A
def confused.B : confused := mystery.B
open confused

theorem A_ne_B_attempt_1 : A ≠ B :=
λ h, mystery.no_confusion h --fails: no_confusion not defined

theorem A_ne_B_attempt_2 : A ≠ B :=
λ h, by cases h -- now I have to prove ⊢ false?

theorem A_ne_B_attempt_3.no_confusion_type : mystery → mystery → Type
| mystery.A mystery.A := _ -- already fails, can't case on mystery
| mystery.B mystery.A := _
| mystery.A mystery.B := _
| mystery.A mystery.B := _

#print mystery.rec
-- protected eliminator tc.mystery.rec : ∀ {C : mystery → Prop},
-- C mystery.A → C mystery.B → ∀ (n : mystery), C n
--
-- Hm, the recursor only eliminates to Prop, so we can't
-- define functions like no_confusion_type

-- Maybe we can prove they are equal instead? If it was a Prop
-- they would be equal by proof irrelevance...
theorem A_eq_B_attempt_1 : A = B := rfl --nope
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 24 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124133116):
The punch line is that `confused` is a type with two elements `A` and `B`, for which it is impossible to prove whether they are equal or not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 24 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124133271):
By the way in the blog post you could have defined `mytype_equal` like so:
```
def  mytype_equal : mytype → mytype →  Prop
| mytype.AA mytype.AA := true
| mytype.AA mytype.ZZ := false
| mytype.ZZ mytype.AA := false
| mytype.ZZ mytype.ZZ := true
```
Not sure if you were deliberately showing off other ways to construct it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 24 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124133419):
Re: the one-sided inverse, that approach actually does work in general, as a "partial projection". So for example you could define `head l : option A` when `l : list A`, to return `none` on the empty list and `a` on `a::l`. In general, you have an inductive type with several constructors, each of which has several arguments, and you can project each element of each constructor in an `option`, returning `none` if the wrong constructor is passed in and `some a` where `a` is the appropriate argument to the constructor otherwise. You can reconstruct the `cases_on` theorem using all these projections.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124133808):
Aah excellent, I will beef up the post tomorrow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124133809):
Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124155749):
PS Do you think I'm wasting my time trying to get to the bottom of things like this? I am currently thinking about getting to the bottom of something else I've always been confused by -- "using-well-founded" (the error you get when you try and define something by recursion but things are slightly too convoluted for the elaborator(?) to figure out that what you're doing will definitely terminate after a finite time). Currently the only way I know how to figure stuff out is to look at the source code and then work stuff out by experimenting. My plan, like the no-confusion post, would be to work out some simple examples, and basically write some docs and either PR them to mathlib docs or blog about them. But when Lean 4 comes is there every chance that everything I write about these sorts of "obscure" parts of Lean will be no longer relevant?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124155850):
I think I'm right in saying that using_well_founded is not mentioned in either the reference manual or TPIL (like no_confusion).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156198):
Re : `mystery` -- why is it any different to `bool`? It clearly is:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156199):
```


inductive {u} mystery : Sort u
| A : mystery
| B : mystery

#print  prefix mystery

inductive  bool'
| TT : bool'
| FF : bool'

#print  prefix bool'

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156251):
we get `bool'.no_confusion` but no `mystery.no_confusion`; and `bool.rec` eliminates to any Sort whereas `mystery.rec` only eliminates to `Prop`. Why is this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 24 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156307):
Because `mystery` can inhabit multiple types including `Prop` and when it does, it's a bit like `or`. If you could eliminate to anything other than `Prop`, you could affect the behavior of a program with just a proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 24 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156364):
for example:

```
def prog : mystery.{0} -> nat
 | A := 0
 | B := 1
```

wouldn't make sense because of proof irrelevance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156746):
I see. The whole point is that mystery is allowed to be a Prop so everything is paranoid. You guys should get classical.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156753):
it's not a waste of time. some version of well-founded recursion will be in lean 4

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156755):
what might change is the exact syntax / `using_well_founded`, so perhaps you could discuss doing it manually using `well_founded.fix`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156804):
I know even less about `well_founded.fix`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156818):
i don't know much either about the fixed points of functions, so i would avidly read your blog post :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156820):
it's a way of expressing well-founded induction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156821):
You should use Coq, everything seems to be defined using Fixpoint there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156862):
Hey, I now realise I don't even understand Lean's definition of nat.div and I am supposed to be a  professor of number theory :-/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156863):
Maybe this was mentioned in TPIL...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124156919):
Maybe it's time I read TPIL Chapter 8 again in fact.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 24 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157073):
Coq just uses the keyword `Fixpoint` to express `Definition` that can recurse, there's not much difference from Lean's `def`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 24 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157175):
The big difference is that Lean takes care of well founded recursion for you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157269):
regarding the div example in TPIL, I wish jeremy had pattern matched on y, it would have been clearer then IMO

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 24 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157270):
Except for when it doesn't and then you're stuck with quoted tactics and such :(.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 24 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157271):
Coq has a better solution to provin gtermination.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 24 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157332):
Not to mention that Coq can in some cases help you show your relation is well founded. Then you're left with proof of termination only.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157333):
Right -- this is what I see with `using_well_founded` -- I am having to actually write a tactic (or know about the "`[" trick)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157372):
I don't know whether as a mathematician I should care about this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157373):
The reason I currently care is that I have been reading software foundations

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157376):
and I defined a positive integer as an inductive type using binary notation: three constructors `one`, `double x` and `double_and_then_add_one x`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157377):
and when I tried to define addition on these things, I have trouble doing (2x+1)+(2y+1)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 24 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157440):
```quote
regarding the div example in TPIL, I wish jeremy had pattern matched on y, it would have been clearer then IMO
```
A clearer way to present that definition of division can be found:

https://github.com/leanprover/lean/blob/bb9e3ddae2396b574b8ab62976bd4db9520d525d/tests/lean/run/conv_tac1.lean#L8-L13

I believe `nat` has access to very little tactic machinery so they have to be frugal there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157564):
i think it's worth caring about using `well_founded.fix` by hand, just like `no_confusion`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157565):
it's applicable whenever you're doing complicated induction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 24 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157664):
Coq just asks for proofs of well foundedness and termination (according some decreasing measure).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157665):
Yes, as an end user I forget all about this "what is the actual state of Lean when this object is being made" stuff. For example with no_confusion I was thinking "why not just return a=a' and L=L'" for `list.no_confusion_type (a::L) (a'::L')`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 24 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157666):
Lean has this weird way of requiring tactics.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157667):
and then Mario points out that `and` might not be defined at this point. Oops.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157672):
@**Moses Schönfinkel** Is it only weird because you are used to the Coq way? i.e. are you saying "I don't like it because I know Coq and Lean is different", or "I don't like it because I know Coq and Lean is worse for this sort of thing"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 24 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157879):
It's worse because you can barely see the state of what you're proving, given it's in a tactic monad. All your feedback is nested exceptions from within the quoted tactics block.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 24 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157916):
In Coq those are first-class proofs.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 24 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124157976):
So instead of a type you need to find a term for, in Lean you're asked to provide tactics.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124158146):
yes, i agree, i always end up writing out everything using `well_founded.fix` just so it's easier to read

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124158155):
i'm glad it's not just my poor Lean programming skills, haha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124158400):
Would defining addition on that binary type I mentioned above be easier in Coq? How hard is it in Lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124158441):
(the inductive type with constructors one, double and double_then_add_one)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124158546):
i remember doing that exercise and trying to solve it by defining a coercion to nat. the trouble is you can have an infinite sequence of `doub doub doub doub doub zero` and you need to normalize the expression before you can do so

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124158589):
I decided that zero was a bad thing to have, I started at one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124158590):
then every positive integer is uniquely represented

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124158592):
and there is no confusion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124158597):
that's cheating! haha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124158659):
the same problem arises in the construction of the integers, where the pair (1,0) is the same as (2,1), but you need some way to say they are equivalent

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 24 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124158710):
I remember doing it in Coq, I am not sure if it would be at all more difficult to do in Lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Mar 24 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124159648):
I solved the problem Kevin and Andrew were talking about.
```lean
lemma  sizeof_pos : ∀ n : pint, 0  < pint.sizeof n
| one := dec_trivial
| (d m) :=  by unfold pint.sizeof; rw add_comm; exact succ_pos _
| (da m) :=  by unfold pint.sizeof; rw add_comm; exact succ_pos _

def  padd2 : pint → pint → pint
| one one := d one
| one (d m) := da m
| one (da m) := d (padd2 one m)
| (d n) one := da n
| (d n) (d m) := d (padd2 n m)
| (d n) (da m) := da (padd2 n m)
| (da n) one := d (padd2 n one)
| (da n) (d m) := da (padd2 n m)
| (da n) (da m):=  have h : 0  < pint.sizeof n, from sizeof_pos _,
d (padd2 one (padd2 n m))
```
The order of arguments in the final case matters, I think because in the default well-founded relation on `Σ' p : pint, pint` , `⟨one, padd2 n m⟩ ≺ ⟨da n, da m⟩` , but not necessarily `⟨padd2 n m, one⟩ ≺ ⟨da n, da m⟩` I'm not sure why it wanted me to prove `sizeof n` was pos however, but that was the goal that came up in the error message.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 24 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124162751):
@**Kevin Buzzard** You should look at mathlib `num` type, which is binary naturals just as you are describing. You don't need wf recursion for any of the definitions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124163808):
yeah, iirc that exercise asks you to define `nat_to_bin` and `bin_to_nat`. Once you've proven there is a bijection between the binary naturals and the"traditional" naturals, you can use nat addition on the binary numbers

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124163818):
this is hard to do if you don't have zero

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124163981):
it's harder to do if you do have zero

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124163982):
because double double double zero is zero

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124163983):
so bijectivity fails much worse

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 24 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124163994):
bijective binary to the rescue

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 24 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124163995):
ok it's literally inside the name

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164046):
yeah, handling the `doub doub doub zero` case is the real trick to the problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 24 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164057):
or you can just surject to the naturals and quotient

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164058):
i solved it a long time ago, let me see if i can find my solution, maybe...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 24 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164060):
literally a~b iff f(a)=f(b)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 24 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164107):
(deleted)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164118):
I only defined the map one way. Did it ask you for the other way later on?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164156):
so, it seems they've made many of the exercises different / a little easier in the new edition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164176):
the original problem was a 4 star advanced take you all day to complete if you're a learner hair-raiser

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164179):
at least it was for me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164237):
which is why i remember some of the details about it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 24 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164281):
They dumbed down for the kids?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164293):
not too badly! and i agree with dumbing it down, it's an introductory text

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164348):
i can't imagine teaching yourself from the original software foundations without guidance or help

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164360):
i eventually found somebody's homework solutions online and figured out how to solve it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164557):
ahh, yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164562):
http://staff.ustc.edu.cn/~bjhua/courses/theory/2012/slides/lec1notes.html

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 24 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124164617):
once you've normalized your binary number, then you can create a bijection, and life is good again

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 25 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169245):
```quote
literally a~b iff f(a)=f(b)
```
if only i had known at the time. they didn't talk much about equivalence relations in engineering school

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 25 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169303):
and if SF had started talking about how `bin_to_nat` was onto but not one-to-one, I doubt many undergraduates would know what that really meant

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 25 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169359):
That's funny. I teach that to maths undergraduates in year 1 term 1. And equivalence relations.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 25 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169369):
I remember learning that in first year of university too, in discrete math

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 25 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169410):
i never had to take discrete math, I was an electrical engineer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 25 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169411):
(I did CS and not engineering though, if that makes a difference)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 25 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169412):
instead there was a 2 semester sequence on fourier transforms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 25 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169419):
where we basically learned very little theory and a lot of how to compute various integrals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 25 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169421):
i may have mentioned this before but i have issues with how they teach math in engineering school :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 25 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169534):
It seems common that people who like math don't get enough of it in engineering school.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 25 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169556):
yes, we get a lot of boring computation instead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 25 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169584):
my linear algebra class was basically doing a lot of gauss-jordan elimination and calculating eigenvectors by hand

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 25 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169601):
which ends up being completely a waste of time since no working engineer would ever do these things without a computer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 25 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169659):
Mine was like that too. I've never missed my calculator more than in that class

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 25 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nearly%20no_confusion/near/124169720):
The follow up class was about numerical methods for linear algebra so I guess I should have been happy to do some implementation. I was not easy to satisfy I guess


{% endraw %}
