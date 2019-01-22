---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/12632onesymbolbyassumption.html
---

## [general](index.html)
### [one-symbol "by assumption"](12632onesymbolbyassumption.html)

#### [Johan Commelin (Dec 27 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152620996):
How would people feel about a 1-symbol version of `by assumption`? I now often have hypotheses with unenlightening names `H1` ... `H5`, and these labels are all over the place in my proofs. But they don't really convey any information. I could use the french quotes to tell Lean the type, and it will start looking for a fitting assumption. But often I find that pretty verbose. Because usually, it's just an annoying proof obligation that we want to get rid of. How about `!`, or maybe the unicode `…`?

#### [Patrick Massot (Dec 27 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152621153):
I can see you are tempted by the SSReflect cabalistic road...

#### [Patrick Massot (Dec 27 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152621161):
I think this is part of what SSReflect `//` does

#### [Johan Commelin (Dec 27 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152621256):
```quote
I can see you are tempted by the SSReflect cabalistic road...
```
 I know of a guild that doesn't write anything when it comes to these proof obligations... it's completely transparent to them.

#### [Patrick Massot (Dec 27 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152621713):
Great, let's have a transparent unicode character! Let's take the one we use in real world math papers.

#### [Andrew Ashworth (Dec 27 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152623829):
I am not a huge fan of this being a mathlib standard. Maybe in your personal code, you can make your own `meta def`, and then when you PR, you can search and replace?

#### [Andrew Ashworth (Dec 27 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152623896):
Or a VSCode tab-completion when you start writing `by a`

#### [Reid Barton (Dec 28 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152626746):
If `H3` is uninformative, wouldn't `!` be even more uninformative?

#### [Reid Barton (Dec 28 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152626787):
At least with `H3` the IDE will tell you the type

#### [Johan Commelin (Dec 28 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152637610):
After a bit more thought, maybe the most most user-friendly version (both for reading and writing) would be to have a VScode keyboard shortcut that looks at the type of the current `_` and replaces it with `\f< the_type \f>`. It really is a pity that we can't invoke hole commands on bare `_`. Otherwise a hole command would be perfect.

#### [Mario Carneiro (Dec 28 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152638100):
a simple available compromise is `\f<_\f>`

#### [Mario Carneiro (Dec 28 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152638105):
I would also be happy if `\f<\f>` worked but I think that requires a bit more parsing magic

#### [Reid Barton (Dec 28 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152638307):
```quote
After a bit more thought, maybe the most most user-friendly version (both for reading and writing) would be to have a VScode keyboard shortcut that looks at the type of the current `_` and replaces it with `\f< the_type \f>`. It really is a pity that we can't invoke hole commands on bare `_`. Otherwise a hole command would be perfect.
```
I would agree with this. I imagine the VSCode extension could just replace the `_` with a `{! _ !}` and then invoke the hole command--we shouldn't be limited by Lean here.

#### [Mario Carneiro (Dec 28 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152638439):
I would prefer it just replace the hole with a reference to the actual hypothesis

#### [Johan Commelin (Dec 28 2018 at 07:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152638457):
Why not the `\f< the_type \f>` version? It is less "Lean-explicit" but it is a whole lot more "math-explicit".

