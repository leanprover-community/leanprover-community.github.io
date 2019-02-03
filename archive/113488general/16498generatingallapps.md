---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/16498generatingallapps.html
---

## Stream: [general](index.html)
### Topic: [generating all `app`s](16498generatingallapps.html)

---


{% raw %}
#### [ Scott Morrison (Apr 25 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125644011):
<p>Say I have an <code>e : expr</code>, which is probably some function type, and some other collection of <code>A : list expr</code>, and I would like to find all ways of plugging something from <code>A</code> into the next argument of <code>e</code>. Should I:<br>
1) Actually look at what type <code>e</code> is, in particular the type of its first argument, and then look through <code>A</code> checking if there is anything of that type?<br>
2) Just invoking <code>mk_app e [a]</code> for each <code>a</code> in <code>A</code>, and collect whatever succeeds?</p>

#### [ Scott Morrison (Apr 25 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125644133):
<p>Option 2) is obviously much easier to write, I'm just wondering if I should expect that it is going to be way slower, or something.</p>

#### [ Simon Hudon (Apr 25 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125645974):
<p>It might be worth experimenting but I don't think 2) would be any slower than 1)</p>

#### [ Scott Morrison (Apr 25 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125649582):
<p>err... <code>mk_app</code> takes a <code>name</code> and a <code>list expr</code> worth of arguments. If I just have <code>a b : expr</code>, what's the idiomatic way to apply <code>a</code> to <code>b</code>, inferring implicit arguments and typechecking?</p>

#### [ Simon Hudon (Apr 25 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125649764):
<p>I think <code>type_check (a b)</code> might do the trick. You can also postpone type checking until you actually use those expressions.</p>

#### [ Scott Morrison (Apr 25 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125650082):
<p>Are there some backticks missing in your suggestion there?</p>

#### [ Scott Morrison (Apr 25 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125650086):
<p>I haven't quite internalised quoting and antiquoting ...</p>

#### [ Simon Hudon (Apr 25 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125650146):
<p>In this case, I'm just using the fact that <code>expr</code> has a <code>has_coe_to_fun</code> instance so you can use an expr as a function and it just wraps it in a <code>expr.app</code></p>

#### [ Scott Morrison (Apr 25 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125650266):
<p>I think I can also use something like <code>try_core (to_expr ``(%%e %%f))</code>.</p>

#### [ Simon Hudon (Apr 25 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125650448):
<p>Yes I think that's right. It might be slower because your going from <code>expr</code> to <code>pexpr</code> and back.</p>

#### [ Simon Hudon (Apr 25 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125650508):
<p>Depending on what you do with the expressions after, you might be able to do better than my proposal. Whatever you do with the resulting expression might need to be type checked again so you could just return <code>a b</code> with the understanding that it might eventually fail to type check</p>

#### [ Mario Carneiro (Apr 25 2018 at 04:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125651850):
<p>How did you get <code>a</code> in your application <code>a b</code>? Lean works at the application list level (i.e. <code>f a1 a2 ... an</code>) when it does implicits and such</p>

#### [ Mario Carneiro (Apr 25 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125652123):
<p>I think the fastest option is to whnf the type of a to a Pi type, get its binding domain, and then <code>unify</code> it with the type of <code>b \in A</code> for each <code>b</code>. That way you minimize the amount for repeated work for failures and don't have to check more than you need to (<code>type_check</code> will go through the whole term)</p>

#### [ Simon Hudon (Apr 25 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125652179):
<p>Interesting! So option 1). I went the other way because I think this work will have to be done by the type checker and since that's done in C++, I would think it would be faster than anything you'd come up with.</p>

#### [ Mario Carneiro (Apr 25 2018 at 04:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125652189):
<p><code>type_check</code> is never done in C++, it's only for debugging</p>

#### [ Mario Carneiro (Apr 25 2018 at 04:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125652192):
<p>it's all incremental in the C++ stuff</p>

#### [ Mario Carneiro (Apr 25 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125652235):
<p>In scott's case the <code>a</code> is constant but the <code>b</code> changes, so it makes sense to precompute it</p>

#### [ Simon Hudon (Apr 25 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125652241):
<p>Good point</p>

#### [ Mario Carneiro (Apr 25 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125652253):
<p>I'm guessing that Scott is building a search algorithm that just strings everything together that's well typed (trying to prove the five lemma maybe?) and for that this will be a really hot path so quick failure is important</p>

#### [ Mario Carneiro (Apr 25 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125652352):
<p>Option 2 would possibly have worked, but it's not type correct as scott points out and there's no immediate fix, lean isn't optimized for this kind of checking</p>

#### [ Scott Morrison (Apr 25 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125665542):
<p>I'm going to defer trying <span class="user-mention" data-user-id="110049">@Mario Carneiro</span>'s suggested fastest option, as I'm not confident playing with binding domains yet.</p>

#### [ Scott Morrison (Apr 25 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125665550):
<p>In the meantime, it seems that when I try <code>to_expr ``(%%e %%f)</code>, Lean doesn't manage to fill in implicit arguments.</p>

#### [ Scott Morrison (Apr 25 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125665598):
<p>Is this expected? Is there a good way to do this? I'll try to come up with a MWE now.</p>

#### [ Scott Morrison (Apr 25 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125666920):
<p>It seems that the problem is that <code>to_expr ``(%%e %%f)</code> is over-eager about implicit arguments.</p>

#### [ Scott Morrison (Apr 25 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125666928):
<p>Say <code>e</code> represented something with a explicit argument then an implicit argument.</p>

#### [ Scott Morrison (Apr 25 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125666937):
<p>Then <code>to_expr ``(%%e %%f)</code> produces not <code>e f</code> but <code>e f ?m_1</code>.</p>

#### [ Scott Morrison (Apr 25 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125667061):
<div class="codehilite"><pre><span></span><span class="kn">axiom</span> <span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Type</span>
<span class="n">def</span> <span class="n">g</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">{</span><span class="n">k</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">f</span> <span class="n">k</span><span class="o">)</span> <span class="o">:=</span> <span class="n">n</span>

<span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">implicit</span> <span class="n">true</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">do</span> <span class="n">e</span> <span class="err">←</span> <span class="n">to_expr</span> <span class="bp">```</span><span class="o">(</span><span class="n">g</span><span class="o">),</span>
     <span class="n">f</span> <span class="err">←</span> <span class="n">to_expr</span> <span class="bp">```</span><span class="o">(</span><span class="mi">57</span><span class="o">),</span>
     <span class="n">to_expr</span> <span class="bp">```</span><span class="o">(</span><span class="err">%%</span><span class="n">e</span> <span class="err">%%</span><span class="n">f</span><span class="o">)</span> <span class="bp">&gt;&gt;=</span> <span class="n">pp</span> <span class="bp">&gt;&gt;=</span> <span class="n">trace</span>
<span class="kn">end</span>
</pre></div>

#### [ Scott Morrison (Apr 25 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125667066):
<p>produces <code>@g 57 ?m_1</code></p>

#### [ Scott Morrison (Apr 25 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125667074):
<p>But I'd really like it to just produce <code>g 57</code>.</p>

#### [ Scott Morrison (Apr 25 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125667526):
<p>Hmm... I think this one is above my pay-grade for now. If anyone would like to help write a </p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">apps</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">expr</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">list</span> <span class="n">expr</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="o">(</span><span class="n">list</span> <span class="n">expr</span><span class="o">)</span> <span class="o">:=</span>
</pre></div>


<p>that actually works (i.e. return a list of all ways to plug in an <code>f ∈ F</code> as the next explicit argument of <code>e</code>) that would be wonderful.</p>

#### [ Scott Morrison (Apr 25 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125667530):
<p>My current implementation is <br>
<code>do l ← F.mmap $ λ f, (do r ← try_core (to_expr ```(%%e %%f)), return r.to_list), return l.join</code></p>

#### [ Scott Morrison (Apr 25 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125667550):
<p>But that suffers from the problem explained above. Mario suggested to me that I first inspect <code>e</code>, find the first explicit binder in it, and try to unify it with each element of <code>F</code>.</p>

#### [ Scott Morrison (Apr 25 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125667610):
<p>Unfortunately I don't know what I'm meant to do with any earlier implicit binders I find before the first explicit one, or how they would end up getting assigned by unification.</p>

#### [ Simon Hudon (Apr 25 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125671135):
<p>When you encounter implicit binders, create a meta variable and use it as a parameter.</p>

#### [ Scott Morrison (Apr 25 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125671191):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> do you know of examples of this I can look at? I got pretty confused dealing with binders. :-(</p>

#### [ Simon Hudon (Apr 25 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125671468):
<p>Sure, have a look at <a href="https://github.com/leanprover/mathlib/blob/master/tactic/basic.lean#L100-L105" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/tactic/basic.lean#L100-L105">https://github.com/leanprover/mathlib/blob/master/tactic/basic.lean#L100-L105</a></p>

#### [ Scott Morrison (Apr 25 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125672334):
<p>Okay, that's helpful. Do you know if there is any existing code  that instead of just producing <code>expr.app e f</code>, produces <code>e</code>, with <code>f</code> stuck into the first explicit argument of <code>e</code> (and any earlier implicit arguments filled)?</p>

#### [ Simon Hudon (Apr 25 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125672812):
<p>I'm sure I have something like that around. Let's see ...</p>

#### [ Simon Hudon (Apr 25 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125673275):
<p>Actually, I can't find exactly that but let me sketch something for you</p>

#### [ Scott Morrison (Apr 25 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125673562):
<p>Thank you! I better go to sleep now, but I'll look forward to seeing your answer when I'm back.</p>

#### [ Simon Hudon (Apr 25 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125673600):
<p>Hopefully, this catches you before sleep does:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">mk_app_aux</span> <span class="o">:</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">tactic</span> <span class="n">expr</span>
 <span class="bp">|</span> <span class="n">f</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">pi</span> <span class="n">n</span> <span class="n">binder_info</span><span class="bp">.</span><span class="n">default</span> <span class="n">d</span> <span class="n">b</span><span class="o">)</span> <span class="n">arg</span> <span class="o">:=</span> <span class="n">do</span>
   <span class="n">infer_type</span> <span class="n">arg</span> <span class="bp">&gt;&gt;=</span> <span class="n">unify</span> <span class="n">d</span><span class="o">,</span>
   <span class="n">return</span> <span class="err">$</span> <span class="n">f</span> <span class="n">arg</span>
 <span class="bp">|</span> <span class="n">f</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">pi</span> <span class="n">n</span> <span class="bp">_</span> <span class="n">d</span> <span class="n">b</span><span class="o">)</span> <span class="n">arg</span> <span class="o">:=</span> <span class="n">do</span>
   <span class="n">v</span> <span class="err">←</span> <span class="n">mk_meta_var</span> <span class="n">d</span><span class="o">,</span>
   <span class="n">t</span> <span class="err">←</span> <span class="n">whnf</span> <span class="o">(</span><span class="n">b</span><span class="bp">.</span><span class="n">instantiate_var</span> <span class="n">v</span><span class="o">),</span>
   <span class="n">mk_app_aux</span> <span class="o">(</span><span class="n">f</span> <span class="n">v</span><span class="o">)</span> <span class="n">t</span> <span class="n">arg</span>
 <span class="bp">|</span> <span class="n">e</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">return</span> <span class="n">e</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">mk_app&#39;</span> <span class="o">(</span><span class="n">f</span> <span class="n">arg</span> <span class="o">:</span> <span class="n">expr</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">expr</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">t</span> <span class="err">←</span> <span class="n">infer_type</span> <span class="n">f</span> <span class="bp">&gt;&gt;=</span> <span class="n">whnf</span><span class="o">,</span>
   <span class="n">mk_app_aux</span> <span class="n">f</span> <span class="n">t</span> <span class="n">arg</span>
</pre></div>

#### [ Scott Morrison (Apr 25 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125674417):
<p>Perfect.</p>

#### [ Scott Morrison (Apr 25 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125674504):
<p>(I changed <code>| e _ _ := return e</code> to <code>| e _ _ := failed</code>)</p>


{% endraw %}
