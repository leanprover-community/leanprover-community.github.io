---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/70736reducevseval.html
---

## Stream: [general](index.html)
### Topic: [#reduce vs #eval](70736reducevseval.html)

---


{% raw %}
#### [ Simon Hudon (Feb 27 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20vs%20%23eval/near/123060876):
<p>Does it ever happen that #reduce runs forever while #eval terminates immediately?</p>

#### [ Kevin Buzzard (Feb 27 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20vs%20%23eval/near/123061271):
<p>Try 1000*1000</p>

#### [ Simon Hudon (Feb 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20vs%20%23eval/near/123061346):
<p>it times out</p>

#### [ Kevin Buzzard (Feb 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20vs%20%23eval/near/123061357):
<p>Does that not count as "I ran forever but I explained this to you in a different kind of way"</p>

#### [ Simon Hudon (Feb 27 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20vs%20%23eval/near/123061395):
<p>It would but my example involves numbers such as 1 and 0</p>

#### [ Kevin Buzzard (Feb 27 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20vs%20%23eval/near/123061409):
<p>Try <code>(1+1)*(1+1)*(1+1)*(1+1)*...*(1+1)</code></p>

#### [ Simon Hudon (Feb 27 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20vs%20%23eval/near/123061467):
<p>... but it also involves an encoding of an infinite tree ... I wonder if that's what is taking super duper long</p>

#### [ Simon Hudon (Feb 27 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20vs%20%23eval/near/123061650):
<p>I'll be more specific. I'm trying:</p>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="n">reduce</span> <span class="n">to_bin_tree</span> <span class="mi">3</span> <span class="o">(</span><span class="n">mk_tree</span> <span class="mi">0</span><span class="o">)</span>
</pre></div>


<p>where <code>my_tree</code> creates an infinite tree starting at 0 and incrementing it from time to time and <code>to_bin_tree</code> truncates it after 3 steps. It creates the following binary tree:</p>
<div class="codehilite"><pre><span></span>(node 0 (node 1 (node ⊥ ⊥)))
</pre></div>

#### [ Simon Hudon (Feb 27 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20vs%20%23eval/near/123061734):
<p>Anyway, you made your point. Truncating the tree is probably much more expensive now that I changed their representation</p>

#### [ Simon Hudon (Feb 27 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20vs%20%23eval/near/123061736):
<p>Thanks!</p>


{% endraw %}
