---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/06032conflictofInstances.html
---

## Stream: [general](index.html)
### Topic: [conflict of Instances](06032conflictofInstances.html)

---


{% raw %}
#### [ AHan (Dec 04 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150822083):
<p>I wanted to prove the following function, but I've run into problems at the commented line<br>
Seems like lean interprets <code>≤ </code> in <code>le_of_not_lt h₂</code> as the <code>le</code> defined in <code>linear_order</code> instead of <code>semilattice_sup_bot</code>, while <code>lattice.sup_of_le_left </code> requires <code>le</code> defined by <code>semilattice_sup_bot</code>...<br>
How can I fix this?</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finset</span>
<span class="kn">namespace</span> <span class="n">finest</span>

<span class="kn">section</span>
<span class="kn">parameters</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">lattice</span><span class="bp">.</span><span class="n">semilattice_sup_bot</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_linear_order</span> <span class="n">α</span><span class="o">]</span>

<span class="kn">lemma</span> <span class="n">mem_of_sup_id&#39;</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">},</span> <span class="n">a</span> <span class="bp">≠</span> <span class="err">∅</span> <span class="bp">→</span> <span class="n">a</span><span class="bp">.</span><span class="n">sup</span> <span class="n">id</span> <span class="err">∈</span> <span class="n">a</span>
<span class="bp">|</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">finset</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">a</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">false</span><span class="bp">.</span><span class="n">elim</span> <span class="o">(</span><span class="n">a</span> <span class="o">(</span><span class="n">refl</span> <span class="bp">_</span><span class="o">)))</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">notin</span> <span class="n">ih</span> <span class="n">notempty</span><span class="o">,</span> <span class="k">begin</span>
        <span class="n">rw</span> <span class="o">[</span><span class="n">insert_eq</span><span class="o">,</span> <span class="n">sup_union</span><span class="o">,</span> <span class="n">mem_union</span><span class="o">,</span> <span class="n">sup_singleton</span><span class="o">]</span> <span class="n">at</span> <span class="bp">*</span><span class="o">,</span>
        <span class="n">simp</span><span class="o">,</span>
        <span class="n">generalize</span> <span class="n">hy</span> <span class="o">:</span> <span class="n">sup</span> <span class="n">y</span> <span class="n">id</span> <span class="bp">=</span> <span class="n">y&#39;</span><span class="o">,</span>
        <span class="k">from</span> <span class="k">if</span> <span class="n">h₁</span> <span class="o">:</span> <span class="n">y</span> <span class="bp">=</span> <span class="err">∅</span>
        <span class="k">then</span> <span class="k">begin</span>
            <span class="n">left</span><span class="o">,</span>
            <span class="n">rw</span> <span class="o">[</span><span class="n">h₁</span><span class="o">,</span> <span class="n">sup_empty</span><span class="o">]</span> <span class="n">at</span> <span class="n">hy</span><span class="o">,</span>
            <span class="n">rw</span> <span class="o">[</span><span class="err">←</span><span class="n">hy</span><span class="o">,</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">sup_bot_eq</span><span class="o">],</span>
        <span class="kn">end</span>
        <span class="k">else</span> <span class="k">begin</span>
            <span class="k">from</span> <span class="k">if</span> <span class="n">h₂</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="n">y&#39;</span>
            <span class="k">then</span> <span class="k">begin</span>
                <span class="n">right</span><span class="o">,</span>
                <span class="n">rw</span> <span class="o">[</span><span class="n">lattice</span><span class="bp">.</span><span class="n">sup_of_le_right</span> <span class="o">(</span><span class="n">le_of_lt</span> <span class="n">h₂</span><span class="o">),</span> <span class="err">←</span><span class="n">hy</span><span class="o">],</span>
                <span class="n">apply</span> <span class="n">ih</span> <span class="n">h₁</span><span class="o">,</span>
            <span class="kn">end</span>
            <span class="k">else</span> <span class="k">begin</span>
                <span class="n">left</span><span class="o">,</span>
                <span class="c1">--rw [lattice.sup_of_le_left (le_of_not_lt h₂)],</span>
            <span class="kn">end</span>
        <span class="kn">end</span>
    <span class="kn">end</span>
<span class="kn">end</span>

<span class="kn">end</span> <span class="n">finset</span>
</pre></div>

#### [ Sebastien Gouezel (Dec 04 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150828636):
<p>You are introducing two orders which have nothing to do with each other, as both <code>semilattice_sup_bot</code> and <code>decidable_linear_order</code> contain an order. Instead, you need to start from one order only, and add some "mixin", i.e., some property of the order but not a new order. For instance, in <code>data/finset.lean</code>, you have</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">sup_lt</span> <span class="o">[</span><span class="n">is_total</span> <span class="n">α</span> <span class="o">(</span><span class="bp">≤</span><span class="o">)]</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="err">⊥</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span><span class="n">b</span> <span class="err">∈</span> <span class="n">s</span><span class="o">,</span> <span class="n">f</span> <span class="n">b</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="o">)</span> <span class="bp">→</span> <span class="n">s</span><span class="bp">.</span><span class="n">sup</span> <span class="n">f</span> <span class="bp">&lt;</span> <span class="n">a</span>
</pre></div>


<p>Your problem can be solved in the same way.</p>

#### [ AHan (Dec 04 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150829193):
<p>So I have to define another class which includes properties of <code>semilattice_sup_bot</code> and <code>decidable_linear_order</code>?</p>

#### [ Johan Commelin (Dec 04 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150829404):
<p>Yes, I think so. So you define a class that <code>extends (semilattice_sup_bot X) (decidable_linear_order X).</code> I think you can just put a <code>.</code> after that extends statement, and then it will merge those two classes. You don't need any extra conditions, so you don't need a <code>:= (foo : blah)</code> part.</p>

#### [ Johan Commelin (Dec 04 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150829408):
<p>But this is all from memory, so I might be wrong.</p>

#### [ AHan (Dec 04 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150829714):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span>  I've tried, but it outputs the error message :<br>
"invalid 'structure' header, field 'le' from 'decidable_linear_order' has already been declared"...</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">decidable_semilattice_sup_bot</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="kn">extends</span> <span class="o">(</span><span class="n">lattice</span><span class="bp">.</span><span class="n">semilattice_sup_bot</span> <span class="n">α</span><span class="o">),</span> <span class="o">(</span><span class="n">decidable_linear_order</span> <span class="n">α</span><span class="o">)</span> <span class="bp">.</span>
</pre></div>


<p><code>function expected at  lattice.semilattice_sup_bot α term has type  Type ?</code></p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">decidable_semilattice_sup_bot</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="kn">extends</span> <span class="o">(</span><span class="n">lattice</span><span class="bp">.</span><span class="n">semilattice_sup_bot</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">decidable_linear_order</span> <span class="n">α</span><span class="o">)</span> <span class="bp">.</span>
</pre></div>

#### [ Johan Commelin (Dec 04 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150829776):
<p>Hmm, then I don't know. Maybe others can help.</p>

#### [ AHan (Dec 04 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150829847):
<p>I checked <code>semilattice_sup_bot</code> which is extended from <code>order_bot</code> and <code>semilattice_sup</code>, and both of them are extended from <code>partial_order</code>, but it doesn't seems to conflict in this case...</p>

#### [ AHan (Dec 04 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150830288):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span>  Solved! Have to <code>set_option</code> lol</p>
<div class="codehilite"><pre><span></span><span class="kn">set_option</span> <span class="n">old_structure_cmd</span> <span class="n">true</span>
<span class="n">class</span> <span class="n">decidable_semilattice_sup_bot</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">semilattice_sup_bot</span> <span class="n">α</span><span class="o">,</span> <span class="n">decidable_linear_order</span> <span class="n">α</span>
</pre></div>

#### [ Kevin Buzzard (Dec 04 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150830341):
<p>This whole aspect of the type class inference system is very cumbersome. It would not surprise me if somewhere someone had made exactly the typeclass that you need to give you the structure you want, but finding it is another matter. The type class system is extremely fussy when it comes to this sort of thing. I am not sure how long the old structure command option will be around for...</p>

#### [ Kevin Buzzard (Dec 04 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150830498):
<p>Although someone will no doubt come along and suggest a fix for your use case that doesn't involve the old structure command, I don't know how to solve this sort of problem in general. I guess it would be nice to be able to define the structures you wanted and then precisely insert them into the type class system by hand.</p>

#### [ Johan Commelin (Dec 04 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150830584):
<p>I thought the entire type class system is going to be redone in <span class="emoji emoji-1f340" title="four leaf clover">:four_leaf_clover:</span>. So by then <code>old_structure_cmd</code> will be <code>ancient_structure_cmd</code> and our current structures will be <code>old_structure</code>...</p>

#### [ AHan (Dec 04 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150830640):
<p>Ancient ! LOL</p>

#### [ Sebastien Gouezel (Dec 04 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150830741):
<p>As I tried to say, you can prove your lemma without introducing a new class, with</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finset</span>
<span class="kn">namespace</span> <span class="n">finest</span>

<span class="kn">section</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">lattice</span><span class="bp">.</span><span class="n">semilattice_sup_bot</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">is_total</span> <span class="n">α</span> <span class="o">(</span><span class="bp">≤</span><span class="o">)]</span>

<span class="kn">lemma</span> <span class="n">mem_of_sup_id&#39;</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">},</span> <span class="n">a</span> <span class="bp">≠</span> <span class="err">∅</span> <span class="bp">→</span> <span class="n">a</span><span class="bp">.</span><span class="n">sup</span> <span class="n">id</span> <span class="err">∈</span> <span class="n">a</span>
<span class="bp">...</span>
</pre></div>

#### [ AHan (Dec 04 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150830975):
<p><span class="user-mention" data-user-id="110050">@Sebastien Gouezel</span>  That's nice! Thanks a lot!</p>

#### [ Sebastian Ullrich (Dec 04 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150831357):
<p>(the typeclass inference system and the structure command are really quite orthogonal topics)</p>

#### [ Sebastian Ullrich (Dec 04 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150831579):
<p>There are no semantic change planned so far for either of them. Though hopefully you'll be able to "just" copy and modify the structure command in Lean 4, after it's rewritten in Lean.</p>

#### [ Kevin Buzzard (Dec 04 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150831588):
<blockquote>
<p>orthogonal topics</p>
</blockquote>
<p>Well, probably they are to a dev. Maybe the dev's answer to this question is "go and define the right mixins". The problems with this approach are (1) it doesn't seem to scale and (2) it confuses newcomers. It also means that mathematicians constantly make fun of Lean having a theory of distribs :D</p>

#### [ Patrick Massot (Dec 04 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150831711):
<p>We have explicitl  promise that Johan will be able to define <code>ancient_structure</code> and <code>fancy_johan_structure</code> that will reuse parts of the grammar of the built-in command. <a href="http://leanprover.github.io/presentations/20181012_MSR/#/1" target="_blank" title="http://leanprover.github.io/presentations/20181012_MSR/#/1">http://leanprover.github.io/presentations/20181012_MSR/#/1</a></p>

#### [ Patrick Massot (Dec 04 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150831727):
<p>Oh, I was too slow finding back the slides, Sebastian already mentioned it</p>

#### [ Kevin Buzzard (Dec 04 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150831755):
<p>Ultimately mathematicians will want to define five new concepts A B C D E, and then 2^5 more concepts of the form "put together this subset of A B C D E" and will want all the obvious compatibiities to hold and will want them all to be typeclasses. Now the two concepts are kind of mixed together. I thought we had the explicit promise that nothing was going to change? In the back of my mind I always figured that if the type class system wasn't up to some complicated collection of maths structures then the answer is simple -- just don't use it.</p>

#### [ Kevin Buzzard (Dec 04 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150831836):
<p>Oh but maybe I am beginning to understand the future better. The devs will leave us the structure command and type class system as it is, but will give us the tools to tweak it so that perhaps I can still do these 2^5 things in my own way and add exactly the fields I want to the type class inference system or whatever.</p>

#### [ AHan (Dec 04 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832214):
<p><span class="user-mention" data-user-id="110050">@Sebastien Gouezel</span>  Sorry, I forgot to ask, what if I also wanted the decidable instance?<br>
I can't just add <code>[decidable_rel (≤)]</code>...</p>

#### [ Kevin Buzzard (Dec 04 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832300):
<div class="codehilite"><pre><span></span><span class="kn">variable</span> <span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span>

<span class="kn">structure</span> <span class="n">basic_thing</span> <span class="n">α</span> <span class="kn">extends</span> <span class="n">has_mul</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">basic</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">a</span><span class="o">)</span>

<span class="c1">-- mathematically sensible object</span>
<span class="kn">structure</span> <span class="n">extension1</span> <span class="n">α</span> <span class="kn">extends</span> <span class="n">basic_thing</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">thing1</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span>
<span class="o">(</span><span class="n">thing2</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">α</span><span class="o">)</span>

<span class="c1">-- mathematically sensible object</span>
<span class="kn">structure</span> <span class="n">extension2</span> <span class="n">α</span> <span class="kn">extends</span> <span class="n">basic_thing</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">thing2</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">α</span><span class="o">)</span>
<span class="o">(</span><span class="n">thing3</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">α</span><span class="o">)</span>
<span class="o">(</span><span class="n">axiom1</span> <span class="o">:</span> <span class="n">thing2</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">=</span> <span class="n">thing3</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span>

<span class="c1">-- mathematically sensible object</span>
<span class="kn">structure</span> <span class="n">extension3</span> <span class="n">α</span> <span class="kn">extends</span> <span class="n">basic_thing</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">thing2</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">α</span><span class="o">)</span>
<span class="o">(</span><span class="n">thing7</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">α</span><span class="o">)</span>
<span class="o">(</span><span class="n">axiom2</span><span class="o">:</span> <span class="n">thing7</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">=</span> <span class="n">thing2</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span>

<span class="c1">-- mathematically sensible object</span>
<span class="kn">structure</span> <span class="n">extension23</span> <span class="n">α</span> <span class="kn">extends</span> <span class="n">basic_thing</span> <span class="n">α</span> <span class="o">:=</span><span class="bp">...</span>
<span class="c1">-- I want to extend extension2 and extension3</span>
<span class="c1">-- but now I have to start defining mixins</span>

<span class="c1">-- insert 1000 lines of code here</span>

<span class="c1">-- object I realise I want later on</span>
<span class="kn">structure</span> <span class="n">extension123</span> <span class="n">α</span> <span class="kn">extends</span> <span class="n">basic_thing</span> <span class="n">α</span> <span class="o">:=</span><span class="bp">...</span>
<span class="c1">-- oh dear, I now have to go back and refactor</span>
<span class="c1">-- everything because I want to extend 1 and 2 and 3 now</span>
<span class="c1">-- so maybe I need to remix my mixins</span>
<span class="c1">-- but the mixins are artificial objects anyway, I don&#39;t</span>
<span class="c1">-- really want to make new ones :-/</span>
</pre></div>

#### [ Johannes Hölzl (Dec 04 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832348):
<p>You need to annotate the <code>(≤)</code> in <code>[decidable_rel (≤)]</code>: <code>[decidable_rel ((≤) : α -&gt; α -&gt; Prop)]</code></p>

#### [ Kevin Buzzard (Dec 04 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832432):
<p>@AHan what happens if you just add exactly the extra hypotheses you need and then insert them manually into the type class inference system?</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="bp">...</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">extra_axiom</span> <span class="n">alpha</span><span class="o">)</span> <span class="bp">...</span> <span class="c1">-- round brackets not square</span>
<span class="bp">...</span>
<span class="k">begin</span>
  <span class="n">letI</span> <span class="o">:=</span> <span class="n">H</span><span class="o">,</span> <span class="c1">-- manually insert</span>
  <span class="n">letI</span> <span class="o">:</span> <span class="n">decidable_linear_order</span> <span class="n">alpha</span> <span class="o">:=</span> <span class="o">{</span> <span class="c1">-- manually build },</span>
<span class="bp">...</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Dec 04 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832451):
<p>You will I guess need to import <code>tactic.interactive</code> for this, from mathlib</p>

#### [ Kevin Buzzard (Dec 04 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832529):
<p>Aah -- Johannes has a better solution ;-)</p>

#### [ AHan (Dec 04 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832535):
<p>Still doesn't work at <code>(le_of_not_lt h₂)</code> in this case...</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finset</span>
<span class="kn">namespace</span> <span class="n">finset</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>
<span class="kn">variables</span> <span class="o">[</span><span class="n">lattice</span><span class="bp">.</span><span class="n">semilattice_sup_bot</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_rel</span> <span class="o">((</span><span class="bp">≤</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)]</span> <span class="o">[</span><span class="n">is_total</span> <span class="n">α</span> <span class="o">(</span><span class="bp">≤</span><span class="o">)]</span>

<span class="kn">lemma</span> <span class="n">mem_of_sup_id</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">},</span> <span class="n">a</span> <span class="bp">≠</span> <span class="err">∅</span> <span class="bp">→</span> <span class="n">a</span><span class="bp">.</span><span class="n">sup</span> <span class="n">id</span> <span class="err">∈</span> <span class="n">a</span>
<span class="bp">|</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">finset</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">a</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">false</span><span class="bp">.</span><span class="n">elim</span> <span class="o">(</span><span class="n">a</span> <span class="o">(</span><span class="n">refl</span> <span class="bp">_</span><span class="o">)))</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">notin</span> <span class="n">ih</span> <span class="n">notempty</span><span class="o">,</span> <span class="k">begin</span>
        <span class="n">rw</span> <span class="o">[</span><span class="n">finset</span><span class="bp">.</span><span class="n">insert_eq</span><span class="o">,</span> <span class="n">finset</span><span class="bp">.</span><span class="n">sup_union</span><span class="o">,</span> <span class="n">finset</span><span class="bp">.</span><span class="n">mem_union</span><span class="o">,</span> <span class="n">finset</span><span class="bp">.</span><span class="n">sup_singleton</span><span class="o">],</span>
        <span class="n">simp</span><span class="o">,</span>
        <span class="k">from</span> <span class="k">if</span> <span class="n">h₁</span> <span class="o">:</span> <span class="n">y</span> <span class="bp">=</span> <span class="err">∅</span>
        <span class="k">then</span> <span class="k">begin</span>
            <span class="n">left</span><span class="o">,</span>
            <span class="n">rw</span> <span class="o">[</span><span class="n">h₁</span><span class="o">,</span> <span class="n">finset</span><span class="bp">.</span><span class="n">sup_empty</span><span class="o">,</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">sup_bot_eq</span><span class="o">],</span>
        <span class="kn">end</span>
        <span class="k">else</span> <span class="k">begin</span>
            <span class="k">from</span> <span class="k">if</span> <span class="n">h₂</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="n">y</span><span class="bp">.</span><span class="n">sup</span> <span class="n">id</span>
            <span class="k">then</span> <span class="k">begin</span>
                <span class="n">right</span><span class="o">,</span>
                <span class="n">rw</span> <span class="o">[</span><span class="n">lattice</span><span class="bp">.</span><span class="n">sup_of_le_right</span> <span class="o">(</span><span class="n">le_of_lt</span> <span class="n">h₂</span><span class="o">)],</span>
                <span class="n">apply</span> <span class="n">ih</span> <span class="n">h₁</span><span class="o">,</span>
            <span class="kn">end</span>
            <span class="k">else</span> <span class="k">begin</span>
                <span class="n">left</span><span class="o">,</span>
                <span class="c1">--rw [lattice.sup_of_le_left (le_of_not_lt h₂)],</span>
            <span class="kn">end</span>
        <span class="kn">end</span>
    <span class="kn">end</span><span class="o">)</span>

<span class="kn">end</span> <span class="n">finset</span>
</pre></div>

#### [ Kevin Buzzard (Dec 04 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832627):
<p>@AHan can you post fully working code? I am lost with the imports, sections, parameters etc. I can try and fix it but it would be nice to just be able to cut and paste one thing</p>

#### [ Kevin Buzzard (Dec 04 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832639):
<p>Sorry, I don't understand sections, parameters etc as well as most of the others here :-)</p>

#### [ Kevin Buzzard (Dec 04 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832652):
<p><span class="user-mention" data-user-id="133545">@AHan</span></p>

#### [ Johannes Hölzl (Dec 04 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832713):
<p><code>#check @le_of_not_lt</code> tells us that it really needs a <code>linear_order</code>.</p>

#### [ Kevin Buzzard (Dec 04 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832794):
<p><span class="user-mention" data-user-id="133545">@AHan</span> oh it's Ok, I got your code (not) working.</p>

#### [ AHan (Dec 04 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150832813):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>  Sorry, I just edited the code!</p>

#### [ AHan (Dec 04 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833026):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span>  Yeah, so seems like <code>[is_total α (≤)]</code> can't work on this case?</p>

#### [ Johannes Hölzl (Dec 04 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833041):
<p>Not when you want to use <code>le_of_not_lt</code>...</p>

#### [ AHan (Dec 04 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833089):
<p>Or is there any better way to prove the function without needing <code>(≤)</code> to be a linear_order ...?</p>

#### [ Kevin Buzzard (Dec 04 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833091):
<div class="codehilite"><pre><span></span>                <span class="n">haveI</span> <span class="o">:</span> <span class="n">linear_order</span> <span class="n">α</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span><span class="o">,</span> <span class="c1">-- fails</span>
                <span class="n">rw</span> <span class="o">[</span><span class="n">lattice</span><span class="bp">.</span><span class="n">sup_of_le_left</span> <span class="o">(</span><span class="n">le_of_not_lt</span> <span class="n">h₂</span><span class="o">)],</span>
</pre></div>


<p>Your problem is that the type class inference system cannot figure out that alpha is a linear order.</p>

#### [ Kevin Buzzard (Dec 04 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833094):
<p>Even though all the data is there.</p>

#### [ Kevin Buzzard (Dec 04 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833124):
<p>You probably need to do some <code>refine_struct</code> stuff</p>

#### [ Kevin Buzzard (Dec 04 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833134):
<p>This is a great example of exactly what the problem is.</p>

#### [ Johannes Hölzl (Dec 04 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833174):
<p>Also not <code>haveI</code> but <code>letI</code> the order contains the relation</p>

#### [ Johannes Hölzl (Dec 04 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833181):
<p><code>letI : linear_order α := { le_total := _ },</code></p>

#### [ Kevin Buzzard (Dec 04 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833183):
<p>Oops, I always screw this up.</p>

#### [ Johan Commelin (Dec 04 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833209):
<p>I think whenever there is data involved you should use <code>let</code> and not <code>have</code>.</p>

#### [ Kevin Buzzard (Dec 04 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833215):
<div class="codehilite"><pre><span></span>invalid structure value { ... }, field &#39;le&#39; was not provided
</pre></div>

#### [ Kevin Buzzard (Dec 04 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833222):
<blockquote>
<p>I think whenever there is data involved you should use <code>let</code> and not <code>have</code>.</p>
</blockquote>
<p>Sure -- I just always forget that there is data involved.</p>

#### [ Kevin Buzzard (Dec 04 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833285):
<blockquote>
<p><code>letI : linear_order α := { le_total := _ },</code></p>
</blockquote>
<p>I think we need to tell Lean about the partial order somehow. But I can never remember these arcane structure extension tricks.</p>

#### [ Kevin Buzzard (Dec 04 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833293):
<p>Do we do refine_struct? extends? <code>by refine</code> somehow?</p>

#### [ Johannes Hölzl (Dec 04 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833324):
<div class="codehilite"><pre><span></span>  letI : linear_order α :=
    { le_total := is_total.total (≤), .. _inst_1 },
</pre></div>

#### [ Johannes Hölzl (Dec 04 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833334):
<p><code>_inst_1</code> is the name of the semilattice sup bot instance.</p>

#### [ AHan (Dec 04 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833401):
<p>Wow! It works!<br>
But... I don't quite get why this work..?</p>

#### [ Kevin Buzzard (Dec 04 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833424):
<p><span class="user-mention" data-user-id="133545">@AHan</span> what is happening with Johannes' magic code is that he is explicitly building the term of type <code>linear_order alpha</code> from the pieces you already have (<code>_inst_1</code> is the partial order etc) and then he is inserting it into the type class inference system with <code>letI</code>.</p>

#### [ Kevin Buzzard (Dec 04 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833484):
<p>It is absolutely clear to anyone watching that this is a pretty hacky and horrible solution, but as far as I can see it is the only one we have that works in general.</p>

#### [ Patrick Massot (Dec 04 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833492):
<p>Having to type <code>_inst_1</code> is always a bad omen</p>

#### [ Kevin Buzzard (Dec 04 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833508):
<p>No doubt you can get around it with some sort of <code>by apply_instance</code> trickery. But ultimately this is not a situation which scales.</p>

#### [ Kevin Buzzard (Dec 04 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833560):
<p>Ultimately one does not want <code>distrib</code>s because they are useless objects. They serve a purpose which is to give a hacky fix to a problem which deserves a better fix but which I have no ideas about.</p>

#### [ Kevin Buzzard (Dec 04 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833600):
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">distrib</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">has_mul</span> <span class="n">α</span><span class="o">,</span> <span class="n">has_add</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">left_distrib</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">a</span> <span class="bp">*</span> <span class="o">(</span><span class="n">b</span> <span class="bp">+</span> <span class="n">c</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">a</span> <span class="bp">*</span> <span class="n">b</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">a</span> <span class="bp">*</span> <span class="n">c</span><span class="o">))</span>
<span class="o">(</span><span class="n">right_distrib</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">)</span> <span class="bp">*</span> <span class="n">c</span> <span class="bp">=</span> <span class="o">(</span><span class="n">a</span> <span class="bp">*</span> <span class="n">c</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">b</span> <span class="bp">*</span> <span class="n">c</span><span class="o">))</span>
</pre></div>


<p>a.k.a. "here are some axioms which make no sense by themselves, but which we need to beef up structure X to structure Y so we have to have an entirely new typeclass"</p>

#### [ Johannes Hölzl (Dec 04 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150833714):
<p>you can always give your <code>semilattie...</code> instance a concrete name, but then you need to mark it a <code>include</code> or add it to your theorem statement (the anonymous instances are always added as long as the type in you type class instance is used in the theorem statement)</p>

#### [ Mario Carneiro (Dec 04 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150835207):
<p>this is one of my favorite uses of the french quotes for getting a term by its type</p>

#### [ Johan Commelin (Dec 04 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150835883):
<p>Hah, now I can golf the <code>assumption</code> tactic:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span> <span class="n">X</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">exact</span> <span class="err">‹</span><span class="bp">_</span><span class="err">›</span>
<span class="c1">--assumption</span>
<span class="kn">end</span>
</pre></div>

#### [ AHan (Dec 04 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conflict%20of%20Instances/near/150836031):
<p>Oh I got it! Thanks a lot for the explanation!!</p>


{% endraw %}
