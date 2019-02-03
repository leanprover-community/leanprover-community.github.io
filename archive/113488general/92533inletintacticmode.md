---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/92533inletintacticmode.html
---

## Stream: [general](index.html)
### Topic: [$ in let in tactic mode](92533inletintacticmode.html)

---


{% raw %}
#### [ Kevin Buzzard (May 12 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20in%20let%20in%20tactic%20mode/near/126468511):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">let</span> <span class="n">d</span> <span class="o">:=</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="err">$</span> <span class="n">nat</span><span class="bp">.</span><span class="n">zero</span><span class="o">,</span> <span class="c1">-- fails</span>
  <span class="n">exact</span> <span class="n">d</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (May 12 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20in%20let%20in%20tactic%20mode/near/126468513):
<p>Replacing the $ with brackets (or in this case not even brackets) fixes it. It seems to me that the $ wants to eat the comma and things after it.</p>

#### [ Kevin Buzzard (May 12 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20in%20let%20in%20tactic%20mode/near/126468514):
<p>Is that expected behaviour?</p>

#### [ Sebastian Ullrich (May 12 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20in%20let%20in%20tactic%20mode/near/126469412):
<p>It's not that <code>$</code> eats too much input, but that it has a lower precedence than is used to parse the argument to <code>let</code>. <code>$</code> has the same precedence as <code>;</code>, and <code>let a := b; c</code> is supposed to be parsed as <code>(let a := b); c</code>. Perhaps it should have a higher precedence than <code>;</code>, but it's never quite clear what would be the best order in all contexts</p>

#### [ Sebastian Ullrich (May 12 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20in%20let%20in%20tactic%20mode/near/126469413):
<p>I.e. <code>let d := (nat.succ $ nat.zero)</code> should work</p>

#### [ Sean Leather (May 14 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20in%20let%20in%20tactic%20mode/near/126524735):
<p>See also <a href="https://groups.google.com/d/msg/lean-user/B5tG4xj4xHc/6z8Ipx1pBQAJ" target="_blank" title="https://groups.google.com/d/msg/lean-user/B5tG4xj4xHc/6z8Ipx1pBQAJ">Use of $ in tactics</a>.</p>


{% endraw %}
