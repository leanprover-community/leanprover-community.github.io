---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/15619implementationissues.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [implementation issues](https://leanprover-community.github.io/archive/113488general/15619implementationissues.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Sep 11 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133692574):
<p>Implementation issues occasionally have knock-on effects. For example the coercion <code>of_nat</code> from <code>nat</code> to <code>int</code> is not a generic coercion from <code>nat</code> to a monoid with 0 and 1, and as a consequence all of the standard coercion lemmas like <code>\u(a+b)=\u a+\u b</code> have to be proved for <code>of_nat</code>separately, giving us <code>int.coe_nat_add</code> as well as <code>nat.cast_add</code>.</p>
<p>My understanding from conversations here is that <code>of_nat</code> is a special case, as it is actually a constructor for <code>int</code> and is hence more efficient. However when it comes to computations we all know that <code>nat</code> is absurdly inefficient, anyone who is doing computations will be using <code>pnum</code> or <code>num</code> or whatever -- the binary version of <code>nat</code> which has been specifically designed to be harder to reason with but more efficient to compute with.</p>
<p>When I arrived here I just assumed that <code>int</code> would be defined the way it's typically defined in a mathematics class -- the quotient of <code>nat x nat</code> by the usual equivalence relation. But it isn't, it's defined in a much more direct and probably quite sensible way. Similarly <code>rat</code> is actually defined as a pair <code>(n,d)</code> of an integer numerator, a positive nat denominator, and a proof that they're coprime. My impression from this is that for some reason quotients are to be avoided -- they are less efficient or less computable in some way. This came up today when discussing polynomials with undergraduates -- someone suggested that a polynomial in one variable could be implemented as a list of coefficients, and I pointed out that leading zeros meant that it would have to be a quotient of list and this might well make it less computationally efficient or something. But then it occurred to me that actually they're defined as finsupps, which need finsets, which are multisets plus a theorem, and a multiset is a nightmarish quotient of list by some extremely delicate and hard to work with equivalence relation which in practice anyone using multiset other than developers stays well away from. Looking at it this way, it looks to me that in terms of sheer content of what is going on, defining polynomials in 1 variable as lists modulo "we're the same modulo a bunch of zeros at the end" looks to have far less baggage associated with it than this finsupp/finset/multiset/list.perm.setoid approach.</p>
<p>So what exactly is informing these decisions? Why do we use nat at all? <code>num</code> is better, we could prove all the right induction etc lemmas for it, etc. Similarly, <code>list.perm.setoid</code> seems to ultimately rely on the fact that every automorphism of [0,n-1] can be written as a possibly huge product of swaps of consecutive nats, which is a terrible way to do permutation groups from the point of view of computation. As a mathematician all I care about is the theorems, but it seems to me that from a computational perspective Lean is in some sense a disaster -- it wasn't designed to do computations -- so why am I having to jump through all these hoops to prove results about coercions from nat to int?</p>

#### [ Reid Barton (Sep 11 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133693662):
<p>So one thing is that anything that's a Prop doesn't exist at runtime at all. And a quotient is just represented by a value of the underlying type. So in the VM, a <code>multiset</code> just looks like a <code>list</code>--there are no actual big products of transpositions.</p>
<p>The issue with using quotients for <code>int</code> and <code>rat</code> is that you could then end up with arbitrarily large representations of the same value of Z (0 = "N - N" for large N) or of Q (1 = "N/N" for large N). This issue doesn't come up for <code>multiset</code> and its relatives because all of the equivalent representations have the same size.</p>

#### [ Reid Barton (Sep 11 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133693807):
<blockquote>
<p>So what exactly is informing these decisions? Why do we use nat at all? num is better, we could prove all the right induction etc lemmas for it, etc.</p>
</blockquote>
<p>You could prove the induction lemmas, but then when you define, say, factorial by induction, it would not be true <em>by definition</em> that (n+1)! = (n+1) * n!. It would be only a propositional equality.</p>

#### [ Kevin Buzzard (Sep 11 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133693881):
<p>I don't even understand what we are trying to make "efficient" here. If I wanted to compute 100! I would not be using Lean. What I would like to be efficient in practice is that I would like mathlib to compile quickly, and I would like the orange bars to disappear more quickly when I am in the middle of a 200-line proof. Is this in any way related to decisions about using nat not num to represent naturals?</p>

#### [ Mario Carneiro (Sep 11 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694125):
<blockquote>
<p>If I wanted to compute 100! I would not be using Lean.</p>
</blockquote>
<p>Obviously this isn't how we build for the future! You can in fact calculate quite large factorials in lean. <code>#eval nat.fact 100</code> takes 26ms</p>

#### [ Mario Carneiro (Sep 11 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694178):
<p>Note that this would be much <em>slower</em> if I used <code>num</code> instead of <code>nat</code></p>

#### [ Kevin Buzzard (Sep 11 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694188):
<p>:-)</p>

#### [ Kevin Buzzard (Sep 11 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694197):
<p>I have no idea what <code>#eval</code> does -- but not that I have no idea what a VM is so I wouldn't launch into an explanation -- I am way behind.</p>

#### [ Kevin Buzzard (Sep 11 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694206):
<p>I know epsilon about java bytecode and the JVM</p>

#### [ Mario Carneiro (Sep 11 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694283):
<div class="codehilite"><pre><span></span>def num.fact : nat → num
| 0     := 1
| (n+1) := num.fact n * num.of_nat&#39; (n+1)

#eval num.fact 100
</pre></div>


<p>takes 61ms</p>

#### [ Mario Carneiro (Sep 11 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694350):
<p>Part of the problem is that you only see half the picture, since you are a mathematician with no interest in lean as a programming language. While that's fine, some design decisions will look strange or unmotivated from that angle</p>

#### [ Mario Carneiro (Sep 11 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694367):
<p>A major part of it is that <code>#eval</code> should be fast on computable things in mathlib</p>

#### [ Kevin Buzzard (Sep 11 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694387):
<p>I thought that #eval was completely irrelevant.</p>

#### [ Kevin Buzzard (Sep 11 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694388):
<p>Do I ever use it?</p>

#### [ Mario Carneiro (Sep 11 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694390):
<p><em>you</em> don't</p>

#### [ Kevin Buzzard (Sep 11 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694391):
<p>I see</p>

#### [ Kevin Buzzard (Sep 11 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694396):
<p>I mean, does the code I write ever use it somehow?</p>

#### [ Mario Carneiro (Sep 11 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694403):
<p>this may change in lean 4 when <code>vm_compute</code> arrives</p>

#### [ Kenny Lau (Sep 11 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694465):
<p>you mean dec_trivial?</p>

#### [ Mario Carneiro (Sep 11 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694467):
<p>Your biggest current contact with <code>#eval</code> is in tactic evaluation. When a tactic takes a long time it is running on the VM</p>

#### [ Mario Carneiro (Sep 11 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694474):
<p>it's dec_trivial in the VM</p>

#### [ Mario Carneiro (Sep 11 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694482):
<p>meaning that we could prove <code>nat.fact 100 = ...</code> in 21ms instead of whatever it is now</p>

#### [ Kevin Buzzard (Sep 11 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694529):
<p>I see, so when I see orange bars because I used <code>ring</code> 10 times already in my proof and I've still not finished writing it, that's because of something to do with <code>num</code> or <code>#eval</code> or something?</p>

#### [ Mario Carneiro (Sep 11 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694531):
<p>if I use <code>norm_num</code> on that I'm sure it will take several seconds at least and probably time out</p>

#### [ Mario Carneiro (Sep 11 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694535):
<p><code>#eval</code> is used to evaluate <code>ring</code> the tactic</p>

#### [ Mario Carneiro (Sep 11 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694600):
<p>in particular, <code>ring</code> does computations on rational numbers, and those computations are evaluating <code>rat</code> in the VM</p>

#### [ Mario Carneiro (Sep 11 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694608):
<p>this is distinct from proving things about <code>rat</code>, where the only thing running is typechecking the proofs</p>

#### [ Mario Carneiro (Sep 11 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694616):
<p>and also distinct from evaluating expressions using <code>dec_trivial</code>, which evaluates in the kernel</p>

#### [ Mario Carneiro (Sep 11 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694774):
<div class="codehilite"><pre><span></span>example : 8 * 10 = 10 * 8 := dec_trivial -- evaluates in the kernel

#reduce to_bool (8 * 10 = 10 * 8) -- evaluates in the kernel

#eval to_bool (8 * 10 = 10 * 8) -- evaluates in the VM

meta def test := if 8 * 10 = 10 * 8 then `[trivial] else sorry
example : true := by test -- evaluates in the VM

example : 8 * 10 = 10 * 8 := mul_comm 8 10 -- no evaluation, only typechecking
</pre></div>

#### [ Mario Carneiro (Sep 11 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133694921):
<p>and <span class="emoji emoji-1f340" title="four leaf clover">:four_leaf_clover:</span></p>
<div class="codehilite"><pre><span></span>example : 8 * 10 = 10 * 8 := vm_trivial -- evaluates in the VM
</pre></div>

#### [ Kevin Buzzard (Sep 11 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133695050):
<p>I only really care about proving theorems, but I still want to occasionally check <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>x</mi><mo>+</mo><mi>y</mi><msup><mo>)</mo><mn>3</mn></msup><mo>=</mo><msup><mi>x</mi><mn>3</mn></msup><mo>+</mo><mn>3</mn><msup><mi>x</mi><mn>2</mn></msup><mi>y</mi><mo>+</mo><mn>3</mn><mi>x</mi><msup><mi>y</mi><mn>2</mn></msup><mo>+</mo><msup><mi>y</mi><mn>3</mn></msup></mrow><annotation encoding="application/x-tex">(x+y)^3=x^3+3x^2y+3xy^2+y^3</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:1.064108em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord mathit">x</span><span class="mbin">+</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mclose"><span class="mclose">)</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">3</span></span></span></span></span></span></span></span><span class="mrel">=</span><span class="mord"><span class="mord mathit">x</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">3</span></span></span></span></span></span></span></span><span class="mbin">+</span><span class="mord mathrm">3</span><span class="mord"><span class="mord mathit">x</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mbin">+</span><span class="mord mathrm">3</span><span class="mord mathit">x</span><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span><span class="mbin">+</span><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">3</span></span></span></span></span></span></span></span></span></span></span> using <code>ring</code>. Is there a similar story here?</p>

#### [ Kevin Buzzard (Sep 11 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133695084):
<p>It seems to me that I am using <code>#eval</code> here.</p>

#### [ Kevin Buzzard (Sep 11 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133695091):
<p>without noticing.</p>

#### [ Kevin Buzzard (Sep 11 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133695109):
<p>which is irritating.</p>

#### [ Kevin Buzzard (Sep 11 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133695203):
<p>Actually what is irritating is that when my proofs get long, I get orange bars that don't go away for a few seconds. I had always assumed that this was because type class inference wasn't as quick as I wanted it to be, and kept forgetting all its calculations and then re-did them every time I pressed a key.</p>

#### [ Kevin Buzzard (Sep 11 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133695231):
<p>What is irritating for Chris is that mathlib gets one extra lemma and then when Chris needs it he has to pull mathlib and then wait for an hour for it to compile on his slow laptop.</p>

#### [ Reid Barton (Sep 11 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133695577):
<p>I expect most of that hour is spent in the elaborator/kernel doing typechecky things, not multiplying natural numbers.</p>

#### [ Reid Barton (Sep 11 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133695725):
<p>That is, I doubt choices about data representation affect mathlib build time much.</p>

#### [ Simon Hudon (Sep 11 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133695746):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> I'm not so sure. Maybe it's not multiplying that many numbers but I suspect that a large portion of proof checking is proof search which is done by functional programs (the tactics) using data structures like lists and natural numbers.</p>

#### [ Kenny Lau (Sep 11 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133696034):
<p>I guess it's ironic that in the Lean "theorem prover", the proofs are given the least relevance. They don't even exist in the VM</p>

#### [ Simon Hudon (Sep 11 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133696379):
<p>They exist in the kernel. They have a central role in the kernel. I think we can't say that they have the least relevance. I would say they have the most relevance though</p>

#### [ Scott Morrison (Sep 11 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133711908):
<p>We really need distributable binary <code>olean</code> files. :-(</p>

#### [ Kevin Buzzard (Sep 11 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/133713478):
<p>Can we get Travis to make them for Ubuntu?</p>

#### [ Minchao Wu (Oct 23 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/136340858):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Is there any current workaround for emulating <code>vm_compute</code>?</p>

#### [ Mario Carneiro (Oct 23 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/136343558):
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">tactic</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">mk_axiom</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">name</span><span class="o">)</span> <span class="o">(</span><span class="n">ty</span> <span class="o">:</span> <span class="n">expr</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">expr</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">env</span> <span class="err">←</span> <span class="n">get_env</span><span class="o">,</span>
  <span class="k">let</span> <span class="n">us</span> <span class="o">:=</span> <span class="n">expr</span><span class="bp">.</span><span class="n">collect_univ_params</span> <span class="n">ty</span><span class="o">,</span>
  <span class="n">add_decl</span> <span class="o">(</span><span class="n">declaration</span><span class="bp">.</span><span class="n">ax</span> <span class="n">n</span> <span class="n">us</span> <span class="n">ty</span><span class="o">),</span>
  <span class="n">return</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">const</span> <span class="n">n</span> <span class="o">(</span><span class="n">level</span><span class="bp">.</span><span class="n">param</span> <span class="bp">&lt;</span><span class="err">$</span><span class="bp">&gt;</span> <span class="n">us</span><span class="o">))</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">vm_trivial</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">t</span> <span class="err">←</span> <span class="n">target</span><span class="o">,</span>
  <span class="n">d</span> <span class="err">←</span> <span class="n">mk_instance</span> <span class="bp">`</span><span class="o">(</span><span class="n">decidable</span> <span class="err">%%</span><span class="n">t</span><span class="o">),</span>
  <span class="n">eval_expr</span> <span class="n">bool</span> <span class="bp">`</span><span class="o">(</span><span class="bp">@</span><span class="n">to_bool</span> <span class="err">%%</span><span class="n">t</span> <span class="err">%%</span><span class="n">d</span><span class="o">)</span> <span class="bp">&gt;&gt;=</span> <span class="n">guardb</span><span class="o">,</span>
  <span class="n">n</span> <span class="err">←</span> <span class="n">new_aux_decl_name</span><span class="o">,</span>
  <span class="n">mk_axiom</span> <span class="n">n</span> <span class="n">t</span> <span class="bp">&gt;&gt;=</span> <span class="n">exact</span>

<span class="kn">end</span> <span class="n">tactic</span>

<span class="kn">example</span> <span class="o">:</span> <span class="mi">200</span> <span class="bp">+</span> <span class="mi">200</span> <span class="bp">=</span> <span class="mi">400</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">vm_trivial</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">prime</span> <span class="mi">134513481061</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">vm_trivial</span>
</pre></div>

#### [ Minchao Wu (Oct 23 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/136345082):
<p>Great. The only concern is that it's actually introducing the thing being proved as an axiom?</p>

#### [ Minchao Wu (Oct 23 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/136345490):
<p>Hmm... but this should be sufficient for my purpose. Thanks Mario!</p>

#### [ Rob Lewis (Oct 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/136346985):
<p>Note that this will only work for <code>example</code> and <code>def</code>. Any changes you make to the environment when proving a <code>theorem</code> get discarded at the end. New declarations will get inlined if possible, but this isn't possible with axioms.</p>

#### [ Rob Lewis (Oct 23 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/136347048):
<p>The reason being, elaboration of theorems happens in parallel/out of order, and changing the environment needs to be sequential.</p>

#### [ Reid Barton (Oct 23 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/136347178):
<p>Is this basically: To prove a decidable statement, have the VM evaluate the decision procedure and then add an axiom which says that we trust that the result of VM execution was correct in this case?</p>

#### [ Rob Lewis (Oct 23 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implementation%20issues/near/136347448):
<p>Yeah. It's using the VM as an oracle for decidable statements.</p>


{% endraw %}
