---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03821isthereatactic.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [is there a tactic?](https://leanprover-community.github.io/archive/113488general/03821isthereatactic.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sean Leather (Sep 12 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133785751):
<p>Is there a tactic for (part of) this?</p>
<div class="codehilite"><pre><span></span><span class="k">by</span> <span class="n">cases</span> <span class="n">l</span><span class="bp">;</span> <span class="n">apply</span> <span class="n">exists</span><span class="bp">.</span><span class="n">intro</span><span class="bp">;</span> <span class="n">assumption</span><span class="bp">;</span> <span class="n">assumption</span>
</pre></div>

#### [ Johan Commelin (Sep 12 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133785823):
<p>Will <code>tidy</code> do this? Or can it not yet do <code>exists.intro</code>?</p>

#### [ Sean Leather (Sep 12 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133785841):
<p>I've never used <code>tidy</code>.</p>

#### [ Johan Commelin (Sep 12 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133785855):
<p>It is really cool. You'll need <code>import tactic.tidy</code>.</p>

#### [ Kenny Lau (Sep 12 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133785901):
<p>I'd just write the whole thing in term mode</p>

#### [ Sean Leather (Sep 12 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786086):
<p>Kenny: I had that, but the tactic is more robust to changes in <code>l</code>, which are happening.</p>

#### [ Sean Leather (Sep 12 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786206):
<p>Also, <code>l</code> has a lot of fields, so either using pattern matching or <code>cases l with ...</code> is annoyingly long.</p>

#### [ Johan Commelin (Sep 12 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786220):
<p>Does <code>tidy</code> work?</p>

#### [ Sean Leather (Sep 12 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786279):
<p><code> by cases l; tidy</code> works</p>

#### [ Sean Leather (Sep 12 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786383):
<p><code> by cases l; tidy {trace_result:=tt}</code> doesn't print anything. <span class="emoji emoji-1f615" title="concerned">:concerned:</span></p>

#### [ Johan Commelin (Sep 12 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786679):
<p>Huh, so <code>tidy</code> won't do the <code>cases</code> for you? I expected that it would try that, as some last resort...</p>

#### [ Johan Commelin (Sep 12 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786702):
<p><span class="user-mention" data-user-id="110045">@Sean Leather</span> You can use hole commands to let VScode replace <code>tidy</code> with the proof it generated.</p>

#### [ Sean Leather (Sep 12 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786713):
<p>I suppose that would be listed here if it did:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">default_tactics</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">tactic</span> <span class="n">string</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">[</span> <span class="n">reflexivity</span>                                 <span class="bp">&gt;&gt;</span> <span class="n">pure</span> <span class="s2">&quot;refl&quot;</span><span class="o">,</span>
  <span class="bp">`</span><span class="o">[</span><span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">]</span>                        <span class="bp">&gt;&gt;</span> <span class="n">pure</span> <span class="s2">&quot;exact dec_trivial&quot;</span><span class="o">,</span>
  <span class="n">propositional_goal</span> <span class="bp">&gt;&gt;</span> <span class="n">assumption</span>            <span class="bp">&gt;&gt;</span> <span class="n">pure</span> <span class="s2">&quot;assumption&quot;</span><span class="o">,</span>
  <span class="bp">`</span><span class="o">[</span><span class="n">ext1</span><span class="o">]</span>                                     <span class="bp">&gt;&gt;</span> <span class="n">pure</span> <span class="s2">&quot;ext1&quot;</span><span class="o">,</span>
  <span class="n">intros1</span>                                     <span class="bp">&gt;&gt;=</span> <span class="bp">λ</span> <span class="n">ns</span><span class="o">,</span> <span class="n">pure</span> <span class="o">(</span><span class="s2">&quot;intros &quot;</span> <span class="bp">++</span> <span class="o">(</span><span class="s2">&quot; &quot;</span><span class="bp">.</span><span class="n">intercalate</span> <span class="o">(</span><span class="n">ns</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">e</span><span class="o">,</span> <span class="n">e</span><span class="bp">.</span><span class="n">to_string</span><span class="o">)))),</span>
  <span class="n">auto_cases</span><span class="o">,</span>
  <span class="bp">`</span><span class="o">[</span><span class="n">apply_auto_param</span><span class="o">]</span>                         <span class="bp">&gt;&gt;</span> <span class="n">pure</span> <span class="s2">&quot;apply_auto_param&quot;</span><span class="o">,</span>
  <span class="bp">`</span><span class="o">[</span><span class="n">dsimp</span> <span class="n">at</span> <span class="bp">*</span><span class="o">]</span>                               <span class="bp">&gt;&gt;</span> <span class="n">pure</span> <span class="s2">&quot;dsimp at *&quot;</span><span class="o">,</span>
  <span class="bp">`</span><span class="o">[</span><span class="n">simp</span> <span class="n">at</span> <span class="bp">*</span><span class="o">]</span>                                <span class="bp">&gt;&gt;</span> <span class="n">pure</span> <span class="s2">&quot;simp at *&quot;</span><span class="o">,</span>
  <span class="n">fsplit</span>                                      <span class="bp">&gt;&gt;</span> <span class="n">pure</span> <span class="s2">&quot;fsplit&quot;</span><span class="o">,</span>
  <span class="n">injections_and_clear</span>                        <span class="bp">&gt;&gt;</span> <span class="n">pure</span> <span class="s2">&quot;injections_and_clear&quot;</span><span class="o">,</span>
  <span class="n">propositional_goal</span> <span class="bp">&gt;&gt;</span> <span class="o">(</span><span class="bp">`</span><span class="o">[</span><span class="n">solve_by_elim</span><span class="o">])</span>    <span class="bp">&gt;&gt;</span> <span class="n">pure</span> <span class="s2">&quot;solve_by_elim&quot;</span><span class="o">,</span>
  <span class="bp">`</span><span class="o">[</span><span class="n">unfold_aux</span><span class="o">]</span>                               <span class="bp">&gt;&gt;</span> <span class="n">pure</span> <span class="s2">&quot;unfold_aux&quot;</span><span class="o">,</span>
  <span class="n">tidy</span><span class="bp">.</span><span class="n">run_tactics</span> <span class="o">]</span>
</pre></div>

#### [ Johan Commelin (Sep 12 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786720):
<p>what does <code>auto_cases</code> do?</p>

#### [ Sean Leather (Sep 12 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786728):
<p>No idea. <span class="emoji emoji-1f642" title="slight smile">:slight_smile:</span></p>

#### [ Sean Leather (Sep 12 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786771):
<div class="codehilite"><pre><span></span>  <span class="n">t&#39;</span> <span class="err">←</span> <span class="n">whnf</span> <span class="n">t&#39;</span><span class="o">,</span>
  <span class="k">let</span> <span class="n">use_cases</span> <span class="o">:=</span> <span class="k">match</span> <span class="n">t&#39;</span> <span class="k">with</span>
  <span class="bp">|</span> <span class="bp">`</span><span class="o">(</span><span class="n">empty</span><span class="o">)</span>     <span class="o">:=</span> <span class="n">tt</span>
  <span class="bp">|</span> <span class="bp">`</span><span class="o">(</span><span class="n">pempty</span><span class="o">)</span>    <span class="o">:=</span> <span class="n">tt</span>
  <span class="bp">|</span> <span class="bp">`</span><span class="o">(</span><span class="n">unit</span><span class="o">)</span>      <span class="o">:=</span> <span class="n">tt</span>
  <span class="bp">|</span> <span class="bp">`</span><span class="o">(</span><span class="n">punit</span><span class="o">)</span>     <span class="o">:=</span> <span class="n">tt</span>
  <span class="bp">|</span> <span class="bp">`</span><span class="o">(</span><span class="n">ulift</span> <span class="bp">_</span><span class="o">)</span>   <span class="o">:=</span> <span class="n">tt</span>
  <span class="bp">|</span> <span class="bp">`</span><span class="o">(</span><span class="n">plift</span> <span class="bp">_</span><span class="o">)</span>   <span class="o">:=</span> <span class="n">tt</span>
  <span class="bp">|</span> <span class="bp">`</span><span class="o">(</span><span class="n">prod</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>  <span class="o">:=</span> <span class="n">tt</span>
  <span class="bp">|</span> <span class="bp">`</span><span class="o">(</span><span class="n">and</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>   <span class="o">:=</span> <span class="n">tt</span>
  <span class="bp">|</span> <span class="bp">`</span><span class="o">(</span><span class="n">sigma</span> <span class="bp">_</span><span class="o">)</span>   <span class="o">:=</span> <span class="n">tt</span>
  <span class="bp">|</span> <span class="bp">`</span><span class="o">(</span><span class="n">subtype</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">tt</span>
  <span class="bp">|</span> <span class="bp">`</span><span class="o">(</span><span class="n">Exists</span> <span class="bp">_</span><span class="o">)</span>  <span class="o">:=</span> <span class="n">tt</span>
  <span class="bp">|</span> <span class="bp">`</span><span class="o">(</span><span class="n">fin</span> <span class="mi">0</span><span class="o">)</span>     <span class="o">:=</span> <span class="n">tt</span>
  <span class="bp">|</span> <span class="bp">`</span><span class="o">(</span><span class="n">sum</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>   <span class="o">:=</span> <span class="n">tt</span> <span class="c1">-- This is perhaps dangerous!</span>
  <span class="bp">|</span> <span class="bp">`</span><span class="o">(</span><span class="n">or</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>    <span class="o">:=</span> <span class="n">tt</span> <span class="c1">-- This is perhaps dangerous!</span>
  <span class="bp">|</span> <span class="bp">_</span>            <span class="o">:=</span> <span class="n">ff</span>
</pre></div>

#### [ Sean Leather (Sep 12 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786777):
<p>Looks like it's restricted to certain patterns.</p>

#### [ Johan Commelin (Sep 12 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786786):
<p>Right... I guess that makes sense.</p>

#### [ Johan Commelin (Sep 12 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786795):
<p>Anyway, we still golfed your proof (-;</p>

#### [ Johan Commelin (Sep 12 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786812):
<p>It makes sense that <code>cases l</code> remains in the proof. It is probably an "idea". After that it is "follow your nose"</p>

#### [ Sean Leather (Sep 12 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786813):
<p>Yep, thanks! I learned something new.</p>

#### [ Sean Leather (Sep 12 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786871):
<p>It would be nice to see what <code>tidy</code> is doing, though.</p>

#### [ Keeley Hoek (Sep 12 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133786948):
<p>Sean, are you using a version of mathlib which incorporates this commit?<br>
<a href="https://github.com/leanprover/mathlib/commit/e95111d38c0b2d666f70624ce25a5d728e0db376" target="_blank" title="https://github.com/leanprover/mathlib/commit/e95111d38c0b2d666f70624ce25a5d728e0db376">https://github.com/leanprover/mathlib/commit/e95111d38c0b2d666f70624ce25a5d728e0db376</a></p>

#### [ Sean Leather (Sep 12 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20there%20a%20tactic%3F/near/133787037):
<p><span class="user-mention" data-user-id="110111">@Keeley Hoek</span> No, certainly not. Thanks!</p>


{% endraw %}
