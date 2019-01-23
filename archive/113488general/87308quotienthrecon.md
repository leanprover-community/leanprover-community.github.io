---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/87308quotienthrecon.html
---

## Stream: [general](index.html)
### Topic: [quotient.hrec_on₂](87308quotienthrecon.html)

---

#### [Sean Leather (Aug 06 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130971695):
I've got a [definition](https://github.com/spl/lean-finmap/blob/fb3f562de05059f136f855b88bf616c8aac7f365/src/data/multiset/dict.lean#L162-L172):

```lean
def kunion : m₁.nodup_keys → m₂.nodup_keys → multiset (sigma β) :=
@quotient.hrec_on₂ _ _ _ _
  (λ (m₁ m₂ : multiset (sigma β)), m₁.nodup_keys → m₂.nodup_keys → multiset (sigma β))
  m₁ m₂
  (λ l₁ l₂ (d₁ : l₁.nodup_keys) (d₂ : l₂.nodup_keys), l₁.kunion l₂) $
    λ l₁ l₂ l₃ l₄ p₁₃ p₂₄,
    hfunext (by rw perm_nodup_keys p₁₃) $
      λ (d₁ : l₁.nodup_keys) (d₃ : l₃.nodup_keys) _,
      hfunext (by rw perm_nodup_keys p₂₄) $
        λ (d₂ : l₂.nodup_keys) (d₄ : l₄.nodup_keys) _,
        heq_of_eq $ quotient.sound $ perm_kunion d₂ d₄ p₁₃ p₂₄

local infixr ` k∪ `:67 := kunion
```

and I want to prove the left and right units:

```lean
@[simp] theorem zero_kunion {m : multiset (sigma β)} : ∀ (d : m.nodup_keys), nodup_keys_zero k∪ d = m
@[simp] theorem kunion_zero {m : multiset (sigma β)} : ∀ (d : m.nodup_keys), d k∪ nodup_keys_zero = m
```

I'm stuck on how to proceed. If I use `quotient.induction_on m`, I just unfold until I get down to `quot.rec_on ↑(hd :: tl)` or `quot.rec_on ↑nil`, but I don't know how to go further. (At one point, I believe I even made the simplifier loop infinitely.)

Any suggestions on how to prove these?

#### [Mario Carneiro (Aug 06 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130971867):
Wow, that's a weird notation

#### [Mario Carneiro (Aug 06 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130971872):
does it have to be a partial function?

#### [Sean Leather (Aug 06 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130971983):
```quote
does it have to be a partial function?
```
I don't follow you.

#### [Mario Carneiro (Aug 06 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972034):
you could make it return empty when the inputs don't have `nodup_keys`

#### [Mario Carneiro (Aug 06 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972054):
or it could be a `roption` if you are worried about the performance cost of checking `nodup_keys`

#### [Sean Leather (Aug 06 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972218):
Sorry, Mario, your  use of “it” in multiple places is a bit too vague for me. Are you suggesting I use a different definition for `kunion`? If so, what is the type signature you're referring to?

#### [Sean Leather (Aug 06 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972526):
Btw, I'm not asking for a completed solution. You're welcome to give me only hints or suggestions. :smile:

#### [Reid Barton (Aug 06 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972544):
I think `def kunion : multiset (sigma β) → multiset (sigma β) → roption (multiset (sigma β))` and then prove that `kunion` is defined exactly when each `multiset` is `nodup_keys`

#### [Sean Leather (Aug 06 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972612):
Reid: Hmm, okay, thanks.

#### [Sean Leather (Aug 06 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972673):
And what's the advantage to this approach? Is it simplicity of the definition and related theorems or performance or both?

#### [Reid Barton (Aug 06 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972677):
Then you can avoid all this dependent eliminator stuff... although it's not clear to me whether your problem is related to this

#### [Sean Leather (Aug 06 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972701):
Okay, well, I'll give it a shot.

#### [Chris Hughes (Aug 06 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972702):
Just proving at ` quotient.hrec_on_beta` lemma might help.

#### [Reid Barton (Aug 06 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972707):
Yes. Is that `↑` just `quotient.mk`?

#### [Sean Leather (Aug 06 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972756):
Yes, I think so.

#### [Sean Leather (Aug 06 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972765):
Chris: I wondered the same thing. I'm not sure how to start with that.

#### [Reid Barton (Aug 06 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972790):
Well, `quotient.rec_on` applied to `quotient.mk` should reduce...

#### [Chris Hughes (Aug 06 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972792):
Or use `show`

#### [Sean Leather (Aug 06 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972893):
I suppose it would look something like:

```lean
lemma quot.ind_beta (p : ∀ a, β (quot.mk r a)) (a : α) : (ind p (quot.mk r a) : β (quot.mk r a)) = p a
```

#### [Mario Carneiro (Aug 06 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130974037):
that is trivially true, since both sides are propositions

#### [Mario Carneiro (Aug 06 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130974063):
The advantage of using `roption` is avoiding all the `hrec` mess. I've had to define partial functions over quotients before, and I wish I'd thought of this then

#### [Sean Leather (Aug 06 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130974158):
```quote
that is trivially true, since both sides are propositions
```
Are you referring to `quot.ind_beta`, which is in the core library, or something else?

```quote
The advantage of using `roption` is avoiding all the `hrec` mess. I've had to define partial functions over quotients before, and I wish I'd thought of this then
```

Great! I'm working on it now.

#### [Reid Barton (Aug 06 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130974410):
I think someone probably copied `lift_beta` to `ind_beta` without realizing it was rather unnecessary.

#### [Sean Leather (Aug 06 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130974532):
Ah! I see what you're saying now. I didn't look that closely at `ind_beta`.

#### [Sean Leather (Aug 06 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130974767):
This is definitely a much nicer definition:

```lean
def kunion' (m₁ m₂ : multiset (sigma β)) : roption (multiset (sigma β)) :=
quotient.lift_on₂ m₁ m₂ (λ l₁ l₂, roption.mk (l₁.nodup_keys ∧ l₂.nodup_keys) (λ _, (l₁.kunion l₂ : multiset (sigma β)))) $
  λ l₁ l₂ l₃ l₄ p₁₃ p₂₄, roption.ext'
    (and_congr (perm_nodup_keys p₁₃) (perm_nodup_keys p₂₄))
    (λ ⟨d₁, d₂⟩ ⟨d₃, d₄⟩, quotient.sound $ perm_kunion d₂ d₄ p₁₃ p₂₄)
```

#### [Mario Carneiro (Aug 06 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130974979):
so now the theorem you want is either `m k∪ 0 = some m` or `m ∈ m k∪ 0` (they are equivalent)

#### [Sean Leather (Aug 06 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130975110):
Right.

#### [Mario Carneiro (Aug 06 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130975212):
and the coercion lemma you want says `l₁.nodup_keys → l₂.nodup_keys → ↑l₁ k∪ ↑l₂ = some (l₁.kunion l₂)`

#### [Sean Leather (Aug 06 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130975700):
Got that, thanks. How should I coerce the 0 (`multiset.zero`) for `kunion' 0 ↑l`?

#### [Sean Leather (Aug 06 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130975782):
If I do `simp [has_zero.zero, multiset.zero]`, lean never ends.

#### [Mario Carneiro (Aug 06 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130975852):
you can just force it to unfold by applying `kunion_coe.trans _`

#### [Mario Carneiro (Aug 06 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130975886):
or you can rewrite with `coe_nil_eq_zero`

#### [Sean Leather (Aug 06 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130980496):
The aforementioned theorems:

```lean
@[simp] theorem zero_kunion : ∀ (d : m.nodup_keys), kunion' 0 m = roption.some m :=
quotient.induction_on m $ λ _ d, (kunion_coe nodup_keys_zero d).trans rfl

@[simp] theorem kunion_zero : ∀ (d : m.nodup_keys), kunion' m 0 = roption.some m :=
quotient.induction_on m $ λ _ d, (kunion_coe d nodup_keys_zero).trans (by simp)
```

#### [Sean Leather (Aug 06 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130981382):
One last related question: Now that I have an `roption`-wrapped `multiset`, how should I specify theorems that involve the result of `kunion'`? For example, I had:

```lean
@[simp] theorem mem_kunion {s : sigma β} : ∀ (d₁ : m₁.nodup_keys) (d₂ : m₂.nodup_keys),
  disjoint m₁.keys m₂.keys → (s ∈ d₁ k∪ d₂ ↔ s ∈ m₁ ∨ s ∈ m₂) :=
quotient.induction_on₂ m₁ m₂ $ λ _ _ _ _, mem_kunion_iff
```

Should this become...?

```lean
@[simp] theorem mem_kunion' {s : sigma β} : ∀ (d₁ : m₁.nodup_keys) (d₂ : m₂.nodup_keys),
  disjoint m₁.keys m₂.keys → ∃ m ∈ kunion' m₁ m₂, s ∈ m ↔ s ∈ m₁ ∨ s ∈ m₂ :=
quotient.induction_on₂ m₁ m₂ $ λ l₁ l₂ d₁ d₂ dk,
  ⟨_, roption.eq_some_iff.mp (kunion_coe d₁ d₂), mem_kunion_iff dk⟩
```

Specifically, I mean: should I use a pattern like `∃ m ∈ kunion' m₁ m₂, ...` for theorems like this, or is there a better way?

#### [Mario Carneiro (Aug 06 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130982225):
I would take `m ∈ kunion' m₁ m₂` as a hypothesis and prove `s ∈ m ↔ s ∈ m₁ ∨ s ∈ m₂`

#### [Mario Carneiro (Aug 06 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130982297):
of course this hypothesis eliminates the need for d1 and d2

#### [Mario Carneiro (Aug 06 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130982374):
alternatively, you can define `kunion` as `(kunion' m1 m2).get <d1, d2>` and have all your old theorems back

#### [Sean Leather (Aug 06 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130991221):
True. I'm not sure which is a better definition to work with. If I were using the `multiset` interface directly, I would lean towards defining `kunion` as `(kunion' m1 m2).get <d1, d2>`. But since it's really meant to be the underlying implementation of `finmap`, perhaps it's not necessary.

#### [Sean Leather (Aug 06 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130991299):
Also, do you think I should use `roption` + `quotient.lift_on` consistently instead of `quotient.hrec_on`? I don't have any more uses of `quotient.hrec_on₂`, but I do have a number of uses of `quotient.hrec_on`.

#### [Sean Leather (Aug 07 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131028609):
@**Mario Carneiro** I'd like to get your thoughts on this :point_up:. I haven't had any problems with `quotient.hrec_on` up to now, but maybe things would just be nicer all around if I used `roption` more. I'm not sure.

#### [Mario Carneiro (Aug 07 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131028618):
I think if it works once, it will probably work again

#### [Mario Carneiro (Aug 07 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131028672):
Also, another option I forgot to mention was to make `kunion` a nondependent function, using the fact that `nodup_keys` is decidable

#### [Sean Leather (Aug 07 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131028674):
Just to be clear about what you mean, do you think I should change the defs [here](https://github.com/spl/lean-finmap/blob/fb3f562de05059f136f855b88bf616c8aac7f365/src/data/multiset/dict.lean) to use `roption`?

#### [Sean Leather (Aug 07 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131028693):
(Just search for `hrec_on`.)

#### [Mario Carneiro (Aug 07 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131028697):
Even if we suppose that checking this is expensive, it doesn't matter if you are just using it as an abstract version so you can prove equations about it

#### [Sean Leather (Aug 07 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131028702):
```quote
Also, another option I forgot to mention was to make `kunion` a nondependent function, using the fact that `nodup_keys` is decidable
```
What do you mean by this?

#### [Mario Carneiro (Aug 07 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131028797):
define `kunion m1 m2 = if h : m1.nodup_keys /\ m2.nodup_keys then (kunion' m1 m2).get h else 0`

#### [Sean Leather (Aug 07 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131028858):
That's an interesting suggestion.

#### [Mario Carneiro (Aug 07 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131028874):
in fact, even if `nodup_keys` wasn't decidable you could make this definition anyway noncomputably and just not use it for evaluation

#### [Sean Leather (Aug 07 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029010):
Hmm, yes, I think I like this definition of `kunion`. I don't have to pass around the `m1.nodup_keys` everywhere.

#### [Sean Leather (Aug 07 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029031):
Okay, well, I'll play around with it.

#### [Mario Carneiro (Aug 07 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029032):
Yet more alternatively, you could define the subtype. Didn't you have `finmap` at one point for this?

#### [Sean Leather (Aug 07 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029090):
I decided to go with the `structure` for the same reasons `finset` is a `structure`:

```lean
structure finmap (α : Type u) (β : α → Type v) : Type (max u v) :=
(val : multiset (sigma β))
(nodup_keys : val.nodup_keys)
```

#### [Sean Leather (Aug 07 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029097):
Mainly, for type class instance resolution.

#### [Mario Carneiro (Aug 07 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029099):
that's fine, my point was that you can define `finmap.rec_on` to encapsulate this definition pattern

#### [Mario Carneiro (Aug 07 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029112):
and this way you never have to carry around any proofs since they are embedded in the type

#### [Sean Leather (Aug 07 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029158):
You mean the `if h : m.nodup_keys ... then ... else ...` pattern?

#### [Mario Carneiro (Aug 07 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029160):
no, the `roption` or `hrec_on` version

#### [Mario Carneiro (Aug 07 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029167):
(it doesn't really matter too much which one you use, since it only has to be done once)

#### [Sean Leather (Aug 07 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029228):
Oh.... I'm awfully dumb today. So, define a `finmap.rec_on` that takes an `roption (multiset (sigma β))` to a `finmap`?

#### [Sean Leather (Aug 07 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029236):
Err, actually the arrow goes the other way...

#### [Sean Leather (Aug 07 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029244):
Anyway, it'd be a higher-order function.

#### [Sean Leather (Aug 07 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029247):
Yeah, I think I see it.

#### [Mario Carneiro (Aug 07 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029289):
`finmap.rec_on` takes a `finmap A B`, a function `list (sigma B) -> C`, and a proof that this function is equal up to permutation when the arguments have `nodup_keys`

#### [Sean Leather (Aug 07 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029296):
Right.

#### [Sean Leather (Aug 07 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029372):
So, given that, I would be skipping defining all of the defs and theorems for `multiset` and define them for only `list` and `finmap`?

#### [Mario Carneiro (Aug 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029445):
right

#### [Mario Carneiro (Aug 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029450):
You can reconstruct the multiset definitions from the finmap ones by the `if ... else 0` trick

#### [Mario Carneiro (Aug 07 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029516):
I think multisets are a good stepping stone if you can actually define functions on them, but in your case the functions already have to assume nodup just to be well defined, so they've already jumped to finmap

#### [Sean Leather (Aug 07 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029523):
That's true.

#### [Sean Leather (Aug 07 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029576):
Okay, I'm convinced.

#### [Mario Carneiro (Aug 07 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029713):
I notice you have theorems like ` s.1 ∈ (m.map_snd f).keys ↔ s.1 ∈ m.keys` with several variations. Why isn't this just `(m.map_snd f).keys = m.keys`?

#### [Sean Leather (Aug 07 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029750):
Because I use the `mem` one in the non-`mem`.

#### [Sean Leather (Aug 07 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029791):
I suppose I don't have to.

#### [Mario Carneiro (Aug 07 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029808):
the proof is just `map_comp`

#### [Mario Carneiro (Aug 07 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029819):
you shouldn't use `mem` to try to characterize a multiset, it gets messy

#### [Sean Leather (Aug 07 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029874):
The other problem with the `map_snd`/`keys` theorems is that I wanted to use it in `finmap`, but the best I could come up with was using `[inhabited (∀ a, β₁ a)]`. I'm not happy with that solution.

#### [Sean Leather (Aug 07 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029887):
```quote
the proof is just `map_comp`
```
The proof of which?

#### [Mario Carneiro (Aug 07 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029966):
I'm really confused about your confusion. It should be provable that `(m.map_snd f).keys = m.keys`, this makes the last 7 theorems or so unnecessary and it doesn't require any weird assumptions

#### [Sean Leather (Aug 07 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131030141):
Okay, I think I see what you're saying. I'll give it a shot.

#### [Mario Carneiro (Aug 07 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131030157):
wait, just the last 4. The ones about `(m.map f).keys` are a bit awkward because `f : sigma B1 -> sigma B2` can mingle keys and values in an unpredictable way. How about defining `m.map f g` where `f : A1 -> A2` and `g : ∀ a, B1 a -> B2 (f a)`; then you should be able to prove `(m.map f g).keys = m.keys.map f` and life is good

#### [Sean Leather (Aug 07 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131030231):
Btw, did you mean `map_map` instead of `map_comp`?

#### [Mario Carneiro (Aug 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131030275):
yes

#### [Mario Carneiro (Aug 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131030288):
it's written backwards for simp lemmas because `comp` is dumb

#### [Mario Carneiro (Aug 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131030292):
so the name becomes `map_map` instead of `map_comp`

#### [Sean Leather (Aug 08 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131093639):
I could only figure out how to do a general 2-arg `finmap` recursor using `quotient.hrec_on₂`:

```lean
protected def lrec_on₂ {γ : Sort*} (f g : finmap α β)
  (φ : ∀ {l₁ l₂ : list (sigma β)}, l₁.nodup_keys → l₂.nodup_keys → γ)
  (c : ∀ {l₁ l₂ l₃ l₄} (p₁₃ : l₁ ~ l₃) (p₂₄ : l₂ ~ l₄) d₁ d₂ d₃ d₄, φ d₁ d₂ = φ d₃ d₄) : γ :=
@quotient.hrec_on₂ _ _ _ _
  (λ (m₁ m₂ : multiset (sigma β)), m₁.nodup_keys → m₂.nodup_keys → γ)
  f.val g.val
  (λ l₁ l₂ (d₁ : l₁.nodup_keys) (d₂ : l₂.nodup_keys), φ d₁ d₂)
  (λ l₁ l₂ l₃ l₄ p₁₃ p₂₄, hfunext (by rw list.perm_nodup_keys p₁₃) $
    λ d₁ d₃ _, hfunext (by rw list.perm_nodup_keys p₂₄) $
      λ d₂ d₄ _, heq_of_eq $ c p₁₃ p₂₄ d₁ d₂ d₃ d₄)
  f.nodup_keys g.nodup_keys
```

I have a general 2-arg `finmap.lift_on₂`:

```lean
protected def lift_on₂ {γ : Type*}
  (f g : finmap α β)
  (φ : ∀ {l₁ l₂ : list (sigma β)}, l₁.nodup_keys → l₂.nodup_keys → γ)
  (c : ∀ {l₁ l₂ l₃ l₄} (p₁₃ : l₁ ~ l₃) (p₂₄ : l₂ ~ l₄) d₁ d₂ d₃ d₄, φ d₁ d₂ = φ d₃ d₄) :
  roption γ :=
quotient.lift_on₂ f.val g.val
  (λ l₁ l₂, roption.mk (l₁.nodup_keys ∧ l₂.nodup_keys) (λ ⟨d₁, d₂⟩, φ d₁ d₂))
  (λ l₁ l₂ l₃ l₄ p₁₃ p₂₄, roption.ext'
    (and_congr (list.perm_nodup_keys p₁₃) (list.perm_nodup_keys p₂₄))
    (λ ⟨d₁, d₂⟩ ⟨d₃, d₄⟩, c p₁₃ p₂₄ d₁ d₂ d₃ d₄))
```

But it seems like the `roption.dom` has a pair of lists, so this only seems useful in combination with `quotient.induction_on₂`. Is that right? Or can I do better?

#### [Mario Carneiro (Aug 08 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131094611):
What does the one arg version look like?

#### [Sean Leather (Aug 08 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131094622):
```lean
protected def lrec_on {γ : Sort*} (f : finmap α β)
  (φ : ∀ {l : list (sigma β)}, l.nodup_keys → γ)
  (c : ∀ {l₁ l₂} (p : l₁ ~ l₂) d₁ d₂, φ d₁ = φ d₂) : γ :=
@quotient.hrec_on _ _ (λ (m : multiset (sigma β)), m.nodup_keys → γ)
  f.val
  (λ l (d : l.nodup_keys), φ d)
  (λ l₁ l₂ p, hfunext (by rw list.perm_nodup_keys p) $ λ d₁ d₂ _, heq_of_eq $ c p d₁ d₂)
  f.nodup_keys
```

#### [Sean Leather (Aug 08 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131094845):
There are theorems where `quotient.induction_on₂` needs more than just `l₁.nodup_keys` and `l₂.nodup_keys`:

```lean
@[simp] theorem mem_kunion' {s : sigma β} : ∀ (d₁ : m₁.nodup_keys) (d₂ : m₂.nodup_keys),
  disjoint m₁.keys m₂.keys → ∃ m ∈ kunion' m₁ m₂, s ∈ m ↔ s ∈ m₁ ∨ s ∈ m₂ :=
quotient.induction_on₂ m₁ m₂ $ λ l₁ l₂ d₁ d₂ dk,
  ⟨_, roption.eq_some_iff.mp (kunion_coe d₁ d₂), mem_kunion_iff dk⟩
```

So, I think the above `finmap.lift_on₂` definition makes sense.

#### [Mario Carneiro (Aug 08 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131098994):
I would suggest you state `lrec_on` like this:
```
protected def lrec_on {γ : Sort*} (f : finmap α β)
  (φ : list (sigma β) → γ)
  (c : ∀ {l₁ l₂} (p : l₁ ~ l₂), l₁.nodup_keys → l₂.nodup_keys → φ l₁ = φ l₂) : γ :=
```
Recall that we are trying to avoid partial functions. The function `φ` is defined on lists, so there presumably won't be any trouble making arbitrary choices that depend on the order

#### [Mario Carneiro (Aug 08 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131099010):
Given this it should not be hard to just iterate it twice to get `lrec_on₂`

#### [Sean Leather (Aug 08 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131103716):
Okay, so I have the following.

My initial version:
```lean
protected def lrec_on {γ : Sort*} (f : finmap α β)
  (φ : ∀ {l : list (sigma β)}, l.nodup_keys → γ)
  (c : ∀ {l₁ l₂} (p : l₁ ~ l₂) d₁ d₂, φ d₁ = φ d₂) : γ :=
@quotient.hrec_on _ _ (λ (m : multiset (sigma β)), m.nodup_keys → γ)
  f.val
  (λ l (d : l.nodup_keys), φ d)
  (λ l₁ l₂ p, hfunext (by rw list.perm_nodup_keys p) $ λ d₁ d₂ _, heq_of_eq $ c p d₁ d₂)
  f.nodup_keys

def erase (f : finmap α β) (a : α) : finmap α β :=
finmap.lrec_on f
  (λ l d, ⟨l.kerase a, list.nodup_keys_kerase a d⟩)
  (λ l₁ l₂ p d₁ d₂, eq_of_veq $ quotient.sound $ list.perm_kerase a d₁ d₂ p)
```

Your suggestion:
```lean
protected def lrec_on' {γ : Sort*} (f : finmap α β)
  (φ : list (sigma β) → γ)
  (c : ∀ {l₁ l₂} (p : l₁ ~ l₂), l₁.nodup_keys → l₂.nodup_keys → φ l₁ = φ l₂) : γ :=
@quotient.hrec_on _ _ (λ (m : multiset (sigma β)), m.nodup_keys → γ)
  f.val
  (λ l _, φ l)
  (λ l₁ l₂ p, hfunext (by simp [list.perm_nodup_keys p]) $ λ d₁ d₂ _, heq_of_eq $ c p d₁ d₂)
  f.nodup_keys

def erase' (f : finmap α β) (a : α) : finmap α β :=
finmap.lrec_on' f
  (λ l, ⟨l.kerase a, list.nodup_keys_kerase a _⟩)
  (λ l₁ l₂ p d₁ d₂, eq_of_veq $ quotient.sound $ list.perm_kerase a d₁ d₂ p)
```

I can define `erase` with `lrec_on`, but how do I define `erase'` with `lrec_on'`?

```lean
error: don't know how to synthesize placeholder
context:
α : Type u,
_inst_1 : decidable_eq α,
β : α → Type v,
f : finmap α β,
a : α,
l : list (sigma β)
⊢ list.nodup_keys l
```

