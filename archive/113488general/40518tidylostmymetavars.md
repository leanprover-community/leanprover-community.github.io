---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/40518tidylostmymetavars.html
---

## Stream: [general](index.html)
### Topic: [tidy lost my metavars](40518tidylostmymetavars.html)

---


{% raw %}
#### [ Johan Commelin (Nov 29 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148774987):
<p>Somehow <code>tidy</code> claims it closed all goals, but the kernel says there are still metavariables left. Is there a good approach to debugging this? Somewhere a metavariable got removed from the goal-list without being fully instantiated. I guess it should be possible to track this, right?</p>

#### [ Mario Carneiro (Nov 29 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148776730):
<p>it is possible to write a tactic that will tell you if the current tactic state is broken, but you will have to sprinkle it around and it will often give false positives because of <code>focus</code> and such</p>

#### [ Mario Carneiro (Nov 29 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148776794):
<p>the <code>recover</code> tactic does this, essentially</p>

#### [ Johan Commelin (Nov 29 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148776998):
<p>Thanks. Didn't know about <code>recover</code>. I'll try it out.</p>

#### [ Johan Commelin (Nov 29 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148782330):
<p>Oh by the way, <code>recover</code> worked. It figured out that there was some naturality condition that wasn't proven. I don't know how it got lost.</p>

#### [ Keeley Hoek (Nov 29 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148782541):
<p>It'd be really great to see a reproducible case of that Johan, probably there is a bug in a tactic somewhere</p>

#### [ Johan Commelin (Nov 29 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148783366):
<p><span class="user-mention" data-user-id="110111">@Keeley Hoek</span> <a href="https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/presheaf.lean#L113" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/presheaf.lean#L113">https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/presheaf.lean#L113</a><br>
Voila. I retried this with a freshly restarted Lean. Problem still occurs. I have no idea how I could build a MWE out of this. It's pretty deep down in ugly maths.</p>

#### [ Keeley Hoek (Nov 29 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148786857):
<p>Seems like a bug in <code>constructor</code> to me</p>

#### [ Keeley Hoek (Nov 29 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148786936):
<p>For anyone who is interested:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">oopsie</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">C</span> <span class="err">⥤</span> <span class="n">D</span><span class="o">)</span> <span class="o">:</span> <span class="n">functor</span><span class="bp">.</span><span class="n">id</span> <span class="o">(</span><span class="n">presheaf</span> <span class="n">C</span><span class="o">)</span> <span class="err">⟹</span> <span class="n">yoneda_extension</span> <span class="n">F</span> <span class="err">⋙</span> <span class="n">restricted_yoneda</span> <span class="n">F</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">constructor</span><span class="o">,</span>
  <span class="c1">-- One goal</span>
  <span class="n">recover</span><span class="o">,</span>
  <span class="c1">-- Two goals :O</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Nov 29 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148786989):
<p>But I guess this ties in to the auto_params, doesn't it?</p>

#### [ Keeley Hoek (Nov 29 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148787002):
<p>I'm not sure I understand</p>

#### [ Keeley Hoek (Nov 29 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148787009):
<p>I mean, surely it shouldn't erase a metavar it creates from history</p>

#### [ Johan Commelin (Nov 29 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148787015):
<p>Maybe <code>constructor</code> is throwing away goals that have an auto_param attached to them?</p>

#### [ Keeley Hoek (Nov 29 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148787126):
<p>I wonder if the <code>extract_opt_auto_param</code> in <code>get_constructors_for</code> has anything to do with it<br>
Actually, I bet it is the <code>mk_const</code> on line 23 of constructor_tactic.lean in lean core</p>

#### [ Keeley Hoek (Nov 29 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148787138):
<p>That could create metavariables which don't get fully bound by the <code>apply</code> maybe</p>

#### [ Johan Commelin (Nov 29 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20lost%20my%20metavars/near/148787258):
<p>Thanks for debugging this!</p>


{% endraw %}
