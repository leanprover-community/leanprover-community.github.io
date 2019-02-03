---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/97139Klikeinductivesdonttakearguments.html
---

## Stream: [general](index.html)
### Topic: [K-like inductives don't take arguments](97139Klikeinductivesdonttakearguments.html)

---


{% raw %}
#### [ Mario Carneiro (Mar 26 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/K-like%20inductives%20don%27t%20take%20arguments/near/124204821):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> I just discovered by reading the source code that lean doesn't consider an inductive suitable for K-like reduction unless it has 0 arguments in the constructor, rather than having all arguments in the output type like I thought (and wrote in my paper). Do you know why this is?</p>
<div class="codehilite"><pre><span></span>inductive  eq&#39; {α} : α → α →  Prop
| refl : ∀ a, eq&#39; a a
variables {α : Sort*} {C : α → α → Sort*}
(e : ∀ (a : α), C a a) (a : α) (h : eq&#39; a a)
#reduce  @eq&#39;.rec α C e a a h --expected: e a
</pre></div>

#### [ Gabriel Ebner (Mar 26 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/K-like%20inductives%20don%27t%20take%20arguments/near/124214212):
<p>The purpose of K-like reduction is that <code>eq</code> and <code>heq</code> reduce better.  And "single constructor with no arguments" is the easiest criterion for that.  IIRC, the code even constructs an explicit <code>eq.refl</code>/<code>heq.refl</code>/etc. term and checks whether it is def-eq with the major premise during reduction.</p>


{% endraw %}
