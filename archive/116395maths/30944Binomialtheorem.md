---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/30944Binomialtheorem.html
---

## Stream: [maths](index.html)
### Topic: [Binomial theorem](30944Binomialtheorem.html)

---


{% raw %}
#### [ Nicholas Scheel (Jun 08 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Binomial%20theorem/near/127788179):
<p>Hey! I proved the binomial theorem, if anyone finds it interesting its in a gist here: <a href="https://gist.github.com/MonoidMusician/ad43301ee3b4e71c0e1c3d440c6898c5" target="_blank" title="https://gist.github.com/MonoidMusician/ad43301ee3b4e71c0e1c3d440c6898c5">https://gist.github.com/MonoidMusician/ad43301ee3b4e71c0e1c3d440c6898c5</a></p>

#### [ Nicholas Scheel (Jun 08 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Binomial%20theorem/near/127788226):
<p>just curious: is there an existing definition of the binomial coefficient anywhere, maybe with some lemmas? I couldn't find one</p>

#### [ Kevin Buzzard (Jun 08 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Binomial%20theorem/near/127788345):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> did this but I'm not sure it ever made it into mathlib. I think Chris did pretty much everything in my introduction to proof course. He even did the multinomial theorem (I think this is one of the reasons he's so good at finite stuff :-) )</p>

#### [ Chris Hughes (Jun 08 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Binomial%20theorem/near/127789175):
<blockquote>
<p>just curious: is there an existing definition of the binomial coefficient anywhere, maybe with some lemmas? I couldn't find one</p>
</blockquote>
<p><code>data.nat.choose</code></p>

#### [ Scott Morrison (Jun 11 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Binomial%20theorem/near/127889314):
<p>Hi <span class="user-mention" data-user-id="111651">@Nicholas Scheel</span> , it would be great to PR this into mathlib. (<span class="user-mention" data-user-id="110044">@Chris Hughes</span>, too :-)</p>

#### [ Chris Hughes (Jun 11 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Binomial%20theorem/near/127908813):
<blockquote>
<p>Hi <span class="user-mention" data-user-id="111651">@Nicholas Scheel</span> , it would be great to PR this into mathlib. (<span class="user-mention" data-user-id="110044">@Chris Hughes</span>, too :-)</p>
</blockquote>
<p>The main reason I didn't do this, is we don't have a sensible definition of sums between naturals yet.</p>

#### [ Kevin Buzzard (Jun 11 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Binomial%20theorem/near/127910585):
<p>You mean sums from a to b? Mario always argued that you should do sums from a to a+b (or perhaps a+b-1) and seeing the troubles Patrick had when summing from a to b I am inclined to take Mario's word for it. I know from years of worrying about this sort of thing that I'm completely happy to see a sum from i to j if (and only if) j&gt;=i-1, but if j&lt;i-1 then I always feel something has gone wrong.</p>

#### [ Chris Hughes (Jun 11 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Binomial%20theorem/near/127912967):
<p>I'm just waiting for some definition to end up in the library. I actually needed non commutative products for Sylow, so it would be useful if Patrick PRed his big operators.</p>

#### [ Patrick Massot (Jun 11 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Binomial%20theorem/near/127914048):
<p>I'm sorry I don't have a lot of time for Lean, and it seemed more fun to jump on the perfectoid train because it means team work. But help is very much welcome on the bigop front.</p>

#### [ Kevin Buzzard (Jun 11 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Binomial%20theorem/near/127914094):
<p>Last time I looked you were doing great with the bigop thing, there didn't seem to be any problems like there were with type class inference for the modules, and I was just leaving you to do it. Then you went back to the normed vector spaces and had type class problems again, which to be honest was a bit depressing, all I remember was the CS people talking about how interesting out_param was. What is the current state of the bigop stuff?</p>

#### [ Patrick Massot (Jun 11 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Binomial%20theorem/near/127914287):
<p>I got tired of nat substraction mainly, especially since <code>cooper</code> seems to promise to make all this easier</p>


{% endraw %}
