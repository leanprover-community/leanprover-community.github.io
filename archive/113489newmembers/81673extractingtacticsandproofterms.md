---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/81673extractingtacticsandproofterms.html
---

## Stream: [new members](index.html)
### Topic: [extracting tactics and proof terms](81673extractingtacticsandproofterms.html)

---


{% raw %}
#### [ Michael Jendrusch (Nov 12 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/extracting%20tactics%20and%20proof%20terms/near/147516992):
<p>This is probably a question with a simple answer, but I'll ask it either way. Is there a way to programmatically extract the sequence of tactics used to prove a given lemma? I can get the proof term pretty easily by doing something like this:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span>
<span class="kn">open</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>

<span class="kn">namespace</span> <span class="n">my_namespace</span>

<span class="kn">lemma</span> <span class="n">my_lemma</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">&gt;</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intros</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">gt</span><span class="o">,</span>
  <span class="n">simp</span><span class="o">,</span>
  <span class="n">comp_val</span><span class="o">,</span>
<span class="kn">end</span>

<span class="bp">#</span><span class="kn">eval</span> <span class="n">do</span>
  <span class="n">env</span> <span class="err">←</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">get_env</span><span class="o">,</span>
  <span class="n">ml</span>  <span class="err">←</span> <span class="n">env</span><span class="bp">.</span><span class="n">get</span><span class="o">(</span><span class="n">mk_str_name</span> <span class="s2">&quot;my_namespace&quot;</span> <span class="s2">&quot;my_lemma&quot;</span><span class="o">),</span>
  <span class="n">fmt</span> <span class="err">←</span> <span class="n">tactic_format_expr</span> <span class="n">ml</span><span class="bp">.</span><span class="n">value</span><span class="o">,</span>
  <span class="n">trace</span> <span class="err">$</span> <span class="s2">&quot;type  : &quot;</span> <span class="bp">++</span> <span class="o">(</span><span class="n">to_string</span> <span class="err">$</span> <span class="n">expr</span><span class="bp">.</span><span class="n">to_raw_fmt</span> <span class="n">ml</span><span class="bp">.</span><span class="n">type</span><span class="o">)</span> <span class="bp">++</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">,</span>
  <span class="n">trace</span> <span class="err">$</span> <span class="s2">&quot;value : &quot;</span> <span class="bp">++</span> <span class="o">(</span><span class="n">to_string</span> <span class="err">$</span> <span class="n">expr</span><span class="bp">.</span><span class="n">to_raw_fmt</span> <span class="n">ml</span><span class="bp">.</span><span class="n">value</span><span class="o">)</span> <span class="bp">++</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">,</span>
  <span class="n">return</span> <span class="n">unit</span><span class="bp">.</span><span class="n">star</span>

<span class="kn">end</span> <span class="n">my_namespace</span>
</pre></div>


<p>but I haven't had any luck extracting tactics yet. On another note, is there some function other than <code>expr.to_raw_fmt</code> for serializing expressions?</p>

#### [ Mario Carneiro (Nov 12 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/extracting%20tactics%20and%20proof%20terms/near/147517509):
<p>No. It's not stored</p>

#### [ Keeley Hoek (Nov 12 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/extracting%20tactics%20and%20proof%20terms/near/147517700):
<p>What do you mean "serializing"?</p>

#### [ Michael Jendrusch (Nov 12 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/extracting%20tactics%20and%20proof%20terms/near/147519876):
<p>Serializing, as in generating some text (s-expression, JSON) or binary representation of expressions which can be read from another program. But I suppose <code>expr.to_raw_fmt</code>should be enough for my purposes.</p>


{% endraw %}
