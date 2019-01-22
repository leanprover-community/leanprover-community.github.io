---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/67902structureequalityfromparts.html
---

## [general](index.html)
### [structure equality from parts](67902structureequalityfromparts.html)

#### [Nicholas Scheel (Mar 21 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033267):
Hi, I'm totally new here, I've spent about a day with Lean so far.

Currently I'm struggling to define a notion of equality for this structure (permutations aka bijective functions, which I represent with a function and its inverse, and the proof that they are inverses):
```
structure Perm (α : Type) :=
permute ::
  (forward : α → α) (backward : α → α)
  (are_inv : function.left_inverse forward backward ∧ function.right_inverse forward backward)
```

It appears that Lean understands `refl` enough to let me do the following:
```
def Perm.eq {α : Type}
  : Π (p1 p2 : Perm α),
    p1.forward = p2.forward →
    p1.backward = p2.backward →
    p1 = p1
| p1 p2 .(rfl) .(rfl) := rfl
```
but what I _really_ want is a proof that `p1 = p2` at the end, but if I give it that type it complains that `rfl : p1 = p1` not `p1 = p2` (even though it looks like the compiler has enough information to determine `p1 = p2` and has already unified them? idk)

I've looked in the standard library for similar examples but couldn't find any.

Would appreciate some pointers or help!

(my overall goal is to prove the group structure of permutations, which I think needs to be done through the components?)

#### [Simon Hudon (Mar 21 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033339):
You might want to build on top of `equiv` from `mathlib`.

#### [Nicholas Scheel (Mar 21 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033356):
in particular, if I try
```
.......
    p1 = p2
| p1 p2 .(rfl) .(rfl) := _
```
I get the following message:
```
don't know how to synthesize placeholder  
context:  
α : Type,  
Perm.eq : ∀ (p1 p2 : Perm α), p1.forward = p2.forward → p1.backward = p2.backward → p1 = p2,  
p1 : Perm α  
⊢ p1 = p1
```
Notice that only p1 is in scope and it wants a proof of `p1 = p1`, which is just `rfl`, but `rfl` won't actually unify in that environment when I try it.

#### [Simon Hudon (Mar 21 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033360):
For your specific problem, try this instead:

```
| ⟨f₀,b₀,p₀⟩ ⟨f₁,b₁,p₁⟩ .(rfl) .(rfl) := rfl
```

#### [Simon Hudon (Mar 21 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033415):
Sorry, I made a mistake:

#### [Simon Hudon (Mar 21 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033422):
```
| ⟨f₀,b₀,p₀⟩ ⟨._,._,._⟩ .(rfl) .(rfl) := rfl
```

I think that should work

#### [Simon Hudon (Mar 21 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033496):
The reason is that, to infer equality of the whole from equality of the parts, you need to pattern match on the whole. Then, the unification of the variables used for the components will translate into the patterns for the two wholes to be syntactically equal and this is where `rfl` works

#### [Nicholas Scheel (Mar 21 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033515):
hmm I'm still getting a cryptic error with both of those:
```
......
has type  
∀ (forward_1 backward_1 : α → α)  
(are_inv_1 : function.left_inverse forward_1 backward_1 ∧ function.right_inverse forward_1 backward_1),  
{forward := forward, backward := backward, are_inv := are_inv}.forward =  
{forward := forward_1, backward := backward_1, are_inv := are_inv_1}.forward →  
{forward := forward, backward := backward, are_inv := are_inv}.backward =  
{forward := forward_1, backward := backward_1, are_inv := are_inv_1}.backward →  
{forward := forward, backward := backward, are_inv := are_inv} =  
{forward := forward, backward := backward, are_inv := are_inv}  
but is expected to have type  
∀ (forward_1 backward_1 : α → α)  
(are_inv_1 : function.left_inverse forward_1 backward_1 ∧ function.right_inverse forward_1 backward_1),  
(λ (p2 : Perm α),  
{forward := forward, backward := backward, are_inv := are_inv}.forward = p2.forward →  
{forward := forward, backward := backward, are_inv := are_inv}.backward = p2.backward →  
{forward := forward, backward := backward, are_inv := are_inv} = p2)  
{forward := forward_1, backward := backward_1, are_inv := are_inv_1}  
```
(I'm using https://leanprover.github.io/live/3.3.0/ btw)

#### [Simon Hudon (Mar 21 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033713):
I see. The problem is the `.` before `rfl`. I think the idea is that they are not irrelevant (or inferred from the context). They actually help you establish that `p1` and `p2` are identical:

```
def Perm.eq {α : Type}
  : Π (p1 p2 : Perm α),
    p1.forward = p2.forward →
    p1.backward = p2.backward →
    p1 = p2
| ⟨a,b,p⟩ ⟨._,._,._⟩ (rfl) (rfl) := rfl
```

#### [Nicholas Scheel (Mar 21 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033784):
aha! that seems to be working, thanks so much!

#### [Kevin Buzzard (Mar 21 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033799):
https://github.com/leanprover/mathlib/blob/master/data/equiv.lean

#### [Kevin Buzzard (Mar 21 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033802):
There are some spoilers for this sort of thing

#### [Kevin Buzzard (Mar 21 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033809):
Your `Perm` is the `equiv` on line 54

#### [Kevin Buzzard (Mar 21 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033932):
no, sorry, equiv can have different source and target. Your `Perm` is the `perm` on line 62

#### [Nicholas Scheel (Mar 21 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033944):
very cool, thanks for the link :) is that accessible in the online editor or no?

#### [Chris Hughes (Mar 21 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033993):
I think not

#### [Simon Hudon (Mar 21 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034017):
I think it is. The online version imports `mathlib` and I don't think `equiv` is too new

#### [Kevin Buzzard (Mar 21 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034029):
```
import data.equiv

#print equiv.perm
 ```

#### [Kevin Buzzard (Mar 21 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034067):
works in lean web editor

#### [Simon Hudon (Mar 21 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034069):
I just checked, it's there

#### [Simon Hudon (Mar 21 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034099):
@**Kevin Buzzard** I'm confused by your reaction to your own post. Which direction are you two pointing to?

#### [Kevin Buzzard (Mar 21 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034103):
I was trying to point to your comment :-)

#### [Kevin Buzzard (Mar 21 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034151):
Lean 3.4 should be with us soon, and perhaps they'll update the lean web editor so it runs 3.4. There was extensive discussion on gitter about getting everything to compile but in the end all the problems were solved IIRC.

#### [Kevin Buzzard (Mar 21 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034165):
https://gitter.im/leanprover_public/lean_js

#### [Kevin Buzzard (Mar 21 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034171):
probably-hard-to-find but useful link if you want to set it up yourself.

#### [Kevin Buzzard (Mar 21 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034230):
but if you're going to compile it I suppose you'd just be better off running it in an IDE :-) I think Scott compiled a more recent version of Lean and left it on an internet-facing server...

#### [Simon Hudon (Mar 21 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034314):
Was it hard to compile because of the new monadic code?

#### [Mario Carneiro (Mar 21 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034362):
No, that discussion predates the monad stuff by a while. I think it was just some JS compilation arcana

#### [Simon Hudon (Mar 21 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034397):
Oh fun!

#### [Nicholas Scheel (Mar 21 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034431):
I have a PureScript background – JS is weird :D

#### [Kevin Buzzard (Mar 21 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034435):
Yes, apparently taking a bunch of C++ code and compiling it into javascript isn't 100% straightforward

#### [Nicholas Scheel (Mar 21 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034481):
I have to say, the online editor is really slick I'm impressed!

#### [Simon Hudon (Mar 21 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034629):
So they actually translate the whole C++ code base to Java script and the whole thing runs in the browser? That's really cool :) I just assumed the code was sent to a server and sent back after verification.

#### [Simon Hudon (Mar 21 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034649):
```quote
I have to say, the online editor is really slick I'm impressed!
```
Microsoft has a few like that. It's a cool idea to get you started before you decide to install it

#### [Kevin Buzzard (Mar 21 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034799):
The moment you try and do something non-trivial in the lean web editor things slow to a crawl; the "recompile the entire file every time the user presses a key" gets old pretty quickly. But for small bits of experimentation I absolutely agree, it's very cute.

#### [Nicholas Scheel (Mar 21 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034866):
yeah, and a little debouncing would go a long ways ... but I'm patient with it ;)

#### [Simon Hudon (Mar 21 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034912):
It might just be a tease: the real thing is actually pretty fast and getting faster.

#### [Simon Hudon (Mar 21 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034928):
I think @**Sebastian Ullrich** should merge an incremental caching strategy pretty soon which will make things even smoother

#### [Kevin Buzzard (Mar 21 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034932):
The next step after Lean Web Editor is to try a nightly. Except that the current nightly might not work with mathlib. Is this now a problem that the community has solved?

#### [Kevin Buzzard (Mar 21 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034935):
What is this #travis stream anyway?

#### [Simon Hudon (Mar 22 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034989):
```quote
What is this #travis stream anyway?
```
Whenever someone commits to `mathlib`, we get the build report there.

#### [Kevin Buzzard (Mar 22 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035007):
Oh, so we still don't have access to e.g. a nightly build before all the monad refactoring stuff went in?

#### [Kevin Buzzard (Mar 22 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035012):
I mean core lean

#### [Kevin Buzzard (Mar 22 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035067):
There was an entire week from 13th to 20th March with no commits and Lean was working just fine for me. And now we have all this monad refactoring and everyone is assuming mathlib won't build any more

#### [Simon Hudon (Mar 22 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035134):
I think older nightlies should still be available. Don't you get a long list of nightlies on the site?

#### [Simon Hudon (Mar 22 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035181):
I think what we might need is for `mathlib` to publish Lean nightlies, a subset of all the nightlies for which `mathlib` passes.

#### [Kevin Buzzard (Mar 22 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035197):
I can pull the repo and checkout a random commit and compile, but I don't think I've ever seen a list of nightlies. Where are they?

#### [Simon Hudon (Mar 22 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035342):
I can't find it anymore. I wonder if they changed the way nightly works

#### [Nicholas Scheel (Mar 22 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035352):
here's my messy code as a whole if anyone is curious :wink: https://gist.github.com/MonoidMusician/b2792a2d9687dd627155996097ad97c1 (we talked about equivalence classes of functions with permutations in my combinatorics class, so I wanted to play around with the idea a little bit – in particular, equivalent surjective functions will have a unique (post-composed) permutation for the equivalence)
thanks again for the help!

#### [Sebastian Ullrich (Mar 22 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035501):
The nightly releases PR was merged today, though today's build has already failed because of broken setup... I'll test it tomorrow by having it build a custom pre-monad nightly

#### [Simon Hudon (Mar 22 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035521):
Are more than one nightly supposed to be available at any given time?

#### [Kevin Buzzard (Mar 22 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035526):
I've never seen more than one available

#### [Kevin Buzzard (Mar 22 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035530):
(per OS of course)

#### [Simon Hudon (Mar 22 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035585):
I should go offline: my dissertation doesn't write itself when I don't look at it :/  (no matter how long I look away)

#### [Mario Carneiro (Mar 22 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035589):
I think your definition of `PostPermEquiv` should use `subtype` (notation `{x // p x}`)

#### [Nicholas Scheel (Mar 22 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036061):
okay, looks good – what's the difference? :)

#### [Nicholas Scheel (Mar 22 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036145):
ah, more specific to Prop?

#### [Mario Carneiro (Mar 22 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036301):
You also shouldn't need the `n+2` case in the definition of `swap` and `swap_involution`

#### [Mario Carneiro (Mar 22 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036316):
Also, as Kevin says most of this theory is in `data.equiv` in mathlib, although we don't do anything with postperm stuff

#### [Nicholas Scheel (Mar 22 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036318):
hmm I get
```
non-exhaustive match, the following cases are missing:
swap ⟨nat.succ (nat.succ _), _⟩
```

#### [Kevin Buzzard (Mar 22 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036500):
`| ⟨n+2, prf⟩ := ⟨n+2,prf⟩` works :-)

#### [Mario Carneiro (Mar 22 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036563):
Ah, I see, it would work except that the underlying inductive type `nat.less_than_or_equal` eliminates to Prop, so it can't be used to define an element of `fin 2` (although it can be used to define an element of `false` which then defines an element of `fin 2`)

#### [Mario Carneiro (Mar 22 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036621):
You can also use `absurd prf dec_trivial` instead of that finis stuff

#### [Nicholas Scheel (Mar 22 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036635):
haha that's really helpful :laughing:

#### [Nicholas Scheel (Mar 22 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036703):
I will learn these voodoo tactics one day!

#### [Kevin Buzzard (Mar 22 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036704):
If you define `swap (n+2)` to be `n+2` then you get to write

```
lemma  swap_involution : ∀ n, swap (swap n) = n
| ⟨0, _⟩ := rfl
| ⟨1, _⟩ := rfl
| ⟨n+2, prf⟩ := rfl
```

#### [Nicholas Scheel (Mar 22 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036766):
true, and that's essentially what the more general swapping does too

#### [Nicholas Scheel (Mar 22 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036972):
thanks for all the help!!

