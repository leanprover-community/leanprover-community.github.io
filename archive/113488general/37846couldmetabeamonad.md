---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/37846couldmetabeamonad.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [could meta be a monad](https://leanprover-community.github.io/archive/113488general/37846couldmetabeamonad.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Oct 15 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135797914):
<p>Something that popped into my head recently, and my curiosity makes me ask this question:<br>
Could <code>meta</code> have been a monad?<br>
In Haskell, there is the <code>IO</code> monad that marks functions "unsafe" (i.e., they can have side effects). I could imagine that <code>meta</code> could also be a monad that marks functions "unsafe" (i.e., they are meta). Would this work? What would be the pros and cons?</p>

#### [ Simon Hudon (Oct 15 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135802955):
<p>Do you mean <code>tactic</code>? It's already a monad.</p>

#### [ Johan Commelin (Oct 15 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135806442):
<p>No, I meant what I wrote. [Edit: misinterpreted Simon's answer.]</p>

#### [ Scott Morrison (Oct 15 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135806499):
<p>I think you're conflating <code>meta</code> and <code>tactic</code> here.</p>

#### [ Johan Commelin (Oct 15 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135806648):
<p>No, I really meant <code>meta</code>.</p>

#### [ Johan Commelin (Oct 15 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135806698):
<p>If I have a trusted piece of code, I could wrap it into the "meta" tactic, and it would no longer be trusted, etc, etc...</p>

#### [ Johan Commelin (Oct 15 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135806700):
<p>Or does <span class="user-mention" data-user-id="110026">@Simon Hudon</span> mean that <code>tactic</code> is already a monad. I see. Yes, that I knew.</p>

#### [ Johan Commelin (Oct 15 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135806707):
<p>So I repeat my question: <em>Could</em> <code>meta</code> be a monad?</p>

#### [ Simon Hudon (Oct 15 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135806807):
<p>Ok so instead of having a keyword meta, you'd have a meta monad which would enable unbounded recursion and access to the prover's internals</p>

#### [ Simon Hudon (Oct 15 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135806815):
<p>I know that they want more parts of the tactics framework to be in pure code for Lean 4 but I don't know if everything can go there.</p>

#### [ Simon Hudon (Oct 15 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135806816):
<p>What gain do you think it would give us?</p>

#### [ Johan Commelin (Oct 15 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135806917):
<p>Like I said in my first post: just curiosity. I don't know anything about theoretical pros and cons.</p>

#### [ Simon Hudon (Oct 15 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135807044):
<p>I think at the moment, pure code doesn't allow unbounded recursion yet but that could be added too. I can't think of other reasons to not write all meta code as pure code</p>

#### [ Mario Carneiro (Oct 15 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135807583):
<p>I think the best analogue here is actually the <code>io</code> monad of lean</p>

#### [ Mario Carneiro (Oct 15 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135807626):
<p>it is non-meta, but you can do lots of external manipulation stuff and unbounded recursion</p>

#### [ Gabriel Ebner (Oct 15 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135814024):
<blockquote>
<p>Could <code>meta</code> have been a monad?</p>
</blockquote>
<p>Yes, instead of the <code>meta</code> keyword we could have a <code>meta</code> monad as follows:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="err">«</span><span class="n">meta</span><span class="err">»</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span>
<span class="bp">|</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">false</span> <span class="bp">→</span> <span class="n">α</span>
</pre></div>


<p>I think you can derive all features of the current meta in this monad, including <code>undefined</code> and general recursion.  But I'm not sure how helpful it would be.</p>

#### [ Johan Commelin (Oct 15 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/135814262):
<p>I'm not sure if it is helpful. But I do find it <em>funny</em>.</p>

#### [ Reid Barton (Oct 19 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/136114496):
<p>Encoding a type of effect as a monad has various generic disadvantages, including:</p>
<ul>
<li>You need different syntaxes to form the application <code>f x</code> depending on whether each of <code>f</code> or <code>x</code> is a monadic value or an ordinary value (here: <code>meta</code> or not).</li>
<li>You need to specify an order of effects, which forces you to linearize your program to a certain extent, whereas a pure program can have a tree structure.</li>
<li>If you want to use a second monad as well (say the <code>list</code> monad), now you need to figure out some way to combine the second monad with your effect monad (using something like monad transformers perhaps).</li>
</ul>
<p>In some contexts these points could be viewed as advantages, but the effect of nontermination is so mild that that doesn't apply here. For example, if <code>x</code> and <code>y</code> are possibly nonterminating computations, then computing <code>x</code> and then <code>y</code> is the same as computing <code>y</code> and then <code>x</code>.</p>

#### [ Reid Barton (Oct 19 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/could%20meta%20be%20a%20monad/near/136114667):
<p>The only advantage of <code>meta</code> as a monad that I can think of is on the implementation side: Lean would no longer have to track the <code>meta</code> property. However, I think there would still be special cases required to reproduce the current behavior, e.g., <code>meta</code> inductive types have a relaxed syntax for recursion--Lean would have to make the constructors and/or recursors operate in the <code>meta</code> monad</p>


{% endraw %}
