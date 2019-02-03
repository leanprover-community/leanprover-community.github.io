---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/87350Stilldontunderstandsimp.html
---

## Stream: [general](index.html)
### Topic: [Still don't understand simp](87350Stilldontunderstandsimp.html)

---


{% raw %}
#### [ Kevin Buzzard (Jul 27 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130435282):
<p>I still don't understand simp. I tried</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">+</span> <span class="mi">0</span> <span class="bp">+</span> <span class="n">c</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">H</span><span class="o">]</span>
</pre></div>


<p>fully expecting it to work, and it didn't. So I switched to <code>by simp at H;assumption</code> which works fine -- but I feel like I'm missing a trick. What is the correct way to solve this goal? I know I could prove it using <code>zero_add</code> a couple of times -- is best practice to spell out the proof in full or use automation?</p>

#### [ Kevin Buzzard (Jul 27 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130435357):
<p>The moment I try <code>zero_add</code> in term mode I find myself in triangle hell.</p>

#### [ Chris Hughes (Jul 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130435434):
<p><code>simpa using h</code></p>

#### [ Chris Hughes (Jul 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130435456):
<p><code>simp * at *</code></p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130435851):
<blockquote>
<p><code>simpa using h</code></p>
</blockquote>
<p>Do I need an import for this?</p>

#### [ Mario Carneiro (Jul 27 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130436468):
<p>just the usual</p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437084):
<p>That's happening to me more and more. Is there any way I can import every mathlib tactic automatically?</p>

#### [ Mario Carneiro (Jul 27 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437123):
<p><code>import tactic.interactive</code> gets the main tactics, but advanced tactics have their own imports, in particular <code>ring</code> and <code>finish</code></p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437133):
<p>Is there any reason I shouldn't import <code>ring</code> always?</p>

#### [ Mario Carneiro (Jul 27 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437138):
<p>if you don't need it, don't import it</p>

#### [ Mario Carneiro (Jul 27 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437143):
<p>and you shouldn't overuse it anyway, it's slow</p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437145):
<blockquote>
<p>if you don't need it, don't import it</p>
</blockquote>
<p>Why not? If I don't use it, it doesn't even matter</p>

#### [ Mario Carneiro (Jul 27 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437200):
<p>it adds a spurious dependency, which is probably a bigger problem for me than for you</p>

#### [ Mario Carneiro (Jul 27 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437223):
<p>Of course, adding additional dependencies also slows down startup and recompile times</p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437228):
<p>Even if I never use them?</p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437273):
<p>They're compiled on sight?</p>

#### [ Mario Carneiro (Jul 27 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437281):
<p>of course, how would it know if you have used the file unless it compiles the dependency?</p>

#### [ Mario Carneiro (Jul 27 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437292):
<p>the way you are supposed to signal what you depend on is in your import list</p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437304):
<p>How about I don't import it, and every time I use it a little pop-up appears saying "I see you're using <code>ring</code>. Do you want to import <code>tactic.ring</code>?"</p>

#### [ Mario Carneiro (Jul 27 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437309):
<p>how would it know that <code>ring</code> exists?</p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437312):
<p>and same for <code>simpa</code> and <code>tactic.interactive</code></p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437322):
<blockquote>
<p>how would it know that <code>ring</code> exists?</p>
</blockquote>
<p>Because I just tell it, using a "snippet" or something?</p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437377):
<p>"I see that you just deleted the last occurrence of <code>simpa</code>. Do you want me to unimport it again?"</p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437387):
<p>"I see that you used <code>simp</code>. Do you want me to replace that argument with what Lean actually did?"</p>

#### [ Mario Carneiro (Jul 27 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437389):
<p>hm, I suppose one option is to somehow generate an "index" of all definitions in mathlib and their locations, and then store this info in some file with no dependencies and use it for hints</p>

#### [ Mario Carneiro (Jul 27 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437409):
<p>Import analysis like that is very expensive</p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437410):
<p>I'm basically asking for some sort of tactic manager I think.</p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437411):
<p>I just have no idea about what is possible.</p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437471):
<p>Does <code>simpa !? only? (* | [(* | (- id | expr)), ...]?) (with id*)? (using expr)? tactic.simp_config_ext?</code> actually mean something? Where can I learn about what it means?</p>

#### [ Mario Carneiro (Jul 27 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437472):
<p>It is hard to get the analysis exactly right without just recompiling the current file, and if it's not exactly right then there is the possibility of incorrect hints, which will get old fast</p>

#### [ Mario Carneiro (Jul 27 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437486):
<p>yes, it's a description of the parsing of arguments following <code>simpa</code></p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437537):
<p>I want it to be a regex but I can't make sense of it</p>

#### [ Mario Carneiro (Jul 27 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437544):
<p>Basically <code>?</code> means that the previous thing may or may not be present, and <code>*</code> means zero or more of the previous thing</p>

#### [ Sebastian Ullrich (Jul 27 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437546):
<p>It's a pseudorex</p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437547):
<p>oh is it just a regex but using stuff I don't know?</p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437548):
<p>Aah thanks!</p>

#### [ Mario Carneiro (Jul 27 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437559):
<p><code>|</code> means alternatives</p>

#### [ Mario Carneiro (Jul 27 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437563):
<p>i.e. <code>a | b</code> means parse <code>a</code> or parse <code>b</code></p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437618):
<p>and <code>expr</code> is some kind of variable? Or you want something of type <code>expr</code>?</p>

#### [ Mario Carneiro (Jul 27 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437621):
<p><code>expr</code> means parse an expression</p>

#### [ Mario Carneiro (Jul 27 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437622):
<p>and <code>id</code> means parse an identifier</p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437625):
<p>I thought that <code>h</code> was a name in <code>simpa using h</code>, not an <code>expr</code></p>

#### [ Mario Carneiro (Jul 27 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437637):
<p>nope, look for <code>simpa using show</code> in mathlib and you will find several larger examples</p>

#### [ Mario Carneiro (Jul 27 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437644):
<p>it's a nice way to say "use this term, but clean it up first"</p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437689):
<p>so what's <code>with</code>?</p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437693):
<p>I just apply these things at random usually.</p>

#### [ Mario Carneiro (Jul 27 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437699):
<p>most of the args are just passed to <code>simp</code> as is</p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437700):
<p>I have a list of "incantations formed with <code>simp</code> or <code>simpa</code> which have worked for me in the past"</p>

#### [ Mario Carneiro (Jul 27 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437704):
<p>that includes <code>!</code> and <code>with</code></p>

#### [ Mario Carneiro (Jul 27 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437719):
<p>the <code>with</code> arg of <code>simp</code> allows you to simplify with custom simp sets, like <code>functor_norm</code></p>

#### [ Mario Carneiro (Jul 27 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437726):
<p>I don't use it much at all</p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437773):
<p>What does <code>simpa [this]</code> do? Does that not even parse?</p>

#### [ Chris Hughes (Jul 27 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437781):
<p>The same as <code>simp [this], assumption</code></p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437859):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">+</span> <span class="mi">0</span> <span class="bp">+</span> <span class="n">c</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simpa</span> <span class="c1">-- fails</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">+</span> <span class="mi">0</span> <span class="bp">+</span> <span class="n">c</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="n">c</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simpa</span> <span class="c1">-- works</span>
</pre></div>


<p>If you'd told me one works and one failed I would have guessed the other way around.</p>

#### [ Chris Hughes (Jul 27 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437929):
<p>The second one is simplified to <code>c=0 -&gt; c=0</code>. The first one doesn't simplify <code>H</code></p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437940):
<p><code>example : ∀ (y : ℕ), (λ (c : ℕ), 0 + 0 + c = 0) y → y = 0 := by simp </code></p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437982):
<p>I wouldn't have dreamed of applying <code>simp</code> to that because it's not an equality. Am I using <code>simp</code> completely wrong?</p>

#### [ Mario Carneiro (Jul 27 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437984):
<p>Actually <code>simpa [this]</code> is a bit funny - it's more like <code>have this' := this, simp [this] at this', simp [this], exact this'</code></p>

#### [ Mario Carneiro (Jul 27 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130438007):
<p>for the first example you want <code>by simpa using H</code></p>

#### [ Mario Carneiro (Jul 27 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130438050):
<p>The <code>using</code> argument of <code>simpa</code> is pretty important. It's not really optional, it just has a default value of <code>this</code></p>

#### [ Mario Carneiro (Jul 27 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130438054):
<p>so <code>by simpa</code> where there is no <code>this</code> in the context is kind of pointless</p>

#### [ Chris Hughes (Jul 27 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130438060):
<p>One nice feature of <code>simp</code> I discovered today, is it doesn't let you make horrible simp lemma. I tried to prove <code>forall x : zmod 2, x = -x</code> and it didn't let me make it <code>simp</code></p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130438080):
<p>If you try it again you might get banned</p>

#### [ Kevin Buzzard (Jul 27 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130438084):
<p>"no more simp for you for a week"</p>

#### [ Mario Carneiro (Jul 27 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130438146):
<p>your use of <code>simp</code> to prove that is valid but a bit funny and doesn't generalize well</p>

#### [ Mario Carneiro (Jul 27 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130438155):
<p>I would do <code>intros y H; simpa using H</code></p>

#### [ Mario Carneiro (Jul 27 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130438163):
<p><code>simp {contextual := tt}</code> often works in these situations, but I don't think it simplifies the assumptions first</p>


{% endraw %}
