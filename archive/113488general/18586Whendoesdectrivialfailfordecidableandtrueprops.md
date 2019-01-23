---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/18586Whendoesdectrivialfailfordecidableandtrueprops.html
---

## Stream: [general](index.html)
### Topic: [When does dec_trivial fail for decidable and true props?](18586Whendoesdectrivialfailfordecidableandtrueprops.html)

---


{% raw %}
#### [ Seul Baek (Nov 11 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/When%20does%20dec_trivial%20fail%20for%20decidable%20and%20true%20props%3F/near/147484281):
I'm encountering cases where I have a decidable prop `p` that is also true (which I know because the decidability proof term `t : decidable p` evaluates to `is_true ...` when checked with the vm) but `exact dec_trivial` fails to discharge the goal, with the message 
```
exact tactic failed, type mismatch, given expression has type
  true
but is expected to have type
  as_true (p)
```
Are there specific conditions under which this happens? I'm guessing that some definitions in the decidability proof term is not unfolding, but I'm not sure why. 

This is really strange because it used to work for the exact cases that's broken now. This started happening after I reinstalled mathlib. I wonder if that has anything to do with it.

#### [ Seul Baek (Nov 11 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/When%20does%20dec_trivial%20fail%20for%20decidable%20and%20true%20props%3F/near/147487874):
More precisely : are there specific kinds of of definitions that might occur in a `t : decidable p`  that might prevent `as_true p` from evaluating to `true`?  I'm trying `exact dec_trivial` with various other decidable props, and it seems to have no problem reducing `as_true p` to `true`for most choices of `p`, so I'm wondering what's causing the difference.

#### [ Bryan Gin-ge Chen (Nov 11 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/When%20does%20dec_trivial%20fail%20for%20decidable%20and%20true%20props%3F/near/147489969):
Can you give a minimum (non)working example that illustrates the problem?

#### [ Seul Baek (Nov 11 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/When%20does%20dec_trivial%20fail%20for%20decidable%20and%20true%20props%3F/near/147490427):
https://github.com/skbaek/qe/blob/master/src/tests.lean

In the first example 
```
example : ∃ (x : int), (x = x) := 
begin
  lia.reify, lia.trim, lia.qelim, 
  exact dec_trivial, exact dec_trivial,
end
```
the second use of `exact dec_trivial` fails now, although it used to work. 
I'm trying to find a more minimal example that does not require a whole library to reproduce, but I'm having trouble isolating the exact point where it fails

#### [ Seul Baek (Nov 11 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/When%20does%20dec_trivial%20fail%20for%20decidable%20and%20true%20props%3F/near/147490781):
I think it would be easier to pinpoint the problem if I can see how far lean evaluates `as_true p` before failing to match it with `true`.  Are there options for displaying this?

#### [ Mario Carneiro (Nov 11 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/When%20does%20dec_trivial%20fail%20for%20decidable%20and%20true%20props%3F/near/147491600):
what are the goals there?

#### [ Mario Carneiro (Nov 11 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/When%20does%20dec_trivial%20fail%20for%20decidable%20and%20true%20props%3F/near/147491631):
Proofs are irreducible, meaning that definitions by well founded recursion will fail to reduce when using `dec_trivial` or `rfl`

#### [ Seul Baek (Nov 11 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/When%20does%20dec_trivial%20fail%20for%20decidable%20and%20true%20props%3F/near/147492318):
I didn't use `well_founded` in any of the definitions, if that's what you mean

#### [ Seul Baek (Nov 13 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/When%20does%20dec_trivial%20fail%20for%20decidable%20and%20true%20props%3F/near/147561312):
Oh I see what you mean. There was a non-structural recursion hiding in one of the defs

#### [ Seul Baek (Nov 13 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/When%20does%20dec_trivial%20fail%20for%20decidable%20and%20true%20props%3F/near/147561483):
Hunting these down isn't exactly fun though... a lot of time poring over the text output. Is there some option that displays all defs in a file/folder that use well-founded recursion?


{% endraw %}
