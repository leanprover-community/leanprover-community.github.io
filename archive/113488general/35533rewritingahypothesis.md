---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/35533rewritingahypothesis.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [rewriting a hypothesis](https://leanprover-community.github.io/archive/113488general/35533rewritingahypothesis.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Apr 24 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125608657):
<p>This belongs in its own topic.<br>
(Originally <a href="#narrow/stream/113488-general/subject/statement.20of.20the.20five.20lemma/near/125607928" title="#narrow/stream/113488-general/subject/statement.20of.20the.20five.20lemma/near/125607928">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/statement.20of.20the.20five.20lemma/near/125607928</a>)</p>
<blockquote>
<p>Can I easily rewrite the hypothesis <code>(com₁ : m ∘ f = r ∘ l)</code> into <code>com₁' : \fo x, (m (f x) = r (l x))</code> ?</p>
</blockquote>

#### [ Sean Leather (Apr 24 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125608662):
<p>Did you try <code>unfold function.comp</code>?</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125608722):
<p>Wouldn't you need extensionality for it first?</p>

#### [ Sean Leather (Apr 24 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125608842):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">A</span> <span class="n">B</span> <span class="n">C</span> <span class="n">D</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">f₁</span> <span class="n">f₂</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">g₁</span> <span class="n">g₂</span> <span class="o">:</span> <span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="o">:</span> <span class="n">g₁</span> <span class="err">∘</span> <span class="n">f₁</span> <span class="bp">=</span> <span class="n">g₂</span> <span class="err">∘</span> <span class="n">f₂</span> <span class="o">:=</span>
  <span class="k">by</span> <span class="n">unfold</span> <span class="n">function</span><span class="bp">.</span><span class="n">comp</span><span class="bp">;</span> <span class="n">funext</span> <span class="n">x</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="n">A</span> <span class="n">B</span> <span class="n">C</span> <span class="n">D</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">,</span>
<span class="n">f₁</span> <span class="n">f₂</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">B</span><span class="o">,</span>
<span class="n">g₁</span> <span class="n">g₂</span> <span class="o">:</span> <span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">,</span>
<span class="n">x</span> <span class="o">:</span> <span class="n">A</span>
<span class="err">⊢</span> <span class="n">g₁</span> <span class="o">(</span><span class="n">f₁</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">g₂</span> <span class="o">(</span><span class="n">f₂</span> <span class="n">x</span><span class="o">)</span>
</pre></div>

#### [ Moses Schönfinkel (Apr 24 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125608848):
<p>Right, I am a moron :).</p>

#### [ Sean Leather (Apr 24 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125608893):
<p>Or you read from right to left. <span class="emoji emoji-1f643" title="upside down face">:upside_down_face:</span></p>

#### [ Moses Schönfinkel (Apr 24 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125608900):
<p>I think my fingers typed before my brain got involved.</p>

#### [ Sean Leather (Apr 24 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125608909):
<p>Actually, in my current version of Lean (dated to February, I think), <code>unfold</code> isn't necessary.</p>

#### [ Sean Leather (Apr 24 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125608912):
<div class="codehilite"><pre><span></span><span class="n">A</span> <span class="n">B</span> <span class="n">C</span> <span class="n">D</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">,</span>
<span class="n">f₁</span> <span class="n">f₂</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">B</span><span class="o">,</span>
<span class="n">g₁</span> <span class="n">g₂</span> <span class="o">:</span> <span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">,</span>
<span class="n">x</span> <span class="o">:</span> <span class="n">A</span>
<span class="err">⊢</span> <span class="o">(</span><span class="n">g₁</span> <span class="err">∘</span> <span class="n">f₁</span><span class="o">)</span> <span class="n">x</span> <span class="bp">=</span> <span class="o">(</span><span class="n">g₂</span> <span class="err">∘</span> <span class="n">f₂</span><span class="o">)</span> <span class="n">x</span>
</pre></div>

#### [ Sean Leather (Apr 24 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125608959):
<p>Okay, but that's not what you want. So I revoke my statement.</p>

#### [ Sean Leather (Apr 24 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125608982):
<p>And to alleviate <span class="user-mention" data-user-id="110027">@Moses Schönfinkel</span>'s concerns, you can do it the other way around:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">A</span> <span class="n">B</span> <span class="n">C</span> <span class="n">D</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">f₁</span> <span class="n">f₂</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">g₁</span> <span class="n">g₂</span> <span class="o">:</span> <span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="o">:</span> <span class="n">g₁</span> <span class="err">∘</span> <span class="n">f₁</span> <span class="bp">=</span> <span class="n">g₂</span> <span class="err">∘</span> <span class="n">f₂</span> <span class="o">:=</span>
  <span class="k">by</span> <span class="n">funext</span> <span class="n">x</span><span class="bp">;</span> <span class="n">unfold</span> <span class="n">function</span><span class="bp">.</span><span class="n">comp</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="n">A</span> <span class="n">B</span> <span class="n">C</span> <span class="n">D</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">,</span>
<span class="n">f₁</span> <span class="n">f₂</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">B</span><span class="o">,</span>
<span class="n">g₁</span> <span class="n">g₂</span> <span class="o">:</span> <span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">,</span>
<span class="n">x</span> <span class="o">:</span> <span class="n">A</span>
<span class="err">⊢</span> <span class="n">g₁</span> <span class="o">(</span><span class="n">f₁</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">g₂</span> <span class="o">(</span><span class="n">f₂</span> <span class="n">x</span><span class="o">)</span>
</pre></div>

#### [ Sean Leather (Apr 24 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125608989):
<p><span class="user-mention" data-user-id="110027">@Moses Schönfinkel</span> So you're not a moron after all.</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125609106):
<p>I am at least a partial moron because I thought extensionality needs to come before unfolding :). For some definition of "thought" which is just "don't think and fetch a pattern you'd encountered before".</p>

#### [ Johan Commelin (Apr 24 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125609543):
<p>Ok, so I unfolded that hypothesis. Now how do I apply it? Part of my (50-line) context is like this:</p>
<div class="codehilite"><pre><span></span>com₃ : (λ (x : C₁), m (h₁ x)) = λ (x : C₁), h₂ (l x),
x : C₁,
this : h₂ (l x) = 1
⊢ m (h₁ x) = 1
</pre></div>

#### [ Johan Commelin (Apr 24 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125609747):
<p>Why can't <code>cc</code> solve this one?</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125609789):
<p>I don't know anything about cc</p>

#### [ Johan Commelin (Apr 24 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125609790):
<p>Somehow it needs a slightly rewritten version of <code>com₃</code>, I guess</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125609793):
<p>but are you having trouble proving this in general?</p>

#### [ Johan Commelin (Apr 24 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125609794):
<p>Yup</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125609816):
<p>com3 says "two functions are equal"</p>

#### [ Johan Commelin (Apr 24 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125609818):
<p>AFAIK, <code>cc</code> follows it's nose, deducing equalities and occasionally applying some functions.</p>

#### [ Johan Commelin (Apr 24 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125609823):
<p>But that is simplistic</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125609826):
<p>I would be tempted to really use the functions themselves</p>

#### [ Johan Commelin (Apr 24 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125609827):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Right, so I need to do some funext</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125609833):
<p>I am sure I can give a hands-on proof</p>

#### [ Johan Commelin (Apr 24 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125609834):
<p>Or what</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125609879):
<p>You can write "show (m circ h1) x = 1" probably</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125609881):
<p>this will rewrite the goal</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125609886):
<p>because <code>show</code> will change a goal to something definitionally equivalent</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125609887):
<p>Do you know about definitional equivalence?</p>

#### [ Johan Commelin (Apr 24 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125609888):
<p>yes</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125609897):
<p>and you can use "change" to rewrite hypotheses to definitionally equivalent things too</p>

#### [ Sean Leather (Apr 24 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125609902):
<p>As well as <code>refine</code>.</p>

#### [ Johan Commelin (Apr 24 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125609906):
<p>Hmmz, ok</p>

#### [ Johan Commelin (Apr 24 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125609907):
<p>Let's see if I can find a proof</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125609910):
<p>Let me just get your context into some MWE</p>

#### [ Kenny Lau (Apr 24 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125609947):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> <code>exaxt (congr_fun com\3 _).trans this</code></p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610023):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">W</span> <span class="n">X</span> <span class="n">Y</span> <span class="n">Z</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">W</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Z</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">W</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">j</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">Z</span><span class="o">)</span> <span class="o">(</span><span class="n">w</span> <span class="o">:</span> <span class="n">W</span><span class="o">)</span> <span class="o">(</span><span class="n">one</span> <span class="o">:</span> <span class="n">Z</span><span class="o">)</span>
<span class="o">(</span><span class="n">Hcom</span> <span class="o">:</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">t</span><span class="o">,</span> <span class="n">g</span> <span class="o">(</span><span class="n">f</span> <span class="n">t</span><span class="o">))</span> <span class="bp">=</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">t</span><span class="o">,</span> <span class="n">j</span> <span class="o">(</span><span class="n">h</span> <span class="n">t</span><span class="o">)))</span> <span class="o">(</span><span class="n">Hthis</span> <span class="o">:</span> <span class="n">j</span> <span class="o">(</span><span class="n">h</span> <span class="n">w</span><span class="o">)</span> <span class="bp">=</span> <span class="n">one</span><span class="o">)</span> <span class="o">:</span> <span class="n">g</span> <span class="o">(</span><span class="n">f</span> <span class="n">w</span><span class="o">)</span> <span class="bp">=</span> <span class="n">one</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Apr 24 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610026):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> if you write your question like this (i.e. make it easily cut-and-pasteable)</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610029):
<p>then when Kenny goes into proof mode</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610066):
<p>he's more likely to print out more proofs</p>

#### [ Johan Commelin (Apr 24 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610069):
<p>Ok, I see</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610140):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">W</span> <span class="n">X</span> <span class="n">Y</span> <span class="n">Z</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">W</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Z</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">W</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">j</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">Z</span><span class="o">)</span> <span class="o">(</span><span class="n">w</span> <span class="o">:</span> <span class="n">W</span><span class="o">)</span> <span class="o">(</span><span class="n">one</span> <span class="o">:</span> <span class="n">Z</span><span class="o">)</span>
<span class="o">(</span><span class="n">Hcom</span> <span class="o">:</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">t</span><span class="o">,</span> <span class="n">g</span> <span class="o">(</span><span class="n">f</span> <span class="n">t</span><span class="o">))</span> <span class="bp">=</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">t</span><span class="o">,</span> <span class="n">j</span> <span class="o">(</span><span class="n">h</span> <span class="n">t</span><span class="o">)))</span> <span class="o">(</span><span class="n">Hthis</span> <span class="o">:</span> <span class="n">j</span> <span class="o">(</span><span class="n">h</span> <span class="n">w</span><span class="o">)</span> <span class="bp">=</span> <span class="n">one</span><span class="o">)</span> <span class="o">:</span> <span class="n">g</span> <span class="o">(</span><span class="n">f</span> <span class="n">w</span><span class="o">)</span> <span class="bp">=</span> <span class="n">one</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">change</span> <span class="o">(</span><span class="n">g</span> <span class="err">∘</span> <span class="n">f</span><span class="o">)</span> <span class="n">w</span> <span class="bp">=</span> <span class="n">one</span><span class="o">,</span>
<span class="n">change</span> <span class="o">(</span><span class="n">j</span> <span class="err">∘</span> <span class="n">h</span><span class="o">)</span> <span class="n">w</span> <span class="bp">=</span> <span class="n">one</span> <span class="n">at</span> <span class="n">Hthis</span><span class="o">,</span>
<span class="n">change</span> <span class="o">(</span><span class="n">g</span> <span class="err">∘</span> <span class="n">f</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">j</span> <span class="err">∘</span> <span class="n">h</span><span class="o">)</span> <span class="n">at</span> <span class="n">Hcom</span><span class="o">,</span>
<span class="n">rwa</span> <span class="n">Hcom</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 24 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610146):
<p>If you're not ready for Kenny's gobble-de-gook then there is how I would think about it</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610154):
<p><code>rwa</code> means <code>rewrite, and then note that the goal is an assumption so close it</code></p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610206):
<p>and <code>change</code> lets you change things to definitionally equivalent things</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610211):
<p>The problem with rewrite is that it will not change stuff to definitionally equivalent stuff</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610214):
<p>it has to already be exactly right</p>

#### [ Johan Commelin (Apr 24 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610290):
<p>Ok, got that. Thanks!</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610296):
<p>Here's Kenny's proof:</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610339):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">W</span> <span class="n">X</span> <span class="n">Y</span> <span class="n">Z</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">W</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Z</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">W</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">j</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">Z</span><span class="o">)</span> <span class="o">(</span><span class="n">w</span> <span class="o">:</span> <span class="n">W</span><span class="o">)</span> <span class="o">(</span><span class="n">one</span> <span class="o">:</span> <span class="n">Z</span><span class="o">)</span>
<span class="o">(</span><span class="n">Hcom</span> <span class="o">:</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">t</span><span class="o">,</span> <span class="n">g</span> <span class="o">(</span><span class="n">f</span> <span class="n">t</span><span class="o">))</span> <span class="bp">=</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">t</span><span class="o">,</span> <span class="n">j</span> <span class="o">(</span><span class="n">h</span> <span class="n">t</span><span class="o">)))</span> <span class="o">(</span><span class="n">Hthis</span> <span class="o">:</span> <span class="n">j</span> <span class="o">(</span><span class="n">h</span> <span class="n">w</span><span class="o">)</span> <span class="bp">=</span> <span class="n">one</span><span class="o">)</span> <span class="o">:</span> <span class="n">g</span> <span class="o">(</span><span class="n">f</span> <span class="n">w</span><span class="o">)</span> <span class="bp">=</span> <span class="n">one</span> <span class="o">:=</span>
<span class="o">((</span><span class="n">congr_fun</span> <span class="n">Hcom</span><span class="o">)</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">trans</span> <span class="n">Hthis</span>
</pre></div>

#### [ Patrick Massot (Apr 24 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610340):
<p>That's a nice example. I'm sure we can have a 23rd PR about simp vs rw vs change</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610341):
<p>This really shows the power of term mode</p>

#### [ Patrick Massot (Apr 24 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610345):
<p>Kevin, you forgot to switch browser</p>

#### [ Patrick Massot (Apr 24 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610350):
<p>To the one where you are logged in as Kenny</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610360):
<p>darn, I'm getting forgetful in my old age</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610367):
<p>General mathlib style guide says "if it's trivially true, then the best proof is an incomprehensible one-liner"</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610405):
<p>because there's no point writing a four line tactic proof like mine, which makes it clear how you are doing something completely trivial</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610426):
<p>But I spent a long long time writing all proofs in tactic mode before I felt comfortable with these fancy one-line term mode proofs</p>

#### [ Johan Commelin (Apr 24 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610428):
<p>Ok, so now I have proven that <code>h_1 x = 1</code>. So now I want to say <code>ker h_1 = im g_1</code> hence there is a <code>y : B_1</code> such that <code>g_1 y = x</code>.</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610430):
<p>How have you set things up: is ker h1 a set?</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610431):
<p>There are two ways of talking about what a mathematician would call a subset of a set</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610471):
<p>you can use sets or subtypes</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610478):
<p>they carry the same data, but packaged in different ways</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610480):
<p>One is a term, one is a type</p>

#### [ Johan Commelin (Apr 24 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610485):
<p><a href="https://gist.github.com/jcommelin/d097eb8f2587d34e5c337450bca543db" target="_blank" title="https://gist.github.com/jcommelin/d097eb8f2587d34e5c337450bca543db">https://gist.github.com/jcommelin/d097eb8f2587d34e5c337450bca543db</a></p>

#### [ Johan Commelin (Apr 24 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610486):
<p>That's an update</p>

#### [ Johan Commelin (Apr 24 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610489):
<p>With what I have so far</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610554):
<p>You're using sets</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610555):
<p>Oh wow, the message everyone was replying to has changed.</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610568):
<p>If you write <code>have := ...</code> in tactic mode</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610607):
<p>then Lean calls the thing you proved <code>this</code> by default</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610611):
<p>so you have about 20 hypotheses all called <code>this</code></p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610614):
<p>and you won't be able to use most of them</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610616):
<p>because <code>this</code> will only refer to one of them</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610619):
<p>and the rest will be inaccessible</p>

#### [ Johan Commelin (Apr 24 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610691):
<blockquote>
<p>Oh wow, the message everyone was replying to has changed.</p>
</blockquote>
<p>Yes, still need to figure out how github behaves. Sorry...</p>

#### [ Patrick Massot (Apr 24 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610707):
<p>For the record, the calc version of the previous question:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">W</span> <span class="n">X</span> <span class="n">Y</span> <span class="n">Z</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">W</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Z</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">W</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">j</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">Z</span><span class="o">)</span> <span class="o">(</span><span class="n">w</span> <span class="o">:</span> <span class="n">W</span><span class="o">)</span> <span class="o">(</span><span class="n">one</span> <span class="o">:</span> <span class="n">Z</span><span class="o">)</span>
<span class="o">(</span><span class="n">Hcom</span> <span class="o">:</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">t</span><span class="o">,</span> <span class="n">g</span> <span class="o">(</span><span class="n">f</span> <span class="n">t</span><span class="o">))</span> <span class="bp">=</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">t</span><span class="o">,</span> <span class="n">j</span> <span class="o">(</span><span class="n">h</span> <span class="n">t</span><span class="o">)))</span> <span class="o">(</span><span class="n">Hthis</span> <span class="o">:</span> <span class="n">j</span> <span class="o">(</span><span class="n">h</span> <span class="n">w</span><span class="o">)</span> <span class="bp">=</span> <span class="n">one</span><span class="o">)</span> <span class="o">:</span> <span class="n">g</span> <span class="o">(</span><span class="n">f</span> <span class="n">w</span><span class="o">)</span> <span class="bp">=</span> <span class="n">one</span> <span class="o">:=</span>
<span class="k">calc</span> <span class="n">g</span> <span class="o">(</span><span class="n">f</span> <span class="n">w</span><span class="o">)</span> <span class="bp">=</span> <span class="n">j</span> <span class="o">(</span><span class="n">h</span> <span class="n">w</span><span class="o">)</span> <span class="o">:</span> <span class="n">congr_fun</span> <span class="n">Hcom</span> <span class="n">w</span>
         <span class="bp">...</span> <span class="bp">=</span> <span class="bp">_</span> <span class="o">:</span> <span class="n">Hthis</span>
</pre></div>

#### [ Johan Commelin (Apr 24 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610708):
<p>About all the <code>this</code>es. My current strategy is to give them a name if I need to. But hopefully things like <code>rwa</code> and <code>apply_assumption</code> will just figure it out.</p>

#### [ Patrick Massot (Apr 24 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610767):
<p>I guess Kevin/Kenny term proof is a rather direct translation of that calc proof</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610778):
<p>yes, <code>calc</code> is just some elaborate way of applying <code>trans</code>, as we see from the calc docs ;-)</p>

#### [ Patrick Massot (Apr 24 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610843):
<p>I swear I didn't look at your term proof before writing this</p>

#### [ Patrick Massot (Apr 24 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610844):
<p>Because this is what I do with term proof</p>

#### [ Patrick Massot (Apr 24 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610845):
<p>My eyes refuse to stay on them</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610944):
<p>eew</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610945):
<p>the definition of kernel</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610947):
<p>is "the pre-image of the trivial subgroup"</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610951):
<p>Is that really better than "the things which map to the identity element"?</p>

#### [ Kenny Lau (Apr 24 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610954):
<p>they don’t like fibres</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610957):
<p><code>@[simp] lemma mem_trivial [group α] {g : α} : g ∈ trivial α ↔ g = 1</code></p>

#### [ Kenny Lau (Apr 24 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125610958):
<p>search for fibre in zulip</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611012):
<p>I wonder if they have the lemma that h is in ker beta iff beta h = 1? ;-)</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611034):
<p><code>lemma duh (f : A  → B) [is_group_hom f] (a : A) : a ∈ ker f ↔ f a = 1 := sorry</code></p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611036):
<p>That would definitely be a good start</p>

#### [ Johan Commelin (Apr 24 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611105):
<p>Ok, I have the hypothesis that <code>m</code> is bijective. I want to apply the fact that <code>m</code> is injective. The definition of <code>bijective m</code> is <code>injective m \and surjective m</code>. Is there a general tactic that kills this?</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611151):
<p>If <code>H</code> is a proof of <code>P \and Q</code> then <code>H.1</code> is a proof of <code>P</code></p>

#### [ Kenny Lau (Apr 24 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611158):
<p>I was going to say that</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611162):
<p>Don't bait Patrick</p>

#### [ Johan Commelin (Apr 24 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611184):
<p>Ok, thanks.</p>

#### [ Johan Commelin (Apr 24 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611388):
<p>What is the best way of writing <code>have := y : B_1 "such that g_1 y = x"</code>?</p>

#### [ Johan Commelin (Apr 24 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611400):
<p>Ok, that is pseudo-pseudo-Lean</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611448):
<p>Maybe you want to know about subtypes now</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611450):
<p>There's also <code>\ex</code></p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611451):
<p>exists</p>

#### [ Johan Commelin (Apr 24 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611461):
<p>ok, maybe that is useful</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611463):
<p><code>∃ y : B_1, g_1 y = x</code></p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611465):
<p>that's a Prop, so something of that type is a proof of that prop</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611470):
<p>and then you can uses <code>cases</code> on the proof in tactic mode to get to <code>y</code></p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611474):
<p>assuming you're in the middle of a proof.</p>

#### [ Johan Commelin (Apr 24 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611479):
<p>ok, going to try that</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611518):
<p>If you're in the middle of a construction (i.e. defining something, not proving something) then you need to invoke the axiom of choice to get <code>y</code> out ;-)</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611534):
<p>The other thing you can do is to actually make a new type -- a subtype</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611553):
<p><code>X := {y : B_1 // g_1 y = x}</code></p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611564):
<p>Now to build something of that type you need both an element y of B_1 and a proof that g_1 y = x</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611610):
<p>and then <code>⟨y,Hy⟩</code> has type X, where Hy is the proof</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611621):
<p>Or you can build the subset</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611635):
<p><code>X : set B_1 := {y : B_1 | g_1 y = x}</code></p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611639):
<p>but now X isn't a type, so you can't have things of type X</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611650):
<p>X is just the function from B_1 to Prop sending z to the statement that g_1 z = x</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611700):
<p>so now the assertion that y has the property you want is literally just <code>X y</code></p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611705):
<p>but the notation <code>y ∈ X</code> also exists</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611706):
<p><code>\in</code></p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611711):
<p>Which of these three answers you want might depend on what you're doing</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611720):
<p>and when I was learning Lean I found it very frustrating that there didn't seem to be a "right" answer for expressing something which in mathematics was unambiguous</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611724):
<p>but it's something I've now come to terms with</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611796):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> </p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">group_theory</span><span class="bp">.</span><span class="n">subgroup</span>

<span class="kn">open</span> <span class="n">function</span>

<span class="n">universes</span> <span class="n">u</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">A</span> <span class="n">B</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">group</span> <span class="n">A</span><span class="o">]</span> <span class="o">[</span><span class="n">group</span> <span class="n">B</span><span class="o">]</span>

<span class="kn">definition</span> <span class="n">ker</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">A</span>  <span class="bp">→</span> <span class="n">B</span><span class="o">)</span> <span class="o">[</span><span class="n">is_group_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">:=</span> <span class="n">is_group_hom</span><span class="bp">.</span><span class="n">ker</span> <span class="n">f</span>

<span class="kn">lemma</span> <span class="n">duh</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">A</span>  <span class="bp">→</span> <span class="n">B</span><span class="o">)</span> <span class="o">[</span><span class="n">is_group_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">A</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">ker</span> <span class="n">f</span> <span class="bp">↔</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Apr 24 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125611799):
<p>Ok enough of this, I had better go to work</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125612020):
<p>but I can't find this in subgroup.lean</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125612025):
<p>I just found it</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125612029):
<p><code>mem_ker</code></p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125612084):
<p>not a simp lemma, presumably because it relies on f</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125612087):
<p>so is not part of the simp philosophy</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125612111):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> I think you should open <code>is_group_hom</code></p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125612155):
<p>not least because then you don't have to define <code>ker</code>, it is just there for you</p>

#### [ Johan Commelin (Apr 24 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125612160):
<p>yes</p>

#### [ Johan Commelin (Apr 24 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125612162):
<p>I did that 2 minutes ago</p>

#### [ Johan Commelin (Apr 24 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125612166):
<p>the proof is really stupid funny</p>

#### [ Johan Commelin (Apr 24 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125612169):
<p>it is almost only <code>apply_assumption</code> and <code>cc</code></p>

#### [ Johan Commelin (Apr 24 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting%20a%20hypothesis/near/125612179):
<p>with a very rare <code>rwa</code> or <code>simp</code></p>


{% endraw %}
