---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89093notesonparametricity.html
---

## Stream: [general](index.html)
### Topic: [notes on parametricity](89093notesonparametricity.html)

---


{% raw %}
#### [ Reid Barton (Apr 28 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notes%20on%20parametricity/near/125810022):
<p>Since the subject of parametricity came up, here are some papers which may be of interest and should be relatively readable for mathematicians (especially those who are also Lean users). These papers pertain to non-dependently typed languages; I don't know what differences there might be in the dependently typed setting.</p>
<ul>
<li>Types, abstraction and parametric polymorphism <a href="http://www.cse.chalmers.se/edu/year/2010/course/DAT140_Types/Reynolds_typesabpara.pdf" target="_blank" title="http://www.cse.chalmers.se/edu/year/2010/course/DAT140_Types/Reynolds_typesabpara.pdf">http://www.cse.chalmers.se/edu/year/2010/course/DAT140_Types/Reynolds_typesabpara.pdf</a></li>
<li>Theorems for free! <a href="http://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.38.9875" target="_blank" title="http://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.38.9875">http://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.38.9875</a></li>
</ul>

#### [ Johan Commelin (Apr 28 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notes%20on%20parametricity/near/125810743):
<p>Reid, thanks for those links. The Fable about complex numbers was a good illustration.</p>

#### [ Johan Commelin (Apr 28 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notes%20on%20parametricity/near/125810841):
<p>However, I think it is slightly different from transport of structure</p>

#### [ Mario Carneiro (Apr 28 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notes%20on%20parametricity/near/125812837):
<p>Theorems for free! is exactly the paper that covers the right generic approach to parametricity</p>

#### [ Reid Barton (Apr 28 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notes%20on%20parametricity/near/125825527):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> You're right that what those papers talk about isn't quite transport of structure. Instead it's the question about transfer of structure commuting with user-defined functions. For example the free theorem for <code>list</code> implies in particular that any defined function of type <code>list a \to list a</code> must commute with the "transfer of structure" equivalence <code>list a \simeq list b</code> that arises from an equivalence <code>a \simeq b</code>.</p>

#### [ Reid Barton (Apr 28 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notes%20on%20parametricity/near/125825533):
<p>(The "transfer of structure" equivalence in this case just being the list map function.)</p>

#### [ Reid Barton (Apr 28 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notes%20on%20parametricity/near/125825621):
<p>I think the reason that the scope does not extend to transfer of structure itself is that in the languages used in those papers, type constructors like <code>list : Type \to Type</code> are not definable, or at least do not have the same status as value-level functions, and so they are not in the universe of things to which one might apply parametricity theorems.</p>

#### [ Reid Barton (Apr 28 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notes%20on%20parametricity/near/125825677):
<p>But I guess if you extend the idea of parametricity to a setting (like Lean) where you can have user-defined functions which produce <code>Type</code>, then you get a parametricity result which is "one category level higher" in that it produces an equivalence between two types, rather than an equation between two values</p>

#### [ Johan Commelin (Apr 28 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notes%20on%20parametricity/near/125826902):
<p>I see. I'm going to give Wadlers "Theorems for free" a close look. I think it contains important ideas.</p>


{% endraw %}
