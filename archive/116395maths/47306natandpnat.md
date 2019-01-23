---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/47306natandpnat.html
---

## Stream: [maths](index.html)
### Topic: [nat and pnat](47306natandpnat.html)

---


{% raw %}
#### [ Kevin Buzzard (May 27 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168435):
Should I not be using these functions:

#### [ Kevin Buzzard (May 27 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168436):
```lean
definition plus_to_nat (n : ℕ+) := (n : ℕ)
definition nat_to_plus (n : ℕ) := (n : ℕ+)

-- example (n : ℕ+) : nat_to_plus (plus_to_nat n) = n := by simp -- fails
```

#### [ Kevin Buzzard (May 27 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168437):
Not only are we no longer refl, we are not even simp apparently

#### [ Kevin Buzzard (May 27 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168438):
Is that because simp won't unfold my definition by default?

#### [ Kevin Buzzard (May 27 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168444):
I am trying to make working with pnat easier. Nobody like a subtype.

#### [ Kevin Buzzard (May 27 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168445):
But I really want it to be easy to work with

#### [ Kevin Buzzard (May 27 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168492):
```lean
@[reducible] definition plus_to_nat (n : ℕ+) := (n : ℕ)
@[reducible] definition nat_to_plus (n : ℕ) := (n : ℕ+)

example (n : ℕ+) : nat_to_plus (plus_to_nat n) = n := begin
unfold nat_to_plus plus_to_nat, -- still need to do this
simp,
end
```
What am I doing wrong? Should those functions not have names and I am expected to always use coercion?

#### [ Mario Carneiro (May 27 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168493):
The functions have names

#### [ Mario Carneiro (May 27 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168494):
Have you looked at `pnat.lean`?

#### [ Kevin Buzzard (May 27 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168854):
I have

#### [ Kevin Buzzard (May 27 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168860):
Oh I see, you're saying don't make new names for old functions

#### [ Kevin Buzzard (May 27 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168862):
because the old ones will have been made better

#### [ Mario Carneiro (May 27 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168873):
By the way I'm revising pnat right now

#### [ Mario Carneiro (May 27 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168877):
to remove that funny coercion

#### [ Kevin Buzzard (May 27 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168938):
So am I supposed to refer to these functions as `coe_nat_pnat` and `coe_pnat_nat` if I ever talk about them?

#### [ Kevin Buzzard (May 27 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168954):
wait those aren't the functions

#### [ Kevin Buzzard (May 27 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168998):
`nat.to_pnat'` and `subtype.val` are the rather unsexy  names of the functions

#### [ Kevin Buzzard (May 27 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169005):
Is the idea behind coercion that I do not ever mention these names?

#### [ Mario Carneiro (May 27 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169006):
yes

#### [ Mario Carneiro (May 27 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169012):
`nat.to_pnat'` is going to be used instead of the coercion

#### [ Mario Carneiro (May 27 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169014):
but the other coercion will stay

#### [ Kevin Buzzard (May 27 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169016):
and what happens when I end up with `↑↑↑↑↑n`?

#### [ Mario Carneiro (May 27 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169024):
what are those coercions?

#### [ Kevin Buzzard (May 27 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169025):
Oh -- you're removing the instance?

#### [ Kevin Buzzard (May 27 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169029):
the coercion from nat to pnat?

#### [ Mario Carneiro (May 27 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169032):
yes

#### [ Kevin Buzzard (May 27 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169033):
Oh great

#### [ Kevin Buzzard (May 27 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169080):
you will really break Reid's code which I'm trying to maintain :-)

#### [ Kevin Buzzard (May 27 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169084):
I can't help but think that this is good though

#### [ Kevin Buzzard (May 27 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169093):
So you'll replace it with a dependent coercion which typechecks but when it actually runs it will ask the type class resolution system for a proof that n > 0?

#### [ Kevin Buzzard (May 27 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169136):
and then the coercion from pnat to nat to pnat will become refl

#### [ Kevin Buzzard (May 27 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169140):
or some other cool new system

#### [ Kevin Buzzard (May 27 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169144):
I don't know if the typeclass resolution system will be the right thing

#### [ Kevin Buzzard (May 27 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169149):
I want it to check the properties of all the pnats it can see :-)

#### [ Kevin Buzzard (May 27 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169152):
and then use known lemmas like a>0 and b>0 implies a+b>0

#### [ Kevin Buzzard (May 27 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169187):
Can it work like that? That's how it works in a mathematician's head

#### [ Mario Carneiro (May 27 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169193):
that is not at all what I'm suggesting :)

#### [ Kevin Buzzard (May 27 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169194):
thought not

#### [ Mario Carneiro (May 27 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169195):
I'm just removing the nat_pnat coercion, that's it

#### [ Kevin Buzzard (May 27 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169196):
less ambitious

#### [ Mario Carneiro (May 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169204):
there is a coercion that asks dec_trivial for the positivity proof

#### [ Kevin Buzzard (May 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169205):
What is stopping my idea above being built into Lean 7?

#### [ Mario Carneiro (May 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169206):
that's `nat.to_pnat`

#### [ Kevin Buzzard (May 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169207):
Oh yeah I saw that

#### [ Kevin Buzzard (May 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169208):
you fill in the hole with a tactic

#### [ Kevin Buzzard (May 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169209):
I see

#### [ Mario Carneiro (May 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169211):
it could ask some other tactic, like simp

#### [ Kevin Buzzard (May 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169213):
so at some point you might want to get hold of a proof

#### [ Kevin Buzzard (May 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169215):
and you have loads of options

#### [ Mario Carneiro (May 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169217):
and then it would do some kind of a+b>0 thing

#### [ Kevin Buzzard (May 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169218):
you could ask the type class dude

#### [ Kevin Buzzard (May 27 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169258):
or a tactic

#### [ Kevin Buzzard (May 27 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169264):
or you could pester the user

#### [ Kevin Buzzard (May 27 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169267):
But I'm a busy guy and I don't want to be pestered

#### [ Mario Carneiro (May 27 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169268):
But I hope that people provide a positivity proof of a+b just by adding a b : pnat

#### [ Kevin Buzzard (May 27 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169272):
Yes

#### [ Kevin Buzzard (May 27 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169274):
so in some sense my example was not good

#### [ Mario Carneiro (May 27 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169276):
as long as you stay in pnat world it's all good

#### [ Kevin Buzzard (May 27 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169277):
but how about "n^2 + 1 : pnat"

#### [ Kevin Buzzard (May 27 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169280):
if n is a nat

#### [ Kevin Buzzard (May 27 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169283):
A mathematician would be able to do that

#### [ Mario Carneiro (May 27 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169284):
that's `succ_pnat`

#### [ Kevin Buzzard (May 27 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169286):
damn you

#### [ Kevin Buzzard (May 27 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169288):
What about (n + 4 + n : pnat)

#### [ Mario Carneiro (May 27 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169326):
but I think there is space for add_pnat_left : N -> N+ -> N+

#### [ Kevin Buzzard (May 27 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169327):
A mathematician could do that

#### [ Kevin Buzzard (May 27 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169331):
what about (4 + n : pnat)

#### [ Mario Carneiro (May 27 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169333):
that would cover your example

#### [ Kevin Buzzard (May 27 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169334):
I see

#### [ Kevin Buzzard (May 27 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169335):
But can we get the coercion to do it?

#### [ Kevin Buzzard (May 27 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169337):
Why is the coercion system part of type class resolution?

#### [ Kevin Buzzard (May 27 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169339):
could it be its own system?

#### [ Mario Carneiro (May 27 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169341):
no, the old coercion did that by cheating

#### [ Mario Carneiro (May 27 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169346):
you can still use `nat.to_pnat'` if you don't want to be bothered

#### [ Kevin Buzzard (May 27 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169347):
So how do I get (4 + n : pnat) to work?

#### [ Mario Carneiro (May 27 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169349):
(4+n).to_pnat'

#### [ Kevin Buzzard (May 27 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169395):
But that's bad

#### [ Kevin Buzzard (May 27 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169398):
because the value is now not defeq to 4+n

#### [ Mario Carneiro (May 27 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169400):
Really there's no need to use `to_pnat` unless you care that the nat component is defeq to the given arg

#### [ Kevin Buzzard (May 27 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169401):
`to_pnat' is not the function I had in mind

#### [ Mario Carneiro (May 27 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169403):
the point is that it works when the input made sense

#### [ Kevin Buzzard (May 27 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169405):
The function I had in mind sends `4 + n` to a pnat whose value is 4 + n

#### [ Mario Carneiro (May 27 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169406):
it's like nat.sub

#### [ Kevin Buzzard (May 27 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169408):
We are missing a function

#### [ Kevin Buzzard (May 27 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169448):
That's what causes the problem

#### [ Kevin Buzzard (May 27 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169449):
Definitional equality is so important to you guys

#### [ Kevin Buzzard (May 27 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169451):
and I don't want to throw it away here

#### [ Mario Carneiro (May 27 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169453):
that function exists too

#### [ Mario Carneiro (May 27 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169454):
that's `nat.to_pnat`

#### [ Mario Carneiro (May 27 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169457):
that's why there's two versions

#### [ Mario Carneiro (May 27 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169463):
or just `pnat.mk`

#### [ Mario Carneiro (May 27 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169464):
i.e. the constructor

#### [ Kevin Buzzard (May 27 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169466):
`example (n : ℕ) : ℕ+ := nat.to_pnat (4 + n)`

#### [ Kevin Buzzard (May 27 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169467):
```lean
exact tactic failed, type mismatch, given expression has type
  true
but is expected to have type
  as_true (4 + n > 0)
state:
n : ℕ
⊢ as_true (4 + n > 0)
state:
n : ℕ
⊢ 4 + n > 0
```

#### [ Mario Carneiro (May 27 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169471):
but that one gives you a proof obligation

#### [ Kevin Buzzard (May 27 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169472):
But 4 + n > 0 is true by schookid

#### [ Mario Carneiro (May 27 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169510):
and you'd better prove it

#### [ Kevin Buzzard (May 27 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169513):
It's true by schoolkid

#### [ Mario Carneiro (May 27 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169514):
`nat.to_pnat (4 + n) (by schoolkid)`

#### [ Kevin Buzzard (May 27 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169516):
I really want this schoolkid tactic

#### [ Kevin Buzzard (May 27 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169517):
Mathematicians want to pass over schoolkid stuff without any comment

#### [ Kevin Buzzard (May 27 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169518):
I see

#### [ Mario Carneiro (May 27 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169524):
the scope of things you could write there is unbounded

#### [ Mario Carneiro (May 27 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169527):
At some point you have to actually prove things

#### [ Mario Carneiro (May 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169572):
If you don't care to prove that statement, you can use `(4+n).to_pnat'`

#### [ Kevin Buzzard (May 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169574):
rofl

#### [ Mario Carneiro (May 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169575):
unless it's an important definition you are going to unfold later, I doubt you will even notice the difference

#### [ Kevin Buzzard (May 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169576):
```lean
import data.pnat
#check nat.to_pnat -- chaos ensues
```

#### [ Kevin Buzzard (May 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169578):
I think #check might have dealt with that one better

#### [ Kevin Buzzard (May 27 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169586):
Is that a bug?

#### [ Kevin Buzzard (May 27 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169587):
`#check @nat.to_pnat` works fine

#### [ Kevin Buzzard (May 27 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169627):
you went for exact_dec_trivial??

#### [ Kevin Buzzard (May 27 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169628):
Not even simp?

#### [ Kevin Buzzard (May 27 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169631):
`def to_pnat (n : ℕ) (h : n > 0 . tactic.exact_dec_trivial) : ℕ+ := ⟨n, h⟩`

#### [ Mario Carneiro (May 27 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169632):
Those are incomparable tactics

#### [ Kevin Buzzard (May 27 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169634):
I think you should use sledgehammer

#### [ Kevin Buzzard (May 27 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169639):
We want this coercion to *work*!

#### [ Kevin Buzzard (May 27 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169644):
`to_pnat` : 3/10. Must try harder to coerce.

#### [ Mario Carneiro (May 27 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169645):
this is a basic function, it's not my job to select my favorite finishing tactic and introduce dependencies early in the development

#### [ Kevin Buzzard (May 27 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169689):
Dependencies?!

#### [ Kevin Buzzard (May 27 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169692):
We want it to *work*!

#### [ Kevin Buzzard (May 27 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169695):
So in fact you are suggesting that I should write "mathematicians mode"

#### [ Kevin Buzzard (May 27 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169700):
where we put the coercion back but we use by schoolkid

#### [ Mario Carneiro (May 27 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169703):
The thing about auto params is that they can't be changed later

#### [ Kevin Buzzard (May 27 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169704):
right

#### [ Kevin Buzzard (May 27 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169706):
I am seriously suggesting a "mathematicians overlay"

#### [ Kevin Buzzard (May 27 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169707):
I was thinking about this earlier when chatting to Kenny and Chris

#### [ Kevin Buzzard (May 27 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169708):
So there's a coercion from nat to pnat

#### [ Kevin Buzzard (May 27 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169709):
(although it might not last long)

#### [ Kevin Buzzard (May 27 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169748):
and so of course my first question is "what the hell are you going to do with zero"

#### [ Kevin Buzzard (May 27 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169749):
because of course you can use nat.rec to define it, and succ n goes to succ n together with the proof that succ n > 0

#### [ Kevin Buzzard (May 27 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169752):
and 0 goes to...this is just stupid

#### [ Kevin Buzzard (May 27 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169755):
So I think you should send 0 to 37

#### [ Kenny Lau (May 27 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169756):
`nat -> option pnat` problem solved

#### [ Kevin Buzzard (May 27 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169757):
I think that that's a much better instance for the coercion because I think it better represents what is happening

#### [ Kevin Buzzard (May 27 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169797):
At the places it was supposed to be defined, it does what it is supposed to do

#### [ Kevin Buzzard (May 27 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169800):
and it sends everything else to 37

#### [ Mario Carneiro (May 27 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169803):
That's a weird option for a *coercion*

#### [ Kevin Buzzard (May 27 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169807):
I don't see why it's any weirder than 1

#### [ Mario Carneiro (May 27 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169808):
It's not even making a pnat?

#### [ Andrew Ashworth (May 27 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169809):
how often do you move between nat and pnat? I feel like most people, once working with pnats, will continue to deal only in pnats

#### [ Kevin Buzzard (May 27 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169812):
Oh sorry

#### [ Kevin Buzzard (May 27 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169814):
I'll make it a pnat, sure

#### [ Andrew Ashworth (May 27 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169819):
in that case explicitly providing the proof obligation `n > 0` is not such a burden

#### [ Mario Carneiro (May 27 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169820):
Of course pnat is inhabited, so we can use iget on that...

#### [ Kevin Buzzard (May 27 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169821):
but I just want to make the point that if you're coercing then you'd better realise that if you do this on 0 then you just did something stupid

#### [ Mario Carneiro (May 27 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169822):
OF COURSE

#### [ Kevin Buzzard (May 27 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169824):
But I think that if the coercion did that

#### [ Kevin Buzzard (May 27 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169825):
then I think it would force people to write better code

#### [ Kevin Buzzard (May 27 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169828):
because they wouldn't do the lazy junk theorem thing which you do

#### [ Mario Carneiro (May 27 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169833):
coercions don't have that luxury

#### [ Kevin Buzzard (May 27 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169872):
oh really

#### [ Kenny Lau (May 27 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169873):
```
def coe (n):
  assert (n > 0)
  return [code]
```

#### [ Mario Carneiro (May 27 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169874):
They are functions A -> B, where the user gets to pick A and B

#### [ Kenny Lau (May 27 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169875):
Python style

#### [ Kenny Lau (May 27 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169878):
we should have errors in Lean

#### [ Mario Carneiro (May 27 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169882):
That's called monadic programming

#### [ Mario Carneiro (May 27 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169885):
mathematicians don't want to deal with that

#### [ Kevin Buzzard (May 27 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169889):
so I'm sending nat to pnat, where everything positive goes to the correct thing (including defeq) and 0 goes to 37

#### [ Mario Carneiro (May 27 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169891):
sure

#### [ Kevin Buzzard (May 27 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169892):
because then *none* of the junk theorems would work

#### [ Kenny Lau (May 27 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169893):
@**Kevin Buzzard** I think you want something like `nat.rec 37 id` where you replace `id` with the appropriate thing so it works `defeq`

#### [ Kevin Buzzard (May 27 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169894):
and you would be forced to carry around the proof that n > 0 properly

#### [ Mario Carneiro (May 27 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169895):
I don't think I prove any junk theorems about to_pnat'

#### [ Kevin Buzzard (May 27 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169935):
no but that's why you computer scientists tell us that functions should be total

#### [ Mario Carneiro (May 27 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169936):
but I think you are making an issue where none exists here

#### [ Kevin Buzzard (May 27 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169938):
I am suggesting that real.sqrt should send all negative reals to 37

#### [ Mario Carneiro (May 27 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169939):
There are options available, pick your favorite

#### [ Kevin Buzzard (May 27 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169940):
I think that 0 is the worst option

#### [ Kenny Lau (May 27 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169946):
```quote
because then *none* of the junk theorems would work
```
except the one which says `(0 : pnat) = 37` :P

#### [ Kevin Buzzard (May 27 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169948):
because it maximises the chance that the human prover doesn't spot their error

#### [ Mario Carneiro (May 27 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169950):
Don't worry, they will notice

#### [ Mario Carneiro (May 27 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169952):
you can't finish the proof if your model is wrong

#### [ Kevin Buzzard (May 27 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169989):
That one time you take a square root and you forget to check the argument was non-negative

#### [ Mario Carneiro (May 27 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169992):
then your theorem fails

#### [ Kevin Buzzard (May 27 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169993):
you will discover this the very next time you try and use the square root

#### [ Kevin Buzzard (May 27 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169995):
that's the point

#### [ Kevin Buzzard (May 27 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169997):
it fails earlier

#### [ Mario Carneiro (May 27 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169998):
and you come here and ask about it

#### [ Kevin Buzzard (May 27 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170001):
which is a good thing

#### [ Kevin Buzzard (May 27 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170002):
not me asking :-)

#### [ Kevin Buzzard (May 27 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170003):
the failure

#### [ Mario Carneiro (May 27 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170004):
but composition is a really nice way to write expressions, and I don't want to lose it

#### [ Kevin Buzzard (May 27 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170011):
because the error says "x isn't 37" and I look at it and think "37? What the...Oh! I didn't check it wasn't negative!"

#### [ Kenny Lau (May 27 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170012):
lol 37

#### [ Mario Carneiro (May 27 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170013):
Obviously removing the coercion solves all these problems

#### [ Kenny Lau (May 27 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170014):
as if x<0 is decidable

#### [ Kevin Buzzard (May 27 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170015):
It _has_ to be 37

#### [ Kenny Lau (May 27 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170016):
they won't ever give 37 to you

#### [ Kenny Lau (May 27 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170017):
x<0 is not decidable

#### [ Mario Carneiro (May 27 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170018):
yes it is, it's false

#### [ Kevin Buzzard (May 27 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170019):
rofl you should have seen the original version of complex.lean

#### [ Kevin Buzzard (May 27 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170048):
I had to prove it was inhabited

#### [ Kevin Buzzard (May 27 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170060):
but I changed it before I made the PR

#### [ Kevin Buzzard (May 27 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170061):
You're right, I'd never have got away with it

#### [ Mario Carneiro (May 27 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170069):
When I removed the coercion, there was one place where it appeared in mathlib

#### [ Mario Carneiro (May 27 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170119):
I had to define a positive sequence that converged to zero, and used (n:ℕ+)⁻¹

#### [ Mario Carneiro (May 27 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170127):
I think that's a good example of use, since it doesn't matter what the value is at zero, it's just a value

#### [ Johan Commelin (May 27 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127172155):
@**Kevin Buzzard** I'm a bit confused. With division by zero, or subtraction of nat's you say "just get over it, there is a footnote explaining some edge cases". Why isn't that enough here? Why don't you want to define `x / 0` as 37? (I actually prefer 57, since that is Grothendieck's prime...)

#### [ Johan Commelin (May 27 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127172198):
Or similarly `(3 : nat) - (5 : nat)`. That should also be `57`, I think...

#### [ Kenny Lau (May 28 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127180246):
https://github.com/leanprover/mathlib/blob/master/data/pnat.lean

#### [ Kenny Lau (May 28 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127180248):
@**Kevin Buzzard** congratulations, it has been removed

#### [ Kevin Buzzard (May 28 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127188139):
Maybe one day it will come back with super powers


{% endraw %}
