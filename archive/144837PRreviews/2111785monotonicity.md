---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/2111785monotonicity.html
---

## Stream: [PR reviews](https://leanprover-community.github.io/archive/144837PRreviews/index.html)
### Topic: [#85 monotonicity](https://leanprover-community.github.io/archive/144837PRreviews/2111785monotonicity.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Simon Hudon (Oct 07 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/135362082):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span>: what is missing on this PR?</p>

#### [ Johan Commelin (Oct 08 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/135399492):
<p>Is it correct that there is some overlap with <code>linarith</code> in use cases? (I'm just trying to get a feel for what this is doing.)</p>

#### [ Simon Hudon (Oct 08 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/135407173):
<p>In the cases where no arithmetic or little arithmetic is involved, yes, that's true. It also works with any relation you want</p>

#### [ Simon Hudon (Oct 08 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/135407285):
<p>The overlap is just enough that if you have a long chain of monotonicity, you don't have to drop <code>mono</code> in the middle to use <code>linarith</code></p>

#### [ Johannes Hölzl (Oct 15 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/135827830):
<p>what I like is that it works with different relations. But I think we want a more general rewrite. Where congruence rules are added in a database for arbitrary relations. And then I just say <code>grw [r1, r2, r3]</code>. maybe even trying to match modulo AC?</p>

#### [ Simon Hudon (Oct 15 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/135839710):
<p>I like the idea but I'm hesitant. One benefit of calling <code>mono</code> directly is that, unlike with rewrite, with orderings, only one direction works.</p>

#### [ Johannes Hölzl (Oct 15 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/135841066):
<p>yes, the relation may not be symmetric, or reflexive or even transitive. And with symmetry for rewrite its only a special case for <code>&lt;- r</code>. For rewriting its more important that the relation is reflexive, and for <code>simp</code> that it is transitive.</p>

#### [ Simon Hudon (Oct 15 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/135841718):
<p>In terms of usability I think it goes further. If you have <code>h : x ≤ y</code> and you want to rewrite <code>a ≤ b - x</code>, only <code>rw &lt;- h</code> is available.</p>

#### [ Johannes Hölzl (Oct 15 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/135843736):
<p>This works with generalized rewriting. The congruence rules would be:</p>
<div class="codehilite"><pre><span></span>((≥) ⇒ (≤) ⇒ (→)) (≤) (≤)
i.e. a&#39; ≥ a → b&#39; ≤ b → (a&#39; ≤ b&#39; → a ≤ b)

((≤) ⇒ (≥) ⇒ (≤)) (-) (-)
i.e. a&#39; ≤ a → b&#39; ≥ b → (a&#39; - b&#39; ≤ a - b)
</pre></div>

#### [ Johannes Hölzl (Oct 15 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/135843793):
<p>So the <code>&lt;- h</code> translates to a flip of the actual relation.</p>

#### [ Johannes Hölzl (Oct 15 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/135843955):
<p>This is by the way how <code>transfer</code> works, just that it doesn't apply a rewrite step, but tries to build up the relation proof exhaustively (hoping that it has rules for all constants and variables)</p>

#### [ Simon Hudon (Oct 15 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/135852211):
<p>I like the idea. It is quite a bit different from what I implemented and I would rather do it as a separate project</p>

#### [ Simon Hudon (Oct 16 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/135925544):
<p>Survery: do you (the reviewers) prefer for the attribute to be named <code>monotonic</code> or <code>mono</code>?</p>

#### [ Scott Morrison (Oct 17 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/135949962):
<p><code>monotonic</code> (on the unpopular principle that abbreviations are always a bad idea)</p>

#### [ Simon Hudon (Oct 17 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/135950021):
<p>The tactic's name is <code>mono</code> though so do you think it's also a bad idea?</p>

#### [ Johannes Hölzl (Oct 17 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/135953945):
<p>if possible the tactic and attribute should have the same name. I prefer <code>mono</code> over <code>monotonicity</code> due to its length, and for me <code>mono</code> is clearly <code>monotonicity</code></p>

#### [ Scott Morrison (Oct 17 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136001257):
<p>monotone, monomorphism, monoid, monomial, monopole</p>

#### [ Mario Carneiro (Oct 17 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136001322):
<p>I vote <code>mono</code>. The shorter the name of a tactic is, the more awesome it sounds</p>

#### [ Scott Morrison (Oct 17 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136001332):
<p>... but I have never understood the desire to abbreviate (or rather, I think I understand the stated desire, to require fewer keystrokes and to fit more content per pixel, but don't think it's a valuable outcome)</p>

#### [ Scott Morrison (Oct 17 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136001335):
<p>I'd prefer things to be clear, rather than just clear from context.</p>

#### [ Mario Carneiro (Oct 17 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136001366):
<p>tactics with short and cryptic names like <code>omega</code> and <code>auto</code> seem to be quite popular</p>

#### [ Mario Carneiro (Oct 17 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136001385):
<p>it makes them more "name-like" rather than "decription-like"</p>

#### [ Scott Morrison (Oct 17 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136001433):
<p>but that is because they are useful!</p>

#### [ Mario Carneiro (Oct 17 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136001437):
<p>as in "use the mono tactic" rather than "use the tactic that does monotonicity reasoning"</p>

#### [ Scott Morrison (Oct 17 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136001470):
<p><code>/- the result now follows -/ by monotonicity</code></p>

#### [ Scott Morrison (Oct 17 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136001492):
<p>But again, I understand that no one is interested at this point in writing literate proofs.</p>

#### [ Simon Hudon (Oct 17 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136001539):
<blockquote>
<p>But again, I understand that no one is interested at this point in writing literate proofs.</p>
</blockquote>
<p>Why do you believe that?</p>

#### [ Mario Carneiro (Oct 17 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136001545):
<p>No, I mean literally name like, as in Joe or Sue</p>

#### [ Mario Carneiro (Oct 17 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136001560):
<p>I think it makes the language more colourful</p>

#### [ Mario Carneiro (Oct 17 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136001613):
<p>because I don't think you should take too seriously the "description-like" aspect of a tactic name anyway</p>

#### [ Mario Carneiro (Oct 17 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136001690):
<p>for a given tactic you will usually want to know exactly what it does and the description itself always falls short</p>

#### [ Scott Morrison (Oct 17 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136001694):
<p>I do appreciate this point.</p>

#### [ Mario Carneiro (Oct 17 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136001707):
<p>if it's just a name, then you just get used to the foibles of that tactic</p>

#### [ Scott Morrison (Oct 17 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136001725):
<blockquote>
<blockquote>
<p>But again, I understand that no one is interested at this point in writing literate proofs.</p>
</blockquote>
<p>Why do you believe that?</p>
</blockquote>
<p>Because I've never seen anyone try to write one? I considered trying to make the proof of the infinitude of primes in mathlib 'literate', but went on to other things.</p>

#### [ Mario Carneiro (Oct 17 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136001734):
<p>looks like Neil beat you to it</p>

#### [ Scott Morrison (Oct 17 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136001739):
<p>Oh, I didn't see.</p>

#### [ Mario Carneiro (Oct 17 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136001741):
<p><a href="http://neil-strickland.staff.shef.ac.uk/dagstuhl/Systems/Lean_mathlib/Tasks/primes/" target="_blank" title="http://neil-strickland.staff.shef.ac.uk/dagstuhl/Systems/Lean_mathlib/Tasks/primes/">http://neil-strickland.staff.shef.ac.uk/dagstuhl/Systems/Lean_mathlib/Tasks/primes/</a></p>

#### [ Mario Carneiro (Oct 17 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136001789):
<p>I would like to see what you would add or change, you've done a few presentations with this proof now</p>

#### [ Scott Morrison (Oct 17 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136001827):
<p>Well, I think it's important to have everything in a single text file, even if there are tools to extract "human" and "cryptic Lean" available.</p>

#### [ Mario Carneiro (Oct 17 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136001994):
<p>it looks like neil invented his own version of coqdoc, with popout text</p>

#### [ Scott Morrison (Oct 17 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136002240):
<p>I would hope that from same text file that we produce the <code>olean</code> file, we can also extract the following text:</p>
<blockquote>
<p>We take p to be the smallest prime factor of N!+1.</p>
<p>First, we need to show that p is prime; this is immediate from the definition of the smallest prime factor, as long as we know that N!+1 is greater than one. (This follows since N! is at least one, so N!+1 is greater than one.)</p>
<p>Next we show that p &gt; N. We prove this by contradiction, so we assume p &lt;= N. We observe that p | N! + 1, and p | N!. The first follows since p was chosen as a prime factor of N!+1. The second follows as 1 &lt;= p &lt;= N, and any such number divides N!. Combining these two facts, we have that p | 1. (This is just the fact that if n | a and n | a+b, then n | b.) We showed earlier that a prime cannot divide one, giving the desired contradiction.</p>
</blockquote>
<p>I think this text very faithfully follows the proof given in mathlib.</p>

#### [ Scott Morrison (Oct 17 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136002251):
<p>Now, it is unclear to me whether that text should appear in the <code>lean</code> file.</p>

#### [ Scott Morrison (Oct 17 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136002261):
<p>But if it doesn't, that's only because we'd have written some tool that could _generate_ that text from the Lean source.</p>

#### [ Scott Morrison (Oct 17 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136002307):
<p>Generating an approximation of that text is not at all crazy, I think.</p>

#### [ Mario Carneiro (Oct 17 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136002407):
<p>that text is in the lean file</p>

#### [ Scott Morrison (Oct 17 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136002413):
<p>Even better would be that that text is what appears in the Lean file, and the "lean source" is extracted from it ...</p>

#### [ Scott Morrison (Oct 17 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136002421):
<p>What do you mean?</p>

#### [ Mario Carneiro (Oct 17 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136002434):
<p>click on the show raw text button</p>

#### [ Scott Morrison (Oct 17 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136002577):
<p>Okay, yes, I understand. It's great that Neil has written a prototype tool for <code>leandoc</code>. Now we need to think about what lean sources should look like with <code>leandoc</code> available.</p>

#### [ Scott Morrison (Oct 17 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136002593):
<p>Obviously they should not have html in the comments, but markdown.</p>

#### [ Scott Morrison (Oct 17 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136002614):
<p>But maybe what Neil has written is an excellent start.</p>

#### [ Simon Hudon (Oct 18 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%2385%20monotonicity/near/136045229):
<p>On the subject of <code>mono</code>, do we agree that if the tactic is called <code>mono</code>, <code>mono</code> is also a good name for the attribute?</p>


{% endraw %}
