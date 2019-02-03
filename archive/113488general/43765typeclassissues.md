---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/43765typeclassissues.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [type class issues](https://leanprover-community.github.io/archive/113488general/43765typeclassissues.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Nov 14 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147694692):
<p>This is amazing: <a href="https://gist.githubusercontent.com/jcommelin/8736c28a8e74f3d478b1c2b7737fa513/raw/d655018af064ef75572afb17d2ffb7d051c500c0/crazy_type_class_error.lean" target="_blank" title="https://gist.githubusercontent.com/jcommelin/8736c28a8e74f3d478b1c2b7737fa513/raw/d655018af064ef75572afb17d2ffb7d051c500c0/crazy_type_class_error.lean">https://gist.githubusercontent.com/jcommelin/8736c28a8e74f3d478b1c2b7737fa513/raw/d655018af064ef75572afb17d2ffb7d051c500c0/crazy_type_class_error.lean</a><br>
I feel like the algorithm could be a lot smarter here. For example, search for <code>x_52</code> on that page, and go to the first match. You will be on the last line of this chunk of code:</p>
<div class="codehilite"><pre><span></span><span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">1</span><span class="o">)</span> <span class="err">?</span><span class="n">x_32</span> <span class="o">:</span> <span class="n">category</span>
  <span class="o">(</span><span class="bp">@</span><span class="n">comma</span> <span class="o">{</span><span class="n">X</span> <span class="bp">//</span> <span class="n">B</span> <span class="n">X</span><span class="o">}</span>
     <span class="o">(</span><span class="bp">@</span><span class="n">category_theory</span><span class="bp">.</span><span class="n">full_subcategory</span> <span class="o">(</span><span class="bp">@</span><span class="n">opens</span> <span class="n">X</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">)</span>
        <span class="o">(</span><span class="bp">@</span><span class="n">site</span><span class="bp">.</span><span class="n">to_category</span> <span class="o">(</span><span class="bp">@</span><span class="n">opens</span> <span class="n">X</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">)</span> <span class="o">(</span><span class="bp">@</span><span class="n">category_theory</span><span class="bp">.</span><span class="n">site</span> <span class="n">X</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">))</span>
        <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="bp">@</span><span class="n">opens</span> <span class="n">X</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">),</span> <span class="n">B</span> <span class="n">X</span><span class="o">))</span>
     <span class="n">punit</span>
     <span class="n">category_theory</span><span class="bp">.</span><span class="n">punit_category</span>
     <span class="o">(</span><span class="bp">@</span><span class="n">opens</span> <span class="n">X</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">)</span>
     <span class="o">(</span><span class="bp">@</span><span class="n">site</span><span class="bp">.</span><span class="n">to_category</span> <span class="o">(</span><span class="bp">@</span><span class="n">opens</span> <span class="n">X</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">)</span> <span class="o">(</span><span class="bp">@</span><span class="n">category_theory</span><span class="bp">.</span><span class="n">site</span> <span class="n">X</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">))</span>
     <span class="o">(</span><span class="bp">@</span><span class="n">full_subcategory_inclusion</span> <span class="o">(</span><span class="bp">@</span><span class="n">opens</span> <span class="n">X</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">)</span>
        <span class="o">(</span><span class="bp">@</span><span class="n">site</span><span class="bp">.</span><span class="n">to_category</span> <span class="o">(</span><span class="bp">@</span><span class="n">opens</span> <span class="n">X</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">)</span> <span class="o">(</span><span class="bp">@</span><span class="n">category_theory</span><span class="bp">.</span><span class="n">site</span> <span class="n">X</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">))</span>
        <span class="n">B</span><span class="o">)</span>
     <span class="o">(</span><span class="bp">@</span><span class="n">functor</span><span class="bp">.</span><span class="n">of_obj</span> <span class="o">(</span><span class="bp">@</span><span class="n">opens</span> <span class="n">X</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">)</span> <span class="o">(</span><span class="bp">@</span><span class="n">site</span><span class="bp">.</span><span class="n">to_category</span> <span class="o">(</span><span class="bp">@</span><span class="n">opens</span> <span class="n">X</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">)</span> <span class="o">(</span><span class="bp">@</span><span class="n">category_theory</span><span class="bp">.</span><span class="n">site</span> <span class="n">X</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">))</span> <span class="n">U</span><span class="o">))</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">category_theory</span><span class="bp">.</span><span class="n">comma_category</span> <span class="err">?</span><span class="n">x_51</span> <span class="err">?</span><span class="n">x_52</span> <span class="err">?</span><span class="n">x_53</span> <span class="err">?</span><span class="n">x_54</span> <span class="err">?</span><span class="n">x_55</span> <span class="err">?</span><span class="n">x_56</span> <span class="err">?</span><span class="n">x_57</span> <span class="err">?</span><span class="n">x_58</span>
</pre></div>


<p>So basically it has already figured out all these type class instances, and it should immediately be able to fill in <code>?x_52</code> and friends. But it doesn't... and then it hits the search limit.</p>

#### [ Johan Commelin (Nov 14 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147695687):
<div class="codehilite"><pre><span></span><span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">4</span><span class="o">)</span> <span class="err">?</span><span class="n">x_238</span> <span class="o">:</span> <span class="n">category</span> <span class="n">punit</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">category_theory</span><span class="bp">.</span><span class="n">small_category</span> <span class="err">?</span><span class="n">x_422</span> <span class="err">?</span><span class="n">x_423</span>
</pre></div>


<p>goes all the way down to</p>
<div class="codehilite"><pre><span></span><span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">12</span><span class="o">)</span> <span class="err">?</span><span class="n">x_460</span> <span class="o">:</span> <span class="n">linear_ordered_field</span> <span class="n">punit</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">discrete_linear_ordered_field</span><span class="bp">.</span><span class="n">to_linear_ordered_field</span> <span class="err">?</span><span class="n">x_461</span> <span class="err">?</span><span class="n">x_462</span>
</pre></div>


<p>I guess it might be a good idea to insert a shortcut somewhere?</p>

#### [ Reid Barton (Nov 14 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147695787):
<p>looks like the actual solution is <code>category punit := category_theory.punit_category</code></p>

#### [ Reid Barton (Nov 14 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147695801):
<p>can we use instance priority to guide the search here?</p>

#### [ Reid Barton (Nov 14 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147695900):
<p>the funny thing is that <code>punit</code>actually has a unique structure of all those classes it looks for</p>

#### [ Johan Commelin (Nov 14 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147695970):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> I'm really confused, because a lot of the time it is finding that instance. But that sometimes it goes astray...</p>

#### [ Reid Barton (Nov 14 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147696000):
<p>Well, it did find it here, eventually</p>

#### [ Reid Barton (Nov 14 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147696077):
<p>Everything looks more or less fine until the max depth error</p>

#### [ Johan Commelin (Nov 14 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147696157):
<p>Hmmm, would it be good strategy if Lean is searching for an instance of <code>foo bar</code> to first check if maybe <code>bar.foo</code> exists?</p>

#### [ Johan Commelin (Nov 14 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147696190):
<p>Because that would find <code>punit.category</code> instantly...</p>

#### [ Johan Commelin (Nov 14 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147696563):
<p>Ahrg, this is so annoying. So now I can start writing lots of <code>@</code> signs, and insert the typeclass instances manually, and the code becomes unreadable...</p>

#### [ Kenny Lau (Nov 14 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147696720):
<p>I really doubt how this will scale</p>

#### [ Kenny Lau (Nov 14 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147696724):
<p>as we get more things into mathlib</p>

#### [ Mario Carneiro (Nov 14 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147696835):
<p>I think <code>category_theory.small_category</code> is misnamed...</p>

#### [ Reid Barton (Nov 14 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697038):
<p>Either <span class="emoji emoji-1f340" title="four leaf clover">:four_leaf_clover:</span> will have to improve the instance search algorithm, or we will have to start being more careful about how we write instances, with other tradeoffs</p>

#### [ Johan Commelin (Nov 14 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697069):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Can you elaborate?</p>

#### [ Johan Commelin (Nov 14 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697085):
<p>I now have</p>
<div class="codehilite"><pre><span></span><span class="n">obj</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span><span class="o">,</span> <span class="bp">@</span><span class="n">limit</span> <span class="bp">_</span> <span class="o">(</span><span class="bp">@</span><span class="n">category_theory</span><span class="bp">.</span><span class="n">opposite</span> <span class="bp">_</span>
<span class="o">(</span><span class="bp">@</span><span class="n">category_theory</span><span class="bp">.</span><span class="n">comma_category</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">punit_category</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">))</span> <span class="bp">_</span> <span class="bp">_</span>
<span class="o">((</span><span class="n">comma</span><span class="bp">.</span><span class="n">fst</span> <span class="o">(</span><span class="n">full_subcategory_inclusion</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">of_obj</span> <span class="n">U</span><span class="o">))</span><span class="bp">.</span><span class="n">op</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">)</span> <span class="bp">_</span><span class="o">,</span>
</pre></div>


<p>and I get red squiggles under the <code>⋙</code> at the end.</p>

#### [ Johan Commelin (Nov 14 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697150):
<p>Errors:</p>
<div class="codehilite"><pre><span></span><span class="n">failed</span> <span class="n">to</span> <span class="n">synthesize</span> <span class="n">type</span> <span class="n">class</span> <span class="kn">instance</span> <span class="n">for</span>
<span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">X</span><span class="o">,</span>
<span class="n">B</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">opens</span> <span class="n">X</span><span class="o">),</span>
<span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="err">𝒞</span> <span class="o">:</span> <span class="n">category</span> <span class="n">C</span><span class="o">,</span>
<span class="n">F</span> <span class="o">:</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">presheaf</span> <span class="err">↥</span><span class="n">B</span> <span class="n">C</span><span class="o">,</span>
<span class="n">U</span> <span class="o">:</span> <span class="n">opens</span> <span class="n">X</span><span class="err">ᵒᵖ</span>
<span class="err">⊢</span> <span class="n">category</span> <span class="n">comma</span> <span class="o">(</span><span class="n">full_subcategory_inclusion</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">of_obj</span> <span class="n">U</span><span class="o">)</span><span class="err">ᵒᵖ</span>
<span class="n">sheaf</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="mi">414</span><span class="o">:</span><span class="mi">66</span><span class="o">:</span> <span class="n">error</span>

<span class="n">synthesized</span> <span class="n">type</span> <span class="n">class</span> <span class="kn">instance</span> <span class="n">is</span> <span class="n">not</span> <span class="n">definitionally</span> <span class="n">equal</span> <span class="n">to</span> <span class="n">expression</span> <span class="n">inferred</span> <span class="k">by</span> <span class="n">typing</span> <span class="n">rules</span><span class="o">,</span> <span class="n">synthesized</span>
  <span class="err">⁇</span>
<span class="n">inferred</span>
  <span class="n">category_theory</span><span class="bp">.</span><span class="n">opposite</span>
<span class="n">sheaf</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="mi">414</span><span class="o">:</span><span class="mi">66</span><span class="o">:</span> <span class="n">error</span>

<span class="n">failed</span> <span class="n">to</span> <span class="n">synthesize</span> <span class="n">type</span> <span class="n">class</span> <span class="kn">instance</span> <span class="n">for</span>
<span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">X</span><span class="o">,</span>
<span class="n">B</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">opens</span> <span class="n">X</span><span class="o">),</span>
<span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="err">𝒞</span> <span class="o">:</span> <span class="n">category</span> <span class="n">C</span><span class="o">,</span>
<span class="n">F</span> <span class="o">:</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">presheaf</span> <span class="err">↥</span><span class="n">B</span> <span class="n">C</span><span class="o">,</span>
<span class="n">U</span> <span class="o">:</span> <span class="n">opens</span> <span class="n">X</span><span class="err">ᵒᵖ</span>
<span class="err">⊢</span> <span class="n">category</span> <span class="n">comma</span> <span class="o">(</span><span class="n">full_subcategory_inclusion</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">of_obj</span> <span class="n">U</span><span class="o">)</span><span class="err">ᵒᵖ</span>
<span class="n">sheaf</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="mi">414</span><span class="o">:</span><span class="mi">66</span><span class="o">:</span> <span class="n">error</span>

<span class="n">synthesized</span> <span class="n">type</span> <span class="n">class</span> <span class="kn">instance</span> <span class="n">is</span> <span class="n">not</span> <span class="n">definitionally</span> <span class="n">equal</span> <span class="n">to</span> <span class="n">expression</span> <span class="n">inferred</span> <span class="k">by</span> <span class="n">typing</span> <span class="n">rules</span><span class="o">,</span> <span class="n">synthesized</span>
  <span class="err">⁇</span>
<span class="n">inferred</span>
  <span class="n">category_theory</span><span class="bp">.</span><span class="n">opposite</span>
<span class="n">sheaf</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="mi">414</span><span class="o">:</span><span class="mi">66</span><span class="o">:</span> <span class="n">error</span>

<span class="n">synthesized</span> <span class="n">type</span> <span class="n">class</span> <span class="kn">instance</span> <span class="n">is</span> <span class="n">not</span> <span class="n">definitionally</span> <span class="n">equal</span> <span class="n">to</span> <span class="n">expression</span> <span class="n">inferred</span> <span class="k">by</span> <span class="n">typing</span> <span class="n">rules</span><span class="o">,</span> <span class="n">synthesized</span>
  <span class="err">𝒞</span>
<span class="n">inferred</span>
  <span class="err">?</span><span class="n">m_1</span>
<span class="n">sheaf</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="mi">414</span><span class="o">:</span><span class="mi">66</span><span class="o">:</span> <span class="n">error</span>

<span class="n">synthesized</span> <span class="n">type</span> <span class="n">class</span> <span class="kn">instance</span> <span class="n">is</span> <span class="n">not</span> <span class="n">definitionally</span> <span class="n">equal</span> <span class="n">to</span> <span class="n">expression</span> <span class="n">inferred</span> <span class="k">by</span> <span class="n">typing</span> <span class="n">rules</span><span class="o">,</span> <span class="n">synthesized</span>
  <span class="err">𝒞</span>
<span class="n">inferred</span>
  <span class="err">?</span><span class="n">m_1</span>
<span class="n">Additional</span> <span class="n">information</span><span class="o">:</span>
<span class="bp">/</span><span class="n">home</span><span class="bp">/</span><span class="n">jmc</span><span class="bp">/</span><span class="n">data</span><span class="bp">/</span><span class="n">math</span><span class="bp">/</span><span class="n">community</span><span class="bp">-</span><span class="n">mathlib</span><span class="bp">/</span><span class="n">category_theory</span><span class="bp">/</span><span class="n">sheaf</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="mi">415</span><span class="o">:</span><span class="mi">20</span><span class="o">:</span> <span class="kn">context</span><span class="o">:</span> <span class="n">switched</span> <span class="n">to</span> <span class="n">simple</span> <span class="n">application</span> <span class="n">elaboration</span> <span class="n">procedure</span> <span class="n">because</span> <span class="n">failed</span> <span class="n">to</span> <span class="n">use</span> <span class="n">expected</span> <span class="n">type</span> <span class="n">to</span> <span class="n">elaborate</span> <span class="n">it</span><span class="o">,</span> <span class="n">error</span> <span class="n">message</span>
  <span class="n">type</span> <span class="n">mismatch</span><span class="o">,</span> <span class="n">term</span>
    <span class="n">limits</span><span class="bp">.</span><span class="n">limit</span><span class="bp">.</span><span class="n">pre</span> <span class="err">?</span><span class="n">m_7</span> <span class="err">?</span><span class="n">m_9</span>
  <span class="n">has</span> <span class="n">type</span>
    <span class="n">limits</span><span class="bp">.</span><span class="n">limit</span> <span class="err">?</span><span class="n">m_5</span> <span class="err">⟶</span> <span class="n">limits</span><span class="bp">.</span><span class="n">limit</span> <span class="o">(</span><span class="err">?</span><span class="n">m_9</span> <span class="err">⋙</span> <span class="err">?</span><span class="n">m_5</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="err">?</span>
  <span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
    <span class="err">⁇</span> <span class="n">U₁</span> <span class="err">⟶</span> <span class="err">⁇</span> <span class="n">U₂</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span>
<span class="n">sheaf</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="mi">414</span><span class="o">:</span><span class="mi">66</span><span class="o">:</span> <span class="n">error</span>

<span class="n">synthesized</span> <span class="n">type</span> <span class="n">class</span> <span class="kn">instance</span> <span class="n">is</span> <span class="n">not</span> <span class="n">definitionally</span> <span class="n">equal</span> <span class="n">to</span> <span class="n">expression</span> <span class="n">inferred</span> <span class="k">by</span> <span class="n">typing</span> <span class="n">rules</span><span class="o">,</span> <span class="n">synthesized</span>
  <span class="err">𝒞</span>
<span class="n">inferred</span>
  <span class="err">?</span><span class="n">m_1</span>
<span class="n">sheaf</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="mi">414</span><span class="o">:</span><span class="mi">66</span><span class="o">:</span> <span class="n">error</span>

<span class="n">synthesized</span> <span class="n">type</span> <span class="n">class</span> <span class="kn">instance</span> <span class="n">is</span> <span class="n">not</span> <span class="n">definitionally</span> <span class="n">equal</span> <span class="n">to</span> <span class="n">expression</span> <span class="n">inferred</span> <span class="k">by</span> <span class="n">typing</span> <span class="n">rules</span><span class="o">,</span> <span class="n">synthesized</span>
  <span class="err">𝒞</span>
<span class="n">inferred</span>
  <span class="err">?</span><span class="n">m_1</span>
<span class="n">sheaf</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="mi">414</span><span class="o">:</span><span class="mi">66</span><span class="o">:</span> <span class="n">error</span>

<span class="n">synthesized</span> <span class="n">type</span> <span class="n">class</span> <span class="kn">instance</span> <span class="n">is</span> <span class="n">not</span> <span class="n">definitionally</span> <span class="n">equal</span> <span class="n">to</span> <span class="n">expression</span> <span class="n">inferred</span> <span class="k">by</span> <span class="n">typing</span> <span class="n">rules</span><span class="o">,</span> <span class="n">synthesized</span>
  <span class="err">𝒞</span>
<span class="n">inferred</span>
  <span class="err">?</span><span class="n">m_1</span>
</pre></div>

#### [ Reid Barton (Nov 14 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697169):
<p><code>instance [preorder α] : small_category α := ...</code> got the name <code>category_theory.small_category</code></p>

#### [ Johan Commelin (Nov 14 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697217):
<p>Aaah, that's not so nice. That should be in the <code>preorder</code> namespace.</p>

#### [ Kenny Lau (Nov 14 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697224):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> talk about <code>is_ring_hom.is_ring_hom</code></p>

#### [ Mario Carneiro (Nov 14 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697277):
<p>what is that even?</p>

#### [ Kenny Lau (Nov 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697318):
<p><a href="https://github.com/leanprover/mathlib/blob/master/ring_theory/subring.lean#L28" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/ring_theory/subring.lean#L28">https://github.com/leanprover/mathlib/blob/master/ring_theory/subring.lean#L28</a></p>

#### [ Kenny Lau (Nov 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697322):
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">is_ring_hom</span>

<span class="kn">instance</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">R</span><span class="o">}</span> <span class="o">[</span><span class="n">is_subring</span> <span class="n">S</span><span class="o">]</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="o">(</span><span class="bp">@</span><span class="n">subtype</span><span class="bp">.</span><span class="n">val</span> <span class="n">R</span> <span class="n">S</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">refine</span> <span class="o">{</span><span class="bp">..</span><span class="o">}</span> <span class="bp">;</span> <span class="n">intros</span> <span class="bp">;</span> <span class="n">refl</span>

<span class="kn">end</span> <span class="n">is_ring_hom</span>
</pre></div>

#### [ Kenny Lau (Nov 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697323):
<p>guess how this would be called</p>

#### [ Kenny Lau (Nov 14 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697386):
<p>also what on earth is it with the <code>local attribute [instance] classical.prop_decidable</code></p>

#### [ Reid Barton (Nov 14 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697389):
<p>There's also some bug where Lean's normal naming strategy for an instance is not used under certain circumstances (I'm not sure exactly which)</p>

#### [ Mario Carneiro (Nov 14 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697402):
<p><code>classical.prop_decidable</code> existed long before <code>classical.dec</code>, I think it's in the style guide and TPIL</p>

#### [ Kenny Lau (Nov 14 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697419):
<p>I mean, who on earth put it there</p>

#### [ Kenny Lau (Nov 14 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697433):
<p>you don't need any classical stuff for subrings</p>

#### [ Reid Barton (Nov 14 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697448):
<p>We could have a strategy where we don't write instances like <code>instance [preorder α] : small_category α</code>, but rather <code>instance [preorder α] : small_category (preorder α)</code>, where <code>def preorder α := α</code></p>

#### [ Mario Carneiro (Nov 14 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697501):
<p>maybe it was needed once, or a mathematician wrote the file</p>

#### [ Mario Carneiro (Nov 14 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697510):
<div class="codehilite"><pre><span></span>Authors: Johan Commelin
</pre></div>

#### [ Kenny Lau (Nov 14 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697534):
<p>but curiously he was never part of the file's history</p>

#### [ Reid Barton (Nov 14 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697546):
<p>That would cut out all the silly search starting <code>preorder punit</code> (actually it is not really silly, since <code>punit</code> could very well be a <code>preorder</code>, but anyways we want a different instance)</p>

#### [ Mario Carneiro (Nov 14 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697571):
<p>I think we need to think about a more principled approach to instance priorities</p>

#### [ Mario Carneiro (Nov 14 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697726):
<p>for preorder categories, I guess it depends on whether you view it as "a preorder is a special kind of category" or "any preorder can be equipped with a canonical category structure"</p>

#### [ Kenny Lau (Nov 14 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697751):
<p>I think we need to refactor the typeclass search system</p>

#### [ Kenny Lau (Nov 14 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697754):
<p>but I don't know how any of those things work</p>

#### [ Kenny Lau (Nov 14 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697761):
<p>so I might have said nothing in the first place</p>

#### [ Reid Barton (Nov 14 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697770):
<p>Well I'm not necessarily thinking about anything as anything, I just want to avoid these 20 pages of failed instance searches whenever I try to look for a category instance which is after the preorder one.</p>

#### [ Mario Carneiro (Nov 14 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697771):
<p><span class="emoji emoji-1f340" title="four leaf clover">:four_leaf_clover:</span></p>

#### [ Kenny Lau (Nov 14 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697786):
<p>I think the instance search is as stupid as <code>simp</code></p>

#### [ Mario Carneiro (Nov 14 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697792):
<p>it's much worse than <code>simp</code></p>

#### [ Kenny Lau (Nov 14 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697793):
<p>and we still haven't fixed the problem with <code>simp</code></p>

#### [ Kenny Lau (Nov 14 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697796):
<p>for the love of god</p>

#### [ Kenny Lau (Nov 14 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697859):
<p>who thought depth first search is a good idea (instance) and who thought breadth first search is a good idea (simp)</p>

#### [ Kenny Lau (Nov 14 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697865):
<p>but I don't study CS</p>

#### [ Mario Carneiro (Nov 14 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697892):
<p>But it's not a tactic, it's built into lean, so there is very little customization or alternatives we can try in lean 3</p>

#### [ Mario Carneiro (Nov 14 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697903):
<p>at least not without forking lean</p>

#### [ Reid Barton (Nov 14 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697923):
<p>OK here is a thought. What if we by convention give each instance which doesn't match against the head a lower priority</p>

#### [ Reid Barton (Nov 14 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147697982):
<p>i.e. each instance of the form \Pi a, ... : C a</p>

#### [ Reid Barton (Nov 14 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698031):
<p>Because of course we want to match against things like ... : C (T a) first, if we're trying to find an instance C (T ...)</p>

#### [ Kenny Lau (Nov 14 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698041):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> but from your CS experience, what is the best search method?</p>

#### [ Mario Carneiro (Nov 14 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698061):
<p>There are two essentially different kinds of instances: "parent coercions" that change the head, and things that change the type to something smaller and leave the head alone</p>

#### [ Mario Carneiro (Nov 14 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698151):
<p>we know the search terminates in the second case because it's well founded on the structure construction, and in the first case because our tree of classes is finite</p>

#### [ Johan Commelin (Nov 14 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698155):
<div class="codehilite"><pre><span></span>git grep &quot;^instance&quot; | wc -l
1515
</pre></div>

#### [ Mario Carneiro (Nov 14 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698156):
<p>that last one is obviously problematic</p>

#### [ Mario Carneiro (Nov 14 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698176):
<p>because it gets worse as you add more things anywhere in mathlib</p>

#### [ Kenny Lau (Nov 14 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698179):
<p>I think TREE(3) is also finite so I don't really get your point</p>

#### [ Kenny Lau (Nov 14 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698220):
<p>are we satisfied with "it will eventually terminate"?</p>

#### [ Mario Carneiro (Nov 14 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698273):
<p>it's an important first step</p>

#### [ Mario Carneiro (Nov 14 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698287):
<p>the next question is "how finite" of course</p>

#### [ Mario Carneiro (Nov 14 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698316):
<p>and this depends on how much typeclass caching lean does</p>

#### [ Mario Carneiro (Nov 14 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698326):
<p>so I'm not sure on the details</p>

#### [ Mario Carneiro (Nov 14 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698353):
<p>We want it to be mostly linear</p>

#### [ Johan Commelin (Nov 14 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698380):
<p>How about prioritizing type 1? Like Reid suggested?</p>

#### [ Mario Carneiro (Nov 14 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698457):
<p>Parent coercions have a fixed priority, I don't think we can change it</p>

#### [ Mario Carneiro (Nov 14 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698471):
<p>This is one place where I think lean is using the wrong search strategy btw</p>

#### [ Reid Barton (Nov 14 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698489):
<p>Oh I forgot about parent coercions.</p>

#### [ Kenny Lau (Nov 14 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698509):
<p>we don't we ask the big guys about the typeclass system  in lean 4?</p>

#### [ Mario Carneiro (Nov 14 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698568):
<p>If we call type coercions type 1 and parent / "head changing" coercions type 2, then I think we should use backward chaining for type 1 and forward chaining for type 2</p>

#### [ Mario Carneiro (Nov 14 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698636):
<p>For example, if you prove that <code>ordered_field real</code> then lean will pre-calculate proofs of <code>preorder real</code> and a bunch of other stuff</p>

#### [ Reid Barton (Nov 14 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698639):
<p>Are we talking about actual parent coercions like from <code>group</code> to <code>monoid</code>?</p>

#### [ Mario Carneiro (Nov 14 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698640):
<p>yes</p>

#### [ Reid Barton (Nov 14 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698651):
<p>So then there are also things like <code>preorder</code> to <code>category</code></p>

#### [ Mario Carneiro (Nov 14 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698657):
<p>yes</p>

#### [ Reid Barton (Nov 14 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698711):
<p>And I guess both of those fall under type 2</p>

#### [ Mario Carneiro (Nov 14 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698721):
<p>and if you have <code>ordered_field A</code> in the context then it calculates <code>preorder A</code> when solving typeclass problems</p>

#### [ Kenny Lau (Nov 14 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698730):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> how does this work in metamath?</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698822):
<p>You get to do this stuff yourself, but there is a smallish spine so it's at most two or three theorem applications to get from anything to anything else</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698838):
<p>the backward chaining stuff might be done automatically in later versions?</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698844):
<p>It's all third party stuff though</p>

#### [ Johan Commelin (Nov 14 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698856):
<p>So is there any hope we can improve the system in Lean 3?</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698861):
<p>this is emphatically not part of "metamath core"</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698889):
<p>priorities seem like the best option, but we need a good rule</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147698960):
<p>I have hope for reid's proposal</p>

#### [ Reid Barton (Nov 14 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699006):
<p>The obvious, but more annoying variant is to raise the priority of every "type 1" instance</p>

#### [ Johan Commelin (Nov 14 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699081):
<p>I think Mario said that those were fixed... but maybe I misunderstood which type he referred to...</p>

#### [ Reid Barton (Nov 14 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699099):
<p>I'm also a little confused about Mario's description of the two types</p>

#### [ Reid Barton (Nov 14 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699106):
<p>In Haskell, if we have an instance C (T a b), we call T the instance head</p>

#### [ Reid Barton (Nov 14 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699112):
<p>C is the class</p>

#### [ Reid Barton (Nov 14 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699143):
<p>I'm not sure whether Mario is using the same terminology, or switched the classes or what</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699181):
<p>I called <code>C</code> the head there</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699257):
<p>so parent coercions change the head, i.e. C a =&gt; D a</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699274):
<p>and type coercions are like C a , C b =&gt; C (T a b)</p>

#### [ Reid Barton (Nov 14 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699409):
<p>I might be wrong in assuming instances like C a, C b =&gt; C (T a b) are more common in mathlib--in standard Haskell they're the only kind of instances you are allowed to write</p>

#### [ Reid Barton (Nov 14 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699421):
<p>(instance C a =&gt; D a is illegal)</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699422):
<p>That's not true, I think you can do parent coercions in Haskell too</p>

#### [ Reid Barton (Nov 14 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699436):
<p>With GHC extensions</p>

#### [ Reid Barton (Nov 14 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699460):
<p>But the effect is probably like 99% of all instances are of the C (T a b) form</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699675):
<p>oh, I see, there are parent coercions but no user defined parent coercions</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699698):
<div class="codehilite"><pre><span></span>class Test a where
  test :: a -&gt; a
class Test a =&gt; Test2 a where
  test2 :: a -&gt; a
</pre></div>

#### [ Mario Carneiro (Nov 14 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699702):
<p>this is okay</p>

#### [ Reid Barton (Nov 14 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699713):
<p>There isn't even a coercion in the same sense as in Lean</p>

#### [ Reid Barton (Nov 14 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699716):
<p>There, to write a <code>Test2</code> instance, you must first write a <code>Test</code> instance</p>

#### [ Reid Barton (Nov 14 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699746):
<p>The purpose of <code>Test a =&gt; Test2 a</code> is instead to avoid writing contexts like <code>(Test a, Test2 a) =&gt; t</code></p>

#### [ Mario Carneiro (Nov 14 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699751):
<p>that's the same as in lean</p>

#### [ Reid Barton (Nov 14 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699839):
<p>Oh, well... I guess Lean hides the need to write the <code>Test</code> instance separately</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699854):
<div class="codehilite"><pre><span></span>class Test (a : Type) := (test : a → a)
class Test2 (a : Type) extends Test a := (test2 : a → a)

instance : Test nat := {test := id}
instance : Test2 nat := {test2 := id} --requires the first instance
</pre></div>

#### [ Reid Barton (Nov 14 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699882):
<p>But you can also write <code>instance : Test2 nat := {test := id, test2 := id}</code> without the first instance, which has no equivalent in Haskell</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699933):
<p>Maybe lean should do that too</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699943):
<p>that is essentially requiring the user to do the forward chaining thing I said</p>

#### [ Reid Barton (Nov 14 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699966):
<p>I actually don't know off-hand how GHC solves a <code>Test a</code> constraint if you only have <code>Test2</code> in the context</p>

#### [ Reid Barton (Nov 14 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147699996):
<p>I wouldn't be surprised if it does forward chaining in that situation</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147700076):
<p>you mean when you have <code>test :: Test2 a =&gt; a -&gt; a</code>?</p>

#### [ Reid Barton (Nov 14 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147700092):
<p>Basically, yeah.</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147700424):
<p>I think it is complete in Haskell's case to always saturate downwards (derive all superclasses of all the things in the context) and then backward chain from uses (without using any parent coercions)</p>

#### [ Johan Commelin (Nov 15 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147731225):
<p>Aahrg, Lean is just becoming completely unresponsive when I try to fill in the instances by hand.</p>

#### [ Johan Commelin (Nov 15 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147731254):
<p>Look at the code that I have now: this is getting pretty crazy...</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">extend</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="n">X</span> <span class="n">C</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">obj</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span><span class="o">,</span> <span class="bp">@</span><span class="n">limit</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="bp">_</span> <span class="o">(</span><span class="bp">@</span><span class="n">category_theory</span><span class="bp">.</span><span class="n">opposite</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span> <span class="n">v</span><span class="o">}</span> <span class="bp">_</span>
<span class="o">(</span><span class="bp">@</span><span class="n">category_theory</span><span class="bp">.</span><span class="n">comma_category</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span> <span class="n">v</span> <span class="n">v</span> <span class="n">v</span> <span class="n">v</span> <span class="n">v</span><span class="o">}</span>
  <span class="bp">_</span> <span class="o">(</span><span class="n">category_theory</span><span class="bp">.</span><span class="n">full_subcategory</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span> <span class="n">v</span><span class="o">}</span> <span class="bp">_</span><span class="o">)</span>
  <span class="bp">_</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">punit_category</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span><span class="o">}</span>
  <span class="bp">_</span> <span class="o">(</span><span class="bp">@</span><span class="n">site</span><span class="bp">.</span><span class="n">to_category</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span><span class="o">}</span> <span class="o">(</span><span class="bp">@</span><span class="n">opens</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span><span class="o">}</span> <span class="n">X</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">)</span> <span class="o">(</span><span class="bp">@</span><span class="n">category_theory</span><span class="bp">.</span><span class="n">site</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span><span class="o">}</span> <span class="n">X</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">))</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">))</span>
  <span class="bp">_</span> <span class="bp">_</span>
<span class="o">((</span><span class="n">comma</span><span class="bp">.</span><span class="n">fst</span> <span class="o">(</span><span class="n">full_subcategory_inclusion</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">of_obj</span> <span class="n">U</span><span class="o">))</span><span class="bp">.</span><span class="n">op</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">)</span>
<span class="o">(</span><span class="n">limits</span><span class="bp">.</span><span class="n">has_limit_of_has_limits_of_shape</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">map</span> <span class="o">:=</span> <span class="bp">_</span> <span class="o">}</span>
</pre></div>

#### [ Kenny Lau (Nov 15 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147731470):
<p>welcome to the club :P</p>

#### [ Johan Commelin (Nov 15 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147731810):
<p>Ok, I need to confess. I'm making a big fool out of myself. There was actually a missing assumption... so no wonder Lean couldn't find the instance. The code is now back to</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">extend</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="n">X</span> <span class="n">C</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">obj</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span><span class="o">,</span> <span class="n">limit</span> <span class="o">((</span><span class="n">comma</span><span class="bp">.</span><span class="n">fst</span> <span class="o">(</span><span class="n">full_subcategory_inclusion</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">of_obj</span> <span class="n">U</span><span class="o">))</span><span class="bp">.</span><span class="n">op</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">),</span>
  <span class="n">map</span> <span class="o">:=</span> <span class="bp">_</span> <span class="o">}</span>
</pre></div>


<p><strong>However</strong> it is still taking &gt;10s to typecheck this stuff. Before I removed all the explicit instances, it also took &gt;10s.</p>

#### [ Leonardo de Moura (Nov 16 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147797050):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> </p>
<blockquote>
<p>Johan Commelin: So is there any hope we can improve the system in Lean 3?</p>
</blockquote>
<p>To improve Lean 3, you need to fork it, and improve it yourself. The development is frozen in the main repo, and all efforts are focused on Lean 4. That being said, nobody should expect Lean 4 will solve all problems and everybody will be happy.</p>

#### [ Leonardo de Moura (Nov 16 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147797116):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> </p>
<blockquote>
<p>Kenny Lau: we don't we ask the big guys about the typeclass system in lean 4?</p>
</blockquote>
<p>We didn't get there yet. We have only random ideas on how to improve the typeclass system in lean 4.</p>

#### [ Leonardo de Moura (Nov 16 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147797179):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> </p>
<blockquote>
<p>Kenny Lau: I think we need to refactor the typeclass search system</p>
</blockquote>
<p>If you want a better typeclass system in the next few months, you should fork the current system, and refactor the typeclass search system yourself.</p>

#### [ Johan Commelin (Nov 16 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147797342):
<p><span class="user-mention" data-user-id="112857">@Leonardo de Moura</span> Ok, I was hoping that maybe we could use priorities to guide the type class system. Anyway, thanks for the input! And thanks for all you're doing for Lean (3 and 4).</p>

#### [ Leonardo de Moura (Nov 16 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147797450):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> Yes, priorities will help. Shortcuts will help too. Example: <a href="https://github.com/leanprover/lean/blob/master/library/init/data/int/basic.lean#L418-L429" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/init/data/int/basic.lean#L418-L429">https://github.com/leanprover/lean/blob/master/library/init/data/int/basic.lean#L418-L429</a></p>

#### [ Leonardo de Moura (Nov 16 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147797467):
<p>These are just workarounds.</p>

#### [ Mario Carneiro (Nov 16 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147800392):
<p>It's not clear to me how much shortcuts actually help, though, because they make the typeclass graph even larger</p>

#### [ Mario Carneiro (Nov 16 2018 at 08:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147800445):
<p>if you have instances from A -&gt; B -&gt; C and add a shortcut A -&gt; C, then a typeclass search for some unrelated F will traverse both paths to C (and possibly the entire subtree rooted at C)</p>

#### [ Mario Carneiro (Nov 16 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147800469):
<p>Are there any plans for lean 4 to do anything with the typeclass system?</p>

#### [ Leonardo de Moura (Nov 16 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147800852):
<p>You can add the shortcuts using local attributes. In this way, you can add shortcuts to a file without affecting other files.</p>

#### [ Leonardo de Moura (Nov 16 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20issues/near/147800886):
<p>Sebastian and I discussed a few improvements (e.g., better indexing and caching), but as I said above these are just ideas on the whiteboard. We didn’t get there yet.</p>


{% endraw %}
