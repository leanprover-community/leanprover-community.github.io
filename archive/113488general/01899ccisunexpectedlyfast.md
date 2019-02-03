---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01899ccisunexpectedlyfast.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [cc is unexpectedly fast](https://leanprover-community.github.io/archive/113488general/01899ccisunexpectedlyfast.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Aug 17 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20unexpectedly%20fast/near/132284614):
<p><a href="/user_uploads/3121/H2XKxrFTq7Uuh78QYpIZg00o/2018-08-17-1.png" target="_blank" title="2018-08-17-1.png">2018-08-17-1.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/H2XKxrFTq7Uuh78QYpIZg00o/2018-08-17-1.png" target="_blank" title="2018-08-17-1.png"><img src="/user_uploads/3121/H2XKxrFTq7Uuh78QYpIZg00o/2018-08-17-1.png"></a></div>

#### [ Kenny Lau (Aug 17 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20unexpectedly%20fast/near/132284629):
<p>oh... it's cheating :P</p>

#### [ Kenny Lau (Aug 17 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20unexpectedly%20fast/near/132284630):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test</span> <span class="o">:</span> <span class="mi">1001</span> <span class="bp">=</span> <span class="mi">2000</span> <span class="bp">→</span> <span class="n">false</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="mi">1001</span> <span class="bp">=</span> <span class="mi">2000</span><span class="o">),</span> <span class="n">false</span><span class="bp">.</span><span class="n">elim</span> <span class="o">(</span><span class="n">false_of_true_eq_false</span> <span class="o">(</span><span class="n">absurd</span> <span class="n">H</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">bit1_ne_bit0</span> <span class="mi">500</span> <span class="mi">1000</span><span class="o">)))</span>
</pre></div>

#### [ Johan Commelin (Aug 17 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20unexpectedly%20fast/near/132284942):
<p>That's not cheating. That's being smart (-;</p>


{% endraw %}
