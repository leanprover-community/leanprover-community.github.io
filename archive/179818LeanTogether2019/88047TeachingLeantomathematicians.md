---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/179818LeanTogether2019/88047TeachingLeantomathematicians.html
---

## Stream: [Lean Together 2019](index.html)
### Topic: [Teaching Lean to mathematicians](88047TeachingLeantomathematicians.html)

---


{% raw %}
#### [ Kevin Buzzard (Jan 06 2019 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154532336):
<p>I have been thinking for a while now about how to teach Lean to absolute beginners, because that is currently the bottleneck we have at Imperial -- not enough people able to get started. Gabriel and I are running a teaching session tomorrow 0900-1030 and 1100-1200 and some people have confessed to knowing no Lean at all, which is of course absolutely fine, but how to get them started?</p>
<p>My boys like learning through puzzle-solving. So here are some puzzles:</p>
<p><a href="https://github.com/kbuzzard/mathematics-in-lean" target="_blank" title="https://github.com/kbuzzard/mathematics-in-lean">https://github.com/kbuzzard/mathematics-in-lean</a></p>

#### [ Kevin Buzzard (Jan 06 2019 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154532337):
<p>The problem is that if you know no Lean at all, even these problems are too hard. You have to install Lean, and then how do you fill in the sorry?</p>

#### [ Kevin Buzzard (Jan 06 2019 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154532342):
<p>So there is some stuff which helps with that here:</p>
<p><a href="http://wwwf.imperial.ac.uk/~buzzard/lean_together/source/leantogether.html" target="_blank" title="http://wwwf.imperial.ac.uk/~buzzard/lean_together/source/leantogether.html">http://wwwf.imperial.ac.uk/~buzzard/lean_together/source/leantogether.html</a></p>

#### [ Kevin Buzzard (Jan 06 2019 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154532354):
<p>This is some teaching material written in sphinx.</p>

#### [ Kenny Lau (Jan 06 2019 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154532362):
<p>I mean, Lean is intended for CS majors..</p>

#### [ Gabriel Ebner (Jan 06 2019 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154532432):
<blockquote>
<p>I mean, Lean is intended for CS majors..</p>
</blockquote>
<p>Lean is definitely not intended for CS majors only.  Isn't the whole point of this workshop/project to get mathematicians to like Lean?</p>

#### [ Patrick Massot (Jan 06 2019 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154532551):
<p>to get <em>more</em> mathematicians to like Lean</p>

#### [ Kevin Buzzard (Jan 06 2019 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154532552):
<p>And there's a very poor quality video which I made on my own laptop, and which is a bit laughable in places, but it's currently the best I've got. It's sort of an advert for what an absolute beginner can aspire to.</p>
<p><a href="http://wwwf.imperial.ac.uk/~buzzard/lean_together/lean_intro.mp4" target="_blank" title="http://wwwf.imperial.ac.uk/~buzzard/lean_together/lean_intro.mp4">http://wwwf.imperial.ac.uk/~buzzard/lean_together/lean_intro.mp4</a></p>
<p>Videos are a pain to make, I want to zoom into various bits of the screen etc, and I know how to do all of this in theory but it would take me absolutely hours to make it exactly how I want it.</p>

#### [ Kenny Lau (Jan 06 2019 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154532607):
<p>you can certainly give a side (or interface) of Lean that is more suitable for mathematicians, but it won't change the fact that Lean is built for CS majors</p>

#### [ Patrick Massot (Jan 06 2019 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154532610):
<p>Should we  play the video tomorrow morning in case you have difficulties getting up on time?</p>

#### [ Kenny Lau (Jan 06 2019 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154532618):
<p>How would you understand structural induction if you're just some regular mathematician who never thinks about logic</p>

#### [ Sebastian Ullrich (Jan 06 2019 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154532665):
<p>You think most CS majors think about logic?</p>

#### [ Johan Commelin (Jan 07 2019 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154546873):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I like the video!</p>

#### [ Kevin Buzzard (Jan 07 2019 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154564805):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">ring</span>

<span class="kn">inductive</span> <span class="n">is_even</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">zero</span> <span class="o">:</span> <span class="n">is_even</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="n">step</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">:</span> <span class="n">is_even</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">is_even</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">2</span><span class="o">)</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">is_even</span> <span class="mi">4</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">repeat</span> <span class="o">{</span> <span class="n">apply</span> <span class="n">is_even</span><span class="bp">.</span><span class="n">step</span> <span class="o">},</span>
<span class="n">apply</span> <span class="n">is_even</span><span class="bp">.</span><span class="n">zero</span><span class="o">,</span>
<span class="kn">end</span>

<span class="kn">example</span> <span class="o">:</span> <span class="bp">¬</span> <span class="n">is_even</span> <span class="mi">5</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">intro</span> <span class="n">even_five</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">even_five</span> <span class="k">with</span> <span class="bp">_</span> <span class="n">even_three</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">even_three</span> <span class="k">with</span> <span class="bp">_</span> <span class="n">even_one</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">even_one</span><span class="o">,</span>
<span class="kn">end</span>

<span class="kn">lemma</span> <span class="n">even_if_double</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">:</span> <span class="n">is_even</span> <span class="o">(</span><span class="mi">2</span><span class="bp">*</span><span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">induction</span> <span class="n">n</span> <span class="k">with</span> <span class="n">d</span> <span class="n">hd</span><span class="o">,</span>
<span class="o">{</span> <span class="n">exact</span> <span class="n">is_even</span><span class="bp">.</span><span class="n">zero</span> <span class="o">},</span>
<span class="o">{</span> <span class="k">show</span> <span class="n">is_even</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">*</span> <span class="o">(</span><span class="n">d</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)),</span>
  <span class="n">rw</span> <span class="n">mul_add</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">is_even</span><span class="bp">.</span><span class="n">step</span><span class="o">,</span>
  <span class="n">assumption</span><span class="o">,</span>
 <span class="o">},</span>
<span class="kn">end</span>

<span class="kn">lemma</span> <span class="n">double_if_even</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">:</span> <span class="n">is_even</span> <span class="n">n</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">m</span><span class="o">,</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">2</span><span class="bp">*</span><span class="n">m</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">intro</span> <span class="n">h</span><span class="o">,</span> <span class="n">induction</span> <span class="n">h</span> <span class="k">with</span> <span class="n">d</span> <span class="n">Hd</span> <span class="n">ih</span><span class="o">,</span>
<span class="o">{</span> <span class="n">use</span> <span class="mi">0</span><span class="o">,</span>
  <span class="n">refl</span>
<span class="o">},</span>
<span class="o">{</span> <span class="n">cases</span> <span class="n">ih</span> <span class="k">with</span> <span class="n">n</span> <span class="n">Hn</span><span class="o">,</span>
  <span class="n">use</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">),</span>
  <span class="n">rw</span> <span class="n">Hn</span><span class="o">,</span>
  <span class="n">refl</span><span class="o">,</span>
 <span class="o">}</span>
<span class="kn">end</span>

<span class="kn">lemma</span> <span class="n">even_iff_double</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">:</span> <span class="n">is_even</span> <span class="n">n</span> <span class="bp">↔</span> <span class="bp">∃</span> <span class="n">m</span><span class="o">,</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">2</span><span class="bp">*</span><span class="n">m</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">split</span><span class="o">,</span> <span class="n">apply</span> <span class="n">double_if_even</span><span class="o">,</span>
<span class="n">intro</span> <span class="n">h</span><span class="o">,</span> <span class="n">cases</span> <span class="n">h</span> <span class="k">with</span> <span class="n">d</span> <span class="n">Hd</span><span class="o">,</span> <span class="n">rw</span> <span class="n">Hd</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">even_if_double</span>
<span class="kn">end</span>

<span class="kn">inductive</span> <span class="n">is_odd</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">one</span> <span class="o">:</span> <span class="n">is_odd</span> <span class="mi">1</span>
<span class="bp">|</span> <span class="n">step</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">:</span> <span class="n">is_odd</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">is_odd</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">2</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">odd_iff_double_add_one</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">:</span> <span class="n">is_odd</span> <span class="n">n</span> <span class="bp">↔</span> <span class="bp">∃</span> <span class="n">m</span><span class="o">,</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">2</span><span class="bp">*</span><span class="n">m</span> <span class="bp">+</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="n">sorry</span>

<span class="kn">lemma</span> <span class="n">even_of_not_odd</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span>
<span class="bp">¬</span> <span class="n">is_odd</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">is_even</span> <span class="n">n</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="n">h</span> <span class="o">:=</span> <span class="n">is_even</span><span class="bp">.</span><span class="n">zero</span>
<span class="bp">|</span> <span class="mi">1</span> <span class="n">h</span> <span class="o">:=</span> <span class="k">begin</span> <span class="n">exfalso</span><span class="o">,</span> <span class="n">apply</span> <span class="n">h</span><span class="o">,</span> <span class="n">constructor</span> <span class="kn">end</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">2</span><span class="o">)</span> <span class="n">h</span> <span class="o">:=</span>
  <span class="k">have</span> <span class="n">ih</span> <span class="o">:</span> <span class="bp">_</span><span class="o">,</span> <span class="k">from</span> <span class="n">even_of_not_odd</span> <span class="n">n</span><span class="o">,</span>
  <span class="k">begin</span>
  <span class="n">constructor</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">ih</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">hn</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">constructor</span><span class="o">,</span> <span class="n">assumption</span><span class="o">,</span>
  <span class="kn">end</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">even_of_not_odd</span>

<span class="kn">lemma</span> <span class="n">not_odd_of_even</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">is_even</span> <span class="n">n</span> <span class="bp">→</span> <span class="bp">¬</span> <span class="n">is_odd</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">intros</span> <span class="n">n</span> <span class="n">h</span><span class="o">,</span>
<span class="n">induction</span> <span class="n">h</span> <span class="k">with</span> <span class="n">m</span> <span class="n">m</span> <span class="n">hm</span><span class="o">,</span>
<span class="o">{</span><span class="n">intro</span> <span class="n">h</span><span class="o">,</span> <span class="n">cases</span> <span class="n">h</span><span class="o">},</span>
<span class="o">{</span><span class="n">intro</span> <span class="n">h</span><span class="o">,</span> <span class="n">apply</span> <span class="n">hm</span><span class="o">,</span> <span class="n">cases</span> <span class="n">h</span><span class="o">,</span> <span class="n">assumption</span><span class="o">},</span>
<span class="kn">end</span>

<span class="kn">lemma</span> <span class="n">even_iff_not_odd</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">is_even</span> <span class="n">n</span> <span class="bp">↔</span> <span class="bp">¬</span> <span class="n">is_odd</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">intro</span> <span class="n">n</span><span class="o">,</span> <span class="n">split</span><span class="o">,</span> <span class="n">apply</span> <span class="n">not_odd_of_even</span><span class="o">,</span> <span class="n">apply</span> <span class="n">even_of_not_odd</span>
<span class="kn">end</span>

<span class="kn">lemma</span> <span class="n">odd_square</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">is_odd</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">is_odd</span> <span class="o">(</span><span class="n">n</span><span class="bp">*</span><span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">simp</span> <span class="o">[</span><span class="n">odd_iff_double_add_one</span><span class="o">],</span>
<span class="n">intro</span> <span class="n">m</span><span class="o">,</span>
<span class="n">intros</span>  <span class="n">h</span><span class="o">,</span>
<span class="n">use</span> <span class="mi">2</span><span class="bp">*</span><span class="n">m</span> <span class="bp">+</span> <span class="mi">2</span><span class="bp">*</span><span class="n">m</span><span class="bp">*</span><span class="n">m</span><span class="o">,</span> <span class="n">subst</span> <span class="n">h</span><span class="o">,</span> <span class="n">ring</span><span class="o">,</span>
<span class="kn">end</span>

<span class="kn">lemma</span> <span class="n">even_square</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">is_even</span> <span class="o">(</span><span class="n">n</span><span class="bp">*</span><span class="n">n</span><span class="o">)</span> <span class="bp">→</span> <span class="n">is_even</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">conv</span> <span class="k">in</span> <span class="o">(</span><span class="n">is_even</span> <span class="o">(</span><span class="n">n</span><span class="bp">*</span><span class="n">n</span><span class="o">))</span> <span class="o">{</span> <span class="n">simp</span> <span class="o">[</span><span class="n">even_iff_not_odd</span><span class="o">]</span> <span class="o">},</span>
<span class="n">simp</span> <span class="o">[</span><span class="n">even_iff_not_odd</span><span class="o">],</span>
<span class="n">intros</span> <span class="n">h1</span> <span class="n">h2</span><span class="o">,</span> <span class="n">apply</span> <span class="n">h1</span><span class="o">,</span>
<span class="n">apply</span> <span class="n">odd_square</span><span class="o">,</span> <span class="n">assumption</span>
<span class="kn">end</span>

<span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">all</span> <span class="n">true</span>
<span class="bp">#</span><span class="kn">check</span> <span class="o">(</span><span class="mi">7</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span>
</pre></div>


<p>This is what Gabriel and I generated in the second hour of the tutorial</p>

#### [ Kevin Buzzard (Jan 07 2019 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154565129):
<p>If any beginners have any questions about this then feel free to ask.</p>

#### [ Kevin Buzzard (Jan 07 2019 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154566899):
<p><a href="https://github.com/kbuzzard/xena/tree/master/lean_together" target="_blank" title="https://github.com/kbuzzard/xena/tree/master/lean_together">https://github.com/kbuzzard/xena/tree/master/lean_together</a> Random stuff from Monday tutorial</p>

#### [ David Holmes (Jan 07 2019 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154581547):
<p>Does anyone have a hint for the following exercise? The idea is to replace the `sorry' with a proof, as elementary as possible (without importing any libraries, if possible). As you can guess, I'm quite new to this! </p>
<p><code>variables (X : Type) (P Q : X → Prop)</code></p>
<p><code>example : ∀ x, P x ∧ Q x → ∀ x, Q x ∧ P x :=
begin
sorry
end</code></p>
<p>So far I have <br>
<code> intro a, intro G, cases G with PH QH, intro b, split, </code><br>
but then I have a proof of Q a, and I want a proof of Q b. I want to say `but a was arbitrary', but don't know how to do this in Lean... </p>
<p>Thanks very much!</p>

#### [ Kenny Lau (Jan 07 2019 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154581665):
<p>I think you are missing a pair of parentheses</p>

#### [ Rob Lewis (Jan 07 2019 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154581713):
<p>Yes, I think you want to prove <code>(∀ x, P x ∧ Q x) → (∀ x, Q x ∧ P x)</code>, that will be easier!</p>

#### [ David Holmes (Jan 07 2019 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154581797):
<p>Thanks, will try that. The version I gave was Kevin's exercise, so maybe there is a type there.</p>

#### [ Rob Lewis (Jan 07 2019 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154581808):
<p>Note, on Zulip you can format Lean code by enclosing it with  </p>
<div class="codehilite"><pre><span></span>```lean
</pre></div>


<p>and three backticks at the end.</p>

#### [ Kevin Buzzard (Jan 07 2019 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154592069):
<p>Oh many thanks David -- I always forget that \forall is super-greedy. Do you know how computer scientists do BIDMAS by the way?</p>

#### [ Kevin Buzzard (Jan 07 2019 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154594472):
<p>PS did I manage to fix it?</p>

#### [ David Holmes (Jan 07 2019 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154600678):
<p>Yup, looks good (and also the exists one below). I'm almost there, having fun with the final one now... BIDMAS I'm not sure about, but for now I like lots of brackets for certainty!</p>

#### [ Kevin Buzzard (Jan 07 2019 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604138):
<p>Each piece of notation has a number between 0 and about 1000 attached to it (to both sides of it in the case that it's an infix operator like +)</p>

#### [ Kevin Buzzard (Jan 07 2019 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604237):
<p>You can see the numbers using <code>#print notation *</code> or whatever notation you want to understand</p>

#### [ Kevin Buzzard (Jan 07 2019 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604272):
<p>My favourite piece of notation is <code>$</code></p>

#### [ Kevin Buzzard (Jan 07 2019 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604360):
<p>Away from notation, actual functions given by name have a super high number</p>

#### [ Kevin Buzzard (Jan 07 2019 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604397):
<p>You can tell functions from notation because function names are in lower case letters and notation is pretty much everything else</p>

#### [ Kevin Buzzard (Jan 07 2019 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604490):
<p>And then you just say "Pratt parser" and all your inputs are resolved by lean</p>

#### [ Patrick Massot (Jan 07 2019 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604521):
<p>Functions don't have to be lower case letters. But function application indeed has super high priority</p>

#### [ Kevin Buzzard (Jan 07 2019 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604523):
<p>And the CS guys are excited about something in Lean 4 relating to this</p>

#### [ Kevin Buzzard (Jan 07 2019 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604592):
<p>I think because it will make notation cooler or something</p>

#### [ Kevin Buzzard (Jan 07 2019 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604660):
<p>Have you seen the notation for "mod n" is some crazy [ZMOD n] thing? I can't even remember what the notation is, I always have to look it up</p>

#### [ Kevin Buzzard (Jan 07 2019 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604719):
<p>Will this be fixed in Lean 4?</p>

#### [ Kevin Buzzard (Jan 07 2019 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604726):
<p>I had better get back to my talk</p>

#### [ Rob Lewis (Jan 07 2019 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154604915):
<p>The notation for a ≡ b (mod n) when n, a, and b are integers is <code>a ≡ b [ZMOD n]</code>, that hardly seems so crazy.</p>

#### [ Kevin Buzzard (Jan 08 2019 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154609481):
<blockquote>
<p>The notation for a ≡ b (mod n) when n, a, and b are integers is <code>a ≡ b [ZMOD n]</code>, that hardly seems so crazy.</p>
</blockquote>
<p>Why isn't it just <code>a ≡ b mod n</code> ?</p>

#### [ Zans Mihejevs (Jan 08 2019 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154636786):
<blockquote>
<p>The problem is that if you know no Lean at all, even these problems are too hard. You have to install Lean, and then how do you fill in the sorry?</p>
</blockquote>
<p>Hmm,  I know someone who co-wrote a book for teaching haskell to complete beginners (Haskell Book). She might be a good person to talk to!</p>

#### [ Kevin Buzzard (Jan 10 2019 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154832510):
<p><span class="user-mention" data-user-id="198366">@David Holmes</span> complained that the basic logic exercises were too boring :-) [I think in the sense that he felt that the proofs should be done by automation rather than by him]. He liked the canonical nat exercise (defining <code>+ and </code>*<code> and </code>&lt;` and proving basic stuff about them) at <a href="https://xenaproject.wordpress.com/2017/10/31/building-the-non-negative-integers-from-scratch/" target="_blank" title="https://xenaproject.wordpress.com/2017/10/31/building-the-non-negative-integers-from-scratch/">https://xenaproject.wordpress.com/2017/10/31/building-the-non-negative-integers-from-scratch/</a></p>
<p>That exercise involves building a new structure from scratch and then defining functions on it and proving stuff about it. But the new structure relies on nothing at all. Here is a sketch of how to build the complex numbers, given the real numbers.</p>
<p><a href="https://github.com/kbuzzard/xena/blob/master/lean_together/complex.lean" target="_blank" title="https://github.com/kbuzzard/xena/blob/master/lean_together/complex.lean">https://github.com/kbuzzard/xena/blob/master/lean_together/complex.lean</a></p>
<p>Here we need to have mathlib installed, so we can have the reals. Actually probably one could get away with axiomatising the reals here and avoiding mathlib, but I did not do this. If we made a new constant called <code>real</code> and added an axiom that it was a ring, one should be able to prove that the complexes are also a ring, because really we are constructing <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mi>x</mi><mo>]</mo><mi mathvariant="normal">/</mi><mo>(</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>1</mn><mo>)</mo></mrow><annotation encoding="application/x-tex">R[x]/(x^2+1)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:1.064108em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathit">x</span><span class="mclose">]</span><span class="mord mathrm">/</span><span class="mopen">(</span><span class="mord"><span class="mord mathit">x</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span><span class="mbin">+</span><span class="mord mathrm">1</span><span class="mclose">)</span></span></span></span> where <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span> is an arbitrary ring.</p>

#### [ David Holmes (Jan 10 2019 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154863761):
<p>Too boring? Hmm, maybe. I think the problem is that I would have found them painful to do on paper, forgetting lean, because I'm not sure what I should assume and what needs to be proven (for example, it was not immediately clear that I should assume excluded middle, but prove <code>\not (p \and \not p)</code>, just because I am not used to working with these things. Certainly I wouldn't be unhappy to have them done by automation! I did find the exercises with the natural numbers much more fun, because I felt I understood what I was aiming for. Occasionally it felt like fighting with the system, but most of the time things just worked as I hoped. May have a go at the complexes soon...</p>

#### [ David Holmes (Jan 10 2019 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154877253):
<p>Hmm, can I cheat/have a hint? Is there a command to say 'apply the ring structure of the real numbers' without giving every detail? For example, I want to show <code>re a * re c - im a * im c + (re b * re c - im b * im c) = re a * re c - im a * im c + re b * re c - im b * im c</code>, which is `immediate' from the fact that \bbR is a commutative ring, but fiddly to prove step by step... Thanks! On the other hand, if this is part of the exercise I'm pretty sure I can do it, but I don't want to :-).</p>

#### [ Mario Carneiro (Jan 10 2019 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154877565):
<p><code>by ring</code></p>

#### [ Kevin Buzzard (Jan 11 2019 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154899369):
<p>When I do this exercise now David, I write a tactic to do all the work for me :-)</p>

#### [ Kevin Buzzard (Jan 11 2019 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154899374):
<p>Ie a tactic which just applies other tactics :-)</p>

#### [ David Holmes (Jan 11 2019 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154900247):
<p>Thanks very much, but I'm still doing something wrong. A minimal non-working example with the same error is </p>
<div class="codehilite"><pre><span></span>import data.real.basic
example : (1 : ℝ) + 2 = 3 :=
begin
by ring,
end

example (a b c: ℝ) :
(a + b) * c = a * c + b * c :=
begin
by ring,
end
</pre></div>


<p>giving the error </p>
<p>type mismatch at application<br>
  tactic.istep 5 3 5 3 ring<br>
term<br>
  ring<br>
has type<br>
  Type ? → Type ? : Type (?+1)<br>
but is expected to have type<br>
  tactic ?m_1 : Type ?</p>
<p>Kevin's suggestion of writing a tactic sounds sensible, but I think I'm not at that point yet...</p>

#### [ Johan Commelin (Jan 11 2019 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154900257):
<p><code>import tactic.ring</code>?</p>

#### [ Johan Commelin (Jan 11 2019 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154900261):
<p>Or whatever auto-completion makes of that.</p>

#### [ Johan Commelin (Jan 11 2019 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154900306):
<p>I agree that the error message is cryptic. It would be nicer if it said "tactic ring not found" or something like that.</p>

#### [ Kevin Buzzard (Jan 11 2019 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154900327):
<p>I'm not at a pc right now (indeed I'm waiting for a 51 and am going to be a few minutes late) but I just mean defining a new tactic which strings together other tactics, it's trivial</p>

#### [ Johan Commelin (Jan 11 2019 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154900331):
<p><span class="user-mention" data-user-id="198366">@David Holmes</span>  The problem is: tactics are just a certain kind of types. And now we have two versions of <code>ring</code>, living in different namespaces. One is a tactic, and the other is the typeclass that gives ring structure to a <code>R : Type</code>. (E.g. the ring structure on the reals). Without importing the tactic, it finds the other one, which confuses Lean, and gives you a cryptic error message.</p>

#### [ David Holmes (Jan 11 2019 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154900643):
<p>It works, thanks Johan! Kevin, writing tactics to string together others sounds really neat, especially if its trivial :-).</p>

#### [ Johan Commelin (Jan 11 2019 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154900739):
<p>If you want to know what <code>ring</code> does (up to "isomorphism of algorithms" <span class="emoji emoji-1f606" title="lol">:lol:</span>), you should read Kevin's blogpost about it.</p>

#### [ Rob Lewis (Jan 11 2019 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154901337):
<p>A small additional note: <code>by _</code> is equivalent to <code>begin _ end</code>, where <code>_</code> is a single tactic. So you can just write <code>by ring</code>, or <code>begin ring end</code>.</p>

#### [ David Holmes (Jan 11 2019 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154928489):
<p>Hi Kevin, <br>
In the `complex' exercises, I made it up to and including </p>
<div class="codehilite"><pre><span></span>theorem add_mul (a b c : ℂ) :
(a + b) * c = a * c + b * c := sorry
</pre></div>


<p>Will try the next ones later. The only thing I needed (other than what you provided) was the line </p>
<div class="codehilite"><pre><span></span>import tactic.ring
</pre></div>


<p>and the tactic <code>by ring</code>. </p>
<p>I wonder about more efficient ways to do some of this. I defined addition by </p>
<div class="codehilite"><pre><span></span>definition add : ℂ → ℂ → ℂ
| ⟨x1,y1⟩ ⟨x2,y2⟩ := ⟨x1 + x2, y1 + y2⟩
</pre></div>


<p>then needed things like </p>
<div class="codehilite"><pre><span></span>lemma re_add (a b : ℂ) :
re (a + b) = re a + re b:=
begin
have h : a + b = ⟨re(a+b), im(a+b) ⟩, rw eta,
have ha : a = ⟨ re a, im a ⟩,rw eta,
have hb : b = ⟨ re b, im b ⟩,rw eta,
have H : a + b = ⟨re(a) + re(b), im(a+b) ⟩, rw ha, rw hb,
unfold re, refl, rw H, refl,
end
</pre></div>


<p>whose proof was harder than I expected. Then my proof of distributivity was </p>
<div class="codehilite"><pre><span></span>theorem add_mul (a b c : ℂ) :
(a + b) * c = a * c + b * c :=
begin
apply ext,
have Hrleft: re ((a+b) * c) = re(a + b)* re(c) - im(a + b) * im(c),
apply re_mult,
have Hrright : re(a * c + b * c) = re a * re c - im a * im c + re b * re c - im b * im c,
have h1 : re(a*c) = re a * re c - im a * im c, apply re_mult,
have h2 : re(b*c) = re b * re c - im b * im c, apply re_mult,
rw [re_add], rw[h1], rw [h2], by ring, rw [Hrright],
have H : re(a + b)* re(c) - im(a + b) * im(c) = re a * re c - im a * im c + re b * re c - im b * im c,
rw [re_add], rw im_add, by ring, rw [Hrleft], rw H, -- now done with the real component
-- onto the imaginary part
have Hileft : im((a + b) * c) = re (a + b) * im c + re c * im (a + b),
apply im_mult,
have Hiright : im(a * c + b * c) = re a * im c + re c * im a + re b * im c + re c * im b,
have h1 : im(a*c) = re a * im c + re c * im a, apply im_mult,
have h2 : im(b*c) = re b * im c + re c * im b, apply im_mult,
rw [im_add], rw[h1], rw [h2], by ring, rw [Hiright],
have H : re(a + b)* im(c) + re(c) * im(a + b) = re a * im c + re b * im c + re c * im a + re c * im b,
rw [re_add], rw im_add, by ring, rw [Hileft], rw H, by ring,
end
</pre></div>


<p>(attached my code <a href="/user_uploads/3121/W5bzU97AUkl2kyShuTAzZRbM/complex.lean" target="_blank" title="complex.lean">complex.lean</a> in case interesting/easier to read). Which was not really so bad, but doing this for every axiom would hurt a bit. </p>
<p>These proof were all basically computations, so maybe tactic mode was not the best choice? But I am starting to like tactic mode quite a bit. </p>
<p>I often felt I wanted to start a proof about a complex number <code>a</code> by saying 'write <code>a = x + iy</code>', but not sure if there is an analogue of that in Lean that functions as I would hope. Working around it got kind of messy, but perhaps that's life. </p>
<p>[I'm putting this here (and not as a pm to Kevin) in case it is useful to other people, but I don't really know how the forum works so please let me know if I'm spamming!]</p>

#### [ Kevin Buzzard (Jan 11 2019 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154930105):
<p>Posts like this are fine. Yes, there are better ways, but in my mind these struggles are interesting to go through once, just to make sure you understand what's going on.</p>
<p><a href="https://github.com/leanprover/mathlib/blob/774e7fa39a8513c5c06e27c3e8bf4c124efd9db7/analysis/complex.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/774e7fa39a8513c5c06e27c3e8bf4c124efd9db7/analysis/complex.lean">https://github.com/leanprover/mathlib/blob/774e7fa39a8513c5c06e27c3e8bf4c124efd9db7/analysis/complex.lean</a></p>
<p>That was my effort at the time. I wrote a tactic called <code>crunch</code> which just did the ring theory I needed.</p>
<p>Defining structures and making them work properly is hard for mathematicians, because mathematicians don't instinctively think to define things like eta and ext.</p>

#### [ Kevin Buzzard (Jan 12 2019 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154987156):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">add_mul</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">)</span> <span class="o">:</span>
<span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">)</span> <span class="bp">*</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">c</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">*</span> <span class="n">c</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">ext</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">rw</span> <span class="o">[</span><span class="n">re_add</span><span class="o">,</span><span class="n">re_mul</span><span class="o">,</span><span class="n">re_add</span><span class="o">,</span><span class="n">im_add</span><span class="o">,</span><span class="n">re_mul</span><span class="o">,</span><span class="n">re_mul</span><span class="o">],</span>
    <span class="n">ring</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">rw</span> <span class="o">[</span><span class="n">im_add</span><span class="o">,</span><span class="n">im_mul</span><span class="o">,</span><span class="n">re_add</span><span class="o">,</span><span class="n">im_add</span><span class="o">,</span><span class="n">im_mul</span><span class="o">,</span><span class="n">im_mul</span><span class="o">],</span>
    <span class="n">ring</span> <span class="o">},</span>
<span class="kn">end</span>
</pre></div>


<p>The <code>ring</code> tactic can solve a goal of the form <code>(re a + re b) * re c - (im a + im b) * im c = re a * re c - im a * im c + (re b * re c - im b * im c)</code> so we just apply the lemmas we know to turn it into a goal of this form. If the lemmas <code>re_add</code> etc are all tagged with the <code>simp</code> attribute then perhaps instead of the rewrite one could write <code>suffices : (re a + re b) * re c - blah blah blah, by simp</code>.</p>

#### [ Kenny Lau (Jan 12 2019 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/154987800):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">add_mul</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">)</span> <span class="bp">*</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">c</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">*</span> <span class="n">c</span> <span class="o">:=</span>
<span class="n">ext</span>
  <span class="o">(</span><span class="k">show</span> <span class="o">(</span><span class="bp">_+_</span><span class="o">)</span><span class="bp">*_-</span><span class="o">(</span><span class="bp">_+_</span><span class="o">)</span><span class="bp">*_=</span><span class="o">(</span><span class="bp">_-_</span><span class="o">)</span><span class="bp">+</span><span class="o">(</span><span class="bp">_-_</span><span class="o">),</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">add_mul</span><span class="o">,</span> <span class="n">add_mul</span><span class="o">,</span> <span class="n">add_sub_comm</span><span class="o">])</span>
  <span class="o">(</span><span class="k">show</span> <span class="o">(</span><span class="bp">_+_</span><span class="o">)</span><span class="bp">*_+</span><span class="o">(</span><span class="bp">_+_</span><span class="o">)</span><span class="bp">*_=</span><span class="o">(</span><span class="bp">_+_</span><span class="o">)</span><span class="bp">+</span><span class="o">(</span><span class="bp">_+_</span><span class="o">),</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">add_mul</span><span class="o">,</span> <span class="n">add_mul</span><span class="o">,</span> <span class="n">add_assoc</span><span class="o">,</span> <span class="n">add_left_comm</span> <span class="o">(</span><span class="n">b</span><span class="bp">.</span><span class="mi">1</span><span class="bp">*_</span><span class="o">),</span> <span class="err">←</span> <span class="n">add_assoc</span><span class="o">])</span>
</pre></div>

#### [ Bryan Gin-ge Chen (Jan 15 2019 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/155132580):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> What's the new link for whatever was at <a href="http://wwwf.imperial.ac.uk/~buzzard/lean_together/source/leantogether.html" target="_blank" title="http://wwwf.imperial.ac.uk/~buzzard/lean_together/source/leantogether.html">http://wwwf.imperial.ac.uk/~buzzard/lean_together/source/leantogether.html</a> ?</p>

#### [ Kevin Buzzard (Jan 15 2019 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/155152962):
<p>Sorry -- link fixed. I added some more (very sketchy) exercises and broke everything in the process.</p>

#### [ David Holmes (Jan 18 2019 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/156402310):
<p>Thanks Kevin, your proof is very nice - doing in 2 lines what took me 7. Also much easier to read! Moving on to the other cases seems more reasonable now.</p>

#### [ David Holmes (Jan 18 2019 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/156402395):
<p>Kenny, what you wrote looks very neat, but I can't get it to work. I guess i need to add <code>begin</code> and <code>end</code>, but then I get an error on the first <code>show</code>, saying <code>function expected at
  (λ (this : (?m_5 + ?m_6) * ?m_7 - (?m_10 + ?m_11) * ?m_12 = ?m_15 - ?m_16 + (?m_18 - ?m_19)), this) ?m_20
term has type
  (?m_5 + ?m_6) * ?m_7 - (?m_10 + ?m_11) * ?m_12 = ?m_15 - ?m_16 + (?m_18 - ?m_19)
</code>.<br>
Any suggestions on what I'm doing wrong?</p>

#### [ Kenny Lau (Jan 18 2019 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/156402574):
<p>I think at that time I couldn't import mathlib so I made up my own complex numbers; the definition of multiplication may have been different (my proof relies heavily on definitional equalities)</p>

#### [ Mario Carneiro (Jan 18 2019 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/156403084):
<p>doesn't something like <code>by ext; ring</code> work?</p>

#### [ Mario Carneiro (Jan 18 2019 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/156403365):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">complex</span><span class="bp">.</span><span class="n">basic</span>

<span class="n">attribute</span> <span class="o">[</span><span class="n">extensionality</span><span class="o">]</span> <span class="n">complex</span><span class="bp">.</span><span class="n">ext</span>

<span class="kn">theorem</span> <span class="n">add_mul&#39;</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">)</span> <span class="bp">*</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">c</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">*</span> <span class="n">c</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">ext</span><span class="bp">;</span> <span class="n">simp</span><span class="bp">;</span> <span class="n">ring</span>
</pre></div>

#### [ David Holmes (Jan 18 2019 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/156405084):
<p>Hi Mario, <br>
Thanks for the suggestion. I'm sure that works with the complex numbers in Lean, but this was part of an exercise to construct the complex numbers from the real numbers (so never used <code>import data.complex.basic</code>). I just get the usual <code>simplify tactic failed to simplify</code>. I think if some of my earlier lemmas had the simp attribute it might also work, but not yet sure how to go about that (and maybe it is not the goal of the exercise).</p>

#### [ Mario Carneiro (Jan 19 2019 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/156408900):
<p>You need simp lemmas for addition and multiplication</p>

#### [ Mario Carneiro (Jan 19 2019 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/156408917):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">add_re</span> <span class="o">(</span><span class="n">z</span> <span class="n">w</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">z</span> <span class="bp">+</span> <span class="n">w</span><span class="o">)</span><span class="bp">.</span><span class="n">re</span> <span class="bp">=</span> <span class="n">z</span><span class="bp">.</span><span class="n">re</span> <span class="bp">+</span> <span class="n">w</span><span class="bp">.</span><span class="n">re</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">add_im</span> <span class="o">(</span><span class="n">z</span> <span class="n">w</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">z</span> <span class="bp">+</span> <span class="n">w</span><span class="o">)</span><span class="bp">.</span><span class="n">im</span> <span class="bp">=</span> <span class="n">z</span><span class="bp">.</span><span class="n">im</span> <span class="bp">+</span> <span class="n">w</span><span class="bp">.</span><span class="n">im</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">mul_re</span> <span class="o">(</span><span class="n">z</span> <span class="n">w</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">z</span> <span class="bp">*</span> <span class="n">w</span><span class="o">)</span><span class="bp">.</span><span class="n">re</span> <span class="bp">=</span> <span class="n">z</span><span class="bp">.</span><span class="n">re</span> <span class="bp">*</span> <span class="n">w</span><span class="bp">.</span><span class="n">re</span> <span class="bp">-</span> <span class="n">z</span><span class="bp">.</span><span class="n">im</span> <span class="bp">*</span> <span class="n">w</span><span class="bp">.</span><span class="n">im</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">mul_im</span> <span class="o">(</span><span class="n">z</span> <span class="n">w</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">z</span> <span class="bp">*</span> <span class="n">w</span><span class="o">)</span><span class="bp">.</span><span class="n">im</span> <span class="bp">=</span> <span class="n">z</span><span class="bp">.</span><span class="n">re</span> <span class="bp">*</span> <span class="n">w</span><span class="bp">.</span><span class="n">im</span> <span class="bp">+</span> <span class="n">z</span><span class="bp">.</span><span class="n">im</span> <span class="bp">*</span> <span class="n">w</span><span class="bp">.</span><span class="n">re</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>

#### [ Mario Carneiro (Jan 19 2019 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Teaching%20Lean%20to%20mathematicians/near/156408984):
<p>of course you can prove the theorem by <code>add_mul</code> since this is already proven in <code>data.complex.basic</code>, but if you are rewriting it on your own you want <code>complex.ext</code> and these re/im lemmas and then everything should follow by <code>ring</code> like I said</p>


{% endraw %}
