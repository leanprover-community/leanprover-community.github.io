---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64659notationintroducevariables.html
---

## Stream: [general](index.html)
### Topic: [notation introduce variables](64659notationintroducevariables.html)

---


{% raw %}
#### [ Joe Hendrix (Aug 10 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20introduce%20variables/near/131200648):
<p>Is it possible to write notation that will allow introducing variables?  e.g. have something like the following work:</p>
<div class="codehilite"><pre><span></span>local notation `flet` var `:=` rhs `fin` body := let var := rhs in body
example : ℕ := flet x := 1 fin x
</pre></div>

#### [ Simon Hudon (Aug 10 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20introduce%20variables/near/131200900):
<p>Yes, the following can be found in <code>core.lean</code>: <code>notation `exists` binders `, ` r:(scoped P, Exists P) := r</code> which illustrates how the binder / scoped notation works.</p>
<p>It let's you tell Lean how to parse a lambda abstract and choose a function (i.e. <code>Exists</code>) to feed that lambda expression to.</p>

#### [ Simon Hudon (Aug 10 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20introduce%20variables/near/131200992):
<p>I think your notation could work as <code>local notation `flet` binder `:=` rhs `fin` body:(scoped P, P rhs) := body</code></p>

#### [ Simon Hudon (Aug 10 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20introduce%20variables/near/131201428):
<p>To help with the pretty printing, you may way to define a function that Lean will associate with your notation:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">my_let</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">f</span> <span class="n">x</span>

<span class="n">local</span> <span class="kn">notation</span> <span class="bp">`</span><span class="n">flet</span><span class="bp">`</span> <span class="n">binder</span> <span class="bp">`</span><span class="o">:=</span><span class="bp">`</span> <span class="n">rhs</span> <span class="bp">`</span><span class="n">fin</span><span class="bp">`</span> <span class="n">body</span><span class="o">:(</span><span class="n">scoped</span> <span class="n">P</span><span class="o">,</span> <span class="n">my_let</span> <span class="n">P</span> <span class="n">rhs</span><span class="o">)</span> <span class="o">:=</span> <span class="n">body</span>
</pre></div>

#### [ Joe Hendrix (Aug 10 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20introduce%20variables/near/131202287):
<p>Great.  Thanks for finding that.</p>

#### [ Simon Hudon (Aug 10 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20introduce%20variables/near/131202453):
<p><span class="emoji emoji-1f44d" title="+1">:+1:</span> To be fair, a few months back, there was intense session on gitter, looking through the C++ code and figuring out the ins and outs of the <code>notation</code> notation</p>


{% endraw %}
