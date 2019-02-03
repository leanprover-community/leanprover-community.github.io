---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/67651Tryitonline.html
---

## Stream: [general](index.html)
### Topic: [Try it online!](67651Tryitonline.html)

---


{% raw %}
#### [ Kenny Lau (Mar 31 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/124444027):
<p><a href="https://tio.run/##y0lNzPv/PzO3IL@oRCExLzGnsjizWK8oNTGHSzk5IzU5WyEvsUQvMSUlPjk/NxcmpmGkYKUAUqT5/z8A" target="_blank" title="https://tio.run/##y0lNzPv/PzO3IL@oRCExLzGnsjizWK8oNTGHSzk5IzU5WyEvsUQvMSUlPjk/NxcmpmGkYKUAUqT5/z8A">Lean is now available at tio.run</a></p>

#### [ Kenny Lau (Mar 31 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/124444036):
<p>It’s a website hosted by a guy named Dennis mainly for the purpose of code-golfing competitions held in codegolf.SE</p>

#### [ Kenny Lau (Mar 31 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/124444076):
<p>of which I have been a regular for 3 years</p>

#### [ Kenny Lau (Mar 31 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/124444084):
<p>it was added shortly after I <a href="https://codegolf.stackexchange.com/a/160919/48934" target="_blank" title="https://codegolf.stackexchange.com/a/160919/48934">answered a challenge in Lean for the first time</a></p>

#### [ Mario Carneiro (Mar 31 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/124444387):
<p>Re your golf:</p>
<div class="codehilite"><pre><span></span>def f:_-&gt;nat|(n+2):=f(n+1)+f n|x:=x
</pre></div>

#### [ Kenny Lau (Mar 31 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/124444436):
<p>nice... how does that _ work?</p>

#### [ Mario Carneiro (Mar 31 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/124444445):
<p>It figures out the type from <code>(n+2)</code></p>

#### [ Kenny Lau (Mar 31 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/124444447):
<p>you seriously should joins us! <span class="emoji emoji-1f61b" title="stuck out tongue">:stuck_out_tongue:</span></p>

#### [ Mario Carneiro (Mar 31 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/124444448):
<p>I watch a lot</p>

#### [ Kenny Lau (Mar 31 2018 at 08:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/124444535):
<p>i could even prove its correctness at the end of my answer <span class="emoji emoji-1f61b" title="stuck out tongue">:stuck_out_tongue:</span></p>

#### [ Mario Carneiro (Mar 31 2018 at 08:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/124444586):
<p>Heh, my only answer on PPCG is a program that creates optimal golfs in another language</p>

#### [ Kenny Lau (Mar 31 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/124457803):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Kenny Lau (Mar 31 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/124457805):
<p>Dennis got his thing to automatically build the latest version of mathlib once it got OK'ed by travis</p>

#### [ Chris Hughes (Mar 31 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/124462918):
<p>Impressively fast. Is there a way to change the layout?</p>

#### [ Kenny Lau (Mar 31 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/124462920):
<p>what kind of layout?</p>

#### [ Chris Hughes (Mar 31 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/124463425):
<p>So it's like VScode, with goals on the right.</p>

#### [ Kenny Lau (Mar 31 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/124463465):
<p>I'm afraid that isn't possible, since every other language on the site uses the same layout</p>

#### [ Kenny Lau (Mar 31 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/124463467):
<p>you can still see the goals if you leave them blank, it will be displayed as an error</p>

#### [ Kenny Lau (Apr 05 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/124672274):
<p><a href="https://tio.run/##y0lNzPv/PzO3IL@oRCExLzGnsjizWK8oNTGHSzk5IzU5WyEvsUQvMSUlPjk/NxcmpmGkYKUAUqT5/z8A" target="_blank" title="https://tio.run/##y0lNzPv/PzO3IL@oRCExLzGnsjizWK8oNTGHSzk5IzU5WyEvsUQvMSUlPjk/NxcmpmGkYKUAUqT5/z8A">Lean@TIO</a> has updated to mathlib <code> 22e671 </code> on lean <code> 96c932a </code></p>

#### [ Kenny Lau (Apr 24 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/125600886):
<p><a href="https://codegolf.stackexchange.com/a/163239/48934" target="_blank" title="https://codegolf.stackexchange.com/a/163239/48934">https://codegolf.stackexchange.com/a/163239/48934</a></p>

#### [ Andrew Ashworth (Apr 24 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/125603271):
<p>I see the top answer is very awesome, <code>ṗṬML</code>. Dear god what am I reading</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/125611300):
<p>I quit Lean. I'm moving over to Jelly.</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/125611305):
<p>[that's what we call Jello in the UK]</p>

#### [ Sean Leather (Apr 24 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/125613031):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Why not <code>ℕ</code> instead of <code>nat</code>?</p>

#### [ Kenny Lau (Apr 24 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/125613033):
<p>not sure how many bytes the former is</p>

#### [ Sean Leather (Apr 24 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/125613089):
<p>Hmm, 3 bytes according to <a href="https://mothereff.in/byte-counter" target="_blank" title="https://mothereff.in/byte-counter">https://mothereff.in/byte-counter</a> .</p>

#### [ Kenny Lau (Apr 24 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/125613094):
<p>then it saves no bytes :P</p>

#### [ Sean Leather (Apr 24 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/125613097):
<p>Indeed.</p>

#### [ Kenny Lau (Nov 16 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/147846641):
<p><a href="https://codegolf.stackexchange.com/a/176122/48934" target="_blank" title="https://codegolf.stackexchange.com/a/176122/48934">https://codegolf.stackexchange.com/a/176122/48934</a></p>

#### [ Scott Morrison (Nov 16 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/147848525):
<p>Quick, a PR!</p>

#### [ Chris Hughes (Nov 16 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/147849345):
<p>you could <code>import data.rat</code> and save one character</p>

#### [ Chris Hughes (Nov 16 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/147849432):
<p>I would have commented on stackexchange but I needed 50 reputation.</p>

#### [ Kevin Buzzard (Nov 16 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/147849439):
<p>Are you allowed to use "the standard library"?</p>

#### [ Mario Carneiro (Nov 16 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/147849595):
<p>yes, as long as you don't update the standard library after the challenge</p>

#### [ Mario Carneiro (Nov 16 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/147849650):
<p>you will notice the mathematica answer is a cheeky <code>DirichletConvolve</code></p>

#### [ Mario Carneiro (Nov 16 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/147849669):
<p>(so in particular scott's strategy is disallowed by the rules)</p>

#### [ Mario Carneiro (Nov 16 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/147849792):
<p>wait, kenny's last post on this thread is a codegolf for the number of surjections, plus a proof of correctness. Why doesn't mathlib have that?</p>

#### [ Kenny Lau (Nov 16 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/147849855):
<p>does it?</p>

#### [ Mario Carneiro (Nov 16 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/147849864):
<p><a href="https://codegolf.stackexchange.com/a/163239/11143" target="_blank" title="https://codegolf.stackexchange.com/a/163239/11143">https://codegolf.stackexchange.com/a/163239/11143</a></p>

#### [ Kenny Lau (Nov 16 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/147849969):
<p>I mean, does mathlib have that?</p>

#### [ Kevin Buzzard (Nov 16 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/147850001):
<p>We could just start working on getting all of OEIS in, right?</p>

#### [ Mario Carneiro (Nov 16 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/147850991):
<p>it doesn't, that's my point</p>

#### [ Mario Carneiro (Nov 16 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/147851047):
<p>I don't see any reason we shouldn't have the stirling numbers defined, especially if you have a nice thing to prove about them</p>

#### [ Mario Carneiro (Nov 16 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Try%20it%20online%21/near/147851151):
<p>I'm not saying we should all go out and formalize OEIS, but if someone has already gone to the trouble of formalizing some of it, I'd like to get in on that</p>


{% endraw %}
