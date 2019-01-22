---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/79834quotienttypewoes.html
---

## [general](index.html)
### [quotient type woes](79834quotienttypewoes.html)

#### [Kevin Buzzard (May 19 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126772251):
I find myself finally having to engage with the quotient type.

#### [Kevin Buzzard (May 19 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126772325):
I am in the middle of a definition of "add" for a quotient type and I find myself with a proof that contains a line `(sorry)`

#### [Kevin Buzzard (May 19 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126772330):
and if I replace that line with `(begin sorry end)`

#### [Kevin Buzzard (May 19 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126772333):
then suddenly the proof stops type checking.

#### [Kevin Buzzard (May 19 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126772335):
How can that happen?

#### [Kenny Lau (May 19 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126772337):
because you want `begin admit end`

#### [Kevin Buzzard (May 19 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126772360):
`sorry` works now!

#### [Kevin Buzzard (May 19 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126772392):
it's a recent change

#### [Kevin Buzzard (May 19 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126772399):
Same problem with admit

#### [Kevin Buzzard (May 19 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126772545):
https://github.com/kbuzzard/lean-stacks-project/blob/master/src/tag007N.lean

#### [Kevin Buzzard (May 19 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126772551):
In our project @**Kenny Lau**

#### [Kevin Buzzard (May 19 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126772559):
How many exams left by the way?

#### [Kenny Lau (May 19 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126772563):
3

#### [Kevin Buzzard (May 19 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126772574):
Mon Wed Fri next week?

#### [Kenny Lau (May 19 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126772580):
tue wed fri

#### [Kevin Buzzard (May 19 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126772586):
And Chris the same

#### [Kenny Lau (May 19 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126772594):
right

#### [Kevin Buzzard (May 19 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126772595):
I can't wait until Friday, I have to learn quotient types!

#### [Kenny Lau (May 19 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126772600):
well...

#### [Kevin Buzzard (May 19 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126772642):
It's about time I learnt them.

#### [Kevin Buzzard (May 19 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126772647):
After all, I am supposed to have taught them to 267 students this year

#### [Kevin Buzzard (May 19 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126774059):
If you replace `(sorry)` with `({sorry})` you get a different error :-)

#### [Kevin Buzzard (May 19 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126774063):
```
type mismatch at application
  quotient.lift ?m_4 {sorry}
term
  {sorry}
has type
  ?m_1 : Type ?
but is expected to have type
  ∀ (a b : ?m_1), a ≈ b → ?m_4 a = ?m_4 b : Prop
Additional information:
/home/buzzard/lean-projects/lean-stacks-project/src/tag007N.lean:21:21: context: 'eliminator' elaboration is not used for 'quotient.lift' because resulting type is not of the expected form

state:
X : Type u,
_inst_1 : topological_space X,
B : set (set X),
HB : topological_space.is_topological_basis B,
FPRB : presheaf_of_rings_on_basis HB,
x : X,
Hstandard : ∀ (U V : set X), U ∈ B → V ∈ B → U ∩ V ∈ B
⊢ aux (FPRB.to_presheaf_of_types_on_basis) x → stalk FPRB x → stalk FPRB x
```

#### [Kevin Buzzard (May 19 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126774081):
` 'eliminator' elaboration is not used for 'quotient.lift' because resulting type is not of the expected form`

#### [Kevin Buzzard (May 19 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126774084):
I'd never seen that one until today and now I've seen it a lot :-/

#### [Kevin Buzzard (May 19 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126774092):
It must change the order things are elaborated?

#### [Kevin Buzzard (May 19 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126774134):
There is more than one sorry in this definition

#### [Kevin Buzzard (May 19 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126774294):
(deleted)

#### [Kevin Buzzard (May 19 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126774344):
(deleted)

#### [Kevin Buzzard (May 19 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126774400):
So `by sorry` is also an error (the same error)

#### [Mario Carneiro (May 19 2018 at 03:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126777870):
I think this is a "dependent sorry" issue, similar to one that came up earlier with sorry in structure fields. If you write `quotient.lift _ sorry`, then the sorry has a metavariable type and this is not allowed (gives an error at the sorry application). Whereas if you write `quotient.lift sorry sorry` then the metavariable is replaced with `sorry` which is an actual term, so it should work. (You can still get these kinds of errors if you put too many sorries around because this can cause implicit variables that are normally solved by unification fail to be resolved because of `sorry`'s unhelpful type.)

#### [Mario Carneiro (May 19 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126778029):
And `quotient.lift (by admit) sorry` causes the same error since the tactic causes a delay in elaboration of the first sorry, so it tries to make sense of `quotient.lift _ sorry` first before getting to the tactic, and this is what causes the error.

#### [Kevin Buzzard (May 19 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126796711):
`init_quotient: initialize quotient type computational rules`

#### [Kevin Buzzard (May 19 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126796712):
Just found that with `#help commands`

#### [Kevin Buzzard (May 19 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126796713):
What does that do?

#### [Kenny Lau (May 19 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126796714):
that gives you the `quot.lift` axioms etc

#### [Kenny Lau (May 19 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126796753):
it appears in core

#### [Kevin Buzzard (May 19 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126796756):
documentation for that command is better than for coinductive:

#### [Kevin Buzzard (May 19 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126796757):
`coinductive: description`

#### [Kevin Buzzard (May 19 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126796764):
Oh I see -- so I don't really need to run `init_quotient` myself?

#### [Kenny Lau (May 19 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126796765):
no, you don't

#### [Kevin Buzzard (May 19 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126796809):
Anyway, my next quotient type woe is that if I have an object defined as a quotient type and I want to put, say, a group structure on it, then my definition of the multiplication should presumably be done in term mode and should avoid idioms such as `\lam \<U,BU,Hx,s\>`

#### [Kevin Buzzard (May 19 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126796815):
which makes the code look horrible.

#### [Kevin Buzzard (May 19 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126796857):
Is there any way around this? I tried writing a definition of a ring structure on a stalk of a sheaf of rings and the moment I started using `\lam \<U,BU,...\>` I ran into what I think are standard issues of things not being refl because they are `something._match1.something` or something

#### [Mario Carneiro (May 19 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126796963):
use projections instead of a lambda match

#### [Kevin Buzzard (May 19 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126797167):
Right, so `\lam X` and then `X.U`, `X.BU` etc.

#### [Kevin Buzzard (May 19 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20type%20woes/near/126797210):
I am a bit surprised that Lean won't do something this simple internally. Presumably what's going on is that the matching machinery is sophisticated and does not guarantee unravelling to something simple even if ultimately I am doing nothing more than a simple match on the components of a structure.

