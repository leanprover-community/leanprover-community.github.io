---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/30756monadrefactoring.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [monad refactoring](https://leanprover-community.github.io/archive/113488general/30756monadrefactoring.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Mar 01 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123127367):
<p><span class="user-mention" data-user-email="sebasti@nullri.ch" data-user-id="110024">@Sebastian Ullrich</span> woke up with a lot of homework... Does anyone knows whether basic users like me will see any difference after merging this?</p>

#### [ Simon Hudon (Mar 01 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123127532):
<p>Are you referring to the commits in his own fork?</p>

#### [ Sean Leather (Mar 01 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123127592):
<p>To avoid ambiguity and for posterity: <a href="https://github.com/leanprover/lean/pull/1881" target="_blank" title="https://github.com/leanprover/lean/pull/1881">https://github.com/leanprover/lean/pull/1881</a></p>

#### [ Simon Hudon (Mar 01 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123127763):
<p>Thanks <span class="user-mention" data-user-email="sean.leather@gmail.com" data-user-id="110045">@Sean Leather</span></p>

#### [ Sean Leather (Mar 01 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123127842):
<blockquote>
<p>woke up with a lot of homework... Does anyone knows whether basic users like me will see any difference after merging this?</p>
</blockquote>
<p><span class="user-mention" data-user-email="patrickmassot@free.fr" data-user-id="110031">@Patrick Massot</span>: I'm guessing you're referring to Leo's comments, of which there were a lot.</p>

#### [ Patrick Massot (Mar 01 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123127851):
<p>Yes.</p>

#### [ Patrick Massot (Mar 01 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128035):
<p>There are a lot of comments but there is a <em>lot</em> of code in this PR.</p>

#### [ Mario Carneiro (Mar 01 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128054):
<p>I'm also curious about this. <span class="user-mention" data-user-email="sebasti@nullri.ch" data-user-id="110024">@Sebastian Ullrich</span> , could you maybe discuss or point to a place where you discuss the purpose of the monad refactoring project? From what little I can garner from Leo's comments, it looks like you are maybe adding more advanced monad features from Haskell like monad transformers, the continuation monad and call/cc?</p>

#### [ Simon Hudon (Mar 01 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128087):
<p>I think you'll see a difference (hopefully for the best) if you use Lean to write programs. Otherwise, I don't think you'll see a difference</p>

#### [ Patrick Massot (Mar 01 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128109):
<p>It's very hard to resist going to Leo's most cryptic comment and add: "Yeah, I wondered about that too".</p>

#### [ Patrick Massot (Mar 01 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128115):
<p>What do you mean "write program"? Write a tactic?</p>

#### [ Simon Hudon (Mar 01 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128135):
<p>I think not much if you write tactics. More if you use Lean as a functional programming language (with or without much verification)</p>

#### [ Patrick Massot (Mar 01 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128181):
<p>Are there people doing that?</p>

#### [ Sean Leather (Mar 01 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128182):
<p>As in I/O?! <span class="emoji emoji-1f631" title="scream">:scream:</span></p>

#### [ Simon Hudon (Mar 01 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128187):
<p>On top of my head, there's me</p>

#### [ Simon Hudon (Mar 01 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128230):
<p>I/O or other kind of code. There's a lot you can do with monads</p>

#### [ Simon Hudon (Mar 01 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128232):
<p>Why do you seem so scared of I/O?</p>

#### [ Patrick Massot (Mar 01 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128233):
<p>Doesn't sound functional to me</p>

#### [ Sean Leather (Mar 01 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128234):
<p>I meant, as in writing a “real” program that does I/O, not as in using the <code>io</code> monad... <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Simon Hudon (Mar 01 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128241):
<blockquote>
<p>Doesn't sound functional to me</p>
</blockquote>
<p>Why not?</p>

#### [ Sean Leather (Mar 01 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128285):
<blockquote>
<p>Why do you seem so scared of I/O?</p>
</blockquote>
<p>Because of the meme that theorem-proving languages are generally only used for proofs and type-checking.</p>

#### [ Kevin Buzzard (Mar 01 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128287):
<blockquote>
<blockquote>
<p>Doesn't sound functional to me</p>
</blockquote>
<p>Why not?</p>
</blockquote>
<p>Every article I read about functional programming makes a huge fuss about i/o. That's probably what he means. In contrast to procedural languages, where the first program you ever see is "print hello world"</p>

#### [ Patrick Massot (Mar 01 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128290):
<p>I thought functional programming swears to be isolated from real world</p>

#### [ Sean Leather (Mar 01 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128301):
<blockquote>
<p>I thought functional programming swears to be isolated from real world</p>
</blockquote>
<p>That's a myth and a well-disproven one at that.</p>

#### [ Simon Hudon (Mar 01 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128303):
<p>That was true of Haskell before they invented monads but the <code>io</code> monad makes I/O into a perfectly ok part of pure functional programming.</p>

#### [ Simon Hudon (Mar 01 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128365):
<p>Some people write OSs and web servers using purely functional programming. It looks pretty real to me and their users :)</p>

#### [ Sean Leather (Mar 01 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128373):
<p>It's funny how, as you climb up the ladder of high-level programming languages, each level above seems to be less useful than the level you're on, at least until you understand it.</p>

#### [ Patrick Massot (Mar 01 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128376):
<p>What's funny is right now I'm staring at my NodeJS I/O code which doesn't work. I don't know why it insisted trying to read all 29668 files in this directory before starting to work on the first one (and then FATAL ERROR: CALL_AND_RETRY_LAST Allocation failed - JavaScript heap out of memory)</p>

#### [ Simon Hudon (Mar 01 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128378):
<p>Yeah! And as I climb up, I get nervous about climbing down. Everything makes sense up here!</p>

#### [ Sean Leather (Mar 01 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128420):
<p>Yes, you can get complacent with all of the protection you have.</p>

#### [ Patrick Massot (Mar 01 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128433):
<p>I love functional programming languages guys. They are brothers to mathematicians. We also think what we do is more powerful and more beautiful than what other do. And normal people think what we do is un-understandable and useless</p>

#### [ Simon Hudon (Mar 01 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128434):
<p>I have a friend whom i'm mentoring with Haskell. He works with JavaScript. He's more courageous than me. I don't think I'd want to go back to object oriented programming ... unless it was generated from afull functional specification</p>

#### [ Simon Hudon (Mar 01 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128479):
<p>And we're also insufferable when coming in contact with other communities</p>

#### [ Patrick Massot (Mar 01 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128484):
<p>In my case the trouble is not object oriented programming, it's asynchronicity</p>

#### [ Simon Hudon (Mar 01 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128485):
<p>"You're getting into trouble because your pointers are aliasing each other? How quaint!"</p>

#### [ Sean Leather (Mar 01 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128527):
<p>Aliased pointers in JavaScript? <span class="emoji emoji-1f615" title="confused">:confused:</span></p>

#### [ Simon Hudon (Mar 01 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128532):
<p>Object oriented programming is supposed to be a solution (some might disagree <em>cough cough</em>) but asynchronicity is an actual programming challenge ... at the center of my research as it happens</p>

#### [ Simon Hudon (Mar 01 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128538):
<blockquote>
<p>Aliased pointers in JavaScript? <span class="emoji emoji-1f615" title="confused">:confused:</span></p>
</blockquote>
<p>References to objects, etc. I'm fairly sure they don't have a complete value semantics</p>

#### [ Patrick Massot (Mar 01 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128579):
<p>It's fun here but I need to take a shower, see you</p>

#### [ Simon Hudon (Mar 01 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123128585):
<p>Alright! Let's be insufferable later! <span class="emoji emoji-1f601" title="grin">:grin:</span></p>

#### [ Sebastian Ullrich (Mar 01 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123131312):
<p>I'll leave this link as a hint to our motivation... :P <a href="https://github.com/Kha/syntax/blob/master/macro.lean#L5" target="_blank" title="https://github.com/Kha/syntax/blob/master/macro.lean#L5">https://github.com/Kha/syntax/blob/master/macro.lean#L5</a></p>

#### [ Scott Morrison (Mar 01 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123134401):
<p>Hi <span class="user-mention" data-user-email="sebasti@nullri.ch" data-user-id="110024">@Sebastian Ullrich</span> , is there some explanation I can read of what you did to <code>bind</code>?</p>

#### [ Sebastian Ullrich (Mar 01 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123134448):
<p><span class="user-mention" data-user-email="scott@tqft.net" data-user-id="110087">@Scott Morrison</span> Does the test file help? <a href="https://github.com/leanprover/lean/blob/master/tests/lean/run/rebind_bind.lean" target="_blank" title="https://github.com/leanprover/lean/blob/master/tests/lean/run/rebind_bind.lean">https://github.com/leanprover/lean/blob/master/tests/lean/run/rebind_bind.lean</a></p>

#### [ Scott Morrison (Mar 01 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123134454):
<p>There are lots of places mathlib has broken, e.g.</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">length_bind</span> <span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">list</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">length</span> <span class="o">(</span><span class="n">bind</span> <span class="n">l</span> <span class="n">f</span><span class="o">)</span> <span class="bp">=</span> <span class="n">sum</span> <span class="o">(</span><span class="n">map</span> <span class="o">(</span><span class="n">length</span> <span class="err">∘</span> <span class="n">f</span><span class="o">)</span> <span class="n">l</span><span class="o">)</span>
</pre></div>

#### [ Scott Morrison (Mar 01 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123134460):
<p>Where is says</p>
<div class="codehilite"><pre><span></span>type mismatch at application
  l &gt;&gt;= f
term
  f
has type
  α → list β : Type (max u v)
but is expected to have type
  α → list ?m_1 : Type u
</pre></div>

#### [ Sebastian Ullrich (Mar 01 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123134518):
<p>Ah, <code>list.bind</code> is <code>protected</code> now, as it should have been from the beginning</p>

#### [ Scott Morrison (Mar 01 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123134572):
<p>So it should use ...?</p>

#### [ Sebastian Ullrich (Mar 01 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123134588):
<p>You can replace <code>bind</code> with <code>list.bind</code></p>

#### [ Scott Morrison (Mar 01 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123134589):
<p>thanks</p>

#### [ Sebastian Ullrich (Mar 01 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123134636):
<p>But I would argue that we should usually prefer using the generic operations (i.e. <code>bind</code>/<code>&gt;&gt;=</code> here) even if it means that alpha and beta have to live in the same universe in this case</p>

#### [ Sebastian Ullrich (Mar 01 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123134637):
<p><span class="user-mention" data-user-email="di.gama@gmail.com" data-user-id="110049">@Mario Carneiro</span> thoughts?</p>

#### [ Scott Morrison (Mar 01 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123135235):
<p>The other place I'm seeing trouble from the monad refactoring is in mathlib's <code>data/encodable.lean</code>.</p>

#### [ Scott Morrison (Mar 01 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123135285):
<p>where it looks like the problem is that there are too many <code>bind</code>s available</p>

#### [ Scott Morrison (Mar 01 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123135288):
<p>and the <code>do</code> notation is now failing as a result.</p>

#### [ Sebastian Ullrich (Mar 01 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123136383):
<p>I guess <code>option.bind</code> should be protected as well? Gaah.</p>

#### [ Mario Carneiro (Mar 01 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123140100):
<p>The "named" bind is there in part exactly for this universe distinguishing thing. There are times when it matters, and you need the polymorphic version. For most of these operations, there is also a symbol name for them, which is preferred when universes don't matter or you are over a known structure.</p>

#### [ Sebastian Ullrich (Mar 01 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123140604):
<p>Yah, it's the curse of the monad. I'll mark <code>option.bind</code> as protected then.</p>

#### [ Simon Hudon (Mar 01 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123157560):
<p>I took the liberty of commenting on your pull request. Is this the best way to interact on this subject or should I stick to Zulip / Gitter?</p>

#### [ Sebastian Ullrich (Mar 02 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123159187):
<p>That's fine, I just didn't get to it yet</p>

#### [ Simon Hudon (Mar 02 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123159201):
<p>No worries. I just don't want to be intrusive by commenting directly on github</p>

#### [ Sebastian Ullrich (Mar 02 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123159573):
<p>I'm happy for any feedback by experienced Haskell programmers, since neither Leo nor me is one of them</p>

#### [ Simon Hudon (Mar 02 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123159859):
<p>Excellent then :) I'll keep them coming. In passing, I am truly amazed by the language that you guys came up with. Learning Haskell was like a religious conversion for me and it ended a three year programming hiatus. Lean is comparing really well</p>

#### [ Sebastian Ullrich (Mar 02 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monad%20refactoring/near/123160171):
<p>Thank you <span class="emoji emoji-1f604" title="smile">:smile:</span></p>


{% endraw %}
