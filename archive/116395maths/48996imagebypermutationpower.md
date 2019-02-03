---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/48996imagebypermutationpower.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [image by permutation power](https://leanprover-community.github.io/archive/116395maths/48996imagebypermutationpower.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Apr 17 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188730):
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">perm</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">g</span> <span class="err">&#39;&#39;</span> <span class="n">U</span>         <span class="c1">-- set α</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">g</span><span class="err">^</span><span class="n">i</span>             <span class="c1">-- perm α</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">g</span><span class="err">^</span><span class="n">i</span> <span class="err">&#39;&#39;</span> <span class="n">U</span>     <span class="c1">-- maximum class-instance resolution depth has been reached</span>
</pre></div>


<p>I tried adding various type annotations and parentheses, getting a variety of error messages but no luck</p>

#### [ Patrick Massot (Apr 17 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188792):
<p>Trying <code>(g^i) '' U</code> is probably a better start</p>

#### [ Patrick Massot (Apr 17 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188794):
<p>But then g is coerced to function too early</p>

#### [ Patrick Massot (Apr 17 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188808):
<p>Is this related to the recent changes to powers?</p>

#### [ Mario Carneiro (Apr 17 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188854):
<p>did you try <code>((g^i:perm α):set α) '' U</code>?</p>

#### [ Kenny Lau (Apr 17 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188856):
<p>but g^i isn't a set</p>

#### [ Patrick Massot (Apr 17 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188901):
<p>He means <code>(g^i : perm α) '' U : set α</code></p>

#### [ Patrick Massot (Apr 17 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188902):
<p>That works indeed</p>

#### [ Mario Carneiro (Apr 17 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188905):
<p>huh. You're right, that's nonsense, but lean is okay with it for some reason</p>

#### [ Patrick Massot (Apr 17 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188915):
<p>Of course I tried <code>(g^i : perm α) '' U</code></p>

#### [ Patrick Massot (Apr 17 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188960):
<p>But didn't think of giving <code>: set α</code> at the end</p>

#### [ Mario Carneiro (Apr 17 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188966):
<p>This is weird. Apparently the second type ascription isn't checked at all, the only important thing is that it's a function type so <code>coe_fn</code> is inserted</p>

#### [ Mario Carneiro (Apr 17 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188968):
<div class="codehilite"><pre><span></span>#check ((g^i:perm α):_ → unit) &#39;&#39; U --ok
</pre></div>

#### [ Patrick Massot (Apr 17 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188969):
<p>At least I can continue. But I'd be interested in a shorter way</p>

#### [ Patrick Massot (Apr 17 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188972):
<p>wow</p>

#### [ Patrick Massot (Apr 17 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188973):
<p>strange</p>

#### [ Patrick Massot (Apr 17 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189026):
<p><code>#check (↑(g^i : perm α)) '' U </code> also works</p>

#### [ Patrick Massot (Apr 17 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189033):
<p><code>#check ↑(g^i) '' U</code> also!</p>

#### [ Mario Carneiro (Apr 17 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189037):
<p><code>#check ⇑(g^i) '' U</code></p>

#### [ Patrick Massot (Apr 17 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189102):
<p>Do you understand what happens?</p>

#### [ Patrick Massot (Apr 17 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189157):
<p>Actually I think it's not so far from stuff we already saw (but without me understanding enough to handle new instances of the problem)</p>

#### [ Mario Carneiro (Apr 17 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189199):
<p>The explicit coercion gives no information to the expected type on the inside, so <code>g^i : _</code> is inferred to <code>g^i : perm A</code> (usually it goes the other way around), so <code>⇑(g^i)</code> gets the coe_fn instance for <code>perm A</code> which is <code>A -&gt; A</code>, and it's simple from then on</p>

#### [ Patrick Massot (Apr 17 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189254):
<p>And what happens when it does not work?</p>

#### [ Patrick Massot (Apr 17 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189263):
<p>I mean when we don't help Lean at all</p>

#### [ Mario Carneiro (Apr 17 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189364):
<p>Without a literal arrow, it first assumes the types match up. So <code>(g^i) '' U : _</code> infers <code>set ?B</code> where <code>g^i : A -&gt; ?B</code> (using <code>U : set A</code>). By the type of <code>^</code> we get <code>g : A -&gt; ?B</code> and <code>i : ?C</code> which solves to <code>i : nat</code> and a coercion is inserted for <code>g</code> so <code>⇑g : A -&gt; A</code>. Finally, it tries to find <code>has_pow (A -&gt; A) nat</code> and no such instance exists.</p>

#### [ Patrick Massot (Apr 17 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189513):
<p>Thanks</p>

#### [ Patrick Massot (Apr 17 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189574):
<p>Would it make any sense to try to define a coercion from <code>perm X</code> to <code>set X -&gt; set X</code> and hope Lean would use that if I write <code>g U</code> or <code>g^i U</code>?</p>

#### [ Mario Carneiro (Apr 17 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189585):
<p>The original instance resolution overflow is due to <code>g^i '' U</code> which by precedence quirks means <code>g ^ (i '' U)</code>; it gets caught in a loop looking for <code>has_coe_to_fun nat</code> for some reason</p>

#### [ Patrick Massot (Apr 17 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189597):
<p>Yes, I understood that bit</p>

#### [ Mario Carneiro (Apr 17 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189642):
<p>No, <code>coe_fn</code> only takes one argument, the domain, unlike <code>coe</code> which has domain and target</p>

#### [ Patrick Massot (Apr 17 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189652):
<p>Not sure why <code>''</code> has higher precedence than <code>^</code> though</p>

#### [ Mario Carneiro (Apr 17 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189653):
<p>so you can only coerce to one kind of function for a given object</p>

#### [ Patrick Massot (Apr 17 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189661):
<p>What about using the general <code>has_coe</code>?</p>

#### [ Mario Carneiro (Apr 17 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189671):
<p>it's way too underdetermined, I think</p>

#### [ Patrick Massot (Apr 17 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189676):
<p>That's what I feared</p>

#### [ Mario Carneiro (Apr 17 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189678):
<p>Any function can be treated as a set function by applying <code>image</code></p>

#### [ Mario Carneiro (Apr 17 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189681):
<p>it's basically just a functor</p>

#### [ Mario Carneiro (Apr 17 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189684):
<p>and there are loads of those</p>

#### [ Kenny Lau (Apr 17 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189686):
<p>I heard functor</p>

#### [ Patrick Massot (Apr 17 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189728):
<p>Even without the perm layer, this <code>f '' U</code> notation is definitely the part of my file that looks further away from usual mathematical notation</p>

#### [ Mario Carneiro (Apr 17 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189741):
<p>I know at least one math book which uses double open quotes as an infix operator for image</p>

#### [ Patrick Massot (Apr 17 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189744):
<p>really?</p>

#### [ Mario Carneiro (Apr 17 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189754):
<p>Takeuti-Zaring Axiomatic Set Theory :P</p>

#### [ Patrick Massot (Apr 17 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189760):
<p>I guess it makes sense to have some kind of specific notation for beginners</p>

#### [ Patrick Massot (Apr 17 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189762):
<p>I see</p>

#### [ Patrick Massot (Apr 17 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189764):
<p>that kind of books</p>

#### [ Mario Carneiro (Apr 17 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189766):
<p>I think it's more about unambiguous notation</p>

#### [ Mario Carneiro (Apr 17 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189767):
<p>it's not a beginners book</p>

#### [ Patrick Massot (Apr 17 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189808):
<p>It seems to be a set theory book</p>

#### [ Patrick Massot (Apr 17 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189814):
<p>of course if you pretend to be serious when you say everything is a set then you need contortions everywhere</p>

#### [ Mario Carneiro (Apr 17 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189821):
<p>Or if you pretend to be serious when you say everything you write is well typed</p>

#### [ Kevin Buzzard (Apr 17 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192260):
<p>This is all (both Patrick's coercion issue and the weird '' notation) part of one underlying problem.</p>

#### [ Kevin Buzzard (Apr 17 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192262):
<p>Mathematicians have developed a really good system for overloading notation</p>

#### [ Kevin Buzzard (Apr 17 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192274):
<p>Patrick is exactly right about '' -- I've never seen it used to mean image so it doesn't surprise me that he hasn't, and it also doesn't surprise me that the only place Mario has is some set theory book (as opposed to what Patrick and I would call mathematics)</p>

#### [ Kevin Buzzard (Apr 17 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192283):
<p>In maths the notation for the image of U under f : X -&gt; Y is of course just f(U)</p>

#### [ Kevin Buzzard (Apr 17 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192284):
<p>but I am well aware that life is not so easy in Lean</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192329):
<p>What the current fix seems to be is this exotic type class system plus clever coercions</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192331):
<p>I must be frank</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192332):
<p>I am not sure that it scales</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192335):
<p>I have seen problems with diamonds</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192337):
<p>I have seen problems with the wrong coercion being chosen</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192343):
<p>so my instinct is to</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192345):
<p>(a) give up type classes to a large extent</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192346):
<p>and (b) to give up on mathematician's overloading</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192353):
<p>With my schemes repo I've not made any attempt to do anything clever like this</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192355):
<p>If F is a sheaf then F is not the function on open sets, it's some other thing</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192358):
<p>and I have F.whatever_i_called_it for the function</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192399):
<p>It looks a bit messier</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192402):
<p>but I am coming round to the idea that it is not the end of the world to actually begin distinguishing between these things</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192413):
<p>In particular if I were writing the code Patrick is writing I simply would not attempt to identify the permutation, the bijection and the function</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192416):
<p>they would all be different notation</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192420):
<p>and I would not moan about ''</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192422):
<p>because f(U) doesn't really make sense</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192424):
<p>The reason for me is a practical one</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192425):
<p>I just want to write code that works</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192465):
<p>so I don't want to get bogged down with all the issues Patrick is running into just to make it look more like mathematics</p>

#### [ Sean Leather (Apr 17 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192471):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I think you should be sure that you're distinguishing between coercion issues and type class issues. I'm not sure they're the same.</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192477):
<p>You're right</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192481):
<p>but in some sense they are both solved by filling in the answers myself</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192482):
<p>and in all cases I know the answers</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192483):
<p>the issue is that they are both issues</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192484):
<p>and I don't want to be dealing with issues</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192485):
<p>and filling in the answers myself resolves them</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192524):
<p>I am very happy with how <code>{ H : blah}</code> works</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192531):
<p>because if I have <code>{U : set X} (OU : is_open U)</code> then Lean is going to be able to guess what U is</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192540):
<p>but I am becoming more and more suspicious of user-added coercions</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192542):
<p>I cannot see a viable way of stopping different users creating loops</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192543):
<p>What if person X and person Y are both interested in widgets and foos</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192545):
<p>but one of them is more widgety</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192556):
<p>and one more fooey</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192594):
<p>so one has some coercion from widgets to foos</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192599):
<p>and the other a coercion from foos to widgets</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192601):
<p>and all of a sudden we have two pieces of incompatible code</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192613):
<p>user-added type class inference I guess I'm talking about here</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192619):
<p>but I am also avoiding has_coe_to_fun</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192663):
<p>and this more cautious approach solved a lot of problems for me</p>

#### [ Sean Leather (Apr 17 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192665):
<p>I agree with what you're saying in a purely practical sense. However, I think it stems in general from Lean using elaboration (esp. but not solely via coercions and type-class instance resolution) to guess what you mean. It gets it right most of the time, but it's those few times that it doesn't that wind up frustrating you.</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192677):
<p>I think that what happened was that in these cases where it didn't work I first got completely stuck</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192678):
<p>and then I learnt how to unravel things in some cases</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192679):
<p>and then I got used to the unravelling</p>

#### [ Kevin Buzzard (Apr 17 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192680):
<p>and then I figured unravelling wasn't so bad</p>

#### [ Patrick Massot (Apr 17 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125193991):
<p>I'm not convinced unraveling everything will scale</p>

#### [ Patrick Massot (Apr 17 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125194000):
<p>And, up to now, I've always been able to solve those kind of issue (well, Mario has always been able...)</p>

#### [ Patrick Massot (Apr 17 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125194004):
<p>And I'm very happy to see how it looks like now</p>

#### [ Patrick Massot (Apr 17 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125194058):
<p>Ok, it's summer here and I have a lot of maths to read. I'll be trying the IHES garden as a working place, without bringing a computer. See you. <span class="emoji emoji-1f60e" title="sunglasses">:sunglasses:</span></p>


{% endraw %}
