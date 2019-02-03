---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/43082538opposites.html
---

## Stream: [PR reviews](https://leanprover-community.github.io/archive/144837PRreviews/index.html)
### Topic: [#538 opposites](https://leanprover-community.github.io/archive/144837PRreviews/43082538opposites.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Dec 20 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152229118):
<p>maybe someone can write a tactic!</p>

#### [ Kevin Buzzard (Dec 20 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238513):
<p>Do we have modules over a non-commutative ring? If so you could do left modules over R = right modules over <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>R</mi><mrow><mi>o</mi><mi>p</mi></mrow></msup></mrow><annotation encoding="application/x-tex">R^{op}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">o</span><span class="mord mathit mtight">p</span></span></span></span></span></span></span></span></span></span></span></span>.</p>

#### [ Kevin Buzzard (Dec 20 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238562):
<p>I agree that what you did should all be automated somehow. This is just the sort of thing that as a lecturer I would skip over -- I would let the students automate it.</p>

#### [ Kenny Lau (Dec 20 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238632):
<p>do we have right modules?</p>

#### [ Kevin Buzzard (Dec 20 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238648):
<p>Oh well if we don't that would be great because you can just define them as left modules over the opposite ring :P</p>

#### [ Kenny Lau (Dec 20 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238695):
<p>great!</p>

#### [ Mario Carneiro (Dec 20 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238699):
<p>Note that by kenny's definition <code>R^op = R</code> for any ring</p>

#### [ Kenny Lau (Dec 20 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238702):
<p>what?</p>

#### [ Mario Carneiro (Dec 20 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238706):
<p>you commuted the addition, which is commutative in a ring</p>

#### [ Kenny Lau (Dec 20 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238709):
<p>but multiplication?</p>

#### [ Mario Carneiro (Dec 20 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238724):
<p>did you commute both? that's confusing</p>

#### [ Kenny Lau (Dec 20 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238725):
<p>yes, I commuted both</p>

#### [ Kenny Lau (Dec 20 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238727):
<p>since addition doesn't matter anyway</p>

#### [ Kenny Lau (Dec 20 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238730):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> what's an argument against commuting both?</p>

#### [ Mario Carneiro (Dec 20 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238787):
<p>it might still matter for defeq which way you have it</p>

#### [ Mario Carneiro (Dec 20 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238800):
<p>like I asked on the PR, what do you want to use this for?</p>

#### [ Mario Carneiro (Dec 20 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238809):
<p>I thought that everything is commutative in Kevin's world</p>

#### [ Kenny Lau (Dec 20 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238859):
<p>not really</p>

#### [ Kenny Lau (Dec 20 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238870):
<p>as long as he cares about group representation</p>

#### [ Kenny Lau (Dec 20 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238955):
<p>End(A,A) = A^op</p>

#### [ Kenny Lau (Dec 20 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239077):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> what do you think?</p>

#### [ Johan Commelin (Dec 20 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239244):
<p>Ehm, we definitely care about non-commutative rings. It's just that we call them that: <em>non-commutative rings</em>, instead of <em>rings</em>.</p>

#### [ Johan Commelin (Dec 20 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239251):
<p>Whether commuting the addition is a good idea, I don't know. Mathematically it doesn't matter, and I guess it might make some things a bit easier to prove?</p>

#### [ Mario Carneiro (Dec 20 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239312):
<blockquote>
<p>End(A,A) = A^op</p>
</blockquote>
<p>what does that mean exactly? Since A^op ~= A why isn't it just End(A,A) = A?</p>

#### [ Johan Commelin (Dec 20 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239481):
<p><code>End(_,_)</code> looks a bit funny anyway <span class="emoji emoji-1f923" title="rolling on the floor laughing">:rolling_on_the_floor_laughing:</span></p>

#### [ Kenny Lau (Dec 20 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239555):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> oops I meant End(A), I don't know what's wrong with me</p>

#### [ Johan Commelin (Dec 20 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239560):
<p>Well, maybe you're human? <span class="emoji emoji-1f600" title="grinning">:grinning:</span></p>

#### [ Kenny Lau (Dec 20 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239562):
<p>I don't think A^op and A are isomorphic in general?</p>

#### [ Johan Commelin (Dec 20 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239569):
<p>Definitely not.</p>

#### [ Reid Barton (Dec 20 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239573):
<p>Not that I can visualize a concrete situation where the choice matters, but it feels wrong to me to reverse the order of addition in the opposite ring</p>

#### [ Kenny Lau (Dec 20 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239576):
<p>G^op and G are in fact isomorphic</p>

#### [ Kenny Lau (Dec 20 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239581):
<p>for a group G</p>

#### [ Kenny Lau (Dec 20 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239583):
<p>I think this still works for division rings</p>

#### [ Johan Commelin (Dec 20 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239585):
<p>Sure, for groups it's fine.</p>

#### [ Kenny Lau (Dec 20 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239590):
<p>so H and H^op are isomorphic</p>

#### [ Johan Commelin (Dec 20 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239633):
<p>That's coincidence.</p>

#### [ Johan Commelin (Dec 20 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239636):
<p>Because H has order 2 in the Brauer group.</p>

#### [ Johan Commelin (Dec 20 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239640):
<p>In general division rings arent isom to their opposite.</p>

#### [ Kenny Lau (Dec 20 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239664):
<p>oh right never mind sorry</p>

#### [ Reid Barton (Dec 20 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239676):
<p>Also, I wonder if these opposites will run into the same kind of issues we had/have in category theory, where it's too easy to get confused between an object of a category and an object of the opposite category</p>

#### [ Kenny Lau (Dec 20 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239679):
<p>that's exactly why I put <code>irreducible</code>!</p>

#### [ Reid Barton (Dec 20 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239729):
<p>Oh whoops, my mind was numbed by the endless identical instances and I missed that line</p>

#### [ Johan Commelin (Dec 20 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239745):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> What do you think of the <code>irreducible</code> thing? It seems like a good idea to me? (But then, I might not know all the consequences...)</p>

#### [ Kenny Lau (Dec 20 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239793):
<blockquote>
<p>I don't like the use of irreducible here. What is the application of this file? additive and multiplicative are useful in contexts where you just assert that a theorem has a type involving addition instead of multiplication, and the kernel figures out the defeq; irreducible will block that kind of move. Also you aren't being specific about whether the addition or multiplication is being commuted here.</p>
</blockquote>
<p>(by Mario)</p>

#### [ Mario Carneiro (Dec 20 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239934):
<p>For example, suppose I want to prove add_comm from mul_comm. The <code>multiplicative</code> trick relies on the fact that <code>add A x y = add A y x</code> is definitionally equal to <code>mul (multiplicative A) x y = mul (multiplicative A) y x</code>. With irreducible in there I have to insert lots of ops and unops and the kernel can't do it on its own</p>

#### [ Mario Carneiro (Dec 20 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240032):
<p>By the way re: isom to opposite, I was thinking of the map x |-&gt; x, and using antihoms where appropriate</p>

#### [ Kenny Lau (Dec 20 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240043):
<p>and I think using that defintional equality is not very safe</p>

#### [ Mario Carneiro (Dec 20 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240049):
<p>it's not, it has to be used in carefully controlled circumstances</p>

#### [ Mario Carneiro (Dec 20 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240100):
<p>its use is more or less restricted to one liner proofs where you reinterpret a multiplicative theorem as additive</p>

#### [ Johan Commelin (Dec 20 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240111):
<p>Right, but here we will want to talk about <code>op R</code>, which is a completely different ring.</p>

#### [ Johan Commelin (Dec 20 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240116):
<p>I think it is fitting to make it irreducible.</p>

#### [ Kenny Lau (Dec 20 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240121):
<blockquote>
<p>its use is more or less restricted to one liner proofs where you reinterpret a multiplicative theorem as additive</p>
</blockquote>
<p>and it's open to abuse / misuse</p>

#### [ Mario Carneiro (Dec 20 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240126):
<p>if you want it to be a different ring, then you should use a structure</p>

#### [ Kenny Lau (Dec 20 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240192):
<p>really?</p>

#### [ Kenny Lau (Dec 20 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240203):
<p>well isn't the effect the same</p>

#### [ Reid Barton (Dec 20 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240312):
<p>It's not exactly the same, as <code>op (unop x)</code> will not be defeq to <code>x</code>.<br>
(... <code>newtype</code>?)</p>

#### [ Kenny Lau (Dec 20 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240326):
<p>then I think the current definition is better :P</p>

#### [ Kenny Lau (Dec 20 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240382):
<p>and this is consistent with my support of auxiliary types</p>

#### [ Kenny Lau (Dec 20 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240387):
<p>I think <code>additive</code> and <code>multiplicative</code> should be irreducible as well</p>

#### [ Johan Commelin (Dec 20 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240399):
<blockquote>
<p>I think <code>additive</code> and <code>multiplicative</code> should be irreducible as well</p>
</blockquote>
<p>I still hope that one day we will have a system where they don't exist.</p>

#### [ Mario Carneiro (Dec 20 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240461):
<p>If you are giving a newtype API for opposite, then I would rather have no defeqs at all</p>

#### [ Mario Carneiro (Dec 20 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240464):
<p><code>op (unop x) = x</code> is a theorem</p>

#### [ Mario Carneiro (Dec 20 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240470):
<p>as well as <code>unop (op x) = x</code></p>

#### [ Kenny Lau (Dec 20 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240482):
<p>what is newtype?</p>

#### [ Mario Carneiro (Dec 20 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240492):
<p>it's a structure with one field</p>

#### [ Kenny Lau (Dec 20 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240493):
<blockquote>
<p>If you are giving a newtype API for opposite, then I would rather have no defeqs at all</p>
</blockquote>
<p>don't we like defeqs?</p>

#### [ Mario Carneiro (Dec 20 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240500):
<p>recall the real irreducible discussion</p>

#### [ Mario Carneiro (Dec 20 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240534):
<p>defeq breaks abstractions</p>

#### [ Reid Barton (Dec 20 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240544):
<p>I was hoping for "newtype" to be defeq in both directions but still a new type</p>

#### [ Kenny Lau (Dec 20 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240550):
<p>it's a new type to the kernel</p>

#### [ Mario Carneiro (Dec 20 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240551):
<p>if lean had structure eta that would be possible</p>

#### [ Reid Barton (Dec 20 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240561):
<p>on the basis that Haskell semantic equality (considering bottom) ~ Lean definitional equality</p>

#### [ Kenny Lau (Dec 20 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240565):
<blockquote>
<p>defeq breaks abstractions</p>
</blockquote>
<p>I don't understand</p>

#### [ Kenny Lau (Dec 20 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240568):
<p>and also why is <code>unop (op x) = x</code> being defeq ok</p>

#### [ Reid Barton (Dec 20 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240594):
<p>(BTW, <em>lots</em> of category theory stuff would be less awful with eta for structures)</p>

#### [ Mario Carneiro (Dec 20 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241162):
<p>it's called a newtype because it's underlying representation is the same</p>

#### [ Mario Carneiro (Dec 20 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241163):
<p>it's a "zero cost abstraction"</p>

#### [ Mario Carneiro (Dec 20 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241305):
<blockquote>
<p>on the basis that Haskell semantic equality (considering bottom) ~ Lean definitional equality</p>
</blockquote>
<p>I don't think this is a good comparison; why isn't that ~ lean propositional equality?</p>

#### [ Reid Barton (Dec 20 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241327):
<p>I don't understand why, but it seems to be a useful heuristic in practice.</p>

#### [ Reid Barton (Dec 20 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241333):
<p>For example <code>fst (a, b) = a</code> is okay, but <code>(fst p, snd p) = p</code> is not.</p>

#### [ Reid Barton (Dec 20 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241465):
<p>The stuff about "lazy patterns" should fit in somehow, too. But I don't know how to make real sense out of any of this. For one thing, Haskell has a (partial) definedness ordering between things like <code>(fst p, snd p)</code> and <code>p</code>, but in Lean, the thing that would be more defined in Haskell is instead somehow "better", but I don't know why.</p>

#### [ Reid Barton (Dec 20 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241485):
<p>It's not like <code>\lam \&lt;a, b\&gt;, \&lt;a, b\&gt;</code> is "less defined" than <code>\lam p, p</code></p>

#### [ Mario Carneiro (Dec 20 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241532):
<p>hm, you may be on to something here</p>

#### [ Reid Barton (Dec 20 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241566):
<p>I hope you can figure out what it is, because I find it puzzling!</p>

#### [ Mario Carneiro (Dec 20 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241577):
<p>It reminds me of the problem of understanding metamath semantics</p>

#### [ Mario Carneiro (Dec 20 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241588):
<p>Maybe another way to think of it is that every type is populated, in additional to the usual things, with "raw variables"</p>

#### [ Mario Carneiro (Dec 20 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241593):
<p>which are just terms that don't denote anything, like atoms</p>

#### [ Mario Carneiro (Dec 20 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241633):
<p>and those two lambdas behave differently on raw variables</p>

#### [ Reid Barton (Dec 20 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241638):
<p>Yes, this sounds promising</p>

#### [ Reid Barton (Dec 20 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241655):
<p>that gives an ordering too perhaps, by specializing variables to values (which might contain new variables inside)</p>

#### [ Mario Carneiro (Dec 20 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241661):
<p>exactly</p>

#### [ Mario Carneiro (Dec 20 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241663):
<p>that's how metamath semantics works</p>

#### [ Mario Carneiro (Dec 20 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241667):
<p>it's all about the metavariables</p>

#### [ Kenny Lau (Jan 07 2019 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/154559706):
<p>so what should we do? <span class="user-mention" data-user-id="112680">@Johan Commelin</span> <span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Kenny Lau (Jan 08 2019 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/154631186):
<p>I guess I have made opposite inductive</p>

#### [ Kenny Lau (Jan 12 2019 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/154975129):
<p>Should we make <code>order_dual</code> in <code>order/basic.lean</code> also a structure / inductive?</p>

#### [ Kenny Lau (Jan 12 2019 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/154975174):
<p>or maybe we should merge these two</p>

#### [ Kenny Lau (Jan 22 2019 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643371):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> what do you think about merging those two?</p>

#### [ Reid Barton (Jan 22 2019 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643518):
<p>Which two?</p>

#### [ Johannes Hölzl (Jan 22 2019 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643551):
<p>I guess Kenny meant "merge this too"</p>

#### [ Johannes Hölzl (Jan 22 2019 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643596):
<p>I would prefer <code>opposite</code> to be like <code>order_dual</code>, just a definition</p>

#### [ Patrick Massot (Jan 22 2019 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643616):
<p>I think he continues from the previous message in this thread</p>

#### [ Patrick Massot (Jan 22 2019 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643678):
<p>From January 12th</p>

#### [ Reid Barton (Jan 22 2019 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643731):
<p>Ah</p>

#### [ Johannes Hölzl (Jan 22 2019 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643736):
<p>ah</p>

#### [ Kenny Lau (Jan 22 2019 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643776):
<p>oh, sorry, I meant merging opposite and order_dual</p>

#### [ Johannes Hölzl (Jan 22 2019 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643870):
<p>Hm, or we need <code>multiplicative_opp</code> and <code>additive_opp</code>...</p>

#### [ Reid Barton (Jan 22 2019 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643898):
<p>I suppose you could have an ordered group and want to reverse the multiplication but not the order, or vice versa</p>

#### [ Johannes Hölzl (Jan 22 2019 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643913):
<p>Yep</p>

#### [ Kenny Lau (Jan 22 2019 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643940):
<p>then what should I do?</p>

#### [ Kenny Lau (Jan 22 2019 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644221):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> I don't see why we need multiplicative_opp and additive_opp; the only structure with both addition and multiplication are children of <code>semiring</code> in which addition is commutative anyway, right?</p>

#### [ Johannes Hölzl (Jan 22 2019 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644378):
<p>I don't know. I don't do a lot of non-commutative algebra.</p>

#### [ Johannes Hölzl (Jan 22 2019 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644453):
<p>I wouldn't merge it, for the problem Reid mentioned. I think we should restrict <code>opposite</code> to <code>*</code> currently, and see what the actual applications are.</p>

#### [ Kenny Lau (Jan 22 2019 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644457):
<p>there's a heavy lack of consensus on this thread... everyone seems to want different things</p>

#### [ Reid Barton (Jan 22 2019 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644497):
<p>I also have the sense which I can't explain clearly that <code>opposite</code> should be just for multiplication and not addition.</p>

#### [ Mario Carneiro (Jan 22 2019 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644622):
<p>I agree that <code>opposite</code> should not flip both. If necessary we can have <code>add_opposite</code></p>

#### [ Kenny Lau (Jan 22 2019 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644718):
<p>ok, but what about merging opposite and order_dual?</p>

#### [ Kenny Lau (Jan 22 2019 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644744):
<p>and what about irreducible def vs. just def vs. newtype?</p>

#### [ Reid Barton (Jan 22 2019 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644854):
<p>I've just been trying out different options for opposite categories and my impression there is that an irreducible def is the best option, though you could probably make do with other options for algebra because there isn't as heavy use of dependent types there</p>

#### [ Mario Carneiro (Jan 22 2019 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644857):
<p>these all seem like different things</p>

#### [ Mario Carneiro (Jan 22 2019 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644876):
<p>you may want to invert the order without commuting the multiplication, or the addition</p>

#### [ Mario Carneiro (Jan 22 2019 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644888):
<p>they are independent axes</p>

#### [ Mario Carneiro (Jan 22 2019 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644900):
<p>so they should be different constructions</p>

#### [ Mario Carneiro (Jan 22 2019 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644989):
<p>I'm sure there will be various diamond issues like how <code>opposite (order_dual A) != order_dual (opposite A)</code>... I don't have a unified suggestion here</p>

#### [ Mario Carneiro (Jan 22 2019 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156645129):
<p>remind me why newtypes are bad <span class="user-mention" data-user-id="110032">@Reid Barton</span> . refl is overrated</p>

#### [ Mario Carneiro (Jan 22 2019 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156645153):
<p>you should be using simp lemmas anyway in category theory</p>

#### [ Reid Barton (Jan 22 2019 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156645265):
<p>It's really hard to deal with nondefinitional equalities between objects in category theory though.</p>

#### [ Reid Barton (Jan 22 2019 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156645445):
<p>If you define the objects of C^op to be an inductive type/structure, then eventually you have to deal with the fact that a general object of C^op is not definitionally of the form <code>op</code> of something</p>

#### [ Mario Carneiro (Jan 22 2019 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156645580):
<p>isn't that by cases on the objects?</p>

#### [ Mario Carneiro (Jan 22 2019 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156645637):
<p>Or you can state your theorem to only apply to objects of the form <code>op X</code></p>

#### [ Reid Barton (Jan 22 2019 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156645671):
<p>you can't really though, because you need to provide a natural transformation between two functors C^op -&gt; Type or something</p>

#### [ Reid Barton (Jan 22 2019 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156645732):
<p>You could define it using cases on the object but putting that in a definition feels like a bad idea</p>

#### [ Reid Barton (Jan 22 2019 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156645771):
<p>I need to run but later I can prepare a version with irreducible and a version with an inductive type to compare</p>

#### [ Mario Carneiro (Jan 22 2019 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156645789):
<p>In that case you can just use the <code>unop</code> function; the cases happens in the equality proof part</p>

#### [ Reid Barton (Jan 22 2019 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156645860):
<p>Well, this hasn't happened yet but potentially you could need to build something by composing a function ... -&gt; X with a function op (unop X) -&gt; ...</p>

#### [ Mario Carneiro (Jan 22 2019 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156646207):
<p>I guess the categorical formulation of what's going on is that <code>op : C =&gt; C^op</code> is a contravariant functor, and <code>unop</code> is its essential inverse</p>

#### [ Mario Carneiro (Jan 22 2019 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156646226):
<p>so the roundtrip is an iso</p>

#### [ Kenny Lau (Jan 22 2019 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156646280):
<p>but in category theory (at least the way I learnt it), C^op is the category with the same objects as C but <code>Mor[C^op](X,Y) := Mor[C](Y,X)</code></p>

#### [ Mario Carneiro (Jan 22 2019 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156646408):
<p>I mean in category theoretic language, not using material properties of the category</p>

#### [ Mario Carneiro (Jan 22 2019 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156646425):
<p>"the objects of C^op are the objects of C" does not typecheck in category language</p>

#### [ Kenny Lau (Jan 22 2019 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156646501):
<p>I'm not sure how to define C^op using universal properties</p>

#### [ Mario Carneiro (Jan 22 2019 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156646575):
<p>Just like any category language definition, it is defined up to a natural (2-)isomorphism</p>

#### [ Kenny Lau (Jan 22 2019 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156646940):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> what do you think? irreducible def or newtype?</p>

#### [ Johannes Hölzl (Jan 22 2019 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156647057):
<p>I prefer a (ir)reducible def. Or at least a <code>structure</code> with one field instead of a inductive</p>

#### [ Mario Carneiro (Jan 22 2019 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156647129):
<p>I think the "newtype" option is a structure with one field</p>

#### [ Kenny Lau (Jan 22 2019 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156647311):
<p>so... irreducible def it is?</p>

#### [ Mario Carneiro (Jan 22 2019 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156647491):
<p>I think using a newtype is the "purist" approach, and it is workable if you are consistent about it. the (ir)reducible def approach has lower overhead, but lean will not check as much for you - the onus is on you to not misuse the defeqs</p>

#### [ Kenny Lau (Jan 22 2019 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156647738):
<p>well but Reid has more experience on this?</p>

#### [ Mario Carneiro (Jan 22 2019 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156647816):
<p>I'm just saying what the tradeoff is</p>

#### [ Kenny Lau (Jan 23 2019 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156648359):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> are you happy with making it an irreducible def and then afterwards see if it brings any problems?</p>

#### [ Mario Carneiro (Jan 23 2019 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156648373):
<p>I would prefer to just make it a regular def for now</p>

#### [ Mario Carneiro (Jan 23 2019 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156648425):
<p>which is I think the current state of the PR</p>

#### [ Kenny Lau (Jan 23 2019 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156648458):
<p>well it's an inductive type currently</p>

#### [ Kenny Lau (Jan 23 2019 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156648463):
<p>the first version was an irreducible def</p>

#### [ Scott Morrison (Jan 23 2019 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156649703):
<p>Hmm... in the category theory opposites PR it is currently a (normal reducibility) definition. Perhaps Mario was talking about that one.</p>

#### [ Kenny Lau (Jan 23 2019 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156649757):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> what do you think then?</p>

#### [ Scott Morrison (Jan 23 2019 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156649849):
<p>I think the semireducible def seems like a reasonable compromise. I wouldn't go all the way to the inductive type yet, unless we find that we're still finding confusing situations (because Lean is happily accepting things that "aren't quite right").</p>

#### [ Scott Morrison (Jan 23 2019 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156649931):
<p>Certainly making the def irreducible (using a newtype would have had the same benefit) revealed lots of places in the category_theory files where things "weren't quite right". So I appreciate the argument for keeping this level of protection permanently, and this is the argument for using a newtype.</p>

#### [ Kenny Lau (Jan 23 2019 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156650004):
<p>semireducible is the default right?</p>

#### [ Scott Morrison (Jan 23 2019 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156650024):
<p>Yes</p>

#### [ Kenny Lau (Jan 23 2019 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156650101):
<p>done</p>

#### [ Kenny Lau (Jan 23 2019 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156650107):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> do you see any problem with this PR?</p>

#### [ Kenny Lau (Jan 23 2019 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156650116):
<p>Actually I'm not in a hurry; I would rather <a href="https://github.com/leanprover/mathlib/issues/614" target="_blank" title="https://github.com/leanprover/mathlib/issues/614">#614</a> to be merged first</p>

#### [ Reid Barton (Jan 23 2019 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156694975):
<blockquote>
<p>I'm just saying what the tradeoff is</p>
</blockquote>
<p>Indeed this comes down to a tradeoff between conciseness/implicitness/ambiguity and unambiguity/explicitness/verbosity. The best point on the spectrum is I think not something we can deduce by pure thought but have to learn from experience.</p>

#### [ Reid Barton (Jan 23 2019 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156695266):
<p>In category theory, we've had the experience that a plain (semireducible) type can lead to confusion or to difficulty getting Lean to understand what we want to do. Note that the ambiguity can occur in either direction--Lean might not interpret our input as expected but also the types and goals that Lean displays might not mean what we would guess. (For example, it was easy to get into a situation where the goal was <code>X \hom Y</code> but you really needed to supply <code>Y \hom X</code> because the implicit category instance was that of the opposite category.)</p>

#### [ Reid Barton (Jan 23 2019 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156695306):
<p>I don't know whether usages of the "implicit" style for opposites in algebra would run into the same kinds of difficulties.</p>

#### [ Reid Barton (Jan 23 2019 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156695447):
<p>I do like the way <span class="user-mention" data-user-id="110064">@Kenny Lau</span> has set up a mini-API for converting to and from opposites, which should make it easy to try out the different implementation choices (I copied this to try out different designs for opposite categories)</p>


{% endraw %}
