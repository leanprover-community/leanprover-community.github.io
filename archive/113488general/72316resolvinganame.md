---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72316resolvinganame.html
---

## Stream: [general](index.html)
### Topic: [resolving a name](72316resolvinganame.html)

---


{% raw %}
#### [ Keeley Hoek (Sep 11 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133714444):
Say I've got `n : name`, which I get passed, but would like to be of type `my_type`.  I know I can use `t <- infer_type n` to get the type of the identifier pointed to by `n`, and then can use an if to guard against the type being wrong. But I'd really like to do more and "cast" `n` to type `my_type`, getting some `inst : my_type` from `n`.  Would anyone be able to point me to a nice/any facility for doing this? (I've grepped for `cast` without success, is `mk_app` what I'm looking for?)

#### [ Mario Carneiro (Sep 11 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133714683):
I don't quite understand the setup here. How does `my_type` relate to `n`?

#### [ Keeley Hoek (Sep 11 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133714858):
Sorry: secretly in some file a user wrote `def foo : my_type := blah`, and then in tactic mode later on they called my code ``cast_fn `(foo) ``. So here ``n = `foo``, and I'd like `cast_fn` to be of type `name -> tactic my_type`.

#### [ Keeley Hoek (Sep 11 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133714912):
Maybe my attempt at an MWE confused the issue. I'm getting a `name` in an attribute handler, and I expect what was annotated to be of a particular type. I'd like to get the actual thing that was annotated and call a function on it.

#### [ Mario Carneiro (Sep 11 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133714916):
`eval_expr` is what you want

#### [ Keeley Hoek (Sep 11 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133714953):
Right. So to invoke it, I only get to pass a single `expr`, so I figure I need to convert the name of the function I want to call into an `expr` and then create a `expr` which says "evaluate the function at the first `expr`". How can I build such an `expr`?

#### [ Keeley Hoek (Sep 11 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133715275):
Ah. I think ``eval_expr my_type (expr.app `(my_fn) n)`` does the job!

#### [ Keeley Hoek (Sep 11 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133715292):
Ok, so the point of `mk_app` is that I don't need to know the type beforehand? Right.

#### [ Mario Carneiro (Sep 11 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133715294):
`mk_const` will turn a name into an `expr`

#### [ Kevin Buzzard (Sep 11 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133715409):
This whole area is just screaming out for a small pdf or web page containing 10 very basic examples followed by 10 very basic questions.

#### [ Patrick Massot (Sep 11 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133715483):
What happened to @**Edward Ayers**? He started to write such documentation and then vanished? Is there a meta-documentation curse?

#### [ Keeley Hoek (Sep 11 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133722360):
What does the `local` in `local attribute ...` mean?

#### [ Kenny Lau (Sep 11 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133722435):
https://en.wikipedia.org/wiki/Scope_(computer_science)

#### [ Kevin Buzzard (Sep 11 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133722660):
I *think* it means "it's an attribute for this `.lean` file only" in this case, but I'm certainly not an expert.

#### [ Johan Commelin (Sep 11 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133723327):
Well, even "this `section` only"

#### [ Keeley Hoek (Sep 11 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133730395):
Haha thanks Kenny, I've written a fair few curly-braces in my time!

In that case does anyone know if the `before_unset` member of `user_attribute` is ever actually called when a `local` attribute is removed for the reason that a section has ended? It seems that it is not, which I find very strange.

#### [ Keeley Hoek (Sep 11 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133730604):
It seems that the none of mathlib and only one file in the lean library itself uses the feature, and this is in `library/init/meta/smt/ematch.lean` where `before_unset` is defined to do nothing anyway.

#### [ Keeley Hoek (Sep 11 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133730914):
It seems that `tactic.unset_attribute` does perform the unsetting... Perhaps this is a bug in lean?

#### [ Sebastian Ullrich (Sep 11 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133746407):
@**Keeley Hoek** "Unsetting" an attribute means using `attribute [-simp] ...`, not just leaving the scope of a local attribute declaration

#### [ Keeley Hoek (Sep 11 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133746476):
fair enough!

#### [ Edward Ayers (Sep 17 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/134089643):
Hi I've been on hols.

#### [ Patrick Massot (Sep 17 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/134089683):
Welcome back!

#### [ Kevin Buzzard (Sep 17 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/134089684):
We thought you were dead!

#### [ Kevin Buzzard (Sep 17 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/134089686):
We were worried

#### [ Patrick Massot (Sep 17 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/134089692):
Or worse than dead: decided to use another proof assistant

#### [ Edward Ayers (Sep 17 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/134089697):
I was flirting with Isabelle again a bit

#### [ Johan Commelin (Sep 17 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/134089761):
Lol, I knew that :thumbs_up: was coming...

#### [ Johannes Hölzl (Sep 17 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/134089764):
hehe

#### [ Patrick Massot (Sep 17 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/134089767):
Scott, did we understand correctly what you learned in Dagstuhl?


{% endraw %}
