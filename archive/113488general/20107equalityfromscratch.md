---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20107equalityfromscratch.html
---

## Stream: [general](index.html)
### Topic: [equality from scratch](20107equalityfromscratch.html)

---


{% raw %}
#### [ Adam Kurkiewicz (Aug 07 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131035424):
<p>While looking at Kevin's <a href="https://xenaproject.wordpress.com/2017/10/31/building-the-non-negative-integers-from-scratch/" target="_blank" title="https://xenaproject.wordpress.com/2017/10/31/building-the-non-negative-integers-from-scratch/">great blog post</a> about unsigned integers from scratch I thought to push myself a little bit and I've tried to do them <em>even more</em> from scratch, by giving up the existing <code>eq</code> or <code>=</code>.</p>
<p>So let's say we have an inductive <code>xnat</code> and an inductive xnat <code>equality</code> like this:</p>
<div class="codehilite"><pre><span></span>inductive xnat : Type
| zero : xnat
| succ : xnat → xnat

inductive equality (a : xnat): xnat → Prop
    | refl : equality a
</pre></div>


<p>We're getting reflexivity for free from the type system, but we want to prove transitivity and symmetry. Let's assume we don't know anything about default parameters, universes, etc, but we know about recursors. We might write something like this:</p>
<div class="codehilite"><pre><span></span>definition equality.symm: Π (a b : xnat), Π eq1 : (equality a b), equality b a :=
    λ a b : xnat,
    λ eq1 : (equality a b),
    equality.rec_on eq1 _
</pre></div>


<p>And now, the strangest thing happens, the placeholder no longer expects a proof of <code>equality b a</code>, suddenly <code>equality a a</code> suffices. This relieves us, and we proceed, almost automatically, to write <code>(equality.refl a)</code> instead of the placeholder, and this typechecks. Phew.</p>
<p>But why does it typecheck? Why suddently a proof of <code>equality a a</code> is good enough as a proof of <code>equality b a</code>. Is there something special in the type-system that makes it work?</p>

#### [ Mario Carneiro (Aug 07 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131035618):
<p>Look at the type of <code>equality.rec_on</code>.</p>
<div class="codehilite"><pre><span></span><span class="kn">protected</span> <span class="n">def</span> <span class="n">equality</span><span class="bp">.</span><span class="n">rec_on</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">xnat</span><span class="o">}</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="n">xnat</span> <span class="bp">→</span> <span class="n">Sort</span> <span class="n">l</span><span class="o">}</span> <span class="o">{</span><span class="n">a_1</span> <span class="o">:</span> <span class="n">xnat</span><span class="o">},</span> <span class="n">equality</span> <span class="n">a</span> <span class="n">a_1</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">a_1</span>
</pre></div>


<p>It says that if you want to prove a property <code>C</code> of <code>a_1 : xnat</code> given <code>equality a a_1</code>, it suffices to prove <code>C a</code>. In this case we know <code>equality a b</code>, so we need a property <code>C</code> depending on <code>b</code> such that <code>C a</code> is easy. In this case we take <code>\lam b, equality b a</code> as our <code>C</code>, so <code>C a</code> is <code>equality a a</code> which we prove by <code>refl</code>, and <code>C b</code> is <code>equality b a</code> which is what we wanted to show.</p>

#### [ Mario Carneiro (Aug 07 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131035869):
<p>You should be sure to look at the definition of <code>equality.symm</code> with <code>pp.all true</code>, so you can see how lean filled in the "motive" <code>C</code> in that rec_on application</p>

#### [ Mario Carneiro (Aug 07 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131035878):
<p>or use <code>@equality.rec_on</code> and fill in all the fields yourself</p>

#### [ Adam Kurkiewicz (Aug 07 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131036133):
<p>Thanks Mario, this is making it less magical. I'm on your most recent suggestion.</p>

#### [ Kevin Buzzard (Aug 07 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131036339):
<p>Kenny Lau once said to me "Lean does not do magic", and at that time I thought that lots of things Lean did (simp, type class inference) were magic. Kenny's comment spurred me on to trying to figure out how everything was working; the point is that Lean <em>never</em> does magic, and in any given case you can simply look at what it did and how it did it. Figuring out how to do that really helped me to learn Lean better.</p>

#### [ Adam Kurkiewicz (Aug 07 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131036344):
<p>Ah, of course, it makes sense. <code>equality a b</code> is the same as <code>(equality a) b</code>. So our <code>C</code> becomes <code>equality a</code>. Thanks Mario!</p>

#### [ Mario Carneiro (Aug 07 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131036376):
<p>ah, be careful: <code>equality a</code> would be a perfect motive to prove <code>equality a b -&gt; equality a b</code>, but this is symmetry, so there is a twist</p>

#### [ Adam Kurkiewicz (Aug 07 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131036388):
<p>So the solution is simply <code>@equality.rec_on a (equality a) b eq1 (equality.refl a)</code>, and that makes sense.</p>

#### [ Adam Kurkiewicz (Aug 07 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131036435):
<p>Is <code>C</code> the motif?</p>

#### [ Mario Carneiro (Aug 07 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131036451):
<p>yes, that's the usual terminology</p>

#### [ Mario Carneiro (Aug 07 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131036476):
<p>sometimes you get an error message talking about a motive, that's what it is referring to</p>

#### [ Mario Carneiro (Aug 07 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131036675):
<p>If you use the "flipped" motive <code>λ b, equality b a</code>, you have:</p>
<div class="codehilite"><pre><span></span>#check λ a b eq1, @equality.rec_on a (λ b, equality b a) b eq1 (equality.refl a)
-- : ∀ (a b : xnat), equality a b → (λ (b : xnat), equality b a) b
</pre></div>


<p>and notice that the conclusion there, <code>(λ (b : xnat), equality b a) b</code>, beta reduces to <code>equality b a</code> which is the desired symmetrized equality</p>

#### [ Adam Kurkiewicz (Aug 07 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131037522):
<p>Yes you're right, I didn't notice this wasn't typechecking. This lambda abstraction is a really nice trick, I don't think I would have come up with this myself.</p>

#### [ Adam Kurkiewicz (Aug 07 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131037601):
<p>Anyway, thank you Mario, I think this is now really clear.</p>

#### [ Adam Kurkiewicz (Aug 07 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131037619):
<p>I'll try to work through transitivity in a similar manner</p>

#### [ Mario Carneiro (Aug 07 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131037620):
<p>the really interesting thing is that lean will automatically do that lambda abstraction trick</p>

#### [ Adam Kurkiewicz (Aug 07 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131037733):
<p>Now, <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>  if this is not magic I don't know what is.</p>

#### [ Kevin Buzzard (Aug 07 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131037744):
<p>I'm not sure it's magic</p>

#### [ Kevin Buzzard (Aug 07 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131037799):
<p>Is it just matching types up?</p>

#### [ Kevin Buzzard (Aug 07 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131037814):
<p>I'm not quite following, I'm trying to get on a bus in Majorca</p>

#### [ Mario Carneiro (Aug 07 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131037826):
<p>the algorithm is very simple: the goal says <code>equality b a</code>, and we just replace every <code>b</code> with <code>a</code>, then we look at what we changed and replace that with a variable, let's call it <code>x</code>. So the motive is <code>λ x, equality x a</code></p>

#### [ Mario Carneiro (Aug 07 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131037911):
<p>this produces a lambda term such that replacing <code>x</code> with <code>b</code> gives us our original goal, and replacing <code>x</code> with <code>a</code> gives us our new goal which should be easier, in this case <code>equality a a</code></p>

#### [ Mario Carneiro (Aug 07 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131037993):
<p>you should try using this algorithm in the proof of transitivity to work out the right motive, then see whether you got it right by letting lean do it for you</p>

#### [ Adam Kurkiewicz (Aug 07 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131038529):
<p>I've actually just done it in my head. It worked:</p>
<div class="codehilite"><pre><span></span>inductive xnat : Type
| zero : xnat
| succ : xnat → xnat

inductive equality (a : xnat): xnat → Prop
    | refl : equality a

definition equality.trans: Π (a b c : xnat), Π eq1: (equality a b), Π eq2 : (equality b c), equality a c :=
    λ a b c : xnat,
    λ eq1 : (equality a b),
    λ eq2 : (equality b c),
    @equality.rec_on b (λ x, equality a x) c eq2 eq1
</pre></div>


<p>I'm sure I'll learn the algorithm one day, but I think I'll go and buy some beef now. Cooking sous vide steaks for friends this evening.</p>

#### [ Adam Kurkiewicz (Aug 07 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131038727):
<p>Thank you Mario, this was really helpful!</p>

#### [ Kevin Buzzard (Aug 07 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131041113):
<p>Warning: sometimes Lean can't generate the right motive. CS people start going on about higher order unification being undecidable when this sort of thing comes up. The problem is that if Lean can figure out that <code>C b</code> is supposed to be <code>f a b c b = 0</code> then it can't work out if <code>C x</code> is supposed to be <code>f a x c x = 0</code> or <code>f a b c x = 0</code> or ... etc.  So don't expect Lean to do miracles. See <a href="https://leanprover.github.io/theorem_proving_in_lean/interacting_with_lean.html#elaboration-hints" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/interacting_with_lean.html#elaboration-hints">https://leanprover.github.io/theorem_proving_in_lean/interacting_with_lean.html#elaboration-hints</a></p>

#### [ Kevin Buzzard (Aug 07 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20from%20scratch/near/131041181):
<p>Remember -- Lean does not do magic. Part of the art is working out when you're asking Lean to do magic :-)</p>


{% endraw %}
