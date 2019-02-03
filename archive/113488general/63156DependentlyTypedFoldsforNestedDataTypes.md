---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/63156DependentlyTypedFoldsforNestedDataTypes.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Dependently Typed Folds for Nested Data Types](https://leanprover-community.github.io/archive/113488general/63156DependentlyTypedFoldsforNestedDataTypes.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sean Leather (Jul 05 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129137513):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> <a href="#narrow/stream/113488-general/subject/cases/near/126323093" title="#narrow/stream/113488-general/subject/cases/near/126323093">wrote</a>:</p>
<blockquote>
<p>With nested and mutual inductives moving into the kernel, there shouldn't be any need for an abstraction layer. Well, it's still not clear how nested inductives would be represented.</p>
</blockquote>
<p>Would this paper help?</p>
<p><a href="https://arxiv.org/abs/1806.05230" target="_blank" title="https://arxiv.org/abs/1806.05230">Dependently Typed Folds for Nested Data Types</a>:</p>
<blockquote>
<p>We present an approach to develop folds for nested data types using dependent types. We call such folds dependently typed folds, they have the following properties. (1) Dependently typed folds are defined by well-founded recursion and they can be defined in a total dependently typed language. (2) Dependently typed folds do not depend on maps, map functions and many terminating functions can be defined using dependently typed folds. (3) The induction principles for nested data types follow from the definitions of dependently typed folds and the programs defined by dependently typed folds can be formally verified. (4) Dependently typed folds exist for any nested data types and they can be specialized to the traditional higher-order folds. Using various of examples, we show how to program and reason about dependently typed folds. We also show how to obtain dependently typed folds in general and how to specialize them to the corresponding higher-order folds.</p>
</blockquote>

#### [ Sebastian Ullrich (Jul 05 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129145511):
<p><span class="user-mention" data-user-id="110045">@Sean Leather</span> This seems to be about a different kind of nested types. Note that <code>Bush</code> cannot even be defined in Lean 3 because of universe constraints.</p>

#### [ Sean Leather (Jul 05 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129145627):
<p>What are the nested inductives that you're referring to?</p>

#### [ Sebastian Ullrich (Jul 05 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129145672):
<p>And conversely, the type <code>Term</code> from the first case study is just a regular inductive type according to Lean. I didn't compare the induction principles, though.</p>

#### [ Sebastian Ullrich (Jul 05 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129145876):
<p><span class="user-mention" data-user-id="110045">@Sean Leather</span>  Any inductive type that is passed to another inductive type in its own definition, as in <a href="https://github.com/leanprover/lean/wiki/Inductive-datatypes#encoding-datatypes-that-contain-recursive-occurrences-nested-in-existing-datatypes" target="_blank" title="https://github.com/leanprover/lean/wiki/Inductive-datatypes#encoding-datatypes-that-contain-recursive-occurrences-nested-in-existing-datatypes">https://github.com/leanprover/lean/wiki/Inductive-datatypes#encoding-datatypes-that-contain-recursive-occurrences-nested-in-existing-datatypes</a></p>

#### [ Sean Leather (Jul 05 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129146139):
<p>Ok, right. That's the "simple" version of nested data types.</p>

#### [ Mario Carneiro (Jul 06 2018 at 03:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129175542):
<blockquote>
<p>Note that Bush cannot even be defined in Lean 3 because of universe constraints.</p>
</blockquote>
<p>Actually this is an instance of non-uniform parameters, which I have figured out how to simulate in lean without any kernel extensions</p>

#### [ Sean Leather (Jul 06 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129183673):
<blockquote>
<p>Actually this is an instance of non-uniform parameters, which I have figured out how to simulate in lean without any kernel extensions</p>
</blockquote>
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Please do share. Can you define a <code>Bush</code> type from constants?</p>

#### [ Mario Carneiro (Jul 06 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129183675):
<p>what do you mean from constants?</p>

#### [ Sean Leather (Jul 06 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129183799):
<p>I mean the sort of constants generated by the equation compiler.</p>

#### [ Sean Leather (Jul 06 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129183844):
<p>Err, maybe I'm using the wrong terminology. What do you call the process of taking an <code>inductive</code> to its constants?</p>

#### [ Mario Carneiro (Jul 06 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129184389):
<p>the constructors?</p>

#### [ Mario Carneiro (Jul 06 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129184456):
<p>To be precise, I can define a type <code>Bush</code> together with constructors of the stated types, the natural recursion principle, and a computation rule (as a provable equality, not definitional) while circumventing any universe inconsistencies</p>

#### [ Sean Leather (Jul 06 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129184572):
<blockquote>
<p>To be precise, I can define a type <code>Bush</code> together with constructors of the stated types, the natural recursion principle, and a computation rule (as a provable equality, not definitional) while circumventing any universe inconsistencies</p>
</blockquote>
<p>Yes, that's what I'd like to see.</p>

#### [ Mario Carneiro (Jul 06 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129189453):
<p>I think I will just give a rough sketch:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="n">bushn</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span>
<span class="bp">|</span> <span class="n">zero</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">bushn</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="n">nil</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">:</span> <span class="n">bushn</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">cons</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">:</span> <span class="n">bushn</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">bushn</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">2</span><span class="o">)</span> <span class="bp">→</span> <span class="n">bushn</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span>

<span class="n">def</span> <span class="n">bush</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">:=</span> <span class="n">bushn</span> <span class="n">α</span> <span class="mi">1</span>

<span class="n">def</span> <span class="n">bushn</span><span class="bp">.</span><span class="n">equiv</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">bushn</span> <span class="n">α</span> <span class="n">n</span> <span class="err">≃</span> <span class="o">(</span><span class="n">bush</span><span class="err">^</span><span class="o">[</span><span class="n">n</span><span class="o">]</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="n">def</span> <span class="n">bush</span><span class="bp">.</span><span class="n">nil</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">:</span> <span class="n">bush</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">bushn</span><span class="bp">.</span><span class="n">nil</span> <span class="n">α</span>
<span class="n">def</span> <span class="n">bush</span><span class="bp">.</span><span class="n">cons</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">bush</span> <span class="o">(</span><span class="n">bush</span> <span class="n">α</span><span class="o">))</span> <span class="o">:</span> <span class="n">bush</span> <span class="n">α</span> <span class="o">:=</span>
<span class="n">bushn</span><span class="bp">.</span><span class="n">cons</span> <span class="o">(</span><span class="n">bushn</span><span class="bp">.</span><span class="n">zero</span> <span class="n">a</span><span class="o">)</span> <span class="o">((</span><span class="n">bushn</span><span class="bp">.</span><span class="n">equiv</span> <span class="n">α</span> <span class="mi">2</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span> <span class="n">b</span><span class="o">)</span>

<span class="n">def</span> <span class="o">{</span><span class="n">u</span> <span class="n">l</span><span class="o">}</span> <span class="n">bush</span><span class="bp">.</span><span class="n">rec</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">},</span> <span class="n">bush</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span> <span class="n">l</span><span class="o">}</span>
  <span class="o">(</span><span class="n">C0</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">α</span><span class="o">,</span> <span class="n">C</span> <span class="o">(</span><span class="n">bush</span><span class="bp">.</span><span class="n">nil</span> <span class="n">α</span><span class="o">))</span>
  <span class="o">(</span><span class="n">C1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">α</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">C</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">C</span> <span class="o">(</span><span class="bp">@</span><span class="n">bush</span><span class="bp">.</span><span class="n">cons</span> <span class="n">α</span> <span class="n">a</span> <span class="n">b</span><span class="o">))</span>
  <span class="o">(</span><span class="n">α</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="bp">@</span><span class="n">C</span> <span class="n">α</span> <span class="n">b</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="n">def</span> <span class="n">bush</span><span class="bp">.</span><span class="n">rec_nil</span> <span class="o">{</span><span class="n">C</span><span class="o">}</span> <span class="o">(</span><span class="n">C0</span> <span class="n">C1</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="bp">@</span><span class="n">bush</span><span class="bp">.</span><span class="n">rec</span> <span class="bp">@</span><span class="n">C</span> <span class="n">C0</span> <span class="n">C1</span> <span class="n">α</span> <span class="o">(</span><span class="n">bush</span><span class="bp">.</span><span class="n">nil</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="n">C0</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="n">def</span> <span class="n">bush</span><span class="bp">.</span><span class="n">rec_cons</span> <span class="o">{</span><span class="n">C</span><span class="o">}</span> <span class="o">(</span><span class="n">C0</span> <span class="n">C1</span> <span class="n">α</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span>
  <span class="bp">@</span><span class="n">bush</span><span class="bp">.</span><span class="n">rec</span> <span class="bp">@</span><span class="n">C</span> <span class="n">C0</span> <span class="n">C1</span> <span class="n">α</span> <span class="o">(</span><span class="n">bush</span><span class="bp">.</span><span class="n">cons</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="bp">=</span>
  <span class="n">C1</span> <span class="n">α</span> <span class="n">a</span> <span class="n">b</span> <span class="o">(</span><span class="bp">@</span><span class="n">bush</span><span class="bp">.</span><span class="n">rec</span> <span class="bp">@</span><span class="n">C</span> <span class="n">C0</span> <span class="n">C1</span> <span class="o">(</span><span class="n">bush</span> <span class="n">α</span><span class="o">)</span> <span class="n">b</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Sean Leather (Jul 06 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129190374):
<p>At a glance, that looks similar to what's in the article I linked.</p>

#### [ Mario Carneiro (Jul 06 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129190460):
<p>Is it? I thought they assume that <code>bush</code> makes sense as an inductive without further justification, since Agda accepts it</p>

#### [ Sean Leather (Jul 06 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129190525):
<p>Copy-paste:</p>
<div class="codehilite"><pre><span></span><span class="kr">data</span> BushN <span class="ow">:</span> Nat <span class="ow">-&gt;</span> <span class="kt">Set</span> <span class="ow">-&gt;</span> <span class="kt">Set</span> <span class="kr">where</span>
  <span class="nf">Base</span> <span class="ow">:</span> <span class="o">{</span>a <span class="ow">:</span> <span class="kt">Set</span><span class="o">}</span> <span class="ow">-&gt;</span> a <span class="ow">-&gt;</span> BushN Z a
  <span class="nf">NilBN</span> <span class="ow">:</span> <span class="o">{</span>a <span class="ow">:</span> <span class="kt">Set</span><span class="o">}</span> <span class="ow">-&gt;</span> <span class="o">{</span>n <span class="ow">:</span> Nat<span class="o">}</span> <span class="ow">-&gt;</span> BushN <span class="o">(</span>S n<span class="o">)</span> a
  <span class="nf">ConsBN</span> <span class="ow">:</span> <span class="o">{</span>a <span class="ow">:</span> <span class="kt">Set</span><span class="o">}</span> <span class="ow">-&gt;</span> <span class="o">{</span>n <span class="ow">:</span> Nat<span class="o">}</span> <span class="ow">-&gt;</span> BushN n a <span class="ow">-&gt;</span> BushN <span class="o">(</span>S <span class="o">(</span>S n<span class="o">))</span> a <span class="ow">-&gt;</span> BushN <span class="o">(</span>S n<span class="o">)</span> a
</pre></div>

#### [ Mario Carneiro (Jul 06 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129190559):
<p>Oh, I missed that</p>


{% endraw %}
