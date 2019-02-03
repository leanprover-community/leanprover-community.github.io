---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/35885finsetsum.html
---

## Stream: [general](index.html)
### Topic: [finset.sum](35885finsetsum.html)

---


{% raw %}
#### [ Morenikeji Neri (Aug 06 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130977419):
<p>I'm having some trouble proving this. Help would be much appreciated.<br>
<code>lean lemma sum_keji {α β : Type*} [add_comm_monoid α] {f : β → α}
  (s : finset β) (g : Π a ∈ s, β) (h₁ : ∀ a ha, f a + f (g a ha) = 0)
  (h₂ : ∀ a ha, g a ha ≠ a) (h₂ : ∀ a₁ a₂ ha₁ ha₂, g a₁ ha₁ = g a₂ ha₂ → a₁ = a₂)
  (h₃ : ∀ a ha, ∃ b hb, g b hb = a) : s.sum f = 0 := sorry </code></p>

#### [ Mario Carneiro (Aug 06 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130979862):
<p>I guess you should first prove <code>g a ha ∈ s</code> using the pigeonhole principle</p>

#### [ Mario Carneiro (Aug 06 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130979907):
<p>then the assumptions say that <code>g : s -&gt; s</code> is a bijection, so you can use <code>sum_bij</code> to shift things around and cancel using <code>h1</code></p>

#### [ Mario Carneiro (Aug 06 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130979982):
<p>Oh wait, you only have that it is an <code>add_comm_monoid</code>, that's not enough to conclude</p>

#### [ Mario Carneiro (Aug 06 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130979991):
<p>you will be able to prove <code>s.sum f + s.sum f = 0</code></p>

#### [ Mario Carneiro (Aug 06 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130980256):
<p>So for example if <code>α = Z/2Z</code>, <code>β=Z/3Z</code>, <code>s={0,1,2}</code>, <code>f a = 1</code> and <code>g n = n+1</code> then we have a counterexample</p>

#### [ Morenikeji Neri (Aug 06 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130982346):
<p>sorry about that. I realized I missed out a few assumptions in the theorem.<br>
It should read.</p>
<p><code>lean lemma sum_keji {α β : Type*} [add_comm_monoid α] {f : β → α}
  (s : finset β) (g : Π a ∈ s, β) (h₁ : ∀ a ha, f a + f (g a ha) = 0)
  (h₂ : ∀ a ha, g a ha ≠ a) (h₂ : ∀ a₁ a₂ ha₁ ha₂, g a₁ ha₁ = g a₂ ha₂ → a₁ = a₂)
  (h₃ : ∀ a ha, ∃ b hb, g b hb = a) (h₄ : ∀ a ha, g a ha ∈ s) (h₅ : ∀ a ha, g (g a ha) (h₄ a ha) = a ) : s.sum f = 0 := sorry </code></p>

#### [ Mario Carneiro (Aug 06 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130982614):
<p>Oh I see, it's an involution</p>

#### [ Mario Carneiro (Aug 06 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130982654):
<p>You can prove this by complete induction on <code>s</code>. Just take out <code>a</code> and <code>g a ha</code> in one step of the induction</p>

#### [ Chris Hughes (Aug 06 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130982680):
<p>Is there a short proof using lemmas?</p>

#### [ Mario Carneiro (Aug 06 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130982691):
<p>not with those hypotheses</p>

#### [ Mario Carneiro (Aug 06 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130982711):
<p>half of the work will be unpacking them</p>

#### [ Mario Carneiro (Aug 06 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130982788):
<p>I mean, the stuff about <code>sum</code> is there but most of the work is showing that the reduced <code>g</code> function is still an involution</p>

#### [ Morenikeji Neri (Aug 06 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/130982854):
<p>yep!</p>

#### [ Scott Morrison (Nov 24 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271569):
<p>Okay... after way too many inequalities (thanks, everyone!), I now have "the right" proof that $\sum_m \binom n m = 2^n$, based on reindexing sums and splitting off and joining single terms. This uses the following four lemmas:</p>
<div class="codehilite"><pre><span></span>lemma finset.sum.interval_split_left (n m : ℕ) (h₁ : n &lt; m) (f : ℕ → β) :
(interval n m).sum f = f n + (interval (n+1) m).sum f :=

lemma finset.sum.interval_split_right (n m : ℕ) (h : m &gt; n) (f : ℕ → β) :
(interval n m).sum f = (interval n (m-1)).sum f + f (m-1) :=

lemma finset.sum.interval_reindex_left (k n m : ℕ) (h : k ≤ n) (f : ℕ → β) :
(interval n m).sum f = (interval (n-k) (m-k)).sum (λ x, f (x + k)) :=

lemma finset.sum.interval_reindex_right (k n m : ℕ) (f : ℕ → β) :
(interval n m).sum f = (interval (n+k) (m+k)).sum (λ x, f (x - k)) :=
</pre></div>


<p>which I've proved (and some infrastructure for <code>interval</code>).</p>

#### [ Scott Morrison (Nov 24 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271613):
<p>The proofs still need a lot of golfing, but I think it's progress.</p>

#### [ Scott Morrison (Nov 24 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271669):
<p>I would like to write some tactics to help with this, so you can just write things like "reindex_sum +3" in tactic mode, and it will <code>conv</code> it's way to the first <code>(interval n m).sum f</code>, and replace it with <code>(interval (n+3) (m+3)).sum (\lambda x, f (x-3))</code>, etc.</p>

#### [ Kevin Buzzard (Nov 24 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271672):
<p>Now on to multinomial coefficients!</p>

#### [ Scott Morrison (Nov 24 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271675):
<p>I'd also like to write a <code>conv</code> tactic for rewriting inside the summand of a <code>finset.sum</code>, that gives you a hypothesis saying you're actually in the domain.</p>

#### [ Scott Morrison (Nov 24 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271831):
<p>If I'm going to clean this up for a PR, where should it go? In <code>big_operators.lean</code>? Or start a new file for summations over intervals in <code>nat</code>?</p>

#### [ Mario Carneiro (Nov 24 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271914):
<p>I think a file for summations over intervals is appropriate</p>

#### [ Mario Carneiro (Nov 24 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271960):
<p>I think the name should be <code>finset.Icc</code> though</p>

#### [ Mario Carneiro (Nov 24 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271964):
<p>thiat gives us plenty of room for future variation</p>

#### [ Mario Carneiro (Nov 24 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271969):
<p>er, <code>Ico</code>?</p>

#### [ Scott Morrison (Nov 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271987):
<p>does that stand for "interval closed open"?</p>

#### [ Scott Morrison (Nov 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271989):
<p>okay</p>

#### [ Mario Carneiro (Nov 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148271995):
<p>yeah, for compatibility with <code>set.Ico</code></p>

#### [ Scott Morrison (Nov 24 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272044):
<p>how about when I define <code>Ico</code> as a list/multiset/finset? Should those go in those three files, or in the file about summations over intervals?</p>

#### [ Mario Carneiro (Nov 24 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272047):
<p>they can all be in the same file, I think</p>

#### [ Scott Morrison (Nov 24 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272061):
<p>excellent, that means I can safely use tactics :-)</p>

#### [ Mario Carneiro (Nov 24 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272065):
<p>oh, you mean the definitions themselves</p>

#### [ Scott Morrison (Nov 24 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272069):
<p>yes...</p>

#### [ Mario Carneiro (Nov 24 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272071):
<p>I guess they could go near <code>finset.range</code></p>

#### [ Mario Carneiro (Nov 24 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272079):
<p>but the development should go in its own file</p>

#### [ Mario Carneiro (Nov 24 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272119):
<p>especially stuff combining sums and these sets</p>

#### [ Scott Morrison (Nov 24 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272126):
<p>okay, that's what I've done so far --- in fact put them next to <code>list.range'</code>, <code>multiset.range</code>, and <code>finset.range</code>, and then the actual lemmas about dealing with <code>(Ico n m).sum</code> are in their own file.</p>

#### [ Mario Carneiro (Nov 24 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272130):
<p>great</p>

#### [ Scott Morrison (Nov 24 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272164):
<p>a few lemmas about slicing and dicing intervals use <code>tidy</code> to blast through... those proofs will have to be rewritten if they are going to live in <code>finset.lean</code> or earlier.</p>

#### [ Scott Morrison (Nov 24 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272167):
<p>oh well...</p>

#### [ Scott Morrison (Nov 24 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272211):
<p>(Not having <code>work_on_goal</code> available will make me cry, as it means I'll actually have to restructure the proofs <code>tidy</code> outputs.)</p>

#### [ Mario Carneiro (Nov 24 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272241):
<p>oh no, structured proof</p>

#### [ Scott Morrison (Nov 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272346):
<p>don't hold your breath :-) This PR is going to have some low-quality tactic proofs, that get the job done.</p>

#### [ Scott Morrison (Nov 24 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272542):
<p>On the subject, if anyone wants to suggest to me some nice examples of proofs that rely on re-indexing and slicing and dicing sums, please do!</p>

#### [ Mario Carneiro (Nov 24 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272764):
<p>you should look at <code>exp_add</code></p>

#### [ Mario Carneiro (Nov 24 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148272770):
<p>and possibly quadratic reciprocity</p>

#### [ Patrick Massot (Nov 24 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273678):
<p>Seriously guys, what's wrong with you? What the fuck is this thread?</p>

#### [ Patrick Massot (Nov 24 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273733):
<p>I really think this proof assistant thing is going nowhere if we keep working like this, ignoring everything done by other people, including the ones who proved they can do much more than what we can currently do</p>

#### [ Patrick Massot (Nov 24 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273831):
<p>I've pointed out repeatedly the existence of mathcomp's bigop library. They figured out all the issues, and they use it in linear algebra, in calculus, in finite group theory... I said it would very important to try to port that library to mathlib. Nobody cared. I started trying to do it, nobody cared. I struggled with nat substraction so I gave up for now. Then suddenly Scott asks many nat substraction questions, and, guess what, he is doing big operators again.</p>

#### [ Mario Carneiro (Nov 24 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273841):
<p>The point is to see if our new techniques help with the proofs</p>

#### [ Patrick Massot (Nov 24 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273846):
<p>I think the point is people thinking they are smarter than Gonthier and his friends</p>

#### [ Mario Carneiro (Nov 24 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273888):
<p>if you get ahead of yourself writing theorems before the automation or appropriate structures and idioms come you get a load of unmaintainable hackery</p>

#### [ Mario Carneiro (Nov 24 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273891):
<p>I'm afraid I can't read any of gonthier's proofs</p>

#### [ Patrick Massot (Nov 24 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273892):
<p>Then why don't you ask?</p>

#### [ Mario Carneiro (Nov 24 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273899):
<p>I highly respect him and I know he has a method to the madness but ssreflect style is not something I want to teach</p>

#### [ Patrick Massot (Nov 24 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273900):
<p>We have Assia and Cyril who can read them, and explain everything</p>

#### [ Patrick Massot (Nov 24 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273905):
<p>And they are really puzzled by our attitude</p>

#### [ Patrick Massot (Nov 24 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273906):
<p>It has nothing to do with SSReflect crazyness</p>

#### [ Patrick Massot (Nov 24 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273981):
<p>They thought about what are the right data structures, how to formulate the right induction principles for big operators, in what order to prove stuff</p>

#### [ Patrick Massot (Nov 24 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273983):
<p>And it <em>works</em></p>

#### [ Mario Carneiro (Nov 24 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148273995):
<p>sure, that's valuable</p>

#### [ Mario Carneiro (Nov 24 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274000):
<p>it's the reason I periodically bring up metamath here, because many of our new problems are old problems somewhere else</p>

#### [ Mario Carneiro (Nov 24 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274002):
<p>but I can't help that my experience is in metamath, not coq</p>

#### [ Mario Carneiro (Nov 24 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274061):
<p>to get good information about how to do stuff in coq we would need Assia or Cyril guiding the path, and they have better things to do</p>

#### [ Patrick Massot (Nov 24 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274071):
<p>What about letting them decide whether they have better things to do?</p>

#### [ Patrick Massot (Nov 24 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274078):
<p>They both repeatedly offered to help us understand what's in mathcomp</p>

#### [ Mario Carneiro (Nov 24 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274122):
<p>of course, if they actually think that's a good idea I'm all ears, that's not a rejection at all</p>

#### [ Mario Carneiro (Nov 24 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274127):
<p>but in my view it's one more idea on the table, which can be considered equally among others</p>

#### [ Patrick Massot (Nov 24 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274133):
<p>And what about trying to work together? <span class="user-mention" data-user-id="110087">@Scott Morrison</span> could you publicly write why you chose to restart from scratch instead of helping me in my attempt?</p>

#### [ Mario Carneiro (Nov 24 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274135):
<p>I don't think we should blindly port any specific library</p>

#### [ Patrick Massot (Nov 24 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274179):
<p>I'm not saying we should blindly do anything. Quite the contrary, I'm suggesting to open our eyes to the existing stuff</p>

#### [ Mario Carneiro (Nov 24 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274182):
<p>are you referring to the notation for filtered sums of nats?</p>

#### [ Patrick Massot (Nov 24 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274195):
<p>I don't think Lean would be there is Leo had the same attitude with existing software. And it doesn't mean Lean is "blindly ported"</p>

#### [ Patrick Massot (Nov 24 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274243):
<p>It's not only about notations, I proved many lemmas in <a href="https://github.com/PatrickMassot/bigop/blob/master/src/bigop.lean" target="_blank" title="https://github.com/PatrickMassot/bigop/blob/master/src/bigop.lean">https://github.com/PatrickMassot/bigop/blob/master/src/bigop.lean</a>. I know some stuff should be rethought, and everything could be improved, but why not starting there?</p>

#### [ Mario Carneiro (Nov 24 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274272):
<p>one could ask the same of that approach... try it on <code>exp_sum</code>, try it on quadratic reciprocity, see if it helps</p>

#### [ Mario Carneiro (Nov 24 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274322):
<p>this is not in any way a loaded question, it's a test bed for new ideas</p>

#### [ Mario Carneiro (Nov 24 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274332):
<p>if it's a good approach, the proof will reflect that</p>

#### [ Mario Carneiro (Nov 24 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274352):
<p>I don't know if scott's <code>Ico</code> will make things better than just using <code>range</code>, we need more data</p>

#### [ Patrick Massot (Nov 24 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148274361):
<p>It's lunch time, and this conversation is going nowhere anyway. Bye</p>

#### [ Kevin Buzzard (Nov 24 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275683):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> do you have any comments on this? I remember a couple of times over the summer you saying you were having to battle with finite sums. What did you feel was missing from the library? Maybe it's time to compile a wishlist instead of all writing our own workarounds. Last year I wrote <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msubsup><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></msubsup><msub><mi>a</mi><mi>i</mi></msub><mo>=</mo><msubsup><mo>∑</mo><mrow><mi>j</mi><mo>=</mo><mn>1</mn></mrow><mi>n</mi></msubsup><msub><mi>a</mi><mrow><mi>n</mi><mo>+</mo><mn>1</mn><mo>−</mo><mi>j</mi></mrow></msub></mrow><annotation encoding="application/x-tex">\sum_{i=1}^na_i=\sum_{j=1}^na_{n+1-j}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.804292em;"></span><span class="strut bottom" style="height:1.24011em;vertical-align:-0.43581800000000004em;"></span><span class="base"><span class="mop"><span class="mop op-symbol small-op" style="position:relative;top:-0.0000050000000000050004em;">∑</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.804292em;"><span style="top:-2.40029em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">i</span><span class="mrel mtight">=</span><span class="mord mathrm mtight">1</span></span></span></span><span style="top:-3.2029em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.29971000000000003em;"></span></span></span></span></span><span class="mord"><span class="mord mathit">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mrel">=</span><span class="mop"><span class="mop op-symbol small-op" style="position:relative;top:-0.0000050000000000050004em;">∑</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.804292em;"><span style="top:-2.40029em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight" style="margin-right:0.05724em;">j</span><span class="mrel mtight">=</span><span class="mord mathrm mtight">1</span></span></span></span><span style="top:-3.2029em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.43581800000000004em;"></span></span></span></span></span><span class="mord"><span class="mord mathit">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.311664em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">n</span><span class="mbin mtight">+</span><span class="mord mathrm mtight">1</span><span class="mbin mtight">−</span><span class="mord mathit mtight" style="margin-right:0.05724em;">j</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span></span></span></span> because I needed it for an example sheet question, and I remember it being a real pain.</p>

#### [ Mario Carneiro (Nov 24 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275731):
<p>My impression of nat subtraction is it's best to avoid it appearing in lemmas to start with</p>

#### [ Kevin Buzzard (Nov 24 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275732):
<p>Well it's in my lemma :-/</p>

#### [ Kevin Buzzard (Nov 24 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275737):
<p>oh I see what you mean</p>

#### [ Mario Carneiro (Nov 24 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275776):
<p>I wonder how much mileage you can get out of <code>finset.diag : finset (nat x nat) := {(0, n), ..., (n, 0)}</code></p>

#### [ Kevin Buzzard (Nov 24 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275788):
<p>you want me to prove that the function sending i to n+1-i is a bijection and then have some lemma about summing over a bijection, which actually might be in there already I guess. Is it?</p>

#### [ Chris Hughes (Nov 24 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275794):
<p>I want to be able to sum between integers and naturals, and also do non commutative products over arbitrary lists. I think Patrick's approach seems to unify all these things nicely.</p>

#### [ Chris Hughes (Nov 24 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275801):
<p><code>sum_bij</code> is the lemma</p>

#### [ Mario Carneiro (Nov 24 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275810):
<blockquote>
<p>the function sending i to n+1-i is</p>
</blockquote>
<p>nope, you said minus</p>

#### [ Mario Carneiro (Nov 24 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275854):
<p>the goal is to state the whole theorem without using minus</p>

#### [ Kevin Buzzard (Nov 24 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275855):
<p>But I literally needed to prove that the sum of <code>F i</code> was equal to the sum of <code>F (n + 1 - i)</code></p>

#### [ Mario Carneiro (Nov 24 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275856):
<p><code>finset.diag.map swap = finset.diag.reverse</code></p>

#### [ Mario Carneiro (Nov 24 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275859):
<p>no minus</p>

#### [ Mario Carneiro (Nov 24 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275861):
<p>and <code>swap</code> is a bijection, etc etc</p>

#### [ Kevin Buzzard (Nov 24 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275873):
<p>If I set as an example sheet question <code>binom n m = binom n (n - m)</code> you can't now avoid the minus. Are you suggesting that binom should take integer coefficients?</p>

#### [ Mario Carneiro (Nov 24 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275878):
<p>if it's literally the input statement, then you should apply a lemma to get rid of it first, and work with that</p>

#### [ Kevin Buzzard (Nov 24 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275924):
<p>so what lemma gets me rid of <code>n - m</code> in my input statement? :-/</p>

#### [ Mario Carneiro (Nov 24 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275926):
<p><code>binom n i = binom n j</code> when <code>i + j = n</code></p>

#### [ Kevin Buzzard (Nov 24 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275927):
<p><em>boggle</em></p>

#### [ Mario Carneiro (Nov 24 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275929):
<p>aka <code>(i, j) in finset.diag</code></p>

#### [ Mario Carneiro (Nov 24 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275990):
<p>inductions go through so much more smoothly when there is no break in the function</p>

#### [ Kevin Buzzard (Nov 24 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275996):
<p>My theorem isn't even true when <code>m &gt; n</code></p>

#### [ Mario Carneiro (Nov 24 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148275999):
<p>my theorem can't even have m &gt; n</p>

#### [ Kevin Buzzard (Nov 24 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148276005):
<p>right</p>

#### [ Mario Carneiro (Nov 24 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148276016):
<p>of course you can substitute in <code>n</code> in that statement, and then it's an easy induction on i,j</p>

#### [ Mario Carneiro (Nov 24 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148276062):
<p>in general you might also want to generalize i,j and do induction on n, or something related</p>

#### [ Kevin Buzzard (Nov 24 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148276073):
<p>So one way of proving <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>s</mi><mo>:</mo><mrow><mi mathvariant="double-struck">Z</mi></mrow><mo>:</mo><mo>=</mo><msubsup><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>0</mn></mrow><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow></msubsup><mo>(</mo><mo>−</mo><mn>1</mn><msup><mo>)</mo><mi>i</mi></msup><mrow><mo fence="true">(</mo><mfrac linethickness="0px"><mrow><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn></mrow><mrow><mi>i</mi></mrow></mfrac><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">s : \mathbb{Z} :=\sum_{i=0}^{2n+1}(-1)^i\binom{2n+1}{i}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.954008em;"></span><span class="strut bottom" style="height:1.304018em;vertical-align:-0.35001em;"></span><span class="base"><span class="mord mathit">s</span><span class="mrel">:</span><span class="mord"><span class="mord mathbb">Z</span></span><span class="mrel">:</span><span class="mrel">=</span><span class="mop"><span class="mop op-symbol small-op" style="position:relative;top:-0.0000050000000000050004em;">∑</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.954008em;"><span style="top:-2.40029em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">i</span><span class="mrel mtight">=</span><span class="mord mathrm mtight">0</span></span></span></span><span style="top:-3.2029em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">2</span><span class="mord mathit mtight">n</span><span class="mbin mtight">+</span><span class="mord mathrm mtight">1</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.29971000000000003em;"></span></span></span></span></span><span class="mopen">(</span><span class="mord">−</span><span class="mord mathrm">1</span><span class="mclose"><span class="mclose">)</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.824664em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span></span></span></span></span><span class="mord"><span class="mopen delimcenter" style="top:0em;"><span class="delimsizing size1">(</span></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.8951079999999999em;"><span style="top:-2.3550000000000004em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">i</span></span></span></span><span style="top:-3.144em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">2</span><span class="mord mathit mtight">n</span><span class="mbin mtight">+</span><span class="mord mathrm mtight">1</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.345em;"></span></span></span></span><span class="mclose delimcenter" style="top:0em;"><span class="delimsizing size1">)</span></span></span></span></span></span> is 0 is to set <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>j</mi><mo>=</mo><mn>2</mn><mi>n</mi><mo>+</mo><mn>1</mn><mo>−</mo><mi>i</mi></mrow><annotation encoding="application/x-tex">j=2n+1-i</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.65952em;"></span><span class="strut bottom" style="height:0.85396em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05724em;">j</span><span class="mrel">=</span><span class="mord mathrm">2</span><span class="mord mathit">n</span><span class="mbin">+</span><span class="mord mathrm">1</span><span class="mbin">−</span><span class="mord mathit">i</span></span></span></span> and note that this substitution proves that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>s</mi><mo>=</mo><mo>−</mo><mi>s</mi></mrow><annotation encoding="application/x-tex">s=-s</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.58333em;"></span><span class="strut bottom" style="height:0.66666em;vertical-align:-0.08333em;"></span><span class="base"><span class="mord mathit">s</span><span class="mrel">=</span><span class="mord">−</span><span class="mord mathit">s</span></span></span></span>. You would do all this without any nat subtraction?</p>

#### [ Scott Morrison (Nov 24 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148287845):
<blockquote>
<p>@Scott Morrison could you publicly write why you chose to restart from scratch instead of helping me in my attempt?</p>
</blockquote>
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span>, my apologies if it appeared that I was intentionally ignoring your work at &lt;<a href="https://github.com/PatrickMassot/bigop/blob/master/src/bigop.lean" target="_blank" title="https://github.com/PatrickMassot/bigop/blob/master/src/bigop.lean">https://github.com/PatrickMassot/bigop/blob/master/src/bigop.lean</a>&gt;. In fact I didn't even know that it existed. I remember looking at the top of <code>big_operators.lean</code> and thinking "huh, that's funny, Patrick's name isn't in the <code>Authors</code> line, I thought he helped write this file". But that was the extent of my memory of what you'd done. :-(</p>
<p>I'd be very happy to discuss what you wrote already and to make some plans about how to proceed.</p>
<p>Right now I need to go out for a while, but I'll look more closely at your repo soon. There is a lot there, and I see that working over <code>int</code> rather than <code>nat</code> index sets makes life easier. However I don't much like that you've "rolled your own" subsets built into your <code>bigop</code> notation, containing both a <code>list I</code> and an <code>I -&gt; Prop</code>, rather than using existing technology (e.g. <code>multiset</code>, and <code>filter</code>). I think it's best if we decouple as much as possible here.</p>

#### [ Scott Morrison (Nov 25 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148294592):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span>, moreover, I will attempt to read the big operators paper. :-)</p>

#### [ Scott Morrison (Nov 25 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148294612):
<p>I see already that your <code>list I</code> and <code>I -&gt; Prop</code> is imitating what they do, although my limited understanding so far is that they do something more general than <code>list I</code>.</p>

#### [ Patrick Massot (Nov 25 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148294656):
<p>I just came back from the hospital after some climbing session, so I didn't see your message earlier</p>

#### [ Patrick Massot (Nov 25 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148294663):
<p>I'm sorry I was so upset this morning, but I'm really tired of these problems.</p>

#### [ Patrick Massot (Nov 25 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148294712):
<p>I didn't "roll my own subset" rather using filter, everything is based on filter. The question is the interface question, and this is precisely the kind of question where I think it makes sense to have a look at what mathcomp successfully used</p>

#### [ Patrick Massot (Nov 25 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148294783):
<p>I moved from nat to int mostly because of nat substraction hell, but also because sums indexed by integers do arise, for instance with Fourier series</p>

#### [ Scott Morrison (Nov 25 2018 at 04:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148302363):
<p>Okay, a few disorganised thoughts post bike-ride:<br>
1) While I absolutely agree that we want "generic operation" big operations, I mostly wanted to explore writing useful tactics for manipulating big operations, and thought that testing this out more narrowly (just with <code>finset.sum</code> at first) would be helpful.</p>
<p>2) The sort of tactics I have in mind are: <code>shift 5</code> (and <code>shift -2</code>, and <code>shift_left</code>, etc.), <code>split_first</code>, <code>split_at</code>, etc, and very importantly making it possible to <code>conv</code> your way inside the summand, and be given a hypothesis that you're in the domain, so you can perform appropriate conditional rewrites. There are many more tactics suitable for multivariable big operations, changing between int and nat, etc. (Does the Coq library provide tactic level support?)</p>
<p>3) I feel pretty dubious about the Coq model where there is apparently a multiset, and a filter, being carried around in the notation. It then seems there are two places we can add an extra filter: on the actual multiset, and composed with the filter. There's then an extra dimension worth of rewriting to move the filters back on forth. Why cause yourself that trouble? (I still haven't read the Coq paper -- so this question is perhaps an invitation for someone to point me to a relevant comment.)</p>
<p>4) In Patrick's prototype, I think there's a real semantic problem with using a <code>list I</code> and a <code>I -&gt; Prop</code>. What is the meaning of repeated elements in the list? Presumably that we're summing with multiplicity. What is the meaning of the order of the list? It's strange that the filter removes all copies of some element --- surely you want to be able to control multiplicities directly if you're summing with multiplicity? I suspect here that the answer is just to change from <code>list I</code> to <code>finset I</code>.</p>
<p>5) A more fundamental objection to following the Coq approach is indexing by the binary operation, rather than the carrier type, is completely alien to the rest of the design in Lean. Pursuing this for a big operators library seems likely to cause of lot of friction. In their paper (okay, I've now read the first 3 pages) they say they don't want to index by the carrier type because of course there is more than one relevant operation we want bigops for, for a single type (their example is nat, with +,*, max, min, lcm, gcd, and so on). I think this is actually an easy problem to solve, that we've solved elsewhere in mathlib by "wrapper types", and providing alternative instances for the wrapper. For example we might define </p>
<div class="codehilite"><pre><span></span>def as_gcd_monoid (X : Type) := X
</pre></div>


<p>and then</p>
<div class="codehilite"><pre><span></span>instance [has_gcd X] : has_mul (as_gcd_monoid X) := ...
</pre></div>


<p>and finally </p>
<div class="codehilite"><pre><span></span>def finset.gcd (t : finset X) (f : X -&gt; Y) [has_gcd Y] := @finset.big_op X (as_gcd_monoid Y) t (\lambda x, f x)
</pre></div>


<p>(or something like that... )</p>

#### [ Kenny Lau (Nov 25 2018 at 04:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148302414):
<p>don't drive and derive...</p>

#### [ Scott Morrison (Nov 25 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148302765):
<p>Also, if we're going to make some progress on big ops, I think it would be great if we can ask Assia and Cyril for some advice. I'd like to do a few experiments perhaps first (actually try writing some of the <code>conv</code> style tactics for manipulating sums, and seeing if it really is okay to index by carrier type), but maybe we could even schedule a skype call with whoever is interested so we can ask them some questions.</p>

#### [ Patrick Massot (Nov 25 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148314025):
<p>Scott, I think you completely missed the point that we want to handle non-commutative operations</p>

#### [ Patrick Massot (Nov 25 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148314037):
<p>Next, I think the list + predicate is there to handle the very common case of summing on a range of integers subjects to conditions, like "sum for n from 1 to N, with n odd"</p>

#### [ Patrick Massot (Nov 25 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148314038):
<p>I'm not sure I understand what you'd like your tactic to do that a rewriting lemma couldn't</p>

#### [ Scott Morrison (Nov 25 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148335113):
<p>I did miss the intention to also do noncommutative things. What do you have in mind? (And in any case, while we're writing prototypes, I'd prefer to work in simpler special cases, so I suspect I'll propose we ignore the noncommutative stuff for now anyway.)</p>

#### [ Scott Morrison (Nov 25 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148335286):
<p>It might be good to at some point list all the things that conceivably could count as "big operations". Here's a sampling of things that could conceivably be in scope:</p>
<ul>
<li>sums, </li>
<li>products, </li>
<li>unions, </li>
<li>maxs, </li>
<li>gcds, </li>
<li>convergent sums, </li>
<li>integrals, </li>
<li>limits (e.g. as x goes to a), </li>
<li>limits (of a functor over a diagram).</li>
</ul>

#### [ Scott Morrison (Nov 25 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148335293):
<p>But Patrick, why not just filter the list, if you want to sum over odd integers? I really don't understand why you want to carry around an "unapplied" filter.</p>

#### [ Scott Morrison (Nov 25 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148335464):
<p>And I think my point stands, even if we're going to do noncommutative operations: a list is a bad way to model a ordered set. Using a list commits us to dealing with multiplicities, and I don't think that's what you intend.</p>

#### [ Scott Morrison (Nov 25 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148335685):
<p>Regarding tactics: at the moment, rewriting inside the summand is a royal pain. As far as I can see, you need to use <code>rw sum_congr</code>, having carefully prepared the equation you want to rewrite along ahead of time in the form <code>\forall x \in t, f x  = g x</code>. <code>conv</code> completely fails to enter the summand giving you appropriate hypotheses, and this could easily be fixed.</p>

#### [ Scott Morrison (Nov 25 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148335754):
<p>Going back to my "big list of big operations"... I think it would be a bad idea to try to write a framework so general it encompasses all of these.</p>

#### [ Chris Hughes (Nov 25 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148335806):
<p>So for non commutative stuff, might it be better to use a finset with <code>linear_order</code> on the indexing type? I like that idea.</p>

#### [ Scott Morrison (Nov 26 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148335959):
<p>It's possible. I'm not sure though how to make the commutative case a specialisation of the non-commutative case.</p>

#### [ Scott Morrison (Nov 26 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148335976):
<p>Another possibility is to have the range of the big operation be a "list without duplicates" (a new type?), and then have extra lemmas that apply when the operation is known to be commutative, and that list comes from a finset.</p>

#### [ Scott Morrison (Nov 26 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148335979):
<p>That design would mean lemmas proved about the noncommutative case would specialise.</p>

#### [ Chris Hughes (Nov 26 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148336031):
<p>Are there any concrete examples of where a list with duplicates is annoying?</p>

#### [ Chris Hughes (Nov 26 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148336037):
<p>I don't want to ask for that proof obligation without a good reason.</p>

#### [ Scott Morrison (Nov 26 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148336105):
<p>I ... guess not.</p>

#### [ Scott Morrison (Nov 26 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148336148):
<p>One problem is perhaps getting a list back out of a finset in the first place.</p>

#### [ Scott Morrison (Nov 26 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148336160):
<p>I'm still unhappy about carrying along unapplied predicates, but I'm now open to the idea of using a list to represent the range.</p>

#### [ Scott Morrison (Nov 26 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148337035):
<p>Just thinking out loud for a moment here: I wonder about really embracing the typeclass system here. What if we did big operations over arbitrary types A, and require an extra piece of evidence, possibly depending on the summand function <code>f : A -&gt; X</code> that the big operation makes sense. There could be lots of mechanisms here:</p>
<ul>
<li><code>[fintype A] [ordered A] [monoid X]</code> (summing over an ordered finite set)</li>
<li><code>[fintype A] [comm_monoid X]</code> (summing over a unordered finite set)</li>
<li>with <code>f : (near a) -&gt; X</code>, where <code>def near {A : Type} (a : A) := A</code>, the evidence for <code>lim_{a : near A} f</code> could be computed from something like <code>[topological_space A] [continuous_at f a]</code></li>
<li><code>[normed_space X]  [absolute_convergence f]</code>,</li>
<li><code>[category A] [category X] [is_functorial f] [has_limits_of_shape A]</code> (computing a limit)<br>
Could one prove enough of the needed lemmas in this ridiculous generality that it would be worth doing?</li>
</ul>

#### [ Chris Hughes (Nov 26 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148337512):
<p>distributivity of multiplication is true for lots of types of sums. Not sure how you'd state or prove that though. Unless you made a new class for more or less every lemma.</p>

#### [ Johan Commelin (Nov 26 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148345914):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> I think that limits (in topology or category theory) are a completely different kind of big operators from the others. All the others have some sort of iterative or recursive aspect to them. (Btw, we could add tensor products to your big list.) For those iterative instances I think it will probably be very useful to also have <code>product L</code> if <code>L</code> is a list of matrices. So we do care about the non-commutative case, I think.<br>
About tactics vs rewrites: I completely agree that it is crucial that we have slick rewriting of the summand, and currently this is a pain. I also agree with <span class="user-mention" data-user-id="110031">@Patrick Massot</span> That most of the "slicing and dicing" probably doesn't need tactics, but could be done with regular rewrite lemmas, because that doesn't touch the summand.<br>
But making <code>conv</code> access the summand would be get you a major hooray from my side! I just recently reexperienced how awful it is, when I tried to prove that <code>boundary_boundary</code> lemma in the simplicial branch. You get nested sums over finsets, and manipulating them is a silly gamble where you just hope that <code>simp</code> and <code>erw</code> drill down far enough to make a bit of progress.</p>

#### [ Scott Morrison (Nov 26 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148351986):
<p>The other tactic support I realised we can do is unrolling sums of "explicit length". Just like my <code>fin_cases</code> command, we can have a single tactic that takes for example $\sum_{n=k}^{k+3} f(n)$ and replaces it with $f(k) + f(k+1) + f(k+2) + f(k+3)$. This is quite a pain to achieve with pure rewriting, and is not so bad to automate in tactic mode.</p>

#### [ Scott Morrison (Nov 26 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148352070):
<p>I'm not sure sure that limits (in category theory or in topology) are completely different big operators. If you just categorify your natural numbers as finite sets, a sum of natural numbers is just the colimit of the discrete diagram of those sets (and a product is just the colimit)! Nevertheless, I wasn't seriously suggested we do this --- in fact I was setting up a straw man to try to argue we should not go for maximum generality. :-)</p>

#### [ Johan Commelin (Nov 26 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148352123):
<blockquote>
<p>The other tactic support I realised we can do is unrolling sums of "explicit length". Just like my <code>fin_cases</code> command, we can have a single tactic that takes for example $\sum_{n=k}^{k+3} f(n)$ and replaces it with $f(k) + f(k+1) + f(k+2) + f(k+3)$. This is quite a pain to achieve with pure rewriting, and is not so bad to automate in tactic mode.</p>
</blockquote>
<p>I suppose this could be done with <code>repeat { rw split_last }, simp</code>.</p>

#### [ Johan Commelin (Nov 26 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148352148):
<p>But I agree that an <code>unroll_bigop</code> tactic might make sense.</p>

#### [ Scott Morrison (Nov 26 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148352194):
<p>I'm not quite convinced it's that easy, but perhaps I'm thinking about the <code>fin_cases</code> situation, which was quite a bit more painful.</p>

#### [ Patrick Massot (Nov 26 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148356624):
<p>I agree it seems to make sense to drop the predicate part, at least until we see a need for it, although I'll try to ask Cyril and Assia before doing so. But non-commutative operators are crucial. I started this project because I wanted to do group theory. And I still hope that one day we will be able to handle differential forms as well.  Now that I think about it, I'm not sure I could find any big operator in one of my papers that uses a commutative operation.</p>

#### [ Patrick Massot (Nov 26 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148367393):
<p>I worked on my bigop attempt today, reaching a new sorry-free equilibrium point. I did find a use for the predicate thing as a convenient way to prove stuff, keeping track of information.</p>

#### [ Patrick Massot (Nov 26 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset.sum/near/148371544):
<p>Ok, I pushed <a href="https://github.com/leanprover-community/mathlib/tree/bigop" target="_blank" title="https://github.com/leanprover-community/mathlib/tree/bigop">https://github.com/leanprover-community/mathlib/tree/bigop</a> Any contributor is very welcome. In particular, cleaning up <a href="https://github.com/leanprover-community/mathlib/blob/bigop/pending_lemmas.lean" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/bigop/pending_lemmas.lean">https://github.com/leanprover-community/mathlib/blob/bigop/pending_lemmas.lean</a>  requires no big operators skills, only knowing mathlib (or searching efficiently), or being good at either list or nat vs int bashing.</p>


{% endraw %}
