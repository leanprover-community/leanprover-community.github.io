---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/42489metaprogrammingandstructureinheritance.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [metaprogramming and structure inheritance](https://leanprover-community.github.io/archive/113488general/42489metaprogrammingandstructureinheritance.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Simon Hudon (Mar 11 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metaprogramming%20and%20structure%20inheritance/near/123582486):
<p>I'm trying to write a tactic that explores the inheritance structure. Given the name of a structure type, can I discover what are its ancestors?</p>

#### [ Sebastian Ullrich (Mar 11 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metaprogramming%20and%20structure%20inheritance/near/123583537):
<p>Only for the new structure command. You need to reimplement <a href="https://github.com/leanprover/lean/blob/bdea7d420dbcdb7cce700eb62c129387707016fc/src/frontends/lean/structure_cmd.cpp#L139" target="_blank" title="https://github.com/leanprover/lean/blob/bdea7d420dbcdb7cce700eb62c129387707016fc/src/frontends/lean/structure_cmd.cpp#L139">get_parent_structures</a>, but that shouldn't be too hard.</p>

#### [ Sebastian Ullrich (Mar 11 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metaprogramming%20and%20structure%20inheritance/near/123583547):
<p>tl;dr: subobject fields start with "_"</p>

#### [ Simon Hudon (Mar 11 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metaprogramming%20and%20structure%20inheritance/near/123583803):
<p>How does one use the new structure command? Also, is <code>get_parent_structures</code> exposed to Lean?</p>

#### [ Andrew Ashworth (Mar 11 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metaprogramming%20and%20structure%20inheritance/near/123583950):
<p>you're using the new structure command by default, I think</p>

#### [ Andrew Ashworth (Mar 11 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metaprogramming%20and%20structure%20inheritance/near/123583951):
<p>as opposed to the old structure command which is accessed with <code>set option</code></p>

#### [ Sebastian Ullrich (Mar 11 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metaprogramming%20and%20structure%20inheritance/near/123583953):
<p>yep</p>

#### [ Simon Hudon (Mar 11 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metaprogramming%20and%20structure%20inheritance/near/123584118):
<p>Thanks! And is it possible that <code>structure_fields</code> by default does not list those symbols starting with <code>_</code>?</p>

#### [ Sebastian Ullrich (Mar 11 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metaprogramming%20and%20structure%20inheritance/near/123584218):
<p>Sorry, that was ambiguous. It's only in the inductive constructor parameters that they are encoded with <code>_</code></p>

#### [ Sebastian Ullrich (Mar 11 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metaprogramming%20and%20structure%20inheritance/near/123584227):
<p>All <code>structure_fields</code> does is get the parameter names and strip any leading <code>_</code></p>

#### [ Simon Hudon (Mar 11 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metaprogramming%20and%20structure%20inheritance/near/123584544):
<p>Let's say that I'm constructing an instance of <code>group</code> (but I don't know in the tactic that it is specifically group). I'd like to know that <code>monoid</code> is a direct parent so that I can use <code>mk_instance</code> and use the result as a source in <code>pexpr.mk_structure_instance</code>. How would you do it?</p>


{% endraw %}
