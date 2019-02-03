---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26316inequalityproof.html
---

## Stream: [general](index.html)
### Topic: [inequality proof](26316inequalityproof.html)

---


{% raw %}
#### [ Kevin Sullivan (Sep 14 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133955902):
<p>What is the simplest exact proof term that proves ~0=1 (not zero equals one)?</p>

#### [ Kevin Sullivan (Sep 14 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133956061):
<p>I.e., without tactics complete this: theorem zneqo: not 0 = 1 := _</p>

#### [ Rob Lewis (Sep 14 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133956252):
<p><code>zero_ne_one</code></p>

#### [ Rob Lewis (Sep 14 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133956802):
<p>Oh, wait, there's a better one, although it may not count depending on what you call an "exact proof term."</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">zneqo</span> <span class="o">:</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">0</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span><span class="bp">.</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">zneqo</span>
</pre></div>

#### [ Kenny Lau (Sep 14 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133956828):
<p>dec_trivial</p>

#### [ Rob Lewis (Sep 14 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133957509):
<p><code>dec_trivial</code> is notation for a tactic though.</p>

#### [ Kenny Lau (Sep 14 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133957581):
<p>dec_trivial isn't a tactic</p>

#### [ Rob Lewis (Sep 14 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133957629):
<p>It's notation for <code>of_as_true (by tactic.triv)</code></p>

#### [ Kenny Lau (Sep 14 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133958450):
<p>heh...</p>

#### [ Kevin Sullivan (Sep 14 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133958695):
<p>Right. I'm really looking for the proof term that I'd write to fill in the _. It'd presumably say something about injectivity of constructors.</p>

#### [ Rob Lewis (Sep 14 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133958745):
<p>That's what the <code>.</code> proof is doing under the hood. Look at the proof term it generates.</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">zneqo</span> <span class="o">:</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">0</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span><span class="bp">.</span>
<span class="bp">#</span><span class="kn">print</span> <span class="n">zneqo</span>
</pre></div>

#### [ Kevin Sullivan (Sep 14 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133958775):
<blockquote>
<p>Oh, wait, there's a better one, although it may not count depending on what you call an "exact proof term."</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">zneqo</span> <span class="o">:</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">0</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span><span class="bp">.</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">zneqo</span>
</pre></div>


</blockquote>
<p>Right, I'm really looking for the proof term that I'd use to fill in the _. Presumably something about injectivity of constructors. Also, where is it documented that and how Lean accepts your version?</p>

#### [ Reid Barton (Sep 14 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133958894):
<p>This is the <code>no_confusion</code> stuff right?</p>

#### [ Reid Barton (Sep 14 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133959044):
<p>The strategy is: you can define a function <code>t : nat \to Prop</code> which sends <code>nat.zero</code> to <code>false</code> and <code>nat.succ _</code> to <code>true</code> (using <code>nat.cases</code>). Then if you had an equality <code>nat.zero = nat.succ x</code>, you could use it to transport <code>trivial : true</code> to a proof of <code>false</code></p>

#### [ Rob Lewis (Sep 14 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133959061):
<p>It's an empty pattern match. I guess it's documented somewhere in TPiL, but I couldn't tell you where. The only proof that <code>0 = 1</code> is by <code>rfl</code>, but this is structurally impossible, and the equation compiler fills in the <code>no_confusion</code> proof automatically.</p>

#### [ Reid Barton (Sep 14 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133959100):
<p>I think if you look for <code>no_confusion</code> in TPiL you might be able to find it</p>

#### [ Kenny Lau (Sep 14 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133959429):
<div class="codehilite"><pre><span></span><span class="n">prelude</span>

<span class="kn">inductive</span> <span class="n">nat</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">zero</span> <span class="o">:</span> <span class="n">nat</span>
<span class="bp">|</span> <span class="n">succ</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="n">nat</span>

<span class="kn">inductive</span> <span class="n">eq</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="n">refl</span> <span class="o">:</span> <span class="n">eq</span> <span class="n">x</span>

<span class="kn">inductive</span> <span class="n">false</span> <span class="o">:</span> <span class="n">Sort</span> <span class="mi">0</span><span class="bp">.</span>

<span class="n">def</span> <span class="n">strange_prop</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span> <span class="n">Sort</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="n">nat</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">n</span> <span class="o">(</span><span class="n">eq</span> <span class="n">nat</span><span class="bp">.</span><span class="n">zero</span> <span class="n">nat</span><span class="bp">.</span><span class="n">zero</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">n</span> <span class="bp">_</span><span class="o">,</span> <span class="n">false</span><span class="o">)</span>

<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="n">eq</span> <span class="n">nat</span><span class="bp">.</span><span class="n">zero</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">nat</span><span class="bp">.</span><span class="n">zero</span><span class="o">))</span> <span class="bp">→</span> <span class="n">false</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="k">show</span> <span class="n">strange_prop</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">nat</span><span class="bp">.</span><span class="n">zero</span><span class="o">),</span>
<span class="k">from</span> <span class="n">eq</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">H</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="n">nat</span><span class="bp">.</span><span class="n">zero</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Sep 14 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133959494):
<p>also see <a href="https://xenaproject.wordpress.com/2018/03/24/no-confusion-over-no_confusion/" target="_blank" title="https://xenaproject.wordpress.com/2018/03/24/no-confusion-over-no_confusion/">this</a> blogpost by kevin</p>

#### [ Kenny Lau (Sep 14 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133959561):
<p>(I followed Reid Barton's idea)</p>

#### [ Kevin Sullivan (Sep 15 2018 at 05:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133993284):
<blockquote>
<p>That's what the <code>.</code> proof is doing under the hood. Look at the proof term it generates.</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">zneqo</span> <span class="o">:</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">0</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span><span class="bp">.</span>
<span class="bp">#</span><span class="kn">print</span> <span class="n">zneqo</span>
</pre></div>


</blockquote>
<p>Sorry, here's a better response.</p>
<p>First, the proof term is: λ (a : 0 = 1), eq.dcases_on a (λ (a_1 : 1 = 0), nat.no_confusion a_1) (eq.refl 1) (heq.refl a)</p>
<p>However, when I copy and paste it in place of the underscore, after the :=, I get the following error. Still not sure exactly what I need to type after the := as an exact proof term.</p>
<p>[Lean]<br>
"eliminator" elaborator type mismatch, term<br>
  λ (a_1 : 1 = 0), nat.no_confusion a_1<br>
has type<br>
  1 = 0 → nat.no_confusion_type (_ == _ → false) 1 0<br>
but is expected to have type<br>
  0 = 0 → _ == _ → false<br>
Additional information:<br>
/Users/sullivan/teaching/2102f18/cs-dm.sullivan/06_Negation/00_intro.lean:60:40: context: the inferred motive for the eliminator-like application is<br>
  λ (_x : ℕ) (_x_1 : 0 = _x), _x = _x → _x_1 == _x_1 → false<br>
eq.dcases_on : ∀ {α : Type} {a : α} {C : Π (a_1 : α), a = a_1 → Prop} {a_1 : α} (n : a = a_1), C a _ → C a_1 n</p>

#### [ Andrew Ashworth (Sep 15 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/133998674):
<p><code>example : 0 ≠ 1 := λ h, nat.no_confusion h</code></p>

#### [ Kevin Sullivan (Sep 15 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inequality%20proof/near/134026746):
<blockquote>
<p><code>example : 0 ≠ 1 := λ h, nat.no_confusion h</code></p>
</blockquote>
<p>Thank you. That got me where I needed to go.</p>


{% endraw %}
