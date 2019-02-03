---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/23254Splittingfields.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Splitting fields](https://leanprover-community.github.io/archive/116395maths/23254Splittingfields.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (Dec 12 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151535820):
<p>So I thought I'd revive the splitting fields branch on community mathlib. So far I've just updated it to work with current mathlib. This is my definition of splitting fields. It's a bit unusual to write a recursive function like this returning a Type; is this a good approach? Also my definition of <code>of_field</code> the embedding from the base field gives me the error <code>rec_fn_macro only allowed in meta definitions</code>. What is this?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">splitting_field&#39;</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">discrete_field</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="k">by</span> <span class="n">exactI</span> <span class="n">polynomial</span> <span class="n">α</span><span class="o">),</span>
  <span class="k">by</span> <span class="n">exactI</span> <span class="n">nat_degree</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">I</span> <span class="n">f</span> <span class="n">hn</span><span class="o">,</span> <span class="n">α</span>
<span class="bp">|</span> <span class="mi">1</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">I</span> <span class="n">f</span> <span class="n">hn</span><span class="o">,</span> <span class="n">α</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">2</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">I</span> <span class="n">f</span> <span class="n">hn</span><span class="o">,</span> <span class="k">by</span> <span class="n">exactI</span>
  <span class="k">have</span> <span class="n">hf</span> <span class="o">:</span> <span class="n">nat_degree</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span><span class="n">coe</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">adjoin_root</span> <span class="o">(</span><span class="n">irr_factor</span> <span class="n">f</span> <span class="o">(</span><span class="k">by</span> <span class="n">rw</span> <span class="n">hn</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">)))</span> <span class="bp">/</span>
    <span class="o">(</span><span class="n">X</span> <span class="bp">-</span> <span class="n">C</span> <span class="n">root</span><span class="o">))</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">,</span> <span class="k">from</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">splitting_field&#39;</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span><span class="n">coe</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">adjoin_root</span> <span class="o">(</span><span class="n">irr_factor</span> <span class="n">f</span> <span class="o">(</span><span class="k">by</span> <span class="n">rw</span> <span class="n">hn</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">)))</span> <span class="bp">/</span>
    <span class="o">(</span><span class="n">X</span> <span class="bp">-</span> <span class="n">C</span> <span class="n">root</span><span class="o">))</span> <span class="n">hf</span>

<span class="n">def</span> <span class="n">of_field&#39;</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">discrete_field</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="k">by</span> <span class="n">exactI</span> <span class="n">polynomial</span> <span class="n">α</span><span class="o">)</span>
  <span class="o">(</span><span class="n">hf</span> <span class="o">:</span> <span class="k">by</span> <span class="n">exactI</span> <span class="n">nat_degree</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">n</span><span class="o">),</span> <span class="n">α</span> <span class="bp">→</span> <span class="k">by</span> <span class="n">exactI</span> <span class="n">splitting_field&#39;</span> <span class="n">f</span> <span class="n">hf</span>
<span class="bp">|</span> <span class="mi">0</span>     <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">I</span> <span class="n">f</span> <span class="n">hf</span> <span class="n">a</span><span class="o">,</span> <span class="n">a</span>
<span class="bp">|</span> <span class="mi">1</span>     <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">I</span> <span class="n">f</span> <span class="n">hf</span> <span class="n">a</span><span class="o">,</span> <span class="n">a</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">2</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">I</span> <span class="n">f</span> <span class="n">hf</span> <span class="n">a</span><span class="o">,</span> <span class="k">by</span> <span class="n">exactI</span> <span class="n">of_field&#39;</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="err">↑</span><span class="n">a</span> <span class="o">:</span> <span class="n">adjoin_root</span> <span class="bp">_</span><span class="o">)</span>
</pre></div>

#### [ Chris Hughes (Dec 12 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151536840):
<p>Okay I still get the error <code>rec_fn_macro only allowed in meta definitions</code> even if I make it <code>meta</code></p>

#### [ Rob Lewis (Dec 12 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151536970):
<p>Could you rearrange the arguments so that <code> {α : Type u} [discrete_field α]</code> are left of the colon? If nothing else it will let you get rid of the <code>exactI</code>s.</p>

#### [ Rob Lewis (Dec 12 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151536981):
<p>That error sounds like something funny in the equation compiler, so simplifying its job might help.</p>

#### [ Chris Hughes (Dec 12 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151537095):
<p>Not without changing my method significantly. I use a different type when I recursively call it.</p>

#### [ Rob Lewis (Dec 12 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151537161):
<p>Oh, yeah, sorry. I misread that.</p>

#### [ Rob Lewis (Dec 12 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151537354):
<p>Where is <code>adjoin_root</code> defined?</p>

#### [ Rob Lewis (Dec 12 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151537395):
<p>In the splitting field branch on community, I take it.</p>

#### [ Rob Lewis (Dec 12 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151537405):
<p>Think I'm having trouble reading today.</p>

#### [ Johan Commelin (Dec 12 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151537835):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> I think this is exactly the approach that we had in mind when <span class="user-mention" data-user-id="110049">@Mario Carneiro</span>, you and me were hacking on this in Orsay. Too bad it's giving troubles.</p>

#### [ Reid Barton (Dec 12 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151538608):
<p>I'm always tempted to package everything I care about together in a single recursive definition--here the type, its field instance, the map from the base field, the factorization of f</p>

#### [ Reid Barton (Dec 12 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151538615):
<p>using a big sigma or a structure</p>

#### [ Chris Hughes (Dec 12 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151541456):
<p>I found a work around by using <code>nat.rec_on</code> instead of the equation compiler. Seems like it has something to do with this <a href="https://github.com/leanprover/lean/issues/1890" target="_blank" title="https://github.com/leanprover/lean/issues/1890">https://github.com/leanprover/lean/issues/1890</a></p>

#### [ Johan Commelin (Dec 12 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151552987):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> I think that this thread should know about this thread: <a href="#narrow/stream/116395-maths/topic/simple.20field.20theory" title="#narrow/stream/116395-maths/topic/simple.20field.20theory">https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple.20field.20theory</a></p>

#### [ Chris Hughes (Dec 14 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151806515):
<p>I've had a new problem, and it's taken me most of the day to figure out what's going on. I think the trouble is that I have an expression where <code>f : polynomial α</code> is mentioned and also some stuff of type <code>adjoin_root f</code>. When I try to rewrite with <code>f = _</code> It tries to rewrite all the types that mention <code>f</code> and hangs. I solved it using <code>conv</code> but I thought there might be a better way to do this.</p>

#### [ Johan Commelin (Dec 15 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151831239):
<p>Isn't this what <code>conv</code> is meant for? I think there's nothing wrong with using it here.</p>

#### [ Chris Hughes (Dec 16 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868222):
<p>So I've some up against a more serious problem. I've defined something of this type</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">splitting_field_aux</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">discrete_field</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="k">by</span> <span class="n">exactI</span> <span class="n">polynomial</span> <span class="n">α</span><span class="o">),</span>
  <span class="k">by</span> <span class="n">exactI</span> <span class="err">Σ&#39;</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">discrete_field</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">is_field_hom</span> <span class="n">i</span><span class="o">]</span>
  <span class="o">(</span><span class="n">hs</span> <span class="o">:</span> <span class="k">by</span> <span class="n">exactI</span> <span class="n">splits</span> <span class="n">i</span> <span class="n">f</span><span class="o">),</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">discrete_field</span> <span class="n">γ</span><span class="o">]</span> <span class="o">(</span><span class="n">j</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span>
  <span class="o">[</span><span class="n">is_field_hom</span> <span class="n">j</span><span class="o">]</span> <span class="o">(</span><span class="n">hj</span> <span class="o">:</span> <span class="k">by</span> <span class="n">exactI</span> <span class="n">splits</span> <span class="n">j</span> <span class="n">f</span><span class="o">),</span>
  <span class="bp">∃</span> <span class="n">k</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">,</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">k</span> <span class="o">(</span><span class="n">i</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">j</span> <span class="n">x</span><span class="o">)</span> <span class="bp">∧</span> <span class="n">is_field_hom</span> <span class="n">k</span>
</pre></div>


<p>I bundled everything we needed to know together in one definition because I didn't want to have to deal with <code>eq.rec</code> and non definitional equation lemmas. The only trouble with this approach is that the homomorphism from the splitting field into any field that splits only goes into fields in the same universe. The only way around this that I can see is to unbundle the definition, and deal with nasty equation lemmas. Is there any easier way around this?</p>

#### [ Johan Commelin (Dec 16 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868598):
<p>I'm inclined to say that we shouldn't worry about universes here. If universe issues show up, I hope <code>ulift</code> will help.</p>

#### [ Kenny Lau (Dec 16 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868614):
<p>good luck transporting everything to <code>ulift</code> :P</p>

#### [ Mario Carneiro (Dec 16 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868620):
<p>what is the problem with unbundling exactly?</p>

#### [ Mario Carneiro (Dec 16 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868667):
<p>I guess that would be much more convenient to use if it were unbundled, although maybe you need this for the construction?</p>

#### [ Mario Carneiro (Dec 16 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868675):
<p>I think you should try to stay away from "universal definitions" of universal objects, because they are never universe polymorphic enough</p>

#### [ Chris Hughes (Dec 16 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868679):
<p>Then I'd have to unfold the definition to prove things about it. And the equation lemmas are not definitional, so I'd need eq.rec to turn it into <code>adjoin_root whatever </code> and eq.rec is hard to use.</p>

#### [ Chris Hughes (Dec 16 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868720):
<p>What do you mean by stay away from universal definitions?</p>

#### [ Mario Carneiro (Dec 16 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868721):
<p>right, we definitely want to avoid that. But I'm still not following. Could you show a bit of how you get to this point?</p>

#### [ Mario Carneiro (Dec 16 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868729):
<p>For example, you can define <code>nat := \forall X, {X -&gt; (X -&gt; X) -&gt; X // naturality property}</code> but it's not a good definition because <code>X</code> only lives in one universe</p>

#### [ Chris Hughes (Dec 16 2018 at 08:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868774):
<p><a href="https://github.com/ChrisHughes24/mathlib/blob/5efef7b26f78b5bcbcbc43d4d3ae32be7aa6018b/field_theory/splitting_field.lean" target="_blank" title="https://github.com/ChrisHughes24/mathlib/blob/5efef7b26f78b5bcbcbc43d4d3ae32be7aa6018b/field_theory/splitting_field.lean">https://github.com/ChrisHughes24/mathlib/blob/5efef7b26f78b5bcbcbc43d4d3ae32be7aa6018b/field_theory/splitting_field.lean</a></p>

#### [ Mario Carneiro (Dec 16 2018 at 08:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868775):
<p>instead you want some kind of "intrinsic" characterization of the object that implies the universal property, in any universe</p>

#### [ Chris Hughes (Dec 16 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868790):
<p>So in this example, maybe the fact that any proper subfield does not split?</p>

#### [ Chris Hughes (Dec 16 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868793):
<p>I'll have to think about whether that approach is much harder.</p>

#### [ Mario Carneiro (Dec 16 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868957):
<p>In this case, it looks like that is indeed the right "smallness" property</p>

#### [ Mario Carneiro (Dec 16 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868963):
<p>another way to express it is to start from the theorem you just proved, and show that splitting in one universe implies splitting in all the rest</p>

#### [ Mario Carneiro (Dec 16 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151868966):
<p>by taking a special choice of gamma, namely the subfield isomorphic to the gamma in another universe</p>

#### [ Chris Hughes (Dec 16 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151869580):
<p>Proving that such a subfield exists is hard though, unless I'm missing a trick?</p>

#### [ Mario Carneiro (Dec 16 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151869584):
<p>This is a general fact about fields</p>

#### [ Mario Carneiro (Dec 16 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151869631):
<p>Every field hom is injective, so when you restrict to the range you get an isomorphism</p>

#### [ Mario Carneiro (Dec 16 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151869647):
<p>(the isomorphism is not constructive in the reverse direction)</p>

#### [ Chris Hughes (Dec 16 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151869788):
<p>I still don't understand. Given a field, which subfield do I choose?</p>

#### [ Mario Carneiro (Dec 16 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151869922):
<p>oh wait I had it backwards, you need a field <em>into</em> the large universe</p>

#### [ Mario Carneiro (Dec 16 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151869945):
<p>for that you can take a subfield of gamma sufficiently large to contain all the action from beta</p>

#### [ Mario Carneiro (Dec 16 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151869949):
<p>like the subfield generated by polynomials in alpha</p>

#### [ Mario Carneiro (Dec 16 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870003):
<p>this subfield will be isomorphic to a quotient of a polynomial ring etc etc which is in <code>Type u</code></p>

#### [ Chris Hughes (Dec 16 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870007):
<p>I see.</p>

#### [ Mario Carneiro (Dec 16 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870008):
<p>and so your lemma applies and the polynomial splits there</p>

#### [ Mario Carneiro (Dec 16 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870059):
<p>you should double check with <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> , I walked him through this a few months ago and I think he did almost exactly the same thing in the perfectoid project</p>

#### [ Mario Carneiro (Dec 16 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870110):
<p>as an alternative, returning to the unbundling problem: I assume the reason it isn't definitional is because you are using wf recursion</p>

#### [ Mario Carneiro (Dec 16 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870112):
<p>If you define one step of the induction as a lemma, then it will be definitional there</p>

#### [ Chris Hughes (Dec 16 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870163):
<p>That sounds easier.</p>

#### [ Mario Carneiro (Dec 16 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870166):
<p>so you have something like <code>F : (A : Type u) (h : P.{u} A), Type u</code> and <code>prop : (A : Type u) (h : P.{u} A), P.{v} (F A)</code></p>

#### [ Mario Carneiro (Dec 16 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870228):
<p>and then you have an induction proof putting it together, which does <code>F /\ P.{u} F</code>, and a cases proof doing the same thing with conclusion <code>P.{v} F</code></p>

#### [ Chris Hughes (Dec 16 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870287):
<p>It's also not definitional because I've got an <code>ite</code> on <code>degree f \le 1</code></p>

#### [ Mario Carneiro (Dec 16 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870289):
<p>Also, before I forget: a very general way of avoiding problems with types defined by complicated rules is to use an inductive type instead</p>

#### [ Mario Carneiro (Dec 16 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870347):
<p>for example, simulating <code>if x &lt; 2 then nat else unit</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">my_cases</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">nat</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">2</span> <span class="bp">→</span> <span class="n">nat</span> <span class="bp">→</span> <span class="n">my_cases</span>
<span class="bp">|</span> <span class="n">unit</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">&gt;=</span> <span class="mi">2</span> <span class="bp">→</span> <span class="n">unit</span> <span class="bp">→</span> <span class="n">my_cases</span>
</pre></div>

#### [ Mario Carneiro (Dec 16 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870352):
<p>You can do similar stuff with crazy well founded definitions</p>

#### [ Mario Carneiro (Dec 16 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870393):
<p>in the inductive case you don't even have to worry about well foundedness</p>

#### [ Chris Hughes (Dec 16 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151870896):
<p>The other major issue I have is that making it a def gives me the error <code>rec_fn_macro</code> only allowed in meta definitions.</p>

#### [ Mario Carneiro (Dec 16 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151871212):
<p>that means there is probably a tactic referencing one of the <code>_match</code> type variables in the context by accident</p>

#### [ Mario Carneiro (Dec 16 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151871259):
<p>you can fix this by <code>clear</code>ing it when you have used it, or even using it right at the start and clearing it then (or if its random junk then just remove it)</p>

#### [ Chris Hughes (Dec 16 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151871614):
<p>Will <code>resetI</code> cause problems with that?</p>

#### [ Mario Carneiro (Dec 16 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151871616):
<p>I don't think so</p>

#### [ Mario Carneiro (Dec 16 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151871661):
<p>At some version of <code>resetI</code> I recall it deleting the recursive function variable as a side effect, not sure if that's still the case but I think not</p>

#### [ Kevin Buzzard (Dec 16 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/151874009):
<p>I've only just seen this thread. Chris I'll dig out the universe conversation Mario and I had when I'm at a pc</p>

#### [ Chris Hughes (Dec 17 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152018880):
<p>All done and sorry free. <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> are you happy for me to push all of this to the splitting fields branch in community?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">splitting_field</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">polynomial</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">splitting_field</span><span class="bp">.</span><span class="n">type_aux</span> <span class="n">f</span> <span class="n">rfl</span>

<span class="kn">namespace</span> <span class="n">splitting_field</span>

<span class="kn">instance</span> <span class="n">field</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">polynomial</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">discrete_field</span> <span class="o">(</span><span class="n">splitting_field</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">unfold</span> <span class="n">splitting_field</span><span class="bp">;</span> <span class="n">apply_instance</span>

<span class="n">def</span> <span class="n">mk</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">polynomial</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">splitting_field</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">mk_aux</span> <span class="n">f</span> <span class="n">rfl</span>

<span class="kn">instance</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">polynomial</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">is_field_hom</span> <span class="o">(</span><span class="n">mk</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">unfold</span> <span class="n">mk</span><span class="bp">;</span> <span class="n">apply_instance</span>

<span class="kn">lemma</span> <span class="n">splitting_field_splits</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">polynomial</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">splits</span> <span class="o">(</span><span class="n">mk</span> <span class="n">f</span><span class="o">)</span> <span class="n">f</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">splitting_field_aux</span> <span class="n">f</span> <span class="n">rfl</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">2</span>

<span class="n">def</span> <span class="n">hom</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">discrete_field</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">is_field_hom</span> <span class="n">i</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">polynomial</span> <span class="n">α</span><span class="o">)</span>
  <span class="o">(</span><span class="n">hβ</span> <span class="o">:</span> <span class="n">splits</span> <span class="n">i</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="n">splitting_field</span> <span class="n">f</span> <span class="bp">→</span> <span class="n">β</span> <span class="o">:=</span>
<span class="n">classical</span><span class="bp">.</span><span class="n">some</span> <span class="o">(</span><span class="n">exists_hom</span> <span class="bp">_</span> <span class="n">f</span> <span class="n">rfl</span> <span class="n">i</span> <span class="n">hβ</span><span class="o">)</span>

<span class="bp">@</span><span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">hom_is_field_hom</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">discrete_field</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">is_field_hom</span> <span class="n">i</span><span class="o">]</span>
  <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">polynomial</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">hβ</span> <span class="o">:</span> <span class="n">splits</span> <span class="n">i</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="n">is_field_hom</span> <span class="o">(</span><span class="n">hom</span> <span class="n">i</span> <span class="n">f</span> <span class="n">hβ</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">some_spec</span> <span class="o">(</span><span class="n">exists_hom</span> <span class="bp">_</span> <span class="n">f</span> <span class="n">rfl</span> <span class="n">i</span> <span class="n">hβ</span><span class="o">))</span><span class="bp">.</span><span class="mi">2</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">hom_fixes</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">discrete_field</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">is_field_hom</span> <span class="n">i</span><span class="o">]</span>
  <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">polynomial</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">hβ</span> <span class="o">:</span> <span class="n">splits</span> <span class="n">i</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">hom</span> <span class="n">i</span> <span class="n">f</span> <span class="n">hβ</span> <span class="o">(</span><span class="n">mk</span> <span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">i</span> <span class="n">x</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">some_spec</span> <span class="o">(</span><span class="n">exists_hom</span> <span class="bp">_</span> <span class="n">f</span> <span class="n">rfl</span> <span class="n">i</span> <span class="n">hβ</span><span class="o">))</span><span class="bp">.</span><span class="mi">1</span>

<span class="n">attribute</span> <span class="o">[</span><span class="kn">irreducible</span><span class="o">]</span> <span class="n">hom</span> <span class="n">splitting_field</span> <span class="n">splitting_field</span><span class="bp">.</span><span class="n">field</span> <span class="n">splitting_field</span><span class="bp">.</span><span class="n">mk</span>
</pre></div>

#### [ Kenny Lau (Dec 17 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152018894):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> so how did you extract an element from <code>factor_set</code>?</p>

#### [ Chris Hughes (Dec 17 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152018952):
<p>I proved the irreducible factor lemma for a noetherian domain.</p>

#### [ Kenny Lau (Dec 17 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152018963):
<p>see <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> this is problematic</p>

#### [ Chris Hughes (Dec 17 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019049):
<p>I don't think it's problematic. You shouldn't use UFD for that anyway since it's true in greater generality.</p>

#### [ Mario Carneiro (Dec 17 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019448):
<p>Looks good to me, although I would call <code>hom</code> <code>lift</code> instead</p>

#### [ Mario Carneiro (Dec 17 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019459):
<p>what's problematic?</p>

#### [ Kenny Lau (Dec 17 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019463):
<p>that <code>factor_set</code> is hard to use</p>

#### [ Mario Carneiro (Dec 17 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019540):
<p>demo? what's <code>factor_set</code> doing here</p>

#### [ Kenny Lau (Dec 17 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019543):
<p>well could you prove that the factor set of a non-unit non-zero element is nonempty?</p>

#### [ Mario Carneiro (Dec 17 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019546):
<p>what is <code>factor_set</code></p>

#### [ Kenny Lau (Dec 17 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019590):
<p><code>associates.factor_set</code></p>

#### [ Patrick Massot (Dec 17 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019591):
<p>Kenny, you shouldn't be so negative</p>

#### [ Mario Carneiro (Dec 17 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019604):
<p>it's not in the mathlib version, remind me what it does</p>

#### [ Kenny Lau (Dec 17 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019613):
<div class="codehilite"><pre><span></span><span class="n">associates</span><span class="bp">.</span><span class="n">factors</span> <span class="o">:</span>
  <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">}</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">integral_domain</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_2</span> <span class="o">:</span> <span class="n">unique_factorization_domain</span> <span class="n">α</span><span class="o">]</span>
  <span class="o">[</span><span class="bp">_</span><span class="n">inst_3</span> <span class="o">:</span> <span class="n">decidable_eq</span> <span class="o">(</span><span class="n">associates</span> <span class="n">α</span><span class="o">)],</span> <span class="n">associates</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">associates</span><span class="bp">.</span><span class="n">factor_set</span> <span class="n">α</span>
</pre></div>

#### [ Kenny Lau (Dec 17 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019624):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> well played</p>

#### [ Chris Hughes (Dec 17 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019637):
<p>If it was empty the product would be one. Seems like it's probably not that hard.</p>

#### [ Mario Carneiro (Dec 17 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019643):
<p>oh it's a ufd thing</p>

#### [ Kenny Lau (Dec 17 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019646):
<p>how about that any non-zero non-unit is divisible by an irreducible</p>

#### [ Kenny Lau (Dec 17 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019685):
<p>how do we convert from factors to divisibility</p>

#### [ Mario Carneiro (Dec 17 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019697):
<p><code>dvd_eq_le</code></p>

#### [ Chris Hughes (Dec 17 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019698):
<p>Prove that a UFD is noetherian, and use the lemma I proved.</p>

#### [ Mario Carneiro (Dec 17 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019702):
<p>and <code>factors_le</code></p>

#### [ Kenny Lau (Dec 17 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019721):
<p>I see <span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Mario Carneiro (Dec 17 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019761):
<p>it's a bit cumbersome to state, but it looks like the lemmas are there</p>

#### [ Mario Carneiro (Dec 17 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019840):
<p>Anyway I think you could certainly push this</p>

#### [ Mario Carneiro (Dec 17 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019848):
<p>next stop algebraic closure?</p>

#### [ Mario Carneiro (Dec 17 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152019851):
<p>I guess that's another messy induction like this</p>

#### [ Johan Commelin (Dec 17 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152022286):
<p>Before going towards algebraic closure, I would like to have this PR'd. This is going to be a very useful tool in the theory if finite extensions. I think it makes sense to start defining <code>separable</code> and <code>normal</code> extensions now. We're pretty close to finite Galois extensions.</p>

#### [ Johan Commelin (Dec 17 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152022370):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> What are your plans now?</p>

#### [ Johan Commelin (Dec 17 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152023539):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> I merged master into this branch and pushed.</p>

#### [ Chris Hughes (Dec 17 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152023867):
<p>This branch does now depend on unmerged PRs that I have made.</p>

#### [ Johan Commelin (Dec 17 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152023951):
<p>The one on multiplicities?</p>

#### [ Chris Hughes (Dec 17 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152023975):
<p>And some others. I have three open to do with polynomials right now I think.</p>

#### [ Johan Commelin (Dec 17 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152024033):
<p>Yes, I see. Ok, let's hope those get merged soon.</p>

#### [ Johan Commelin (Dec 17 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152024064):
<p>Do you want to do more with this branch? I mean, it's name is <code>splitting_fields</code>, so maybe new stuff should happen on a new branch?</p>

#### [ Chris Hughes (Dec 17 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152024628):
<p>I think new stuff should happen on a new branch. I think it's best to not make PRs too big.</p>

#### [ Johan Commelin (Dec 17 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152025969):
<p>So, if I'm not mistaken... the first 10 points of <a href="https://github.com/kckennylau/Lean/blob/master/algebraic-closure-roadmap.md" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/algebraic-closure-roadmap.md">https://github.com/kckennylau/Lean/blob/master/algebraic-closure-roadmap.md</a> have now been done. (Although not everything is in mathlib yet.)</p>

#### [ Johan Commelin (Dec 17 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152026250):
<p>Kenny, do you mind if I copy-paste that roadmap to the github wiki of the community repo? Then we can start ticking of things that we've done.</p>

#### [ Kenny Lau (Dec 17 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152026341):
<p>might want to replace the whole discriminant business with just GCD? ah the beauty of impredicativity</p>

#### [ Johan Commelin (Dec 17 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152026448):
<p>According to wiki, a polynomial is separable if it has just as many roots in its splitting field as its degree. So a square of a separable polynomial is not separable... choices...</p>

#### [ Kenny Lau (Dec 17 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152026483):
<p>I don't think we're talking about the same thing</p>

#### [ Johan Commelin (Dec 17 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152026504):
<p>No, indeed. I was asking if we should copy your roadmap to the github wiki...</p>

#### [ Kenny Lau (Dec 17 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152027091):
<p>and I was asking if you might want to change 11-14 to just 14</p>

#### [ Johan Commelin (Dec 17 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152027295):
<p>That seems like a good plan.</p>

#### [ Kenny Lau (Dec 17 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152027590):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> and my only objection would be predicativity</p>

#### [ Kenny Lau (Dec 17 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152027650):
<p>which I'm sure less people care about, compared to constructivity...</p>

#### [ Johan Commelin (Dec 17 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20fields/near/152033427):
<p><a href="https://github.com/leanprover-community/mathlib/wiki/Algebraic-closure-roadmap" target="_blank" title="https://github.com/leanprover-community/mathlib/wiki/Algebraic-closure-roadmap">https://github.com/leanprover-community/mathlib/wiki/Algebraic-closure-roadmap</a></p>


{% endraw %}
