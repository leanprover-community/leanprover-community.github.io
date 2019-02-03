---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85762equationcompiler.html
---

## Stream: [general](index.html)
### Topic: [equation compiler](85762equationcompiler.html)

---


{% raw %}
#### [ Minchao Wu (Jul 24 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130222550):
<p>Hi friends, is there a way to fill up this underscore?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">foo</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span> <span class="n">nat</span> <span class="o">:=</span>
<span class="k">match</span> <span class="n">n</span> <span class="k">with</span>
<span class="bp">|</span> <span class="mi">0</span>     <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="n">k</span>     <span class="o">:=</span> <span class="k">have</span> <span class="n">k</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">,</span> <span class="k">from</span> <span class="bp">_</span><span class="o">,</span>
           <span class="mi">0</span>
<span class="kn">end</span>
</pre></div>


<p>Usually <code>n</code> is of some complicated inductive types, but I really just need to handle one specific constructor. For all the other constructors the proofs are long but exactly the same.  <br>
I could use <code>rec</code> or <code>cases</code> or <code>if then else</code> but that would be awkward. So I am wondering how I can refer to the facts that the equation compiler knows but are not listed as hypotheses?</p>

#### [ Kenny Lau (Jul 24 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130222560):
<p>use k+1 instead of k</p>

#### [ Minchao Wu (Jul 24 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130222573):
<p>that works in the case of nat but not other complicated inductive types</p>

#### [ Kenny Lau (Jul 24 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130222582):
<p>then you can't</p>

#### [ Minchao Wu (Jul 24 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130222696):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">bar</span> <span class="o">:</span> <span class="n">bool</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="n">tt</span>     <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="n">b</span>     <span class="o">:=</span> <span class="k">have</span> <span class="n">b</span> <span class="bp">≠</span> <span class="n">tt</span><span class="o">,</span> <span class="k">from</span> <span class="bp">_</span><span class="o">,</span> <span class="mi">1</span>
</pre></div>


<p>well maybe this one is a better toy example</p>

#### [ Kenny Lau (Jul 24 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130222747):
<p>you can't.</p>

#### [ Minchao Wu (Jul 24 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130222758):
<p>reason?</p>

#### [ Kenny Lau (Jul 24 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130222768):
<p>in that environment you do not know that b is not tt</p>

#### [ Kenny Lau (Jul 24 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130222788):
<p>also how do you use <code>rec</code> or <code>cases</code>?</p>

#### [ Minchao Wu (Jul 24 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130222792):
<p>but the equation compiler knows that if it's tt then the thing is not exhaustive</p>

#### [ Kenny Lau (Jul 24 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130222798):
<p>the <code>b</code> is a catch-all clause</p>

#### [ Kenny Lau (Jul 24 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130222801):
<p>it is intended to match everything</p>

#### [ Minchao Wu (Jul 24 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130222804):
<p>that's true</p>

#### [ Minchao Wu (Jul 24 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130222864):
<p>I am saying that the compiler knows that tt will never be matched by b</p>

#### [ Kenny Lau (Jul 24 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130222869):
<p>but that's already outside your environment</p>

#### [ Minchao Wu (Jul 24 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130222890):
<p>perhaps, so I am asking if there is a clever hack</p>

#### [ Kenny Lau (Jul 24 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130222892):
<p>what was your idea with <code>rec</code> and <code>cases</code>?</p>

#### [ Minchao Wu (Jul 24 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130222941):
<blockquote>
<p>also how do you use <code>rec</code> or <code>cases</code>?</p>
</blockquote>
<p>you just don't use <code>match</code></p>

#### [ Kenny Lau (Jul 24 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130222950):
<blockquote>
<p>that works in the case of nat but not other complicated inductive types</p>
</blockquote>
<p>does using <code>rec</code> solve this problem?</p>

#### [ Minchao Wu (Jul 24 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130222965):
<p>it's the same as your suggestion of using <code>(k+1)</code></p>

#### [ Minchao Wu (Jul 24 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130222983):
<p>namely explicitly writing down all the constructors</p>

#### [ Simon Hudon (Jul 24 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130224157):
<p>What you could do is:</p>
<div class="codehilite"><pre><span></span>begin
  cases n,
  case 0 :
  { /- proof -/ },
  all_goals { /- proof -/ },
end
</pre></div>

#### [ Kenny Lau (Jul 24 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130224169):
<p>but how are you going to prove n != 0?</p>

#### [ Johan Commelin (Jul 24 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130224343):
<p>I think that you don't have to.</p>

#### [ Johan Commelin (Jul 24 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130224351):
<p>That is Simon's trick.</p>

#### [ Johan Commelin (Jul 24 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130224422):
<p>You just prove it case by case, for all cases. But then, you prove all but one case with a single proof.</p>

#### [ Minchao Wu (Jul 24 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130224489):
<p>I forgot to mention that foll all the other cases I need the fact that n!=0</p>

#### [ Minchao Wu (Jul 24 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130224536):
<p>but this trick might work</p>

#### [ Johan Commelin (Jul 24 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130224585):
<p>Right, so now you somehow need to know that fact, but now it should be even true in your environment (I hope).</p>

#### [ Simon Hudon (Jul 24 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130224590):
<p>Off the top of my head, <code>cases h : n</code> will preserve the variable n and you can do your proof with <code>subst n</code> and <code>contradiction</code></p>

#### [ Simon Hudon (Jul 24 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130225161):
<p>concretely, here is how I do it:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">foo</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span> <span class="n">nat</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">h</span> <span class="o">:</span> <span class="n">n</span><span class="o">,</span>
  <span class="n">case</span> <span class="n">nat</span><span class="bp">.</span><span class="n">zero</span> <span class="o">:</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="mi">0</span> <span class="o">},</span>
  <span class="n">all_goals</span>
  <span class="o">{</span> <span class="k">have</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">subst</span> <span class="n">n</span><span class="o">,</span> <span class="n">contradiction</span> <span class="o">},</span>
    <span class="n">exact</span> <span class="n">n</span> <span class="o">},</span>
<span class="kn">end</span>
</pre></div>

#### [ Simon Hudon (Jul 24 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130225220):
<p>(deleted)</p>

#### [ Minchao Wu (Jul 24 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130225363):
<p>when you use <code>cases 0:</code> to handle the specific constructor, how do you supply the arguments to that constructor?</p>

#### [ Minchao Wu (Jul 24 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130225389):
<p>in the case of nat there is no parameters</p>

#### [ Simon Hudon (Jul 24 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130225432):
<p>(note that it's <code>case nat.zero :</code>, no s, and full constructor name)</p>

#### [ Simon Hudon (Jul 24 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130225455):
<p>if we were looking at a list for instance, it would be <code>case list.cons : x xs { /- my proof -/ }</code></p>

#### [ Minchao Wu (Jul 24 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130226138):
<p>Very cool, it worked</p>

#### [ Minchao Wu (Jul 24 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130226143):
<p>Thanks!</p>

#### [ Minchao Wu (Jul 24 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130226210):
<p>I wasn't aware of the <code>case</code> tatic</p>

#### [ Simon Hudon (Jul 24 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130226238):
<p>The more you know <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Minchao Wu (Jul 24 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130226248):
<p>I'm going to embrace it from now on :)</p>

#### [ Nicholas Scheel (Jul 25 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler/near/130244135):
<p>(deleted)</p>


{% endraw %}
