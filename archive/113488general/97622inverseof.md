---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/97622inverseof.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [inverse of $](https://leanprover-community.github.io/archive/113488general/97622inverseof.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Andrew Ashworth (May 28 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186287):
<p>is there an inverse of <code>$</code>? (the backwards pipe operator<code>&lt;|</code>)  i.e. instead of <code>g (f x)</code> being written as <code>g $ f x</code> I'd like to write <code>f x &lt;| g</code></p>

#### [ Brendan Zabarauskas (May 28 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186348):
<p>I though <code>$</code> was backwards pipe? Do you mean you'd like to write <code>x |&gt; f |&gt; g</code>?</p>

#### [ Brendan Zabarauskas (May 28 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186357):
<p>(big fan of directional composition/application operators at any rate)</p>

#### [ Andrew Ashworth (May 28 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186402):
<p>er, maybe it's a forwards pipe? but yes, I'd like to reverse the order that function arguments appear</p>

#### [ Andrew Ashworth (May 28 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186414):
<p>in fact, I just googled and yeah, seems I have my directions mixed up, whoops</p>

#### [ Brendan Zabarauskas (May 28 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186455):
<p>To be more precise, I'd also recommend saying 'apply' and 'application' rather than 'pipe', which is a little ambiguous.</p>

#### [ Mario Carneiro (May 28 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186527):
<p>short answer: no</p>

#### [ Mario Carneiro (May 28 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186532):
<p>I believe that operator is used for <code>option.lhoare</code></p>

#### [ Andrew Ashworth (May 28 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186590):
<p>eughhh. <code>|&gt;</code> and <code>&lt;|</code> have been around for ages  to represent reverse and forward function application.... maybe I can steal them back after Lean 4 releases</p>

#### [ Mario Carneiro (May 28 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186593):
<p>I think that <code>lhoare</code> and <code>rhoare</code> are surprisingly useless operators</p>

#### [ Brendan Zabarauskas (May 28 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186631):
<p>what on earth is a <code>hoare</code>?</p>

#### [ Mario Carneiro (May 28 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186634):
<p>I have never seen a use for them</p>

#### [ Mario Carneiro (May 28 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186635):
<p>as in tony</p>

#### [ Brendan Zabarauskas (May 28 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186636):
<p>hoare logic?</p>

#### [ Andrew Ashworth (May 28 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186637):
<p>i don't have a problem with useless library files, but the problem is you can't unset global notation :(</p>

#### [ Brendan Zabarauskas (May 28 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186688):
<p>Also a big fan of <code>&gt;&gt;</code> and <code>&lt;&lt;</code> for composition (as in F#, Elm), but those are often stolen by haskell-like langs for monady stuff. I just say use <code>*&gt;</code> and <code>&lt;*</code> from applicative instead.</p>

#### [ Mario Carneiro (May 28 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186692):
<p>looks like <code>lhoare</code> and <code>rhoare</code> are not used anywhere in core either</p>

#### [ Mario Carneiro (May 28 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186700):
<p><code>rhoare</code> is almost the same as <code>option.guard</code> but its logic is reversed</p>

#### [ Mario Carneiro (May 28 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186748):
<p>maybe I can get <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> to burninate it?</p>

#### [ Andrew Ashworth (May 28 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186757):
<p>for symmetry reasons I'd vote for that, <code>|&gt;</code> and <code>&lt;|</code> is more pleasant to look at than dollar signs</p>

#### [ Mario Carneiro (May 28 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186798):
<p>the dollar's not going anywhere though</p>

#### [ Andrew Ashworth (May 28 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186799):
<p>and whatever arbitrary unicode symbol i would pick to replace <code>&lt;|</code></p>

#### [ Mario Carneiro (May 28 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186804):
<p>what about <code>&lt;$</code>?</p>

#### [ Andrew Ashworth (May 28 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186805):
<p>yea, I know the dollar sign is one character and from haskell</p>

#### [ Mario Carneiro (May 28 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186808):
<p>that is more obviously related to application</p>

#### [ Mario Carneiro (May 28 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186814):
<p>I assume <code>&lt;|</code> and <code>|&gt;</code> have something to do with orelse</p>

#### [ Mario Carneiro (May 28 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186815):
<p>and the hoare things are also orelsey</p>

#### [ Andrew Ashworth (May 28 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186818):
<p><code>|&gt;</code> and <code>&lt;|</code> is ocaml notation</p>

#### [ Andrew Ashworth (May 28 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186864):
<p>does haskell have a <code>&lt;|</code> equiv</p>

#### [ Mario Carneiro (May 28 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186876):
<p>I assume that haskell has a meaning for every sequence of &lt;= 3 punctuation chars</p>

#### [ Andrew Ashworth (May 28 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186921):
<p>I can get behind <code>&lt;$</code> if <code>$</code> is sticking around</p>

#### [ Johan Commelin (May 28 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186928):
<p>But don't you want <code>$&gt;</code> ?</p>

#### [ Johan Commelin (May 28 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186929):
<p>That seems more intuitive to me...</p>

#### [ Johan Commelin (May 28 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186971):
<p>But then, I've never used OCaml</p>

#### [ Andrew Ashworth (May 28 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186977):
<p>as in <code>g (f x)</code> would be written <code>f x $&gt; g</code>?</p>

#### [ Johan Commelin (May 28 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186980):
<p>Yes...</p>

#### [ Johan Commelin (May 28 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186981):
<p>The <code>&gt;</code> conveys in which way the arguments flow</p>

#### [ Johan Commelin (May 28 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186985):
<p>Just like in Bash...</p>

#### [ Johan Commelin (May 28 2018 at 05:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187024):
<p>if you write to a file</p>

#### [ Andrew Ashworth (May 28 2018 at 05:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187027):
<p>i can see that some might prefer that, i always thought of it as moving the top function instead of the arguments</p>

#### [ Johan Commelin (May 28 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187035):
<p>Ok, that also makes sense...</p>

#### [ Mario Carneiro (May 28 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187036):
<p>I was thinking <code>$</code> with a reversal, so a backward arrow to indicate that</p>

#### [ Mario Carneiro (May 28 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187038):
<p>oh, <code>&lt;$</code> is taken...</p>

#### [ Mario Carneiro (May 28 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187039):
<p><code>functor.map_const</code></p>

#### [ Johan Commelin (May 28 2018 at 05:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187078):
<p>What about <code>$&lt;</code> ?</p>

#### [ Johan Commelin (May 28 2018 at 05:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187082):
<p>(No lean here, atm)</p>

#### [ Andrew Ashworth (May 28 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187083):
<p>i prefer the bracket to be on the correct side of the dollar sign, haha</p>

#### [ Mario Carneiro (May 28 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187089):
<p><code>$&lt;</code> is clear</p>

#### [ Mario Carneiro (May 28 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187090):
<p>yeah, that's why it's taken :P</p>

#### [ Mario Carneiro (May 28 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187135):
<p>I guess <code>&lt;$</code> is named similar to <code>&lt;$&gt;</code></p>

#### [ Andrew Ashworth (May 28 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187190):
<p>when lean 4 is released I will have to be very quick and reserve <code>|&gt;</code> and <code>&lt;|</code> as fast as possible in some large library most users install...</p>

#### [ Andrew Ashworth (May 28 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187229):
<p>since it seems those might have a chance of being deleted anyway</p>

#### [ Andrew Ashworth (May 28 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187243):
<p>or maybe there's some unicode variant of the eq.subst triangle hanging around</p>

#### [ Mario Carneiro (May 28 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187284):
<p>there is unicode for everything</p>

#### [ Mario Carneiro (May 28 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187288):
<p><code>◁ </code>?</p>

#### [ Mario Carneiro (May 28 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187289):
<p>= \lhd</p>

#### [ Mario Carneiro (May 28 2018 at 05:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187299):
<p>but mathematicians are also jockeying for these symbols</p>

#### [ Andrew Ashworth (May 28 2018 at 05:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187301):
<p>this operator is so commonly used I'm boggled nobody has complained about it yet in this chat</p>

#### [ Johan Commelin (May 28 2018 at 05:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187302):
<p>I hope in Lean 4 there will be a way to selectively import notation</p>

#### [ Johan Commelin (May 28 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187344):
<p><code>import foo with bar as xyzzy</code></p>

#### [ Johan Commelin (May 28 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187345):
<p>Like in python</p>

#### [ Andrew Ashworth (May 28 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187346):
<p>am I really the first person to miss the dual of <code>$</code></p>

#### [ Mario Carneiro (May 28 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187347):
<p>for CS things I prefer ascii because mathematicians won't lower themselves to use them</p>

#### [ Johan Commelin (May 28 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187354):
<p>lol</p>

#### [ Mario Carneiro (May 28 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187355):
<p>well, it is obviously redundant...</p>

#### [ Johan Commelin (May 28 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187411):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> So plug a zero-width char in between, an create a keyboard shortcut to type the 3-char-combo. Or does VScode not render 0-width-chars with 0 width?</p>

#### [ Mario Carneiro (May 28 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187414):
<p>nooo</p>

#### [ Johan Commelin (May 28 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187420):
<p>Or use <code>local notation</code> to override the global stuff. I did that with <code>[n]</code>.</p>

#### [ Johan Commelin (May 28 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187471):
<p>Does Lean recognize 0-width space as whitespace?</p>

#### [ Andrew Ashworth (May 28 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187570):
<p>i guess.. but when people do more actual programming, it's nice to write something like <code>[1..10] |&gt; map f</code> (with the arrow the way Johan likes it)</p>

#### [ Reid Barton (May 28 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187574):
<p>I was going to say, isn't <code>|&gt;</code> the flipped application?</p>

#### [ Reid Barton (May 28 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187576):
<p>But in lean, can't you write <code>[1..10].map f</code>?</p>

#### [ Andrew Ashworth (May 28 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187619):
<p><code>[1..10]</code> might be some arbitrary expression that spans multiple lines</p>

#### [ Mario Carneiro (May 28 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187621):
<div class="codehilite"><pre><span></span>def «te​st» := 1
#print «te​st»
</pre></div>

#### [ Mario Carneiro (May 28 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187625):
<p>it doesn't like it as a space or as an identifier</p>

#### [ Andrew Ashworth (May 28 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187627):
<p>also I've completely got the application directions mixed up in my head, if I could delete it all I would :)</p>

#### [ Reid Barton (May 28 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187636):
<p>I don't really see what you gain over using parentheses or a variety of other options</p>

#### [ Johan Commelin (May 28 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187639):
<p>/me should prove <code>fermаt_lаst_theorem</code> in a couple lines, after importing <a href="https://github.com/formalabstracts/formalabstracts/blob/master/fabstract/Wiles_A_and_Taylor_R_FermatLast/fabstract.lean" target="_blank" title="https://github.com/formalabstracts/formalabstracts/blob/master/fabstract/Wiles_A_and_Taylor_R_FermatLast/fabstract.lean">https://github.com/formalabstracts/formalabstracts/blob/master/fabstract/Wiles_A_and_Taylor_R_FermatLast/fabstract.lean</a>, and some other obscure libraries... <span class="emoji emoji-1f61c" title="stuck out tongue winking eye">:stuck_out_tongue_winking_eye:</span></p>

#### [ Reid Barton (May 28 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187684):
<p>The uses I know of for flipped application are when you have left-to-right type inference / overloading resolution (Haskell doesn't have this, Lean might, not sure) or you want the order of effects to be left-to-right (Haskell has <code>&gt;&gt;=</code>)</p>

#### [ Johan Commelin (May 28 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187687):
<p>No-one will notice that I used a Cyrillic <code>a</code> in <code>fermat</code></p>

#### [ Reid Barton (May 28 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187695):
<p>And of course it can be a style thing. One can debate the merits of having more styles available versus having fewer styles available</p>

#### [ Johan Commelin (May 28 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187696):
<p>Just want to point out that I am a mathematician who loves ascii</p>

#### [ Andrew Ashworth (May 28 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187790):
<p>it is a little redundant, yes, you can argue field notation, <code>$</code>, and parens should be all you need, for me it's a stylistic issue v0v</p>

#### [ Andrew Ashworth (May 28 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187801):
<p>it's a bigger deal in F# because as you mentioned type checking is done left-to-right</p>

#### [ Andrew Ashworth (May 28 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187845):
<p>but it enables you to build up nice looking data transformation definitions that look natural</p>

#### [ Mario Carneiro (May 28 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187851):
<p>actually the type checking thing is a good point</p>

#### [ Andrew Ashworth (May 28 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187891):
<p>with no parentheses like you might need with Lean's field notation</p>

#### [ Andrew Ashworth (May 28 2018 at 06:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187900):
<blockquote>
<p>actually the type checking thing is a good point</p>
</blockquote>
<p>how so?</p>

#### [ Mario Carneiro (May 28 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127188224):
<p>hm, I'm having trouble coming up with an example of a difference from the order change</p>

#### [ Mario Carneiro (May 28 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127188228):
<p>but in theory there should be some differences due to the parse order, which does matter</p>

#### [ Andrew Ashworth (May 28 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127188235):
<p>consider this F# snippet: </p>
<div class="codehilite"><pre><span></span><span class="k">let</span> <span class="nv">res</span> <span class="o">=</span>
  <span class="o">[</span> <span class="mi">1</span> <span class="o">..</span> <span class="mi">10</span> <span class="o">]</span>
  <span class="o">|&gt;</span> <span class="nn">List</span><span class="p">.</span><span class="n">filter</span> <span class="n">isEven</span>
  <span class="o">|&gt;</span> <span class="nn">List</span><span class="p">.</span><span class="n">map</span> <span class="n">formatInt</span>
</pre></div>


<p>writing this in Lean using field notation is a little cumbersome, and doesn't look as pretty</p>


{% endraw %}
