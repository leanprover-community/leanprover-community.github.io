---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/73049notationandvariables.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [notation and variables](https://leanprover-community.github.io/archive/113488general/73049notationandvariables.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Nov 30 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20and%20variables/near/148826839):
<p>It suddenly occurs to me, about 10 hours before a lecture (and I intend to spend at least 7 of those hours sleeping) that it would be cool if I could do some examples of basic arguments with equivalence relations in Lean, live in the lecture. But actually I am not sure of the best way to do this. Here's the sort of thing I want to do -- prove, for example, that if <code>r</code> is an equivalence relation, and <code>r a b</code> and <code>r c b</code> and <code>r c d</code>, then <code>r a d</code>. But I want to do it with notation -- I want to write <code>a ~ b</code> or some -- any -- random symbol, rather than the prefix notation <code>r</code>. However when I define <code>r : S -&gt; S -&gt; Prop</code> as a variable I find that I can't use notation, because <code>r</code> is a local variable, and if I define <code>r</code> within an example -- <code>example (S : Type) (r : S -&gt; S -&gt; Prop)...</code> then I can't figure out how to get notation working before I state the theorem. What am I missing? This is for teaching purposes, so I want it to look as slick as possible.</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">S</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">equivalence</span> <span class="n">r</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">S</span><span class="o">,</span> <span class="n">r</span> <span class="n">a</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">H</span><span class="bp">.</span><span class="mi">1</span>
</pre></div>


<p>That is not ideal either -- <code>H.1</code> looks a bit weird to a mathematician :-/ But I think I'd rather have the notation, and worry about <code>H.1</code> later...</p>

#### [ Reid Barton (Nov 30 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20and%20variables/near/148827043):
<p>You can use local notation. For example <a href="https://gist.github.com/rwbarton/7bd5b3b19d930f577355a596a5ed8b4d#file-crec-lean-L7" target="_blank" title="https://gist.github.com/rwbarton/7bd5b3b19d930f577355a596a5ed8b4d#file-crec-lean-L7">https://gist.github.com/rwbarton/7bd5b3b19d930f577355a596a5ed8b4d#file-crec-lean-L7</a><br>
I don't think the fact that I used <code>parameter</code> rather than <code>variable</code> there matters for this</p>

#### [ Kevin Buzzard (Nov 30 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20and%20variables/near/148828911):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">S</span> <span class="bp">→</span> <span class="o">(</span><span class="n">S</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">))</span>

<span class="n">local</span> <span class="kn">notation</span> <span class="n">a</span> <span class="bp">`</span> <span class="bp">~</span> <span class="bp">`</span> <span class="n">b</span> <span class="o">:=</span> <span class="n">r</span> <span class="n">a</span> <span class="n">b</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">equivalence</span> <span class="n">r</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="o">:</span> <span class="n">S</span><span class="o">)</span>
  <span class="o">(</span><span class="n">Hab</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">~</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">Hcb</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">~</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">Hcd</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">~</span> <span class="n">d</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">~</span> <span class="n">d</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rcases</span> <span class="n">H</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">Hrefl</span><span class="o">,</span><span class="n">Hsymm</span><span class="o">,</span><span class="n">Htrans</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">Hbc</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">~</span> <span class="n">c</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">Hsymm</span> <span class="n">Hcb</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">Hac</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">~</span> <span class="n">c</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">Htrans</span> <span class="n">Hab</span> <span class="n">Hbc</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">Htrans</span> <span class="n">Hac</span> <span class="n">Hcd</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>Works! I am in two minds about whether to use rcases or cases twice and save myself the import.</p>

#### [ Kevin Buzzard (Nov 30 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20and%20variables/near/148828913):
<p>Thanks Reid.</p>

#### [ Mario Carneiro (Nov 30 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20and%20variables/near/148829124):
<p>don't save yourself the import</p>

#### [ Mario Carneiro (Nov 30 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20and%20variables/near/148829126):
<p>I think it is good to show off mathlib tactics when possible</p>

#### [ Kevin Buzzard (Nov 30 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20and%20variables/near/148830140):
<p>Hey! I've just noticed that the pretty printer doesn't use my nice notation for r!</p>

#### [ Kevin Buzzard (Nov 30 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20and%20variables/near/148830862):
<p>aww man, that's a bit annoying. I definitely want to work with an arbitrary equivalence relation but I'd really like the notation.</p>


{% endraw %}
