---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/36054uncheckedcast.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [unchecked cast](https://leanprover-community.github.io/archive/113488general/36054uncheckedcast.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Sep 15 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134005017):
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">eval</span> <span class="bp">@</span><span class="n">unchecked_cast</span> <span class="n">int</span> <span class="n">nat</span> <span class="o">(</span><span class="bp">-</span><span class="mi">3</span><span class="o">)</span> <span class="c1">-- 2147483645</span>
<span class="bp">#</span><span class="kn">eval</span> <span class="bp">@</span><span class="n">unchecked_cast</span> <span class="o">(</span><span class="n">list</span> <span class="n">nat</span><span class="o">)</span> <span class="o">(</span><span class="n">list</span> <span class="n">nat</span><span class="o">)</span> <span class="o">[</span><span class="mi">3</span><span class="o">]</span> <span class="c1">-- [3]</span>
<span class="bp">#</span><span class="kn">eval</span> <span class="bp">@</span><span class="n">unchecked_cast</span> <span class="n">nat</span> <span class="o">(</span><span class="n">list</span> <span class="n">nat</span><span class="o">)</span> <span class="mi">3</span> <span class="c1">-- []</span>
<span class="bp">#</span><span class="kn">eval</span> <span class="bp">@</span><span class="n">unchecked_cast</span> <span class="n">nat</span> <span class="o">(</span><span class="n">nat</span> <span class="bp">→</span> <span class="n">nat</span><span class="o">)</span> <span class="mi">3</span> <span class="mi">3</span>
<span class="c1">-- vm check failed: cidx(closure) == 0 (possibly due to incorrect axioms, or sorry)</span>
<span class="bp">#</span><span class="kn">eval</span> <span class="bp">@</span><span class="n">unchecked_cast</span> <span class="o">(</span><span class="n">list</span> <span class="o">(</span><span class="n">list</span> <span class="n">nat</span><span class="o">))</span> <span class="o">(</span><span class="n">list</span> <span class="n">nat</span><span class="o">)</span> <span class="o">[[</span><span class="mi">3</span><span class="o">]]</span>
<span class="c1">-- vm check failed: is_mpz(o) (possibly due to incorrect axioms, or sorry)</span>
</pre></div>

#### [ Kenny Lau (Sep 15 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134005054):
<p>quite fun</p>

#### [ Kevin Buzzard (Sep 15 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134005957):
<p>can you cast int to nat?</p>

#### [ Kevin Buzzard (Sep 15 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134005964):
<p>Lean always has fun trying to do that</p>

#### [ Kevin Buzzard (Sep 15 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134005972):
<p>oh duh that's exactly what you just did</p>

#### [ Kevin Buzzard (Sep 15 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134005990):
<p>Is this related to why Lean times out if you try to do this?</p>

#### [ Chris Hughes (Sep 15 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134006063):
<p>I doubt it. I don't think the kernel or the elaborator care about the VM representation.</p>

#### [ Kevin Buzzard (Sep 15 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134006455):
<p>How come the VM can deal with integers bigger than 2^32 if it is storing things in this classical manner?</p>

#### [ Kenny Lau (Sep 15 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134006602):
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">eval</span> <span class="bp">@</span><span class="n">unchecked_cast</span> <span class="n">int</span> <span class="n">nat</span> <span class="o">(</span><span class="bp">-</span><span class="mi">21474836450</span><span class="o">)</span> <span class="c1">-- -21474836450</span>
</pre></div>

#### [ Kenny Lau (Sep 15 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134006604):
<p>looks like <code>-21474836450</code> is a natural number!</p>

#### [ Keeley Hoek (Sep 15 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134007206):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> for small enough integers it stores them in 4-bytes, for bigger ones it uses the GMP multiprecision library</p>

#### [ Chris Hughes (Sep 15 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134007226):
<blockquote>
<p>How come the VM can deal with integers bigger than 2^32 if it is storing things in this classical manner?</p>
</blockquote>
<p>My guess is that a nat is 31 bits for the nat, plus one more bit that says we need more bits. An int is probably <code>30</code> bits plus a sign and one more bit for if we need more bits.</p>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">eval</span> <span class="bp">@</span><span class="n">unchecked_cast</span> <span class="n">nat</span> <span class="n">int</span> <span class="o">(</span><span class="mi">2</span> <span class="err">^</span> <span class="mi">30</span><span class="o">)</span> <span class="c1">-- -1073741824</span>
</pre></div>

#### [ Keeley Hoek (Sep 15 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134007280):
<p><a href="https://gmplib.org" target="_blank" title="https://gmplib.org">https://gmplib.org</a></p>

#### [ Kevin Buzzard (Sep 15 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134007294):
<p>rofl the "need help" bit.</p>

#### [ Reid Barton (Sep 15 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unchecked%20cast/near/134013568):
<p>Interesting, it hadn't occurred to me that you could define <code>unchecked_cast</code> (in <code>meta</code>) yourself, without a special constant.<br>
I wonder how badly you can break things with it. I tried casting a nat to a function nat -&gt; nat and then applying it, hoping for a crash, but all I got was a boring vm check failure.</p>


{% endraw %}
