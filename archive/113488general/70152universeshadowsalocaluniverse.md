---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/70152universeshadowsalocaluniverse.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [universe shadows a local universe](https://leanprover-community.github.io/archive/113488general/70152universeshadowsalocaluniverse.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sean Leather (May 17 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684147):
<p>In a file with only this:</p>
<div class="codehilite"><pre><span></span><span class="n">universes</span> <span class="n">u</span>
<span class="kn">variables</span> <span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span>
</pre></div>


<p>I get this:</p>
<div class="codehilite"><pre><span></span><span class="n">error</span><span class="o">:</span> <span class="n">invalid</span> <span class="kn">universe</span> <span class="n">declaration</span><span class="o">,</span> <span class="err">&#39;</span><span class="n">u_1&#39;</span> <span class="n">shadows</span> <span class="n">a</span> <span class="n">local</span> <span class="kn">universe</span>
</pre></div>


<p>Why?</p>

#### [ Kenny Lau (May 17 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684197):
<p>This also annoys me but I just didn't bother to ask</p>

#### [ Brendan Zabarauskas (May 17 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684203):
<p>What does <code>Type*</code> do? Does it elaborate into introducing some hidden <code>u</code> universe?</p>

#### [ Sean Leather (May 17 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684204):
<p>Yeah, it happened once too often for me: passed the annoyance threshold. <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Sean Leather (May 17 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684205):
<blockquote>
<p>What does <code>Type*</code> do? Does it elaborate into introducing some hidden <code>u</code> universe?</p>
</blockquote>
<p>It uses an implicit universe, as far as I understand it.</p>

#### [ Johan Commelin (May 17 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684207):
<p><code>set.option annoyance_threshold 100</code></p>

#### [ Johan Commelin (May 17 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684211):
<p>Solves it</p>

#### [ Brendan Zabarauskas (May 17 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684255):
<p>I've kind of noticed that Lean's elaboration isn't hygenic... guessing that's by design though?</p>

#### [ Sean Leather (May 17 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684324):
<p>It's very powerful, but it does have some annoying corner cases in various places. I believe the idea is that as long as the kernel is safe and the core language is well-typed, elaboration and tactics can be less so.</p>

#### [ Brendan Zabarauskas (May 17 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684451):
<p>By hygiene I mean in the macro sense. Racket works hard to preserve it. It might make encapsulation harder and increase the chance of breaking things downstream due to updates in libraries.</p>

#### [ Brendan Zabarauskas (May 17 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684503):
<p>(warning, might be being imprecise in my language here, feel free to correct me)</p>

#### [ Sean Leather (May 17 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684632):
<p>I sometimes like to think of Lean as one big code generator. I tries by various means to produce kernel code for definitions and theorems. Elaboration is an advanced form of unification and uses definitional equality to try to convert terms into other terms. Tactics are like imperatively programming the code generation. Type class instance resolution is another code generation mechanism. All of these try to interpret what you want and produce some kernel code. But they are all imperfect and sometimes require fiddling to get what you want.</p>
<p>(<em>Edit</em>: Language is also imprecise, but the idea helps me comprehend it.)</p>

#### [ Brendan Zabarauskas (May 17 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684811):
<p>Yeah, definitely. That's how I'm starting to sort of see it. Just wondering if some of the learning from languages like Scheme and Racket into theorem provers. Not experienced enough with Coq to know how they handle hygiene (if they do any identifier generation in their tactics/elaboration). <span class="emoji emoji-1f914" title="thinking face">:thinking_face:</span></p>

#### [ Mario Carneiro (May 17 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684948):
<p>Hygenic macros are a planned feature in the next version of lean</p>

#### [ Brendan Zabarauskas (May 17 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684951):
<p>Oh nice!</p>

#### [ Brendan Zabarauskas (May 17 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126684962):
<p>Yeah thought it might just be an intermediate state of affairs. Hard to do everything at once.</p>

#### [ Mario Carneiro (May 17 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685006):
<p>As for the given error, basically this is because <code>variables A B : Type*</code> desugars to</p>
<div class="codehilite"><pre><span></span>universe u_1
variable A : Type u_1
universe u_1
variable B : Type u_1
</pre></div>


<p>and universe shadowing is disallowed (for some reason...). This is a known bug, but it's unlikely to be addressed in the current version of lean</p>

#### [ Mario Carneiro (May 17 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685019):
<p>the workaround is to write <code>variables (A : Type*) (B : Type*)</code></p>

#### [ Brendan Zabarauskas (May 17 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685021):
<p>So I'm guessing <code>universes u</code> does nothing to affect the issue?</p>

#### [ Mario Carneiro (May 17 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685023):
<p>no, it's unrelated</p>

#### [ Mario Carneiro (May 17 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685027):
<p>although I bet you can also get a name shadowing issue with only one <code>variable</code> if it was <code>universe u_1</code></p>

#### [ Sean Leather (May 17 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685065):
<p>Yeah, I discovered that, too. What is the difference from this?</p>
<div class="codehilite"><pre><span></span><span class="kn">variable</span> <span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span>
<span class="kn">variable</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span>
</pre></div>

#### [ Mario Carneiro (May 17 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685071):
<p>that desugars to</p>
<div class="codehilite"><pre><span></span>universe u_1
variable A : Type u_1
universe u_2
variable B : Type u_2
</pre></div>


<p>which is okay</p>

#### [ Brendan Zabarauskas (May 17 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685081):
<p>In the future, is the intention to make those generated <code>u_1</code> identifiers inaccessable?</p>

#### [ Mario Carneiro (May 17 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685086):
<p>the variable command in general is more than a little hackish</p>

#### [ Sean Leather (May 17 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685090):
<p>Ah. So, it's smart enough to create a fresh universe variable there.</p>

#### [ Mario Carneiro (May 17 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685093):
<p>inaccessible? Why?</p>

#### [ Mario Carneiro (May 17 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685094):
<p>I think "fresh" is more appropriate</p>

#### [ Mario Carneiro (May 17 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685140):
<p>In fact, they come up explicitly in proofs, although it's bad form to refer to autogenerated names</p>

#### [ Mario Carneiro (May 17 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685141):
<p>but the fact that they are literal names like <code>u_1</code> and not some mystery private thing is important</p>

#### [ Brendan Zabarauskas (May 17 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685143):
<p>Hah, I might be conflicting with an existing term by the use of 'inaccessable', but yeah, it seems like it could result in fragile code if you referred to those generated names.</p>

#### [ Brendan Zabarauskas (May 17 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685195):
<p>But happy to be persuaded otherwise - I'm still new to Lean and might not fully understand.</p>

#### [ Sean Leather (May 17 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685197):
<p>Here's my first experience with <a href="https://groups.google.com/d/msg/lean-user/-Da6fPijAjY/ZK9JHUfyKAAJ" target="_blank" title="https://groups.google.com/d/msg/lean-user/-Da6fPijAjY/ZK9JHUfyKAAJ">variable name shadowing</a>.</p>

#### [ Mario Carneiro (May 17 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685273):
<p>I'm not advocating explicit reference to generated names, just the opposite (that's what I mean by "bad form"). But I can believe that sometimes it is necessary to refer to an autogenerated name, maybe because the tactic that produced the name doesn't have enough configuration space to supply nice names.</p>

#### [ Brendan Zabarauskas (May 17 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685371):
<p>What do you mean by 'configuration space'?</p>

#### [ Mario Carneiro (May 17 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685432):
<p>Some tactics have complicated logic for when they introduce new names, intro variables, etc, and it may not be easy to specify names at the top level so that after the tactic you know what you will get</p>

#### [ Brendan Zabarauskas (May 17 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685475):
<p>Interesting! That seems like a tantilising design problem to solve! <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Mario Carneiro (May 17 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685477):
<p>The lazy option (for the tactic writer) is not to bother with providing names to the tactic, so you get what you get, and then after the tactic you might need to refer to those auto names (if only to rename them)</p>

#### [ Mario Carneiro (May 17 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685487):
<p>I think that <code>finish</code> has this problem, although it's not really designed for nonterminal use so it's not a big problem</p>

#### [ Mario Carneiro (May 17 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126685535):
<p>Some tactics like <code>injections</code> just take a big list of names at the start and pull from that pool whenever something is intro'd</p>

#### [ Patrick Massot (May 17 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126688626):
<p><span class="user-mention" data-user-id="117066">@Brendan Zabarauskas</span> see <a href="https://github.com/leanprover/lean/issues/1674" target="_blank" title="https://github.com/leanprover/lean/issues/1674">https://github.com/leanprover/lean/issues/1674</a> which, I believe, is one the main issue Lean 4 is meant to solve, and contains "Hygienic macro system" in the title. Lean 4 is currently worked on (but won't come soon).</p>

#### [ Brendan Zabarauskas (May 17 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126689678):
<p>Very cool! And understandable that it will take time - good to know it's coming though.</p>

#### [ Johan Commelin (May 17 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126690354):
<p>Wow, I like the ideas in that issue! <span class="user-mention" data-user-id="110031">@Patrick Massot</span> do you remember asking about tikzcd notation for commutative diagrams in lean? That might become a true option then! I like it (-;</p>

#### [ Patrick Massot (May 17 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe%20shadows%20a%20local%20universe/near/126692094):
<p>Indeed I was thinking about this when I mentioned tikz-cd syntax</p>


{% endraw %}
