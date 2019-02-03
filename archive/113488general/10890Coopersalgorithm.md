---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/10890Coopersalgorithm.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Cooper's algorithm](https://leanprover-community.github.io/archive/113488general/10890Coopersalgorithm.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Seul Baek (May 20 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126812643):
<p>I've implemented Cooper's algorithm for linear integer arithmetic as a Lean tactic (<a href="https://github.com/skbaek/qelim" target="_blank" title="https://github.com/skbaek/qelim">https://github.com/skbaek/qelim</a>). It's still quite limited, but it should work for simple goals.</p>
<ul>
<li><code>cooper</code> is the completely verified tactic that is proof-producing all the way. Unfortunately, it is unusably slow.</li>
<li><code>cooper_vm</code> is the partially verified tactic whose first step (replacing the original goal with the new quantifier-eliminated goal) is proof-producing. The second step (evaluating the new goal to a tautology) is trusted.</li>
<li>The tactics assume sentential goals, so you'll have to generalize variables and hypotheses before calling it.</li>
<li>The implementation is based on Tobias Nipkow's paper (<a href="http://www21.in.tum.de/~nipkow/pubs/jar10.pdf" target="_blank" title="http://www21.in.tum.de/~nipkow/pubs/jar10.pdf">http://www21.in.tum.de/~nipkow/pubs/jar10.pdf</a>).</li>
<li>I've added a few test cases (qelim/lia/cooper/tests.lean) from John Harrison's book.</li>
<li>Right now I'm having trouble making absolute paths work. All references to mathlib are relative.</li>
</ul>

#### [ Mario Carneiro (May 20 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126812751):
<p>Hey! Seul's here! And he brings gifts</p>

#### [ Mario Carneiro (May 20 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126813048):
<p>I notice that your <code>atom</code> type uses <code>int</code>. This will kill your efficiency, if you are doing kernel evaluation. You should use <code>znum</code> instead</p>

#### [ Mario Carneiro (May 20 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126813108):
<p>Re: paths, do you have a <code>leanpkg.toml</code> file in your project? I don't see one, but it's important for making file resolution work</p>

#### [ Mario Carneiro (May 20 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126813252):
<p>For others who may not be aware: this is basically the <code>omega</code> tactic everyone's been talking about, although Cooper's is a slightly different algorithm for the same problem</p>

#### [ Andrew Ashworth (May 20 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126817604):
<p>Thanks for releasing this! It looks like it was quite a substantial effort, with the first commit being a few months ago. I definitely want to spend some time looking over it!</p>

#### [ Seul Baek (May 20 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126844501):
<blockquote>
<p>I notice that your <code>atom</code> type uses <code>int</code>. This will kill your efficiency, if you are doing kernel evaluation. You should use <code>znum</code> instead</p>
</blockquote>
<p>Thanks for the suggestion! Maybe this is what's making <code>cooper</code> so much slower than <code>cooper_vm</code>.</p>

#### [ Seul Baek (May 20 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126844596):
<blockquote>
<p>Re: paths, do you have a <code>leanpkg.toml</code> file in your project? I don't see one, but it's important for making file resolution work</p>
</blockquote>
<p>I'm actually having problems with mathlib itself—when I clone mathlib it won't work as is, because Lean doesn't like its absolute paths for some reason. It works after I manually relativize them.  This is strange because mathlib does have a <code>leanpkg.toml</code> file.</p>

#### [ Kevin Buzzard (May 20 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126844646):
<p>You want to make mathlib a dependency for your project</p>

#### [ Kevin Buzzard (May 20 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126844687):
<p>if you use leanpkg and add mathlib as a dependency then it should sort out everything for you</p>

#### [ Kevin Buzzard (May 20 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126844697):
<p>see section 1.4.3 of the reference manual</p>

#### [ Kevin Buzzard (May 20 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126844698):
<p><a href="https://leanprover.github.io/reference/using_lean.html#using-the-package-manager" target="_blank" title="https://leanprover.github.io/reference/using_lean.html#using-the-package-manager">https://leanprover.github.io/reference/using_lean.html#using-the-package-manager</a></p>

#### [ Kevin Buzzard (May 20 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126844748):
<p>I am really grateful for your work by the way, and maybe <span class="user-mention" data-user-id="110031">@Patrick Massot</span> will be even more grateful -- Patrick maybe this solves some of your nat woes?</p>

#### [ Patrick Massot (May 21 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126864044):
<p>I hope it can help me. I need to find some time to try it.</p>

#### [ Patrick Massot (May 21 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126864048):
<p>Maybe I'm not trying very hard to find this time because I'm afraid I'll be disappointed</p>

#### [ Patrick Massot (May 21 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126865859):
<p>Any hint about how to actually import that cooper thing?</p>

#### [ Patrick Massot (May 21 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126865899):
<p>I tried <code>leanpkg add skbaek/qelim</code> and then import</p>

#### [ Patrick Massot (May 21 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126865902):
<p>I tried adding a <code>leanpkg.toml</code> to it</p>

#### [ Patrick Massot (May 21 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126865905):
<p>But <code>import lia.cooper.main</code> doesn't work</p>

#### [ Patrick Massot (May 21 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126866474):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Did you manage to import this tactic?</p>

#### [ Mario Carneiro (May 21 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126866481):
<p>I haven't attempted it, no</p>

#### [ Mario Carneiro (May 21 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126866527):
<p>You could just copy the files into your project</p>

#### [ Patrick Massot (May 21 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126866593):
<p>Then all mathlib imports fail...</p>

#### [ Patrick Massot (May 21 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/126866594):
<p>I guess we need to wait a bit more until this can be tested</p>

#### [ Seul Baek (May 28 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127217640):
<p>I figured out what was wrong and added a .toml file. Now you can install and use the repo using leanpkg.</p>

#### [ Johan Commelin (May 28 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127218789):
<p>This is cool!</p>

#### [ Johan Commelin (May 28 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127218832):
<p>Is it planned to merge this into mathlib? Or will it remain a separate lib?</p>

#### [ Johan Commelin (May 28 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127218837):
<p>I'm not sure what the planning is in general: a monolithic lib, or distributed libs</p>

#### [ Patrick Massot (May 28 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127219807):
<p><span class="user-mention" data-user-id="116585">@Seul Baek</span>  Do you have any example of use? I can now import the lib, but haven't yet managed to proved anything using Cooper</p>

#### [ Patrick Massot (May 28 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220285):
<p>actually I can prove stuff about integers (that <code>ring</code> also proves),  so maybe I misunderstood the scope of this tactic. I thought it would work on natural numbers</p>

#### [ Patrick Massot (May 28 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220332):
<p>With nat I always get <code>type error at eval_expr, argument has type  ℕ but is expected to have type  ℤ</code></p>

#### [ Mario Carneiro (May 28 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220429):
<p>The core tactic is designed to work on <code>int</code>. There are some missing preprocessing steps to prove natural number theorems</p>

#### [ Mario Carneiro (May 28 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220432):
<p>Of course a nat quantifier is the same as an int quantifier with the additional assumption 0 &lt;= n</p>

#### [ Patrick Massot (May 28 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220439):
<p>What do you get in addition to <code>ring</code> then?</p>

#### [ Mario Carneiro (May 28 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220443):
<p>I think Seul's tactic is still more of a backend thing</p>

#### [ Mario Carneiro (May 28 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220482):
<p>it needs a front end to generalize and revert quantifiers, and convert nats to ints</p>

#### [ Patrick Massot (May 28 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220487):
<p>Do you know whether he's working on this?</p>

#### [ Mario Carneiro (May 28 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220488):
<p><code>ring</code> will not be able to prove that <code>\forall n : int, n &lt;= 0 \/ n &gt;= 1</code> for example</p>

#### [ Mario Carneiro (May 28 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220495):
<p>Or <code>3 | n -&gt; 5 | n -&gt; 15 | n</code></p>

#### [ Mario Carneiro (May 28 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220537):
<p>or <code>3 | n -&gt; n &gt; 0 -&gt; n*n - n &gt; 0</code></p>

#### [ Mario Carneiro (May 28 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220544):
<p>oh wait actually that last one might not work because of the square</p>

#### [ Patrick Massot (May 28 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220546):
<p>This sounds pretty nice</p>

#### [ Mario Carneiro (May 28 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220587):
<p>but more importantly, it allows full quantifier alternation</p>

#### [ Patrick Massot (May 28 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220588):
<p>But Lean doesn't let me state the divisibility stuff</p>

#### [ Mario Carneiro (May 28 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220590):
<p>type <code>3 \| n</code></p>

#### [ Patrick Massot (May 28 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220601):
<p>Oh, Johan will like this unicode trickery</p>

#### [ Patrick Massot (May 28 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127220609):
<div class="codehilite"><pre><span></span><span class="kn">example</span>  <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">),</span> <span class="o">(</span><span class="mi">3</span> <span class="err">∣</span> <span class="n">n</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="mi">5</span> <span class="err">∣</span> <span class="n">n</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="mi">15</span> <span class="err">∣</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">cooper</span>
</pre></div>


<p>doesn't work though</p>

#### [ Mario Carneiro (May 28 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221407):
<p>looking at the code, it's pretty sparse on extended syntax</p>

#### [ Mario Carneiro (May 28 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221412):
<p>you have to use exists <del>and forall</del> and times and le</p>

#### [ Mario Carneiro (May 28 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221417):
<p>I'm not even sure equality is supported</p>

#### [ Mario Carneiro (May 28 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221426):
<p>so you would have to write <code>\ex k, 3 * k &lt;= n /\ n &lt;= 3 * k</code> instead of <code>3 | n</code></p>

#### [ Kenny Lau (May 28 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221537):
<p>I thought everything is decidable</p>

#### [ Seul Baek (May 28 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221538):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> I'm not sure what'd be the best way to integrate this to other libraries in the long term.  It'll stay separate for the short term for convenience of further development.</p>

#### [ Mario Carneiro (May 28 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221553):
<p>actually I take it back, forall is also not supported</p>

#### [ Mario Carneiro (May 28 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221555):
<p>you have to use negation and exists</p>

#### [ Seul Baek (May 28 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221653):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span>  It should definitely be possible to write a preprocessor for nat, although I'm not working on it at the moment. I'm trying to first replace <code>int</code> with <code>znum</code> to improve efficiency.</p>

#### [ Seul Baek (May 28 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221777):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> forall and equality are indirectly supported by the rewriting step before calling the main quantifier elimination tactic. E.g., <code>cooper_vm</code> works for <code>forall (x: int), exists (y : int), x = 1 + y</code></p>

#### [ Mario Carneiro (May 28 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221833):
<p>oh, I see it</p>

#### [ Mario Carneiro (May 28 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221835):
<p>I guess you should add the definition of dvd in that list</p>

#### [ Seul Baek (May 28 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221944):
<p>You mean the list of indirectly supported relations?</p>

#### [ Mario Carneiro (May 28 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221945):
<p>yes</p>

#### [ Mario Carneiro (May 28 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221947):
<p>as a simp lemma in the preprocessing</p>

#### [ Mario Carneiro (May 28 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221959):
<p>something like <code>a | b &lt;-&gt; ∃ c, b = a * c</code></p>

#### [ Mario Carneiro (May 28 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127221977):
<p>surprisingly not stated as a theorem that I can see, but easy to prove by refl</p>

#### [ Seul Baek (May 28 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127222107):
<p>Yes, I think it should be possible to do this even more directly (w/o preprocessing), since the internal syntax already includes dvd</p>

#### [ Patrick Massot (May 29 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127241177):
<p>Thanks Seul and Mario. I'll wait a bit more then (a tactic handling ℕ crazyness is what I really need).</p>

#### [ Kevin Buzzard (May 29 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246452):
<blockquote>
<p>surprisingly not stated as a theorem that I can see, but easy to prove by refl</p>
</blockquote>
<p>Hey wait a minute! I asked for the name of a theorem recently (if a structure is made with a : A and b : B then  (<a href="http://structure.mk" target="_blank" title="http://structure.mk">structure.mk</a> a b).a = a) and you said "oh that's true by refl so it doesn't have a name"</p>

#### [ Kevin Buzzard (May 29 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246465):
<p>What's the algorithm for determining whether an equality whose proofs is rfl gets blessed with a name?</p>

#### [ Mario Carneiro (May 29 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246748):
<p>It doesn't usually matter, Seul is writing a tactic so he needs to have names for his automation. It's fine even if he just declares a local theorem with a particular statement he can rely on.</p>

#### [ Mario Carneiro (May 29 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246755):
<p>For example there are lots of theorems in <code>tactic.ring</code> that are like this - they have very particular statements to make it easy for the automation, but no one would ever use those theorems otherwise</p>

#### [ Kevin Buzzard (May 29 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246826):
<p>But the other day I said "I want to do this rewrite and it's refl but I want to know the name anyway" and your response was "use show"</p>

#### [ Kevin Buzzard (May 29 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246833):
<p>and I bought this at the time</p>

#### [ Kevin Buzzard (May 29 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246834):
<p>but this response stinks</p>

#### [ Mario Carneiro (May 29 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246876):
<p>But it's also common for definitional expansions to have a name, particularly when the definition is hidden in a typeclass</p>

#### [ Kevin Buzzard (May 29 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246878):
<p>because I have to keep changing things to definitionally equal things in my head</p>

#### [ Kevin Buzzard (May 29 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246879):
<p>and I am sitting at a computer</p>

#### [ Mario Carneiro (May 29 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246885):
<p>for example <code>finset.subset_iff</code></p>

#### [ Kevin Buzzard (May 29 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246889):
<p>can I do targetted dsimp?</p>

#### [ Kevin Buzzard (May 29 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cooper%27s%20algorithm/near/127246896):
<p>This is a new thread. Hang on</p>


{% endraw %}
