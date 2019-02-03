---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/91157spotthemetavariable.html
---

## Stream: [general](index.html)
### Topic: [spot the metavariable](91157spotthemetavariable.html)

---


{% raw %}
#### [ Kevin Buzzard (Apr 09 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124814424):
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">print</span> <span class="n">false</span><span class="bp">.</span><span class="n">rec</span> <span class="c1">-- protected eliminator false.rec : Π (C : Sort l), false → C</span>
<span class="kn">constant</span> <span class="n">oops</span> <span class="o">:</span> <span class="n">false</span>
<span class="kn">definition</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">false</span><span class="bp">.</span><span class="n">rec</span> <span class="bp">ℕ</span> <span class="n">oops</span> <span class="c1">-- the &quot;expected type must not contain metavariables&quot; error</span>
<span class="kn">definition</span> <span class="n">m</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">false</span><span class="bp">.</span><span class="n">rec</span> <span class="bp">ℕ</span> <span class="n">oops</span> <span class="c1">-- typechecks just fine</span>
</pre></div>

#### [ Kevin Buzzard (Apr 09 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124814469):
<p>I am not sure I have seen <code>foo</code> and <code>@foo</code> behave differently before, in a situation where there are no implicit arguments</p>

#### [ Gabriel Ebner (Apr 09 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124823987):
<p>In case you didn't already see it, the metavariable is in the type of the definition:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">_</span> <span class="o">:=</span> <span class="bp">...</span>
<span class="n">def</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">_</span> <span class="o">:=</span> <span class="bp">...</span>
</pre></div>

#### [ Gabriel Ebner (Apr 09 2018 at 08:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124824035):
<p>The elaborator does not only take a pre-expression, but also an expected type as argument.  Expected types are important to elaborate many pre-expressions, for example recursor applications or anonymous structure instances.  This is why <code>foo</code> works but <code>bar</code> doesn't:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">foo</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">×</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="mi">1</span><span class="o">,</span> <span class="mi">2</span><span class="bp">⟩</span>
<span class="n">def</span> <span class="n">bar</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="mi">1</span><span class="o">,</span> <span class="mi">2</span><span class="bp">⟩</span>
</pre></div>

#### [ Gabriel Ebner (Apr 09 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124824642):
<p>Elaboration of recursor applications is particularly sensitive to the expected type since the motive is computed by generalizing all occurrences of the major premise in the expected type.  So when we elaborate <code>nat.rec_on k _ _</code>, we elaborate the major premise <code>k</code> and then replace <code>k</code> by a fresh variable in the expected type to get the motive.  If the expected type is <code>C k (k+1)</code> for example, then we'd compute the motive <code>λ x, C x (x+1)</code>.  In your example, the elaborator just has a metavariable as expected type and cannot replace occurrences of the major premise (in a sensible way) to compute a motive.</p>

#### [ Gabriel Ebner (Apr 09 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124824743):
<p>Maybe this is already clear, but in elaboration the "expected type" is the type the elaborated expression is supposed to have.  For example, when we elaborate <code>⟨1, 2⟩ : ℕ × ℕ</code>, we elaborate the pre-expression <code>⟨1, 2⟩</code> with the expected type <code>ℕ × ℕ</code>.</p>

#### [ Gabriel Ebner (Apr 09 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124824750):
<p>Fun trick: you can suppress expected type propagation with <code>: _</code>.</p>

#### [ Kevin Buzzard (Apr 09 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124831500):
<p>I don't understand your answer. In contrast to most <code>blah.rec</code> recursors, which have type <code> Π {C : blah -&gt; Sort u},...</code>, <code>false.rec</code> has type <code> Π (C : Sort u_1), false → C </code>, so whilst in general I can see the issue and why that generic error shows up, for <code>false.rec</code> the information is there. I guess what I am saying is that perhaps the definition <code>false.rec</code> seems to have been explicitly manipulated by the system so that the motive is not implicit, but the error seems to indicate that some generic rule for recursors has been applied without noticing that in this case it does not apply. I have given Lean all the information it needs to work out the expected type and it has chosen to ignore it because I didn't put the <code>@</code>. That's the point I'm trying to make -- the elaborator, in this case, has all the information it needs, despite no <code>@</code>.</p>

#### [ Kevin Buzzard (Apr 09 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124831511):
<p>I am trying to figure out how the elaborator works without reading the source code. Am I crazy? Is this not even possible, really? Stuff like " The elaborator does not only take a pre-expression, but also an expected type as argument. " are gold dust to me because I don't see any way of working this stuff out without asking.</p>

#### [ Kevin Buzzard (Apr 09 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124831692):
<p>Another way of saying what I don't understand -- <code> false.rec ℕ oops </code> and <code>@false.rec ℕ oops </code> carry exactly the same information, but one works in a situation where the other does not, so it looks to me like some code somewhere is incorrectly distinguishing between them based on a "oh, there's an eliminator without an @, we are going to have to do some guesswork" principle which does not apply in this case.</p>

#### [ Kevin Buzzard (Apr 09 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124831834):
<p>I guess a rather more tasteful way of demonstrating this behaviour is <code>definition  n (oops : false) := false.rec ℕ oops</code></p>

#### [ Gabriel Ebner (Apr 09 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124832445):
<blockquote>
<p>the error seems to indicate that some generic rule for recursors has been applied without noticing that in this case it does not apply.</p>
</blockquote>
<p>You're completely right. <a href="https://github.com/leanprover/lean/blob/8f55ec4c50379c612731ced2424fd3eda0cf69a6/src/frontends/lean/elaborator.cpp#L117-L121" target="_blank" title="https://github.com/leanprover/lean/blob/8f55ec4c50379c612731ced2424fd3eda0cf69a6/src/frontends/lean/elaborator.cpp#L117-L121">https://github.com/leanprover/lean/blob/8f55ec4c50379c612731ced2424fd3eda0cf69a6/src/frontends/lean/elaborator.cpp#L117-L121</a></p>
<div class="codehilite"><pre><span></span>    <span class="k">if</span> <span class="p">(</span><span class="n">inductive</span><span class="o">::</span><span class="n">is_elim_rule</span><span class="p">(</span><span class="n">env</span><span class="p">,</span> <span class="n">n</span><span class="p">)</span> <span class="o">||</span>
        <span class="n">is_aux_recursor</span><span class="p">(</span><span class="n">env</span><span class="p">,</span> <span class="n">n</span><span class="p">)</span> <span class="o">||</span>
        <span class="n">is_user_defined_recursor</span><span class="p">(</span><span class="n">env</span><span class="p">,</span> <span class="n">n</span><span class="p">))</span> <span class="p">{</span>
        <span class="k">return</span> <span class="n">elaborator_strategy</span><span class="o">::</span><span class="n">AsEliminator</span><span class="p">;</span>
    <span class="p">}</span>
</pre></div>

#### [ Gabriel Ebner (Apr 09 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124832656):
<blockquote>
<p>I have given Lean all the information it needs</p>
</blockquote>
<p>The goal of the elaborator is not to fill in missing pieces, it is to create a type-correct expression using the pre-expression as a recipe.  The meaning of <code>false.rec _ oops</code> is <em>not</em> <code> app (app (const `false.rec [level.mvar `a]) [mvar `b]) (local_const `oops ...) </code>, it is a <em>command</em> to the elaborator, instructing it to (essentially) do an induction on <code>oops</code>.  And well, the <code>induction</code> tactic can fail even if the goal would be solvable by induction.</p>

#### [ Kevin Buzzard (Apr 09 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124832682):
<p>Do you think that I will have to learn some C++ if I want to understand Lean well enough to use it in practice?</p>

#### [ Gabriel Ebner (Apr 09 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124832743):
<p>I don't think it's necessary to know the Lean implementation or even just C++ in order to understand and use Lean.  I think I have a good mental model of how C++ or Scala work, without ever having seen their compilers.</p>

#### [ Kevin Buzzard (Apr 09 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124832748):
<p>That's a relief :-)</p>

#### [ Gabriel Ebner (Apr 09 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124832790):
<p>I think it took me about half a year to have a mental model for the Lean elaborator.  I looked into the C++ code, though.</p>

#### [ Gabriel Ebner (Apr 09 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124832798):
<p>Before that, I just added type annotations everywhere until the red squiggles went away.</p>

#### [ Kevin Buzzard (Apr 09 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124832800):
<p>My impression is that it's very difficult to get a clear idea of what the elaborator is doing without reading the source.</p>

#### [ Kevin Buzzard (Apr 09 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124832838):
<p>Currently I just add type class annotations everywhere until the red squiggles go away.</p>

#### [ Kevin Buzzard (Apr 09 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124832849):
<p>I mean, there are general principles, but to get beyond them I think you just have to look at what is actually going on.</p>

#### [ Kevin Buzzard (Apr 09 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124832892):
<p>Thanks for your help, by the way!</p>

#### [ Gabriel Ebner (Apr 09 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spot%20the%20metavariable/near/124832894):
<p>You're welcome.</p>


{% endraw %}
