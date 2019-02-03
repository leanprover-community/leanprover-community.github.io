---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/67902structureequalityfromparts.html
---

## Stream: [general](index.html)
### Topic: [structure equality from parts](67902structureequalityfromparts.html)

---


{% raw %}
#### [ Nicholas Scheel (Mar 21 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033267):
<p>Hi, I'm totally new here, I've spent about a day with Lean so far.</p>
<p>Currently I'm struggling to define a notion of equality for this structure (permutations aka bijective functions, which I represent with a function and its inverse, and the proof that they are inverses):</p>
<div class="codehilite"><pre><span></span>structure Perm (α : Type) :=
permute ::
  (forward : α → α) (backward : α → α)
  (are_inv : function.left_inverse forward backward ∧ function.right_inverse forward backward)
</pre></div>


<p>It appears that Lean understands <code>refl</code> enough to let me do the following:</p>
<div class="codehilite"><pre><span></span>def Perm.eq {α : Type}
  : Π (p1 p2 : Perm α),
    p1.forward = p2.forward →
    p1.backward = p2.backward →
    p1 = p1
| p1 p2 .(rfl) .(rfl) := rfl
</pre></div>


<p>but what I _really_ want is a proof that <code>p1 = p2</code> at the end, but if I give it that type it complains that <code>rfl : p1 = p1</code> not <code>p1 = p2</code> (even though it looks like the compiler has enough information to determine <code>p1 = p2</code> and has already unified them? idk)</p>
<p>I've looked in the standard library for similar examples but couldn't find any.</p>
<p>Would appreciate some pointers or help!</p>
<p>(my overall goal is to prove the group structure of permutations, which I think needs to be done through the components?)</p>

#### [ Simon Hudon (Mar 21 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033339):
<p>You might want to build on top of <code>equiv</code> from <code>mathlib</code>.</p>

#### [ Nicholas Scheel (Mar 21 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033356):
<p>in particular, if I try</p>
<div class="codehilite"><pre><span></span>.......
    p1 = p2
| p1 p2 .(rfl) .(rfl) := _
</pre></div>


<p>I get the following message:</p>
<div class="codehilite"><pre><span></span>don&#39;t know how to synthesize placeholder
context:
α : Type,
Perm.eq : ∀ (p1 p2 : Perm α), p1.forward = p2.forward → p1.backward = p2.backward → p1 = p2,
p1 : Perm α
⊢ p1 = p1
</pre></div>


<p>Notice that only p1 is in scope and it wants a proof of <code>p1 = p1</code>, which is just <code>rfl</code>, but <code>rfl</code> won't actually unify in that environment when I try it.</p>

#### [ Simon Hudon (Mar 21 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033360):
<p>For your specific problem, try this instead:</p>
<div class="codehilite"><pre><span></span>| ⟨f₀,b₀,p₀⟩ ⟨f₁,b₁,p₁⟩ .(rfl) .(rfl) := rfl
</pre></div>

#### [ Simon Hudon (Mar 21 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033415):
<p>Sorry, I made a mistake:</p>

#### [ Simon Hudon (Mar 21 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033422):
<div class="codehilite"><pre><span></span>| ⟨f₀,b₀,p₀⟩ ⟨._,._,._⟩ .(rfl) .(rfl) := rfl
</pre></div>


<p>I think that should work</p>

#### [ Simon Hudon (Mar 21 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033496):
<p>The reason is that, to infer equality of the whole from equality of the parts, you need to pattern match on the whole. Then, the unification of the variables used for the components will translate into the patterns for the two wholes to be syntactically equal and this is where <code>rfl</code> works</p>

#### [ Nicholas Scheel (Mar 21 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033515):
<p>hmm I'm still getting a cryptic error with both of those:</p>
<div class="codehilite"><pre><span></span>......
has type
∀ (forward_1 backward_1 : α → α)
(are_inv_1 : function.left_inverse forward_1 backward_1 ∧ function.right_inverse forward_1 backward_1),
{forward := forward, backward := backward, are_inv := are_inv}.forward =
{forward := forward_1, backward := backward_1, are_inv := are_inv_1}.forward →
{forward := forward, backward := backward, are_inv := are_inv}.backward =
{forward := forward_1, backward := backward_1, are_inv := are_inv_1}.backward →
{forward := forward, backward := backward, are_inv := are_inv} =
{forward := forward, backward := backward, are_inv := are_inv}
but is expected to have type
∀ (forward_1 backward_1 : α → α)
(are_inv_1 : function.left_inverse forward_1 backward_1 ∧ function.right_inverse forward_1 backward_1),
(λ (p2 : Perm α),
{forward := forward, backward := backward, are_inv := are_inv}.forward = p2.forward →
{forward := forward, backward := backward, are_inv := are_inv}.backward = p2.backward →
{forward := forward, backward := backward, are_inv := are_inv} = p2)
{forward := forward_1, backward := backward_1, are_inv := are_inv_1}
</pre></div>


<p>(I'm using <a href="https://leanprover.github.io/live/3.3.0/" target="_blank" title="https://leanprover.github.io/live/3.3.0/">https://leanprover.github.io/live/3.3.0/</a> btw)</p>

#### [ Simon Hudon (Mar 21 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033713):
<p>I see. The problem is the <code>.</code> before <code>rfl</code>. I think the idea is that they are not irrelevant (or inferred from the context). They actually help you establish that <code>p1</code> and <code>p2</code> are identical:</p>
<div class="codehilite"><pre><span></span>def Perm.eq {α : Type}
  : Π (p1 p2 : Perm α),
    p1.forward = p2.forward →
    p1.backward = p2.backward →
    p1 = p2
| ⟨a,b,p⟩ ⟨._,._,._⟩ (rfl) (rfl) := rfl
</pre></div>

#### [ Nicholas Scheel (Mar 21 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033784):
<p>aha! that seems to be working, thanks so much!</p>

#### [ Kevin Buzzard (Mar 21 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033799):
<p><a href="https://github.com/leanprover/mathlib/blob/master/data/equiv.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/data/equiv.lean">https://github.com/leanprover/mathlib/blob/master/data/equiv.lean</a></p>

#### [ Kevin Buzzard (Mar 21 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033802):
<p>There are some spoilers for this sort of thing</p>

#### [ Kevin Buzzard (Mar 21 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033809):
<p>Your <code>Perm</code> is the <code>equiv</code> on line 54</p>

#### [ Kevin Buzzard (Mar 21 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033932):
<p>no, sorry, equiv can have different source and target. Your <code>Perm</code> is the <code>perm</code> on line 62</p>

#### [ Nicholas Scheel (Mar 21 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033944):
<p>very cool, thanks for the link :) is that accessible in the online editor or no?</p>

#### [ Chris Hughes (Mar 21 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124033993):
<p>I think not</p>

#### [ Simon Hudon (Mar 21 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034017):
<p>I think it is. The online version imports <code>mathlib</code> and I don't think <code>equiv</code> is too new</p>

#### [ Kevin Buzzard (Mar 21 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034029):
<div class="codehilite"><pre><span></span>import data.equiv

#print equiv.perm
 ```
</pre></div>

#### [ Kevin Buzzard (Mar 21 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034067):
<p>works in lean web editor</p>

#### [ Simon Hudon (Mar 21 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034069):
<p>I just checked, it's there</p>

#### [ Simon Hudon (Mar 21 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034099):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I'm confused by your reaction to your own post. Which direction are you two pointing to?</p>

#### [ Kevin Buzzard (Mar 21 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034103):
<p>I was trying to point to your comment :-)</p>

#### [ Kevin Buzzard (Mar 21 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034151):
<p>Lean 3.4 should be with us soon, and perhaps they'll update the lean web editor so it runs 3.4. There was extensive discussion on gitter about getting everything to compile but in the end all the problems were solved IIRC.</p>

#### [ Kevin Buzzard (Mar 21 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034165):
<p><a href="https://gitter.im/leanprover_public/lean_js" target="_blank" title="https://gitter.im/leanprover_public/lean_js">https://gitter.im/leanprover_public/lean_js</a></p>

#### [ Kevin Buzzard (Mar 21 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034171):
<p>probably-hard-to-find but useful link if you want to set it up yourself.</p>

#### [ Kevin Buzzard (Mar 21 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034230):
<p>but if you're going to compile it I suppose you'd just be better off running it in an IDE :-) I think Scott compiled a more recent version of Lean and left it on an internet-facing server...</p>

#### [ Simon Hudon (Mar 21 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034314):
<p>Was it hard to compile because of the new monadic code?</p>

#### [ Mario Carneiro (Mar 21 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034362):
<p>No, that discussion predates the monad stuff by a while. I think it was just some JS compilation arcana</p>

#### [ Simon Hudon (Mar 21 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034397):
<p>Oh fun!</p>

#### [ Nicholas Scheel (Mar 21 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034431):
<p>I have a PureScript background – JS is weird :D</p>

#### [ Kevin Buzzard (Mar 21 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034435):
<p>Yes, apparently taking a bunch of C++ code and compiling it into javascript isn't 100% straightforward</p>

#### [ Nicholas Scheel (Mar 21 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034481):
<p>I have to say, the online editor is really slick I'm impressed!</p>

#### [ Simon Hudon (Mar 21 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034629):
<p>So they actually translate the whole C++ code base to Java script and the whole thing runs in the browser? That's really cool :) I just assumed the code was sent to a server and sent back after verification.</p>

#### [ Simon Hudon (Mar 21 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034649):
<blockquote>
<p>I have to say, the online editor is really slick I'm impressed!</p>
</blockquote>
<p>Microsoft has a few like that. It's a cool idea to get you started before you decide to install it</p>

#### [ Kevin Buzzard (Mar 21 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034799):
<p>The moment you try and do something non-trivial in the lean web editor things slow to a crawl; the "recompile the entire file every time the user presses a key" gets old pretty quickly. But for small bits of experimentation I absolutely agree, it's very cute.</p>

#### [ Nicholas Scheel (Mar 21 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034866):
<p>yeah, and a little debouncing would go a long ways ... but I'm patient with it ;)</p>

#### [ Simon Hudon (Mar 21 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034912):
<p>It might just be a tease: the real thing is actually pretty fast and getting faster.</p>

#### [ Simon Hudon (Mar 21 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034928):
<p>I think <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> should merge an incremental caching strategy pretty soon which will make things even smoother</p>

#### [ Kevin Buzzard (Mar 21 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034932):
<p>The next step after Lean Web Editor is to try a nightly. Except that the current nightly might not work with mathlib. Is this now a problem that the community has solved?</p>

#### [ Kevin Buzzard (Mar 21 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034935):
<p>What is this #travis stream anyway?</p>

#### [ Simon Hudon (Mar 22 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124034989):
<blockquote>
<p>What is this #travis stream anyway?</p>
</blockquote>
<p>Whenever someone commits to <code>mathlib</code>, we get the build report there.</p>

#### [ Kevin Buzzard (Mar 22 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035007):
<p>Oh, so we still don't have access to e.g. a nightly build before all the monad refactoring stuff went in?</p>

#### [ Kevin Buzzard (Mar 22 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035012):
<p>I mean core lean</p>

#### [ Kevin Buzzard (Mar 22 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035067):
<p>There was an entire week from 13th to 20th March with no commits and Lean was working just fine for me. And now we have all this monad refactoring and everyone is assuming mathlib won't build any more</p>

#### [ Simon Hudon (Mar 22 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035134):
<p>I think older nightlies should still be available. Don't you get a long list of nightlies on the site?</p>

#### [ Simon Hudon (Mar 22 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035181):
<p>I think what we might need is for <code>mathlib</code> to publish Lean nightlies, a subset of all the nightlies for which <code>mathlib</code> passes.</p>

#### [ Kevin Buzzard (Mar 22 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035197):
<p>I can pull the repo and checkout a random commit and compile, but I don't think I've ever seen a list of nightlies. Where are they?</p>

#### [ Simon Hudon (Mar 22 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035342):
<p>I can't find it anymore. I wonder if they changed the way nightly works</p>

#### [ Nicholas Scheel (Mar 22 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035352):
<p>here's my messy code as a whole if anyone is curious <span class="emoji emoji-1f609" title="wink">:wink:</span> <a href="https://gist.github.com/MonoidMusician/b2792a2d9687dd627155996097ad97c1" target="_blank" title="https://gist.github.com/MonoidMusician/b2792a2d9687dd627155996097ad97c1">https://gist.github.com/MonoidMusician/b2792a2d9687dd627155996097ad97c1</a> (we talked about equivalence classes of functions with permutations in my combinatorics class, so I wanted to play around with the idea a little bit – in particular, equivalent surjective functions will have a unique (post-composed) permutation for the equivalence)<br>
thanks again for the help!</p>

#### [ Sebastian Ullrich (Mar 22 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035501):
<p>The nightly releases PR was merged today, though today's build has already failed because of broken setup... I'll test it tomorrow by having it build a custom pre-monad nightly</p>

#### [ Simon Hudon (Mar 22 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035521):
<p>Are more than one nightly supposed to be available at any given time?</p>

#### [ Kevin Buzzard (Mar 22 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035526):
<p>I've never seen more than one available</p>

#### [ Kevin Buzzard (Mar 22 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035530):
<p>(per OS of course)</p>

#### [ Simon Hudon (Mar 22 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035585):
<p>I should go offline: my dissertation doesn't write itself when I don't look at it :/  (no matter how long I look away)</p>

#### [ Mario Carneiro (Mar 22 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124035589):
<p>I think your definition of <code>PostPermEquiv</code> should use <code>subtype</code> (notation <code>{x // p x}</code>)</p>

#### [ Nicholas Scheel (Mar 22 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036061):
<p>okay, looks good – what's the difference? :)</p>

#### [ Nicholas Scheel (Mar 22 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036145):
<p>ah, more specific to Prop?</p>

#### [ Mario Carneiro (Mar 22 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036301):
<p>You also shouldn't need the <code>n+2</code> case in the definition of <code>swap</code> and <code>swap_involution</code></p>

#### [ Mario Carneiro (Mar 22 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036316):
<p>Also, as Kevin says most of this theory is in <code>data.equiv</code> in mathlib, although we don't do anything with postperm stuff</p>

#### [ Nicholas Scheel (Mar 22 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036318):
<p>hmm I get</p>
<div class="codehilite"><pre><span></span>non-exhaustive match, the following cases are missing:
swap ⟨nat.succ (nat.succ _), _⟩
</pre></div>

#### [ Kevin Buzzard (Mar 22 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036500):
<p><code>| ⟨n+2, prf⟩ := ⟨n+2,prf⟩</code> works :-)</p>

#### [ Mario Carneiro (Mar 22 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036563):
<p>Ah, I see, it would work except that the underlying inductive type <code>nat.less_than_or_equal</code> eliminates to Prop, so it can't be used to define an element of <code>fin 2</code> (although it can be used to define an element of <code>false</code> which then defines an element of <code>fin 2</code>)</p>

#### [ Mario Carneiro (Mar 22 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036621):
<p>You can also use <code>absurd prf dec_trivial</code> instead of that finis stuff</p>

#### [ Nicholas Scheel (Mar 22 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036635):
<p>haha that's really helpful <span class="emoji emoji-1f606" title="laughing">:laughing:</span></p>

#### [ Nicholas Scheel (Mar 22 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036703):
<p>I will learn these voodoo tactics one day!</p>

#### [ Kevin Buzzard (Mar 22 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036704):
<p>If you define <code>swap (n+2)</code> to be <code>n+2</code> then you get to write</p>
<div class="codehilite"><pre><span></span>lemma  swap_involution : ∀ n, swap (swap n) = n
| ⟨0, _⟩ := rfl
| ⟨1, _⟩ := rfl
| ⟨n+2, prf⟩ := rfl
</pre></div>

#### [ Nicholas Scheel (Mar 22 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036766):
<p>true, and that's essentially what the more general swapping does too</p>

#### [ Nicholas Scheel (Mar 22 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality%20from%20parts/near/124036972):
<p>thanks for all the help!!</p>


{% endraw %}
