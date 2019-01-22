---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/77414wlogexample.html
---

## [general](index.html)
### [wlog example](77414wlogexample.html)

#### [Simon Hudon (Apr 02 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531148):
What about: 

```
Lean: 28f4143be31b7aa3c63a907be5443ca100025ef1
mathlib: d84af03bdb8ec4e02c96b6262e7b78c8f3de412b 
```

#### [Patrick Massot (Apr 02 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531422):
Thanks

#### [Patrick Massot (Apr 02 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531475):
In the mean time I've found that March 27th nightly seems to allow compiling mathlib HEAD

#### [Patrick Massot (Apr 02 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531479):
But now `rcases` doesn't work in my code

#### [Patrick Massot (Apr 02 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531492):
I see `tactic.rcases_patt.has_reflect._rec_2: trying to evaluate sorry ` each time I  use `rcases`

#### [Patrick Massot (Apr 02 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531500):
Sorry

#### [Patrick Massot (Apr 02 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531501):
It's gone now

#### [Patrick Massot (Apr 02 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531502):
I missed one server restart

#### [Simon Hudon (Apr 02 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531517):
```quote
Sorry
```
I can't evaluate that

#### [Patrick Massot (Apr 02 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531558):
Now I need to figure out how `wlog` is meant to be used

#### [Patrick Massot (Apr 02 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531583):
My naive attempt leads to ` failed to revert '_inst_3', it is a frozen local instance (possible solution: use tactic `tactic.unfreeze_local_instances` to reset the set of local instances) `

#### [Patrick Massot (Apr 02 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531634):
context is
```lean
X : Type,
_inst_3 : topological_space X,
f g : homeo X X,
H : supp f ∩ supp g = ∅,
x : X,
h : x ∈ supp f ∪ supp g
⊢ (f ∘ g) x = (g ∘ f) x
```

#### [Patrick Massot (Apr 02 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531657):
I'm trying to use `wlog` (without knowing anything about it, only hoping from the name) to say it suffices to prove the statement when `x` is in the support of `f`

#### [Simon Hudon (Apr 02 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531658):
Is that instance used in your proof?

#### [Patrick Massot (Apr 02 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531664):
What proof?

#### [Patrick Massot (Apr 02 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531666):
I have no proof yet

#### [Patrick Massot (Apr 02 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531671):
(actually I have one but without `wlog`)

#### [Simon Hudon (Apr 02 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531719):
Right ... and does the part that `wlog` would replace make use of `_inst_3`?

#### [Patrick Massot (Apr 02 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531726):
Of course

#### [Patrick Massot (Apr 02 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531728):
everything makes use of that

#### [Patrick Massot (Apr 02 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531732):
it's the topological space structure on X

#### [Patrick Massot (Apr 02 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531739):
https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/support.lean#L133

#### [Simon Hudon (Apr 02 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531833):
It's curious because `wlog` shouldn't need to revert anything but `f`, `g`, `H` and `h`

#### [Simon Hudon (Apr 02 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531843):
Can you show me the command that you're using?

#### [Patrick Massot (Apr 02 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531924):
I'm trying to replace the proof with:
```lean
lemma fundamental' (f g : homeo X X) (H : supp f ∩ supp g = ∅) : f ∘ g = g ∘ f  :=
begin
  funext,
  by_cases h : x ∈ supp f ∪ supp g,
  { wlog  h : x ∈ supp f using x y, 
    },
  { replace h : x ∈ -(supp f ∪ supp g) := h,
    rw compl_union (supp f) (supp g) at h,
    
    have f_x : f x = x := compl_supp_subset_fix f h.1,
    have g_x : g x = x := compl_supp_subset_fix g h.2,
    
    
    exact calc (f ∘ g) x = f (g x) : rfl
        ... = f x : by rw g_x 
        ... = x : by  rw f_x
        ... = g x : by rw g_x
        ... = g (f x) : by rw f_x }
end

```

#### [Patrick Massot (Apr 02 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531932):
I only remove everything inside the first branch of the `by_cases` and `wlog` there

#### [Patrick Massot (Apr 02 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531980):
Maybe I completely misunderstood what `wlog` is meant to do

#### [Patrick Massot (Apr 02 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124532067):
I also don't manage to change the topic of messages that should be elsewhere

#### [Patrick Massot (Apr 02 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124532099):
How did you do that?

#### [Simon Hudon (Apr 02 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124532157):
I went to one of my messages preceding most of this conversation, I changed its topic and selected the option "change the topic of everything that came later"

#### [Simon Hudon (Apr 02 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124532168):
```quote
Maybe I completely misunderstood what `wlog` is meant to do
```
I think I misled you. Try `wlog h : x ∈ supp f using f g` instead.

#### [Patrick Massot (Apr 02 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124532230):
```lean
intron tactic failed, insufficient binders
state:
X : Type,
_inst_3 : topological_space X,
x : X,
f g : homeo X X,
this :
  ∀ (f g : homeo X X),
    x ∈ supp f → supp f ∩ supp g = ∅ → x ∈ supp f ∪ supp g → (f ∘ g) x = (g ∘ f) x,
h : x ∈ supp f
⊢ homeo X X
```

#### [Simon Hudon (Apr 02 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124532399):
Is that the only goal being printed?

#### [Patrick Massot (Apr 02 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124532471):
yes

#### [Simon Hudon (Apr 02 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124532600):
Ok I'm going to clone your repo and see what I can do

#### [Patrick Massot (Apr 02 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124532607):
Thanks a lot!

#### [Simon Hudon (Apr 02 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124534063):
No worries! I found a serious bug in wlog. I'll let you know when I figured out a fix. In the mean time, I hope this is not stopping you

#### [Patrick Massot (Apr 02 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124534127):
No I'm not stopped, I have a working proof (with lot of duplication, hence I thought that would be a good opportunity to learn `wlog`)

#### [Kenny Lau (Apr 19 2018 at 06:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/125287082):
how is wlog now?

#### [Kenny Lau (Apr 19 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/125287125):
I don't really think one can use wlog

#### [Kenny Lau (Apr 19 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/125287129):
I mean, it passed those simple examples in the tests

#### [Simon Hudon (Apr 20 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/125330112):
Can you show what you tried?

