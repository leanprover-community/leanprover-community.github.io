---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/58662Additivegrouphomeomorphismsonfields.html
---

## Stream: [new members](index.html)
### Topic: [Additive group homeomorphisms on fields](58662Additivegrouphomeomorphismsonfields.html)

---


{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Jan 11 2019 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907204):
<p>Since fields extend additive groups , I thought that something <code>hom_int_to_field</code> below should work:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">field</span>
<span class="kn">import</span> <span class="n">field_theory</span><span class="bp">.</span><span class="n">subfield</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">K</span> <span class="n">L</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">field</span> <span class="n">K</span><span class="o">]</span> <span class="o">[</span><span class="n">field</span> <span class="n">L</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">K</span> <span class="bp">→</span> <span class="n">L</span><span class="o">)</span>

<span class="n">def</span> <span class="n">nat_to_field</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">K</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="n">nat_to_field</span><span class="o">(</span><span class="n">n</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">1</span>

<span class="n">def</span> <span class="n">int_to_field</span> <span class="o">:</span> <span class="bp">ℤ</span> <span class="bp">→</span> <span class="n">K</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">of_nat</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="n">nat_to_field</span> <span class="n">n</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">neg_succ_of_nat</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">-</span><span class="o">(</span><span class="mi">1</span> <span class="bp">+</span> <span class="n">nat_to_field</span><span class="o">(</span><span class="n">n</span><span class="o">))</span>

<span class="kn">theorem</span> <span class="n">hom_int_to_field</span> <span class="o">:</span> <span class="n">is_add_group_hom</span> <span class="n">int_to_field</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>But it doesn't -- it tells me it can't synthesise the instance. Instead, I need to create a proof that <code>K</code> is an additive group, give it a name:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">AK</span> <span class="o">:</span> <span class="n">add_group</span> <span class="n">K</span> <span class="o">:=</span>
<span class="o">{</span>   <span class="n">add</span> <span class="o">:=</span> <span class="n">has_add</span><span class="bp">.</span><span class="n">add</span><span class="o">,</span>
    <span class="n">add_assoc</span> <span class="o">:=</span> <span class="n">add_monoid</span><span class="bp">.</span><span class="n">add_assoc</span><span class="o">,</span>
    <span class="n">zero</span> <span class="o">:=</span> <span class="mi">0</span><span class="o">,</span>
    <span class="n">zero_add</span> <span class="o">:=</span> <span class="n">add_monoid</span><span class="bp">.</span><span class="n">zero_add</span><span class="o">,</span>
    <span class="n">add_zero</span> <span class="o">:=</span> <span class="n">add_monoid</span><span class="bp">.</span><span class="n">add_zero</span><span class="o">,</span>
    <span class="n">neg</span> <span class="o">:=</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">neg</span><span class="o">,</span>
    <span class="n">add_left_neg</span> <span class="o">:=</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">add_left_neg</span> <span class="o">}</span>
</pre></div>


<p>And then use it:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">hom_int_to_field</span> <span class="o">:</span> <span class="bp">@</span><span class="n">is_add_group_hom</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">AK</span> <span class="o">:</span> <span class="n">add_group</span> <span class="n">K</span><span class="o">)</span> <span class="n">int_to_field</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>Can't I use the fact that fields are -- by definition -- additive groups?</p>

#### [ Johan Commelin (Jan 11 2019 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907306):
<p>You know about <code>int.cast</code>?</p>

#### [ Johan Commelin (Jan 11 2019 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907333):
<p>It is your <code>int_to_field</code>, for arbitrary rings</p>

#### [ Abhimanyu Pallavi Sudhir (Jan 11 2019 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907334):
<p>Oh, I didn't know it casted to a general field. Yes, <code>int.cast.is_ring_hom</code></p>

#### [ Johan Commelin (Jan 11 2019 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907414):
<p>And somewhere there must be a proof that it is a ring hom</p>

#### [ Johan Commelin (Jan 11 2019 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907423):
<p>But that doesn't answer why your instance can't be found.</p>

#### [ Johan Commelin (Jan 11 2019 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907425):
<p>I don't know what's wrong there.</p>

#### [ Johan Commelin (Jan 11 2019 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907451):
<p>(Also, mathematician's field is <code>discrete_field</code>. For reasons that I don't get. Since I'm a mathematician <span class="emoji emoji-1f648" title="see no evil">:see_no_evil:</span>)</p>

#### [ Abhimanyu Pallavi Sudhir (Jan 11 2019 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907550):
<p>Oh -- what about subfields? Is there a "discrete subfield"?</p>

#### [ Johan Commelin (Jan 11 2019 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907558):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> <span class="emoji emoji-2b06" title="up">:up:</span></p>

#### [ Kenny Lau (Jan 11 2019 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907566):
<p>I think every subfield of a discrete field is discrete by default</p>

#### [ Kenny Lau (Jan 11 2019 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907568):
<p>but I don't think this is in mathlib yet</p>

#### [ Abhimanyu Pallavi Sudhir (Jan 11 2019 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907673):
<p>And discrete field homeomorphisms? Can I just use <code>is_field_hom</code>?</p>

#### [ Kenny Lau (Jan 11 2019 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154907740):
<p>yes</p>

#### [ Abhimanyu Pallavi Sudhir (Jan 11 2019 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154908228):
<blockquote>
<p>But that doesn't answer why your instance can't be found.</p>
</blockquote>
<p>If I change <code>theorem</code> to <code>instance</code>, it works.</p>

#### [ Abhimanyu Pallavi Sudhir (Jan 11 2019 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Additive%20group%20homeomorphisms%20on%20fields/near/154908234):
<p>That's how they do it in mathlib.</p>


{% endraw %}
