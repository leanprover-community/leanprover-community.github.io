---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/71163multifixbracketnotation.html
---

## Stream: [general](index.html)
### Topic: [multifix bracket notation](71163multifixbracketnotation.html)

---


{% raw %}
#### [ Johan Commelin (Jun 11 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127889037):
<p>Is this bound to become a massive headache, if possible at all?</p>
<div class="codehilite"><pre><span></span><span class="kn">universe</span> <span class="n">u</span>
<span class="n">class</span> <span class="n">has_bracket</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">bracket</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span>
<span class="n">local</span> <span class="kn">notation</span> <span class="bp">`</span><span class="o">[</span><span class="bp">`</span> <span class="n">a</span> <span class="bp">`</span><span class="o">,</span><span class="bp">`</span> <span class="n">b</span> <span class="bp">`</span><span class="o">]</span><span class="bp">`</span> <span class="o">:=</span> <span class="n">has_bracket</span><span class="bp">.</span><span class="n">bracket</span>
</pre></div>


<p>The notation <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>[</mo><mi>x</mi><mo separator="true">,</mo><mi>y</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">[x,y]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">[</span><span class="mord mathit">x</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mclose">]</span></span></span></span> is very common (I would say, <em>mandatory</em>) in the theory of Lie algebras.</p>

#### [ Kevin Buzzard (Jun 11 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127889262):
<p>it breaks list notation, so one question is: are you likely to be using list notation? Let's face it, list notation isn't that common in mathematics. Will you use it behind the scenes though? I am not sure I used a single list when doing schemes.</p>

#### [ Kevin Buzzard (Jun 11 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127889303):
<p>(at least, not explicitly)</p>

#### [ Johan Commelin (Jun 11 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127899035):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">module</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>

<span class="n">class</span> <span class="n">has_bracket</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">bracket</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span>

<span class="n">local</span> <span class="kn">notation</span> <span class="bp">`</span><span class="o">[</span><span class="bp">`</span> <span class="n">a</span> <span class="bp">`</span><span class="o">,</span><span class="bp">`</span> <span class="n">b</span> <span class="bp">`</span><span class="o">]</span><span class="bp">`</span> <span class="o">:=</span> <span class="n">has_bracket</span><span class="bp">.</span><span class="n">bracket</span> <span class="n">a</span> <span class="n">b</span>

<span class="n">class</span> <span class="n">lie_algebra</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="n">out_param</span> <span class="err">$</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="err">𝔤</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">[</span><span class="n">out_param</span> <span class="err">$</span> <span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span>
<span class="kn">extends</span> <span class="n">module</span> <span class="n">R</span> <span class="err">𝔤</span><span class="o">,</span> <span class="n">has_bracket</span> <span class="err">𝔤</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">left_linear</span>  <span class="o">:=</span> <span class="bp">∀</span> <span class="n">y</span> <span class="o">:</span> <span class="err">𝔤</span><span class="o">,</span> <span class="n">is_linear_map</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="o">:</span> <span class="err">𝔤</span><span class="o">,</span> <span class="o">[</span><span class="n">x</span><span class="o">,</span><span class="n">y</span><span class="o">]))</span>
<span class="o">(</span><span class="n">right_linear</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="err">𝔤</span><span class="o">,</span> <span class="n">is_linear_map</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">y</span> <span class="o">:</span> <span class="err">𝔤</span><span class="o">,</span> <span class="o">[</span><span class="n">x</span><span class="o">,</span><span class="n">y</span><span class="o">]))</span>
<span class="o">(</span><span class="n">alternating</span>  <span class="o">:=</span> <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="err">𝔤</span><span class="o">,</span> <span class="o">[</span><span class="n">x</span><span class="o">,</span><span class="n">x</span><span class="o">]</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span>
<span class="o">(</span><span class="n">Jacobi_identity</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="o">:</span> <span class="err">𝔤</span><span class="o">,</span> <span class="o">[</span><span class="n">x</span><span class="o">,[</span><span class="n">y</span><span class="o">,</span><span class="n">z</span><span class="o">]]</span> <span class="bp">+</span> <span class="o">[</span><span class="n">z</span><span class="o">,[</span><span class="n">x</span><span class="o">,</span><span class="n">y</span><span class="o">]]</span> <span class="bp">+</span> <span class="o">[</span><span class="n">y</span><span class="o">,[</span><span class="n">z</span><span class="o">,</span><span class="n">x</span><span class="o">]]</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span>
<span class="o">(</span><span class="n">anti_comm</span>    <span class="o">:=</span> <span class="bp">∀</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="err">𝔤</span><span class="o">,</span> <span class="o">[</span><span class="n">x</span><span class="o">,</span><span class="n">y</span><span class="o">]</span> <span class="bp">=</span> <span class="bp">-</span><span class="o">([</span><span class="n">y</span><span class="o">,</span><span class="n">x</span><span class="o">]))</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">{</span><span class="err">𝔤</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">lie_algebra</span> <span class="n">R</span> <span class="err">𝔤</span><span class="o">]</span>

<span class="c">/-</span><span class="cm">- `𝔥` is a Lie subalgebra: a set closed under the Lie bracket. -/</span>
<span class="n">class</span> <span class="n">is_lie_subalgebra</span> <span class="o">(</span><span class="err">𝔥</span> <span class="o">:</span> <span class="n">set</span> <span class="err">𝔤</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">closed</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span><span class="o">}</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="err">𝔥</span> <span class="bp">→</span> <span class="n">y</span> <span class="err">∈</span> <span class="err">𝔥</span> <span class="bp">→</span> <span class="o">[</span><span class="n">x</span><span class="o">,</span><span class="n">y</span><span class="o">]</span> <span class="err">∈</span> <span class="err">𝔥</span><span class="o">)</span>
</pre></div>


<p>I am bitten again by type class inference. Once again Lean can't infer the class of <code>has_bracket 𝔤</code> in the last line, even though it knows that <code>𝔤</code> is a Lie algebra. <br>
If I compare this with</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">is_add_subgroup</span> <span class="o">[</span><span class="n">add_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">is_add_submonoid</span> <span class="n">s</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">neg_mem</span> <span class="o">{</span><span class="n">a</span><span class="o">}</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">→</span> <span class="bp">-</span><span class="n">a</span> <span class="err">∈</span> <span class="n">s</span><span class="o">)</span>
</pre></div>


<p>How does Lean figure out <code>has_mem α</code> to make sense of the <code>-a</code>? The cargo-cult programmer in me is stumped.</p>

#### [ Reid Barton (Jun 11 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127899473):
<p>I don't know why, but changing the last line to</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="err">𝔤</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">la</span> <span class="o">:</span> <span class="n">lie_algebra</span> <span class="n">R</span> <span class="err">𝔤</span><span class="o">]</span>
<span class="n">include</span> <span class="n">la</span>
</pre></div>


<p>made it work for me.</p>

#### [ Reid Barton (Jun 11 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127899477):
<p>If I had to guess, it has something to do with the additional parameter <code>R</code></p>

#### [ Johan Commelin (Jun 11 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127899495):
<p>Thanks... that'll do for now <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Sebastian Ullrich (Jun 11 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127899771):
<p>Yes, section variables used as <code>out_param</code>s are a bit broken. Lean will auto-include section class variables only when all its parameters are (auto-)included, but it should ignore <code>out_param</code>s during that.</p>

#### [ Sebastian Ullrich (Jun 11 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127899782):
<p>So <code>include R</code> should work too</p>

#### [ Johan Commelin (Jun 11 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127899849):
<p>It doesn't...</p>

#### [ Sebastian Ullrich (Jun 11 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127899927):
<p>¯\_(ツ)_/¯</p>

#### [ Reid Barton (Jun 11 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127900028):
<p>Maybe need to include the <code>[comm_ring R]</code> variable also then</p>

#### [ Johan Commelin (Jun 11 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127900036):
<p>Then yours becomes more efficient (-;</p>

#### [ Johan Commelin (Jun 11 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127900184):
<p>After Reid's (hacky) fix, the next line gives problems. I would like to solve it myself, but I don't know why Lean is unhappy. Here is the line:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">subset</span><span class="bp">.</span><span class="n">lie_algebra</span> <span class="o">{</span><span class="err">𝔥</span> <span class="o">:</span> <span class="n">set</span> <span class="err">𝔤</span><span class="o">}</span> <span class="o">[</span><span class="n">is_lie_subalgebra</span> <span class="err">𝔥</span><span class="o">]</span> <span class="o">:</span> <span class="n">lie_algebra</span> <span class="n">R</span> <span class="err">𝔥</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>I get red squiggles before the <code>is_lie_subalgebra</code> instance. Lean thinks it needs to infer an extra Type. I have tried some <code>set_option</code>s to get more info, but I couldn't figure it out (e.g. <code>trace.class_instances</code> and <code>pp.all</code>). How should I attack this error?</p>

#### [ Johan Commelin (Jun 11 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127914479):
<p>Is there documentation for <code>out_param</code>? What is it's purpose? I think I heard somewhere that there have been long discussions about it. Has that been condensed into some docs? It feels to me like <code>out_param</code> is making it harder to work with modules, rather than easier.</p>

#### [ Patrick Massot (Jun 11 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127914499):
<p>I think all documentation is here on Zulip (or gitter) and source code</p>

#### [ Johan Commelin (Jun 11 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127914575):
<p>I tried implicitly turning an <code>R</code>-algebra into an <code>R</code>-module, by chaining together <code>ring.to_module</code> and restriction of scalars... guess what happened</p>

#### [ Johan Commelin (Jun 11 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127914657):
<p>(I wanted to put the commutator bracket on the algebra [to make the link with this thread])</p>

#### [ Johan Commelin (Jun 11 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127914674):
<p>Anyway, I ran head first into the type class loop again.</p>

#### [ Kevin Buzzard (Jun 12 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127924610):
<p>Mario explaining out_param to me on gitter:</p>

#### [ Kevin Buzzard (Jun 12 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127924612):
<div class="codehilite"><pre><span></span>elaborator deals with opt_param, type class deals with out_param

Normally a typeclass won&#39;t trigger until all its parameters are fixed

So for example [has_mem A B] won&#39;t be solved until A and B are known

i.e. if I have x \in y and the types of x y are unknown, it will fail

However, has_mem works a bit differently than this because A is marked as an out_param

@[class]
structure has_mem : out_param (Type u) → Type v → Type (max u v)
fields:
has_mem.mem : Π {α : out_param (Type u)} {γ : Type v} [c : has_mem α γ], α → γ → Prop

In fact, if you have x \in y and y : B, even if the type of x is unknown it will try to solve the typeclass problem has_mem ?M B

This is important because it often comes up in notations like \forall x \in y, ... where y : set A and x is unknown type, we want lean to figure out that x : A

This doesn&#39;t affect the meta theory in any way, of course, once the full term is given the elaborator and typeclass inference is done and it&#39;s basic DTT. In that situation it really is just an identity function


And opt_param?
Mario Carneiro
@digama0
20:39
That&#39;s just the way (x : A := y) is translated, to x : opt_param A y
it holds the optional value so it can be inferred by the usual rules for optional arguments


It is occasionally useful when you want to have an optional argument right of the colon (the := syntax only works on the parameters)
</pre></div>

#### [ Kevin Buzzard (Jun 12 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127924746):
<p>Mario and Sebastian talking about module and params:</p>

#### [ Kevin Buzzard (Jun 12 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127924752):
<div class="codehilite"><pre><span></span>To review, the problem is that the definition:

class module (α : out_param $ Type u) (β : Type v) [out_param $ ring α]
  extends has_scalar α β, add_comm_group β :=
...

leads to a search problem in which ring ?M1 is solved before module ?M1 β, which leads to a loop when there is an instance like [ring A] [ring B] : ring (A x B)
I would like to make lean search for module ?M1 β only, obtaining α and the ring instance by unification
Johannes suggested using {out_param $ ring α} instead of [out_param $ ring α], but then it doesn&#39;t work as a typeclass, and all the multiplications etc in the theorem statements break
A possible solution is to skip out_param typeclass search problems until after all the others are solved

***

So the real issue is: You want the elaborator to handle applying a function {A B} [ring A] [module A B] (x : B) : ..., yes...?
Mario Carneiro
@digama0
Jan 19 10:10
yes
Sebastian Ullrich
@Kha
Jan 19 10:10
Where you want it to solve the second instance first, which fixes A and the first instance
</pre></div>

#### [ Kevin Buzzard (Jun 12 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127924890):
<p><a href="https://gitter.im/leanprover_public/Lobby?at=5a61beb85ade18be399654c0" target="_blank" title="https://gitter.im/leanprover_public/Lobby?at=5a61beb85ade18be399654c0">https://gitter.im/leanprover_public/Lobby?at=5a61beb85ade18be399654c0</a></p>

#### [ Kevin Buzzard (Jun 12 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127924893):
<p>Johannes too</p>

#### [ Johan Commelin (Jun 12 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127939887):
<p>Ok, I think I half understand the issues involved. Does this mean that</p>
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">restriction_of_scalars</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">S</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">S</span><span class="o">}</span>  <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">}</span> <span class="o">[</span><span class="n">module</span> <span class="n">S</span> <span class="n">M</span><span class="o">]</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">module</span> <span class="n">R</span> <span class="n">M</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">smul</span>     <span class="o">:=</span> <span class="bp">λ</span> <span class="n">r</span> <span class="n">m</span><span class="o">,</span> <span class="n">f</span><span class="o">(</span><span class="n">r</span><span class="o">)</span> <span class="err">•</span> <span class="n">m</span><span class="o">,</span>
  <span class="n">smul_add</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">smul_add</span><span class="o">,</span>
  <span class="n">add_smul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">r</span> <span class="n">s</span> <span class="n">m</span><span class="o">,</span> <span class="k">begin</span>
    <span class="k">show</span> <span class="n">f</span> <span class="o">(</span><span class="n">r</span> <span class="bp">+</span> <span class="n">s</span><span class="o">)</span> <span class="err">•</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">f</span><span class="o">(</span><span class="n">r</span><span class="o">)</span> <span class="err">•</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">f</span><span class="o">(</span><span class="n">s</span><span class="o">)</span> <span class="err">•</span> <span class="n">m</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_add</span> <span class="n">f</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">add_smul</span><span class="o">,</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">mul_smul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">r</span> <span class="n">s</span> <span class="n">m</span><span class="o">,</span> <span class="k">begin</span>
    <span class="k">show</span> <span class="n">f</span> <span class="o">(</span><span class="n">r</span> <span class="bp">*</span> <span class="n">s</span><span class="o">)</span> <span class="err">•</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">f</span><span class="o">(</span><span class="n">r</span><span class="o">)</span> <span class="err">•</span> <span class="n">f</span><span class="o">(</span><span class="n">s</span><span class="o">)</span> <span class="err">•</span> <span class="n">m</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_mul</span> <span class="n">f</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">mul_smul</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">one_smul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">m</span><span class="o">,</span> <span class="k">begin</span>
    <span class="k">show</span> <span class="n">f</span> <span class="o">(</span><span class="mi">1</span><span class="o">)</span> <span class="err">•</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">m</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_one</span> <span class="n">f</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">one_smul</span><span class="o">,</span>
  <span class="kn">end</span><span class="o">,</span>
<span class="o">}</span>

<span class="kn">end</span> <span class="n">restriction_of_scalars</span>
</pre></div>


<p>implies self-destruction <span class="emoji emoji-1f4a5" title="boom">:boom:</span> ?</p>

#### [ Johan Commelin (Jun 12 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multifix%20bracket%20notation/near/127940673):
<p>Ok, maybe this is asking to much. But would it be ok if we restrict to the case where <code>R</code> is a subring, and <code>f = subtype.val</code>?</p>


{% endraw %}
