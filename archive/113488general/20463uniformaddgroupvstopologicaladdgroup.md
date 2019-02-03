---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20463uniformaddgroupvstopologicaladdgroup.html
---

## Stream: [general](index.html)
### Topic: [uniform_add_group vs topological_add_group](20463uniformaddgroupvstopologicaladdgroup.html)

---


{% raw %}
#### [ Kenny Lau (Nov 01 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891308):
<p>We know that a topological additive abelian group is a uniform additive group, and that a uniform additive group is a topological additive group</p>

#### [ Kenny Lau (Nov 01 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891315):
<p>but which one of them should be an instance? <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> <span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Mario Carneiro (Nov 01 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891448):
<p>if they are equivalent, then they should be the same</p>

#### [ Mario Carneiro (Nov 01 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891459):
<p>(I have a preference for the topological terminology)</p>

#### [ Kenny Lau (Nov 01 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891467):
<p>a topological additive group is based on a topological space and an additive group; a uniform additive group is based on a uniform space and an additive group</p>

#### [ Kenny Lau (Nov 01 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891473):
<p>they can't be the same, right</p>

#### [ Mario Carneiro (Nov 01 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891478):
<p>A topological add group has a uniform structure</p>

#### [ Mario Carneiro (Nov 01 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891487):
<p>so it's both</p>

#### [ Kenny Lau (Nov 01 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891488):
<p>but that would cause a loop in the inferrence</p>

#### [ Mario Carneiro (Nov 01 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891490):
<p>how?</p>

#### [ Mario Carneiro (Nov 01 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891493):
<p>I'm saying delete uniform add group and replace it with top add group</p>

#### [ Kenny Lau (Nov 01 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891536):
<p>aha</p>

#### [ Kenny Lau (Nov 01 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891546):
<p>now?</p>

#### [ Mario Carneiro (Nov 01 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891551):
<p>Actually I guess this is already how uniform_add_group is defined</p>

#### [ Mario Carneiro (Nov 01 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891553):
<p>so it's just a rename</p>

#### [ Kenny Lau (Nov 01 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891571):
<p>well, currently we have:</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">uniform_add_group</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">add_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">uniform_continuous_sub</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="o">(</span><span class="bp">λ</span><span class="n">p</span><span class="o">:</span><span class="n">α</span><span class="bp">×</span><span class="n">α</span><span class="o">,</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">-</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span><span class="o">))</span>
</pre></div>

#### [ Mario Carneiro (Nov 01 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891572):
<p>maybe you don't need uniform continuity</p>

#### [ Mario Carneiro (Nov 01 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891616):
<p>oh, it's a predicate</p>

#### [ Mario Carneiro (Nov 01 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891633):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> will object, but I want it to be a class</p>

#### [ Kenny Lau (Nov 01 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891713):
<p>indeed it is Hoelzl who introduced uniform add groups, at least according to <a href="https://github.com/leanprover/mathlib/commit/ba95269a65a77c8ab5eae075f842fdad0c0a7aaf#diff-da2fc75300f00796d9262c2c7c3bd09aR87" target="_blank" title="https://github.com/leanprover/mathlib/commit/ba95269a65a77c8ab5eae075f842fdad0c0a7aaf#diff-da2fc75300f00796d9262c2c7c3bd09aR87">this</a></p>

#### [ Mario Carneiro (Nov 01 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891731):
<p>oh, wait we do need uniform continuity</p>

#### [ Mario Carneiro (Nov 01 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891750):
<p>Is the uniformity of a uniform add group uniquely defined?</p>

#### [ Mario Carneiro (Nov 01 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891808):
<p>Topological groups actually have two induced uniformities, the left and right uniformity</p>

#### [ Mario Carneiro (Nov 01 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891834):
<p>so topological add group and uniform add group aren't exactly the same</p>

#### [ Mario Carneiro (Nov 01 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136891887):
<p>a uniform add group comes with a chosen uniformity, a top add group doesn't</p>

#### [ Kenny Lau (Nov 01 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136892371):
<p>so what should I do?</p>

#### [ Kenny Lau (Nov 01 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136908449):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> what do you think about this?</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136908529):
<p>This is an implementation issue and I have no idea.</p>

#### [ Kevin Buzzard (Nov 01 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136908576):
<p>I will comment though that with something like the Haar measure on a locally compact Hausdorff topological group, there are two: a left Haar measure and a right Haar measure, but mathematicians often just talk about "the Haar measure" and they have just randomly chosen one of them.</p>

#### [ Johan Commelin (Nov 01 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136909588):
<p>But these are additive groups, which should always be abelian, and then the uniformities coincide.</p>

#### [ Kevin Buzzard (Nov 01 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136909840):
<p>No -- Haar measure doesn't need abelian. It's Pontrjagin duality which needs abelian</p>

#### [ Johan Commelin (Nov 01 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136911163):
<p>Sure, I know that. Infinite Galois groups have Haar measures...<br>
So I think my point is: in the non-commutative case we don't want an instance from <code>topological_group</code> to <code>uniform_group</code> because in that case we want the user to explicitly say "Use the left uniformity" (or "use the left Haar measure", etc...). But in the commutative case, the left and right uniformity agree (just as with Haar measures), so it would make sense if the system could automatically pick one. But then we get diamond issues, and maybe it is just not worth it.</p>

#### [ Kevin Buzzard (Nov 01 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136926698):
<p>Oh I see! Sorry :-) What I'm suggesting is that we always use the left one.</p>

#### [ Patrick Massot (Nov 01 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136940731):
<p>I was also confused by uniform_add_group in the beginning, and wanted to get rid of it and keep topological add groups. But then I had this completion diamond issue, and Johannes fixed it by using more uniform_add_group...</p>

#### [ Kenny Lau (Nov 01 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136942309):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> the problem is that I'm cleaning up the perfectoid project in which you have an instance of topological add comm group -&gt; uniform add group</p>

#### [ Kenny Lau (Nov 01 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136942317):
<p>which messes up everything</p>

#### [ Johan Commelin (Nov 01 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136942896):
<p>How much breaks if you remove that instance?</p>

#### [ Patrick Massot (Nov 01 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136944935):
<p>Everything about topological rings in the perfectoid project has been merged into mathlib, you can get rid of everything</p>

#### [ Kenny Lau (Nov 01 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136945077):
<p>I don't think it's everything</p>

#### [ Kenny Lau (Nov 01 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136945126):
<p>here's what is left of <code>for_mathlib/uniform_space.lean</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">completion</span>
<span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">uniform_space</span>

<span class="kn">namespace</span> <span class="n">uniform_space</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">γ</span><span class="o">]</span>
<span class="kn">open</span> <span class="n">Cauchy</span> <span class="n">set</span>

<span class="n">def</span> <span class="n">pure_cauchy₂</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">Cauchy</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">Cauchy</span> <span class="n">β</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="o">(</span><span class="n">pure_cauchy</span> <span class="n">x</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">pure_cauchy</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">pure_cauchy_dense₂</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">x</span> <span class="o">:</span> <span class="n">Cauchy</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">Cauchy</span> <span class="n">β</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">closure</span> <span class="o">(</span><span class="n">range</span> <span class="o">(</span><span class="bp">@</span><span class="n">pure_cauchy₂</span> <span class="n">α</span> <span class="bp">_</span> <span class="n">β</span> <span class="bp">_</span><span class="o">))</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intro</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">dsimp</span><span class="o">[</span><span class="n">pure_cauchy₂</span><span class="o">],</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span><span class="n">prod_range_range_eq</span><span class="o">,</span> <span class="n">closure_prod_eq</span><span class="o">],</span>
  <span class="n">simp</span><span class="o">[</span><span class="n">prod</span><span class="bp">.</span><span class="n">ext_iff</span><span class="o">,</span> <span class="n">pure_cauchy_dense</span><span class="o">],</span>
<span class="kn">end</span>

<span class="kn">namespace</span> <span class="n">pure_cauchy</span>

<span class="kn">lemma</span> <span class="n">prod</span><span class="bp">.</span><span class="n">de</span> <span class="o">:</span> <span class="n">dense_embedding</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">β</span><span class="o">,</span> <span class="o">(</span><span class="n">pure_cauchy</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">pure_cauchy</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span><span class="o">))</span> <span class="o">:=</span>
<span class="n">dense_embedding</span><span class="bp">.</span><span class="n">prod</span> <span class="n">dense_embedding_pure_cauchy</span> <span class="n">dense_embedding_pure_cauchy</span>
<span class="kn">end</span> <span class="n">pure_cauchy</span>

<span class="kn">end</span> <span class="n">uniform_space</span>
</pre></div>

#### [ Johan Commelin (Nov 01 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136945274):
<p>Are those lemmas used elsewhere in the perfectoid project?</p>

#### [ Kenny Lau (Nov 01 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136945292):
<p>I don't know</p>

#### [ Patrick Massot (Nov 01 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/uniform_add_group%20vs%20topological_add_group/near/136948798):
<p>You can remove this.</p>


{% endraw %}
