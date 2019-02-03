---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/14638Basicquestions.html
---

## Stream: [general](index.html)
### Topic: [Basic questions](14638Basicquestions.html)

---


{% raw %}
#### [ Charles Rezk (Oct 18 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010459):
<p>How would I go about proving things about functions between sets, especially finite sets?  I see some machinery for sets (really, "subsets" of a given type), but nothing about functions between them.  On the other hand, I can certainly have functions between types, but I don't see a convenient way to produce a particular "finite type".</p>

#### [ Mario Carneiro (Oct 18 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010589):
<p>what do you want to do with them exactly?</p>

#### [ Mario Carneiro (Oct 18 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010606):
<p>for the most part you can just write functions between types</p>

#### [ Mario Carneiro (Oct 18 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010607):
<p>which happen to be finite</p>

#### [ Charles Rezk (Oct 18 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010704):
<p>Let's say I want to construct a particular finite type, e.g., of size n.  How do I do it?</p>

#### [ Charles Rezk (Oct 18 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010713):
<p>And how do I prove things about it?</p>

#### [ Mario Carneiro (Oct 18 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010720):
<p><code>fin n</code> is a type of size n</p>

#### [ Mario Carneiro (Oct 18 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010771):
<p>and functions out of <code>fin n</code> have various properties not shared by general types, for example <code>list.of_fn</code> turns a function out of <code>fin n</code> into a list of values</p>

#### [ Charles Rezk (Oct 18 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010780):
<p>Where is the code for fin?</p>

#### [ Mario Carneiro (Oct 18 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010858):
<p><code>init/data/fin</code> I think</p>

#### [ Mario Carneiro (Oct 18 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010862):
<p>it's imported by default</p>

#### [ Charles Rezk (Oct 18 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010937):
<p>I don't see "list" in there.</p>

#### [ Mario Carneiro (Oct 18 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136010957):
<p>that definition is in <code>data.list.basic</code></p>

#### [ Charles Rezk (Oct 18 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136011168):
<p>How would I go about constructing a function out of a S:fin n ?</p>

#### [ Mario Carneiro (Oct 18 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136011570):
<p>You can just define the function as a lambda...</p>

#### [ Mario Carneiro (Oct 18 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136011581):
<p>or you can use <code>fin.cases</code></p>

#### [ Charles Rezk (Oct 18 2018 at 02:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136011725):
<p>Not sure how to construct anything other than identity function that way.  Because I don't know what the "elements" of fin n are called.</p>

#### [ Mario Carneiro (Oct 18 2018 at 02:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136011734):
<p><code>0</code>, <code>1</code>, <code>2</code>, ...</p>

#### [ Charles Rezk (Oct 18 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136011786):
<p>Where in the code for fin does it say that I can do that?</p>

#### [ Mario Carneiro (Oct 18 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136011836):
<p><code>has_one</code> and <code>has_add</code> give you that for free</p>

#### [ Mario Carneiro (Oct 18 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136011845):
<p><code>init.fin.ops</code> I think</p>

#### [ Charles Rezk (Oct 18 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136011997):
<p>Nothing about looking at the code would suggest why that's the case</p>

#### [ Mario Carneiro (Oct 18 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012053):
<p>The code that actually causes <code>2</code> to be parsed as <code>bit0 1</code> is in the parser (C++ code), and <code>bit0</code> is defined in <code>init.core</code></p>

#### [ Charles Rezk (Oct 18 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012063):
<p>okay</p>

#### [ Charles Rezk (Oct 18 2018 at 02:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012088):
<p>I'd rather read the documentation than look at the code, but there doesn't seem to be any.</p>

#### [ Mario Carneiro (Oct 18 2018 at 02:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012104):
<p>Every type that has a 0 and 1 and addition has all numerals</p>

#### [ Charles Rezk (Oct 18 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012310):
<p>So I can treat elements of a fin n as natural numbers, e.g., add them and such?</p>

#### [ Mario Carneiro (Oct 18 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012314):
<p>yes</p>

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012316):
<p>Here's the definition of <code>fin</code> in <code>init/data/fin/basic.lean</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">val</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">(</span><span class="n">is_lt</span> <span class="o">:</span> <span class="n">val</span> <span class="bp">&lt;</span> <span class="n">n</span><span class="o">)</span>
</pre></div>


<p>This says that <code>fin</code> takes as input <code>n</code>, which should be a <code>nat</code> (natural number). <code>fin n</code> is then a structure (a certain simple kind of inductive type) which contains a field called <code>val</code> (which takes values in <code>nat</code>) and a field called <code>is_lt</code> (which is a proof that <code>val &lt; n</code>). So I would say that <code>(val : nat)</code> tells you that the elements of <code>fin n</code> can be written as natural numbers.</p>

#### [ Charles Rezk (Oct 18 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012324):
<p>I see.</p>

#### [ Mario Carneiro (Oct 18 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012374):
<p>when you write <code>10 : fin 3</code> you actually get <code>1 = 10 % 3</code></p>

#### [ Charles Rezk (Oct 18 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012414):
<p>Suppose I have an a:nat and an h:a&lt;10.  How do I construct an element of fin 10 from that?</p>

#### [ Mario Carneiro (Oct 18 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012503):
<p><code>\langle a, h\rangle</code></p>

#### [ Charles Rezk (Oct 18 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012514):
<p>Nothing more readable than than?</p>

#### [ Charles Rezk (Oct 18 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012516):
<p>than that?</p>

#### [ Mario Carneiro (Oct 18 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012543):
<p>There are several ways to write constructors for structures</p>

#### [ Jeremy Avigad (Oct 18 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012546):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> This is how I would do it:</p>
<div class="codehilite"><pre><span></span>def foo : fin 3 → nat
| ⟨0, _⟩   := 7
| ⟨1, _⟩   := 5
| ⟨2, _⟩   := 6
| ⟨n+3, h⟩ := absurd h (by simp)
</pre></div>


<p>Is there a better way?</p>

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012547):
<p>In VS code when you start typing <code>\langle</code>, you can hit tab and it will autocomplete into the left angle bracket unicode symbol <code>⟨</code></p>

#### [ Charles Rezk (Oct 18 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012595):
<p>What is "by simp" doing there?</p>

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012604):
<p>And you can always put in an explicit type ascription if you're worried that the ⟨⟩ syntax is too obscure.</p>

#### [ Charles Rezk (Oct 18 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012620):
<p>Assume I know nothing.  What is an explicit type ascription?</p>

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012632):
<p>e.g. <code>let f := (⟨a : nat ,h : a &lt; 10⟩ : fin 10)</code></p>

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012704):
<p>A type ascription is this colon syntax; basically the stuff to the right of the colon is the type of the stuff to the left.</p>

#### [ Mario Carneiro (Oct 18 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012719):
<p><span class="user-mention" data-user-id="110865">@Jeremy Avigad</span> That's the nicest way to define functions out of <code>fin n</code> currently (and you can use <code>dec_trivial</code> in place of <code>by simp</code>), although if you want to prove properties about it <code>fin.cases</code> gives a slightly better reasoning</p>

#### [ Mario Carneiro (Oct 18 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012766):
<p>I've been wondering whether we should have an explicit <code>fin2 n</code> type defined as an inductive type so that you get a nice recursion principle</p>

#### [ Mario Carneiro (Oct 18 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012772):
<p>(This type actually exists in <code>dioph.lean</code> but is unused elsewhere)</p>

#### [ Charles Rezk (Oct 18 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012859):
<p><span class="user-mention" data-user-id="110865">@Jeremy Avigad</span> When I put in that code, it says "simplify tactic failed to simplify"</p>

#### [ Charles Rezk (Oct 18 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012903):
<p><span class="user-mention" data-user-id="110865">@Jeremy Avigad</span>  When I put in that code it says "simply tactic failed to simplify"</p>

#### [ Jeremy Avigad (Oct 18 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012904):
<p>Each element of <code>fin 3</code> is something of the form <code>fin.mk n h</code> where <code>n</code> is a natural number and <code>h : n &lt; 3</code>. We can abbreviate <code>fin.mk n h</code> as <code>⟨n, h⟩</code> because Lean can figure out the relevant constructor from the context.<br>
The style of writing functions using definition by cases is described in Chapter 8 of Theorem Proving in Lean: <a href="https://leanprover.github.io/theorem_proving_in_lean/" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/">https://leanprover.github.io/theorem_proving_in_lean/</a>. In the last case, <code>h</code> is of the form <code>n + 3 &lt; n</code>. We can rule out the case by showing that it is never true. <code>by simp</code> calls some built in automation to do that. As Mario points out, <code>dec_trivial</code> does something similar. It recognizes that there is a built-in procedure for evaluating inequalities, and uses that to determine that the negation of <code>n + 3 &lt; 3</code> is true.</p>

#### [ Mario Carneiro (Oct 18 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012912):
<p><span class="user-mention" data-user-id="131794">@Charles Rezk</span>  does <code>absurd h dec_trivial</code> work in place of that code?</p>

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012921):
<p>Yes, replacing <code>(by simp)</code> with <code>dec_trivial</code> works.</p>

#### [ Mario Carneiro (Oct 18 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012924):
<p>you may need some simp lemmas from mathlib</p>

#### [ Charles Rezk (Oct 18 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012927):
<p>yes</p>

#### [ Charles Rezk (Oct 18 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012929):
<p>grrr</p>

#### [ Mario Carneiro (Oct 18 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012948):
<p>do you not use mathlib?</p>

#### [ Charles Rezk (Oct 18 2018 at 03:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012992):
<p>Sure I use mathlib.</p>

#### [ Scott Olson (Oct 18 2018 at 03:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136012994):
<p><span class="user-mention" data-user-id="110865">@Jeremy Avigad</span> I think you mean <code>n + 3 &lt; 3</code></p>

#### [ Charles Rezk (Oct 18 2018 at 03:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013000):
<p>I probably haven't gotten to it.  I'm still trying to figure out functions from finite sets.</p>

#### [ Mario Carneiro (Oct 18 2018 at 03:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013008):
<p>gotten to what</p>

#### [ Charles Rezk (Oct 18 2018 at 03:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013039):
<p>I don't know.  I started trying to look at groups, then I went backwards because i didn't know how to do anything.</p>

#### [ Jeremy Avigad (Oct 18 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013102):
<p>@Scott thanks, fixed. @Charles, you are right. If you add <code>import filter.order</code> to the top of the file it should work. As Mario points out, <code>absurd h dec_trivial</code> also works without importing anything.</p>

#### [ Mario Carneiro (Oct 18 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013165):
<p>it's in filter.order? That's embarrasing</p>

#### [ Jeremy Avigad (Oct 18 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013191):
<p>It's probably in something more basic, I just happened to have <code>filter.order</code> open and that was sufficient.</p>

#### [ Mario Carneiro (Oct 18 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013200):
<p>also, I think you mean <code>order.filter</code></p>

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013424):
<p>Using <code>squeeze_simp</code>, it's <code>simp only [not_lt, zero_le, le_add_iff_nonneg_left]</code>, where <code>not_lt</code> is in <code>algebra.order</code> and the other two are in <code>algebra.ordered_group</code>.</p>

#### [ Charles Rezk (Oct 18 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013630):
<p>How would I write that without using any tactics?</p>

#### [ Mario Carneiro (Oct 18 2018 at 03:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013862):
<p><code>dec_trivial</code></p>

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 03:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013865):
<p><del><code>dec_trivial</code> isn't a tactic, technically, though it's true that it is kind of opaque.</del> I'll let someone more knowledgeable try to explain what precisely it's doing under the hood.</p>
<p>It looks like the term <code>(not_lt.mpr $ (le_add_iff_nonneg_left 3).mpr $ zero_le n)</code> also works, though I just reverse-engineered this from the <code>squeeze_simp</code> output above.</p>

#### [ Mario Carneiro (Oct 18 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013876):
<p>there are more efficient term proofs too</p>

#### [ Mario Carneiro (Oct 18 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136013883):
<p>but that's the one that simp finds</p>

#### [ Jeremy Avigad (Oct 18 2018 at 03:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136014109):
<p>@Charles Writing out a fully detailed proof from basic lemmas is painful. Here is one way to do it:</p>
<div class="codehilite"><pre><span></span>example (n : nat) : ¬ (n + 3 &lt; 3) :=
have h1 : 0 ≤ n, from nat.zero_le n,
have h2 : 0 + 3 ≤ n + 3, from nat.add_le_add_right h1 3,
have h3 : 3 ≤ n + 3, from h2,
show ¬ (n + 3 &lt; 3), from not_lt_of_ge h3
</pre></div>


<p>But this is the sort of thing we really want automation to do: we should just say "this is obvious" and let Lean figure it out. The fact that we generally have to muck around to figure out what to do is a sign that interactive theorem proving is not yet ready for prime time. We are not yet where we want to be.<br>
In fact, Scott Morrison has written an automated procedure called <code>tidy</code> that tries lots of "straightforward" things. In this case, it works:</p>
<div class="codehilite"><pre><span></span>import tactic.tidy

example (n : nat) : ¬ (n + 3 &lt; 3) :=
by tidy
</pre></div>

#### [ Charles Rezk (Oct 18 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136014218):
<p>I understand, but I'm trying to understand what is actually going on here.</p>

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 03:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136014236):
<p>In this case, tidy just calls <code>dec_trivial</code> as you can see if you put in <code>tidy { trace_result:=tt}</code>.</p>

#### [ Charles Rezk (Oct 18 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136014375):
<p>It's not clear to me why I should have to have anything there: defining a function out of fin 3, I wouldn't expect to have to say anything abut its values on 3,4,5,...</p>

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 03:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136014426):
<p>But an element of <code>fin 3</code> is defined as a <code>nat</code> called <code>val</code> plus a proof that <code>val</code> is less than 3. So to define a function out of <code>fin 3</code> you need to tell it what to do for every <code>nat</code>.</p>

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136014492):
<p>For <code>val</code>=3,4,5,... that means that you have to show that the proof that <code>val&lt;3</code> can't exist.</p>

#### [ Mario Carneiro (Oct 18 2018 at 04:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136015055):
<p>The <code>fin.cases</code> approach avoids this, although it can't use the equation compiler because it's not built in to lean.</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">f</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">3</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span>
<span class="n">fin</span><span class="bp">.</span><span class="n">cases</span> <span class="mi">7</span> <span class="err">$</span>
<span class="n">fin</span><span class="bp">.</span><span class="n">cases</span> <span class="mi">5</span> <span class="err">$</span>
<span class="n">fin</span><span class="bp">.</span><span class="n">cases</span> <span class="mi">6</span> <span class="err">$</span>
<span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="n">elim0</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">f</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">3</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span>
<span class="n">fin</span><span class="bp">.</span><span class="n">cases</span> <span class="mi">7</span> <span class="err">$</span>
<span class="n">fin</span><span class="bp">.</span><span class="n">cases</span> <span class="mi">5</span> <span class="err">$</span>
<span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="mi">6</span>
</pre></div>

#### [ Mario Carneiro (Oct 18 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136015126):
<p>the last one you can also do in the equation compiler version:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">foo</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">3</span> <span class="bp">→</span> <span class="n">nat</span>
<span class="bp">|</span> <span class="bp">⟨</span><span class="mi">0</span><span class="o">,</span> <span class="bp">_⟩</span> <span class="o">:=</span> <span class="mi">7</span>
<span class="bp">|</span> <span class="bp">⟨</span><span class="mi">1</span><span class="o">,</span> <span class="bp">_⟩</span> <span class="o">:=</span> <span class="mi">5</span>
<span class="bp">|</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="bp">_⟩</span> <span class="o">:=</span> <span class="mi">6</span>
</pre></div>

#### [ Johan Commelin (Oct 18 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136019493):
<p><span class="user-mention" data-user-id="131794">@Charles Rezk</span> Have you seen the tutorials by Neil Strickland? They are amazing. I think they can help you get up to speed with Lean. Besides that, most of us has learned everything we know by just being very persistent in asking questions here.</p>

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136020103):
<p>I would recommend slowly working through "Theorem Proving in Lean" as well. The lean-focused chapters of <a href="http://avigad.github.io/logic_and_proof/" target="_blank" title="http://avigad.github.io/logic_and_proof/">Logic &amp; Proof</a> were also quite useful to me.</p>

#### [ Kevin Buzzard (Oct 18 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136021426):
<p><span class="user-mention" data-user-id="131794">@Charles Rezk</span> The thing about <code>fin 3</code> is that it's a theorem that it has three elements. If you make your own type which has three elements "by definition" then you could do this:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">threetype</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">zero</span> <span class="o">:</span> <span class="n">threetype</span>
<span class="bp">|</span> <span class="n">one</span> <span class="o">:</span> <span class="n">threetype</span>
<span class="bp">|</span> <span class="n">two</span> <span class="o">:</span> <span class="n">threetype</span>

<span class="kn">open</span> <span class="n">threetype</span>

<span class="kn">definition</span> <span class="n">f</span> <span class="o">:</span> <span class="n">threetype</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="n">zero</span> <span class="o">:=</span> <span class="mi">59</span>
<span class="bp">|</span> <span class="n">one</span> <span class="o">:=</span> <span class="mi">65537</span>
<span class="bp">|</span> <span class="n">two</span> <span class="o">:=</span> <span class="mi">341</span>
</pre></div>


<p>You can think of the <code>n + 3 &gt; 3</code> story as just supplying the proof that there aren't any more elements of <code>fin 3</code>.</p>

#### [ Kevin Buzzard (Oct 18 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Basic%20questions/near/136024546):
<blockquote>
<p><del><code>dec_trivial</code> isn't a tactic, technically, though it's true that it is kind of opaque.</del> I'll let someone more knowledgeable try to explain what precisely it's doing under the hood.</p>
</blockquote>
<p>The writers of TPIL probably fit the bill:</p>
<p><a href="https://leanprover.github.io/theorem_proving_in_lean/type_classes.html#decidable-propositions" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/type_classes.html#decidable-propositions">https://leanprover.github.io/theorem_proving_in_lean/type_classes.html#decidable-propositions</a></p>


{% endraw %}
