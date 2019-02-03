---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52419typemismatcherror.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [type mismatch error](https://leanprover-community.github.io/archive/113488general/52419typemismatcherror.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Nov 09 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375133):
<p>I don't have a good strategy for debugging errors like this:</p>
<div class="codehilite"><pre><span></span><span class="n">type</span> <span class="n">mismatch</span> <span class="n">at</span> <span class="n">application</span>
  <span class="n">galois_connection</span><span class="bp">.</span><span class="n">l_supr</span> <span class="n">opens</span><span class="bp">.</span><span class="n">gc</span>
<span class="n">term</span>
  <span class="n">opens</span><span class="bp">.</span><span class="n">gc</span>
<span class="n">has</span> <span class="n">type</span>
  <span class="n">galois_connection</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">val</span> <span class="n">opens</span><span class="bp">.</span><span class="n">interior</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="n">galois_connection</span> <span class="err">?</span><span class="n">m_5</span> <span class="err">?</span><span class="n">m_6</span>
</pre></div>


<p>My initial reaction is: Hey Lean, look, you just figured out what <code>?m_5</code> and <code>?m_6</code> are. Unify, and move on.<br>
But apparently Lean thinks otherwise...</p>

#### [ Kenny Lau (Nov 09 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375216):
<p>I would <code>set_option pp.all true</code>, but that's me</p>

#### [ Johan Commelin (Nov 09 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375240):
<p>I'll try, but I fear that I get something extremely long and complicated.</p>

#### [ Kenny Lau (Nov 09 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375263):
<p>I'm not afraid of that</p>

#### [ Rob Lewis (Nov 09 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375316):
<p>This pattern shows up a lot when there's a type class argument to <code>galois_connection.l_supr</code> that <code>opens.gc</code> doesn't satisfy.</p>

#### [ Johan Commelin (Nov 09 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375361):
<p>Hmmm, it's even reasonable short:</p>
<div class="codehilite"><pre><span></span>type mismatch at application
  @galois_connection.l_supr.{?l_1 ?l_2 ?l_3} ?m_4 ?m_5 ?m_6 ?m_7 ?m_8 ?m_9 ?m_10
    (@topological_space.opens.gc.{?l_11} ?m_12 ?m_13)
term
  @topological_space.opens.gc.{?l_1} ?m_2 ?m_3
has type
  @galois_connection.{?l_1 ?l_1}
    (@subtype.{(max (?l_1+1) 1)} (set.{?l_1} ?m_2) (λ (s : set.{?l_1} ?m_2), @is_open.{?l_1} ?m_2 ?m_3 s))
    (set.{?l_1} ?m_2)
    (@subtype.preorder.{?l_1} (set.{?l_1} ?m_2)
       (@partial_order.to_preorder.{?l_1} (set.{?l_1} ?m_2)
          (@lattice.order_bot.to_partial_order.{?l_1} (set.{?l_1} ?m_2)
             (@lattice.bounded_lattice.to_order_bot.{?l_1} (set.{?l_1} ?m_2)
                (@lattice.complete_lattice.to_bounded_lattice.{?l_1} (set.{?l_1} ?m_2)
                   (@set.lattice_set.{?l_1} ?m_2)))))
       (λ (s : set.{?l_1} ?m_2), @is_open.{?l_1} ?m_2 ?m_3 s))
    (@partial_order.to_preorder.{?l_1} (set.{?l_1} ?m_2)
       (@lattice.order_bot.to_partial_order.{?l_1} (set.{?l_1} ?m_2)
          (@lattice.bounded_lattice.to_order_bot.{?l_1} (set.{?l_1} ?m_2)
             (@lattice.complete_lattice.to_bounded_lattice.{?l_1} (set.{?l_1} ?m_2) (@set.lattice_set.{?l_1} ?m_2)))))
    (@subtype.val.{(max (?l_1+1) 1)} (set.{?l_1} ?m_2) (λ (s : set.{?l_1} ?m_2), @is_open.{?l_1} ?m_2 ?m_3 s))
    (@topological_space.opens.interior.{?l_1} ?m_2 ?m_3)
but is expected to have type
  @galois_connection.{?l_1 ?l_2} ?m_3 ?m_4
    (@partial_order.to_preorder.{?l_1} ?m_3
       (@lattice.order_bot.to_partial_order.{?l_1} ?m_3
          (@lattice.bounded_lattice.to_order_bot.{?l_1} ?m_3
             (@lattice.complete_lattice.to_bounded_lattice.{?l_1} ?m_3 ?m_5))))
    (@partial_order.to_preorder.{?l_2} ?m_4
       (@lattice.order_bot.to_partial_order.{?l_2} ?m_4
          (@lattice.bounded_lattice.to_order_bot.{?l_2} ?m_4
             (@lattice.complete_lattice.to_bounded_lattice.{?l_2} ?m_4 ?m_6))))
</pre></div>

#### [ Johan Commelin (Nov 09 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375378):
<p><span class="user-mention" data-user-id="110596">@Rob Lewis</span> That's probably what's going on here.</p>

#### [ Kenny Lau (Nov 09 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375392):
<p>when I can't handle it, I use <a href="https://text-compare.com" target="_blank" title="https://text-compare.com">https://text-compare.com</a></p>

#### [ Kenny Lau (Nov 09 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375456):
<p>and in some rare cases it's some universe issues</p>

#### [ Johan Commelin (Nov 09 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375481):
<p>Otoh, I think all typeclass instances ought to be satisfied.</p>

#### [ Johan Commelin (Nov 09 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375700):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> There are two <code>sorry</code>s in <code>sheaf.lean</code>. They are math-trivial, but I find them Lean-hard.</p>

#### [ Kenny Lau (Nov 09 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375716):
<p>link?</p>

#### [ Johan Commelin (Nov 09 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375725):
<p>If you have some time, I would be really happy if you could take a look.</p>

#### [ Johan Commelin (Nov 09 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375762):
<p><a href="https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/sheaf.lean#L262" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/sheaf.lean#L262">https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/sheaf.lean#L262</a></p>

#### [ Kenny Lau (Nov 09 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375817):
<p>I think you have a rather different definition of "math-trivial"</p>

#### [ Johan Commelin (Nov 09 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375819):
<p>What this is saying is, you've got an open set <code>V</code> and a cover <code>Us</code> of an open set <code>U</code>. And <code>V ⊆ U</code>.</p>

#### [ Johan Commelin (Nov 09 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375831):
<p>Now you intersect all the <code>Ui</code> in <code>Us</code> with <code>V</code>, and the result covers <code>V</code>.</p>

#### [ Kenny Lau (Nov 09 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375838):
<p>can you show me the context?</p>

#### [ Johan Commelin (Nov 09 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375850):
<p>You mean explain the context?</p>

#### [ Kenny Lau (Nov 09 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375853):
<p>no, the context</p>

#### [ Johan Commelin (Nov 09 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375866):
<p>Aaah</p>

#### [ Johan Commelin (Nov 09 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375878):
<div class="codehilite"><pre><span></span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">X</span><span class="o">,</span>
<span class="n">U</span> <span class="n">V</span> <span class="o">:</span> <span class="n">opens</span> <span class="n">X</span><span class="o">,</span>
<span class="n">i</span> <span class="o">:</span> <span class="n">V</span> <span class="err">⟶</span> <span class="n">U</span><span class="o">,</span>
<span class="n">Us</span> <span class="o">:</span> <span class="n">covering_family</span> <span class="n">U</span><span class="o">,</span>
<span class="n">Us_cover</span> <span class="o">:</span> <span class="n">U</span> <span class="bp">=</span> <span class="err">⨆</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="n">over</span> <span class="n">U</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">u</span> <span class="err">∈</span> <span class="n">Us</span><span class="o">),</span> <span class="n">u</span><span class="bp">.</span><span class="n">left</span>
<span class="err">⊢</span> <span class="n">V</span><span class="bp">.</span><span class="n">val</span> <span class="bp">≤</span> <span class="o">(</span><span class="err">⨆</span> <span class="o">(</span><span class="n">Ui</span> <span class="o">:</span> <span class="n">over</span> <span class="n">U</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">Ui</span> <span class="err">∈</span> <span class="n">Us</span><span class="o">),</span> <span class="o">((</span><span class="n">over</span><span class="bp">.</span><span class="n">comap</span> <span class="n">i</span><span class="o">)</span><span class="bp">.</span><span class="n">obj</span> <span class="n">Ui</span><span class="o">)</span><span class="bp">.</span><span class="n">left</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span>
</pre></div>

#### [ Johan Commelin (Nov 09 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375942):
<p>So I want to show that <code>V ⊆ ⨆ Ui, (V ∩ Ui)</code>.</p>

#### [ Johan Commelin (Nov 09 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375950):
<p>That is the math version of the goal.</p>

#### [ Kenny Lau (Nov 09 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375958):
<p>where is V on the right hand side?</p>

#### [ Johan Commelin (Nov 09 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375972):
<p><code>V : opens X</code></p>

#### [ Johan Commelin (Nov 09 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375980):
<p>Aah, it is hidden in <code>comap i</code></p>

#### [ Johan Commelin (Nov 09 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147375990):
<p>Which in this setting just means: <code>V ∩ _</code></p>

#### [ Johan Commelin (Nov 09 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376084):
<p>Now I would think that <code>opens.gc</code> should let me transform the right hand side from<br>
<code>(⨆ (Ui : over U) (H : Ui ∈ Us), ((over.comap i).obj Ui).left).val</code> into<br>
<code>⨆ (Ui : over U) (H : Ui ∈ Us), (((over.comap i).obj Ui).left).val</code>.<br>
(I moved a parentheses to before <code>over.comap</code>.)</p>

#### [ Kenny Lau (Nov 09 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376244):
<p>do you know what it is definitionally equivalent to?</p>

#### [ Kenny Lau (Nov 09 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376250):
<p>if not can you just unfold everything?</p>

#### [ Johan Commelin (Nov 09 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376252):
<p>If this goal could be transformed into <code>V.val ∩ Ui.left.val ≤ (over.comap i) blah).val</code> for all <code>Ui</code>, then I could take it from there.</p>

#### [ Kenny Lau (Nov 09 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376399):
<p>if you <code>intro x</code>, then <code>i x</code> says that <code>x \in U</code> right</p>

#### [ Kenny Lau (Nov 09 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376408):
<p>then you rewrite <code>Us_cover</code></p>

#### [ Johan Commelin (Nov 09 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376455):
<p>Ok</p>

#### [ Kenny Lau (Nov 09 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376463):
<p>so now it says <code>x \in set.bUnion _</code></p>

#### [ Johan Commelin (Nov 09 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376471):
<p><del>Make that an <code>x</code></del></p>

#### [ Kenny Lau (Nov 09 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376502):
<p>then <code>set.mem_bUnion_iff</code> or something should give you something useful</p>

#### [ Johan Commelin (Nov 09 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376505):
<p>Now I want to extract a <code>Ui</code> that contains <code>x</code></p>

#### [ Johan Commelin (Nov 09 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376520):
<p>Aah, let me try to find that one.</p>

#### [ Johan Commelin (Nov 09 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376595):
<p>Except that it is a <code>supr</code> instead of a <code>bUnion</code>.</p>

#### [ Kenny Lau (Nov 09 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376607):
<p>aren't they defeq?</p>

#### [ Johan Commelin (Nov 09 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376616):
<p>There should be a <code>lattice.mem_supr_iff</code>.</p>

#### [ Johan Commelin (Nov 09 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376618):
<p>Aah, probably yes. I'll try.</p>

#### [ Kenny Lau (Nov 09 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376619):
<p>you can't be the member of just any supremum</p>

#### [ Johan Commelin (Nov 09 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376886):
<p>Yay! First use of <code>erw</code> in my Lean-life. Context is now</p>
<div class="codehilite"><pre><span></span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">X</span><span class="o">,</span>
<span class="n">U</span> <span class="n">V</span> <span class="o">:</span> <span class="n">opens</span> <span class="n">X</span><span class="o">,</span>
<span class="n">i</span> <span class="o">:</span> <span class="n">V</span> <span class="err">⟶</span> <span class="n">U</span><span class="o">,</span>
<span class="n">Us</span> <span class="o">:</span> <span class="n">covering_family</span> <span class="n">U</span><span class="o">,</span>
<span class="n">Us_cover</span> <span class="o">:</span> <span class="n">U</span> <span class="bp">=</span> <span class="err">⨆</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="n">over</span> <span class="n">U</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">u</span> <span class="err">∈</span> <span class="n">Us</span><span class="o">),</span> <span class="n">u</span><span class="bp">.</span><span class="n">left</span><span class="o">,</span>
<span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">,</span>
<span class="n">hx</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">V</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span>
<span class="n">this</span> <span class="o">:</span>
  <span class="bp">∃</span> <span class="o">(</span><span class="n">x_1</span> <span class="o">:</span> <span class="n">order_dual</span> <span class="o">(</span><span class="n">opens</span> <span class="n">X</span><span class="o">)),</span>
    <span class="n">x_1</span> <span class="err">∈</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">opens</span> <span class="n">X</span> <span class="bp">|</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">over</span> <span class="n">U</span><span class="o">),</span> <span class="n">a</span> <span class="bp">=</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="n">over</span> <span class="n">U</span><span class="o">),</span> <span class="err">⨆</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">u</span> <span class="err">∈</span> <span class="n">Us</span><span class="o">),</span> <span class="n">u</span><span class="bp">.</span><span class="n">left</span><span class="o">)</span> <span class="n">i</span><span class="o">}</span> <span class="bp">∧</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">x_1</span><span class="bp">.</span><span class="n">val</span>
<span class="err">⊢</span> <span class="n">x</span> <span class="err">∈</span> <span class="o">(</span><span class="err">⨆</span> <span class="o">(</span><span class="n">Ui</span> <span class="o">:</span> <span class="n">over</span> <span class="n">U</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">Ui</span> <span class="err">∈</span> <span class="n">Us</span><span class="o">),</span> <span class="o">((</span><span class="n">over</span><span class="bp">.</span><span class="n">comap</span> <span class="n">i</span><span class="o">)</span><span class="bp">.</span><span class="n">obj</span> <span class="n">Ui</span><span class="o">)</span><span class="bp">.</span><span class="n">left</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span>
</pre></div>

#### [ Johan Commelin (Nov 09 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147376921):
<p>That looks encouraging, right? Especially that <code>order_dual</code> that is leaking through.</p>

#### [ Johan Commelin (Nov 09 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20error/near/147377202):
<p>Ok, need to go. But now I think I can complete this. Thanks a lot!</p>


{% endraw %}
