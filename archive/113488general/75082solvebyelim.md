---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/75082solvebyelim.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [solve_by_elim](https://leanprover-community.github.io/archive/113488general/75082solvebyelim.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Mar 09 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123468417):
<p><span class="user-mention" data-user-email="simon.hudon@gmail.com" data-user-id="110026">@Simon Hudon</span>, the new solve_by_elim is really nice, and now I’d like it to do even more. I know that there is a mechanism to pass arbitrary assumptions, rather than using local context, and perhaps I should just use that.</p>

#### [ Scott Morrison (Mar 09 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123468426):
<p>But a particular thing I find myself using frequently now is applying eq.symm to various things in the context, before solve_by_elim can do its thing.</p>

#### [ Simon Hudon (Mar 09 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123468582):
<p>That's interesting. Maybe I could add <code>cc</code> to <code>solve_by_elim</code>. In terms of performance, I don't know what kind of slow down that would be but maybe this could be enabled by <code>solve_by_elim!</code></p>

#### [ Scott Morrison (Mar 09 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123468654):
<p>The other thing I'm finding I have to do is replace a hypothesis <code>h : f = g</code> with <code>funext</code> applied to it, to get <code>h' : \forall x : X, f x = g x</code>.</p>

#### [ Simon Hudon (Mar 09 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123468659):
<p>Can you try something for me? Write:</p>
<div class="codehilite"><pre><span></span>meta def my_solve_by_elim (asms : option (list expr) := none)  : opt_param ℕ 3 → tactic unit
| 0 := done
| (succ n) :=
apply_assumption asms $ cc &lt;|&gt; my_solve_by_elim n
</pre></div>


<p>and tell me if that does the job</p>

#### [ Scott Morrison (Mar 09 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123468660):
<p>Again, it would be nice to automate a bit.</p>

#### [ Scott Morrison (Mar 09 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123468663):
<p>I'll investigate, thanks.</p>

#### [ Simon Hudon (Mar 09 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123468795):
<p>For the second bit, maybe adding <code>simp [function.funext_iff] at *</code> before <code>solve_by_elim</code> would help.</p>

#### [ Simon Hudon (Mar 09 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123468807):
<p>(<code>function.funext_iff</code> is a new theorem in <code>mathlib</code>)</p>

#### [ Scott Morrison (Mar 09 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123468920):
<p>(ha, I'd actually just written <code>funext_iff</code> myself)</p>

#### [ Scott Morrison (Mar 09 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469450):
<p>No, <code>cc</code> doesn't seem to help here.</p>

#### [ Simon Hudon (Mar 09 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469466):
<p>Can you should me a situation where the issue arises?</p>

#### [ Scott Morrison (Mar 09 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469512):
<p>Oh -- a bug in solve_by_elim: the recursive call doesn't pass the arguments asms.</p>

#### [ Scott Morrison (Mar 09 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469531):
<p>Well, maybe this is too trivial ... :-)</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">f</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">my_solve_by_elim</span>
<span class="kn">end</span>
</pre></div>

#### [ Simon Hudon (Mar 09 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469532):
<p>It doesn't need to because it's declared on the left of <code>:</code></p>

#### [ Scott Morrison (Mar 09 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469535):
<p>ah, great, sorry.</p>

#### [ Simon Hudon (Mar 09 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469596):
<p>This example could be handled by <code>cc</code> on its own</p>

#### [ Scott Morrison (Mar 09 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469598):
<p>I guess it's obviously not going to help here...</p>

#### [ Kenny Lau (Mar 09 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469736):
<p>what does <code>solve_by_elim</code> do?</p>

#### [ Scott Morrison (Mar 09 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469744):
<p>repeatedly tries to apply hypotheses, discharging new goals created by <code>apply</code> by calling itself</p>

#### [ Scott Morrison (Mar 09 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469746):
<p>(i.e. discharging them by matching against other hypotheses)</p>

#### [ Simon Hudon (Mar 09 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469801):
<p><span class="user-mention" data-user-email="scott@tqft.net" data-user-id="110087">@Scott Morrison</span> Can you show me something that <code>cc</code> doesn't solve?</p>

#### [ Scott Morrison (Mar 09 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469857):
<p>I'll have to look further. I'll try to see how much <code>cc</code> and <code>solve_by_elim</code> together let me automate, and get back to you if I find such an example.</p>

#### [ Simon Hudon (Mar 09 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469863):
<p>cool :)</p>

#### [ Simon Hudon (Mar 09 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469907):
<p>btw, have you tried <code>tauto</code>? Does it help?</p>

#### [ Scott Morrison (Mar 09 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469930):
<p>no, I haven't looked much at tauto yet. I already have tactics that do a lot of automatic <code>cases</code>, so I'm guessing it won't help much?</p>

#### [ Scott Morrison (Mar 09 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469990):
<p>The other pattern I have all the time is: a hypothesis <code>p : x = y</code>, where <code>x</code> and <code>y</code> are terms of some structure type <code>S</code>, then I go: <code>have p' := congr_arg S.f p, solve_by_elim</code>.</p>

#### [ Scott Morrison (Mar 09 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123470004):
<p>It would be lovely to handle that automatically... that is, not just apply hypotheses, but apply structure fields <code>congr_arg</code>d over hypotheses.</p>

#### [ Simon Hudon (Mar 09 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123470117):
<p>That's an interesting case. It's a bit like funext_iff which we talked about earlier in that we infer the equality of the parts from the equality of the whole. I feel like there's probably a greek-letter-reduction for that</p>

#### [ Simon Hudon (Mar 09 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123470312):
<p>I'm wondering if <code>congr_arg</code> / <code>funext_iff</code> / <code>cc</code> might be the best combination</p>

#### [ Scott Morrison (Mar 09 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123470376):
<p>I'm not sure what you mean. I guess what I'm hoping for it some automation for finding the correct applications of <code>congr_arg</code>.</p>

#### [ Scott Morrison (Mar 09 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123470431):
<p>(i.e. work out for itself what the field <code>S.f</code> should be in my example above: <code>have p' := congr_arg S.f p</code>.)</p>

#### [ Simon Hudon (Mar 09 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123470446):
<p>If I see <code>x = y</code> where <code>x</code> and <code>y</code> are functions, I'd specialize <code>∀ i, x i = y i</code> for every <code>i</code> such that <code>x i</code> appears in the context. Same thing <code>y</code>. I'd do the same with the fields of structure types</p>

#### [ Simon Hudon (Mar 09 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123470504):
<p>I'll write something, make a PR to mathlib and send you a link. How about that?</p>

#### [ Scott Morrison (Mar 09 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123470518):
<p>sounds amazing :-)</p>

#### [ Simon Hudon (Mar 09 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123471150):
<p>Do you have an example where that would be useful? All the examples I can think of can be handled directly by <code>cc</code></p>

#### [ Scott Morrison (Apr 13 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125017118):
<p><code>cc</code> successfully solves</p>
<div class="codehilite"><pre><span></span>example {α β : Type} (f g : α → β) (w : g = f) (y : α) : f y = g y := by cc
</pre></div>


<p>but not</p>
<div class="codehilite"><pre><span></span>example {α β : Type} (f g : α → β) (w : (λ x, g x) = (λ x, f x)) (y : α) : f y = g y := by cc
</pre></div>


<p>Does anyone see some slight generalisation of <code>cc</code> (and/or possibly <code>solve_by_elim</code>) that can handle the second case?</p>

#### [ Scott Morrison (Apr 13 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125017465):
<p>This example is unnecessarily complicated, sorry: even this pair:</p>
<div class="codehilite"><pre><span></span>example {α β : Type} (f g : α → β) (w : f = g) (y : α) : f y = g y := by cc -- success
example {α β : Type} (f g : α → β) (w : (λ x, f x) = (λ x, g x)) (y : α) : f y = g y := by cc -- FAIL
</pre></div>

#### [ Scott Morrison (Apr 13 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125017472):
<p>shows what's going on</p>

#### [ Simon Hudon (Apr 13 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125017524):
<p>What happens if you call <code>simp</code> on <code>w</code> before <code>cc</code>? If it does eta reduction, then <code>cc</code> should succeed</p>

#### [ Scott Morrison (Apr 13 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125017540):
<p>That does work, but only because my MWE is too M!</p>

#### [ Scott Morrison (Apr 13 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125017603):
<p>Maybe </p>
<div class="codehilite"><pre><span></span>example {α : Type} (f g : α → α) (w : (λ x, f (f x)) = (λ x, g (g x))) (y : α) : f (f y) = g (g y) :=
</pre></div>


<p>shows more of what I want.</p>

#### [ Simon Hudon (Apr 13 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125017605):
<p>That sounds like my conversations with my advisor: "- what are you looking at now? - Large scale software. - Cool, do you have a small example to illustrate your idea? - ..."</p>

#### [ Mario Carneiro (Apr 13 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125017708):
<p>scott, you are talking higher order matching here. It's very unlikely you will get something as powerful as what you are envisioning. Your best bet is to apply (reverse) funext on your hypotheses to turn it into a first order problem</p>

#### [ Simon Hudon (Apr 13 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125017711):
<p>By reverse funext, do you mean <code>congr_fun</code>?</p>

#### [ Mario Carneiro (Apr 13 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125017722):
<p>yes, with some beta postprocessing</p>

#### [ Simon Hudon (Apr 13 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125017788):
<p>Maybe <span class="user-mention" data-user-id="110524">@Scott Morrison</span> would be satisfied with converting <code>f (f x)</code> to <code>(f o f) x</code>. Then <code>simp, cc</code> would be good enough.</p>

#### [ Mario Carneiro (Apr 13 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125018251):
<p>My point is that if <code>\forall x, f (f x) = g (g x)</code> was in the context instead of the lambda equality, I think cc would get it... maybe. (Honestly I don't understand how cc works, and I never trust it for anything significant.)</p>

#### [ Simon Hudon (Apr 13 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125018302):
<p>It seems to work a bit like the ematching feature of smt solvers, doesn't it? I wouldn't count on it to do any specialization</p>

#### [ Scott Morrison (Apr 13 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125018404):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span>, thanks, this had been my past solution, but I'd been a bit worried by it. I'll leave it in place for now.</p>

#### [ Simon Hudon (Apr 13 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125018449):
<p><span class="user-mention" data-user-id="110524">@Scott Morrison</span> Can you elaborate on why you prefer the equality between lambda terms?</p>

#### [ Scott Morrison (Apr 13 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125020210):
<p>It’s just that the earlier steps of my automation are giving my equalities<br>
between lambdas as hypotheses, and I’m having trouble automatically always<br>
getting these into a form that cc / solve_by_elim / rewrite_search can deal<br>
with. I think just replacing hypotheses which are equations between<br>
functions types with foralls will do the job, and doesn’t seem to cause<br>
problems elsewhere.</p>

#### [ Gabriel Ebner (Apr 13 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125022906):
<p>Congruence closure (<code>cc</code>) performs purely equational reasoning via congruences.  It can prove <code>a=b, c=b |- f a = f c</code>, but that's essentially it.  One nice feature is that since it uses the congruence lemmas, it effectively ignores subsingleton arguments.</p>

#### [ Gabriel Ebner (Apr 13 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125022965):
<p>It definitely won't solve <code> forall x, f x = g x |- f a = g a</code> or <code>fun x, f x = g x |- f a = g a</code>.  (They're clearly equivalent via funext, as you've observed.)  If you solve such problems, then you have a first-order prover---and this is out of scope for <code>cc</code>.  Congruence closure is supposed to be fast, predictable, and well, do congruence closure (and not general first-order proving).</p>

#### [ Gabriel Ebner (Apr 13 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125023122):
<p>Re: E-matching.  Yes, you can solve the example with <code>forall x, f x = g x</code> using it (I think <code>by[smt] eblast</code> should do it).  What E-matching does is that it heuristically generates instances of universally quantified formulas (I think the <code>ematch</code> tactic uses the local context and lemmas tagged <code>[ematch]</code>).   In the example it would generate the instance <code>f y = g y</code>, and with this instance <code>cc</code> can solve the goal.  The instance <code>f y = g y</code> is generated because the <em>trigger</em> <code>f ?m_1</code> (in this example the lhs of the lemma)  E-<em>matches</em> a currently known subterm, namely <code>f y</code> (the lhs of the target in the example).</p>

#### [ Scott Morrison (Apr 18 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125222682):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span>, how would you feel about generalising the definition of <code>solve_by_elim</code> to </p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">solve_by_elim</span> <span class="o">(</span><span class="n">asms</span> <span class="o">:</span> <span class="n">option</span> <span class="o">(</span><span class="n">list</span> <span class="n">expr</span><span class="o">)</span> <span class="o">:=</span> <span class="n">none</span><span class="o">)</span> <span class="o">(</span><span class="n">discharger</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">done</span><span class="o">)</span> <span class="o">:</span> <span class="n">opt_param</span> <span class="bp">ℕ</span> <span class="mi">3</span> <span class="bp">→</span> <span class="n">tactic</span> <span class="n">unit</span>
<span class="bp">|</span> <span class="mi">0</span>     <span class="o">:=</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">done</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="n">discharger</span> <span class="bp">&lt;|&gt;</span> <span class="o">(</span><span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span><span class="bp">.</span><span class="n">apply_assumption</span> <span class="n">asms</span> <span class="err">$</span> <span class="n">solve_by_elim</span> <span class="n">n</span><span class="o">)</span>
</pre></div>


<p>I find myself using this as <code>solve_by_elim none cc</code> frequently and it's very helpful.</p>

#### [ Mario Carneiro (Apr 18 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125223029):
<p>Won't you have to write this as <code>tactic.cc</code> in an interactive tactic script?</p>

#### [ Simon Hudon (Apr 18 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125223045):
<p>I like it. Let's switch the order of <code>asms</code> and <code>discharger</code> though.</p>

#### [ Simon Hudon (Apr 18 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125223109):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Why? <code>cc</code> is also in <code>tactic.interactive</code>, no?</p>

#### [ Mario Carneiro (Apr 18 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125223202):
<p>but if it's not being parsed in interactive mode, you have to use the right namespace</p>

#### [ Mario Carneiro (Apr 18 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125223249):
<p>one option is to have an <code>itactic</code> for the discharger, then you can write <code>{cc}</code> or some other tactic block</p>

#### [ Simon Hudon (Apr 18 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125223254):
<p>Right. Alternatively, we can provide a variant such as <code>solve_by_elim_with { cc }</code> with a <code>itactic</code> argument (and a better name)</p>

#### [ Mario Carneiro (Apr 18 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125223261):
<p>I think you can still make it optional</p>

#### [ Simon Hudon (Apr 18 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125223279):
<p>No because <code>itactic</code> doesn't use the same parsing framework as everything else</p>

#### [ Mario Carneiro (Apr 18 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125223288):
<p>Have you used <code>asms</code>? I think it needs a parser</p>

#### [ Simon Hudon (Apr 18 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125223349):
<p>If we don't want multiple tactic names, we'd have to live with <code>solve_by_elim { }</code> when we don't use that feature.</p>

#### [ Mario Carneiro (Apr 18 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125223360):
<p>or stick with just passing a regular tactic and live with <code>solve_by_elim `[cc]</code></p>

#### [ Simon Hudon (Apr 18 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125223417):
<blockquote>
<p>Have you used <code>asms</code>? I think it needs a parser</p>
</blockquote>
<p>I haven't used it in interactive mode. I think similarly to the options that you can feed <code>simp</code> (e.g. <code>{ single_pass := tt }</code>) you can give it a literal as an expression</p>

#### [ Scott Morrison (Apr 20 2018 at 03:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125335574):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> just checking -- should I PR this, or would you prefer to do it? I'm happy either way.</p>

#### [ Scott Morrison (Jun 23 2018 at 04:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504293):
<p>Hi @SimonHudon, I'm finding often <code>solve_by_elim</code> would succeed, except for the fact that an applicable equation needs to be wrapped in <code>eq.symm</code> first. In this case, <code>{discharger := cc}</code> works, but this tends to be very expensive and I'd really like to avoid it.</p>

#### [ Scott Morrison (Jun 23 2018 at 04:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504299):
<p>It's certainly possible to pass a more limited discharger, that just tries to apply hypotheses backwards, but I'm wondering what you think about building this behaviour in?</p>

#### [ Scott Morrison (Jun 23 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504331):
<p>(e.g. by writing a version of <code>apply</code> that knows about symmetric relations, and then using that --- I'd be happy to implement if you thought this was reasonable behaviour)</p>

#### [ Simon Hudon (Jun 23 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504349):
<p>I think that's feasible. We could probably define it as <code>sym_apply (r) := apply r &lt;|&gt; (symmetry &gt;&gt; apply r)</code></p>

#### [ Scott Morrison (Jun 23 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504366):
<p>oh, that's much sneakier than what I had in mind</p>

#### [ Scott Morrison (Jun 23 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504392):
<p>Currently in <code>apply_assumption</code> you do an initial filtering step by <code>find_matching_head</code>, and I guess this wouldn't be viable.</p>

#### [ Scott Morrison (Jun 23 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504400):
<p>Do you know if this actually saves much time? I'd hope that <code>apply</code> returns very quickly on anything <code>find_matching_head</code> had discarded.</p>

#### [ Simon Hudon (Jun 23 2018 at 04:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504510):
<p>You're right. I have a feeling we could get rid of the filtering. I'm not sure that testing the assumptions is any faster than just applying them</p>

#### [ Simon Hudon (Jun 23 2018 at 04:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504515):
<p>It might actually be slower because we might be doing the same work twice</p>

#### [ Simon Hudon (Jun 23 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504570):
<p>I naively copied the behavior of <code>assumption</code> when I wrote that tactic. I didn't spend too much time thinking of the performances. It might be interesting to remove the filtering and measure the performances before adding the symmetry</p>

#### [ Simon Hudon (Jun 23 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504777):
<p>The other thing I'm wondering is if we should try every assumption directly first and only then try symmetry or try symmetry as we go. The upside of the first approach is that when you don't need symmetry, you get better performances. The downside is that you can't say that the tactic applies "the first assumption that matches" anymore. If assumption 11 matches directly and assumption 2 matches modulo symmetry, which one do we want the tactic to pick?</p>

#### [ Scott Morrison (Jun 23 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504778):
<p>Hmm... my preference is to just make the change. :-) We do need some better tools for measuring performance. I know I neglect doing it, and then suffer for it later. (e.g. just now realising that letting solve_by_elim call <code>cc</code> can be very expensive)</p>

#### [ Simon Hudon (Jun 23 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504831):
<p>I would prefer just making the change too. I guess the rest is for extra credits :D</p>

#### [ Scott Morrison (Jun 23 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504832):
<p>interesting... my inclination is to try symmetry as we go. When we're using <code>apply</code>, the semantic difference between <code>a=b</code> and <code>b=a</code> has pretty much disappeared.</p>

#### [ Scott Morrison (Jun 23 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504837):
<p>In that case, <a href="https://github.com/leanprover/mathlib/pull/164" target="_blank" title="https://github.com/leanprover/mathlib/pull/164">https://github.com/leanprover/mathlib/pull/164</a></p>

#### [ Simon Hudon (Jun 23 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504879):
<p>I prefer that too. And my intuition is that the difference in performances will be unnoticeable</p>

#### [ Simon Hudon (Jun 23 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504886):
<p>That was fast!</p>

#### [ Simon Hudon (Jun 23 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504899):
<p>The added benefit is the code gets shorter and neater :)</p>

#### [ Simon Hudon (Jun 23 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504904):
<p>Would you care to add a test case?</p>

#### [ Scott Morrison (Jun 23 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504957):
<p>Sure!</p>


{% endraw %}
