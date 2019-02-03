---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/80114ringalgebras.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [ring algebras](https://leanprover-community.github.io/archive/113488general/80114ringalgebras.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Sep 04 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299335):
<p>This problem has come up several times in this year, and I decided it's time to face it instead of to avoid it. This is the definition of an algebra over a commutative ring:</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">algebra</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="n">out_param</span> <span class="err">$</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">ring</span> <span class="n">A</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">A</span><span class="o">)</span> <span class="o">[</span><span class="n">hom</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span>
<span class="o">(</span><span class="n">commutes</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">r</span> <span class="n">s</span><span class="o">,</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">f</span> <span class="n">r</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">r</span> <span class="bp">*</span> <span class="n">s</span><span class="o">)</span>
</pre></div>


<p>Mathematically there are no problems, but somehow every time I try to introduce this class, the class inferences become a mess, consistently. So, my question is: what is the best way to introduce this whole algebra thing to Lean?</p>

#### [ Johan Commelin (Sep 04 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299411):
<p>Yeah! Go for it! I recognize the troubles, and I don't know the answer...</p>

#### [ Johan Commelin (Sep 04 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299424):
<p>Concerning terminology... I think Bourbaki has a more general notion of algebra.</p>

#### [ Johan Commelin (Sep 04 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299477):
<p>For example, a Lie algebra is an algebra.</p>

#### [ Kenny Lau (Sep 04 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299481):
<p>MWE:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">polynomial</span>

<span class="n">class</span> <span class="n">algebra</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="n">out_param</span> <span class="err">$</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">ring</span> <span class="n">A</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">A</span><span class="o">)</span> <span class="o">[</span><span class="n">hom</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span>
<span class="o">(</span><span class="n">commutes</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">r</span> <span class="n">s</span><span class="o">,</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">f</span> <span class="n">r</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">r</span> <span class="bp">*</span> <span class="n">s</span><span class="o">)</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span>

<span class="kn">instance</span> <span class="n">ring</span><span class="bp">.</span><span class="n">to_ℤ_algebra</span> <span class="o">:</span> <span class="n">algebra</span> <span class="bp">ℤ</span> <span class="n">R</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">coe</span><span class="o">,</span>
  <span class="n">hom</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">constructor</span><span class="bp">;</span> <span class="n">intros</span><span class="bp">;</span> <span class="n">simp</span><span class="o">,</span>
  <span class="n">commutes</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">n</span> <span class="n">r</span><span class="o">,</span> <span class="n">int</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">n</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span> <span class="n">ih</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">mul_add</span><span class="o">,</span> <span class="n">add_mul</span><span class="o">,</span> <span class="n">ih</span><span class="o">])</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span> <span class="n">ih</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">mul_add</span><span class="o">,</span> <span class="n">add_mul</span><span class="o">,</span> <span class="n">ih</span><span class="o">]),</span> <span class="o">}</span>

<span class="kn">set_option</span> <span class="n">trace</span><span class="bp">.</span><span class="n">class_instances</span> <span class="n">true</span>
<span class="bp">#</span><span class="kn">check</span> <span class="o">(</span><span class="k">by</span> <span class="n">apply_instance</span> <span class="o">:</span> <span class="n">ring</span> <span class="o">(</span><span class="n">polynomial</span> <span class="bp">ℤ</span><span class="o">))</span>
</pre></div>

#### [ Johan Commelin (Sep 04 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299500):
<p>Don't you get diamonds this way?</p>

#### [ Kenny Lau (Sep 04 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299559):
<p>What do you mean?</p>

#### [ Johan Commelin (Sep 04 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299562):
<p>every algebra is already a ring, and now you are turning rings into algebras, so you are getting loops, not?</p>

#### [ Johan Commelin (Sep 04 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299565):
<p>Maybe diamond is not the right word, but certainly loops.</p>

#### [ Kenny Lau (Sep 04 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299571):
<p>I see</p>

#### [ Kenny Lau (Sep 04 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299574):
<p>but it's an important fact that every ring is a Z-algebra, no?</p>

#### [ Johan Commelin (Sep 04 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299633):
<p>Just as important as the fact that every abelian group is a Z-module.</p>

#### [ Kevin Buzzard (Sep 04 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/133299759):
<p>Maybe that's the place to start this discussion. For example, my correspondence theorem is written for R-modules. How does one deduce the correspondence theorem for abelian groups? For mathematicians, the answer is easy -- "set R=Z; done". How do we do it in Lean?</p>

#### [ Kevin Buzzard (Dec 08 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151194100):
<p>At the time, the answer to this question was "just wait until the module refactor hits and then try again". Did you try again after the module refactor? What is still problematic?</p>

#### [ Kenny Lau (Dec 08 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151194328):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> the original MWE I posted above still works (in the sense that it still fails)</p>

#### [ Kenny Lau (Dec 08 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151194329):
<p>and if you define algebra differently, you run into another typeclass problem:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">polynomial</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>

<span class="n">class</span> <span class="n">algebra</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="n">out_param</span> <span class="err">$</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">[</span><span class="n">out_param</span> <span class="err">$</span> <span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">ring</span> <span class="n">A</span><span class="o">]</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">A</span><span class="o">)</span> <span class="o">[</span><span class="n">hom</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span>
<span class="o">(</span><span class="n">commutes</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">r</span> <span class="n">s</span><span class="o">,</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">f</span> <span class="n">r</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">r</span> <span class="bp">*</span> <span class="n">s</span><span class="o">)</span>

<span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">hom</span>

<span class="kn">namespace</span> <span class="n">algebra</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span>
<span class="kn">variables</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">ring</span> <span class="n">A</span><span class="o">]</span> <span class="o">[</span><span class="n">algebra</span> <span class="n">R</span> <span class="n">A</span><span class="o">]</span>

<span class="kn">instance</span> <span class="n">to_module</span> <span class="o">:</span> <span class="n">module</span> <span class="n">R</span> <span class="n">A</span> <span class="o">:=</span> <span class="n">module</span><span class="bp">.</span><span class="n">of_core</span>
<span class="o">{</span> <span class="n">smul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">r</span> <span class="n">x</span><span class="o">,</span> <span class="n">f</span> <span class="n">A</span> <span class="n">r</span> <span class="bp">*</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">smul_add</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">intros</span><span class="bp">;</span> <span class="n">simp</span> <span class="o">[</span><span class="n">mul_add</span><span class="o">],</span>
  <span class="n">add_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">mul_smul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">one_smul</span> <span class="o">:=</span> <span class="n">sorry</span> <span class="o">}</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">mul_smul</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">A</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">x</span> <span class="bp">*</span> <span class="o">(</span><span class="n">s</span> <span class="err">•</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">s</span> <span class="err">•</span> <span class="o">(</span><span class="n">x</span> <span class="bp">*</span> <span class="n">y</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">smul_def</span><span class="o">,</span> <span class="n">smul_def</span><span class="o">,</span> <span class="err">←</span> <span class="n">mul_assoc</span><span class="o">,</span> <span class="n">commutes</span><span class="o">,</span> <span class="n">mul_assoc</span><span class="o">]</span>

<span class="kn">end</span> <span class="n">algebra</span>
</pre></div>

#### [ Kenny Lau (Dec 08 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151194330):
<p>in any case I'm quite tired of Lean's typeclass inference</p>

#### [ Kevin Buzzard (Dec 08 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151194336):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Help! Is this sort of thing still a problem?</p>

#### [ Johan Commelin (Dec 08 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151194926):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> I know I'm just commenting without having tried anything out. But I have been working with over-categories a bit. And there has been some work with <code>CommRing</code>, I understand. So couldn't we define <code>algebra R</code> as <code>under R</code>?</p>

#### [ Johan Commelin (Dec 08 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151194927):
<p>I hope that should just work.</p>

#### [ Kenny Lau (Dec 08 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151195058):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> could you show me what the code I just posted would become?</p>

#### [ Johan Commelin (Dec 08 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196687):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Sorry, I was distracted for a while. You have worked on colimits in <code>CommRing</code> haven't you?</p>

#### [ Kenny Lau (Dec 08 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196688):
<p>I haven't</p>

#### [ Johan Commelin (Dec 08 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196692):
<p>Aah, I thought you did, together with Ramon and Kevin.</p>

#### [ Johan Commelin (Dec 08 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196694):
<p>Anyway, I think <code>CommRing</code> is currently being PR'd or about to be PR'd.</p>

#### [ Kenny Lau (Dec 08 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196735):
<p>oh well I didn't use the category theory language</p>

#### [ Johan Commelin (Dec 08 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196737):
<p><a href="https://github.com/leanprover/mathlib/blob/master/category_theory/examples/rings.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/category_theory/examples/rings.lean">https://github.com/leanprover/mathlib/blob/master/category_theory/examples/rings.lean</a></p>

#### [ Johan Commelin (Dec 08 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196739):
<p>So, there is something there.</p>

#### [ Johan Commelin (Dec 08 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196744):
<p>Next, you could define under categories, as in <a href="https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/sheafy_preamble.lean#L180" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/sheafy_preamble.lean#L180">https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/sheafy_preamble.lean#L180</a></p>

#### [ Johan Commelin (Dec 08 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196745):
<p>And combining those, you would have commutative algebras over a commring.</p>

#### [ Kenny Lau (Dec 08 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196787):
<p>yes, yes, yes, you could, provided that your URL doesn't contain "leanprover-community"</p>

#### [ Johan Commelin (Dec 08 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196790):
<p>You only need that 1 line.</p>

#### [ Johan Commelin (Dec 08 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196792):
<p>Comma categories are already in mathlib.</p>

#### [ Johan Commelin (Dec 08 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151196803):
<p>The <code>functor.of.obj</code> is currently being PR'd to replace <code>functor.of_obj</code></p>

#### [ Johan Commelin (Dec 09 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151212724):
<p>Is there any chance that we will be able to use <code>\Z</code> notation as an object of <code>Ring</code>? Will we always have to type <code>Ring.int</code>? Somehow I wish that we can automatically coerce a type into an object of a category if the right type class instance is found... (maybe let's not worry if that is possible with modules, atm) It would be possible if that would at least be possible with the most basic examples, like nats, ints (modulo <code>n</code>), rats, reals, complexes.</p>

#### [ Johan Commelin (Dec 09 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151213510):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> This is what I came up with, after a little bit of hacking. <a href="https://github.com/leanprover-community/mathlib/blob/jmc-leftmod/category_theory/examples/left_module.lean" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/jmc-leftmod/category_theory/examples/left_module.lean">https://github.com/leanprover-community/mathlib/blob/jmc-leftmod/category_theory/examples/left_module.lean</a><br>
Need to go now. Of course there is lots to be done.</p>

#### [ Kenny Lau (Dec 09 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151214428):
<p>well... are you sure there will be no type-class issues?</p>

#### [ Johan Commelin (Dec 09 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151217969):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Of course I can't be sure about that. But I think that the more you bundle, the less type class issues you will have. Otoh, the more you will have to be explicit about "coercions", and things like that.</p>

#### [ Kenny Lau (Dec 09 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151217971):
<p>so are you implying that the Lean typeclass system cannot be salvaged unless we bundle everything?</p>

#### [ Johan Commelin (Dec 09 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151218021):
<p>I don't know. The current type class system clearly isn't the most powerful thing imaginable. But for now I wouldn't mind trying more module stuff with less type class stuff.</p>

#### [ Johan Commelin (Dec 09 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151218080):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Shall we try to define <code>map f</code> and <code>comap f</code> between <code>R-Mod</code> and <code>S-Mod</code> if <code>f : R \hom S</code> is a morphism of commutative rings?</p>

#### [ Kenny Lau (Dec 09 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151218120):
<p>sure</p>

#### [ Johan Commelin (Dec 09 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151218181):
<p>First complication: <code>CommRing</code> is not a full subcategory of <code>Ring</code> in the current setup. So we can't just speak of <code>R-Mod</code>.</p>

#### [ Kevin Buzzard (Dec 09 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151220181):
<p>Isn't Lean's type class system the most powerful thing you can imagine subject to the requirement that you promise that if you ever define two terms of a given typeclass then they will be defeq? The problem might be that mathematicians are expecting too much from it perhaps. One way of upgrading it is to weaken the promise from "defeq" to "either defeq, or the typeclass is provably a subsingleton".</p>

#### [ Kevin Buzzard (Dec 09 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151220287):
<p>Maybe there is an art to using priorities somehow? You could imagine that mathematicians could try to get better at this art. I've not seen this technique used before. <span class="user-mention" data-user-id="110044">@Chris Hughes</span> you had problems with finsets or fintypes when you ended up with...something like two "different" empty lists representing the empty finset, right? Could you imagine carefully switching the priority of something to either very low or very high, to ensure that type class inference issues don't occur? Johan/Kenny, could you imagine doing the same thing here?</p>

#### [ Chris Hughes (Dec 09 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151220971):
<p>I don't think priority switching works. In the algebra example maybe who end up with the two different instances because you used a lemma that had to use the polynomial instance, because it was proved in more generality than just the integers, and likewise for the other instance.</p>

#### [ Kenny Lau (Dec 09 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151223377):
<p>will auxiliary types be the solution?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">to_module</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">algebra</span> <span class="n">R</span> <span class="n">A</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span> <span class="o">:=</span> <span class="n">A</span>

<span class="kn">instance</span> <span class="n">to_module</span><span class="bp">.</span><span class="n">comm_ring</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="o">(</span><span class="n">to_module</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">dunfold</span> <span class="n">to_module</span><span class="bp">;</span> <span class="n">apply_instance</span>

<span class="kn">instance</span> <span class="n">to_module</span><span class="bp">.</span><span class="n">module</span> <span class="o">:</span> <span class="n">module</span> <span class="n">R</span> <span class="o">(</span><span class="n">to_module</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span> <span class="n">module</span><span class="bp">.</span><span class="n">of_core</span>
<span class="o">{</span> <span class="n">smul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">r</span> <span class="n">x</span><span class="o">,</span> <span class="n">i</span> <span class="n">r</span> <span class="bp">*</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">smul_add</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">intros</span><span class="bp">;</span> <span class="n">simp</span> <span class="o">[</span><span class="n">mul_add</span><span class="o">],</span>
  <span class="n">add_smul</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">intros</span><span class="bp">;</span> <span class="n">simp</span> <span class="o">[</span><span class="n">add_mul</span><span class="o">],</span>
  <span class="n">mul_smul</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">intros</span><span class="bp">;</span> <span class="n">simp</span> <span class="o">[</span><span class="n">mul_assoc</span><span class="o">],</span>
  <span class="n">one_smul</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">intros</span><span class="bp">;</span> <span class="n">simp</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">one_mul</span> <span class="n">x</span> <span class="o">}</span>
</pre></div>

#### [ Chris Hughes (Dec 09 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151223424):
<p>But you're still going to end up needing to prove the two instances are equal right? If you use lemmas about each of the different instances</p>

#### [ Kenny Lau (Dec 09 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151223593):
<p>I made it a structure</p>

#### [ Kevin Buzzard (Dec 09 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151223656):
<p>Maybe you can use <code>convert</code> cleverly at some point. Can you remove things from the type class inference machine? I can't help but think that it will somehow be possible to do all this, maybe we're not having the clearest ideas about how to do it</p>

#### [ Chris Hughes (Dec 09 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151229632):
<blockquote>
<p>Maybe you can use <code>convert</code> cleverly at some point. Can you remove things from the type class inference machine? I can't help but think that it will somehow be possible to do all this, maybe we're not having the clearest ideas about how to do it</p>
</blockquote>
<p>convert and congr are handy in these situations</p>

#### [ Kenny Lau (Dec 09 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151237409):
<p>(non-MWE incoming)</p>

#### [ Kenny Lau (Dec 09 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151237411):
<p><a href="/user_uploads/3121/OP41IwlpQ8GAgQpW6UFtBNmB/2018-12-09-2.png" target="_blank" title="2018-12-09-2.png">2018-12-09-2.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/OP41IwlpQ8GAgQpW6UFtBNmB/2018-12-09-2.png" target="_blank" title="2018-12-09-2.png"><img src="/user_uploads/3121/OP41IwlpQ8GAgQpW6UFtBNmB/2018-12-09-2.png"></a></div>

#### [ Kenny Lau (Dec 09 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151237456):
<p>"there's a type mismatch so I use <code>convert</code> which produces a proof by <code>eq.mpr (eq.refl _)</code></p>

#### [ Kenny Lau (Dec 09 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151237458):
<p>so what is happening"</p>

#### [ Kenny Lau (Dec 10 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151246670):
<p>R[X] is an R-algebra so it has a module structure (where the scalar multiplication is <code>C r * p</code>). However <code>R[X]</code> is a finsupp so it also gets another module structure</p>

#### [ Kenny Lau (Dec 10 2018 at 03:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151246708):
<p>The two module structures are not definitionally equal</p>

#### [ Kenny Lau (Dec 10 2018 at 03:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151246711):
<p>can we get rid of the latter structure?</p>

#### [ Reid Barton (Dec 10 2018 at 03:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151246878):
<p>Isn't the latter instance "the direct sum of R-modules is an R-module"?</p>

#### [ Kenny Lau (Dec 10 2018 at 03:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151246932):
<p>right</p>

#### [ Reid Barton (Dec 10 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151247189):
<p>How does the second instance come up in practice? Are you manually unfolding to a finsupp?<br>
Ah, do you mean the line <code>instance : module α (polynomial α) := finsupp.to_module ℕ α</code>?</p>

#### [ Reid Barton (Dec 10 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151247250):
<p>(does R[X] refer to <code>data.polynomial</code>?)</p>

#### [ Kenny Lau (Dec 10 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151247375):
<p>yes</p>

#### [ Reid Barton (Dec 10 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151247440):
<p>I think I mostly caught up on this thread. Deleting that instance makes sense, though I wouldn't be too surprised if you end up with new problems...</p>

#### [ Kenny Lau (Dec 10 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151257075):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> what do you think about this?</p>

#### [ Mario Carneiro (Dec 10 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151257150):
<div class="codehilite"><pre><span></span>class algebra (R : out_param $ Type*) [comm_ring R] (A : Type*) extends ring A :=
</pre></div>


<p>this is trouble, because this will make <code>ring A</code> typeclass problems go looking for instances of <code>algebra ? A</code></p>

#### [ Kenny Lau (Dec 10 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151257201):
<p>right, so I am not using this now</p>

#### [ Kenny Lau (Dec 10 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151257205):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">algebra</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">A</span><span class="o">]</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">to_fun</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">A</span><span class="o">)</span> <span class="o">[</span><span class="n">hom</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="n">to_fun</span><span class="o">]</span>
</pre></div>

#### [ Kenny Lau (Dec 10 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151257208):
<p>I've been using this</p>

#### [ Kenny Lau (Dec 10 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151257288):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> would there be any problem if we forgot about the module structure on R[X] induced by finsupp?</p>

#### [ Kenny Lau (Dec 10 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151257303):
<p>or maybe I should just prove that these two modules are isomorphic</p>

#### [ Mario Carneiro (Dec 10 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151257358):
<p>I thought an algebra was a ring that is also a module</p>

#### [ Mario Carneiro (Dec 10 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151257370):
<p>why not have it extend module, and assert that the function's induced smul matches the existing one</p>

#### [ Kenny Lau (Dec 10 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151257442):
<p>I thought we like definitional equalities</p>

#### [ Kenny Lau (Dec 10 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151257466):
<p>hmm, I see that can be a solution</p>

#### [ Kevin Buzzard (Dec 10 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151258425):
<blockquote>
<p>I thought an algebra was a ring that is also a module</p>
</blockquote>
<p>In CS you have to think really carefully about these sorts of things. In my mind, an <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span>-algebra is a ring which is also an <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span>-module, <em>and</em> an <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span>-algebra is the codomain of a ring homomorphism from <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span> -- the two notions are completely interchangeable. In Lean things seem to be much more delicate.</p>

#### [ Kevin Buzzard (Dec 10 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151258478):
<blockquote>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">algebra</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="n">out_param</span> <span class="err">$</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">ring</span> <span class="n">A</span> <span class="o">:=</span>
</pre></div>


<p>this is trouble, because this will make <code>ring A</code> typeclass problems go looking for instances of <code>algebra ? A</code></p>
</blockquote>
<p>Can someone explain this to me? I don't know how the type class machine works <em>at all</em> and I would really like to know what its algorithm is.</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151258929):
<p>Maybe what I need is some abstract examples of classes and instances and an explanation of what typeclass inference does to solve typeclass problems, and also an example of how type class inference can get into trouble and cause one of those huge log files which ends up in a max class instance resolution error.</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151258959):
<p>If this isn't going to change in Lean 4 then perhaps it's worth documenting how all this works a bit better. Currently I just regard it as magic, but as Kenny once informed me, Lean does not do magic.</p>

#### [ Kenny Lau (Dec 10 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151259223):
<p>well in the future a neural network will resolve typeclass issues and none of us would know the algorithm</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151259284):
<p>So Lean 7 does do magic after all.</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151259301):
<p>But how does Lean 7 resolve the problem that it can find two non-defeq instances of <code>topological_space X \times Y</code> when <code>X</code> and <code>Y</code> are both metric spaces?</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151259312):
<p>There is a fundamental issue unrelated to algorithms.</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151259376):
<p>Can we feed useful theorems into the network and tell it to try applying them whenever it can't resolve type class issues? "If you can't prove that <code>instance1 : foo A</code> and <code>instance2 : foo A</code> are defeq, take look at the useful theorems about terms of type <code>foo A</code> which I told you about".</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151259384):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> am I living in a dream world?</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151259442):
<p>This happens to mathematicians in practice, in particular in cases where <code>foo A</code> is a subsingleton and not a prop, and the two terms are not defeq but are trivially equal.</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151259451):
<p>We want to do hard algebra in Lean but we cannot do it in a natural way and also use the typeclass system because our structures seem to be slightly too complex for it.</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151259503):
<p>Well -- maybe we can use it -- maybe we just didn't figure out how to use it yet.</p>

#### [ Sebastian Ullrich (Dec 10 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151259599):
<p>Type classes only work well when all instances are unique. In other languages this property is enforced, but Lean's type class inference is too general to implement that in a sensible way.</p>

#### [ Sebastian Ullrich (Dec 10 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151259686):
<p>I haven't followed these threads closely enough to say what should be done about the examples that don't satisfy this property right now</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151260066):
<p>By "unique" you mean that any two instances are defeq, I guess. Could you imagine a strengthening of the system which could handle non-defeq instances which are equal because of a theorem which the type class system "knows" ? Or is this just somehow completely computationally unfeasible? The simplest case is when the class is a subsingleton.</p>

#### [ Sebastian Ullrich (Dec 10 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151260884):
<p>The type class system doesn't even know anything about definitional equality, it just uses the same unification as any other part of Lean. I'm not sure if it would be weird to add some sense of definitional extensionality to just this one part of the system, or what that should look like.</p>

#### [ Patrick Massot (Dec 10 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151261422):
<p>What about the following modification: if the type class search terminally fails (not an intermediate fail during exploration), unfold the head symbol and try again? It seems to me this would make the type wrapping solution much more usable.</p>

#### [ Sebastian Ullrich (Dec 10 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151261745):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> The failed inference can involve many other classes, should they also be unfolded if possible? No, if you want a def to be unfolded by type class inference, it should be reducible.</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151261760):
<p>Can one locally mark a def as reducible?</p>

#### [ Patrick Massot (Dec 10 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151261761):
<p>I don't want it to be reducible, I want is to be unfolded only in the situation I described</p>

#### [ Patrick Massot (Dec 10 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151261816):
<p>This is strictly an extension of the current algorithm, it takes over after everything else failed, and start again on a different problem</p>

#### [ Kevin Buzzard (Dec 10 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151261829):
<p>By "failure" you presumably do you not include "max type class instance resolution reached", which might just mean it's not trying hard enough.</p>

#### [ Patrick Massot (Dec 10 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151261851):
<p>Excluding maxdepth error</p>

#### [ Patrick Massot (Dec 10 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151261904):
<p>My vague understanding is that Coq canonical structure instance resolution does what I wrote</p>

#### [ Patrick Massot (Dec 10 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151261985):
<p>By the way, Sebastian, would it make sense to add shortcuts for the instance problems that Lean keeps solving for each proof (like <code>has_bind tactic</code> or <code>has_one ℕ</code> or <code>has_add ℕ</code>)?</p>

#### [ Sebastian Ullrich (Dec 10 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151266117):
<blockquote>
<p>By the way, Sebastian, would it make sense to add shortcuts for the instance problems that Lean keeps solving for each proof (like <code>has_bind tactic</code> or <code>has_one ℕ</code> or <code>has_add ℕ</code>)?</p>
</blockquote>
<p>Shortcut instances are a valid optimization, though they can also increase run time when the subproblem fails (whereas the full problem could still succeed) because there simply are more instances to check. In theory, better caching could also help there, which is the one part of the type class system that's likely to change in Lean 4.</p>

#### [ Kenny Lau (Dec 10 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151266186):
<p>how is the Lean 4 system better?</p>

#### [ Sebastian Ullrich (Dec 10 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20algebras/near/151266584):
<p>I don't know, it hasn't changed yet</p>


{% endraw %}
