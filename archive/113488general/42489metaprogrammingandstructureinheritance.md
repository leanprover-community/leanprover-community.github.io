---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/42489metaprogrammingandstructureinheritance.html
---

## Stream: [general](index.html)
### Topic: [metaprogramming and structure inheritance](42489metaprogrammingandstructureinheritance.html)

---

#### [Simon Hudon (Mar 11 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metaprogramming%20and%20structure%20inheritance/near/123582486):
I'm trying to write a tactic that explores the inheritance structure. Given the name of a structure type, can I discover what are its ancestors?

#### [Sebastian Ullrich (Mar 11 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metaprogramming%20and%20structure%20inheritance/near/123583537):
Only for the new structure command. You need to reimplement [get_parent_structures](https://github.com/leanprover/lean/blob/bdea7d420dbcdb7cce700eb62c129387707016fc/src/frontends/lean/structure_cmd.cpp#L139), but that shouldn't be too hard.

#### [Sebastian Ullrich (Mar 11 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metaprogramming%20and%20structure%20inheritance/near/123583547):
tl;dr: subobject fields start with "_"

#### [Simon Hudon (Mar 11 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metaprogramming%20and%20structure%20inheritance/near/123583803):
How does one use the new structure command? Also, is `get_parent_structures` exposed to Lean?

#### [Andrew Ashworth (Mar 11 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metaprogramming%20and%20structure%20inheritance/near/123583950):
you're using the new structure command by default, I think

#### [Andrew Ashworth (Mar 11 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metaprogramming%20and%20structure%20inheritance/near/123583951):
as opposed to the old structure command which is accessed with `set option`

#### [Sebastian Ullrich (Mar 11 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metaprogramming%20and%20structure%20inheritance/near/123583953):
yep

#### [Simon Hudon (Mar 11 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metaprogramming%20and%20structure%20inheritance/near/123584118):
Thanks! And is it possible that `structure_fields` by default does not list those symbols starting with `_`?

#### [Sebastian Ullrich (Mar 11 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metaprogramming%20and%20structure%20inheritance/near/123584218):
Sorry, that was ambiguous. It's only in the inductive constructor parameters that they are encoded with `_`

#### [Sebastian Ullrich (Mar 11 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metaprogramming%20and%20structure%20inheritance/near/123584227):
All `structure_fields` does is get the parameter names and strip any leading `_`

#### [Simon Hudon (Mar 11 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metaprogramming%20and%20structure%20inheritance/near/123584544):
Let's say that I'm constructing an instance of `group` (but I don't know in the tactic that it is specifically group). I'd like to know that `monoid` is a direct parent so that I can use `mk_instance` and use the result as a source in `pexpr.mk_structure_instance`. How would you do it?

