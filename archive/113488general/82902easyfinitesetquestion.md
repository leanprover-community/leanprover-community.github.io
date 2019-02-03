---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/82902easyfinitesetquestion.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [easy finite set question](https://leanprover-community.github.io/archive/113488general/82902easyfinitesetquestion.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Apr 15 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20finite%20set%20question/near/125096226):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">C</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">HC</span> <span class="o">:</span> <span class="n">set</span><span class="bp">.</span><span class="n">finite</span> <span class="n">C</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">C</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span><span class="bp">.</span><span class="n">finite</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Apr 15 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20finite%20set%20question/near/125096272):
<p>I see <code>fintype_range</code>, an instance proving that the range of a function with fintype domain is a fintype, but I have never worked with finite sets/types before. Should I be switching to and fro between finite sets and fintypes? Should I be letting type class inference and/or automation do the work for me? This stuff looks pretty easy in maths so hopefully isn't too painless here.</p>

#### [ Kenny Lau (Apr 15 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20finite%20set%20question/near/125096454):
<div class="codehilite"><pre><span></span>import data.set

local attribute [instance] classical.prop_decidable

example (X Y : Type) (C : set X) (HC : set.finite C) (f : C → Y) : set.finite (set.range f) :=
HC.rec $ λ HF, nonempty.intro $ @set.fintype_range _ _ _ f HF
</pre></div>

#### [ Kenny Lau (Apr 15 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20finite%20set%20question/near/125096493):
<div class="codehilite"><pre><span></span>import data.set

local attribute [instance] classical.prop_decidable

example (X Y : Type) (C : set X) (HC : set.finite C) (f : C → Y) : set.finite (set.range f) :=
let ⟨HF⟩ := HC in ⟨@set.fintype_range _ _ _ f HF⟩
</pre></div>

#### [ Kenny Lau (Apr 15 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20finite%20set%20question/near/125096591):
<div class="codehilite"><pre><span></span>import data.set

local attribute [instance] classical.prop_decidable

example (X Y : Type) (C : set X) (f : C → Y) : set.finite C → set.finite (set.range f)
| ⟨HF⟩ := ⟨@set.fintype_range _ _ _ f HF⟩
</pre></div>

#### [ Kevin Buzzard (Apr 15 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20finite%20set%20question/near/125096597):
<p>Thanks Kenny. I have spent all evening reducing the statement that Spec(R) is compact to the case of covers by a basis ;-)</p>

#### [ Kenny Lau (Apr 15 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20finite%20set%20question/near/125096598):
<p>nice</p>


{% endraw %}
