---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20107equalityfromscratch.html
---

## Stream: [general](index.html)
### Topic: [equality from scratch](20107equalityfromscratch.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 07 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131035424):
While looking at Kevin's [great blog post](https://xenaproject.wordpress.com/2017/10/31/building-the-non-negative-integers-from-scratch/) about unsigned integers from scratch I thought to push myself a little bit and I've tried to do them *even more* from scratch, by giving up the existing `eq` or `=`.

So let's say we have an inductive `xnat` and an inductive xnat `equality` like this:

```
inductive xnat : Type
| zero : xnat
| succ : xnat → xnat

inductive equality (a : xnat): xnat → Prop
    | refl : equality a
```

We're getting reflexivity for free from the type system, but we want to prove transitivity and symmetry. Let's assume we don't know anything about default parameters, universes, etc, but we know about recursors. We might write something like this:

```
definition equality.symm: Π (a b : xnat), Π eq1 : (equality a b), equality b a :=
    λ a b : xnat,
    λ eq1 : (equality a b),
    equality.rec_on eq1 _
```

And now, the strangest thing happens, the placeholder no longer expects a proof of `equality b a`, suddenly `equality a a` suffices. This relieves us, and we proceed, almost automatically, to write `(equality.refl a)` instead of the placeholder, and this typechecks. Phew.

But why does it typecheck? Why suddently a proof of `equality a a` is good enough as a proof of `equality b a`. Is there something special in the type-system that makes it work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 07 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131035618):
Look at the type of `equality.rec_on`.
```lean
protected def equality.rec_on : Π {a : xnat} {C : xnat → Sort l} {a_1 : xnat}, equality a a_1 → C a → C a_1
```
It says that if you want to prove a property `C` of `a_1 : xnat` given `equality a a_1`, it suffices to prove `C a`. In this case we know `equality a b`, so we need a property `C` depending on `b` such that `C a` is easy. In this case we take `\lam b, equality b a` as our `C`, so `C a` is `equality a a` which we prove by `refl`, and `C b` is `equality b a` which is what we wanted to show.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 07 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131035869):
You should be sure to look at the definition of `equality.symm` with `pp.all true`, so you can see how lean filled in the "motive" `C` in that rec_on application

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 07 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131035878):
or use `@equality.rec_on` and fill in all the fields yourself

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 07 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131036133):
Thanks Mario, this is making it less magical. I'm on your most recent suggestion.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 07 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131036339):
Kenny Lau once said to me "Lean does not do magic", and at that time I thought that lots of things Lean did (simp, type class inference) were magic. Kenny's comment spurred me on to trying to figure out how everything was working; the point is that Lean *never* does magic, and in any given case you can simply look at what it did and how it did it. Figuring out how to do that really helped me to learn Lean better.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 07 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131036344):
Ah, of course, it makes sense. `equality a b` is the same as `(equality a) b`. So our `C` becomes `equality a`. Thanks Mario!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 07 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131036376):
ah, be careful: `equality a` would be a perfect motive to prove `equality a b -> equality a b`, but this is symmetry, so there is a twist

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 07 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131036388):
So the solution is simply `@equality.rec_on a (equality a) b eq1 (equality.refl a)`, and that makes sense.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 07 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131036435):
Is `C` the motif?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 07 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131036451):
yes, that's the usual terminology

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 07 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131036476):
sometimes you get an error message talking about a motive, that's what it is referring to

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 07 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131036675):
If you use the "flipped" motive `λ b, equality b a`, you have:
```
#check λ a b eq1, @equality.rec_on a (λ b, equality b a) b eq1 (equality.refl a)
-- : ∀ (a b : xnat), equality a b → (λ (b : xnat), equality b a) b
```
and notice that the conclusion there, `(λ (b : xnat), equality b a) b`, beta reduces to `equality b a` which is the desired symmetrized equality

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 07 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131037522):
Yes you're right, I didn't notice this wasn't typechecking. This lambda abstraction is a really nice trick, I don't think I would have come up with this myself.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 07 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131037601):
Anyway, thank you Mario, I think this is now really clear.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 07 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131037619):
I'll try to work through transitivity in a similar manner

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 07 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131037620):
the really interesting thing is that lean will automatically do that lambda abstraction trick

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 07 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131037733):
Now, @**Kevin Buzzard**  if this is not magic I don't know what is.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 07 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131037744):
I'm not sure it's magic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 07 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131037799):
Is it just matching types up?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 07 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131037814):
I'm not quite following, I'm trying to get on a bus in Majorca

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 07 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131037826):
the algorithm is very simple: the goal says `equality b a`, and we just replace every `b` with `a`, then we look at what we changed and replace that with a variable, let's call it `x`. So the motive is `λ x, equality x a`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 07 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131037911):
this produces a lambda term such that replacing `x` with `b` gives us our original goal, and replacing `x` with `a` gives us our new goal which should be easier, in this case `equality a a`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 07 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131037993):
you should try using this algorithm in the proof of transitivity to work out the right motive, then see whether you got it right by letting lean do it for you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 07 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131038529):
I've actually just done it in my head. It worked:

```
inductive xnat : Type
| zero : xnat
| succ : xnat → xnat

inductive equality (a : xnat): xnat → Prop
    | refl : equality a

definition equality.trans: Π (a b c : xnat), Π eq1: (equality a b), Π eq2 : (equality b c), equality a c :=
    λ a b c : xnat,
    λ eq1 : (equality a b),
    λ eq2 : (equality b c),
    @equality.rec_on b (λ x, equality a x) c eq2 eq1
```

I'm sure I'll learn the algorithm one day, but I think I'll go and buy some beef now. Cooking sous vide steaks for friends this evening.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 07 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131038727):
Thank you Mario, this was really helpful!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 07 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131041113):
Warning: sometimes Lean can't generate the right motive. CS people start going on about higher order unification being undecidable when this sort of thing comes up. The problem is that if Lean can figure out that `C b` is supposed to be `f a b c b = 0` then it can't work out if `C x` is supposed to be `f a x c x = 0` or `f a b c x = 0` or ... etc.  So don't expect Lean to do miracles. See https://leanprover.github.io/theorem_proving_in_lean/interacting_with_lean.html#elaboration-hints

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 07 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131041181):
Remember -- Lean does not do magic. Part of the art is working out when you're asking Lean to do magic :-)


{% endraw %}
