---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/79105extensionality.html
---

## Stream: [general](index.html)
### Topic: [extensionality](79105extensionality.html)

---

#### [Kenny Lau (May 27 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127167357):
Now that we have the `ext` tactic, let's get started tagging every theorem with `@[extensionality]` :D

#### [Kevin Buzzard (May 27 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127168051):
All of them?

#### [Mario Carneiro (May 27 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127168090):
I'm not sure there are that many to add

#### [Kevin Buzzard (May 27 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127168094):
`unknown identifier 'ext'`

#### [Kenny Lau (May 27 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171210):
@**Mario Carneiro** trust me, there is a *lot* to add

#### [Mario Carneiro (May 27 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171211):
then PR them

#### [Mario Carneiro (May 27 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171213):
do you have a nonexhaustive list?

#### [Kenny Lau (May 27 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171214):
not really

#### [Kenny Lau (May 27 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171222):
do you have a estimate of the number of files in mathlib

#### [Kenny Lau (May 27 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171224):
or does @**Kevin Buzzard** have some magic to count that

#### [Mario Carneiro (May 27 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171272):
I mean, just name a few

#### [Kenny Lau (May 27 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171273):
the Z[sqrt(d)] doesn't really have the ext lemma that I want

#### [Kenny Lau (May 27 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171279):
sum, prod

#### [Kenny Lau (May 27 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171280):
I can just name every class I know

#### [Mario Carneiro (May 27 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171296):
"wrong" is a strong word

#### [Mario Carneiro (May 27 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171322):
it's not suitable for the `ext` tactic

#### [Kenny Lau (May 27 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171325):
my apologies

#### [Mario Carneiro (May 27 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171334):
Actually it would be great if `ext` could handle the iff style

#### [Mario Carneiro (May 27 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171336):
because that's the form that `simp` likes

#### [Scott Morrison (Jun 04 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127525559):
@**Simon Hudon**, what do you think of changing `ext` so that it fails if it doesn't apply at least one extensionality lemma?  (when given no identifiers)

#### [Scott Morrison (Jun 04 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127525563):
(This just follows the general principle that tactics should not "fail silently", as it's harder to manage flow control if they might.)

#### [Scott Morrison (Jun 04 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127525567):
(If it seems reasonable, I'm happy to fix it.)

#### [Simon Hudon (Jun 04 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127525612):
That makes sense. At the same time, that would differ from the behavior of `intros`

#### [Simon Hudon (Jun 04 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127525713):
Basically, you'd like to know when you expect an extensionality lemma but that it's not found. Would it make sense to have a special syntax for that? We could do `ext+` for "apply extensionality once or more" and `ext*`for "zero or more times"

#### [Scott Morrison (Jun 04 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127525714):
My vote would be to change `intros` too, but it may be too late for that!

#### [Scott Morrison (Jun 04 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127525728):
Well --- is doing something zero or more times ever actually useful? If you're working interactively, you should just remove it, and if you're working programmatically, it's no hassle to handle a failure, and sometimes helpful to know whether or not progress was made.

#### [Simon Hudon (Jun 04 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127525769):
That's a good point

#### [Simon Hudon (Jun 04 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127525778):
I'm in

#### [Scott Morrison (Jun 04 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127525827):
Shall I do it?

#### [Simon Hudon (Jun 04 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127525830):
Yes please

#### [Scott Morrison (Jun 04 2018 at 05:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127525941):
https://github.com/leanprover/mathlib/pull/151

#### [Scott Morrison (Jun 15 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128115186):
@**Simon Hudon**, there are lots of lemmas that seem to me natural to have `apply`d automatically by `ext`, e.g.:

#### [Scott Morrison (Jun 15 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128115188):
````lemma pair.ext {α : Type u₁} {β : Type u₂} {X Y : α × β} (p1 : X.1 = Y.1) (p2 : X.2 = Y.2) : X = Y````

#### [Scott Morrison (Jun 15 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128115239):
or even `lemma sigma.ext {α : Type u₁} (Z : α → Type u₂) (X Y : Σ a : α, Z a) (w1 : X.1 = Y.1) (w2 : @eq.rec_on _ X.1 _ _ w1 X.2 = Y.2) : X = Y`

#### [Scott Morrison (Jun 15 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128115251):
This isn't possible at the moment: `ext` will happily apply one of these, but then choke because there's nothing to `intro`.

#### [Scott Morrison (Jun 15 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128115254):
What do you think of generalising a little more?

#### [Mario Carneiro (Jun 15 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128115314):
I thought `ext` does 0+ intros

#### [Scott Morrison (Jun 15 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128115378):
````
import tactic.interactive

universes u₁ u₂

@[extensionality] lemma pair.ext {α : Type u₁} {β : Type u₂} {X Y : α × β} (p1 : X.1 = Y.1) (p2 : X.2 = Y.2) : X = Y := 
begin
  induction X, induction Y, dsimp at *, rw p1, rw p2,
end

lemma P (X Y : ℕ × ℕ) : X = Y :=
begin
  ext,
  
end
````

#### [Scott Morrison (Jun 15 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128115379):
The `ext` here does nothing, even though `apply pair.ext` succeeds.

#### [Simon Hudon (Jun 15 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128116141):
Mario was suggesting we extend `ext` to support that kind behavior. I think that's doable. I think we'd only have to fix the `intro1` and change `>>` for `;`

#### [Simon Hudon (Jun 15 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128116157):
As you say, the intro is mandatory right now

#### [Simon Hudon (Jun 15 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128118149):
I'll have a look

#### [Scott Morrison (Jun 15 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128120340):
Another direction to consider is the following:
````
meta def applicable_attribute : user_attribute := {
  name := `applicable,
  descr := "A lemma that should be applied to a goal whenever possible."
}

run_cmd attribute.register `applicable_attribute

/- Try to apply one of the given lemmas, it succeeds if one of them succeeds. -/
meta def any_apply : list name → tactic name
| []      := failed
| (c::cs) := (mk_const c >>= apply >> pure c) <|> any_apply cs

meta def applicable : tactic name :=
do cs ← attribute.get_instances `applicable,
   (any_apply cs) <|> fail "no @[applicable] lemmas could be applied"
````

#### [Scott Morrison (Jun 15 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128120349):
I use this pretty widely: it's for marking lemmas which are so useful that you know they are meant to be applied whenever possible.

#### [Scott Morrison (Jun 15 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128120358):
(`subsingleton.elim` is an example)

#### [Scott Morrison (Jun 15 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128120370):
I guess there's no reason this can't just coexist with `ext`, but if you see some reason to try to combine them I'd be interested.

#### [Simon Hudon (Jun 15 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128120736):
That's interesting. I think I would like to preserve `ext` because it has such a precise meaning but it might be useful to mark all extensionality lemmas as applicable. Is there a way to make one attribute subsume the other?

#### [Scott Morrison (Jun 15 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128120773):
For me it's not really important that one subsumes the other: my intention is just that the default list of tactics for `tidy` tries `applicable` first, and then tries `ext`.

#### [Scott Morrison (Jun 15 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128120833):
(I've also got a tactic `semiapplicable`, which tries applying lemmas marked `semiapplicable`, only succeeding if it can fulfill any remaining parameters by current hypotheses. That one desperately needs a better name. :-)

#### [Scott Morrison (Jun 15 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128120854):
(I've been curious if a case will come up where it's valuable to try applying a `semiapplicable`, and then using `solve_by_elim` to fulfill remaining arguments, but I haven't run into this in the wild.)

#### [Mario Carneiro (Jun 15 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128120917):
extensionality lemmas are definitely not applicable

#### [Mario Carneiro (Jun 15 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128120932):
otherwise you would end up unfolding all your equalities on structures

#### [Simon Hudon (Jun 15 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128120935):
```quote
(I've also got a tactic `semiapplicable`, which tries applying lemmas marked `semiapplicable`, only succeeding if it can fulfill any remaining parameters by current hypotheses. That one desperately needs a better name. :-)
```
Your message raises an important question: what are the grammatical rules for smileys and closing brackets?

#### [Mario Carneiro (Jun 15 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128120965):
(I prefer an additional space with the smiley to keep it clearly delimited :) )

#### [Simon Hudon (Jun 15 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128121022):
( Me too, but to avoid any ambiguity, I think I might start endorsing "turning your head" (-: )

#### [Simon Hudon (Jun 15 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128121115):
On the subject of `semiapplicable`, I think there's a pattern of tactics for killing the current goal and we ought to have a more systematic naming convention.

#### [Simon Hudon (Jun 15 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128121331):
Back to `ext`, if you call it as `ext x y z` and somewhere, product extensionality is applicable, the number of identifiers provided does not reflect the number of rules applied. If it was the last rule, there's no way to just decide to not apply that level of extensionality ... except if we call `ext x y, ext1 z`. Are we ok with that?

#### [Mario Carneiro (Jun 15 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128121398):
How about an optional depth limit like in `congr'`

#### [Simon Hudon (Jun 15 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128121505):
Yes, good idea! Do you think we could use one of `with`, `in` or `at` to specify that limit?

#### [Mario Carneiro (Jun 15 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128121759):
lol our stockpile of prepositions is quite limited

#### [Simon Hudon (Jun 15 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128121760):
How about `ext x y z` without limit and `ext 3 with x y z` if we use a limit?

#### [Simon Hudon (Jun 15 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128121829):
Otherwise we could also go with `ext x y z { depth := 3 }`

#### [Mario Carneiro (Jun 15 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128121841):
I'm not sure that will parse

#### [Simon Hudon (Jun 15 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128122303):
Yeah, I'm not sure how to make that work either actually

#### [Simon Hudon (Jun 15 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128137567):
Here's what I have now:

```lean
example (X Y : ℕ → ℕ × ℕ)  (h : ∀ i, X i = Y i) : true :=
begin
  have : X = Y,
  { ext 1 with i,
    guard_target X i = Y i,
    admit },
  have : X = Y,
  { ext i,
    guard_target (X i).fst = (Y i).fst, admit,
    guard_target (X i).snd = (Y i).snd, admit, },
  have : X = Y,
  { ext 1,
    guard_target X x = Y x,
    admit },
  trivial,
end
```

How do you guys like that?

#### [Mario Carneiro (Jun 15 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128137735):
LGTM

#### [Simon Hudon (Jun 15 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128138565):
:) Good, it's coming up

#### [Scott Morrison (Jun 16 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128145906):
@**Simon Hudon**, and if I just call `ext` with no arguments?

#### [Simon Hudon (Jun 16 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128145918):
Then may God have our souls

#### [Simon Hudon (Jun 16 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128145970):
:stuck_out_tongue_closed_eyes: But seriously, same behavior as before except it now considers extensionality on products as well

#### [Simon Hudon (Jun 16 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128145979):
Also, I fixed extensionality on functions. The attribute was applied to the tactic, not the lemma

#### [Scott Morrison (Jun 16 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128145991):
Excellent. And if I wrote something `@[extensionality] lemma ulift.ext {α : Type u₁} (X Y : ulift.{u₂} α) (w : X.down = Y.down) : X = Y` then just plain `ext` would apply this?

#### [Simon Hudon (Jun 16 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128145995):
Exactly

#### [Scott Morrison (Jun 16 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128145997):
Yay, thanks!

#### [Simon Hudon (Jun 16 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128146094):
:thumbs_up:

#### [Scott Morrison (Jun 16 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128146162):
What should I do with my PR that made `ext` fail if there were no extensionality lemmas to apply?

#### [Simon Hudon (Jun 16 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128146230):
Sorry, I completely spaced out. I should just have added on top of that

#### [Scott Morrison (Jun 16 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128146241):
No problem. I could send a PR to your PR, I guess. :-)

#### [Simon Hudon (Jun 16 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128146254):
Haha! Yeah! Let's see what actually happens with mine when there's no rules to be applied

#### [Scott Morrison (Jun 16 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128146297):
Also --- your commit is failing: <https://travis-ci.org/leanprover/mathlib/builds/392889071?utm_source=github_status&utm_medium=notification>

#### [Simon Hudon (Jun 16 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128146370):
The main branch is broken so I'm going to wait for it to be fixed first

#### [Simon Hudon (Jun 16 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128146596):
Actually, I'll just make sure the trouble is not because of `ext` ...

#### [Simon Hudon (Oct 06 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135291851):
What is people's opinion of making lemmas like this one `extensionality` lemmas?

```lean
theorem subset_ext {s₁ s₂ : finset α} : (∀ x, x ∈ s₁ → x ∈ s₂) → s₁ ⊆ s₂ := ...
```

#### [Bryan Gin-ge Chen (Oct 06 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135291905):
Is the idea that `ext` would do the work of `subset_iff` automatically?

#### [Simon Hudon (Oct 06 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292050):
Yes but only in one direction

#### [Mario Carneiro (Oct 06 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292169):
I'm not sure about this. it makes it less clear to me what `extensionality` means

#### [Mario Carneiro (Oct 06 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292176):
is there a specific sense of what kind of lemmas you want to allow here?

#### [Scott Morrison (Oct 06 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292245):
I guess the idea is "proving things by breaking objects into their constituent parts". I'm on the fence. At first I'm tempted, but I'm not sure where it ends...

#### [Mario Carneiro (Oct 06 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292316):
This also sounds like "unfold definitions" though which is a bit dangerous

#### [Simon Hudon (Oct 06 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292332):
I think Scott's definition would make sense. I'm also unsure. One reason is that I'm not clear if those lemmas could be chained

#### [Mario Carneiro (Oct 06 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292336):
Actually there is a tactic in this area I very much want, which does "definitional unfolding" minus the definitional part

#### [Scott Morrison (Oct 06 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292339):
What do you mean?

#### [Mario Carneiro (Oct 06 2018 at 03:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292342):
I currently use `simp` for this but it could be much more deterministic and hence faster

#### [Scott Morrison (Oct 06 2018 at 03:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292383):
This sounds like the sort of thing that I don't know that I want :-)

#### [Mario Carneiro (Oct 06 2018 at 03:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292385):
many functions are "activated" by some argument in which case they simplify to something else

#### [Mario Carneiro (Oct 06 2018 at 03:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292386):
i.e. recursive definitions

#### [Mario Carneiro (Oct 06 2018 at 03:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292395):
If we had a mechanism for emulating call-by-name evaluation, then we could use it as a replacement for simp in these cases

#### [Mario Carneiro (Oct 06 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292400):
`simp` is also a bit too aggressive in places, e.g. reassociating and commuting additions which can block "computation"

#### [Simon Hudon (Oct 06 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292444):
You could probably build it by using the `simp` machinery with only definitional lemmas

#### [Mario Carneiro (Oct 06 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292451):
But that's the thing, I don't care about them being literally definitional equalities

#### [Simon Hudon (Oct 06 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292453):
How would you select the lemmas?

#### [Mario Carneiro (Oct 06 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292454):
An attribute

#### [Simon Hudon (Oct 06 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292459):
So you need a new simp lemma

#### [Mario Carneiro (Oct 06 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292500):
For example a corecursor applied to a constructor in a coinductive type

#### [Mario Carneiro (Oct 06 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292502):
it's "like" a recursive definition but not definitional because lean didn't decide to support it out of the box

#### [Simon Hudon (Oct 06 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292503):
I was actually about to use that as a counter example

#### [Mario Carneiro (Oct 06 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292510):
I don't want to be tied to whatever lean decided to support out of the box

#### [Mario Carneiro (Oct 06 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292517):
it's not extensible

#### [Simon Hudon (Oct 06 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292520):
Yeah, I agree. I created a `pseudo_eqn` attribute for my corecursive definitions just for that purpose

#### [Mario Carneiro (Oct 06 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292561):
Coq has a `cbv` tactic that has exactly this behavior

#### [Mario Carneiro (Oct 06 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292565):
I asked for it a long time ago and I think `simp` was the response

#### [Simon Hudon (Oct 06 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292569):
The issue with `simp` though is that if you apply it for 

```lean
codef diverge : computation a := think diverge
```

"unfolding" will get ugly.

#### [Mario Carneiro (Oct 06 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292572):
but `cbv` has a much more restricted evaluation behavior that allows you to almost completely skip the "search" part

#### [Mario Carneiro (Oct 06 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292576):
corecursors are values

#### [Mario Carneiro (Oct 06 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292581):
they only simplify when you tell them to explicitly

#### [Mario Carneiro (Oct 06 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292584):
even Coq does this with their builtin coinductives

#### [Simon Hudon (Oct 06 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292626):
But Coq leaves in the `cofix` construct and the match statement which kind of blocks the unfolding

#### [Mario Carneiro (Oct 06 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292627):
I should look up the specifics there though

#### [Mario Carneiro (Oct 06 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292636):
not sure I follow

#### [Simon Hudon (Oct 06 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292687):
We can also do very little search though. One way is caching but we can also enforce a naming scheme that gives us only one candidate every time.

#### [Mario Carneiro (Oct 06 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292708):
I was thinking that when you register a new rule, it analyzes the structure of the lemma to figure out what the active parameter is so that it can have a decision tree based dispatch

#### [Simon Hudon (Oct 06 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292754):
```quote
not sure I follow
```

One of the first difference I noticed between Lean and Coq is that in Lean, unfolding often introduces a match statement because case analysis is a different process than unfolding. It is similar with corecursion

#### [Mario Carneiro (Oct 06 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292758):
i.e. if you say `n + 0 = n` and `n + succ m = succ (n + m)`, then it knows that it starts from `has_add.add`, checks the `nat.has_add` argument, then goes to the last parameter and uses one rule if `0` and another if `succ _`

#### [Mario Carneiro (Oct 06 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292764):
so there is no big search

#### [Simon Hudon (Oct 06 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292768):
Yes, I agree with that idea

#### [Mario Carneiro (Oct 06 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292919):
I think that many uses of `simp` are actually uses of `cbv`/`cbn`

#### [Simon Hudon (Oct 06 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292980):
I think you're right

#### [Simon Hudon (Oct 06 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135293175):
About corecursive definitions, I'm thinking of using a bound on the number of times they can be unfolded

#### [Mario Carneiro (Oct 06 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135293734):
You could also trigger them "in reverse", i.e. a destructor applied to a corecursor reduces

#### [Simon Hudon (Nov 30 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148876325):
@**Mario Carneiro**  @**Scott Morrison|110087** I noticed that `ext` has a weird behavior where with `f g : a -> b -> c |- f = g` if you call `ext i` it will apply extensionality twice instead of only once. I believe it is a mistake that I made. Is this a valuable behavior for you guys?

#### [Simon Hudon (Nov 30 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148876615):
I'm thinking of fixing it

#### [Reid Barton (Nov 30 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148878481):
What exactly are you planning on changing the behavior to?

#### [Reid Barton (Nov 30 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148878498):
My understanding is that currently, `ext` just applies as many extensionality lemmas as possible

#### [Reid Barton (Nov 30 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148878616):
Tricky cases: `ext` lemmas which don't consume any of the names, or which produce multiple goals with different numbers of variables (does `ext` support this currently?)

#### [Simon Hudon (Nov 30 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148879897):
About the tricky case: for the multiple goals scenario, it is currently broken and I'm going to fix that so that ext x y, when it produces multiple goals, will use the same list (x, y) in each goal.

#### [Simon Hudon (Nov 30 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148880086):
Currently, when `ext x` encounters an extensionality rule which does not consume names, it just keeps going until it can't anymore. For instance, with `f g : a -> (b x c) |- f = g`, `ext x` will introduce `x` and use extensionality on pairs. I'd like to change that so that `ext x` only uses functional extensionality and `ext x _` will allow the pair extensionality to be used.

#### [Reid Barton (Nov 30 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148880091):
I guess the main thing is that currently `ext x` with an ext lemma that takes 1 name followed by an ext lemma that takes 0 names applies both, and that should not change

#### [Simon Hudon (Nov 30 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148880114):
Really? Why not?

#### [Reid Barton (Nov 30 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148880135):
Because there are like 1000 uses of `ext` already

#### [Reid Barton (Nov 30 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148880150):
and you can use `ext1` to apply one lemma

#### [Simon Hudon (Nov 30 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148880156):
In mathlib or other projects too? I can fix mathlib, no worries.

#### [Reid Barton (Nov 30 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148880157):
so IMO the current behavior makes sense in that case

#### [Simon Hudon (Nov 30 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148880236):
The thing is that, when you want to use three extensionality lemmas and provide variable names for them but that a fourth is possible, you have to limit using numbers. I'd like to avoid that.

#### [Simon Hudon (Nov 30 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148881908):
Here is what I did: https://github.com/leanprover/mathlib/pull/506

#### [Reid Barton (Nov 30 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148884473):
Why not just add some new syntax for this other behavior that you want?

#### [Reid Barton (Nov 30 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148884498):
I don't see how it can be worth changing the default behavior, which is easy to understand and probably what you want most of the time

#### [Reid Barton (Nov 30 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148884615):
I didn't realize the syntax with `: n` existed. I'm not sure whether I've ever wanted it. I have used `ext1` to apply one extensionality lemma and not a second, but I don't know whether I've wanted to apply specifically 2 or more

#### [Mario Carneiro (Nov 30 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148891407):
it's an upper bound not a lower bound

#### [Reid Barton (Nov 30 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148892238):
I meant "specifically apply a number N, where N >= 2"

#### [Mario Carneiro (Nov 30 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148892283):
right, that's not what it does

#### [Mario Carneiro (Nov 30 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148892294):
it applies extensionality *up to* N times

#### [Reid Barton (Nov 30 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148892399):
Well I would only use it when I didn't want to apply more, right?

#### [Reid Barton (Nov 30 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148892405):
It might as well be an exact number

#### [Simon Hudon (Nov 30 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148893622):
@**Reid Barton** Why do you think `ext x _` is a bad syntax? Having `ext x` apply extensionality even when you run out of names for the new variables is inconsistent with what `intros` does. And instead, you could be writing `ext x; ext`

#### [Reid Barton (Nov 30 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148893667):
What is `ext x _` supposed to mean?

#### [Reid Barton (Nov 30 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148893670):
Anyways I don't think I said it was a bad syntax...?

#### [Reid Barton (Nov 30 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148893719):
Although I do possibly think it is one, depending on what it is supposed to mean...

#### [Reid Barton (Nov 30 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148893770):
What is bad is changing very basic and useful stuff unnecessarily

#### [Reid Barton (Nov 30 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148893793):
Also there's lots of stuff which takes a list of names and just makes up more if there aren't enough provided, like `cases`

#### [Reid Barton (Nov 30 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148893850):
So to me, the current behavior makes perfect sense

#### [Simon Hudon (Nov 30 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894062):
`ext x` would not use extensionality of product after functional extensionality because it runs out of names. `ext x _` would be to trigger extensionality of product by giving it a name it can throw out.

#### [Simon Hudon (Nov 30 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894153):
`ext` is more similar to `intros` than cases because, with cases, if you provide more names, it will not apply additional recursors.

#### [Reid Barton (Nov 30 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894263):
That's pretty gross IMO

#### [Reid Barton (Nov 30 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894274):
Also, your next problem will be how to apply one zero-argument extensionality lemma, when there is a second you could apply as well

#### [Reid Barton (Nov 30 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894288):
I really don't understand why you want to make any change at all frankly

#### [Simon Hudon (Nov 30 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894290):
We could make it more like `cases` (or actually `rcases`) by using syntax like `ext x ⟨ y, z ⟩` to apply extensionality (functional, then product, then functional) on `f g : a -> (b -> c x b -> c) |- f = g`

#### [Simon Hudon (Nov 30 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894363):
```quote
Also, your next problem will be how to apply one zero-argument extensionality lemma, when there is a second you could apply as well
```
 This is where I would need to resort to the `ext : n` syntax.

#### [Simon Hudon (Nov 30 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894477):
```quote
I really don't understand why you want to make any change at all frankly
```
 I think it looks ugly to have to write `ext x y z : 3` and it makes the meaning of `ext x y z` different from what you would assume. It doesn't mean apply extensionality three times. It means apply extensionality multiple times and the first three arguments should be named `x` `y` `z`

#### [Reid Barton (Nov 30 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894511):
How about making it mean "apply extensionality three times" then?

#### [Reid Barton (Nov 30 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894514):
I've never used it and I didn't read the documentation carefully

#### [Reid Barton (Nov 30 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894526):
Oh wait I misparsed

#### [Reid Barton (Nov 30 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894572):
Why would someone think `ext x y z` means extensionality three times?

#### [Reid Barton (Nov 30 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894588):
As you can probably tell, this whole conversation is very confusing to me

#### [Reid Barton (Nov 30 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894777):
An extensionality lemma for a relation would consume two names, so the number of names would never be related to the number of lemmas applied anyways

#### [Simon Hudon (Nov 30 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894794):
That's true

#### [Simon Hudon (Nov 30 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894895):
I'd like an easier way of getting `ext` to stop applying lemmas than `ext : n`

#### [Reid Barton (Nov 30 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148895366):
Okay, so how about making `ext ... : 0` or something mean "apply as few lemmas as possible to use all the names"?

#### [Reid Barton (Nov 30 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148895460):
Or it's not that difficult to just use `: n`, and changing the default behavior just means that some other, probably equally common case (apply as many lemmas as possible) now needs a special syntax instead

#### [Simon Hudon (Nov 30 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148895661):
For "as many lemmas as possible", we could go with `ext* x y z`

#### [Simon Hudon (Dec 01 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148897567):
Or we could also do `ext x y z *` or `ext x y z ... `

#### [Reid Barton (Dec 02 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/150725070):
@**Simon Hudon**  I think the current default behavior (as many lemmas as possible) is better. For one thing, `ext` is often used with no names.

#### [Kevin Buzzard (Dec 02 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/150725075):
That's true -- I often just type `ext` and it does exactly what I want it to do.

#### [Reid Barton (Dec 02 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/150725087):
(And in situations where you really don't need the names, because the whole proof is something like `by ext; simp`.)

#### [Simon Hudon (Dec 02 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/150733721):
I'm not suggesting removing that behavior of `ext`. That's one reason I compare it with `intros`. Without names, go nuts, apply `ext` (or `intro` ) to your heart's content. But with `ext a b c`, like with `intros a b c`, you only go so far as the provided identifiers allow you.

#### [Simon Hudon (Dec 02 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/150733730):
Are you guys only concerned about `ext` or do you also depend on the case where you provide a few names?

#### [Reid Barton (Dec 07 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/151129575):
```quote
Are you guys only concerned about `ext` or do you also depend on the case where you provide a few names?
```
 Honestly, I have no idea. I just use it, and it normally does what I want. I haven't been keeping score of how many times it applied a zero-argument extensionality lemma that I wanted or didn't want.

#### [Reid Barton (Dec 07 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/151129677):
This is a standard problem with *changing* behavior--it's hard to evaluate how useful the old behavior is, because you just use it implicitly, as a matter of course.

#### [Reid Barton (Dec 07 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/151129776):
In this case, it is hard to imagine any compelling argument for changing the default behavior anyways.

