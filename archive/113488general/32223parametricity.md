---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/32223parametricity.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [parametricity](https://leanprover-community.github.io/archive/113488general/32223parametricity.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Cyril Cohen (Nov 11 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147487744):
<p>Hi, <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <span class="user-mention" data-user-id="110596">@Rob Lewis</span>,<br>
I am debugging my -- very buggy -- parametricity plugin. Could you tell me the shortest way to get the name of an inductive type from the name of its recursor? (I found <code>environment.inductive_type_of</code> to get it from the name of a constructor, but I cannot find the same for the recursor, and taking just the namespace sounds dirty to me...)</p>

#### [ Johannes Hölzl (Nov 11 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147488000):
<p>Hm, it looks like there is no other (easy) option. You can analyse the type of the recursor, and try to get the inductive type from this, but this is not easy: there is an arbitrary number of parameters, I guess you need to analyse the motive to figure out what is a parameter and what is the actual inductive value...</p>

#### [ Mario Carneiro (Nov 11 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147491817):
<p>For an arbitrary recursor accepted by <code>induction</code>, the type is a bunch of pis followed by <code>C a1 ... an</code> where <code>C</code> is a variable in the context. The type of this variable is a bunch of pis ending in <code>Type</code> or <code>Prop</code>, and the last argument should have the type <code>T b1 ... bn</code> where <code>T</code> is the type in question</p>

#### [ Mario Carneiro (Nov 11 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147491835):
<p>But if you know it's a builtin recursor the easiest way is just to knock off the last segment from the name</p>

#### [ Mario Carneiro (Nov 11 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147491970):
<p>Oh wait, that doesn't work for the nondependent recursors. I think you can always look at the last pi in the type, which will have type <code>T b1 ... bn</code></p>

#### [ Mario Carneiro (Nov 11 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492002):
<p>for example:</p>
<div class="codehilite"><pre><span></span>inductive T (α : Type) : Type → Prop
| mk1 : T nat
| mk2 : T α

#print T.rec
-- protected eliminator T.rec : ∀ {α : Type} {C : Type → Prop},
-- C ℕ → C α → ∀ {a : Type}, T α a → C a
#check @T.drec
-- T.drec : ∀ {α : Type} {C : Π (a : Type), T α a → Prop},
-- C ℕ _ → C α _ → ∀ {a : Type} (n : T α a), C a n
</pre></div>


<p>Note that the last pi in the type has <code>T α a</code> as its domain, where <code>T</code> is what you want</p>

#### [ Cyril Cohen (Nov 11 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492061):
<p>Sure I know where to get the the type of the inductive from the type of the recursor, but I was looking for a primitive that I think is missing from the API... What does not work for nondependent recursors?</p>

#### [ Mario Carneiro (Nov 11 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492067):
<p>I think if we can figure it out there is no need for an API function</p>

#### [ Mario Carneiro (Nov 11 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492068):
<p>we can add it to mathlib</p>

#### [ Cyril Cohen (Nov 11 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492136):
<p>an API function would always be more efficient than retro-engineering... since the recursor is generated when the inductive type is added it should be indexed in the same way the constructors are...</p>

#### [ Mario Carneiro (Nov 11 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492146):
<p>the API function would do what I just said, this information is not stored</p>

#### [ Cyril Cohen (Nov 11 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492191):
<p>at least it would be coded in C++... meh I guess for my use case efficiency does not matter, but it's a matter of uniformity</p>

#### [ Cyril Cohen (Nov 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492196):
<p>anyway, take the number of parameters + 1 pis out, then take the next pi, take its head symbol, done</p>

#### [ Mario Carneiro (Nov 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492199):
<p>sure but you could say that about anything</p>

#### [ Cyril Cohen (Nov 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492201):
<p>oh + the number of constructors</p>

#### [ Mario Carneiro (Nov 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492203):
<p>well you can't get the constructors until you know the type...</p>

#### [ Cyril Cohen (Nov 11 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492244):
<p>oh right... so last pi then</p>

#### [ Mario Carneiro (Nov 11 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492249):
<p>right</p>

#### [ Cyril Cohen (Nov 11 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492324):
<blockquote>
<p>sure but you could say that about anything</p>
</blockquote>
<p>Since the API function is there for constructors, it should also be there for anything that is generated by adding an inductive, such as recursors. I think none or both should be part of the core api, that is all I am saying.</p>

#### [ Mario Carneiro (Nov 11 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492390):
<p>I think that's reasonable, but, well, core is frozen</p>

#### [ Cyril Cohen (Nov 11 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147492486):
<p>Oh right, I forgot about that, sorry for the noise <span class="emoji emoji-1f914" title="thinking">:thinking:</span></p>

#### [ Cyril Cohen (Nov 11 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147493073):
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">environment</span><span class="bp">.</span><span class="n">trailing_pi_type_of</span> <span class="o">(</span><span class="n">env</span> <span class="o">:</span> <span class="n">environment</span><span class="o">)</span> <span class="o">:</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">name</span>
 <span class="bp">|</span> <span class="o">(</span><span class="n">pi</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">t</span> <span class="n">b</span><span class="o">)</span> <span class="o">:=</span> <span class="k">match</span> <span class="n">b</span> <span class="k">with</span>
   <span class="bp">|</span> <span class="o">(</span><span class="n">pi</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">environment</span><span class="bp">.</span><span class="n">trailing_pi_type_of</span> <span class="n">b</span>
   <span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">some</span> <span class="n">t</span><span class="bp">.</span><span class="n">get_app_fn</span><span class="bp">.</span><span class="n">const_name</span>
   <span class="kn">end</span>
 <span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">none</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">environment</span><span class="bp">.</span><span class="n">inductive_type_of_rec</span> <span class="o">(</span><span class="n">env</span> <span class="o">:</span> <span class="n">environment</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">name</span><span class="o">)</span> <span class="o">:</span> <span class="n">exceptional</span> <span class="n">name</span> <span class="o">:=</span> <span class="n">do</span>
  <span class="n">decl</span> <span class="err">←</span> <span class="n">env</span><span class="bp">.</span><span class="n">get</span> <span class="n">n</span><span class="o">,</span>
  <span class="k">match</span> <span class="n">env</span><span class="bp">.</span><span class="n">trailing_pi_type_of</span> <span class="n">decl</span><span class="bp">.</span><span class="n">type</span> <span class="k">with</span>
  <span class="bp">|</span> <span class="n">some</span> <span class="n">i</span> <span class="o">:=</span> <span class="n">return</span> <span class="n">i</span>
  <span class="bp">|</span> <span class="n">none</span> <span class="o">:=</span> <span class="n">exceptional</span><span class="bp">.</span><span class="n">fail</span> <span class="err">$</span> <span class="s2">&quot;inductive_type_of_rec: not a recursor &quot;</span> <span class="bp">++</span> <span class="n">to_string</span> <span class="n">n</span>
  <span class="kn">end</span>
</pre></div>

#### [ Cyril Cohen (Nov 11 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147493139):
<p>or  for the second one:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">environment</span><span class="bp">.</span><span class="n">inductive_type_of_rec</span> <span class="o">(</span><span class="n">env</span> <span class="o">:</span> <span class="n">environment</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">name</span><span class="o">)</span> <span class="o">:</span> <span class="n">option</span> <span class="n">name</span> <span class="o">:=</span>
  <span class="k">match</span> <span class="n">env</span><span class="bp">.</span><span class="n">get</span> <span class="n">n</span> <span class="k">with</span>
  <span class="bp">|</span> <span class="o">(</span><span class="n">exceptional</span><span class="bp">.</span><span class="n">success</span> <span class="n">decl</span><span class="o">)</span> <span class="o">:=</span> <span class="n">env</span><span class="bp">.</span><span class="n">trailing_pi_type_of</span> <span class="n">decl</span><span class="bp">.</span><span class="n">type</span>
  <span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">none</span>
  <span class="kn">end</span>
</pre></div>

#### [ Cyril Cohen (Nov 12 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147494991):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> <span class="user-mention" data-user-id="110596">@Rob Lewis</span> I am confused by the output of <code>#print has_zero.zero</code> i.e. </p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">has_zero</span><span class="bp">.</span><span class="n">zero</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">c</span> <span class="o">:</span> <span class="n">has_zero</span> <span class="n">α</span><span class="o">],</span> <span class="n">α</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">c</span> <span class="o">:</span> <span class="n">has_zero</span> <span class="n">α</span><span class="o">],</span> <span class="o">[</span><span class="n">has_zero</span><span class="bp">.</span><span class="n">zero</span> <span class="n">c</span><span class="o">]</span>
</pre></div>


<p>what construction is <code>[has_zero.zero c]</code> internally? I figured it is a "macro", but I cannot find its API... is it possible to get its expansion?</p>

#### [ Johannes Hölzl (Nov 12 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147495052):
<p>its a projection. so the projection data you get out of <code>environment</code> should tell you what the inductive is and which position of the constructor it is from. The macro hides a application of the recursor.</p>

#### [ Cyril Cohen (Nov 12 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parametricity/near/147496075):
<p>Nevermind, I was looking for <code>environment.unfold_all_macros</code></p>


{% endraw %}
