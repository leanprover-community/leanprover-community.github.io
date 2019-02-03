---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/81809classinstanceresdepthreachedfintypeclassicalsome.html
---

## Stream: [new members](index.html)
### Topic: ["class-instance res. depth reached" fintype + classical.some](81809classinstanceresdepthreachedfintypeclassicalsome.html)

---


{% raw %}
#### [ Tobias Grosser (Sep 29 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871036):
<p>Hi guys, I am trying to model ssreflects 'pick' method using classical.some. The code I came up with reads:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">finite</span>
<span class="kn">import</span> <span class="n">ring_theory</span><span class="bp">.</span><span class="n">matrix</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>

<span class="n">def</span> <span class="n">vec</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">m</span><span class="o">]</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">m</span> <span class="bp">→</span> <span class="n">α</span>

<span class="n">local</span> <span class="n">attribute</span> <span class="n">classical</span><span class="bp">.</span><span class="n">prop_decidable</span>
<span class="kn">set_option</span> <span class="n">class</span><span class="bp">.</span><span class="n">instance_max_depth</span> <span class="mi">60</span>
<span class="c1">-- set_option trace.class_instances true</span>

<span class="n">noncomputable</span> <span class="n">def</span> <span class="n">get_sample_or_zero</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">ordered_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">has_zero</span> <span class="n">α</span><span class="o">]:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">m</span><span class="o">),</span> <span class="n">vec</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m</span><span class="o">)</span> <span class="n">α</span>  <span class="bp">→</span> <span class="n">α</span>
<span class="bp">|</span> <span class="n">m</span> <span class="n">V</span> <span class="o">:=</span>
  <span class="k">let</span> <span class="n">S</span> <span class="o">:=</span> <span class="o">{</span> <span class="n">i</span>  <span class="bp">|</span> <span class="n">V</span> <span class="n">i</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">}</span> <span class="k">in</span>
  <span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">S</span>
    <span class="k">then</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some</span> <span class="n">h</span>
    <span class="k">else</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span>
</pre></div>


<p>but triggers a "maximum class-instance resolution depth has been reached". Any pointers what could go wrong here?</p>

#### [ Simon Hudon (Sep 29 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871101):
<p>Try removing <code>has_zero</code>. It should be implied by the ordered ring.</p>

#### [ Simon Hudon (Sep 29 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871141):
<p>This is the kind of problem that arises when your instances overlap in conflicting ways</p>

#### [ Tobias Grosser (Sep 29 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871197):
<p>Thanks <span class="user-mention" data-user-id="110026">@Simon Hudon</span> , unfortunately this does not help.</p>

#### [ Tobias Grosser (Sep 29 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871251):
<p>Still the same error<br>
Dropping the ordered_ring instead also does not help.</p>

#### [ Tobias Grosser (Sep 29 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871252):
<p>I can also drop the matrix import, this does not change anything either.</p>

#### [ Simon Hudon (Sep 29 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871307):
<p>I think you should need anything beside <code>has_zero</code> actually.</p>

#### [ Simon Hudon (Sep 29 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871347):
<p>Is it important that the default value be <code>0</code>? If not, you can replace the <code>if</code> with <code>classical.epsilon S</code>.</p>

#### [ Mario Carneiro (Sep 29 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871348):
<div class="codehilite"><pre><span></span>local attribute classical.prop_decidable
</pre></div>


<p>since when is this valid syntax?</p>

#### [ Mario Carneiro (Sep 29 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871355):
<p>oh wait, now I see... this doesn't do anything</p>

#### [ Mario Carneiro (Sep 29 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871395):
<p>you want <code>local attribute [instance] classical.prop_decidable</code></p>

#### [ Mario Carneiro (Sep 29 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871454):
<p>I don't think you need classical anything for this definition, if I read it correctly</p>

#### [ Simon Hudon (Sep 29 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871499):
<p>You can do without classical reasoning but you need to implement a search</p>

#### [ Mario Carneiro (Sep 29 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871527):
<p>Also the <code>then</code> part is not type correct</p>
<div class="codehilite"><pre><span></span>import data.set.finite data.equiv.encodable

def get_sample_or_zero (α : Type) [decidable_eq α] [has_zero α] : Π (m), vec (fin m) α  → α
| m V := if h : ∃ i, V i = 0 then V (encodable.choose h) else 0
</pre></div>

#### [ Mario Carneiro (Sep 29 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871530):
<p>note the <code>V</code> in the middle</p>

#### [ Mario Carneiro (Sep 29 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871576):
<p>then again, this function is always 0, so maybe that's not what you meant</p>

#### [ Mario Carneiro (Sep 29 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871588):
<p>but if this returns a <code>fin m</code> then you have a problem since <code>0 : fin m</code> only holds if <code>m&gt;0</code></p>

#### [ Mario Carneiro (Sep 29 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871701):
<p>wasn't ssreflect's pick function something like this?</p>
<div class="codehilite"><pre><span></span>noncomputable def pick (α : Type*) : option α :=
by haveI := classical.dec (nonempty α); exact
if h : nonempty α then some (classical.choice h) else none
</pre></div>

#### [ Tobias Grosser (Sep 29 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871708):
<p>SSReflects pick is: "[pick x in A] == Some x, with x \in A, or None if A is empty. "</p>

#### [ Tobias Grosser (Sep 29 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871709):
<p>Here the definition: <a href="http://ssr.msr-inria.inria.fr/doc/ssreflect-1.5/Ssreflect.fintype.html" target="_blank" title="http://ssr.msr-inria.inria.fr/doc/ssreflect-1.5/Ssreflect.fintype.html">http://ssr.msr-inria.inria.fr/doc/ssreflect-1.5/Ssreflect.fintype.html</a></p>

#### [ Mario Carneiro (Sep 29 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871756):
<p>right, isn't that what I wrote?</p>

#### [ Tobias Grosser (Sep 29 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871758):
<p>Honestly, I need some more time to think about these solutions.</p>

#### [ Tobias Grosser (Sep 29 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871804):
<p>I mostly was concerned about the then path and therefore just returned zero in the else.</p>

#### [ Mario Carneiro (Sep 29 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871810):
<p>Maybe <code>A</code> is a subset of a type instead of just a type; in that case you have</p>
<div class="codehilite"><pre><span></span>noncomputable def pick {α} (p : α → Prop) : option α :=
by haveI := classical.dec (∃ a, p a); exact
if h : ∃ a, p a then some (classical.some h) else none
</pre></div>

#### [ Tobias Grosser (Sep 29 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871856):
<p>To give some context, what I actually want to write is:</p>
<div class="codehilite"><pre><span></span><span class="kn">Fixpoint</span> <span class="n">Gaussian_elimination</span> <span class="o">{</span><span class="n">m</span> <span class="n">n</span><span class="o">}</span> <span class="o">:</span> <span class="k">&#39;</span><span class="n">M_</span><span class="o">(</span><span class="n">m</span><span class="o">,</span> <span class="n">n</span><span class="o">)</span> <span class="err">→</span> <span class="k">&#39;</span><span class="n">M_m</span> <span class="err">×</span> <span class="k">&#39;</span><span class="n">M_n</span> <span class="err">×</span> <span class="kt">nat</span> <span class="o">:=</span>
  <span class="k">match</span> <span class="n">m</span><span class="o">,</span> <span class="n">n</span> <span class="k">with</span>
  <span class="o">|</span> <span class="o">_.+</span><span class="mi">1</span><span class="o">,</span> <span class="o">_.+</span><span class="mi">1</span> <span class="err">⇒</span> <span class="k">fun</span> <span class="n">A</span> <span class="o">:</span> <span class="k">&#39;</span><span class="n">M_</span><span class="o">(</span><span class="mi">1</span> <span class="o">+</span> <span class="o">_,</span> <span class="mi">1</span> <span class="o">+</span> <span class="o">_)</span> <span class="err">⇒</span>
    <span class="k">if</span> <span class="o">[</span><span class="n">pick</span> <span class="n">ij</span> <span class="o">|</span> <span class="n">A</span> <span class="n">ij</span><span class="o">.</span><span class="mi">1</span> <span class="n">ij</span><span class="o">.</span><span class="mi">2</span> <span class="o">!=</span> <span class="mi">0</span><span class="o">]</span> <span class="k">is</span> <span class="n">Some</span> <span class="o">(</span><span class="n">i</span><span class="o">,</span> <span class="n">j</span><span class="o">)</span> <span class="k">then</span>
      <span class="k">let</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">A</span> <span class="n">i</span> <span class="n">j</span> <span class="k">in</span> <span class="k">let</span> <span class="n">A1</span> <span class="o">:=</span> <span class="n">xrow</span> <span class="n">i</span> <span class="mi">0</span> <span class="o">(</span><span class="n">xcol</span> <span class="n">j</span> <span class="mi">0</span> <span class="n">A</span><span class="o">)</span> <span class="k">in</span>
      <span class="k">let</span> <span class="n">u</span> <span class="o">:=</span> <span class="n">ursubmx</span> <span class="n">A1</span> <span class="k">in</span> <span class="k">let</span> <span class="n">v</span> <span class="o">:=</span> <span class="n">a</span><span class="o">^-</span><span class="mi">1</span> <span class="o">*:</span> <span class="n">dlsubmx</span> <span class="n">A1</span> <span class="k">in</span>
      <span class="k">let</span><span class="o">:</span> <span class="o">(</span><span class="n">L</span><span class="o">,</span> <span class="n">U</span><span class="o">,</span> <span class="n">r</span><span class="o">)</span> <span class="o">:=</span> <span class="n">Gaussian_elimination</span> <span class="o">(</span><span class="n">drsubmx</span> <span class="n">A1</span> <span class="o">-</span> <span class="n">v</span> <span class="err">×</span><span class="n">m</span> <span class="n">u</span><span class="o">)</span> <span class="k">in</span>
      <span class="o">(</span><span class="n">xrow</span> <span class="n">i</span> <span class="mi">0</span> <span class="o">(</span><span class="n">block_mx</span> <span class="mi">1</span> <span class="mi">0</span> <span class="n">v</span> <span class="n">L</span><span class="o">),</span> <span class="n">xcol</span> <span class="n">j</span> <span class="mi">0</span> <span class="o">(</span><span class="n">block_mx</span> <span class="n">a</span><span class="o">%:</span><span class="n">M</span> <span class="n">u</span> <span class="mi">0</span> <span class="n">U</span><span class="o">),</span> <span class="n">r</span><span class="o">.+</span><span class="mi">1</span><span class="o">)</span>
    <span class="k">else</span> <span class="o">(</span><span class="mi">1</span><span class="o">%:</span><span class="n">M</span><span class="o">,</span> <span class="mi">1</span><span class="o">%:</span><span class="n">M</span><span class="o">,</span> <span class="mi">0</span><span class="o">%</span><span class="n">N</span><span class="o">)</span>
  <span class="o">|</span> <span class="o">_,</span> <span class="o">_</span> <span class="err">⇒</span> <span class="k">fun</span> <span class="o">_</span> <span class="err">⇒</span> <span class="o">(</span><span class="mi">1</span><span class="o">%:</span><span class="n">M</span><span class="o">,</span> <span class="mi">1</span><span class="o">%:</span><span class="n">M</span><span class="o">,</span> <span class="mi">0</span><span class="o">%</span><span class="n">N</span><span class="o">)</span>
  <span class="k">end</span><span class="o">.</span>
</pre></div>

#### [ Tobias Grosser (Sep 29 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871864):
<p>I am just taking baby steps, to learn these different things.</p>

#### [ Tobias Grosser (Sep 29 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871874):
<p>Will get back to try to play with your pick function and see how it can be used here.</p>

#### [ Tobias Grosser (Sep 29 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871875):
<p>Thanks for the pointers.</p>

#### [ Mario Carneiro (Sep 29 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134871976):
<p>Maybe the nicest interface for that pick match is something like this:</p>
<div class="codehilite"><pre><span></span>@[elab_as_eliminator]
noncomputable def {u} classical.exists_cases (p : α → Prop) {C : Sort u} (H0 : C) (H : ∀ a, p a → C) : C :=
if h : ∃ a, p a then H (classical.some h) (classical.some_spec h) else H0
</pre></div>

#### [ Mario Carneiro (Sep 29 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872035):
<p>In your context it would be something like <code>classical.exists_cases (λ ij, A ij.1 ij.2 ≠ 0) (1, 1, 0) $ λ ⟨i, j⟩, ...</code></p>

#### [ Tobias Grosser (Sep 29 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872038):
<p>OK. Even more things to try to integrate.</p>

#### [ Tobias Grosser (Sep 29 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872058):
<p>One last question. In the end I want a gaussian elimination which can compute solutions.</p>

#### [ Tobias Grosser (Sep 29 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872104):
<p>Am I on a wrong track here? Aka, can this evolve to something computable eventually?</p>

#### [ Simon Hudon (Sep 29 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872106):
<p>Then you're going to need to specialize that function so that you can implement it using a search function.</p>

#### [ Mario Carneiro (Sep 29 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872108):
<p>Not using the function I just gave you</p>

#### [ Mario Carneiro (Sep 29 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872120):
<p>You want to use <code>encodable.choose</code> to do choicy stuff decidably</p>

#### [ Tobias Grosser (Sep 29 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872133):
<p>What exactly is the difference.</p>

#### [ Mario Carneiro (Sep 29 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872179):
<p>Basically any function with <code>classical</code> in the name will not be computable, even if the inputs are</p>

#### [ Tobias Grosser (Sep 29 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872180):
<p>ssreflect seems to be a hybrid of both.</p>

#### [ Tobias Grosser (Sep 29 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872183):
<p>That's what I know.</p>

#### [ Mario Carneiro (Sep 29 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872187):
<p><code>ssreflect</code> essentially embeds <code>encodable.choose</code> very low in their algebraic hierarchy</p>

#### [ Tobias Grosser (Sep 29 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872194):
<p>I see. So the counterpart in lean would be a "pick based on 'encodable.choose'?"</p>

#### [ Mario Carneiro (Sep 29 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872195):
<p>yes</p>

#### [ Tobias Grosser (Sep 29 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872196):
<p>I see.</p>

#### [ Tobias Grosser (Sep 29 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872203):
<p>Can I also get the nice { (i j) | ... } interface for such a pick?</p>

#### [ Mario Carneiro (Sep 29 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872244):
<p>You can pattern match on <code>i, j</code> in the then branch</p>

#### [ Mario Carneiro (Sep 29 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872247):
<p>like at the end of my example <code>λ ⟨i, j⟩, ...</code></p>

#### [ Tobias Grosser (Sep 29 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872260):
<p>OK.</p>

#### [ Mario Carneiro (Sep 29 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872262):
<p>I think <code>[pick ij | A ij.1 ij.2 != 0]</code> is some composite notation which is basically <code>pick (λ ij, A ij.1 ij.2 != 0)</code></p>

#### [ Tobias Grosser (Sep 29 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872263):
<p>But your example uses classical.choice</p>

#### [ Mario Carneiro (Sep 29 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872270):
<p>You can swap out <code>classical.some</code> with <code>encodable.choose</code> for great good</p>

#### [ Tobias Grosser (Sep 29 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872271):
<p>I see.</p>

#### [ Tobias Grosser (Sep 29 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872312):
<p>I think that's all I need. I will put the things together myself!</p>

#### [ Tobias Grosser (Sep 29 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872314):
<p>Thanks a lot.</p>

#### [ Mario Carneiro (Sep 29 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872321):
<p>We don't have a "choice type" typeclass like ssreflect, so it's one or the other here</p>

#### [ Mario Carneiro (Sep 29 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872332):
<p>but fin n is encodable so it's all good</p>

#### [ Tobias Grosser (Sep 29 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134872334):
<p>:D</p>

#### [ Tobias Grosser (Sep 29 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134896880):
<p>Just to report back. I use for now the function:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">pick_encodable</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="n">p</span><span class="o">]:</span>
<span class="bp">Π</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span><span class="o">),</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">option</span><span class="o">(</span><span class="n">fin</span> <span class="n">m</span> <span class="bp">×</span> <span class="n">fin</span> <span class="n">n</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">x</span> <span class="n">y</span> <span class="n">V</span> <span class="o">:=</span>
  <span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">ij</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">x</span> <span class="bp">×</span> <span class="n">fin</span> <span class="n">y</span><span class="o">),</span> <span class="n">p</span> <span class="o">(</span><span class="n">V</span> <span class="n">ij</span><span class="bp">.</span><span class="mi">1</span> <span class="n">ij</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span>
    <span class="k">then</span> <span class="k">let</span> <span class="n">idx</span> <span class="o">:=</span> <span class="n">encodable</span><span class="bp">.</span><span class="n">choose</span> <span class="n">h</span> <span class="k">in</span>
      <span class="n">some</span> <span class="n">idx</span>
    <span class="k">else</span>
      <span class="n">none</span>
</pre></div>

#### [ Tobias Grosser (Sep 29 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%22class-instance%20res.%20depth%20reached%22%20fintype%20%2B%20classical.some/near/134896882):
<p>This probably needs some more cleanup, but or now it does what I want.</p>


{% endraw %}
