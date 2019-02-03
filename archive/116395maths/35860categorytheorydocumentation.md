---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/35860categorytheorydocumentation.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [category theory documentation](https://leanprover-community.github.io/archive/116395maths/35860categorytheorydocumentation.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Simon Hudon (Jan 01 2019 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154133811):
<p>Is there a transcript of the rationale behind the design decisions of the category theory part? Specifically, I'd like to know what were the pros and cons of defining <code>category</code> as a type class versus as a structure.</p>

#### [ Johan Commelin (Jan 01 2019 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154136146):
<p>I guess one of the big pros of using a type class is that Lean will do more work for you... more automation. And the category theory tries to maximize automation as much as possible.<br>
(There is still a lot more to be done, and in fact more has been done in Scott's repositories. Quite often you will see proof obligations in the category-lib written out explicitly that are transparent in Scott's repos because he has better automation than mathlib.)</p>

#### [ Reid Barton (Jan 01 2019 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154137154):
<p>The main pro is it lets you write <code>a ⟶ b</code></p>

#### [ Simon Hudon (Jan 01 2019 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154138026):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> That's a good point. At the same time, that's also a downside because this notation does not tell you which category you're talking of and, I don't know if it's the corner of category theory that I'm in but it seems to be often relevant to distinguish.</p>

#### [ Simon Hudon (Jan 01 2019 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154138030):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> Can you give me examples of automation that are made possible that way?</p>

#### [ Johan Commelin (Jan 01 2019 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154138082):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Maybe it is not so much automation as it is brevity. Now you don't have to feed Lean the category structure when writing down functors or limits (or hom-sets).</p>

#### [ Johan Commelin (Jan 01 2019 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154138085):
<p>Are you saying that you often have multiple category structures on the same type?</p>

#### [ Reid Barton (Jan 01 2019 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154138484):
<p>You can always use <code>@category.hom</code> explicitly but it might be more convenient (or not) to create synonyms of the underlying type for the different category structures</p>

#### [ Simon Hudon (Jan 01 2019 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154138486):
<p>Yes. Often might be over stating it as I'm a very fresh category noob. Let's say I'm seeing a repetition in the proofs I find the hardest and this confusion contributes to it</p>

#### [ Simon Hudon (Jan 01 2019 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154138563):
<p>But Johan, I'm not suggesting that you write <code>functor C 𝒞 D 𝒟</code>; rather I'd let <code>𝒞</code> and <code>𝒟</code> stand for both the carrier type and the data+proofs by using <code>has_coe_to_sort</code> (please don't kill me <span class="user-mention" data-user-id="110087">@Scott Morrison</span>, I know you're sick of coercions but maybe this time ...)</p>

#### [ Simon Hudon (Jan 01 2019 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154138657):
<blockquote>
<p>You can always use <code>@category.hom</code> explicitly but it might be more convenient (or not) to create synonyms of the underlying type for the different category structures</p>
</blockquote>
<p>Maybe you're right. I could write a reducible definition so that I don't have to feed both the type and the instance. It does not make up for the other shortcoming of type classes though: with <code>category.{u}</code>, inference is often hindered.</p>

#### [ Mario Carneiro (Jan 01 2019 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154138672):
<p><code>small_category</code> was supposed to help with that, but I guess it doesn't get used much in favor of more generality</p>

#### [ Simon Hudon (Jan 01 2019 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154138754):
<p>I thought so. That's too bad!</p>

#### [ Reid Barton (Jan 01 2019 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154138799):
<blockquote>
<p>But Johan, I'm not suggesting that you write <code>functor C 𝒞 D 𝒟</code>; rather I'd let <code>𝒞</code> and <code>𝒟</code> stand for both the carrier type and the data+proofs by using <code>has_coe_to_sort</code> (please don't kill me <span class="user-mention" data-user-id="110087">@Scott Morrison</span>, I know you're sick of coercions but maybe this time ...)</p>
</blockquote>
<p>This sounds like bundled vs unbundled categories (e.g. <a href="https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/category_theory/bundled.lean" target="_blank" title="https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/category_theory/bundled.lean">https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/category_theory/bundled.lean</a>). I'm not sure whether bundled categories were ever considered as the primary interface. It seems like it could be a viable option. It's possible that Scott just chose to use unbundled ones on the basis that other structures (groups, etc.) are unbundled.</p>

#### [ Johan Commelin (Jan 01 2019 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154138871):
<p>Instead of a reducible type, you could also create a <code>local abbreviation</code> for <code>@category.hom</code>, right?</p>

#### [ Simon Hudon (Jan 01 2019 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139060):
<p>I didn't know you could make abbreviation local. Is that useful?</p>

#### [ Simon Hudon (Jan 01 2019 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139071):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> That looks good! I might steal it for myself. Do you see a downside to having the coercion?</p>

#### [ Reid Barton (Jan 01 2019 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139079):
<p>Like at lines 22-23?</p>

#### [ Reid Barton (Jan 01 2019 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139082):
<p>To be honest, I've hardly used this at all. I was going to prove that Cat has colimits, but I didn't get very far.</p>

#### [ Johan Commelin (Jan 01 2019 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139126):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> I think they have <code>tspace</code> as abbreviation for <code>@topological_space</code> in the <code>topological_space.lean</code> file.</p>

#### [ Reid Barton (Jan 01 2019 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139182):
<p>there's some <code>local notation `cont` := @continuous _ _</code> I think</p>

#### [ Johan Commelin (Jan 01 2019 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139194):
<div class="codehilite"><pre><span></span>git grep tspace
analysis/topology/continuity.lean:local notation `tspace` := topological_space
</pre></div>

#### [ Johan Commelin (Jan 01 2019 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139196):
<p>So my memory partly failed me.</p>

#### [ Simon Hudon (Jan 01 2019 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139198):
<p>Ah! Ok! It's a local notation, not an an abbreviation</p>

#### [ Johan Commelin (Jan 01 2019 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139243):
<p>Right... (I don't even know the difference...)</p>

#### [ Reid Barton (Jan 01 2019 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139249):
<p>the difference is nobody knows what <code>abbreviation</code> does <span class="emoji emoji-263a" title="smile">:smile:</span></p>

#### [ Reid Barton (Jan 01 2019 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139267):
<p>Coercions tend to break down once you have implicit parameters inside the term being coerced that Lean needs to infer.</p>

#### [ Simon Hudon (Jan 01 2019 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139279):
<p>Haha! Abbreviation is sometimes useful but if you use it wrong it's pretty annoying because it doesn't come with equations and you can decide to unfold it. And yet, it's not notation because it is represented in the syntax tree, it has a type, etc</p>

#### [ Simon Hudon (Jan 01 2019 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139323):
<p>I've seen that, it's true. I hear coercion used to be better in Lean 2.</p>

#### [ Reid Barton (Jan 01 2019 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139330):
<p>Maybe an example would be if we had <code>over X : Cat</code>, where <code>X : C</code> and <code>C : Cat</code>, then in <code>A : over X</code>, Lean might play dumb and pretend not to be able to figure out what <code>C</code> is</p>

#### [ Simon Hudon (Jan 01 2019 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139386):
<p>Did it happen with this example?</p>

#### [ Reid Barton (Jan 01 2019 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139399):
<p>This is just hypothetical because I never got as far as doing things like that with bundled categories</p>

#### [ Reid Barton (Jan 01 2019 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139415):
<p>I guess one could test with something like <code>def over {C : Cat} (X : C) : Cat := C</code> (not the right definition, but it shouldn't matter) and then try to use the coercion</p>

#### [ Reid Barton (Jan 01 2019 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139465):
<p>It also might only fail when Lean needs to use information from outside the thing being coerced to infer implicit arguments inside it--not sure</p>

#### [ Simon Hudon (Jan 01 2019 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139611):
<p>I mostly ran into trouble when using coercion to function types and never with coerce to sort. And one reason I would run into trouble was that I coerced to a polymorphic function type and I needed to infer some of the type parameters and Lean would just give up</p>

#### [ Simon Hudon (Jan 01 2019 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139820):
<p>I think I'll run an experiment with reformulating mathlib that way and see how difficult it is</p>

#### [ Reid Barton (Jan 01 2019 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154139854):
<p>Yeah, I can't remember having any issues with coercions to sort either</p>

#### [ Simon Hudon (Jan 01 2019 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154140187):
<p>I just had a quick look and the following works:</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">cat</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">.</span><span class="o">{</span><span class="n">max</span> <span class="o">(</span><span class="n">u</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="n">v</span><span class="bp">+</span><span class="mi">1</span><span class="o">}</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">carrier</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span>
<span class="o">[</span><span class="n">inst</span> <span class="o">:</span> <span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span><span class="o">}</span> <span class="n">carrier</span><span class="o">]</span>

<span class="kn">instance</span> <span class="n">has_coe_to_sort</span><span class="bp">.</span><span class="n">cat</span> <span class="o">:</span> <span class="n">has_coe_to_sort</span> <span class="n">cat</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">S</span> <span class="o">:=</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
  <span class="n">coe</span> <span class="o">:=</span> <span class="n">cat</span><span class="bp">.</span><span class="n">carrier</span> <span class="o">}</span>

<span class="n">def</span> <span class="n">Hom</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="n">cat</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}}</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">C</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">category</span><span class="bp">.</span><span class="n">hom</span> <span class="bp">_</span> <span class="n">C</span><span class="bp">.</span><span class="n">inst</span> <span class="n">x</span> <span class="n">y</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="n">cat</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}}</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">C</span><span class="o">)</span>

<span class="bp">#</span><span class="kn">check</span> <span class="n">Hom</span> <span class="n">x</span> <span class="n">y</span>
</pre></div>

#### [ Simon Hudon (Jan 01 2019 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154140275):
<p>And then I can define the following notation:</p>
<div class="codehilite"><pre><span></span><span class="kn">notation</span> <span class="n">x</span> <span class="bp">`</span> <span class="err">⟶</span><span class="o">[</span><span class="bp">`</span> <span class="n">c</span> <span class="bp">`</span><span class="o">]</span> <span class="bp">`</span> <span class="n">y</span> <span class="o">:=</span> <span class="n">Hom</span> <span class="n">c</span> <span class="n">x</span> <span class="n">y</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">Hom</span> <span class="n">C</span> <span class="n">x</span> <span class="n">y</span>
<span class="c1">-- x ⟶[C] y : Type v</span>

<span class="n">local</span> <span class="kn">infix</span> <span class="bp">`</span> <span class="err">⟶</span> <span class="bp">`</span> <span class="o">:=</span> <span class="n">Hom</span> <span class="bp">_</span>

<span class="bp">#</span><span class="kn">check</span> <span class="n">Hom</span> <span class="n">C</span> <span class="n">x</span> <span class="n">y</span>
<span class="c1">-- x ⟶ y : Type v</span>
</pre></div>

#### [ Reid Barton (Jan 01 2019 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154140405):
<p>A bonus is that we can now give the category of types the correct name, namely <strong>Set</strong></p>

#### [ Johan Commelin (Jan 01 2019 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154141701):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Don't you mean to make the argument <code>C</code> to <code>Hom</code> <em>explicit</em>?</p>

#### [ Simon Hudon (Jan 01 2019 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154141723):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> Yes you're right! I changed it in my file and didn't bother fixing it here but it does matter you're right</p>

#### [ Simon Hudon (Jan 01 2019 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154141731):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> Wouldn't you define <em>Set</em> using <code>set_theory</code> instead?</p>

#### [ Reid Barton (Jan 01 2019 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154142219):
<p>Nope!</p>

#### [ Reid Barton (Jan 01 2019 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154142273):
<p>It would be messy, and equivalent anyways</p>

#### [ Reid Barton (Jan 01 2019 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154142345):
<p><code>set_theory</code> sets have notions like global membership/subset predicates, which aren't relevant to Set</p>

#### [ Simon Hudon (Jan 01 2019 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154142459):
<p>Oh! That simplifies a lot! I was trying to understand pushouts and pullbacks and on <a href="http://ncatlab.org" target="_blank" title="http://ncatlab.org">ncatlab.org</a>, they refer to Set a lot so I kind of pulled back from them</p>

#### [ Reid Barton (Jan 01 2019 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154142511):
<p>The dictionary for reading mathematics is <code>Type</code> = set, and <code>set</code> = subset</p>

#### [ Reid Barton (Jan 01 2019 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154142514):
<p>(outside of set theory of course)</p>

#### [ Simon Hudon (Jan 01 2019 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20documentation/near/154142524):
<p>Ooooh</p>


{% endraw %}
