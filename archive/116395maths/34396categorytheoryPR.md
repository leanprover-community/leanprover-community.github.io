---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/34396categorytheoryPR.html
---

## Stream: [maths](index.html)
### Topic: [category theory PR](34396categorytheoryPR.html)

---


{% raw %}
#### [ Scott Morrison (Jun 04 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/127526777):
@**Kevin Buzzard**, @**Reid Barton**, @**Johan Commelin**, the first cut of my category theory PR has just landed as https://github.com/leanprover/mathlib/pull/152. Criticisms welcome!

#### [ Johan Commelin (Jun 04 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/127531032):
Newbie comment: In line 39 of your `category.lean`, you write
```lean
attribute [ematch] category.associativity_lemma
```
But isn't this also on the previous line?

#### [ Scott Morrison (Jun 04 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/127531414):
Ooh, good catch. I didn't mean to have associativity marked as a simp, and will have to fix this. It shouldn't be a problem, but won't happen right now.

#### [ Johan Commelin (Jun 04 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/127531557):
Ok

#### [ Johan Commelin (Jun 04 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/127531564):
I submitted a review with 6 trivial comments.

#### [ Sean Leather (Jun 04 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/127533096):
@**Scott Morrison** You might want to just review your usage of variables. I saw a number of duplicates mentioned in both a `variables` declaration *and* used in a def or theorem. I mentioned one on the PR, but there are more.

#### [ Scott Morrison (Jun 04 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/127535271):
Thanks, @**Sean Leather**. I'm not sure that there were any actual errors, but I have definitely been writing code that sometimes has an explicit argument in a definition, when there is an implicit variable of the same name in scope. I'll be careful to avoid this.

#### [ Sean Leather (Jun 04 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/127535472):
No, there were no errors. It's just a comment on readability. Looks better now.

#### [ Johan Commelin (Jun 04 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/127540230):
Another point is that I think so far in mathlib there is no camel casing. I don't have a strong opinion on this, butI noticed that you use `NaturalTransformation`.

#### [ Johan Commelin (Jun 06 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/127670781):
Once this PR has been merged we can formalise pijul.org. Once code extraction is in place we will have a fully verified abstract nonsense version control system!

#### [ Ned Summers (Jul 25 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/130280546):
I'm working with this and I was wondering why `is_Isomorphism` is defined as it is. In particular, under the label I'd expect it to be a Prop? I'm new to lean in general so I'm sure it's justified, just having difficulty with any statements that involved "f is an isomorphism".

#### [ Reid Barton (Jul 25 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/130281159):
If f is an isomorphism, one wants to be able to talk about the inverse of f (compose it with other morphisms, and so on). Even though the inverse of f is uniquely determined by f, from Lean's point of view it is still additional data. If `is_Isomorphism` was a Prop, it would throw away this data and you would need to use the axiom of choice to get a hold of f's inverse, which is generally less convenient.

#### [ Reid Barton (Jul 25 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/130281667):
If you want the Prop version, you can use `nonempty (is_Isomorphism f)`.

#### [ Reid Barton (Jul 25 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/130281941):
This way you have a choice.
```lean
def blah1 ... : is_Isomorphism f := ...  -- show f is an isomorphism by exhibiting an inverse;
-- Lean now knows that the inverse is given by definition by whatever formula you gave

lemma blah2 ... : nonempty (is_Isomorphism f) := ...  -- show f is an isomorphism but don't specify the inverse;
-- Lean knows nothing about the inverse other than the equations contained in is_Isomorphism
```
Sometimes you don't care about the exact construction of the inverse, and then the second option is appropriate.

#### [ Kevin Buzzard (Jul 25 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/130293640):
If `is_Isomorphism` is not a prop, isn't the name contrary to mathlib conventions?

#### [ Patrick Massot (Jul 25 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/130293672):
I agree, but this is in a not yet revised PR.

#### [ Ned Summers (Jul 26 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/130344859):
Thanks, Reid. Makes a lot of sense; just getting used to this hesitance about choice. Thanks for the suggestion too of the Prop version.


{% endraw %}
