---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/63417ccissopowerful.html
---

## Stream: [general](index.html)
### Topic: [cc is so powerful](63417ccissopowerful.html)

---


{% raw %}
#### [ Kenny Lau (Apr 21 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125493933):
<p><code>cc</code> resolved the following:</p>
<div class="codehilite"><pre><span></span><span class="n">x1</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span>
<span class="n">b1</span> <span class="o">:</span> <span class="n">bool</span><span class="o">,</span>
<span class="n">x2</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span>
<span class="n">b2</span> <span class="o">:</span> <span class="n">bool</span><span class="o">,</span>
<span class="n">H2</span> <span class="o">:</span> <span class="o">(</span><span class="n">x1</span><span class="o">,</span> <span class="n">b1</span><span class="o">)</span> <span class="bp">≠</span> <span class="o">(</span><span class="n">x2</span><span class="o">,</span> <span class="n">b2</span><span class="o">),</span>
<span class="n">L</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">),</span>
<span class="n">H3</span> <span class="o">:</span> <span class="n">L</span> <span class="bp">=</span> <span class="o">(</span><span class="n">x1</span><span class="o">,</span> <span class="n">b1</span><span class="o">)</span> <span class="bp">::</span> <span class="n">L₃</span><span class="o">,</span>
<span class="n">H4</span> <span class="o">:</span> <span class="n">L</span> <span class="bp">=</span> <span class="o">(</span><span class="n">x2</span><span class="o">,</span> <span class="n">b2</span><span class="o">)</span> <span class="bp">::</span> <span class="n">L₄</span>
<span class="err">⊢</span> <span class="n">red</span> <span class="n">L₃</span> <span class="o">((</span><span class="n">x1</span><span class="o">,</span> <span class="n">bnot</span> <span class="n">b1</span><span class="o">)</span> <span class="bp">::</span> <span class="n">L</span><span class="o">)</span>
</pre></div>


<p>which makes me wonder how <code>cc</code> works</p>

#### [ Kenny Lau (Apr 21 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125493934):
<p>The docs say that it attempts to synthesize an empty inductive type</p>

#### [ Kenny Lau (Apr 21 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125493939):
<p>but it doesn't say how it achieves it</p>

#### [ Kenny Lau (Apr 21 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125493940):
<p>the printed theorem says:</p>
<div class="codehilite"><pre><span></span><span class="n">false</span><span class="bp">.</span><span class="n">elim</span>
         <span class="o">(</span><span class="n">false_of_true_eq_false</span>
            <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">trans</span>
               <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">symm</span>
                  <span class="o">(</span><span class="n">eq_true_intro</span>
                     <span class="o">(</span><span class="n">and</span><span class="bp">.</span><span class="n">elim_left</span>
                        <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">no_confusion</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="n">H3</span><span class="o">)</span> <span class="n">H4</span><span class="o">)</span>
                           <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">hd_eq</span> <span class="o">:</span> <span class="o">(</span><span class="n">x1</span><span class="o">,</span> <span class="n">b1</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">x2</span><span class="o">,</span> <span class="n">b2</span><span class="o">))</span> <span class="o">(</span><span class="n">tl_eq</span> <span class="o">:</span> <span class="n">L₃</span> <span class="bp">=</span> <span class="n">L₄</span><span class="o">),</span> <span class="bp">⟨</span><span class="n">hd_eq</span><span class="o">,</span> <span class="n">tl_eq</span><span class="bp">⟩</span><span class="o">)))))</span>
               <span class="o">(</span><span class="n">eq_false_intro</span> <span class="n">H2</span><span class="o">))))</span>
</pre></div>

#### [ Simon Hudon (Apr 21 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494189):
<p>I think it does so by building an equality matching graph. It's a graph where the vertices are terms and they are linked by edges if they  are known to be equal. Once you've added all the equalities in your context, you take the transitive closure of the graph and, for each connected component (i.e. equivalence class) you can elect a term that will represent the whole class and replace every occurrence of every member of that class by that one representative.</p>

#### [ Simon Hudon (Apr 21 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494190):
<p>It's a very algorithmic proof technique</p>

#### [ Kenny Lau (Apr 21 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494191):
<p>very interesting</p>

#### [ Kenny Lau (Apr 21 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494193):
<p>but the transitive closure isn't necessarily decidable?</p>

#### [ Simon Hudon (Apr 21 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494235):
<p>It is because you're only considering the finite set of terms that are visible in your context (and some variation on each)</p>

#### [ Kenny Lau (Apr 21 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494236):
<p>hmm</p>

#### [ Gabriel Ebner (Apr 21 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494530):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Congruence closure does one more thing: it closes these equivalences under congruence.  For example if you know <code>a=b</code> and have two subterms <code>f a</code> and <code>f b</code>, then it will deduce <code>f a = f b</code>.</p>

#### [ Kenny Lau (Apr 21 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494532):
<p>is there any paper regarding this?</p>

#### [ Simon Hudon (Apr 21 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494580):
<p>Thanks for adding this detail! I could only think of it in algorithmic terms and that didn't seem enlightening. But your explanation is nice</p>

#### [ Gabriel Ebner (Apr 21 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494581):
<p>I don't know a canonical citation off the top of my head, it's pretty standard stuff.  Give me a sec.</p>

#### [ Kenny Lau (Apr 21 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494590):
<p>thanks</p>

#### [ Gabriel Ebner (Apr 21 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494591):
<p>Nelson, Oppen, Fast decision procedures based on congruence closure, Journal of the ACM (1980) <a href="http://www.cs.colorado.edu/~bec/courses/csci5535-s09/reading/nelson-oppen-congruence.pdf" target="_blank" title="http://www.cs.colorado.edu/~bec/courses/csci5535-s09/reading/nelson-oppen-congruence.pdf">http://www.cs.colorado.edu/~bec/courses/csci5535-s09/reading/nelson-oppen-congruence.pdf</a></p>

#### [ Gabriel Ebner (Apr 21 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494634):
<p>The congruence lemmas for dependent type theory as used in Lean are described in this paper (de Moura, Selsam IJCAR 2016): <a href="https://leanprover.github.io/papers/congr.pdf" target="_blank" title="https://leanprover.github.io/papers/congr.pdf">https://leanprover.github.io/papers/congr.pdf</a></p>

#### [ Patrick Massot (Apr 21 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494642):
<p>I'm always hesitant to try to read Lean papers because I always fear they will be outdated (say Lean 2 era or worse) and only confuse me</p>

#### [ Gabriel Ebner (Apr 21 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494643):
<p>The <code>cc</code> implementation in Lean does a few more tricks: for example it derives <code>a=b</code> from <code>nat.succ a = nat.succ b</code>, and <code>nat.succ a != nat.zero</code> for any <code>a</code>.</p>

#### [ Patrick Massot (Apr 21 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494644):
<p>Do you have something like a list of still relevant Lean papers?</p>

#### [ Kenny Lau (Apr 21 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494684):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">f</span> <span class="o">(</span><span class="n">f</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">))</span> <span class="bp">=</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">f</span> <span class="o">(</span><span class="n">f</span> <span class="o">(</span><span class="n">f</span> <span class="o">(</span><span class="n">f</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">))))</span> <span class="bp">=</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">cc</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">test</span>
<span class="c">/-</span><span class="cm">of_eq_true</span>
<span class="cm">    (eq_true_intro</span>
<span class="cm">       (eq.trans</span>
<span class="cm">          (eq_of_heq</span>
<span class="cm">             ((λ (a a&#39; : α) (e_0 : a = a&#39;), eq.rec (heq.refl (f a)) e_0) x (f (f x))</span>
<span class="cm">                (eq.trans (eq.symm H2)</span>
<span class="cm">                   (eq_of_heq</span>
<span class="cm">                      ((λ (a a&#39; : α) (e_0 : a = a&#39;), eq.rec (heq.refl (f a)) e_0) (f (f (f (f x)))) (f x)</span>
<span class="cm">                         (eq_of_heq</span>
<span class="cm">                            ((λ (a a&#39; : α) (e_0 : a = a&#39;), eq.rec (heq.refl (f a)) e_0) (f (f (f x))) x H1)))))))</span>
<span class="cm">          H1))-/</span>
</pre></div>

#### [ Patrick Massot (Apr 21 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494713):
<p>Wow</p>

#### [ Kenny Lau (Apr 21 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494739):
<p>(taken from P.1 of the first linked paper)</p>

#### [ Gabriel Ebner (Apr 21 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494856):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span>   Let me look through the publication list at <a href="https://leanprover.github.io/publications/" target="_blank" title="https://leanprover.github.io/publications/">https://leanprover.github.io/publications/</a>.  The system description is pretty high-level and only obsolete in details.  The metaprogramming paper is new and describes Lean 3.2.  The machine learning paper doesn't seem to talk much about Lean. The congruence closure paper seems to be still relevant.  The elaboration paper is completely obsolete as it describes Lean 2.</p>

#### [ Kenny Lau (Apr 21 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494858):
<blockquote>
<p>The congruence lemmas for dependent type theory as used in Lean are described in this paper (de Moura, Selsam IJCAR 2016): <a href="https://leanprover.github.io/papers/congr.pdf" target="_blank" title="https://leanprover.github.io/papers/congr.pdf">https://leanprover.github.io/papers/congr.pdf</a></p>
</blockquote>
<p>of <em>course</em> it is de moura :P</p>

#### [ Patrick Massot (Apr 21 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494992):
<p>Thanks</p>

#### [ Patrick Massot (Apr 21 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495002):
<p>So actually the obsolete one is clearly flagged Lean 2 on  <a href="https://leanprover.github.io/publications/" target="_blank" title="https://leanprover.github.io/publications/">https://leanprover.github.io/publications/</a></p>

#### [ Patrick Massot (Apr 21 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495043):
<p>It reminds me a question: what is the status of <code>super</code> today?</p>

#### [ Patrick Massot (Apr 21 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495101):
<p>And these <code>crush</code> things mentioned in the metaprogramming paper and some slides?</p>

#### [ Gabriel Ebner (Apr 21 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495203):
<p><code>super</code> never progressed beyond a proof of concept.  From my point of view, the main thing holding it back is performance.  Some APIs that would be very nice to do e.g. resolution with unification (such as temporary metavariables) are simply not available from the metaprogramming side.  And I have enough other things to do.  Maybe I will revisit <code>super</code> when Lean 4 arrives.</p>

#### [ Gabriel Ebner (Apr 21 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495211):
<p><code>crush</code> is available as a package: <a href="https://github.com/leanprover/mini_crush" target="_blank" title="https://github.com/leanprover/mini_crush">https://github.com/leanprover/mini_crush</a></p>

#### [ Gabriel Ebner (Apr 21 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495213):
<p><code>rsimp</code> is in the core library</p>

#### [ Simon Hudon (Apr 21 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495253):
<p>What does <code>rsimp</code> do?</p>

#### [ Gabriel Ebner (Apr 21 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495262):
<p>Re: <code>super</code>.  This was the first thing I did with Lean, and at the time I did not know about typeclasses, simp lemmas, the equation compiler, etc.  It did not help that the Lean 3 library at the time did not even have more than a few theorems about natural numbers.</p>

#### [ Gabriel Ebner (Apr 21 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495316):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span>: <code>rsimp</code> is Leo's idea on how to do simplification with congruence closure.  As you've observed, <code>cc</code> stores the equivalence classes of subterms.  Roughly, <code>rsimp</code> then applies simp lemmas on the subterms, and traverses the equivalence classes to pick the smallest subterm as a result.</p>

#### [ Gabriel Ebner (Apr 21 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495366):
<p>The main advantage compared to <code>simp</code> is that it doesn't loop (so easily).  For example, <code>simp*</code> would loop on <code>a=b, b=a :- f a = f b</code> but <code>rsimp</code> would not.</p>

#### [ Kenny Lau (Apr 21 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495368):
<p>why would it not loop on a=b b=a?</p>

#### [ Simon Hudon (Apr 21 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495371):
<p>That is so cool :) Is there a downside to using <code>rsimp</code> instead of <code>simp</code>?</p>

#### [ Gabriel Ebner (Apr 21 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495461):
<p>Just looked back at the paper and apparently I remembered it incorrectly, <code>rsimp</code> uses E-matching to instantiate lemmas instead of <code>simp</code>.  So in the example above, <code>rsimp</code> is essentially <code>cc</code>.</p>

#### [ Patrick Massot (Apr 21 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495466):
<p>Thanks. Indeed it sounds like <code>super</code> needs to wait for Lean 4.</p>

#### [ Gabriel Ebner (Apr 21 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495501):
<p>Maybe more interestingly: if you call rsimp on <code>a=b, a=f a :- p (f (f a))</code> then rsimp would simplify the goal to <code>p a</code> (or <code>p b</code>, randomly).</p>

#### [ Kenny Lau (Apr 21 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495512):
<p>I found that <code>cc</code> automatically does <code>intros</code></p>

#### [ Kenny Lau (Apr 21 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495513):
<p>I was wondering if it rewrote the conditions like <code>simp</code> does</p>

#### [ Kenny Lau (Apr 21 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495514):
<p>I think that's less efficient so I don't prefer it rewriting the conditions</p>

#### [ Kenny Lau (Apr 21 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495553):
<p>so I like <code>cc</code> more :P</p>

#### [ Gabriel Ebner (Apr 21 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495554):
<blockquote>
<p>I was wondering if it rewrote the conditions like <code>simp</code> does</p>
</blockquote>
<p>What do mean by "rewriting conditions"?</p>

#### [ Kenny Lau (Apr 21 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495555):
<p>so the goal is <code>A -&gt; B</code></p>

#### [ Kenny Lau (Apr 21 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495557):
<p>simp would rewrite <code>A</code> to <code>C</code> without intro right</p>

#### [ Gabriel Ebner (Apr 21 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495661):
<p>I'm not sure if there is a meaningful difference in efficiency here.  The reason why <code>simp</code> does not do <code>intros</code> is because <code>simp</code> may not close the goal and you don't want <code>simp</code> to intro stuff randomly.  On the other hand, <code>cc</code> is an end-game tactic and can do whatever it wants.</p>

#### [ Kenny Lau (Apr 21 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495707):
<p>I see</p>


{% endraw %}
