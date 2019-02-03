---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/86943recfnmacro.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [rec_fn_macro](https://leanprover-community.github.io/archive/113488general/86943recfnmacro.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Ben Sherman (May 21 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126885006):
<p>I just updated Lean from 3.3.0 to 3.4.1, and now when I write this code:</p>
<div class="codehilite"><pre><span></span>axiom R : Type

inductive Sampler : Type
| Ret : Sampler
| BindUniform : (R → Sampler) → Sampler

def Bind : Sampler → (ℕ → Sampler) → Sampler
| Sampler.Ret f := f 0
| (Sampler.BindUniform k) f := Sampler.BindUniform (λ x, Bind (k x) f)
</pre></div>


<p>I get the error <code>rec_fn_macro only allowed in meta definitions</code> in the definition of <code>Bind</code>. Is this a bug? Should I submit it as a Github issue? Or do I just not understand what's going on?</p>

#### [ Andrew Ashworth (May 21 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126886035):
<p>whether or not it's a bug, lean 3.4.1 is the last release in the 3xx series and only critical issues are going to be fixed</p>

#### [ Andrew Ashworth (May 21 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126886556):
<p>if you change out <code>axiom R</code> for <code>variable R</code> do you get a more educational error message?</p>

#### [ Andrew Ashworth (May 21 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126886865):
<p>This is some kind of universe problem, I bet</p>

#### [ Andrew Ashworth (May 21 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126887061):
<p>maybe not. I just pasted it into my vscode and replaced <code>axiom R</code> with <code>variable R</code>. If you <code>#print</code> Sampler you get that the Sampler type is <code>Type u -&gt; Type u</code>. Your definition is type incorrect. Now I'm confused why it ever worked in <code>3.3.0</code>...</p>

#### [ Andrew Ashworth (May 21 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126887150):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">Sampler</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u₁</span>
<span class="n">constructors</span><span class="o">:</span>
<span class="n">Sampler</span><span class="bp">.</span><span class="n">Ret</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">),</span> <span class="n">Sampler</span> <span class="n">R</span>
<span class="n">Sampler</span><span class="bp">.</span><span class="n">BindUniform</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">},</span> <span class="o">(</span><span class="n">R</span> <span class="bp">→</span> <span class="n">Sampler</span> <span class="n">R</span><span class="o">)</span> <span class="bp">→</span> <span class="n">Sampler</span> <span class="n">R</span>
</pre></div>

#### [ Andrew Ashworth (May 21 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126887244):
<p>huh, interesting. The definition is correct if you use <code>axiom</code>...</p>

#### [ Kevin Buzzard (May 21 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888047):
<p>I guess a variable is something which, if mentioned in a definition, secretly appends itself as a "forall R : type" in front of definitions</p>

#### [ Ben Sherman (May 21 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888052):
<p>Yeah, if I switch to using a <code>variable</code> or a <code>parameter</code> in a section, the definition goes through fine. And I don't think <code>Sampler</code> becomes universe-polymorphic in any case</p>

#### [ Kevin Buzzard (May 21 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888067):
<p>whereas perhaps with an axiom this does not happen.</p>

#### [ Kevin Buzzard (May 21 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888086):
<p>But isn't the error with <code>Bind</code> simply because Lean can't prove that the definition "terminates"?</p>

#### [ Kevin Buzzard (May 21 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888148):
<p>cf the meta def of that 91 function in Programming In Lean, where the definition is OK but this is too hard for Lean to spot so you have to make it meta</p>

#### [ Kevin Buzzard (May 21 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888224):
<div class="codehilite"><pre><span></span><span class="kn">axiom</span> <span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="kn">variable</span> <span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span>

<span class="kn">theorem</span> <span class="n">X</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">=</span> <span class="n">R</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="kn">theorem</span> <span class="n">Y</span> <span class="o">:</span> <span class="n">S</span> <span class="bp">=</span> <span class="n">S</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="bp">#</span><span class="kn">check</span> <span class="n">X</span> <span class="c1">-- R = R</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">Y</span> <span class="c1">-- ∀ (S : Type), S = S</span>
</pre></div>

#### [ Kevin Buzzard (May 21 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888301):
<p>The axiom makes a new constant, like <code>quotient.sound</code> or whatever -- when you mention quotient.sound you don't get random "forall quotient.sound" hypotheses appearing in theorems</p>

#### [ Kevin Buzzard (May 21 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888317):
<p>but the variable gets inserted. I guess you guys both know this.</p>

#### [ Ben Sherman (May 21 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888389):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> No,  this is actually a primitive recursive definition:</p>
<div class="codehilite"><pre><span></span>protected eliminator Sampler.rec : Π {real : Type} {C : Sampler real → Sort l},
  C (Sampler.Ret real) →
  (Π (a : real → Sampler real), (Π (a_1 : real), C (a a_1)) → C (Sampler.BindUniform a)) →
  Π (n : Sampler real), C n
</pre></div>


<p>Notice how the inductive hypothesis allows you to apply the continuation to any argument.</p>

#### [ Kevin Buzzard (May 21 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888423):
<p>I am suggesting that your definition of Bind relies on evaluating Bind elsewhere, does it not?</p>

#### [ Kevin Buzzard (May 21 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888487):
<p>And with the definition of nat, Lean can use some recursion principle to check that the definition is good.</p>

#### [ Kevin Buzzard (May 21 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888566):
<p>Presumably the error means "I find myself trying to prove that this definition of Bind has a decent recursor but I find myself trying to write some induction over functions, so I give up, make me meta so I don't have to worry about this sort of thing and can just be untrusted code"</p>

#### [ Kevin Buzzard (May 21 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888576):
<p>heh</p>

#### [ Kevin Buzzard (May 21 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888586):
<p>making the definition of Bind meta doesn't make the error go away :-)</p>

#### [ Ben Sherman (May 21 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126888735):
<p>So the definition works if I apply the recursor directly:</p>
<div class="codehilite"><pre><span></span>axiom real : Type

inductive Sampler : Type
| Ret : Sampler
| BindUniform : (real → Sampler) → Sampler

def Bind (x : Sampler) : (ℕ → Sampler) → Sampler
:= @Sampler.rec_on (λ _, (ℕ → Sampler) → Sampler) x
     (λ f, f 0)
     (λ k ih f, Sampler.BindUniform (λ x, ih x f))
</pre></div>


<p>So, even though the definition is primitive recursive, it does look to be something to do with it failing in figuring out the recursion scheme.</p>

#### [ Kevin Buzzard (May 21 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126889923):
<p>I am really confused by that recursor</p>

#### [ Kevin Buzzard (May 21 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126889945):
<p><code>(Π (a_1 : R), C (a a_1))</code></p>

#### [ Kevin Buzzard (May 21 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890135):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">Sampler</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">Ret</span> <span class="o">:</span> <span class="n">Sampler</span>
<span class="bp">|</span> <span class="n">BindUniform</span> <span class="o">:</span> <span class="o">(</span><span class="bp">ℤ</span> <span class="bp">→</span> <span class="n">Sampler</span><span class="o">)</span> <span class="bp">→</span> <span class="n">Sampler</span>



<span class="n">def</span> <span class="n">Bind</span> <span class="o">:</span> <span class="n">Sampler</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">Sampler</span><span class="o">)</span> <span class="bp">→</span> <span class="n">Sampler</span>
<span class="bp">|</span> <span class="n">Sampler</span><span class="bp">.</span><span class="n">Ret</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">f</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">Sampler</span><span class="bp">.</span><span class="n">BindUniform</span> <span class="n">k</span><span class="o">)</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">Sampler</span><span class="bp">.</span><span class="n">BindUniform</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">Bind</span> <span class="o">(</span><span class="n">k</span> <span class="n">x</span><span class="o">)</span> <span class="n">f</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (May 21 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890137):
<p>That works fine</p>

#### [ Kevin Buzzard (May 21 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890155):
<p>replacing the constant with an explicit type</p>

#### [ Kevin Buzzard (May 21 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890565):
<p>The definition with rec_on looks a bit funny to me -- k doesn't seem to play a role</p>

#### [ Kevin Buzzard (May 21 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890599):
<p>oh I see</p>

#### [ Kevin Buzzard (May 21 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890616):
<p><code>ih x</code> is <code>Bind (k x)</code></p>

#### [ Kevin Buzzard (May 21 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890620):
<p>that's the role of <code>ih</code></p>

#### [ Ben Sherman (May 21 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890770):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Yes, exactly!</p>

#### [ Kevin Buzzard (May 21 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890773):
<p>so I finally understand the question :-)</p>

#### [ Kevin Buzzard (May 21 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890852):
<p>so it is a bit weird that it will work for a concrete type like the integers but won't work for the constant, or at least it's weird to me</p>

#### [ Ben Sherman (May 21 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890872):
<p>Right, and if you change from <code>axiom</code> to <code>parameter</code> or <code>variable</code>, it works again. So I'm thinking it's a bug.</p>

#### [ Kevin Buzzard (May 21 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890895):
<p>well, with variable you change the type</p>

#### [ Kevin Buzzard (May 21 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/126890900):
<p>so you have to fiddle with everything</p>

#### [ Ben Sherman (Nov 08 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/147271354):
<p>I'm having another issue with rec_fn_macro: I've reduced it to this bug this time:</p>
<div class="codehilite"><pre><span></span>import analysis.real
def foo : bool → list ℝ
| tt := list.nil
| ff := 1/2 :: foo tt
</pre></div>


<p>I get the error:</p>
<div class="codehilite"><pre><span></span>equation compiler failed to generate bytecode for &#39;foo._main&#39;
nested exception message:
code generation failed, VM does not have code for &#39;real.division_ring&#39;
</pre></div>


<p>If I try to mark <code>foo</code> as <code>noncomputable</code>, I instead get an error about a failure to prove the recursion well-founded.<br>
Does anyone have any idea for how to get around this issue?<br>
In my actual code, I'm getting a <code>rec_fn_macro</code> issue that appears nonlocally - it's failing for a definition that calls some other function <code>bar</code> that involves division on ℝ. If I redefine <code>bar</code> as <code>sorry</code>, there is no longer any issue. But it doesn't even help for me to mark <code>bar</code> as <code>irreducible</code>.</p>

#### [ Mario Carneiro (Nov 08 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/147271582):
<p>I don't see the issue. This is certainly <code>noncomputable</code>, and that's the error you get if you don't mark it so. And it is failing to prove the recursion is well founded because the default well founded instance on bool has tt and ff incomparable, so you can't do any recursion.</p>

#### [ Mario Carneiro (Nov 08 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/147271643):
<p>perhaps you have oversimplified your example?</p>

#### [ Ben Sherman (Nov 08 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_fn_macro/near/147271849):
<p>Thanks! I didn't know that details about the well-foundedness. Then I indeed oversimplified my example - originally it was nat. Let me backtrack with a revised example.</p>


{% endraw %}
