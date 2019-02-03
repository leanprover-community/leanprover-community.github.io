---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/93951ordcaseson.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [or.dcases_on](https://leanprover-community.github.io/archive/113488general/93951ordcaseson.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Zesen Qian (Jul 02 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128973389):
<p>In general, what does this message mean? induction tactic failed, recursor "or.dcases_on" can only eliminate into Prop.</p>

#### [ Zesen Qian (Jul 02 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128973395):
<p>this happens at the head of a inductive function def.</p>

#### [ Kenny Lau (Jul 02 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128973396):
<p>it means you can't decompose an <code>or</code> into data</p>

#### [ Zesen Qian (Jul 02 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128974745):
<p>is it just <code>or</code>, or any inductive types in general? because there is no <code>or</code> in my code.</p>

#### [ Chris Hughes (Jul 02 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128974933):
<p>A lot of (but not all) inductive propositions cannot eliminate into data. inductive non-propositions can always eliminate into data.</p>

#### [ Kevin Buzzard (Jul 02 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128975489):
<p>Stupid question: can one get around this somehow with classical or noncomputable assumptions? Or does one run into contradictions in this generality?</p>

#### [ Kevin Buzzard (Jul 02 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128975510):
<blockquote>
<p>is it just <code>or</code>, or any inductive types in general? because there is no <code>or</code> in my code.</p>
</blockquote>
<p><span class="user-mention" data-user-id="118042">@Zesen Qian</span> If you post a minimal working example as a gist then perhaps someone can locate the <code>or</code> ;-)</p>

#### [ Chris Hughes (Jul 02 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128975607):
<p>You can, but you have to decide what to do when both sides are true.</p>

#### [ Chris Hughes (Jul 02 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128975772):
<p>So you might end up with a function whose behaviour is unknown when they're both true.</p>

#### [ Simon Hudon (Jul 02 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128976030):
<p>By using <code>prod_decidable</code>, you can make a function to go from or to sum:</p>
<div class="codehilite"><pre><span></span><span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">classical</span><span class="bp">.</span><span class="n">prop_decidable</span>

<span class="n">noncomputable</span> <span class="n">def</span> <span class="n">or</span><span class="bp">.</span><span class="n">to_sum</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">∨</span> <span class="n">q</span><span class="o">)</span> <span class="o">:</span> <span class="n">plift</span> <span class="n">p</span> <span class="err">⊕</span> <span class="n">plift</span> <span class="n">q</span> <span class="o">:=</span>
<span class="k">if</span> <span class="n">h&#39;</span> <span class="o">:</span> <span class="n">p</span> <span class="k">then</span> <span class="n">sum</span><span class="bp">.</span><span class="n">inl</span> <span class="bp">⟨</span> <span class="n">h&#39;</span> <span class="bp">⟩</span>
          <span class="k">else</span> <span class="n">sum</span><span class="bp">.</span><span class="n">inr</span> <span class="bp">⟨</span> <span class="k">by</span> <span class="o">{</span> <span class="n">rw</span> <span class="err">←</span> <span class="n">false_or</span> <span class="n">q</span><span class="o">,</span> <span class="n">exact</span> <span class="n">or</span><span class="bp">.</span><span class="n">imp_left</span> <span class="n">h&#39;</span> <span class="n">h</span> <span class="o">}</span> <span class="bp">⟩</span>
</pre></div>

#### [ Reid Barton (Jul 02 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128977157):
<p>What you can't get when eliminating into non-Prop is the computation rule that reduces an application <code>or.cases_on (or.inl p) f g</code> to <code>f p</code> and also <code>or.cases_on (or.inr q) f g</code> to <code>g q</code>, since <code>or.inl trivial = or.inr trivial</code> but <code>f trivial</code> might not be equal to <code>g trivial</code> (unless the result type is a proposition).</p>

#### [ Zesen Qian (Jul 02 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128978404):
<p>sorry so what's default universe level of inductive types that's not specified level? Is it polymorphisized on all levels?</p>

#### [ Simon Hudon (Jul 02 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128978561):
<p>I'm sorry I can't parse your question. Are you talking of an error message?</p>

#### [ Zesen Qian (Jul 02 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128978664):
<p>no I mean like </p>
<div class="codehilite"><pre><span></span>inductive bool
| true
| false
</pre></div>


<p>will there be universe polymorphism for this, or just Type 1?</p>

#### [ Kenny Lau (Jul 02 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128978673):
<p>universe</p>

#### [ Simon Hudon (Jul 02 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128978856):
<p>I would guess it's a <code>Type 0</code> but I recommend you discover it for yourself. Try <code>#check bool</code></p>

#### [ Zesen Qian (Jul 02 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128978943):
<p>yes it's Type 0, thank you.</p>

#### [ Kevin Buzzard (Jul 02 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979001):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">bool1</span>
<span class="bp">|</span> <span class="n">true</span> <span class="o">:</span> <span class="n">bool1</span>
<span class="bp">|</span> <span class="n">false</span> <span class="o">:</span> <span class="n">bool1</span>

<span class="bp">#</span><span class="kn">check</span> <span class="n">bool1</span> <span class="c1">-- Type</span>

<span class="kn">universe</span> <span class="n">u</span>

<span class="kn">inductive</span> <span class="n">bool2</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span>
<span class="bp">|</span> <span class="n">true</span> <span class="o">:</span> <span class="n">bool2</span>
<span class="bp">|</span> <span class="n">false</span> <span class="o">:</span> <span class="n">bool2</span>

<span class="bp">#</span><span class="kn">check</span> <span class="n">bool2</span> <span class="c1">-- Type u_1 (i.e. universe is &quot;whatever&quot;)</span>

<span class="kn">universe</span> <span class="n">v</span>

<span class="bp">#</span><span class="kn">check</span> <span class="n">bool2</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span><span class="o">}</span> <span class="c1">-- Type v</span>
</pre></div>

#### [ Kevin Buzzard (Jul 02 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979004):
<p>There are some tricks</p>

#### [ Zesen Qian (Jul 02 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979252):
<p>Thanks, I guess we can use it to workaround "universe too big" issue with this?</p>

#### [ Zesen Qian (Jul 02 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979305):
<p>I now have an error saying the argument of a constructor is too big.</p>

#### [ Zesen Qian (Jul 02 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979327):
<div class="codehilite"><pre><span></span>inductive t0 : Type u
...

inductive t1 : Type u
| cons : t0 -&gt; t1
</pre></div>

#### [ Simon Hudon (Jul 02 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979349):
<p>On <code>t1</code>?</p>

#### [ Zesen Qian (Jul 02 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979513):
<p>yeah, says the first argument of cons, t0, is too big.</p>

#### [ Kevin Buzzard (Jul 02 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979547):
<p>If you don't tell <code>t1</code> what type it is then this might fix it</p>

#### [ Kevin Buzzard (Jul 02 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979615):
<div class="codehilite"><pre><span></span><span class="kn">universe</span> <span class="n">u</span>

<span class="kn">inductive</span> <span class="n">t0</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span>
<span class="bp">|</span> <span class="n">foo</span> <span class="o">:</span> <span class="n">t0</span>

<span class="kn">inductive</span> <span class="n">t1</span>
<span class="bp">|</span> <span class="n">cons</span> <span class="o">:</span> <span class="n">t0</span> <span class="bp">-&gt;</span> <span class="n">t1</span>
</pre></div>

#### [ Reid Barton (Jul 02 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979630):
<p>Maybe the <code>u</code> of <code>t0</code> is not the same <code>u</code> as in <code>t1</code>, although I would expect a different error message then</p>

#### [ Simon Hudon (Jul 02 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979636):
<p>I was thinking maybe this would be required:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">t1</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span>
<span class="bp">|</span> <span class="n">cons</span> <span class="o">:</span> <span class="n">t0</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="bp">-&gt;</span> <span class="n">t1</span>
</pre></div>

#### [ Simon Hudon (Jul 02 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979662):
<p>But more generally, there is no reason for <code>t0</code> not to be in <code>Type 0</code></p>

#### [ Zesen Qian (Jul 02 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979673):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> thanks, this fixes it.</p>

#### [ Zesen Qian (Jul 02 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979685):
<p>basically I'm still trying out the universes.</p>

#### [ Kevin Buzzard (Jul 02 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979752):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">t0</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">foo</span> <span class="o">:</span> <span class="n">t0</span>

<span class="kn">inductive</span> <span class="n">t1</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">cons</span> <span class="o">:</span> <span class="n">t0</span> <span class="bp">→</span> <span class="n">t1</span>
</pre></div>

#### [ Simon Hudon (Jul 02 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979755):
<p>I learned this the hard way: when definitions are more universe polymorphic than strictly necessary, it gets really painful</p>

#### [ Zesen Qian (Jul 02 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979843):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> but this doesn't provide universe polymorphism.</p>

#### [ Simon Hudon (Jul 02 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979851):
<p>Case in point: my current <code>traversable</code> pull request took me one year to set up. It was not all about universe polymorphism but it certainly made it difficult</p>

#### [ Zesen Qian (Jul 02 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979855):
<p>and I kind of feel my first error in this stream, has something to do with it.</p>

#### [ Andrew Ashworth (Jul 02 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979859):
<p>I'm not sure what universe polymorphism is good for when it comes to concrete programs</p>

#### [ Kenny Lau (Jul 02 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979870):
<p>universe is for consistency</p>

#### [ Andrew Ashworth (Jul 02 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979871):
<p>I feel like everything I need to do lives in <code>Type</code>, for the most part</p>

#### [ Kenny Lau (Jul 02 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979887):
<p>and strengthening</p>

#### [ Zesen Qian (Jul 02 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979892):
<p>I don't know what dependent types is good for when it comes to concrete programs, TBH.</p>

#### [ Kenny Lau (Jul 02 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979895):
<p>and category theory</p>

#### [ Andrew Ashworth (Jul 02 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128979982):
<p>dtt is a bit of an academic stretch right now, true, but one day when there's an efficient method for program extraction, it might be awesome</p>

#### [ Simon Hudon (Jul 02 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980001):
<p>I think we can weaken <span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> 's suggestion and generalize it into: work in <code>Type 0</code> until you run into trouble. Then make the smallest necessary universe generalization</p>

#### [ Andrew Ashworth (Jul 02 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980012):
<p>if you knew how terribly written most of the software that runs the electronics around us was, you'd be rooting for Lean too :)</p>

#### [ Simon Hudon (Jul 02 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980019):
<p>There are tools for lifting monomorphic definitions to using them in polymorphic contexts so <code>Type 0</code> is not handicapping</p>

#### [ Simon Hudon (Jul 02 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980075):
<p>Amen</p>

#### [ Simon Hudon (Jul 02 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980109):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> I'm getting ready for the DeepSpec summer school where people like Adam Chlipala will show us how he uses dependent type theory for building reliable cryptographic implementation. It's hard to argue that it's really just academic</p>

#### [ Andrew Ashworth (Jul 02 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980166):
<p>isn't anything chlipala does academic by definition ;]</p>

#### [ Simon Hudon (Jul 02 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980218):
<p>It depends. Is your definition of academic "anything that happens in a university"? In that case, is the university's janitor studying academic sweeping?</p>

#### [ Simon Hudon (Jul 02 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980322):
<p>In the case of the DeepSpec project, academics are playing the role of leader but the project involves industrial partners so the point is not (only) publication but building systems that work Monday through Sunday</p>

#### [ Zesen Qian (Jul 02 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980388):
<p>before it's getting too far, let me ask one last question:  can I define structure as universe polymorphic?</p>

#### [ Hoang Le Truong (Jul 02 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980390):
<p>Yes it depend. how I get   f (x:α) because I need it to define next object</p>

#### [ Simon Hudon (Jul 02 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980618):
<p><span class="user-mention" data-user-id="116065">@Hoang Le Truong</span> I think you're in the wrong thread</p>

#### [ Reid Barton (Jul 02 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980679):
<p><span class="user-mention" data-user-id="118042">@Zesen Qian</span> about your original error, it has to do with the difference between <code>Prop</code> and <code>Type</code> (or more generally <code>Type u</code>), which is rather different from the difference between <code>Type u</code> for varying <code>u</code></p>

#### [ Reid Barton (Jul 02 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128980778):
<p>You can generalize over both <code>Prop</code> and <code>Type</code> with <code>Sort</code>, but all the <code>Type u</code> for different <code>u</code> work pretty much the same way, while <code>Prop</code> has some different rules</p>

#### [ Zesen Qian (Jul 02 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/128982406):
<p>thanks, I will look into it.</p>

#### [ Zesen Qian (Jul 03 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or.dcases_on/near/129029014):
<p>yeah I give up. Here is the line causing this error:<br>
<a href="https://github.com/riaqn/smtlean/blob/6e5c20aaa344e972528d8089af01f638819ff06c/src/cvc4.lean#L129" target="_blank" title="https://github.com/riaqn/smtlean/blob/6e5c20aaa344e972528d8089af01f638819ff06c/src/cvc4.lean#L129">https://github.com/riaqn/smtlean/blob/6e5c20aaa344e972528d8089af01f638819ff06c/src/cvc4.lean#L129</a></p>


{% endraw %}
