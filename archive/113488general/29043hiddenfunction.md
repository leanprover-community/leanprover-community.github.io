---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/29043hiddenfunction.html
---

## Stream: [general](index.html)
### Topic: [hidden function](29043hiddenfunction.html)

---


{% raw %}
#### [ Mario Carneiro (Dec 15 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/151838238):
<p>I just noticed a very clever trick that was used in a Coq development. We can define the following function:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="kn">reducible</span><span class="o">]</span> <span class="n">def</span> <span class="n">hidden</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:=</span> <span class="n">a</span>
</pre></div>


<p>This obviously isn't a very ergonomic function to write directly, but it can be used in tactics that have to manipulate large proof states and display them to the user, without getting in the way of any automation. (I should investigate if this is an appropriate use of <code>abbreviation</code>.) For example, we could have a tactic <code>hide x</code> which <code>change</code>s the type of <code>x : T</code> to <code>x : @hidden _ T</code>. The zero arg version could just do this for all assumptions whose pp is above a certain length. The Coq example was using this when proving theorems about large programs, to hide the "rest" of the program when working one statement at a time.</p>

#### [ Mario Carneiro (Dec 15 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/151838734):
<p>demo:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="kn">reducible</span><span class="o">]</span> <span class="n">def</span> <span class="n">hidden</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:=</span> <span class="n">a</span>

<span class="kn">open</span> <span class="n">tactic</span>
<span class="n">meta</span> <span class="n">def</span> <span class="n">repl</span> <span class="o">:</span> <span class="n">expr</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">tactic</span> <span class="n">expr</span>
<span class="bp">|</span> <span class="n">e</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">do</span>
  <span class="n">t</span> <span class="err">←</span> <span class="n">infer_type</span> <span class="n">e</span><span class="o">,</span>
  <span class="n">expr</span><span class="bp">.</span><span class="n">sort</span> <span class="n">u</span> <span class="err">←</span> <span class="n">infer_type</span> <span class="n">t</span><span class="o">,</span>
  <span class="n">return</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">app</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">const</span> <span class="bp">``</span><span class="n">hidden</span> <span class="o">[</span><span class="n">u</span><span class="o">])</span> <span class="n">t</span> <span class="n">e</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">app</span> <span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">i</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="n">do</span> <span class="n">f&#39;</span> <span class="err">←</span> <span class="n">repl</span> <span class="n">f</span> <span class="o">(</span><span class="n">i</span><span class="bp">+</span><span class="mi">1</span><span class="o">),</span> <span class="n">x&#39;</span> <span class="err">←</span> <span class="n">repl</span> <span class="n">x</span> <span class="n">i</span><span class="o">,</span> <span class="n">return</span> <span class="o">(</span><span class="n">f&#39;</span> <span class="n">x&#39;</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">lam</span> <span class="n">n</span> <span class="n">b</span> <span class="n">d</span> <span class="n">e</span><span class="o">)</span> <span class="o">(</span><span class="n">i</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="n">do</span>
  <span class="n">var</span> <span class="err">←</span> <span class="n">mk_local&#39;</span> <span class="n">n</span> <span class="n">b</span> <span class="n">d</span><span class="o">,</span>
  <span class="n">e&#39;</span> <span class="err">←</span> <span class="n">repl</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">instantiate_var</span> <span class="n">e</span> <span class="n">var</span><span class="o">)</span> <span class="n">i</span><span class="o">,</span>
  <span class="n">return</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">lam</span> <span class="n">n</span> <span class="n">b</span> <span class="n">d</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">abstract_local</span> <span class="n">e&#39;</span> <span class="n">var</span><span class="bp">.</span><span class="n">local_uniq_name</span><span class="o">))</span>
<span class="bp">|</span> <span class="n">e</span> <span class="o">(</span><span class="n">i</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="n">return</span> <span class="n">e</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span><span class="bp">.</span><span class="n">elide</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">t</span> <span class="err">←</span> <span class="n">target</span><span class="o">,</span>
  <span class="n">t&#39;</span> <span class="err">←</span> <span class="n">repl</span> <span class="n">t</span> <span class="n">n</span><span class="o">,</span>
  <span class="n">tactic</span><span class="bp">.</span><span class="n">change</span> <span class="n">t&#39;</span>

<span class="kn">example</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">+</span> <span class="mi">2</span> <span class="bp">=</span> <span class="mi">4</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">dunfold</span> <span class="n">has_add</span><span class="bp">.</span><span class="n">add</span><span class="o">,</span> <span class="n">delta</span> <span class="n">nat</span><span class="bp">.</span><span class="n">add</span><span class="o">,</span>
  <span class="c1">-- ⊢ nat.brec_on 2</span>
  <span class="c1">--       (λ (a : ℕ) (_F : nat.below (λ (a : ℕ), ℕ → ℕ) a) (a_1 : ℕ),</span>
  <span class="c1">--         (λ (a a_1 : ℕ) (_F : nat.below (λ (a : ℕ), ℕ → ℕ) a_1),</span>
  <span class="c1">--             nat.cases_on a_1 (λ (_F : nat.below (λ (a : ℕ), ℕ → ℕ) 0), id_rhs ℕ a)</span>
  <span class="c1">--               (λ (a_1 : ℕ) (_F : nat.below (λ (a : ℕ), ℕ → ℕ) (nat.succ a_1)),</span>
  <span class="c1">--                 id_rhs ℕ (nat.succ ((_F.fst).fst a)))</span>
  <span class="c1">--               _F)</span>
  <span class="c1">--           a_1</span>
  <span class="c1">--           a</span>
  <span class="c1">--           _F)</span>
  <span class="c1">--       2 =</span>
  <span class="c1">--     4</span>
  <span class="n">elide</span> <span class="mi">5</span><span class="o">,</span>
  <span class="c1">-- ⊢ nat.brec_on 2 (λ (a : ℕ) (_F : nat.below (λ (a : ℕ), ℕ → ℕ) a) (a_1 : ℕ), hidden) 2 = 4</span>
  <span class="n">refl</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Dec 15 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/151839702):
<p>that's pretty cool :-)</p>

#### [ Patrick Massot (Dec 15 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/151841751):
<p>It looks pretty cool. What is the exact meaning of the numeric parameter?</p>

#### [ Mario Carneiro (Dec 15 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/151841879):
<p>it's the depth at which to start replacing subterms by <code>hidden</code></p>

#### [ Mario Carneiro (Dec 15 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/151841932):
<p>so higher means less hidden</p>

#### [ Reid Barton (Dec 30 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154049336):
<p>Would it be possible to have a version which replaces proofs by <code>proof_of P</code>, where <code>@[reducible] def proof_of (P : Prop) {p : P} := p</code></p>

#### [ Reid Barton (Dec 30 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154049346):
<p>and then maybe add some notation for <code>proof_of P</code> to match <code>\f&lt;P\f&gt;</code></p>

#### [ Reid Barton (Dec 30 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154049362):
<p>I thought that some combination of <code>pp</code> options was supposed to do this already, but I never figured out how</p>

#### [ Mario Carneiro (Dec 30 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052011):
<p>well, just replacing that on its own won't work since it's still a prop so it gets displayed as <code>_</code> anyway</p>

#### [ Reid Barton (Dec 30 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052013):
<p>Oh dang</p>

#### [ Mario Carneiro (Dec 30 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052015):
<p>but if you turn off <code>pp.proofs</code> then you can see it</p>

#### [ Mario Carneiro (Dec 30 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052068):
<p>Then again, I think tactics can change options so you could have a tactic like <code>elide</code> that turns of <code>pp.proofs</code> at the same time as the replacement</p>

#### [ Reid Barton (Dec 30 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052069):
<p>Oh, turn <em>off</em>? Okay, that's one thing that confused me</p>

#### [ Mario Carneiro (Dec 30 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052072):
<p>oh that's a good point, I forget the polarity</p>

#### [ Kenny Lau (Dec 30 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052111):
<p>and what difference does <code>reducible</code> make?</p>

#### [ Reid Barton (Dec 30 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052114):
<p>actually now I'm doubly confused</p>

#### [ Reid Barton (Dec 30 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052117):
<p>By experiment, I find that <code>set_option pp.proofs true</code> will display proofs</p>

#### [ Mario Carneiro (Dec 30 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052118):
<p>but that's the default?</p>

#### [ Reid Barton (Dec 30 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052119):
<p>Yes</p>

#### [ Reid Barton (Dec 30 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052120):
<p>That is what is confusing me</p>

#### [ Reid Barton (Dec 30 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052126):
<p>At least, that's what the autocompletion menu claims is the default. But setting it to <code>true</code> still causes proofs to be printed, and <code>false</code> causes them to be elided (which they are by default)</p>

#### [ Mario Carneiro (Dec 30 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052128):
<p>reducible doesn't matter much, but it makes these identity functions not interfere with other tactics</p>

#### [ Mario Carneiro (Dec 30 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052178):
<p>also the option description is a bit interesting -</p>
<blockquote>
<p>(pretty printer) if set to false, the type will be displayed instead of the value for every proof appearing as an argument to a function</p>
</blockquote>

#### [ Reid Barton (Dec 30 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052187):
<p>Okay, that's where I saw it. I knew I'd seen it claimed somewhere that this feature already existed</p>

#### [ Reid Barton (Dec 30 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052246):
<p>Maybe there are like... two options with the same name or something</p>

#### [ Mario Carneiro (Dec 30 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052297):
<p>I think the description is outdated... it used to do that and I recall lobbying for the <code>_</code> behavior</p>

#### [ Mario Carneiro (Dec 30 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052301):
<p>I'm not sure if the type display thing was removed or replaced</p>

#### [ Mario Carneiro (Dec 30 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052308):
<p>at least in the original version it just put the type instead of the proof and it was really confusing because it wasn't typecorrect</p>

#### [ Mario Carneiro (Dec 30 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052357):
<p>looking at the code, I see no evidence that it does anything other than put <code>_</code> in places, and only when <code>pp.proofs = false</code></p>

#### [ Reid Barton (Dec 30 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052437):
<p>I see. That does sound confusing, if there was nothing distinguishing the types of proofs from actual terms</p>

#### [ Mario Carneiro (Dec 30 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052486):
<p>but I still can't figure out how the default turns out to be <code>false</code>, the code says it's <code>true</code></p>

#### [ Kenny Lau (Dec 30 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052595):
<p>truth is an illusion</p>

#### [ Gabriel Ebner (Dec 30 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052597):
<p>There is no constant default: <span class="emoji emoji-263a" title="smile">:smile:</span> <a href="https://github.com/leanprover/lean/blob/30d883efef422facab3bf351d9fcff90c943298f/src/frontends/lean/pp.cpp#L1911-L1917" target="_blank" title="https://github.com/leanprover/lean/blob/30d883efef422facab3bf351d9fcff90c943298f/src/frontends/lean/pp.cpp#L1911-L1917">https://github.com/leanprover/lean/blob/30d883efef422facab3bf351d9fcff90c943298f/src/frontends/lean/pp.cpp#L1911-L1917</a></p>

#### [ Mario Carneiro (Dec 30 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052639):
<p>wtf is that special case</p>

#### [ Mario Carneiro (Dec 30 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052649):
<p>so sneaky</p>

#### [ Mario Carneiro (Dec 30 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hidden%20function/near/154052693):
<p>I guess this is so that <code>#print theorem</code> doesn't show <code>theorem thm : T := _</code> which would not be nice</p>


{% endraw %}
