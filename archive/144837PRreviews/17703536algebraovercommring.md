---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/17703536algebraovercommring.html
---

## Stream: [PR reviews](https://leanprover-community.github.io/archive/144837PRreviews/index.html)
### Topic: [#536 algebra over comm_ring](https://leanprover-community.github.io/archive/144837PRreviews/17703536algebraovercommring.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Jan 10 2019 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154831785):
<p>Changed the target to <code>ring</code> not <code>comm_ring</code>.</p>

#### [ Johan Commelin (Jan 11 2019 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154901762):
<p>So... <code>algebra</code> should probably be a class.</p>

#### [ Kenny Lau (Jan 11 2019 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154901803):
<p>als ik het verandere naar en class, wat zou de name zijn?</p>

#### [ Johan Commelin (Jan 11 2019 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154901811):
<p>Why not keep calling it <code>algebra</code>?</p>

#### [ Kenny Lau (Jan 11 2019 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154901813):
<p>het naam von de morphisme dat het algebra defineeret</p>

#### [ Kenny Lau (Jan 11 2019 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154901826):
<p>waarhijdlijk?</p>

#### [ Kenny Lau (Jan 11 2019 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154901885):
<p>dus als we hebben dat C is een R-algebra, het pi in C wordt “algebra C pi” heetet?</p>

#### [ Johan Commelin (Jan 11 2019 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154901890):
<p>I don't get it. What is the trouble with changing <code>structure algebra</code> on line 28 to <code>class algebra</code>?</p>

#### [ Kenny Lau (Jan 11 2019 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154901913):
<p>dat man kun niet meer “i x” zeggen</p>

#### [ Kenny Lau (Jan 11 2019 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154901919):
<p>voor “i : algebra R A” en “x : R”</p>

#### [ Johan Commelin (Jan 11 2019 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154901969):
<p>Why not? Aaah, because coercions and type class inference don't play well together?</p>

#### [ Kenny Lau (Jan 11 2019 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154901976):
<p>dat als algebra een class is, we zouden niet hebben een naam voor de instance</p>

#### [ Johan Commelin (Jan 11 2019 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902089):
<p>Ok, so this is a question about the levels of bundling we want... is that right?</p>

#### [ Kenny Lau (Jan 11 2019 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902154):
<p>nee, dit is over het naam van de morphism defineerend</p>

#### [ Johan Commelin (Jan 11 2019 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902156):
<p>Wait, no. I really don't get it. We can just use classes as if they are structures, right?</p>

#### [ Kenny Lau (Jan 11 2019 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902167):
<p>nee nog</p>

#### [ Kenny Lau (Jan 11 2019 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902181):
<p>je kunt niet zeggen “i : algebra R A” als algebra class is</p>

#### [ Kenny Lau (Jan 11 2019 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902188):
<p>(je kunt, maar het moet ons niet)</p>

#### [ Johan Commelin (Jan 11 2019 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902322):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> What do you think?</p>

#### [ Johan Commelin (Jan 11 2019 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902418):
<p>Somehow I would expect to use this as <code>{R S : Type} [comm_ring R] [algebra R S]</code>. But apparently that is rather hard. Because now we cannot map an <code>r : R</code> into <code>S</code> without awful contortions.</p>

#### [ Johan Commelin (Jan 11 2019 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902505):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> If we had <code>S : Algebra R</code>, then you could write <code>S.hom r</code> to map <code>r : R</code> to <code>S</code>.</p>

#### [ Kenny Lau (Jan 11 2019 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902561):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> waar ben je?</p>

#### [ Johan Commelin (Jan 11 2019 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902576):
<p>Somewhere in a train in Germany...</p>

#### [ Johan Commelin (Jan 11 2019 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902585):
<p>I had to travel back today, sorry.</p>

#### [ Kenny Lau (Jan 11 2019 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902586):
<p>dus je wil niet class hebben?</p>

#### [ Johan Commelin (Jan 11 2019 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902605):
<p>I no longer know what is good and what I want and what to do <span class="emoji emoji-1f615" title="confused">:confused:</span></p>

#### [ Kenny Lau (Jan 11 2019 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902613):
<p>lekker!</p>

#### [ Johan Commelin (Jan 11 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902678):
<p>What was your reason for <code>algebra R S</code> instead of <code>S : Algebra R</code>?</p>

#### [ Kenny Lau (Jan 11 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902684):
<p>dat we kunnen zeggen dat S een korp is</p>

#### [ Johan Commelin (Jan 11 2019 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902721):
<p>Aah, of course, and you want to move between <code>R1</code>-algebra and <code>R2</code>-algebra structures if there is an <code>f : R1 -&gt; R2</code> and <code>S</code> is an <code>R2</code>-algebra.</p>

#### [ Johan Commelin (Jan 11 2019 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902728):
<p>korp -&gt; lichaam</p>

#### [ Johan Commelin (Jan 11 2019 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902809):
<p><span class="user-mention" data-user-id="110172">@Assia Mahboubi</span> <span class="user-mention" data-user-id="110193">@Cyril Cohen</span> What is the approach that canonical structures take in situations like these? I guess you have the bundled <code>Algebra R</code> version, and you will have to write explicitly the functors for moving between <code>Algebra R1</code> and <code>Algebra R2</code>. Is that right?</p>

#### [ Johan Commelin (Jan 11 2019 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/154902859):
<p><span class="user-mention" data-user-id="110172">@Assia Mahboubi</span> <span class="user-mention" data-user-id="110193">@Cyril Cohen</span> (I subscribed you to this stream. No sure if you want that... It's all about discussing PRs to mathlib.)</p>

#### [ Kenny Lau (Jan 23 2019 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156674418):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> It looks like the instance <code>S : set R, h : is_subring S |- algebra S R</code> would never work if the first parameter of <code>algebra</code> is an out_param</p>

#### [ Kenny Lau (Jan 23 2019 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156674481):
<p>should we reconsider making it a class instead of making it a structure?</p>

#### [ Johannes Hölzl (Jan 23 2019 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156677314):
<p>I think for algebra we cannot have it an <code>out_param</code> anymore. We already see that it is a problem for <code>module</code>, but for <code>algebra</code> it completely breaks down</p>

#### [ Kenny Lau (Jan 23 2019 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156677450):
<p>ok</p>

#### [ Kenny Lau (Jan 23 2019 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156677473):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> then why is module still using out_param?</p>

#### [ Kevin Buzzard (Jan 23 2019 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156677476):
<p>What does this mean in practice for people like me who don't really know what an <code>out_param</code> is?</p>

#### [ Johannes Hölzl (Jan 23 2019 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156679581):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> its some work to change it right now, and it requires the user to annotate more types at inconvenient places</p>

#### [ Kenny Lau (Jan 23 2019 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156679641):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> well I tried to change it before, and then I got some error, and I posted it in the general chat, and nobody helped fix the error</p>

#### [ Kenny Lau (Jan 23 2019 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156679664):
<p><a href="#narrow/stream/113488-general/topic/Module.20refactor" title="#narrow/stream/113488-general/topic/Module.20refactor">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Module.20refactor</a></p>

#### [ Johannes Hölzl (Jan 23 2019 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156679759):
<p>Yes, we should revive this branch.</p>

#### [ Kenny Lau (Jan 23 2019 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156728185):
<p>do we have any more comments for this PR? It's been here for more than a month</p>

#### [ Kenny Lau (Jan 24 2019 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156759442):
<div class="codehilite"><pre><span></span><span class="n">subalgebra</span><span class="bp">.</span><span class="n">comm_ring</span> <span class="o">:</span>
  <span class="bp">Π</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">)</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_2</span><span class="o">)</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_4</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_5</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="n">A</span><span class="o">]</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_6</span> <span class="o">:</span> <span class="n">algebra</span> <span class="n">R</span> <span class="n">A</span><span class="o">]</span>
  <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">subalgebra</span> <span class="n">R</span> <span class="n">A</span><span class="o">),</span> <span class="n">comm_ring</span> <span class="err">↥</span><span class="n">S</span>
</pre></div>


<p>why should this cause an instance loop?</p>

#### [ Kenny Lau (Jan 24 2019 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156759448):
<div class="codehilite"><pre><span></span>[class_instances] (9) ?x_68 : comm_ring ?x_66 := @subalgebra.comm_ring ?x_72 ?x_73 ?x_74 ?x_75 ?x_76 ?x_77
[class_instances] (10) ?x_74 : comm_ring ?x_72 := @subalgebra.comm_ring ?x_78 ?x_79 ?x_80 ?x_81 ?x_82 ?x_83
[class_instances] (11) ?x_80 : comm_ring ?x_78 := @subalgebra.comm_ring ?x_84 ?x_85 ?x_86 ?x_87 ?x_88 ?x_89
[class_instances] (12) ?x_86 : comm_ring ?x_84 := @subalgebra.comm_ring ?x_90 ?x_91 ?x_92 ?x_93 ?x_94 ?x_95
[class_instances] (13) ?x_92 : comm_ring ?x_90 := @subalgebra.comm_ring ?x_96 ?x_97 ?x_98 ?x_99 ?x_100 ?x_101
[class_instances] (14) ?x_98 : comm_ring ?x_96 := @subalgebra.comm_ring ?x_102 ?x_103 ?x_104 ?x_105 ?x_106 ?x_107
...
</pre></div>

#### [ Kenny Lau (Jan 24 2019 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156759463):
<p>can't Lean see that there is no <code>↥</code>?</p>

#### [ Mario Carneiro (Jan 24 2019 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156759558):
<p>You are searching for <code>comm_ring ?</code></p>

#### [ Mario Carneiro (Jan 24 2019 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156759570):
<p>that's already a bad sign - what started this search?</p>

#### [ Kenny Lau (Jan 24 2019 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156759638):
<div class="codehilite"><pre><span></span>[class_instances] (0) ?x_2 : @vector_space ?x_0 L ?x_1
  (@ring.to_add_comm_group L
     (@domain.to_ring L (@division_ring.to_domain L (@field.to_division_ring L (@discrete_field.to_field L _inst_2))))) := @lc.vector_space ?x_3 ?x_4 ?x_5 ?x_6 ?x_7
failed is_def_eq
[class_instances] (0) ?x_2 : @vector_space ?x_0 L ?x_1
  (@ring.to_add_comm_group L
     (@domain.to_ring L (@division_ring.to_domain L (@field.to_division_ring L (@discrete_field.to_field L _inst_2))))) := @algebra.vector_space ?x_8 ?x_9 ?x_10 ?x_11 ?x_12 ?x_13 ?x_14
...
[class_instances] (1) ?x_9 : comm_ring ?x_8 := @subalgebra.comm_ring ?x_24 ?x_25 ?x_26 ?x_27 ?x_28 ?x_29
[class_instances] (2) ?x_26 : comm_ring ?x_24 := @subalgebra.comm_ring ?x_30 ?x_31 ?x_32 ?x_33 ?x_34 ?x_35
[class_instances] (3) ?x_32 : comm_ring ?x_30 := @subalgebra.comm_ring ?x_36 ?x_37 ?x_38 ?x_39 ?x_40 ?x_41
[class_instances] (4) ?x_38 : comm_ring ?x_36 := @subalgebra.comm_ring ?x_42 ?x_43 ?x_44 ?x_45 ?x_46 ?x_47
...
</pre></div>

#### [ Kenny Lau (Jan 24 2019 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156759658):
<p>oh no I see the problem</p>

#### [ Kenny Lau (Jan 24 2019 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156759734):
<p>my private project is actually a very good testcase, I'll test it before hassling you to accept the PR :P</p>

#### [ Kevin Buzzard (Jan 24 2019 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156760833):
<blockquote>
<p>that's already a bad sign - what started this search?</p>
</blockquote>
<p>This is something I've never understood. Why is searching for <code>comm_ring</code> a bad sign? Some things are commutative rings...</p>

#### [ Reid Barton (Jan 24 2019 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156766944):
<p>The problem is that we're searching for <code>comm_ring ?x_8</code>, that is, a commutative ring instance for a type we haven't determined yet</p>

#### [ Kevin Buzzard (Jan 24 2019 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156771325):
<p>I can see that this will be problematic, but maybe later on in our search we'll figure out what that type is and then we'll be fine.</p>

#### [ Chris Hughes (Jan 24 2019 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156772450):
<p>Is searching for an instance on a metavariable not always completely futile?</p>

#### [ Kevin Buzzard (Jan 24 2019 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156773087):
<p>I don't know because I don't understand the search algorithm. It wouldn't be futile if the algorithm said "ok I can't find this immediately so let's put it on hold and search for other stuff and then come back to it"</p>

#### [ Kenny Lau (Jan 24 2019 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23536%20algebra%20over%20comm_ring/near/156788344):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> ok I've tested my file, please merge it :P</p>


{% endraw %}
