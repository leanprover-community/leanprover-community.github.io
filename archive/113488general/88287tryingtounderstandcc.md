---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88287tryingtounderstandcc.html
---

## Stream: [general](index.html)
### Topic: [trying to understand cc](88287tryingtounderstandcc.html)

---


{% raw %}
#### [ Johan Commelin (Apr 24 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125602905):
<p>I had hoped this would work:</p>
<div class="codehilite"><pre><span></span><span class="n">universes</span> <span class="n">u</span>

<span class="kn">variables</span>
<span class="o">{</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">group</span> <span class="n">A</span><span class="o">]</span>
<span class="o">{</span><span class="n">B</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">group</span> <span class="n">B</span><span class="o">]</span>
<span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">B</span><span class="o">}</span> <span class="o">[</span><span class="n">is_group_hom</span> <span class="n">f</span><span class="o">]</span>

<span class="kn">lemma</span> <span class="n">test</span> <span class="o">(</span><span class="n">hf</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">→</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">))</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">A</span><span class="o">)</span> <span class="o">(</span><span class="n">hfx</span> <span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">cc</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Apr 24 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125602950):
<p>So which tactic do I need here?</p>

#### [ Simon Hudon (Apr 24 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125602958):
<p>That's not the kind of stuff it does. Try:</p>
<div class="codehilite"><pre><span></span>import tactic -- from mathlib

lemma ... := by solve_by_elim
</pre></div>

#### [ Johan Commelin (Apr 24 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603006):
<p>Next goal: just have <code>hf : function.injective f</code> as hypothesis</p>

#### [ Johan Commelin (Apr 24 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603018):
<p>Instead of unpacking that definition myself...</p>

#### [ Simon Hudon (Apr 24 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603023):
<p>Have you tried it?</p>

#### [ Johan Commelin (Apr 24 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603067):
<p>Yes. Then it fails:</p>
<div class="codehilite"><pre><span></span><span class="n">universes</span> <span class="n">u</span>

<span class="kn">variables</span>
<span class="o">{</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">group</span> <span class="n">A</span><span class="o">]</span>
<span class="o">{</span><span class="n">B</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">group</span> <span class="n">B</span><span class="o">]</span>
<span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">B</span><span class="o">}</span> <span class="o">[</span><span class="n">is_group_hom</span> <span class="n">f</span><span class="o">]</span>

<span class="kn">lemma</span> <span class="n">test</span> <span class="o">(</span><span class="n">hf</span> <span class="o">:</span> <span class="n">function</span><span class="bp">.</span><span class="n">injective</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">A</span><span class="o">)</span> <span class="o">(</span><span class="n">hfx</span> <span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">solve_by_elim</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Apr 24 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603074):
<p>squiggles under <code>solve_by_elim</code></p>

#### [ Simon Hudon (Apr 24 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603076):
<p>What error message does it give you?</p>

#### [ Johan Commelin (Apr 24 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603130):
<div class="codehilite"><pre><span></span>assumption tactic failed
state:
A : Type u,
_inst_1 : group A,
B : Type u,
_inst_2 : group B,
f : A → B,
_inst_3 : is_group_hom f,
hf : function.injective f,
x : A,
hfx : f x = 1
⊢ x = 1
</pre></div>

#### [ Kenny Lau (Apr 24 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603131):
<p>to be fair the proof needs to go like f x = f 1 and then x = 1</p>

#### [ Kenny Lau (Apr 24 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603133):
<p>and it needs is_group_hom.one</p>

#### [ Johan Commelin (Apr 24 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603138):
<p>Yeah, there is a bit more to be done... but I think there should be a tactic that can do that for me</p>

#### [ Johan Commelin (Apr 24 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603146):
<p>Ideally there is a <code>diagram_chase</code> tactic</p>

#### [ Johan Commelin (Apr 24 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603147):
<p>And I think <code>cc</code> is very close to that</p>

#### [ Johan Commelin (Apr 24 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603149):
<p>It only needs to know little facts like this lemma and some similar stuff.</p>

#### [ Kenny Lau (Apr 24 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603150):
<p>try mixing is_group_hom.one into the ingredient</p>

#### [ Johan Commelin (Apr 24 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603152):
<p>And then it would be able to prove the five lemma on its own</p>

#### [ Kenny Lau (Apr 24 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603198):
<p>have := is_group_hom.one f; solve_by_elim</p>

#### [ Johan Commelin (Apr 24 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603210):
<p>That's not enough</p>

#### [ Johan Commelin (Apr 24 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603215):
<p>Alas</p>

#### [ Simon Hudon (Apr 24 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603273):
<p>This one should work:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">test</span> <span class="o">(</span><span class="n">hf</span> <span class="o">:</span> <span class="n">function</span><span class="bp">.</span><span class="n">injective</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">A</span><span class="o">)</span> <span class="o">(</span><span class="n">hfx</span> <span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="o">:=</span> <span class="n">is_group_hom</span><span class="bp">.</span><span class="n">one</span> <span class="n">f</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">hf</span><span class="o">,</span> <span class="n">cc</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Apr 24 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603276):
<p>Ok, so <code>have := \fo x, (fx = 1 \to x = 1)</code>. How should I prove that? Is it a one-liner?</p>

#### [ Johan Commelin (Apr 24 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603286):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Nice!</p>

#### [ Kenny Lau (Apr 24 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603335):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> I don’t get it at all</p>

#### [ Simon Hudon (Apr 24 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603337):
<p>If you want to go fully anonymous (not name your assumptions like <code>this</code> and <code>hf</code>) you can do:</p>
<div class="codehilite"><pre><span></span>begin
  have := is_group_hom.one f,
  apply_assumption, cc
end
</pre></div>

#### [ Kenny Lau (Apr 24 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603339):
<p>how does apply hf even succeed</p>

#### [ Kenny Lau (Apr 24 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603349):
<p>oh nvm I thought wrongly</p>

#### [ Simon Hudon (Apr 24 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603401):
<p>You apply it to <code>x = 1</code> and <code>hf </code> is <code>hf : ∀ x y, f x = f y → x = y</code>. When you apply it, you instantiate it with <code>x := x, y := 1</code> so the antecedent becomes <code>f x = f 1</code>. Your idea with <code>have</code> gets us <code>this : f 1 = 1</code></p>

#### [ Kenny Lau (Apr 24 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603402):
<p>I mean, I would just write the proof in term mode</p>

#### [ Simon Hudon (Apr 24 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603410):
<p>I think I would keep <code>cc</code> at the very least.</p>

#### [ Simon Hudon (Apr 24 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603418):
<blockquote>
<p>Ok, so <code>have := \fo x, (fx = 1 \to x = 1)</code>. How should I prove that? Is it a one-liner?</p>
</blockquote>
<p>Did you find an answer for this?</p>

#### [ Johan Commelin (Apr 24 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603474):
<p>Not yet, Lean doesn't like that expression</p>

#### [ Simon Hudon (Apr 24 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603523):
<p>Error message?</p>
<p>I would expect it to work but I don't think that's what you're looking for</p>

#### [ Johan Commelin (Apr 24 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603526):
<p>And the problem is not <code>fx</code>, I changed that to <code>f x</code></p>

#### [ Johan Commelin (Apr 24 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603532):
<p><code>invalid expression starting at xx:y</code></p>

#### [ Simon Hudon (Apr 24 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603536):
<p><code>have := expr</code> uses <code>expr</code> as a proof of an unnamed proposition. That proposition is just the type of the expression. If <code>expr</code> is the proposition you want to prove, you write <code>have : expr</code></p>

#### [ Simon Hudon (Apr 24 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603582):
<p>Can you show me the whole proof? Maybe you missed a comma</p>

#### [ Johan Commelin (Apr 24 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603594):
<div class="codehilite"><pre><span></span><span class="n">universes</span> <span class="n">u</span>

<span class="kn">variables</span>
<span class="o">{</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">group</span> <span class="n">A</span><span class="o">]</span>
<span class="o">{</span><span class="n">B</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">group</span> <span class="n">B</span><span class="o">]</span>
<span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">B</span><span class="o">}</span> <span class="o">[</span><span class="n">is_group_hom</span> <span class="n">f</span><span class="o">]</span>

<span class="kn">lemma</span> <span class="n">test</span> <span class="o">(</span><span class="n">hf</span> <span class="o">:</span> <span class="n">function</span><span class="bp">.</span><span class="n">injective</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">A</span><span class="o">)</span> <span class="o">(</span><span class="n">hx</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">ker</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="k">have</span> <span class="o">:=</span> <span class="n">is_group_hom</span><span class="bp">.</span><span class="n">one</span> <span class="n">f</span><span class="o">,</span>
<span class="k">have</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">→</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)),</span>
</pre></div>

#### [ Simon Hudon (Apr 24 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603643):
<p>Do you have an <code>end</code> keyword after that?</p>

#### [ Johan Commelin (Apr 24 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603648):
<p>yes</p>

#### [ Johan Commelin (Apr 24 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603653):
<p>several lines lower</p>

#### [ Simon Hudon (Apr 24 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603719):
<p>Can you show me what the rest of the proof is?</p>

#### [ Simon Hudon (Apr 24 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603720):
<p>Also, do you have imports?</p>

#### [ Johan Commelin (Apr 24 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125603992):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span>
<span class="kn">import</span> <span class="n">init</span><span class="bp">.</span><span class="n">function</span>
<span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">group</span>
<span class="kn">import</span> <span class="n">group_theory</span><span class="bp">.</span><span class="n">subgroup</span>

<span class="n">universes</span> <span class="n">u</span>

<span class="kn">variables</span>
<span class="o">{</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">group</span> <span class="n">A</span><span class="o">]</span>
<span class="o">{</span><span class="n">B</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">group</span> <span class="n">B</span><span class="o">]</span>
<span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">B</span><span class="o">}</span> <span class="o">[</span><span class="n">is_group_hom</span> <span class="n">f</span><span class="o">]</span>

<span class="kn">lemma</span> <span class="n">test</span> <span class="o">(</span><span class="n">hf</span> <span class="o">:</span> <span class="n">function</span><span class="bp">.</span><span class="n">injective</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">A</span><span class="o">)</span> <span class="o">(</span><span class="n">hx</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">ker</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="k">have</span> <span class="o">:=</span> <span class="n">is_group_hom</span><span class="bp">.</span><span class="n">one</span> <span class="n">f</span><span class="o">,</span>
<span class="k">have</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">→</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">))</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Apr 24 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125604019):
<p>All the other stuff in that file is wrapped withing a section</p>

#### [ Kenny Lau (Apr 24 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125604129):
<p>hf $ hx.trans $ eq.symm $ is_group_hom.one f</p>

#### [ Johan Commelin (Apr 24 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125604198):
<p>I first need to get rid of an error message: <code>invalid expression starting at &lt;coords&gt;</code></p>

#### [ Johan Commelin (Apr 24 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125604201):
<p>the <code>&lt;coords&gt;</code> are of the <code>\fo</code></p>

#### [ Simon Hudon (Apr 24 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125604257):
<p>I don't see a problem there. Try restarting your Lean server</p>

#### [ Johan Commelin (Apr 24 2018 at 07:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125604365):
<p>Yay, that did it (-;</p>

#### [ Simon Hudon (Apr 24 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125604377):
<p>Unfortunately, that's a common solution to problems <span class="emoji emoji-1f61c" title="stuck out tongue winking eye">:stuck_out_tongue_winking_eye:</span></p>

#### [ Johan Commelin (Apr 24 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125604527):
<p>Ok, need to go now</p>

#### [ Johan Commelin (Apr 24 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125604528):
<p>Thanks!</p>

#### [ Patrick Massot (Apr 24 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125609972):
<p>I think this happens more frequently since <span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> enabled the new "region of interest" thing</p>

#### [ Patrick Massot (Apr 24 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125610009):
<p>It's nice to have Lean reacting quicker but I did get quite a lot of those random <code>invalid expression starting at &lt;coords&gt;</code> yesterday</p>

#### [ Gabriel Ebner (Apr 24 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125610074):
<p>Do you have a reproducible test case?</p>

#### [ Kenny Lau (Apr 25 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125672053):
<p>Oh so <code>cc</code> deals with commutativity and associativity also?</p>

#### [ Simon Hudon (Apr 25 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125672100):
<p>No. Why do you say that?</p>

#### [ Kenny Lau (Apr 25 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125672103):
<p>apparently it did</p>

#### [ Kenny Lau (Apr 25 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125672486):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">+</span> <span class="n">m</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">cc</span>
<span class="bp">#</span><span class="kn">print</span> <span class="n">test</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">theorem test : ∀ (m n : ℕ), m + n = n + m :=</span>
<span class="cm">λ (m n : ℕ),</span>
<span class="cm">  of_eq_true (eq_true_intro (eq.symm (eq.trans (eq.refl (n + m)) (eq.symm (is_commutative.comm has_add.add m n)))))</span>
<span class="cm">-/</span>
</pre></div>

#### [ Simon Hudon (Apr 25 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trying%20to%20understand%20cc/near/125672553):
<p>Oh interesting! I didn't think it would</p>


{% endraw %}
