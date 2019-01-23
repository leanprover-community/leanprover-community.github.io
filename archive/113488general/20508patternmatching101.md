---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20508patternmatching101.html
---

## Stream: [general](index.html)
### Topic: [pattern matching 101](20508patternmatching101.html)

---


{% raw %}
#### [ Scott Morrison (Apr 25 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125662292):
Easy question: how do I do pattern matching against values? Given `k : nat`, naively I could try writing
```
match n with
| k := something
| _ := something_else
end
```
a glorified `if n = k then something else something_else`, but of course this doesn't work, because Lean doesn't treat the `k` in the pattern as related to the earlier `k`.

Am I just meant to use `if ... then ... else`? Or can I get the pattern matcher to help me?

#### [ Kenny Lau (Apr 25 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125662332):
you need to use `if then else`. `match` only deals with constructors.

#### [ Scott Morrison (Apr 25 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125662414):
That's what I feared. How sad. So if I want to write something that given `some n` where `n = k` does `X`, and given any other `some n` or `none` does `Y`... What's the idiomatic way to write this?

#### [ Scott Morrison (Apr 25 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125662422):
(Preferably your answer shouldn't use `option.is_some` or friends, just pretend `option` is a bare inductive type with no dressing up.)

#### [ Scott Morrison (Apr 25 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125662463):
In particular, how can I do this without writing the symbol `Y` twice?

#### [ Sebastian Ullrich (Apr 25 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125662781):
Other languages have pattern guards for this, but Lean doesn't... yet. You'll have to factor `Y` out into a `let`.

#### [ Sean Leather (Apr 25 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125662792):
```quote
That's what I feared. How sad. So if I want to write something that given `some n` where `n = k` does `X`, and given any other `some n` or `none` does `Y`... What's the idiomatic way to write this?
```

This sounds like something you'd use pattern match guards for in Haskell:

```haskell
case n of
  Just k | n == k -> something
  _ -> something_else
```

#### [ Kenny Lau (Apr 25 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125662838):
```quote
In particular, how can I do this without writing the symbol `Y` twice?
```
`if o = some k then _ else Y`

#### [ Scott Morrison (Apr 25 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125662856):
okay, good, except I've over-minimised of course, and there are lots of other fields that I don't care about matching :-)

#### [ Kenny Lau (Apr 25 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125662899):
so maybe give us more context?

#### [ Simon Hudon (Apr 25 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125671684):
Is it possible that your type is like the following?

```
inductive my_type 
| constr : a -> b -> c -> d -> e -> my_type
| other : a' -> b' -> my_type
```

In Haskell, a common advice is to make that two or more types, separate the sum aspect and the product aspect.

#### [ Simon Hudon (Apr 25 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125671764):
Then, you can use selectors on to access whatever part of the product that you care about

#### [ Scott Morrison (Apr 25 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125671847):
hmm, my type 
```
inductive edit_distance_progress (l₁: list α) (l₂: list α)
| exactly : ℕ → edit_distance_progress
| at_least : ℕ → partial_edit_distance_data α → edit_distance_progress
```

#### [ Scott Morrison (Apr 25 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125671851):
and I need to check if I have an `exactly _ _ k` for some specified value of `k`.

#### [ Simon Hudon (Apr 25 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125672040):
Ok, it's not as bad as I thought. I thought because you didn't want to repeat `Y`. Is it a pattern for `partial_edit_distance_data α`?

#### [ Scott Morrison (Apr 25 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125672190):
I'm not sure what you mean. The offending code (which works, just looks gross) is <https://github.com/semorrison/lean-tidy/blob/master/src/tidy/rewrite_search.lean#L64-L84>. You can see lines 72-74 and lines 76-78 are almost identical because of this.

#### [ Sean Leather (Apr 25 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125672413):
Why can't you do something like `if update_edit_distance h.distance = exactly _ _ k then ... else ...` as Kenny suggested?

#### [ Scott Morrison (Apr 25 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125672494):
Oh... somehow I thought those `_`s would be a problem, but of course they're not. Thank you!

#### [ Scott Morrison (Apr 25 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125672566):
I will need an extra decidable instance for this. I remember there is some trick for synthesising decidable instances for boring inductive types....? Anyone remember?

#### [ Sean Leather (Apr 25 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125672589):
```lean
@[derive decidable_eq]
inductive ...
```

#### [ Scott Morrison (Apr 25 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125672652):
Lovely! And where do I find out what derive is doing? :-)

#### [ Sean Leather (Apr 25 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125672714):
I'm sure there's a `#print` that'll tell you, but I never remember which one. :blush:

#### [ Sean Leather (Apr 25 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125672780):
Perhaps `#print <type-name>.decidable_eq`?


{% endraw %}
