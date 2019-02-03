---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/74562sigmapsigma.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [sigma/psigma](https://leanprover-community.github.io/archive/113489newmembers/74562sigmapsigma.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ petercommand (Nov 03 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116492):
<p>What's the reason for having types like sigma/psigma, sum/psum at the same time?</p>

#### [ Kevin Buzzard (Nov 03 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116506):
<p>Is it to do with universes?</p>

#### [ petercommand (Nov 03 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116556):
<p>Like, when would I want to use psigma instead of sigma/Exists?</p>

#### [ Reid Barton (Nov 03 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116602):
<p>psigma instead of Exists: because you want to keep the information of what the things are whose existence you claim</p>

#### [ Reid Barton (Nov 03 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116613):
<p>psigma with a Prop is basically the same as subtype, whereas Exists is like nonempty</p>

#### [ Reid Barton (Nov 03 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116617):
<p>psigma instead of sigma: if you want to use a Prop instead of a Type, or you might want either a Prop or a Type</p>

#### [ Chris Hughes (Nov 03 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116664):
<p>The equation compiler uses <code>psigma</code> a lot. <code>| (a : nat) (b : nat) (h : 0 &lt; b)</code> is essentially matching on <code>Σ' a b : ℕ, 0 &lt; b</code> underneath.</p>

#### [ Reid Barton (Nov 03 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116741):
<p>I've found psigma most useful in conjunction with the <code>Σ'</code> binder notation with multiple variables where the eventual "body" is a Prop</p>

#### [ Mario Carneiro (Nov 03 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116857):
<p>isn't that exists?</p>

#### [ Reid Barton (Nov 03 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116861):
<p>like "a pair consisting of an open set U and a function f : U -&gt; R which sends x to 0" = <code>Σ' (u : set α) (hu : is_open u) (f : u → ℝ), f x = 0</code></p>

#### [ Chris Hughes (Nov 03 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116878):
<p>What's the point of using <code>sigma</code> instead of <code>psigma</code>?</p>

#### [ Mario Carneiro (Nov 03 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116924):
<p><code>psigma</code> has a difficult target universe</p>

#### [ Mario Carneiro (Nov 03 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116939):
<p><code>Sort (max u 1)</code> is hard to work with</p>

#### [ Mario Carneiro (Nov 03 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116949):
<p>because it's not algebraic: <code>max u 1 = 1</code> does not have a unique solution</p>

#### [ Mario Carneiro (Nov 03 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116960):
<p>so lean will often give up on otherwise solvable universe unification problems</p>

#### [ Mario Carneiro (Nov 03 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137116964):
<p>where <code>Type u = Sort u+1</code> has the much easier solution <code>u+1 = 1 -&gt;  u = 0</code></p>

#### [ Mario Carneiro (Nov 03 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117028):
<p>In fact, there are some expressions which do not have any solution, although you might think it does: <code>max u 1 = v+1</code> has no solution for u</p>

#### [ Reid Barton (Nov 03 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117277):
<p>hmm, that <code>max 1</code> is coming from Lean bumping up the level of a structure I guess? Is it actually wanted? Why should <code>psigma.{0 0}</code> not be a Prop?</p>

#### [ Mario Carneiro (Nov 03 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117417):
<p>That was deliberate. You can define your own <code>psigma'</code> that lives in <code>Sort (max u v)</code></p>

#### [ Mario Carneiro (Nov 03 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117429):
<p>but you will find it's not all it's cracked up to be</p>

#### [ Mario Carneiro (Nov 03 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117444):
<p>in particular, it has a recursor like <code>exists</code></p>

#### [ Mario Carneiro (Nov 03 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117492):
<p>it's not "data"</p>

#### [ Mario Carneiro (Nov 03 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117639):
<p>and if you specialize to <code>u &gt; 0</code> you get the <a href="#narrow/stream/113488-general/subject/nearly.20no_confusion/near/124133073" title="#narrow/stream/113488-general/subject/nearly.20no_confusion/near/124133073"><code>mystery</code> type</a>, which is neither proof nor data</p>

#### [ petercommand (Nov 03 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117691):
<blockquote>
<p>In fact, there are some expressions which do not have any solution, although you might think it does: <code>max u 1 = v+1</code> has no solution for u</p>
</blockquote>
<p>why does <code>max u 1 = v+1</code> not have any solutions?</p>

#### [ Mario Carneiro (Nov 03 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117726):
<p>because there is no universe expression that gives the solution</p>

#### [ Reid Barton (Nov 03 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117727):
<p>Actually, I can't :)</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">ppsigma</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span> <span class="n">v</span><span class="o">)</span> <span class="o">:</span> <span class="n">Sort</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span> <span class="n">mk</span> <span class="bp">::</span> <span class="o">(</span><span class="n">fst</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">snd</span> <span class="o">:</span> <span class="n">β</span> <span class="n">fst</span><span class="o">)</span>
<span class="c1">-- invalid universe polymorphic structure declaration, the resultant universe is not Prop (i.e., 0), but it may be Prop for some parameter values (solution: use &#39;l+1&#39; or &#39;max 1 l&#39;)</span>
</pre></div>

#### [ Reid Barton (Nov 03 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117736):
<p>But I guess it's because otherwise I would be in the situation you describe.</p>

#### [ Mario Carneiro (Nov 03 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117799):
<p>That's because you used <code>structure</code>, it tried and failed to define the projections</p>

#### [ Reid Barton (Nov 03 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117845):
<p>Oh, I see</p>

#### [ Reid Barton (Nov 03 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117869):
<p>Why doesn't singleton elimination help here?<br>
If I manually replace <code>u = v = 0</code>, then I get an eliminator to any sort</p>

#### [ Mario Carneiro (Nov 03 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117873):
<p><span class="user-mention" data-user-id="127883">@petercommand</span> for each fixed <code>v</code> there is a solution for <code>u</code>, but there is no solution function <code>u(v)</code></p>

#### [ Reid Barton (Nov 03 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117929):
<p>Just a weird edge case that Lean doesn't support?</p>

#### [ Mario Carneiro (Nov 03 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117940):
<p>because you need one recursor that is polymorphic in u,v</p>

#### [ Mario Carneiro (Nov 03 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137117970):
<p>and that recursor will have one extra universe variable depending on whether <code>max u v = 0</code></p>

#### [ Mario Carneiro (Nov 03 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137118003):
<p>there is no way to do that with universe expressions</p>

#### [ Mario Carneiro (Nov 03 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137118073):
<p>you could have two recursors, but this breaks parametricity</p>

#### [ Reid Barton (Nov 03 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137118109):
<p>I'm trying out different <code>u</code> and <code>v</code> values and in every case I get an eliminator which goes to any sort.<br>
However there is a difference when <code>u = v = 0</code>, which is that the <code>C</code> doesn't take the <code>ppsigma</code> value as an argument then</p>

#### [ Mario Carneiro (Nov 03 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137118122):
<p>singleton elimination doesn't help because <code>A</code> and <code>B</code> aren't subsingletons</p>

#### [ Mario Carneiro (Nov 03 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137118185):
<p>That's just a convenience thing, the usual recursor is at <code>drec_on</code></p>

#### [ Mario Carneiro (Nov 03 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137118220):
<p>for small eliminating props the dependent and nondependent recursors are interdefinable</p>

#### [ Reid Barton (Nov 03 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137118506):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">ppsigma00</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span> <span class="mi">0</span><span class="o">}</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="n">Sort</span> <span class="o">(</span><span class="n">max</span> <span class="mi">0</span> <span class="mi">0</span><span class="o">)</span> <span class="bp">|</span> <span class="n">m</span> <span class="o">(</span><span class="n">fst</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">snd</span> <span class="o">:</span> <span class="n">β</span> <span class="n">fst</span><span class="o">)</span> <span class="o">:</span> <span class="n">ppsigma00</span>
<span class="bp">#</span><span class="kn">check</span> <span class="bp">@</span><span class="n">ppsigma00</span><span class="bp">.</span><span class="n">drec_on</span>
<span class="err">│</span> <span class="n">ppsigma00</span><span class="bp">.</span><span class="n">drec_on</span> <span class="o">:</span>
<span class="err">│</span>   <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="n">ppsigma00</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">Sort</span> <span class="n">u_1</span><span class="o">}</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">ppsigma00</span> <span class="n">β</span><span class="o">),</span>
<span class="err">│</span>     <span class="o">(</span><span class="bp">Π</span> <span class="o">(</span><span class="n">fst</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">snd</span> <span class="o">:</span> <span class="n">β</span> <span class="n">fst</span><span class="o">),</span> <span class="n">C</span> <span class="bp">_</span><span class="o">)</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">n</span>

<span class="kn">inductive</span> <span class="n">ppsigma11</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span> <span class="mi">1</span><span class="o">}</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="n">Sort</span> <span class="o">(</span><span class="n">max</span> <span class="mi">1</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">|</span> <span class="n">m</span> <span class="o">(</span><span class="n">fst</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">snd</span> <span class="o">:</span> <span class="n">β</span> <span class="n">fst</span><span class="o">)</span> <span class="o">:</span> <span class="n">ppsigma11</span>
<span class="bp">#</span><span class="kn">check</span> <span class="bp">@</span><span class="n">ppsigma11</span><span class="bp">.</span><span class="n">rec_on</span>
<span class="err">│</span> <span class="n">ppsigma11</span><span class="bp">.</span><span class="n">rec_on</span> <span class="o">:</span>
<span class="err">│</span>   <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="n">ppsigma11</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">Sort</span> <span class="n">u_1</span><span class="o">}</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">ppsigma11</span> <span class="n">β</span><span class="o">),</span>
<span class="err">│</span>     <span class="o">(</span><span class="bp">Π</span> <span class="o">(</span><span class="n">fst</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">snd</span> <span class="o">:</span> <span class="n">β</span> <span class="n">fst</span><span class="o">),</span> <span class="n">C</span> <span class="o">(</span><span class="n">ppsigma11</span><span class="bp">.</span><span class="n">m</span> <span class="n">fst</span> <span class="n">snd</span><span class="o">))</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">n</span>
</pre></div>

#### [ Reid Barton (Nov 03 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137118544):
<p>They look the same to me (especially with <code>set_option pp.proofs true</code>)</p>

#### [ Reid Barton (Nov 03 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137118748):
<p>I would maybe believe that the VM can't (easily) implement such a thing, though</p>

#### [ Reid Barton (Nov 03 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137118764):
<p><code>rec_on</code> is an axiom, right? Or one of the related things is?</p>

#### [ Chris Hughes (Nov 03 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137120246):
<p><code>rec_on</code> is <code>rec</code> with the arguments in a different order. <code>rec</code> is an axiom.</p>

#### [ Kenny Lau (Nov 03 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137120259):
<p>to be pedantic, it's an axiom schema</p>

#### [ Chris Hughes (Nov 03 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137120303):
<p>What's an axiom schema?</p>

#### [ Kenny Lau (Nov 03 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137120315):
<p>it isn't one single axiom</p>

#### [ Kenny Lau (Nov 03 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137120317):
<p>it's one axiom per inductive type</p>

#### [ Reid Barton (Nov 03 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/137120323):
<p>Right, I meant <code>[whatever].rec</code></p>

#### [ Floris van Doorn (Nov 05 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/146795757):
<blockquote>
<p>In fact, there are some expressions which do not have any solution, although you might think it does: <code>max u 1 = v+1</code> has no solution for u</p>
</blockquote>
<p>I'm confused. Lean doesn't know that <code>max (v+1) 1 = v+1</code>?</p>

#### [ Floris van Doorn (Nov 05 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/146795876):
<p>I presume you misspoke, and meant that there is no solution for <code>v</code>? (I agree with that.)</p>

#### [ Mario Carneiro (Nov 05 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/sigma/psigma/near/146796140):
<p>oh, yes you are right</p>


{% endraw %}
