---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/23412Derivinghypothesisfromifstatements.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Deriving hypothesis from if statements](https://leanprover-community.github.io/archive/113489newmembers/23412Derivinghypothesisfromifstatements.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Tobias Grosser (Oct 02 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056007):
<p>Hi, I am currently cleaning up my gaussian elimination proof. At one point I defined the following functions:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">fin_first</span> <span class="o">{</span><span class="n">n</span> <span class="n">m</span><span class="o">}</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="n">m</span><span class="o">))</span> <span class="o">{</span><span class="n">h</span><span class="o">:</span> <span class="n">i</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&lt;</span> <span class="n">n</span><span class="o">}:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="n">i</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="k">begin</span> <span class="n">apply</span> <span class="n">h</span> <span class="kn">end</span><span class="bp">⟩</span>

<span class="n">def</span> <span class="n">fin_second</span> <span class="o">{</span><span class="n">n</span> <span class="n">m</span><span class="o">}</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="n">m</span><span class="o">))</span> <span class="o">{</span><span class="n">h</span><span class="o">:</span> <span class="n">i</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&gt;=</span> <span class="n">n</span><span class="o">}:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">m</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="n">i</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">-</span> <span class="n">n</span><span class="o">,</span> <span class="k">begin</span> <span class="n">sorry</span> <span class="kn">end</span><span class="bp">⟩</span>

<span class="n">def</span> <span class="n">block_mx</span> <span class="o">{</span><span class="n">m_down</span> <span class="n">m_up</span> <span class="n">n_left</span> <span class="n">n_right</span><span class="o">:</span> <span class="n">nat</span><span class="o">}</span> <span class="o">:</span>
  <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m_up</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n_left</span><span class="o">)</span> <span class="n">α</span> <span class="bp">→</span>
  <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m_up</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n_right</span><span class="o">)</span> <span class="n">α</span> <span class="bp">→</span>
  <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m_down</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n_left</span><span class="o">)</span> <span class="n">α</span> <span class="bp">→</span>
  <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m_down</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n_right</span><span class="o">)</span> <span class="n">α</span> <span class="bp">→</span>
  <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">m_up</span> <span class="bp">+</span> <span class="n">m_down</span><span class="o">))</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">n_left</span> <span class="bp">+</span> <span class="n">n_right</span><span class="o">))</span> <span class="n">α</span>
<span class="bp">|</span> <span class="n">up_left</span> <span class="n">up_right</span> <span class="n">down_left</span> <span class="n">down_right</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">i</span> <span class="n">j</span><span class="o">,</span>
 <span class="k">if</span> <span class="n">i</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&lt;</span> <span class="n">m_up</span>
 <span class="k">then</span>
    <span class="k">if</span> <span class="n">j</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&lt;</span> <span class="n">n_left</span>
    <span class="k">then</span>
      <span class="n">up_left</span> <span class="o">(</span><span class="n">fin_first</span> <span class="n">i</span><span class="o">)</span> <span class="o">(</span><span class="n">fin_first</span> <span class="n">j</span><span class="o">)</span>
    <span class="k">else</span>
      <span class="n">up_right</span> <span class="o">(</span><span class="n">fin_first</span> <span class="n">i</span><span class="o">)</span> <span class="o">(</span><span class="n">fin_second</span> <span class="n">j</span><span class="o">)</span>
  <span class="k">else</span>
   <span class="k">if</span> <span class="n">j</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&lt;</span> <span class="n">n_left</span>
    <span class="k">then</span>
      <span class="n">down_left</span> <span class="o">(</span><span class="n">fin_second</span> <span class="n">i</span><span class="o">)</span>  <span class="o">(</span><span class="n">fin_first</span> <span class="n">j</span><span class="o">)</span>
    <span class="k">else</span>
      <span class="n">down_right</span> <span class="o">(</span><span class="n">fin_second</span> <span class="n">i</span><span class="o">)</span> <span class="o">(</span><span class="n">fin_second</span> <span class="n">j</span><span class="o">)</span>
<span class="bp">```</span> <span class="n">app</span>

<span class="n">Whenever</span> <span class="n">I</span> <span class="n">apply</span> <span class="n">fin_first</span> <span class="n">and</span> <span class="n">fin_second</span><span class="o">,</span> <span class="n">I</span> <span class="n">would</span> <span class="n">like</span> <span class="n">to</span> <span class="n">make</span> <span class="n">the</span> <span class="kn">hypothesis</span> <span class="s2">&quot;h&quot;</span> <span class="n">available</span> <span class="n">based</span> <span class="n">on</span> <span class="n">the</span> <span class="n">information</span> <span class="k">in</span> <span class="n">the</span> <span class="k">if</span><span class="bp">-</span><span class="n">condition</span><span class="bp">.</span>
</pre></div>

#### [ Tobias Grosser (Oct 02 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056162):
<p>I feel this is a super trivial question, but I did not find a good example googling for it. Can somebody throw me the right keywords / reference?</p>

#### [ Rob Lewis (Oct 02 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056304):
<p>If you write <code>if h :  j.val &lt; n_left then _ else _</code> you'll get local hypotheses with the right types in the placeholders.</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056328):
<div class="codehilite"><pre><span></span><span class="n">test</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="mi">25</span><span class="o">:</span><span class="mi">29</span><span class="o">:</span> <span class="n">error</span>

<span class="n">don&#39;t</span> <span class="n">know</span> <span class="n">how</span> <span class="n">to</span> <span class="n">synthesize</span> <span class="n">placeholder</span>
<span class="kn">context</span><span class="o">:</span>
<span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">,</span>
<span class="n">m_down</span> <span class="n">m_up</span> <span class="n">n_left</span> <span class="n">n_right</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
<span class="n">block_mx</span> <span class="o">:</span>
  <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m_up</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n_left</span><span class="o">)</span> <span class="n">α</span> <span class="bp">→</span>
  <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m_up</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n_right</span><span class="o">)</span> <span class="n">α</span> <span class="bp">→</span>
  <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m_down</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n_left</span><span class="o">)</span> <span class="n">α</span> <span class="bp">→</span>
  <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m_down</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n_right</span><span class="o">)</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">m_up</span> <span class="bp">+</span> <span class="n">m_down</span><span class="o">))</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">n_left</span> <span class="bp">+</span> <span class="n">n_right</span><span class="o">))</span> <span class="n">α</span><span class="o">,</span>
<span class="n">up_left</span> <span class="o">:</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m_up</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n_left</span><span class="o">)</span> <span class="n">α</span><span class="o">,</span>
<span class="n">up_right</span> <span class="o">:</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m_up</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n_right</span><span class="o">)</span> <span class="n">α</span><span class="o">,</span>
<span class="n">down_left</span> <span class="o">:</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m_down</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n_left</span><span class="o">)</span> <span class="n">α</span><span class="o">,</span>
<span class="n">down_right</span> <span class="o">:</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m_down</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n_right</span><span class="o">)</span> <span class="n">α</span><span class="o">,</span>
<span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">m_up</span> <span class="bp">+</span> <span class="n">m_down</span><span class="o">),</span>
<span class="n">j</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n_left</span> <span class="bp">+</span> <span class="n">n_right</span><span class="o">),</span>
<span class="n">h</span> <span class="o">:</span> <span class="n">j</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&lt;</span> <span class="n">n_left</span>
<span class="err">⊢</span> <span class="n">j</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&lt;</span> <span class="n">n_left</span>
</pre></div>

#### [ Tobias Grosser (Oct 02 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056374):
<p>I seem to be so close.</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056407):
<p>I would hope lean picks this from the context. But it does not seem to do so.</p>

#### [ Patrick Massot (Oct 02 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056461):
<p><a href="https://leanprover.github.io/theorem_proving_in_lean/type_classes.html?highlight=dite#decidable-propositions" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/type_classes.html?highlight=dite#decidable-propositions">https://leanprover.github.io/theorem_proving_in_lean/type_classes.html?highlight=dite#decidable-propositions</a></p>

#### [ Rob Lewis (Oct 02 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056479):
<p>You want Lean to fill in those arguments automatically when it finds them in the local context?</p>

#### [ Rob Lewis (Oct 02 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056539):
<p>You can write <code>def fin_first {n m} (i : fin (n + m)) {h: i.val &lt; n . assumption}: fin (n)</code></p>

#### [ Rob Lewis (Oct 02 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056555):
<p>(I think that's the right syntax, don't have Lean open right this second to check.)</p>

#### [ Patrick Massot (Oct 02 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056569):
<p>binders in <code>def fin_first {n m} (i : fin (n + m)) {h: i.val &lt; n}: fin (n)</code> are a bit strange, how <code>h</code> could be inferred from the explicit arguments?</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056585):
<p>I have no idea what I am doing here.</p>

#### [ Patrick Massot (Oct 02 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056588):
<p>Of course Rob's solution should work in your use case</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056601):
<p>I hoped "{" and "}" would create a "free" argument</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056610):
<p>Which would be filled in if available in the local context.</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056664):
<p>Rob suggested to use "assumption", right?</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056695):
<p>This gives:</p>
<div class="codehilite"><pre><span></span><span class="n">test</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="mi">7</span><span class="o">:</span><span class="mi">52</span><span class="o">:</span> <span class="n">error</span>

<span class="n">invalid</span> <span class="n">declaration</span><span class="o">,</span> <span class="err">&#39;</span><span class="o">}</span><span class="err">&#39;</span> <span class="n">expected</span>
<span class="n">test</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="mi">7</span><span class="o">:</span><span class="mi">55</span><span class="o">:</span> <span class="n">error</span>

<span class="n">command</span> <span class="n">expected</span>
</pre></div>

#### [ Tobias Grosser (Oct 02 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056704):
<p>Will  ook for assumption in the lean doc</p>

#### [ Rob Lewis (Oct 02 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056711):
<p>{ } creates implicit arguments. They're arguments that can be filled in completely from other arguments, basically. Lean won't automatically search your local context for matches, because (1) there could be tons of stuff in the context, and (2) there could be multiple matches there.</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056784):
<p>I see. How do I tell lean which matches I want? Should I use ! to make the parameters explicit and then provide the ones needed explicitly?</p>

#### [ Rob Lewis (Oct 02 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056795):
<p>Here's the correct syntax for using auto parameters like my suggestion:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">f</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">1</span> <span class="bp">.</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">assumption</span><span class="o">)</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span> <span class="n">trivial</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span>
<span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">1</span> <span class="k">then</span> <span class="n">f</span> <span class="n">n</span> <span class="k">else</span> <span class="n">trivial</span>
</pre></div>

#### [ Rob Lewis (Oct 02 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135056932):
<p>With auto parameters, you give a tactic that will be executed to fill in that argument. So using <code>tactic.assumption</code> with an auto param will try to find something in the context that will work.</p>

#### [ Rob Lewis (Oct 02 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057019):
<blockquote>
<p>I see. How do I tell lean which matches I want? Should I use ! to make the parameters explicit and then provide the ones needed explicitly?</p>
</blockquote>
<p>I'm not sure exactly what you mean. It's usually clear in a signature which arguments are inferrable from others, assuming the declaration is fully applied. The custom is to make as much implicit as you can.</p>

#### [ Rob Lewis (Oct 02 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057088):
<p>There's no ! syntax anymore, that was only in Lean 2. But you can use placeholders <code>_</code> to ask the elaborator to fill in explicit arguments.</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057250):
<p>Great.</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057251):
<p>I got this working.</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057301):
<p>I previously used "{}" around the assumption tactic, but I need to use "()"</p>

#### [ Rob Lewis (Oct 02 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057335):
<p>Great! Sorry, I should have checked before I wrote it with {}, heh.</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057408):
<p>These seem to be really basic questions, but I have now only a last issue.</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057411):
<p>h_j : ¬j.val &lt; n_left<br>
⊢ j.val ≥ n_left</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057416):
<p>Is what I see in the else branch.</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057421):
<p>This seems to be an obvious rewrite.</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057431):
<p>Unfortunately, I don't understand where I would even insert my tactic to do the rewrite.</p>

#### [ Rob Lewis (Oct 02 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057433):
<p><code>le_of_not_gt</code></p>

#### [ Patrick Massot (Oct 02 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057443):
<p>No you need a lemma here</p>

#### [ Patrick Massot (Oct 02 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057446):
<p>Yes, that lemma</p>

#### [ Rob Lewis (Oct 02 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057473):
<p>Are you using the auto param trick? Because I see that this might complicate things a bit.</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057563):
<p>I currently write "up_right (fin_first i) (fin_second j (begin rw of_not_gt at h_j end))"</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057567):
<div class="codehilite"><pre><span></span><span class="n">up_right</span> <span class="o">(</span><span class="n">fin_first</span> <span class="n">i</span><span class="o">)</span> <span class="o">(</span><span class="n">fin_second</span> <span class="n">j</span> <span class="o">(</span><span class="k">begin</span> <span class="n">rw</span> <span class="n">of_not_gt</span> <span class="n">at</span> <span class="n">h_j</span> <span class="kn">end</span><span class="o">))</span>
</pre></div>

#### [ Tobias Grosser (Oct 02 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057621):
<p>Which seems to not type-check even syntactically.</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057635):
<p>I feel I mix proofs and normal programs beyond what is reasonable.</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057762):
<p>Also, as a lemma I seem to need "ge_of_not_lt", but I can fix this.</p>

#### [ Patrick Massot (Oct 02 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057808):
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">tobias</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="bp">`</span><span class="o">[</span><span class="n">apply</span> <span class="n">le_of_not_gt</span><span class="o">,</span>  <span class="n">assumption</span><span class="o">]</span> <span class="bp">&lt;|&gt;</span>  <span class="bp">`</span><span class="o">[</span><span class="n">assumption</span><span class="o">]</span>

<span class="n">def</span> <span class="n">f</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">≤</span> <span class="mi">1</span> <span class="bp">.</span> <span class="n">tobias</span><span class="o">)</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span> <span class="n">trivial</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span>
<span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="bp">¬</span> <span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">1</span> <span class="k">then</span> <span class="n">f</span> <span class="n">n</span> <span class="k">else</span> <span class="n">trivial</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span>
<span class="k">if</span> <span class="n">h</span> <span class="o">:</span>  <span class="n">n</span> <span class="bp">≤</span> <span class="mi">1</span> <span class="k">then</span> <span class="n">f</span> <span class="n">n</span> <span class="k">else</span> <span class="n">trivial</span>
</pre></div>

#### [ Rob Lewis (Oct 02 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057878):
<p>Haha, you beat me to it, I just wrote almost exactly the same thing.</p>

#### [ Patrick Massot (Oct 02 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057900):
<p>And my daughter tried to help you</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057932):
<p>This is very much appreciated!</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057944):
<p>The full family working on lean!</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135057963):
<p>What I understand is that I can only provide tactics at function definition, not at the call-site.</p>

#### [ Rob Lewis (Oct 02 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058030):
<p>Oh, you can certainly provide them at the call site too.</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058039):
<p>In this case, I could just change the hypothesis of fin_second to what I want.</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058056):
<p>I tried to avoid this, as I felt the hypothesis that I stated is more canonical.</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058066):
<p>Cool so how would I add them to the call site?</p>

#### [ Patrick Massot (Oct 02 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058097):
<p>I meant my daughter tried to help Rob winning the race</p>

#### [ Rob Lewis (Oct 02 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058115):
<p>If you make the inequality hypotheses to <code>fin_first</code> and <code>fin_second</code> explicit arguments, using <code>(h : i.val &lt; n)</code>, then you can apply it using <code>fin_first i (by assumption)</code>.</p>

#### [ Rob Lewis (Oct 02 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058182):
<p>Or <code>by tobias</code> in this case.</p>

#### [ Patrick Massot (Oct 02 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058314):
<p>More seriously, the basics of implicit arguments goes like this: say you have a lemma (or function) with arguments <code>(f : a -&gt; b) (hf : continuous f)</code>. Then having <code>hf</code> forces the value of <code>f</code>, so you can mark <code>f</code> as implicit by changing the declaration to <code>{f : a -&gt; b} (hf : continuous f)</code>. This was you can provide only <code>hf</code> when applying the lemma and Lean will figure out <code>f</code>. In your case Lean had no hope to figure out <code>h</code> from other arguments so you need to keep it explicit, or use auto-param like in Rob's solution.</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058479):
<p>I see.</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058485):
<p>Got it.</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058505):
<p>I can now successfully forward the hypothesis.</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058510):
<p>Thanks again, I learned sth new.</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058568):
<p>For completeness, this is how my code looks like:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">ring_theory</span><span class="bp">.</span><span class="n">matrix</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">n</span> <span class="n">m</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">n</span><span class="o">]</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">m</span><span class="o">]</span>

<span class="n">local</span> <span class="kn">infixl</span> <span class="bp">`</span> <span class="bp">*</span><span class="err">ₘ</span> <span class="bp">`</span> <span class="o">:</span> <span class="mi">70</span> <span class="o">:=</span> <span class="n">matrix</span><span class="bp">.</span><span class="n">mul</span>

<span class="n">def</span> <span class="n">fin_first</span> <span class="o">{</span><span class="n">n</span> <span class="n">m</span><span class="o">}</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="n">m</span><span class="o">))</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">i</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="o">):</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="n">i</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="k">begin</span> <span class="n">apply</span> <span class="n">h</span> <span class="kn">end</span><span class="bp">⟩</span>

<span class="n">def</span> <span class="n">fin_second</span> <span class="o">{</span><span class="n">n</span> <span class="n">m</span><span class="o">}</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="n">m</span><span class="o">))</span> <span class="o">(</span><span class="n">h</span><span class="o">:</span> <span class="n">i</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&gt;=</span> <span class="n">n</span><span class="o">):</span> <span class="n">fin</span> <span class="o">(</span><span class="n">m</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="n">i</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">-</span> <span class="n">n</span><span class="o">,</span> <span class="n">sorry</span><span class="bp">⟩</span>

<span class="n">def</span> <span class="n">block_mx</span> <span class="o">{</span><span class="n">m_down</span> <span class="n">m_up</span> <span class="n">n_left</span> <span class="n">n_right</span><span class="o">:</span> <span class="n">nat</span><span class="o">}</span> <span class="o">:</span>
  <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m_up</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n_left</span><span class="o">)</span> <span class="n">α</span> <span class="bp">→</span>
  <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m_up</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n_right</span><span class="o">)</span> <span class="n">α</span> <span class="bp">→</span>
  <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m_down</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n_left</span><span class="o">)</span> <span class="n">α</span> <span class="bp">→</span>
  <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m_down</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n_right</span><span class="o">)</span> <span class="n">α</span> <span class="bp">→</span>
  <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">m_up</span> <span class="bp">+</span> <span class="n">m_down</span><span class="o">))</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">n_left</span> <span class="bp">+</span> <span class="n">n_right</span><span class="o">))</span> <span class="n">α</span>
<span class="bp">|</span> <span class="n">up_left</span> <span class="n">up_right</span> <span class="n">down_left</span> <span class="n">down_right</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">i</span> <span class="n">j</span><span class="o">,</span>
 <span class="k">if</span> <span class="n">h_i</span><span class="o">:</span> <span class="n">i</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&lt;</span> <span class="n">m_up</span>
 <span class="k">then</span>
    <span class="k">if</span> <span class="n">h_j</span><span class="o">:</span> <span class="n">j</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&lt;</span> <span class="n">n_left</span>
    <span class="k">then</span>
      <span class="n">up_left</span> <span class="o">(</span><span class="n">fin_first</span> <span class="n">i</span> <span class="o">(</span><span class="k">by</span> <span class="n">assumption</span><span class="o">))</span> <span class="o">(</span><span class="n">fin_first</span> <span class="n">j</span> <span class="o">(</span><span class="k">by</span> <span class="n">assumption</span><span class="o">))</span>
    <span class="k">else</span>
      <span class="n">up_right</span> <span class="o">(</span><span class="n">fin_first</span> <span class="n">i</span> <span class="o">(</span><span class="k">by</span> <span class="n">assumption</span><span class="o">))</span> <span class="o">(</span><span class="n">fin_second</span> <span class="n">j</span> <span class="o">(</span><span class="k">by</span> <span class="n">apply</span> <span class="n">le_of_not_gt</span><span class="bp">;</span> <span class="n">assumption</span><span class="o">))</span>
  <span class="k">else</span>
   <span class="k">if</span> <span class="n">h_j</span><span class="o">:</span> <span class="n">j</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&lt;</span> <span class="n">n_left</span>
    <span class="k">then</span>
      <span class="n">down_left</span> <span class="o">(</span><span class="n">fin_second</span> <span class="n">i</span> <span class="o">(</span><span class="k">by</span> <span class="n">apply</span> <span class="n">le_of_not_gt</span><span class="bp">;</span> <span class="n">assumption</span><span class="o">))</span>  <span class="o">(</span><span class="n">fin_first</span> <span class="n">j</span> <span class="o">(</span><span class="k">by</span> <span class="n">assumption</span><span class="o">))</span>
    <span class="k">else</span>
      <span class="n">down_right</span> <span class="o">(</span><span class="n">fin_second</span> <span class="n">i</span> <span class="o">(</span><span class="k">by</span> <span class="n">apply</span> <span class="n">le_of_not_gt</span><span class="bp">;</span> <span class="n">assumption</span><span class="o">))</span> <span class="o">(</span><span class="n">fin_second</span> <span class="n">j</span> <span class="o">(</span><span class="k">by</span> <span class="n">apply</span> <span class="n">le_of_not_gt</span><span class="bp">;</span> <span class="n">assumption</span><span class="o">))</span>
</pre></div>

#### [ Rob Lewis (Oct 02 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058597):
<p>It's not that common to use auto params, but this is actually a pretty good application. <code>linarith</code> would be a reasonable auto param too if it handled negations of inequalities.</p>

#### [ Patrick Massot (Oct 02 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058621):
<p>I can feel the approximate SMT solver temptation here</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058629):
<p>:D</p>

#### [ Patrick Massot (Oct 02 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058649):
<p><a href="#narrow/stream/113488-general/subject/linarith.20.26.20nat/near/134919571" title="#narrow/stream/113488-general/subject/linarith.20.26.20nat/near/134919571">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/linarith.20.26.20nat/near/134919571</a></p>

#### [ Tobias Grosser (Oct 02 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058650):
<p>I certainly would like to explore more powerful linarithmetic tactics here. But this is a separate discussion.</p>

#### [ Tobias Grosser (Oct 02 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135058720):
<p>I know, we have a solver for full Presburger arithmetic based on dual simplex. Eventually, this is what I would like to understand if we can make it work in lean.</p>

#### [ Rob Lewis (Oct 02 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135061274):
<blockquote>
<p>I can feel the approximate SMT solver temptation here</p>
</blockquote>
<p><a href="https://github.com/leanprover/mathlib/pull/384" target="_blank" title="https://github.com/leanprover/mathlib/pull/384">https://github.com/leanprover/mathlib/pull/384</a></p>

#### [ Tobias Grosser (Oct 03 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135087439):
<p>Amazing. This got even merged already. Will try to use it.</p>

#### [ Tobias Grosser (Oct 03 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135087599):
<p>I fact, i tried to use it already and it did not work. Thought I need to dig deeper, but then I found this in the tactic description:  "In particular, it will not work on nat."</p>

#### [ Tobias Grosser (Oct 03 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135087622):
<p>Seems that's a problem in my case. Any reason why it would not work?</p>

#### [ Rob Lewis (Oct 03 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Deriving%20hypothesis%20from%20if%20statements/near/135089959):
<p>Oops, I guess the description is outdated. It will work on <code>nat</code>, but it isn't complete (it's just doing Fourier Motzkin elimination). It also doesn't know about nat subtraction, which could be a problem in your case.</p>


{% endraw %}
