---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/58886partialorderformatrix.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [partial order for matrix](https://leanprover-community.github.io/archive/113489newmembers/58886partialorderformatrix.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Tobias Grosser (Sep 18 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134185883):
<p>Dear all, as you know I just get up-to-speed on lean (and theorem proving) and don't do it fulltime for now. However, I picked as first toy-project to get started the extension of matrix as an instance of partial_order. (See <a href="https://github.com/tobig/lean-polyhedra/blob/master/src/polyhedra.lean" target="_blank" title="https://github.com/tobig/lean-polyhedra/blob/master/src/polyhedra.lean">https://github.com/tobig/lean-polyhedra/blob/master/src/polyhedra.lean</a>)</p>

#### [ Andrew Ashworth (Sep 18 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134185923):
<p>Hi Tobias, you may want to post this in the #maths channel so people who are interested in this sort of stuff see it!</p>

#### [ Andrew Ashworth (Sep 18 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186016):
<p>or you may post in #general if this is a concrete matrix implementation meant for use in computation</p>

#### [ Tobias Grosser (Sep 18 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186420):
<p>Honestly, I don't even know how to post to the #maths channel. I see a "general" and a "new members" stream, but no "#maths" channel. I know streams and topics from <a href="https://zulipchat.com/help/about-streams-and-topics" target="_blank" title="https://zulipchat.com/help/about-streams-and-topics">https://zulipchat.com/help/about-streams-and-topics</a>, but have no ideas of channels. I can obviously move this topic to the general stream if this helps. Would also post it to a math channel, if you can explain what a math channel is? Are you refering to "stream:general topic:#maths"?</p>

#### [ Tobias Grosser (Sep 18 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186434):
<p>I posted it in new members, as my questions are for now still very simple.</p>

#### [ Reid Barton (Sep 18 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186514):
<p>"Channel" means stream in this context I think.</p>

#### [ Andrew Ashworth (Sep 18 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186540):
<p>whew, yes, I forgot Zulip isn't IRC</p>

#### [ Reid Barton (Sep 18 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186549):
<p><a class="stream" data-stream-id="116395" href="/#narrow/stream/116395-maths">#maths</a></p>

#### [ Tobias Grosser (Sep 18 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186552):
<p>OK, got it. Had to subscribe to #maths explicitly</p>

#### [ Tobias Grosser (Sep 18 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186634):
<p>My questions still remain simple. I mostly would like to know how to destruct an equality: <a href="https://github.com/tobig/lean-polyhedra/blob/master/src/polyhedra.lean#L51" target="_blank" title="https://github.com/tobig/lean-polyhedra/blob/master/src/polyhedra.lean#L51">https://github.com/tobig/lean-polyhedra/blob/master/src/polyhedra.lean#L51</a></p>

#### [ Tobias Grosser (Sep 18 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186752):
<p>I spend some time looking and will probably figure it out eventually, but maybe somebody has a pointer.</p>

#### [ Reid Barton (Sep 18 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186772):
<p>Don't you need to construct an equality?</p>

#### [ Reid Barton (Sep 18 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186781):
<p>I guess you mean: "destruct" the goal</p>

#### [ Tobias Grosser (Sep 18 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186787):
<p>Exactly.</p>

#### [ Tobias Grosser (Sep 18 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186843):
<p>I had the same problem with the &lt;=, but there I could just "assume i" and lean would auto-destruct it.</p>

#### [ Reid Barton (Sep 18 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186872):
<p>I'm assuming your matrices are functions (of two variables), so the low-level way is to apply <code>funext</code> (twice)</p>

#### [ Andrew Ashworth (Sep 18 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186888):
<p>you will probably want <code>ext_iff </code> in <code>ring_theory.matrix</code></p>

#### [ Andrew Ashworth (Sep 18 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186956):
<p>this will allow you to turn <code>M = N</code> into <code> (∀ i j, M i j = N i j)</code></p>

#### [ Tobias Grosser (Sep 18 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134187198):
<p>Right. ext_iff looks good. Now I need to figure out how to apply it.</p>

#### [ Tobias Grosser (Sep 18 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134187201):
<p>Reid's proposal also worked.</p>

#### [ Tobias Grosser (Sep 18 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134187220):
<p>But from there I would not know how to proceed.</p>

#### [ Johan Commelin (Sep 18 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134187234):
<p>Either <code>ext</code> or <code>rw ext_iff</code> probably works</p>

#### [ Andrew Ashworth (Sep 18 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134187236):
<p>indeed, <code>ext_iff</code> is defined using multiple <code>funext</code> applications</p>

#### [ Tobias Grosser (Sep 18 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134187309):
<p>Perfect. All works.</p>

#### [ Tobias Grosser (Sep 18 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134187314):
<p>So easy. I tried rw, but had missed a comma before. Thought I needed more magic.</p>

#### [ Tobias Grosser (Sep 18 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134187329):
<p>Thanks guys. This got me over a slow phase. Will finish my proofs and get back. Very nice community here.</p>

#### [ Tobias Grosser (Sep 18 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134187979):
<p>Just to report back, my proof went through and I know have the partial_order I wanted to define on matrix.</p>

#### [ Kevin Buzzard (Sep 18 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134187985):
<div class="codehilite"><pre><span></span><span class="kn">protected</span> <span class="n">def</span> <span class="n">matrix</span><span class="bp">.</span><span class="n">le_antisymm</span> <span class="o">[</span><span class="n">partial_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span><span class="o">:</span> <span class="n">matrix</span> <span class="n">n</span> <span class="n">m</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
<span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">assume</span> <span class="n">h1</span><span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span><span class="o">,</span>
  <span class="k">assume</span> <span class="n">h2</span><span class="o">:</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">funext</span><span class="o">,</span> <span class="n">intro</span> <span class="n">i</span><span class="o">,</span> <span class="n">apply</span> <span class="n">funext</span><span class="o">,</span> <span class="n">intro</span> <span class="n">j</span><span class="o">,</span>
<span class="c1">-- or   funext i,funext j,</span>
<span class="c1">-- or  ext i j,</span>
  <span class="n">exact</span> <span class="n">le_antisymm</span> <span class="o">(</span><span class="n">h1</span> <span class="n">i</span> <span class="n">j</span><span class="o">)</span> <span class="o">(</span><span class="n">h2</span> <span class="n">i</span> <span class="n">j</span><span class="o">),</span>
<span class="kn">end</span>
</pre></div>

#### [ Tobias Grosser (Sep 18 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134187996):
<p>Ah, even better.</p>

#### [ Tobias Grosser (Sep 18 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188004):
<p>Thanks <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Tobias Grosser (Sep 18 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188071):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>, I used this for a proof on polyhedra. Would it make sense to add such defintions to your recent mathlib changes?</p>

#### [ Mario Carneiro (Sep 18 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188081):
<p>golfed:</p>
<div class="codehilite"><pre><span></span>protected lemma matrix.le_antisymm [partial_order α] (a b: matrix n m α)
  (h1 : a ≤ b) (h2 : b ≤ a) : a = b :=
by ext i j; exact le_antisymm (h1 i j) (h2 i j)
</pre></div>

#### [ Mario Carneiro (Sep 18 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188096):
<p>(also I don't have your definitions, so I had to guess if that's right)</p>

#### [ Kevin Buzzard (Sep 18 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188203):
<p>It would not surprise me if the Pi_instance tactic did this automatically, but it might not do.</p>

#### [ Kenny Lau (Sep 18 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188206):
<p>golfeded:</p>
<div class="codehilite"><pre><span></span><span class="kn">protected</span> <span class="kn">lemma</span> <span class="n">matrix</span><span class="bp">.</span><span class="n">le_antisymm</span> <span class="o">[</span><span class="n">partial_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span><span class="o">:</span> <span class="n">matrix</span> <span class="n">n</span> <span class="n">m</span> <span class="n">α</span><span class="o">)</span>
  <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">h2</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">ext</span> <span class="n">i</span> <span class="n">j</span><span class="bp">;</span> <span class="k">from</span> <span class="n">le_antisymm</span> <span class="o">(</span><span class="n">h1</span> <span class="n">i</span> <span class="n">j</span><span class="o">)</span> <span class="o">(</span><span class="n">h2</span> <span class="n">i</span> <span class="n">j</span><span class="o">)</span>
</pre></div>

#### [ Tobias Grosser (Sep 18 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188431):
<p>Nice, this lean golf.</p>

#### [ Tobias Grosser (Sep 18 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188437):
<p>The two solutions from Mario and Kenny don't work in my editor.</p>

#### [ Tobias Grosser (Sep 18 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188444):
<p>Need to replace "by" with "begin .. end"</p>

#### [ Tobias Grosser (Sep 18 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188491):
<p>Not yet sure why, but this proofs starts to look really nice. And you are all fast in golfing. ;-)</p>

#### [ Tobias Grosser (Sep 18 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188689):
<p>Got it, need a semicolon for 'by'.</p>

#### [ Kevin Buzzard (Sep 18 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188751):
<p>yes, <code>by</code> takes only one tactic, so you can either do <code>{tactic 1, tactic 2}</code> or <code>tactic 1;tactic 2</code></p>

#### [ Kevin Buzzard (Sep 18 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188801):
<p>Did you notice that they both moved the hypotheses to the left of the colon? That's standard Lean style, so it seems; put as many hypotheses as possible on the left of the colon unless you can't do this for some reason (e.g. you're using the equation compiler).</p>

#### [ Kevin Buzzard (Sep 18 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188858):
<p>It makes your tactic proof two lines shorter at no extra cost</p>

#### [ Tobias Grosser (Sep 18 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188885):
<p>I noticed and changed my code, but lacked the explanation. Thanks for providing it.</p>

#### [ Mario Carneiro (Sep 18 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188910):
<p>basically, if the very first thing in your proof is a lambda/<code>intro</code>, you should probably shift your colon</p>

#### [ Kevin Buzzard (Sep 18 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188921):
<p>my partner does that for a living</p>

#### [ Kevin Buzzard (Sep 18 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188934):
<p>she's a colorectal surgeon</p>

#### [ Mario Carneiro (Sep 18 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188980):
<p>I need an emoji for this</p>

#### [ Tobias Grosser (Sep 18 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189102):
<p>Meanwhile, things look a lot better: <a href="https://github.com/tobig/lean-polyhedra/blob/master/src/polyhedra.lean" target="_blank" title="https://github.com/tobig/lean-polyhedra/blob/master/src/polyhedra.lean">https://github.com/tobig/lean-polyhedra/blob/master/src/polyhedra.lean</a></p>

#### [ Tobias Grosser (Sep 18 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189125):
<p>In case you have more suggestions:</p>
<div class="codehilite"><pre><span></span>protected def matrix.le_trans [partial_order α] (a b c: matrix n m α)
  (h1 : a ≤ b) (h2 : b ≤ c) : a ≤ c :=
begin
  assume i: n,
  assume j: m,
  have h1l: a i j ≤ b i j, from h1 i j,
  have h2l: b i j ≤ c i j, from h2 i j,
  transitivity,
  apply h1l,
  apply h2l,
end
</pre></div>


<p>and</p>
<div class="codehilite"><pre><span></span>protected def matrix.le_refl [partial_order α] (A: matrix n m α) :
A ≤ A :=
begin
  assume i: n,
  assume j: m,
  refl
end
</pre></div>


<p>are also open for golfing. ;-)</p>

#### [ Tobias Grosser (Sep 18 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189147):
<p>I will golf myself a little browsing mathlib code.</p>

#### [ Kenny Lau (Sep 18 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189154):
<div class="codehilite"><pre><span></span><span class="kn">protected</span> <span class="n">def</span> <span class="n">matrix</span><span class="bp">.</span><span class="n">le_trans</span> <span class="o">[</span><span class="n">partial_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span><span class="o">:</span> <span class="n">matrix</span> <span class="n">n</span> <span class="n">m</span> <span class="n">α</span><span class="o">)</span>
  <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">h2</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">c</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">c</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">intros</span> <span class="n">i</span> <span class="n">j</span><span class="bp">;</span> <span class="k">from</span> <span class="n">le_trans</span> <span class="o">(</span><span class="n">h1</span> <span class="n">i</span> <span class="n">j</span><span class="o">)</span> <span class="o">(</span><span class="n">h2</span> <span class="n">i</span> <span class="n">j</span><span class="o">)</span>

<span class="kn">protected</span> <span class="n">def</span> <span class="n">matrix</span><span class="bp">.</span><span class="n">le_refl</span> <span class="o">[</span><span class="n">partial_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">A</span><span class="o">:</span> <span class="n">matrix</span> <span class="n">n</span> <span class="n">m</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">A</span> <span class="bp">≤</span> <span class="n">A</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">intros</span> <span class="n">i</span> <span class="n">j</span><span class="bp">;</span> <span class="n">refl</span>
</pre></div>

#### [ Kenny Lau (Sep 18 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189245):
<div class="codehilite"><pre><span></span><span class="kn">protected</span> <span class="n">def</span> <span class="n">matrix</span><span class="bp">.</span><span class="n">le_trans</span> <span class="o">[</span><span class="n">partial_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span><span class="o">:</span> <span class="n">matrix</span> <span class="n">n</span> <span class="n">m</span> <span class="n">α</span><span class="o">)</span>
  <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">h2</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">c</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">c</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">intros</span> <span class="n">i</span> <span class="n">j</span><span class="bp">;</span> <span class="n">transitivity</span><span class="bp">;</span> <span class="n">solve_by_elim</span>
</pre></div>

#### [ Kenny Lau (Sep 18 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189264):
<p>hmm the last one may not work</p>

#### [ Tobias Grosser (Sep 18 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189409):
<p>They all work.</p>

#### [ Kevin Buzzard (Sep 18 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189412):
<div class="codehilite"><pre><span></span><span class="kn">protected</span> <span class="n">def</span> <span class="n">matrix</span><span class="bp">.</span><span class="n">le_refl</span> <span class="o">[</span><span class="n">partial_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">A</span><span class="o">:</span> <span class="n">matrix</span> <span class="n">n</span> <span class="n">m</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
<span class="n">A</span> <span class="bp">≤</span> <span class="n">A</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">i</span> <span class="n">j</span><span class="o">,</span> <span class="n">le_refl</span> <span class="bp">_</span>
</pre></div>

#### [ Tobias Grosser (Sep 18 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189417):
<p>I learned a lot. So much fun.</p>

#### [ Kevin Buzzard (Sep 18 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189468):
<div class="codehilite"><pre><span></span><span class="kn">protected</span> <span class="n">def</span> <span class="n">matrix</span><span class="bp">.</span><span class="n">le_refl</span> <span class="o">[</span><span class="n">partial_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">A</span><span class="o">:</span> <span class="n">matrix</span> <span class="n">n</span> <span class="n">m</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
<span class="n">A</span> <span class="bp">≤</span> <span class="n">A</span> <span class="o">:=</span> <span class="bp">λ_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">le_refl</span> <span class="bp">_</span>
</pre></div>

#### [ Kevin Buzzard (Sep 18 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189479):
<p>bad style (should be a space after the lambda)</p>

#### [ Kevin Buzzard (Sep 18 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189493):
<p>but I'm just trying to beat Kenny</p>

#### [ Tobias Grosser (Sep 18 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189508):
<p>Now I am unsure which ones to commit.</p>

#### [ Kevin Buzzard (Sep 18 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189560):
<p><code>set_option profiler true</code> and see which one is quickest :-)</p>

#### [ Tobias Grosser (Sep 18 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189566):
<p>I feel the last ones are a little too tight. What's the stylistic preferred solution?</p>

#### [ Kevin Buzzard (Sep 18 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189584):
<div class="codehilite"><pre><span></span><span class="kn">protected</span> <span class="n">def</span> <span class="n">matrix</span><span class="bp">.</span><span class="n">le_refl</span> <span class="o">[</span><span class="n">partial_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">A</span><span class="o">:</span> <span class="n">matrix</span> <span class="n">n</span> <span class="n">m</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
<span class="n">A</span> <span class="bp">≤</span> <span class="n">A</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">le_refl</span> <span class="bp">_</span>
</pre></div>


<p>would probably be fine for mathlib I suspect</p>

#### [ Chris Hughes (Sep 18 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189797):
<p>Shouldn't all of this be <code>by pi_instance</code>?</p>

#### [ Kevin Buzzard (Sep 18 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189804):
<p>right</p>

#### [ Kevin Buzzard (Sep 18 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189858):
<p>but I don't know if they did partial orders and I didn't look.</p>

#### [ Kenny Lau (Sep 18 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189876):
<p>I believe they did</p>

#### [ Kenny Lau (Sep 18 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189882):
<p>though I too did not look</p>

#### [ Kevin Buzzard (Sep 18 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189931):
<p><span class="user-mention" data-user-id="122318">@Tobias Grosser</span> The original matrix add_comm_group code was written by Ellen Arlt and I was rewriting it in a live Lean coding session with an audience of undergrads, and Chris pointed out that pi_instances just did everything immediately.</p>

#### [ Tobias Grosser (Sep 18 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134190187):
<p>Interesting. I don't know how to use pi_instance(s)</p>

#### [ Tobias Grosser (Sep 18 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134190270):
<p>If I just write pi_instance, I get "too many constructors" for the first two lemmas, and "failed" for the last.</p>

#### [ Tobias Grosser (Sep 19 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134212318):
<p>I made some good progress, but got stuck in type class resolution. I try to do dependent pattern matching in the following code:</p>
<div class="codehilite"><pre><span></span>#check matrix
universe v
def Gaussian_elimination {α : Type v} [ordered_ring α] :
   Π {x y : Type u}  [fintype x] [fintype y], matrix x y α →  α
| _ _ _ := 1
</pre></div>


<p>Unfortunately, I get the following error at location 'matrix':</p>
<div class="codehilite"><pre><span></span>polyhedra.lean:104:46: error

failed to synthesize type class instance for
α : Type v,
_inst_4 : ordered_ring α,
x y : Type u,
_inst_5 : fintype x,
_inst_6 : fintype y
⊢ fintype x
polyhedra.lean:104:46: error
</pre></div>

#### [ Tobias Grosser (Sep 19 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134212376):
<p>I modeled this according to <a href="https://leanprover.github.io/theorem_proving_in_lean/induction_and_recursion.html#dependent-pattern-matching" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/induction_and_recursion.html#dependent-pattern-matching">https://leanprover.github.io/theorem_proving_in_lean/induction_and_recursion.html#dependent-pattern-matching</a>, and therae the example on vector works without problems. In case anybody has some flyby ideas.</p>

#### [ Mario Carneiro (Sep 19 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134213060):
<p><code>by exactI 1</code></p>

#### [ Tobias Grosser (Sep 19 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134213712):
<p>Is this in reply to the type class issue?</p>

#### [ Tobias Grosser (Sep 19 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134213766):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Gaussian_elimination</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">ordered_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span>
   <span class="bp">Π</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>  <span class="o">[</span><span class="n">fintype</span> <span class="n">x</span><span class="o">]</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">y</span><span class="o">],</span> <span class="n">matrix</span> <span class="n">x</span> <span class="n">y</span> <span class="n">α</span> <span class="bp">→</span>  <span class="n">α</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">exactI</span> <span class="mi">1</span>
</pre></div>


<p>does not work for me.</p>

#### [ Tobias Grosser (Sep 19 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134213773):
<p>I still get an error at 'matrix x y \a'</p>

#### [ Tobias Grosser (Sep 19 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134213854):
<p>I also don't see why I would add a tactics proof at a definition of a value. This seems to not make a lot of sense to me.</p>

#### [ Kenny Lau (Sep 19 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134213905):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Gaussian_elimination</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">ordered_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span>
   <span class="bp">Π</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>  <span class="o">[</span><span class="n">fintype</span> <span class="n">x</span><span class="o">]</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">y</span><span class="o">],</span> <span class="n">matrix</span> <span class="n">x</span> <span class="n">y</span> <span class="n">α</span> <span class="bp">→</span>  <span class="n">α</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">exactI</span> <span class="mi">1</span>
</pre></div>

#### [ Tobias Grosser (Sep 19 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134213986):
<p>Thanks, now I know how to use syntax highlighting.</p>

#### [ Tobias Grosser (Sep 19 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134213988):
<p>But your code does not work either.</p>

#### [ Tobias Grosser (Sep 19 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134213990):
<p>I still get:</p>
<div class="codehilite"><pre><span></span>polyhedra.lean:108:46: error

failed to synthesize type class instance for
α : Type v,
_inst_4 : ordered_ring α,
x y : Type u,
_inst_5 : fintype x,
_inst_6 : fintype y
⊢ fintype x
</pre></div>

#### [ Kenny Lau (Sep 19 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214030):
<p>is that the whole error?</p>

#### [ Kenny Lau (Sep 19 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214037):
<p>oh, the error is in the type</p>

#### [ Tobias Grosser (Sep 19 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214038):
<p>I get it 4 times in a row at the same location.</p>

#### [ Tobias Grosser (Sep 19 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214041):
<p>Yes, something is broken. I just don't know how to interpret the error message.</p>

#### [ Tobias Grosser (Sep 19 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214046):
<p>It seems to derive fintype x, but I feel I provided all information.</p>

#### [ Kenny Lau (Sep 19 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214050):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Gaussian_elimination</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">ordered_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span>
   <span class="bp">Π</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>  <span class="o">[</span><span class="n">hx</span> <span class="o">:</span> <span class="n">fintype</span> <span class="n">x</span><span class="o">]</span> <span class="o">[</span><span class="n">hy</span> <span class="o">:</span> <span class="n">fintype</span> <span class="n">y</span><span class="o">],</span> <span class="bp">@</span><span class="n">matrix</span> <span class="n">x</span> <span class="n">y</span> <span class="n">α</span> <span class="n">hx</span> <span class="n">hy</span> <span class="bp">_</span> <span class="bp">→</span>  <span class="n">α</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">exactI</span> <span class="mi">1</span>
</pre></div>

#### [ Kenny Lau (Sep 19 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214051):
<p>something like that</p>

#### [ Kenny Lau (Sep 19 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214055):
<p>the order of the arguments may be wrong</p>

#### [ Kenny Lau (Sep 19 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214096):
<p>I don't see why you would need pattern matching</p>

#### [ Kenny Lau (Sep 19 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214107):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Gaussian_elimination</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">ordered_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">x</span><span class="o">]</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">y</span><span class="o">]</span> <span class="o">:</span>
  <span class="n">matrix</span> <span class="n">x</span> <span class="n">y</span> <span class="n">α</span> <span class="bp">→</span>  <span class="n">α</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span> <span class="mi">1</span>
</pre></div>

#### [ Tobias Grosser (Sep 19 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214156):
<p>The one without pattern matching works (I managed to write sth similar myself).</p>

#### [ Tobias Grosser (Sep 19 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214161):
<p>The @matrix one breaks with:</p>

#### [ Tobias Grosser (Sep 19 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214168):
<div class="codehilite"><pre><span></span>polyhedra.lean:192:57: error

type mismatch at application
  matrix x y
term
  α
has type
  Type v : Type (v+1)
but is expected to have type
  fintype x : Type u
</pre></div>

#### [ Kenny Lau (Sep 19 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214176):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Gaussian_elimination</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">ordered_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span>
   <span class="bp">Π</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>  <span class="o">[</span><span class="n">hx</span> <span class="o">:</span> <span class="n">fintype</span> <span class="n">x</span><span class="o">]</span> <span class="o">[</span><span class="n">hy</span> <span class="o">:</span> <span class="n">fintype</span> <span class="n">y</span><span class="o">],</span> <span class="bp">@</span><span class="n">matrix</span> <span class="n">x</span> <span class="n">y</span> <span class="n">hx</span> <span class="n">hy</span> <span class="n">α</span> <span class="bp">_</span> <span class="bp">→</span> <span class="n">α</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">exactI</span> <span class="mi">1</span>
</pre></div>

#### [ Tobias Grosser (Sep 19 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214177):
<p>I want to implement something similar to</p>
<div class="codehilite"><pre><span></span>Fixpoint Gaussian_elimination {m n} : &#39;M_(m, n) → &#39;M_m × &#39;M_n × nat :=
  match m, n with
  | _.+1, _.+1 ⇒ fun A : &#39;M_(1 + _, 1 + _) ⇒
    if [pick ij | A ij.1 ij.2 != 0] is Some (i, j) then
      let a := A i j in let A1 := xrow i 0 (xcol j 0 A) in
      let u := ursubmx A1 in let v := a^-1 *: dlsubmx A1 in
      let: (L, U, r) := Gaussian_elimination (drsubmx A1 - v ×m u) in
      (xrow i 0 (block_mx 1 0 v L), xcol j 0 (block_mx a%:M u 0 U), r.+1)
    else (1%:M, 1%:M, 0%N)
  | _, _ ⇒ fun _ ⇒ (1%:M, 1%:M, 0%N)
  end.
</pre></div>

#### [ Tobias Grosser (Sep 19 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214224):
<p>As implemented in mathcomp.</p>

#### [ Tobias Grosser (Sep 19 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214229):
<p>Need it to compute the matrix rank.</p>

#### [ Tobias Grosser (Sep 19 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214302):
<div class="codehilite"><pre><span></span>polyhedra.lean:196:57: error

function expected at
  matrix x y α
term has type
  Type (max u v)
</pre></div>


<p>for the last one.</p>

#### [ Tobias Grosser (Sep 19 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214312):
<p>Matrix is defined as <code>matrix : Π (m n : Type u_1) [_inst_1 : fintype m] [_inst_2 : fintype n], Type u_2 → Type (max u_1 u_2)</code></p>

#### [ Tobias Grosser (Sep 19 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214362):
<p>This one works:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Gaussian_elimination5</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">ordered_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span>
   <span class="bp">Π</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>  <span class="o">[</span><span class="n">hx</span> <span class="o">:</span> <span class="n">fintype</span> <span class="n">x</span><span class="o">]</span> <span class="o">[</span><span class="n">hy</span> <span class="o">:</span> <span class="n">fintype</span> <span class="n">y</span><span class="o">],</span> <span class="bp">@</span><span class="n">matrix</span> <span class="n">x</span> <span class="n">y</span> <span class="n">hx</span> <span class="n">hy</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">exactI</span> <span class="mi">1</span>
</pre></div>

#### [ Tobias Grosser (Sep 19 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214378):
<p>Thanks.</p>

#### [ Tobias Grosser (Sep 19 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214379):
<p>Need to read up what all this stuff does.</p>

#### [ Tobias Grosser (Sep 19 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214390):
<p>I am especially surprised that I need to pass the hx, hy as parameters.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214768):
<p>I never answered your question about how to use <code>pi_instances</code>. It was used at some point in the code defining matrices, but this was in a branch of mathlib-community in code that got rewritten and then I think the branch was deleted? I couldn't find it anyway. In short, it's a tactic whereby if <code>f x</code> has a certain structure (e.g. that of an additive group) then<code>Pi x, f x</code> gets it too. For matrices over a ring it would immediately give them the structure of an additive commutative group by just guessing addition and zero and then figuring out the proofs itself. Of course it can't guess multiplication (if you asked it to, I guess it would guess pointwise multiplication of matrices).</p>

#### [ Tobias Grosser (Sep 19 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214936):
<p>Thanks.</p>

#### [ Tobias Grosser (Sep 19 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215050):
<p>Ok, the last one for this morning:</p>
<div class="codehilite"><pre><span></span>def Gaussian_elimination5 {α : Type v} [ordered_ring α] {x y} [has_one x] [has_one y]:
   Π {x y}  [hx : fintype x] [hy : fintype y], @matrix x y hx hy α  → α
| (x+1) _ _ _ _ := by exactI 1
</pre></div>

#### [ Tobias Grosser (Sep 19 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215121):
<p>Gives me "equation compiler failed (use 'set_option trace.eqn_compiler.elim_match true' for additional details)".<br>
Setting this option does not give me more details.</p>

#### [ Kenny Lau (Sep 19 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215131):
<p>1. you have two <code>x</code> and two <code>y</code>, which would cause much confusion, although it is not the source of the error</p>

#### [ Tobias Grosser (Sep 19 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215133):
<p>I wanted x to be both a fintype and a type with has_one.</p>

#### [ Kenny Lau (Sep 19 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215140):
<p>the source of the error is that the type of <code>(x+1)</code>, whatever it is, is not an inductive type with <code>_+1</code> as one of the constructors</p>

#### [ Tobias Grosser (Sep 19 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215193):
<p>Right. It's a fintype.</p>

#### [ Tobias Grosser (Sep 19 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215195):
<p>I also want to make it to satisfy has_one.</p>

#### [ Tobias Grosser (Sep 19 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215198):
<p>That's why I added additional constraints.</p>

#### [ Kenny Lau (Sep 19 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215204):
<p>you have two <code>x</code> and two <code>y</code>. Lean treats those as separate objects.</p>

#### [ Tobias Grosser (Sep 19 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215212):
<p>Right, I lack the notation how to add more constraints on x.</p>

#### [ Tobias Grosser (Sep 19 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215215):
<p>I tried this one before:</p>
<div class="codehilite"><pre><span></span>def Gaussian_elimination5 {α : Type v} [ordered_ring α]  :
   Π {x y} [has_one x] [has_one y]  [hx : fintype x] [hy : fintype y], @matrix x y hx hy α  → α
| (x+1) _ _ _ _ := by exactI 1
</pre></div>

#### [ Mario Carneiro (Sep 19 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215256):
<p><code>x</code> is not a number, it's a type</p>

#### [ Kenny Lau (Sep 19 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215257):
<p>I don't know what <code>x+1</code> is supposed to mean</p>

#### [ Mario Carneiro (Sep 19 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215259):
<p>This differs from the Coq development because matrices are not defined with indices in 1..n, they are drawn from an arbitrary finite type</p>

#### [ Tobias Grosser (Sep 19 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215271):
<p>Right.</p>

#### [ Tobias Grosser (Sep 19 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215277):
<p>I assumed I can fix this by defining my algorithm to only work if x and y are both finite _and_ satisfy has_one.</p>

#### [ Mario Carneiro (Sep 19 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215317):
<p>You could define your function on <code>matrix (fin m) (fin n) α</code> if you want to do induction on m and n</p>

#### [ Mario Carneiro (Sep 19 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215322):
<p>there is no problem with assuming your type has a one, but that doesn't license you to write <code>x+1</code></p>

#### [ Tobias Grosser (Sep 19 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215328):
<p>That's what I tried ( I forgot that fin m exists, Johannes mentioned it at some point)</p>

#### [ Mario Carneiro (Sep 19 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215331):
<p>if <code>x</code> is a type containing a <code>1</code>, then <code>1 : x</code> is okay</p>

#### [ Tobias Grosser (Sep 19 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215334):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Gaussian_elimination5</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">ordered_ring</span> <span class="n">α</span><span class="o">]</span>  <span class="o">:</span>
   <span class="bp">Π</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span><span class="o">}</span> <span class="o">[</span><span class="n">hx</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">x</span><span class="o">]</span> <span class="o">[</span><span class="n">hy</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">y</span><span class="o">],</span> <span class="bp">@</span><span class="n">matrix</span> <span class="n">x</span> <span class="n">y</span> <span class="n">hx</span> <span class="n">hy</span> <span class="n">α</span>  <span class="bp">→</span> <span class="n">α</span>
<span class="bp">|</span> <span class="o">(</span><span class="bp">_+</span><span class="mi">1</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">exactI</span> <span class="mi">1</span>
</pre></div>

#### [ Tobias Grosser (Sep 19 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215411):
<p>Now I am here. This works so far, but gives the error:</p>
<div class="codehilite"><pre><span></span>polyhedra.lean:201:46: error

maximum class-instance resolution depth has been reached (the limit can be increased by setting option &#39;class.instance_max_depth&#39;) (the class-instance resolution trace can be visualized by setting option &#39;trace.class_instances&#39;)
</pre></div>

#### [ Mario Carneiro (Sep 19 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215418):
<p><code>fin</code> is not a typeclass, it is an actual type</p>
<div class="codehilite"><pre><span></span>def Gaussian_elimination5 {α : Type v} [ordered_ring α]  :
   Π (m n : ℕ), matrix (fin m) (fin n) α  → α
| (m+1) (n+1) := 1
</pre></div>

#### [ Tobias Grosser (Sep 19 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215562):
<p>Amazing: </p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Gaussian_elimination6</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">ordered_ring</span> <span class="n">α</span><span class="o">]</span>  <span class="o">:</span>
   <span class="bp">Π</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span><span class="o">),</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="n">α</span>  <span class="bp">→</span> <span class="n">α</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">m</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="n">A</span> <span class="o">:=</span> <span class="n">A</span> <span class="mi">0</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">A</span> <span class="o">:=</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span>
</pre></div>

#### [ Tobias Grosser (Sep 19 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215623):
<p>That type checks and does what I want. Thanks guys for getting me started.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134216363):
<p><code>has_one</code> only means there's some term in your type called <code>1</code>. You need <code>has_add</code> too to make sense of <code>x + 1</code>.</p>

#### [ Johan Commelin (Sep 19 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134216462):
<p>Right, so you want <code>has_one Type</code> and <code>has_add Type</code> (-;</p>

#### [ Tobias Grosser (Sep 19 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217164):
<p>That's what I understand.</p>

#### [ Tobias Grosser (Sep 19 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217168):
<p>Now I don't understand how torequest such a type in a pattern match.</p>

#### [ Tobias Grosser (Sep 19 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217171):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Gaussian_elimination5</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">ordered_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span>
   <span class="bp">Π</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">has_one</span> <span class="n">x</span><span class="o">]</span> <span class="o">[</span><span class="n">has_add</span> <span class="n">x</span><span class="o">]</span> <span class="o">[</span><span class="n">has_one</span> <span class="n">y</span><span class="o">]</span> <span class="o">[</span><span class="n">has_add</span> <span class="n">y</span><span class="o">]</span> <span class="o">[</span><span class="n">hx</span> <span class="o">:</span> <span class="n">fintype</span> <span class="n">x</span><span class="o">]</span> <span class="o">[</span><span class="n">hy</span> <span class="o">:</span> <span class="n">fintype</span> <span class="n">y</span><span class="o">],</span> <span class="bp">@</span><span class="n">matrix</span> <span class="n">x</span> <span class="n">y</span> <span class="n">hx</span> <span class="n">hy</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span>
<span class="bp">|</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="n">e</span> <span class="n">f</span> <span class="n">g</span> <span class="n">h</span> <span class="n">i</span> <span class="o">:=</span>
</pre></div>

#### [ Tobias Grosser (Sep 19 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217173):
<p>This is what I came up with.</p>

#### [ Mario Carneiro (Sep 19 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217219):
<p>you can't pattern match on types</p>

#### [ Kevin Buzzard (Sep 19 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217222):
<p>As a general rule you shouldn't need to name variables which are showing up in <code>[boxes like this]</code></p>

#### [ Kevin Buzzard (Sep 19 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217225):
<p>The system is supposed to do that for you</p>

#### [ Tobias Grosser (Sep 19 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217232):
<p>I don't want to match  on types.</p>

#### [ Tobias Grosser (Sep 19 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217236):
<p>It seems I need to match on all the boxes for this to type check.</p>

#### [ Tobias Grosser (Sep 19 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217239):
<p>What I would like is something like</p>

#### [ Kevin Buzzard (Sep 19 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217247):
<p>You could move stuff to the left of the colon</p>

#### [ Mario Carneiro (Sep 19 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217251):
<p>this line is almost certainly not what you want</p>

#### [ Kevin Buzzard (Sep 19 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217254):
<p>the equation compiler only matches on stuff to the right of the colon</p>

#### [ Kevin Buzzard (Sep 19 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217307):
<p>and similarly in general you should be able to avoid using <code>@</code></p>

#### [ Kevin Buzzard (Sep 19 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217314):
<p>because Lean is supposed to guess correctly</p>

#### [ Mario Carneiro (Sep 19 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217326):
<p>Also, in case it wasn't clear Johan's suggestion above was not serious</p>

#### [ Mario Carneiro (Sep 19 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217332):
<p>you don't actually want <code>has_add Type</code></p>

#### [ Mario Carneiro (Sep 19 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217339):
<p>Perhaps you could explain what you are trying to do informally?</p>

#### [ Kevin Buzzard (Sep 19 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217376):
<p>You're more likely to want <code>has_add X</code> with <code>X : Type</code></p>

#### [ Mario Carneiro (Sep 19 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217383):
<p>I'm not sure you want that either though, in this case</p>

#### [ Kevin Buzzard (Sep 19 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217388):
<p>On the other hand, I am pretty sure we want Gaussian Elimination</p>

#### [ Tobias Grosser (Sep 19 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217402):
<p>I want a function that takes a (matrix n m \a) and returns an alpha (for now)</p>

#### [ Kevin Buzzard (Sep 19 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217403):
<p>It's kind of a disgrace that we only just got matrices and that we still don't have differentiation of functions from R to R</p>

#### [ Tobias Grosser (Sep 19 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217404):
<p>I also want to do induction over n and m</p>

#### [ Tobias Grosser (Sep 19 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217406):
<p>So I looked at dependent type pattern matching</p>

#### [ Kevin Buzzard (Sep 19 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217408):
<p><span class="user-mention" data-user-id="122318">@Tobias Grosser</span> your two goals sound very achievable</p>

#### [ Mario Carneiro (Sep 19 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217409):
<p>In that case you should go with the version I stated with <code>fin m</code> and <code>fin n</code></p>

#### [ Tobias Grosser (Sep 19 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217410):
<p>And my understanding is that I need to constrain n and m to satisfy has_add and has_one.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217413):
<p>if <code>fin n</code> makes sense</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217415):
<p>then <code>n : nat</code></p>

#### [ Tobias Grosser (Sep 19 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217458):
<p>Right. That one works perfectly.</p>

#### [ Mario Carneiro (Sep 19 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217463):
<p><code>fin m</code> is a type, which already has a one and an add</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217464):
<p>and <code>nat</code> already has a 1 and an +</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217467):
<p>as does <code>fin n</code></p>

#### [ Tobias Grosser (Sep 19 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217472):
<p>I have a variant that works</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217505):
<p>feel free to post code</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217506):
<p>Which is:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Gaussian_elimination6</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">ordered_ring</span> <span class="n">α</span><span class="o">]</span>  <span class="o">:</span>
   <span class="bp">Π</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span><span class="o">),</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="n">α</span>  <span class="bp">→</span> <span class="n">α</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">m</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="n">A</span> <span class="o">:=</span> <span class="n">A</span> <span class="mi">0</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">A</span> <span class="o">:=</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span>
</pre></div>

#### [ Tobias Grosser (Sep 19 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217554):
<p>(I mean the pattern match, not the gaussian elimination yet)</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217556):
<p>gotcha</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217558):
<p>You use m and n to mean two different things</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217560):
<p>you were doing this with x and y earlier</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217562):
<p>I find it quite confusing</p>

#### [ Mario Carneiro (Sep 19 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217563):
<p>I think it was a bad idea to call the types <code>m</code> and <code>n</code> in the definition of <code>matrix</code></p>

#### [ Tobias Grosser (Sep 19 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217565):
<p>I was asking for has_one has_add out of curiosity (and also it seemed it would be preferable)</p>

#### [ Mario Carneiro (Sep 19 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217569):
<p>we never use lowercase latin for types</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217572):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Gaussian_elimination6</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">ordered_ring</span> <span class="n">α</span><span class="o">]</span>  <span class="o">:</span>
   <span class="bp">Π</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span><span class="o">),</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="n">α</span>  <span class="bp">→</span> <span class="n">α</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="n">A</span> <span class="o">:=</span> <span class="n">A</span> <span class="mi">0</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">A</span> <span class="o">:=</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Sep 19 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217573):
<p>The matching only matches stuff to the right of the colon, so you're writing "let m = m + 1".</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217618):
<p>I used to do this in mathematics when I was younger -- "I have a quadratic equation x^2+bx+c=0 -- now let's complete the square by setting x=x+b/2"</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217623):
<p>I am aware that 'n' and 'm' in my original example mean different things.</p>

#### [ Mario Carneiro (Sep 19 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217624):
<p>where would you want to perform an addition, where you can't already?</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217634):
<p>All is good in this example.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217638):
<p>I never write that now because it's so easy to lose track of whether you're using the old x or the new x. Now I write "let y = x+b/2"</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217639):
<p>Things work fo rme.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217663):
<p>The only time I let "x=x+1" nowadays is in procedural programming when I actually want the old value to be forgotten forever</p>

#### [ Mario Carneiro (Sep 19 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217710):
<p>Here is a working version that doesn't use fin:</p>
<div class="codehilite"><pre><span></span>def Gaussian_elimination6 {α : Type v} [ordered_ring α]
  (M N) [fintype M] [fintype N] : matrix M N α  → α
| A := A 0 0
</pre></div>


<p>But you can't do induction on <code>m : nat</code> in this case, since there is no <code>m</code></p>

#### [ Tobias Grosser (Sep 19 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217715):
<p>Right.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217716):
<blockquote>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Gaussian_elimination6</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">ordered_ring</span> <span class="n">α</span><span class="o">]</span>  <span class="o">:</span>
   <span class="bp">Π</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span><span class="o">),</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="n">α</span>  <span class="bp">→</span> <span class="n">α</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="n">A</span> <span class="o">:=</span> <span class="n">A</span> <span class="mi">0</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">A</span> <span class="o">:=</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span>
</pre></div>


</blockquote>
<p>Do you see that you're also using the fact that <code>fin (x+1)</code> has a zero here.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217722):
<p>Type class inference figured that out for you and let you use it</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217730):
<p>Yes.</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217736):
<p>That's why I had to write (0:\a) in the second match.</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217741):
<p>I think.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217744):
<p><code>0</code> by itself means "the zero of something"</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217745):
<p>Because in that case it is not known that a zero exists.</p>

#### [ Mario Carneiro (Sep 19 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217746):
<p>Kevin means the <code>0</code> in <code>A 0 0</code></p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217751):
<p>Lean was expecting something of type "fin (x+1)" and you wrote "0"</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217798):
<p>Right.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217801):
<p>and Lean figured "aah, this must be one of those types that has a zero, let me find an instance of has_zero (fin (x+1)) behind the scenes</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217812):
<p>I wrote</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Gaussian_elimination6</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">ordered_ring</span> <span class="n">α</span><span class="o">]</span>  <span class="o">:</span>
   <span class="bp">Π</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span><span class="o">),</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="n">α</span>  <span class="bp">→</span> <span class="n">α</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="n">A</span> <span class="o">:=</span> <span class="n">A</span> <span class="mi">0</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">A</span> <span class="o">:=</span> <span class="n">A</span> <span class="mi">0</span> <span class="mi">0</span>
</pre></div>

#### [ Tobias Grosser (Sep 19 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217815):
<p>Initially</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217828):
<p>Lean's typeclass magic: <code>example (x : ℕ) : has_zero (fin (x+1)) := by apply_instance</code></p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217835):
<p>your initial approach doesn't work becasue <code>fin 0</code> is the empty type and in particular has no zero</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217838):
<p>Right.</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217841):
<p>I understood this.</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217843):
<p>That's very interesting.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217898):
<p><code>example : has_zero (fin 0) := by apply_instance -- "failed to generate instance" error</code></p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217911):
<p>This black magic is related to the square bracket stuff and it took me a very long time before I got comfortable with it.</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217914):
<p>I see.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217924):
<p>In retrospect I wish that people had stressed earlier how basic notation like <code>0</code> and <code>+</code> worked in Lean</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217927):
<p>The only thing I do not understand is if it is possible to take Mario's stuff, but expose n and m without introducing 'fin n', but instead just use has_one and has_add.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217928):
<p>because it seems to me that this is a very good introduction to the type class system</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217935):
<p>I feel this should work, but seems to be far beyond my type_class capabilities.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217937):
<p>I'm afraid I'm not a computer scientist and I don't know what "expose" means</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217970):
<p>As I have a solution, that's not needed. But would be nice to understand this eventually.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217983):
<p><code>matrix</code> eats something of type <code>fin n</code></p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217987):
<p>so you have to give it something of type <code>fin n</code></p>

#### [ Mario Carneiro (Sep 19 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217989):
<p>actually it eats a fintype</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217992):
<p>"expose" means pattern match on n and m to be able to do induction on n and m</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217994):
<p>Right. I can pass it a fin n and all is good.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218002):
<p>wait, that's not even true any more</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218005):
<p>I was wondering if I could pass it a fintype x, where I know that x has_add and has_one.</p>

#### [ Mario Carneiro (Sep 19 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218006):
<p>any fintype has a cardinality, <code>fintype.card X</code>, and you can do induction on that</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218012):
<p>sorry, I seem to be behind the times</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218023):
<p><code>#check @matrix -- matrix : Π (m n : Type u_1) [_inst_1 : fintype m] [_inst_2 : fintype n], Type u_2 → Type (max u_1 u_2)</code></p>

#### [ Mario Carneiro (Sep 19 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218026):
<p>You don't usually need a one and an add on the index type</p>

#### [ Mario Carneiro (Sep 19 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218035):
<p>what is this needed for?</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218072):
<p>So how can I do induction over card? That's what I am trying to figure out.</p>

#### [ Mario Carneiro (Sep 19 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218079):
<p>It's a bit messy</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218084):
<p>Do you want to prove things for matrices indexed by random finite types?</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218085):
<p>I just want to do induction on my dimensionality to do gaussion elimination.</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218090):
<p>No. If you tell me 'fin x' is enough, we are done.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218103):
<p>I guess this is a design decision</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218104):
<p>Just got curious about the type classes. Seems matlib likes to generalize things.</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218111):
<p>I am fine being in 'fin x'. That seems a lot less messy.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218113):
<p>Yes, if mathlib did Gaussian Elimination it would almost certainly do it for random types which are fintypes</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218114):
<p>Let's leave it at this for now.</p>

#### [ Mario Carneiro (Sep 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218116):
<div class="codehilite"><pre><span></span>def Gaussian_elimination6 {α : Type v} [ordered_ring α]
  : ∀ (m n M N) [fintype M] [fintype N], fintype.card M = m → fintype.card N = n → matrix M N α  → α
| m n M N _ _ h1 h2 A := A 0 0
</pre></div>


<p>You will need some <code>@</code>'s in there, my typechecker isn't running</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218164):
<p>If you do it like that then you can induct on m and n</p>

#### [ Mario Carneiro (Sep 19 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218173):
<p>More likely, I would just do it on <code>fin m</code> by induction and then use equivalence lemmas to transfer to the original fintype</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218187):
<div class="codehilite"><pre><span></span><span class="n">failed</span> <span class="n">to</span> <span class="n">synthesize</span> <span class="n">type</span> <span class="n">class</span> <span class="kn">instance</span> <span class="n">for</span>
<span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">ordered_ring</span> <span class="n">α</span><span class="o">,</span>
<span class="n">m</span> <span class="o">:</span> <span class="err">?</span><span class="n">m_1</span><span class="o">,</span>
<span class="n">n</span> <span class="o">:</span> <span class="err">?</span><span class="n">m_2</span><span class="o">,</span>
<span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span> <span class="err">?</span><span class="o">,</span>
<span class="n">N</span> <span class="o">:</span> <span class="kt">Type</span> <span class="err">?</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_2</span> <span class="o">:</span> <span class="n">fintype</span> <span class="n">M</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_3</span> <span class="o">:</span> <span class="n">fintype</span> <span class="n">N</span>
<span class="err">⊢</span> <span class="n">fintype</span> <span class="n">M</span>
</pre></div>

#### [ Kevin Buzzard (Sep 19 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218188):
<p>boo</p>

#### [ Mario Carneiro (Sep 19 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218189):
<p>Or find a way to work with subsets of a fixed type of size <code>m</code></p>

#### [ Mario Carneiro (Sep 19 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218193):
<p>you have to put a <code>by exactI</code> in there</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218199):
<p>in the statement??</p>

#### [ Mario Carneiro (Sep 19 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218200):
<p>yeah</p>

#### [ Mario Carneiro (Sep 19 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218244):
<p>because there are typeclass args right of the colon</p>

#### [ Mario Carneiro (Sep 19 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218249):
<p>either that or use <code>@</code> a lot</p>

#### [ Kenny Lau (Sep 19 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218261):
<p>deja vu</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218284):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Gaussian_elimination6</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">ordered_ring</span> <span class="n">α</span><span class="o">]</span>
  <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="n">M</span> <span class="n">N</span><span class="o">)</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">M</span><span class="o">]</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">N</span><span class="o">],</span>
      <span class="k">by</span> <span class="n">exactI</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="n">M</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">→</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="n">N</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">matrix</span> <span class="n">M</span> <span class="n">N</span> <span class="n">α</span>  <span class="bp">→</span> <span class="n">α</span>
<span class="bp">|</span> <span class="n">m</span> <span class="n">n</span> <span class="n">M</span> <span class="n">N</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">h1</span> <span class="n">h2</span> <span class="n">A</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Sep 19 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218287):
<p>eew</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218289):
<p>soon to be not fixed in Lean 4</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218347):
<p>that looks fine, not at all confusing for beginners</p>

#### [ Mario Carneiro (Sep 19 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218357):
<p>like I said, messy</p>

#### [ Kevin Buzzard (Sep 19 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218362):
<p>Isn't there some pre-rolled <code>fintype.induction_on</code>?</p>

#### [ Mario Carneiro (Sep 19 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218371):
<p>not to mention that this is not going to be a nice inductive proof since you have to build a recursive subtype</p>

#### [ Mario Carneiro (Sep 19 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218392):
<p>It's probably better to do induction over the finsets on a fixed type</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218397):
<p>Cool. At least it works.</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218450):
<p>I feel I can do induction by using x+1 and y+1</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Gaussian_elimination6</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">ordered_ring</span> <span class="n">α</span><span class="o">]</span>
  <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="n">M</span> <span class="n">N</span><span class="o">)</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">M</span><span class="o">]</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">N</span><span class="o">],</span>
      <span class="k">by</span> <span class="n">exactI</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="n">M</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">→</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="n">N</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">matrix</span> <span class="n">M</span> <span class="n">N</span> <span class="n">α</span>  <span class="bp">→</span> <span class="n">α</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="n">M</span> <span class="n">N</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">h1</span> <span class="n">h2</span> <span class="n">A</span> <span class="o">:=</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">M</span> <span class="n">N</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">h1</span> <span class="n">h2</span> <span class="n">A</span> <span class="o">:=</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span>
</pre></div>

#### [ Tobias Grosser (Sep 19 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218453):
<p>Not sure what recursive subtypes mean.</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218458):
<p>I will start with the (fin n) stuff, which is sth I certainly understand.</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218467):
<p>If all works, I can see if I can generalize things.</p>

#### [ Mario Carneiro (Sep 19 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218488):
<p>when applying the induction hypothesis, you will need to build a type that contains one fewer element than the type you started with</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218503):
<p>I see. That's annoying. I will certainly stay with (fin n)</p>

#### [ Tobias Grosser (Sep 19 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218568):
<p>Thanks again. Now I learned quite a bit. Will need to read up on exactI in type definitions.</p>

#### [ Sean Leather (Sep 19 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218604):
<blockquote>
<p>Will need to read up on exactI in type definitions.</p>
</blockquote>
<p>Note that tactics are simply ways of generating code. They can appear in definitions or proofs. It's just that they are most useful in proofs.</p>


{% endraw %}
