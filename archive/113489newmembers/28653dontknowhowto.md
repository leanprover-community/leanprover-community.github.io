---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/28653dontknowhowto.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [don't know how to](https://leanprover-community.github.io/archive/113489newmembers/28653dontknowhowto.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Etienne Laurin (Aug 04 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/130864937):
<p>Hi! I'm a C++ developer in Dublin. I'm trying to learn Lean by doing some exercises.</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">T</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">A</span> <span class="n">B</span> <span class="o">:</span> <span class="n">T</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span>
<span class="kn">lemma</span> <span class="n">t₁</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="n">A</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="o">(</span><span class="n">A</span> <span class="n">x</span> <span class="bp">∨</span> <span class="n">B</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">p</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">p</span><span class="bp">⟩</span>
<span class="kn">lemma</span> <span class="n">t₂</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="n">A</span> <span class="n">x</span><span class="o">)</span> <span class="bp">∨</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="n">B</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="o">(</span><span class="n">A</span> <span class="n">x</span> <span class="bp">∨</span> <span class="n">B</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span>
    <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">h</span><span class="bp">.</span><span class="n">cases_on</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">p</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">p</span><span class="bp">⟩</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">p</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="n">p</span><span class="bp">⟩</span><span class="o">)</span>
</pre></div>


<p>t₁ works but t₂ fails with "don't know how to synthesize placeholder". How can I get Lean to tell me what/where this placeholder is? Is there something better than or.cases_on that I could be using?</p>

#### [ Mario Carneiro (Aug 04 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/130865206):
<p>There is a known issue with using projection notation in conjunction with <code>@[elab_as_eliminator]</code> definitions like <code>or.cases_on</code>. You can fix the proof by either not using projection notation, i.e. <code>or.cases_on h</code> instead of <code>h.cases_on</code>, or by using <code>h.elim</code> instead (which is basically the same as <code>or.cases_on</code> without the weird elaborator marking)</p>

#### [ Etienne Laurin (Aug 04 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/130865584):
<p>Thanks!</p>

#### [ Kevin Buzzard (Aug 04 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/130865651):
<p>How can you tell <code>or.cases_on</code> is tagged <code>@[elab_as_eliminator]</code>? <code>#print or.cases_on</code> only tells me it's <code>@[reducible]</code></p>

#### [ Mario Carneiro (Aug 04 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/130865788):
<p>Hm, that's interesting. <code>T.rec</code>, <code>T.rec_on</code>, and <code>T.cases_on</code> are automatically generated for every inductive type and are always treated as if they have <code>elab_as_eliminator</code> enabled, although you are right that there is no explicit indication of such. You can test it by making a copy of <code>or.cases_on</code> with exactly the definition <code>#print</code> says, and the lemma will typecheck; then if you add <code>elab_as_eliminator</code> you get exactly the same errors</p>

#### [ Kevin Buzzard (Aug 04 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/130865850):
<p><code>example : @or.cases_on = @or.elim := rfl</code>, and they're both there, so they must be different somehow ;-) It's how the elaborator elaborates them.</p>

#### [ Mario Carneiro (Aug 04 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/130865947):
<p>you should be aware that that's not the best way to check that two definitions are the same according to lean, that is only up to defeq which ignores annotations and bindings, as well as unifying universes</p>

#### [ Mario Carneiro (Aug 04 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/130866021):
<p>Also, strange as it may sound I'm pretty sure there are duplicate definitions (completely identical) in lean. Often this has to do with renaming</p>

#### [ Edward Ayers (Aug 08 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131118119):
<p>I got this to work with <br>
<code>λ h, or.cases_on h (λ ⟨x, p⟩, ⟨x, or.inl p⟩) (λ ⟨x, p⟩, ⟨x, or.inr p⟩)</code></p>

#### [ Edward Ayers (Aug 08 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131118228):
<p>Can someone explain what the "synthesize placeholder" error actually means? It is by far the most common error I get and I currently get rid of it by making random transformations to the source until it goes away</p>

#### [ Mario Carneiro (Aug 08 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131118304):
<p>it means the proof is unfinished</p>

#### [ Edward Ayers (Aug 08 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131118316):
<p>proof that the term typechecks?</p>

#### [ Mario Carneiro (Aug 08 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131118320):
<p>lean is saying "there is a missing part of the proof and I don't know how to fill it in"</p>

#### [ Mario Carneiro (Aug 08 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131118344):
<p>No, the term itself is the proof</p>

#### [ Edward Ayers (Aug 08 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131118347):
<p>I often get it where the goal that it is trying to prove is <code>Type ?</code>. What should I do then?</p>

#### [ Mario Carneiro (Aug 08 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131118365):
<p>That means there is a missing type somewhere</p>

#### [ Mario Carneiro (Aug 08 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131118414):
<p>for example, looking at the term you just gave without any other context, I can't figure out the type of <code>h</code></p>

#### [ Mario Carneiro (Aug 08 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131118422):
<p>I know it is an <code>or</code> of something but I don't know what</p>

#### [ Mario Carneiro (Aug 08 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131118427):
<p>so if I were lean I would say "couldn't synth placeholder <code>|- Type ?</code>"</p>

#### [ Edward Ayers (Aug 08 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131119049):
<p>Ok let me paste some code where I can't figure out what it wants<br>
I put this file in <code>mathlib/category_theory/scratch.lean</code></p>
<div class="codehilite"><pre><span></span>import .category
import .functor
universes u1 u2 v1 v2

namespace category_theory
    section
        variables
            {C : Type u1} [𝒞 : category.{u1 v1} C]
            {D : Type u2} [𝒟 : category.{u2 v2} D]
        include 𝒞 𝒟
        def t : Π (a b c : D) (p : a = b) (x : a ⟶ c), b ⟶ c := λ a b c p x, eq.rec x p
        def t2 (F G : C ↝ D) (ob_eq : ∀ (Z : C), F Z = G Z)  (X Y : C) (f : X ⟶ Y) : (G X ⟶ F Y)
            := t (F X) (G X) (F Y) (ob_eq X) (F.map f)
    end
end category_theory
</pre></div>


<p>And I get a synth <code>Type ?</code> error for <code>t</code> in <code>t2</code> but I can't figure out which type I am missing</p>

#### [ Reid Barton (Aug 08 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131119269):
<p>Just looking at this (haven't built recent mathlib yet), I think the problem is that <code>t</code> "depends on" <code>C</code>, because of <code>include 𝒞</code>, but there's nothing in the type of <code>t</code> which can ever determine what <code>C</code> has to be.</p>

#### [ Edward Ayers (Aug 08 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131119333):
<p>Ah, so if you are in a section and write <code>variables</code>, then all definitions in that section implicitly depend on these variables, even if they are not used in the definition?</p>

#### [ Reid Barton (Aug 08 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131119335):
<p>And so there's no reason that <code>t</code>'s <code>C</code> in the use of <code>t</code> in <code>t2</code>needs to be the same as the <code>C</code> in <code>t2</code>, so Lean can't figure out how to assign it.</p>

#### [ Reid Barton (Aug 08 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131119347):
<p>Not in general, but using <code>include</code> forces the <code>variable</code> to be included as a parameter to every subsequent definition.</p>

#### [ Edward Ayers (Aug 08 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131119364):
<p>Where can I find some docs on <code>include</code>? I find it cryptic</p>

#### [ Reid Barton (Aug 08 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131119365):
<p>So if you show the full inferred type of <code>t</code>, it should begin <code>t : \Pi {C : Type u1} [𝒞 : category.{u1 v1} C] ...</code></p>

#### [ Reid Barton (Aug 08 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131119421):
<p><code>𝒞</code>was included because of the <code>include</code>, and <code>C</code> was included because <code>𝒞</code> depends on it</p>

#### [ Edward Ayers (Aug 08 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131119458):
<p>If I comment out <code>include</code>, then the <code>\hom</code> arrows become errors. How would I get rid of those errors without using <code>include</code>?</p>

#### [ Edward Ayers (Aug 08 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131119525):
<p>It can't find evidence for <code>category D</code>.</p>

#### [ Reid Barton (Aug 08 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131119547):
<p><a href="https://leanprover.github.io/theorem_proving_in_lean/tactics.html" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/tactics.html">https://leanprover.github.io/theorem_proving_in_lean/tactics.html</a> mentions <code>include</code>/<code>omit</code> in the first section. I don't remember whether it is also explained elsewhere in TPIL</p>

#### [ Reid Barton (Aug 08 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131119558):
<p>In this case, you could put <code>include 𝒟</code> between the definitions of <code>t</code> and <code>t2</code></p>

#### [ Edward Ayers (Aug 08 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131119625):
<p>Fixed code:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="bp">.</span><span class="n">category</span>
<span class="kn">import</span> <span class="bp">.</span><span class="n">functor</span>
<span class="n">universes</span> <span class="n">u1</span> <span class="n">u2</span> <span class="n">v1</span> <span class="n">v2</span>

<span class="kn">namespace</span> <span class="n">category_theory</span>
    <span class="kn">section</span>
        <span class="kn">variables</span>
            <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u1</span><span class="o">}</span> <span class="o">[</span><span class="err">𝒞</span> <span class="o">:</span> <span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u1</span> <span class="n">v1</span><span class="o">}</span> <span class="n">C</span><span class="o">]</span>
            <span class="o">{</span><span class="n">D</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u2</span><span class="o">}</span> <span class="o">[</span><span class="err">𝒟</span> <span class="o">:</span> <span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u2</span> <span class="n">v2</span><span class="o">}</span> <span class="n">D</span><span class="o">]</span>
        <span class="n">include</span> <span class="err">𝒟</span>
        <span class="n">def</span> <span class="n">t</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">D</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">a</span> <span class="err">⟶</span> <span class="n">c</span><span class="o">),</span> <span class="n">b</span> <span class="err">⟶</span> <span class="n">c</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">p</span> <span class="n">x</span><span class="o">,</span> <span class="n">eq</span><span class="bp">.</span><span class="n">rec</span> <span class="n">x</span> <span class="n">p</span>
        <span class="n">include</span> <span class="err">𝒞</span>
        <span class="n">def</span> <span class="n">t2</span> <span class="o">(</span><span class="n">F</span> <span class="n">G</span> <span class="o">:</span> <span class="n">C</span> <span class="err">↝</span> <span class="n">D</span><span class="o">)</span> <span class="o">(</span><span class="n">ob_eq</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">Z</span> <span class="o">:</span> <span class="n">C</span><span class="o">),</span> <span class="n">F</span> <span class="n">Z</span> <span class="bp">=</span> <span class="n">G</span> <span class="n">Z</span><span class="o">)</span>  <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="n">C</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="err">⟶</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">G</span> <span class="n">X</span> <span class="err">⟶</span> <span class="n">F</span> <span class="n">Y</span><span class="o">)</span>
            <span class="o">:=</span> <span class="n">t</span> <span class="o">(</span><span class="n">F</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">G</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">ob_eq</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span><span class="bp">.</span><span class="n">map</span> <span class="n">f</span><span class="o">)</span>
    <span class="kn">end</span>
<span class="kn">end</span> <span class="n">category_theory</span>
</pre></div>

#### [ Reid Barton (Aug 08 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131119700):
<p>Normally you could just omit the names <code>𝒞 : </code> and <code>𝒟 : </code> and the include statements and Lean would figure out where it needs the instance variables. The fact that that doesn't work here is some combination of there being extra universe parameters involved and a bug in Lean, I think.</p>

#### [ Edward Ayers (Aug 08 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131119729):
<p>Ok but this then errors for me:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="bp">.</span><span class="n">category</span>
<span class="kn">import</span> <span class="bp">.</span><span class="n">functor</span>
<span class="n">universes</span> <span class="n">u1</span> <span class="n">u2</span> <span class="n">v1</span> <span class="n">v2</span>

<span class="kn">namespace</span> <span class="n">category_theory</span>
    <span class="kn">section</span>
        <span class="kn">variables</span>
            <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u1</span><span class="o">}</span> <span class="o">[</span><span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u1</span> <span class="n">v1</span><span class="o">}</span> <span class="n">C</span><span class="o">]</span>
            <span class="o">{</span><span class="n">D</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u2</span><span class="o">}</span> <span class="o">[</span><span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u2</span> <span class="n">v2</span><span class="o">}</span> <span class="n">D</span><span class="o">]</span>
        <span class="c1">--include 𝒟</span>
        <span class="n">def</span> <span class="n">t</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">D</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">a</span> <span class="err">⟶</span> <span class="n">c</span><span class="o">),</span> <span class="n">b</span> <span class="err">⟶</span> <span class="n">c</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">p</span> <span class="n">x</span><span class="o">,</span> <span class="n">eq</span><span class="bp">.</span><span class="n">rec</span> <span class="n">x</span> <span class="n">p</span>
        <span class="c1">--include 𝒞</span>
        <span class="n">def</span> <span class="n">t2</span> <span class="o">(</span><span class="n">F</span> <span class="n">G</span> <span class="o">:</span> <span class="n">C</span> <span class="err">↝</span> <span class="n">D</span><span class="o">)</span> <span class="o">(</span><span class="n">ob_eq</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">Z</span> <span class="o">:</span> <span class="n">C</span><span class="o">),</span> <span class="n">F</span> <span class="n">Z</span> <span class="bp">=</span> <span class="n">G</span> <span class="n">Z</span><span class="o">)</span>  <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="n">C</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="err">⟶</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">G</span> <span class="n">X</span> <span class="err">⟶</span> <span class="n">F</span> <span class="n">Y</span><span class="o">)</span>
            <span class="o">:=</span> <span class="n">t</span> <span class="o">(</span><span class="n">F</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">G</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">ob_eq</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span><span class="bp">.</span><span class="n">map</span> <span class="n">f</span><span class="o">)</span>
    <span class="kn">end</span>
<span class="kn">end</span> <span class="n">category_theory</span>
</pre></div>

#### [ Edward Ayers (Aug 08 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131119748):
<p><code>kernel failed to type check declaration 't' this is usually due to a buggy tactic or a bug in the builtin elaborator</code></p>

#### [ Edward Ayers (Aug 08 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131119757):
<p>cool</p>

#### [ Edward Ayers (Aug 08 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131119821):
<p>which must be why it had <code>𝒞 : </code> in to start with, to avoid the lean bug</p>

#### [ Reid Barton (Aug 08 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131119827):
<p>Yes. The reason is either that Lean doesn't know what universe parameters to specialize <code>⟶</code> to, or that there's a bug where including the instance variable doesn't cause <code>C</code> to also get included.  I don't remember the exact details any more.<br>
When you get that "kernel failed to type check declaration" error, it means it failed to include <code>C</code>, I think.</p>

#### [ Reid Barton (Aug 08 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131119926):
<p>Right, the workaround is that when you manually tell it to include the <code>category</code> instance, then it can correctly infer that it needs <code>C</code> too. The downside is that now you are responsible for making sure the right variables are <code>include</code>d--if you have too many then you end up with your original issue.</p>

#### [ Edward Ayers (Aug 08 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131119929):
<p>thanks so much for your help</p>

#### [ Reid Barton (Aug 08 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131119952):
<p>In general, this class of error can be tough to figure out. I don't know of a better way than thinking really hard about what Lean is trying to do and figuring out where it might be getting stuck.</p>

#### [ Reid Barton (Aug 08 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131119954):
<p>No problem</p>

#### [ Edward Ayers (Aug 08 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131120046):
<p>It seems like solving these errors requires intimately knowing what the elaborator is doing.  And from what I know, the elaborator is very elaborate</p>

#### [ Patrick Massot (Aug 08 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131120215):
<blockquote>
<p>Normally you could just omit the names <code>𝒞 : </code> and <code>𝒟 : </code> and the include statements and Lean would figure out where it needs the instance variables.</p>
</blockquote>
<p>I think this is not true. To me it seems Lean will always include these statements. That explains why we sometimes see unneeded or duplicate instance arguments, even in mathlib</p>

#### [ Patrick Massot (Aug 08 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131120241):
<blockquote>
<p>It seems like solving these errors requires intimately knowing what the elaborator is doing.  And from what I know, the elaborator is very elaborate</p>
</blockquote>
<p>Unfortunately and fortunately, this is all very true.</p>

#### [ Edward Ayers (Aug 08 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131120395):
<p>It would be great if when there was an elaborator error, a textbox appeared that you could enter the missing type or proof into.</p>

#### [ Mario Carneiro (Aug 08 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131120407):
<p>Lean will include an unnamed typeclass variable when all of its dependencies are included (usually because they are mentioned directly in the statement or are dependencies of something mentioned). Like so:</p>
<div class="codehilite"><pre><span></span>variables (A : Type) [group A]
example (x : A) : true := ... -- group A is included
example : true := ... -- group A is not included
</pre></div>

#### [ Patrick Massot (Aug 08 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131120439):
<p>yes, this matches what I saw</p>

#### [ Reid Barton (Aug 08 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131120443):
<p>Yes, good point <span class="user-mention" data-user-id="110031">@Patrick Massot</span>.</p>

#### [ Mario Carneiro (Aug 08 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131120505):
<p>Lean will never include a named typeclass variable unless it is mentioned:</p>
<div class="codehilite"><pre><span></span>variables (A : Type) [G : group A]
example (x : A) : true := ... -- group A is not included
example : x + x = x := ... -- group A is included
</pre></div>


<p>And an included typeclass variable is always included:</p>
<div class="codehilite"><pre><span></span>variables (A : Type) [G : group A]
include G
example (x : A) : true := ... -- group A is included
example : true := ... -- group A is included
</pre></div>

#### [ Scott Morrison (Aug 09 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/don%27t%20know%20how%20to/near/131137096):
<p>I will add some documentation about <code>include</code> right in the <code>category_theory</code> files, specialised to the use case there.</p>
<p>Unfortunately <code>category C</code> has an unbound universe level, because we need to know the universe level of the morphisms, and this is not determined by the universe level of <code>C</code> itself. (This design decision is constrained by the desire to be able to write uniform code for small categories and large categories.)</p>
<p>When we write <code>variable [category.{u v} C]</code>, Lean is reasonably rather hesistant to use this variable, unless it is sure that <code>v</code> is the actually intended universe level. To avoid having to explicitly write this universe variable in every definition that you're hoping will make use of this <code>[category C]</code> variable, we give it a name as in <code>[𝒞 :  category.{u v} C]</code> and explicitly include it in every following declaration, via <code>include 𝒞</code>.</p>
<p>This then adds a danger: if you write another declaration that doesn't actually care about this category (e.g. one declaration refers to four different categories, but a subsequent one only mentions two), this typeclass variable will still be included as an argument, mucking everything up. Hence <code>include 𝒞</code> statements need to be carefully scoped with <code>section .... end</code> commands.</p>


{% endraw %}
