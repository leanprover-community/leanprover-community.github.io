---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/60427Whydoesntdectrivialsolveprime3.html
---

## Stream: [new members](index.html)
### Topic: [Why doesn't dec_trivial solve `prime 3`?](60427Whydoesntdectrivialsolveprime3.html)

---


{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Oct 24 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136416609):
<p>In <code>prime.lean</code>, the following statements are made:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">prime_two</span> <span class="o">:</span> <span class="n">prime</span> <span class="mi">2</span> <span class="o">:=</span> <span class="n">dec_trivial</span>
<span class="kn">theorem</span> <span class="n">prime_three</span> <span class="o">:</span> <span class="n">prime</span> <span class="mi">3</span> <span class="o">:=</span> <span class="n">dec_trivial</span>
</pre></div>


<p>And both work. However if I reproduce the same code on another lean file, e.g.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">prime</span>

<span class="kn">open</span> <span class="n">nat</span>

<span class="kn">theorem</span> <span class="n">prime_two</span> <span class="o">:</span> <span class="n">prime</span> <span class="mi">2</span> <span class="o">:=</span> <span class="n">dec_trivial</span>
<span class="kn">theorem</span> <span class="n">prime_three</span> <span class="o">:</span> <span class="n">prime</span> <span class="mi">3</span> <span class="o">:=</span> <span class="n">dec_trivial</span>
</pre></div>


<p>Only <code>prime_two</code> works. What's going on?</p>

#### [ Bryan Gin-ge Chen (Oct 24 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136417706):
<p>The crucial line in <code>data.nat.prime</code> seems to be <code>local attribute [instance] decidable_prime_1</code>. If you include that, then <code>prime_three</code> works.</p>

#### [ Bryan Gin-ge Chen (Oct 24 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136417744):
<p>I guess what's initially surprising is how lean knows <code>prime 2</code> is decidable without that instance.</p>

#### [ Bryan Gin-ge Chen (Oct 24 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136417839):
<p><code>decidable_prime_1</code> just says: </p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">decidable_prime_1</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">prime</span> <span class="n">p</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">decidable_of_iff&#39;</span> <span class="bp">_</span> <span class="n">prime_def_lt&#39;</span>
</pre></div>

#### [ Bryan Gin-ge Chen (Oct 24 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136418233):
<p>Here's the definition of <code>prime</code>:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">prime</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:=</span> <span class="n">p</span> <span class="bp">≥</span> <span class="mi">2</span> <span class="bp">∧</span> <span class="bp">∀</span> <span class="n">m</span> <span class="err">∣</span> <span class="n">p</span><span class="o">,</span> <span class="n">m</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">∨</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">p</span>
</pre></div>


<p>and here's the type of <code>prime_def_lt</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">prime_def_lt&#39;</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="n">prime</span> <span class="n">p</span> <span class="bp">↔</span> <span class="n">p</span> <span class="bp">≥</span> <span class="mi">2</span> <span class="bp">∧</span> <span class="bp">∀</span> <span class="n">m</span><span class="o">,</span> <span class="mi">2</span> <span class="bp">≤</span> <span class="n">m</span> <span class="bp">→</span> <span class="n">m</span> <span class="bp">&lt;</span> <span class="n">p</span> <span class="bp">→</span> <span class="bp">¬</span> <span class="n">m</span> <span class="err">∣</span> <span class="n">p</span>
</pre></div>


<p>When <code>p=2</code> it's obvious to lean that <code>prime p</code> is decidable, but when <code>p &gt; 2</code> it needs the extra hint that you only need to check <code>m &lt; p</code>.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 24 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136418284):
<p>Ah ok. Interestingly if the file contains <code>local attribute [instance] classical.prop_decidable</code> (and not <code>nat.decidable_prime_1</code>), then even <code>prime 2</code> gets messed up.</p>

#### [ Bryan Gin-ge Chen (Oct 24 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136418800):
<p>Yes, that makes sense. I don't think <code>dec_trivial</code> can do very much for you when every proposition is declared to be decidable.</p>

#### [ Kevin Buzzard (Oct 24 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136425801):
<p>If every proposition is declared to be decidable, but you still want to use <code>dec_trivial</code>, the trick is <code>local attribute [instance, priority 0] classical.prop_decidable</code></p>

#### [ Kevin Buzzard (Oct 24 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136425868):
<p>Then the "fake" decidabilty is always used after the "real" one, if a real one can be found.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 24 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136425939):
<blockquote>
<p>If every proposition is declared to be decidable, but you still want to use <code>dec_trivial</code>, the trick is <code>local attribute [instance, priority 0] classical.prop_decidable</code></p>
</blockquote>
<p>Yeah, I know that -- but I don't get why exactly it is that the fake decidability isn't enough for dec_trivial.</p>

#### [ Kenny Lau (Oct 24 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136426003):
<p>because it uses <code>choice</code> and the VM can't evaluate <code>choice</code></p>

#### [ Kevin Buzzard (Oct 24 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136426010):
<p>fake decidability just confuses <code>dec_trivial</code>. We saw another instance of <code>dec_trivial</code> getting confused in the <code>even</code> thread a week or so ago. I am very much not an expert in these matters, but it's something to do with what the VM does</p>

#### [ Kenny Lau (Oct 24 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136426012):
<p><code>decidable</code> isn't a Prop, it's data</p>

#### [ Kevin Buzzard (Oct 24 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136426014):
<p>what Kenny said</p>

#### [ Kevin Buzzard (Oct 24 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136426117):
<p>Yeah. I don't understand this properly. I don't even really know what the kernel and the VM are. I suspect that this might be quite a good way of learning what the difference is between them.</p>

#### [ Kevin Buzzard (Oct 24 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136426264):
<p><code>decidable blah</code> usually encodes some sort of way of computing whether blah is true or false. But if you make a random instance of it using classical mathematics then the algorithm isn't actually there. What does the kernel think of this situation? What about the VM?</p>

#### [ Kevin Buzzard (Oct 24 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136426305):
<p>What would happen if there were no VM? The kernel does all the typechecking, right? Why do we even need the VM?</p>

#### [ Kevin Buzzard (Oct 24 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136426361):
<p>Sorry for my dumb questions -- given that we are on the "new members" stream I figure they would be OK.</p>

#### [ Chris Hughes (Oct 24 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136426424):
<p>The VM is faster than the kernel. This is useful for executing tactics.</p>

#### [ Reid Barton (Oct 24 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136426930):
<blockquote>
<blockquote>
<p>If every proposition is declared to be decidable, but you still want to use <code>dec_trivial</code>, the trick is <code>local attribute [instance, priority 0] classical.prop_decidable</code></p>
</blockquote>
<p>Yeah, I know that -- but I don't get why exactly it is that the fake decidability isn't enough for dec_trivial.</p>
</blockquote>
<p>The idea behind <code>dec_trivial</code> is basically that the value of type <code>decidable P</code> given by the instance is going to reduce to either <code>is_false p</code> (where <code>p : not P</code>) or <code>is_true p</code> (where <code>p : P</code>). But if you use an axiom to define the instance, like <code>classical.prop_decidable</code> does, then that axiom won't be reducible.</p>

#### [ Reid Barton (Oct 24 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136426949):
<p>I <em>think</em> the VM is actually not involved here. But some things about <code>dec_trivial</code> still confuse me.</p>

#### [ Reid Barton (Oct 24 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136427170):
<p>(Like why do we need this tactic <code>meta def triv : tactic unit := mk_const `trivial &gt;&gt;= exact</code>? Could we just have defined <code>notation `dec_trivial` := of_as_true trivial</code>?)</p>

#### [ Reid Barton (Oct 24 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136427226):
<p>Maybe this is the <code>by exact</code> trick to defer type checking a term, in the hopes that its expected type will be known later?</p>

#### [ Bryan Gin-ge Chen (Oct 24 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136427709):
<p>I'm intrigued. I've never heard of the <code>by exact</code> trick. Where (else) is it used?</p>

#### [ Reid Barton (Oct 24 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136427741):
<p>whenever Lean is being dumb</p>

#### [ Reid Barton (Oct 24 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136427796):
<p>that is to say, I don't really understand when or why it works--I have used it successfully once or twice though</p>

#### [ Reid Barton (Oct 24 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136427913):
<p>I guess something like: if there is a subterm which should type check, but Lean is rejecting it, and there are metavariables in its expected type, then maybe wrapping the subterm in <code>by exact</code> will cause those metavariables to be solved for earlier relative to Lean trying to check the subterm</p>

#### [ Reid Barton (Oct 24 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136427965):
<p>I think it's the kind of thing which only crops up in situations which are a bit complicated</p>

#### [ Bryan Gin-ge Chen (Oct 24 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136428220):
<p>I did a search for "<code>by exact</code>" in mathlib and it looks like <a href="https://github.com/leanprover/mathlib/blob/fedee9835e73df24a367163e87c9c70284acf4f2/set_theory/cardinal.lean#L309" target="_blank" title="https://github.com/leanprover/mathlib/blob/fedee9835e73df24a367163e87c9c70284acf4f2/set_theory/cardinal.lean#L309">there's a concrete example</a> in <code>set_theory/cardinal.lean</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">add_one_le_succ</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="n">cardinal</span><span class="o">)</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">≤</span> <span class="n">succ</span> <span class="n">c</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">refine</span> <span class="n">quot</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">c</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">α</span><span class="o">,</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="n">lt_succ_self</span> <span class="n">c</span><span class="o">),</span>
  <span class="n">refine</span> <span class="n">quot</span><span class="bp">.</span><span class="n">induction_on</span> <span class="o">(</span><span class="n">succ</span> <span class="o">(</span><span class="n">quot</span><span class="bp">.</span><span class="n">mk</span> <span class="n">setoid</span><span class="bp">.</span><span class="n">r</span> <span class="n">α</span><span class="o">))</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">β</span> <span class="n">h</span><span class="o">,</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">cases</span> <span class="n">h</span><span class="bp">.</span><span class="n">left</span> <span class="k">with</span> <span class="n">f</span><span class="o">,</span>
  <span class="k">have</span> <span class="o">:</span> <span class="bp">¬</span> <span class="n">surjective</span> <span class="n">f</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">hn</span><span class="o">,</span>
    <span class="n">ne_of_lt</span> <span class="n">h</span> <span class="o">(</span><span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span> <span class="bp">⟨</span><span class="n">equiv</span><span class="bp">.</span><span class="n">of_bijective</span> <span class="bp">⟨</span><span class="n">f</span><span class="bp">.</span><span class="n">inj</span><span class="o">,</span> <span class="n">hn</span><span class="bp">⟩⟩</span><span class="o">),</span>
  <span class="n">cases</span> <span class="n">classical</span><span class="bp">.</span><span class="n">not_forall</span><span class="bp">.</span><span class="mi">1</span> <span class="n">this</span> <span class="k">with</span> <span class="n">b</span> <span class="n">nex</span><span class="o">,</span>
  <span class="n">refine</span> <span class="bp">⟨⟨</span><span class="n">sum</span><span class="bp">.</span><span class="n">rec</span> <span class="o">(</span><span class="k">by</span> <span class="n">exact</span> <span class="n">f</span><span class="o">)</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">_⟩⟩</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">b</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">intros</span> <span class="n">a</span> <span class="n">b</span> <span class="n">h</span><span class="o">,</span> <span class="n">rcases</span> <span class="n">a</span> <span class="k">with</span> <span class="n">a</span><span class="bp">|⟨⟨⟨⟩⟩⟩;</span> <span class="n">rcases</span> <span class="n">b</span> <span class="k">with</span> <span class="n">b</span><span class="bp">|⟨⟨⟨⟩⟩⟩</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">rw</span> <span class="n">f</span><span class="bp">.</span><span class="n">inj</span> <span class="n">h</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">exact</span> <span class="n">nex</span><span class="bp">.</span><span class="n">elim</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">exact</span> <span class="n">nex</span><span class="bp">.</span><span class="n">elim</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">h</span><span class="bp">.</span><span class="n">symm</span><span class="bp">⟩</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">refl</span> <span class="o">}</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>


<p>Removing <code>by exact</code> from the line <code>refine ⟨⟨sum.rec (by exact f) _, _⟩⟩,</code> causes lean to complain:</p>
<div class="codehilite"><pre><span></span><span class="n">type</span> <span class="n">mismatch</span> <span class="n">at</span> <span class="n">application</span>
  <span class="n">sum</span><span class="bp">.</span><span class="n">rec</span> <span class="err">⇑</span><span class="n">f</span>
<span class="n">term</span>
  <span class="err">⇑</span><span class="n">f</span>
<span class="n">has</span> <span class="n">type</span>
  <span class="n">has_coe_to_fun</span><span class="bp">.</span><span class="n">F</span> <span class="n">f</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="bp">Π</span> <span class="o">(</span><span class="n">val</span> <span class="o">:</span> <span class="err">?</span><span class="n">m_1</span><span class="o">),</span> <span class="err">?</span><span class="n">m_2</span> <span class="o">(</span><span class="n">sum</span><span class="bp">.</span><span class="n">inl</span> <span class="n">val</span><span class="o">)</span> <span class="o">:</span> <span class="n">Sort</span> <span class="o">(</span><span class="n">imax</span> <span class="o">(</span><span class="err">?</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="err">?</span><span class="o">)</span>
</pre></div>


<p>I guess this is what you're describing?</p>
<p>(on the other hand, <a href="https://github.com/leanprover/mathlib/blob/fedee9835e73df24a367163e87c9c70284acf4f2/set_theory/cardinal.lean#L296" target="_blank" title="https://github.com/leanprover/mathlib/blob/fedee9835e73df24a367163e87c9c70284acf4f2/set_theory/cardinal.lean#L296">the <code>by exact</code> at line 296</a> can be removed, at least when I play around with this in VS code.)</p>

#### [ Reid Barton (Oct 24 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136428283):
<p>Yeah, there are metavariables in the expected type, and in this case those prevent the coercion from triggering, I guess</p>

#### [ Bryan Gin-ge Chen (Oct 24 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136429224):
<p>Returning to your question about why <code>dec_trivial</code> isn't just notation for <code>of_as_true trivial</code>, the <code>prime 2</code> and <code>prime 3</code> examples can be proved with <code>of_as_true trivial</code>, which is also disposing of all the other <code>dec_trivial</code> examples I'm throwing at it at the moment.  Can we cook up an example where <code>of_as_true trivial</code> fails and the current <code>dec_trivial</code> works?</p>

#### [ Rob Lewis (Oct 24 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136429357):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">dec_trivial</span>
<span class="kn">example</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">of_as_true</span> <span class="n">trivial</span>
</pre></div>

#### [ Rob Lewis (Oct 24 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136429714):
<p>But returning to the original original question: I think there's something wrong with the current <code>nat.decidable_prime</code> instance. For <code>n &gt; 2</code> it depends on  evaluating <code>min_fac</code>, and reducing <code>min_fac 3</code> takes an implausible amount of time.</p>

#### [ Reid Barton (Oct 24 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136429866):
<p>I remember being confused by exactly this original issue about <code>is_prime 2</code> and <code>is_prime 3</code> as well when I was starting out using Lean. It would be nice if it could be fixed somehow.</p>

#### [ Rob Lewis (Oct 24 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136429876):
<p><code>nat.decidable_prime</code> should evaluate faster than <code>nat.decidable_prime_1</code> in the VM, I think, but apparently not in the kernel.</p>

#### [ Rob Lewis (Oct 24 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136429966):
<p>Maybe this isn't "wrong," it could be the right default for the way <code>prime</code> is used right now.</p>

#### [ Rob Lewis (Oct 24 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136429969):
<p>But it is confusing.</p>

#### [ Bryan Gin-ge Chen (Oct 24 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136430222):
<p>This works:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">of_as_true</span> <span class="o">(</span><span class="k">by</span> <span class="n">exact</span> <span class="n">trivial</span><span class="o">)</span>
</pre></div>


<p>Is the current definition of <code>dec_trivial</code> using <code>meta def triv : tactic unit := mk_const `trivial &gt;&gt;= exact</code> equivalent to <code>of_as_true (by exact trivial)</code>?</p>

#### [ Mario Carneiro (Oct 24 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136430285):
<p>yes, this is just the situation. <code>decidable_prime_1</code> is faster in the kernel, <code>decidable_prime</code> is faster in the VM (and also incorporates some tricks to speed up the checking of largeish numbers)</p>

#### [ Mario Carneiro (Oct 24 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136430327):
<p>I recommend using <code>by norm_num</code> if you want a proof that a number is prime, though, since this builds a proof using similar tricks but the kernel will accept it</p>

#### [ Rob Lewis (Oct 24 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136430389):
<p>Oh, cool, I didn't know <code>norm_num</code> did primality proofs.</p>

#### [ Mario Carneiro (Oct 24 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136430397):
<p>it's a recently added module</p>

#### [ Reid Barton (Oct 24 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136430418):
<blockquote>
<p>Is the current definition of <code>dec_trivial</code> using <code>meta def triv : tactic unit := mk_const `trivial &gt;&gt;= exact</code> equivalent to <code>of_as_true (by exact trivial)</code>?</p>
</blockquote>
<p>It should be, though maybe <code>tactic.interactive.exact</code> is not available yet when <code>dec_trivial</code> is being defined</p>

#### [ Kevin Buzzard (Oct 24 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431051):
<blockquote>
<p>Oh, cool, I didn't know <code>norm_num</code> did primality proofs.</p>
</blockquote>
<p><a href="https://xenaproject.wordpress.com/2018/07/26/617-is-prime/" target="_blank" title="https://xenaproject.wordpress.com/2018/07/26/617-is-prime/">https://xenaproject.wordpress.com/2018/07/26/617-is-prime/</a> -- last line!</p>

#### [ Reid Barton (Oct 24 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431192):
<p>Now I'm wondering: what's the largest number formally proven to be prime</p>

#### [ Kevin Buzzard (Oct 24 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431228):
<p>I would definitely start with the largest known Mersenne prime (i.e. the largest known prime).</p>

#### [ Kevin Buzzard (Oct 24 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431242):
<p>Aren't the primality tests pretty low-level and trivial?</p>

#### [ Kevin Buzzard (Oct 24 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431260):
<p>I think they take a couple of weeks to run though :-/</p>

#### [ Reid Barton (Oct 24 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431264):
<p>You'd probably have to do a bit of elementary number theory to prove they are correct</p>

#### [ Kenny Lau (Oct 24 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431268):
<blockquote>
<p>Aren't the primality tests pretty low-level and trivial?</p>
</blockquote>
<p>...</p>

#### [ Kevin Buzzard (Oct 24 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431270):
<p>right</p>

#### [ Kevin Buzzard (Oct 24 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431314):
<p>They are specific primality tests for Mersenne numbers</p>

#### [ Reid Barton (Oct 24 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431334):
<p>A separate question is, if I gave you a "random" 256-bit prime, could we prove it's prime using the AKS primality test or something like that</p>

#### [ Mario Carneiro (Oct 24 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431355):
<p>The current algorithm is just trial division with some optimizations</p>

#### [ Mario Carneiro (Oct 24 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431364):
<p>so it is still exponential in the bits of the number</p>

#### [ Mario Carneiro (Oct 24 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431416):
<p>I thought about implementing AKS, but it probably won't show an advantage until at least 15-digit primes</p>

#### [ Rob Lewis (Oct 24 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136431457):
<p><a href="http://www.lix.polytechnique.fr/~werner/publis/flops06.pdf" target="_blank" title="http://www.lix.polytechnique.fr/~werner/publis/flops06.pdf">http://www.lix.polytechnique.fr/~werner/publis/flops06.pdf</a> has some benchmarks.</p>

#### [ Reid Barton (Oct 24 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136432039):
<p>Apparently the answer was probably the 20th Mersenne prime <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mn>2</mn><mrow><mn>4</mn><mn>4</mn><mn>2</mn><mn>3</mn></mrow></msup><mo>−</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">2^{4423} - 1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:0.897438em;vertical-align:-0.08333em;"></span><span class="base"><span class="mord"><span class="mord mathrm">2</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">4</span><span class="mord mathrm mtight">4</span><span class="mord mathrm mtight">2</span><span class="mord mathrm mtight">3</span></span></span></span></span></span></span></span></span><span class="mbin">−</span><span class="mord mathrm">1</span></span></span></span>, at least as of whenever that paper was written</p>

#### [ Kevin Buzzard (Oct 24 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136432178):
<p>Is that all??</p>

#### [ Kevin Buzzard (Oct 24 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136432183):
<p>People aren't trying hard enough</p>

#### [ Reid Barton (Oct 24 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136432377):
<p>If I understood the paper correctly, they are using a mode of Coq with a VM implementation of reduction in the kernel, so it's a rather large trusted kernel code base as well</p>

#### [ Reid Barton (Oct 24 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136432418):
<p>though apparently they don't use native machine arithmetic, so I'm not really sure</p>

#### [ Kevin Buzzard (Oct 28 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136669712):
<p>So I finally had a chance to look at the paper Rob linked to. So they seem to be doing lots of things at once. They have implemented a generic primality test (this is before AKS I guess -- IIRC that was discovered around the same time). But I am not sure if people care about 10 more primes being verified prime -- people care about the <em>biggest</em> one. So forget Pocklington -- one wants to go straight for the Mersenne primes and probably use the polynomial time Lucas method. So the thing to go for is <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>P</mi><mo>:</mo><mo>=</mo><msup><mn>2</mn><mrow><mn>9</mn><mn>6</mn><mn>8</mn><mn>9</mn></mrow></msup><mo>−</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">P:=2^{9689}-1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:0.897438em;vertical-align:-0.08333em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">P</span><span class="mrel">:</span><span class="mrel">=</span><span class="mord"><span class="mord mathrm">2</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">9</span><span class="mord mathrm mtight">6</span><span class="mord mathrm mtight">8</span><span class="mord mathrm mtight">9</span></span></span></span></span></span></span></span></span><span class="mbin">−</span><span class="mord mathrm">1</span></span></span></span>. This can be proved prime if one can knock off a proof of <a href="https://en.wikipedia.org/wiki/Lucas%E2%80%93Lehmer_primality_test" target="_blank" title="https://en.wikipedia.org/wiki/Lucas%E2%80%93Lehmer_primality_test">the Lucas-Lehmer primality test</a>, which looks well within reach, and then one has to basically square 9689 numbers modulo <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>P</mi></mrow><annotation encoding="application/x-tex">P</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">P</span></span></span></span>. How feasible is that? I just ran the entire test in 217 ms in pari-gp.</p>

#### [ Kevin Buzzard (Oct 28 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136669835):
<p>The next question of course is how feasible it is to square 77232917 numbers modulo <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mn>2</mn><mrow><mn>7</mn><mn>7</mn><mn>2</mn><mn>3</mn><mn>2</mn><mn>9</mn><mn>1</mn><mn>7</mn></mrow></msup><mo>−</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">2^{77232917}-1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:0.897438em;vertical-align:-0.08333em;"></span><span class="base"><span class="mord"><span class="mord mathrm">2</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">7</span><span class="mord mathrm mtight">7</span><span class="mord mathrm mtight">2</span><span class="mord mathrm mtight">3</span><span class="mord mathrm mtight">2</span><span class="mord mathrm mtight">9</span><span class="mord mathrm mtight">1</span><span class="mord mathrm mtight">7</span></span></span></span></span></span></span></span></span><span class="mbin">−</span><span class="mord mathrm">1</span></span></span></span>.</p>

#### [ Kevin Buzzard (Oct 28 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20doesn%27t%20dec_trivial%20solve%20%60prime%203%60%3F/near/136670082):
<p>It's probably worth pointing out that if numbers are somehow being stored in binary, then reducing modulo a number of the form <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mn>2</mn><mi>n</mi></msup><mo>−</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">2^n-1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.664392em;"></span><span class="strut bottom" style="height:0.747722em;vertical-align:-0.08333em;"></span><span class="base"><span class="mord"><span class="mord mathrm">2</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span></span></span></span></span><span class="mbin">−</span><span class="mord mathrm">1</span></span></span></span> can be done using specialised code which would perhaps be more efficient than usual Euclid? But I have no idea whatsoever how reasonable it would be to expect Lean to do any arithmetic at all with numbers so large.</p>


{% endraw %}
