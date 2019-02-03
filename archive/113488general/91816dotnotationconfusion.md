---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/91816dotnotationconfusion.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [dot notation confusion](https://leanprover-community.github.io/archive/113488general/91816dotnotationconfusion.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Feb 01 2019 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157341136):
<p>I have always been confused about dot notation. I don't use it as much as other people, because I don't understand it as well as other people. I've read <a href="https://github.com/PatrickMassot/mathlib/blob/e5aad2e4e0964c7624183efdb534878b6a06bbb5/docs/extras/structures.md#about-the-namespace-shortcut" target="_blank" title="https://github.com/PatrickMassot/mathlib/blob/e5aad2e4e0964c7624183efdb534878b6a06bbb5/docs/extras/structures.md#about-the-namespace-shortcut">Patrick's notes</a> on this and TPIL but I think there's more to it.</p>
<p>I understand that if I make a new structure <code>structure point (α : Type) := (x : α) (y : α)</code> then for <code>p : point</code> I can use <code>p.x</code> instead of <code>point.x p</code>. I also understand that if we make more functions in the structure's namespace like <code>point.blah</code> (which for simplicity takes as input one point and possibly some other stuff) then <code>p.blah</code> is shorthand for <code>point.blah p</code> (or perhaps <code>point.blah _ _ p</code> if the point happens not to be the first thing that <code>point.blah</code> eats). </p>
<p>What threw me yesterday when working on the perfectoid project was that my proof that if <code>neg</code> was a continuous function on a topological ring then it was also a continuous function on a subring looked like this:</p>
<div class="codehilite"><pre><span></span><span class="n">continuous_neg</span> <span class="o">:=</span> <span class="n">continuous_subtype_mk</span> <span class="bp">_</span> <span class="err">$</span>
                    <span class="n">continuous</span><span class="bp">.</span><span class="n">comp</span>
                      <span class="n">continuous_subtype_val</span> <span class="err">$</span>
                      <span class="n">topological_ring</span><span class="bp">.</span><span class="n">continuous_neg</span> <span class="n">A</span>
</pre></div>


<p>and then Patrick took one look at this code and pointed out that this could be written</p>
<div class="codehilite"><pre><span></span><span class="n">continuous_neg</span> <span class="o">:=</span> <span class="n">continuous_subtype_mk</span> <span class="bp">_</span> <span class="err">$</span>
                      <span class="n">continuous_subtype_val</span><span class="bp">.</span><span class="n">comp</span> <span class="err">$</span>
                      <span class="n">topological_ring</span><span class="bp">.</span><span class="n">continuous_neg</span> <span class="n">A</span>
</pre></div>


<p>It took me a while to realise that he wasn't talking about some fancy new function in the topology directory in mathlib but was in fact advocating the use of the dot notation. It would never have occurred to me to try to use dot notation here. In the examples above, which I understand, we have <code>p : point</code>, i.e. a term whose type is a structure and then a function in the corresponding namespace. But here <code>continuous_subtype_val</code> has type <code>∀ {α : Type u} [_inst_1 : topological_space α] {p : α → Prop}, continuous subtype.val</code> which is definitely not a structure, and even if I remove all the implicit arguments then it becomes <code>continuous subtype.val</code> which is also not a structure, and even if I look at the head function then it's <code>continuous</code> which is also not a structure. But Patrick's code does work. I am fast coming to the conclusion that my understanding of dot notation is nowhere near complete.</p>
<p>Investigating further, I find that <code>#check continuous_subtype_val.comp</code> works, even though there appears to be no function <code>continuous_subtype_val.comp</code>. Moreover, this seems to have nothing to do with structures at all, because <code>continuous</code> is not a structure, it's just a plain old definition. What seems to be going on in this situation is that if <code>p</code> has type <code>{implicit stuff} [more implicit stuff] foo x</code> and <code>foo</code> happens coincidentally to be both a function and a namespace (which is something that <code>continuous</code> seems to be, for some reason I don't understand) then <code>p.blah</code> is defined to mean <code>foo.blah p</code> . In some sense I am surprised that this is ever useful beyond the case I understand, i.e. structures. If <code>continuous_subtype_val</code> had happened to just take one explicit argument, which in a parallel universe it could have done, I am assuming that this trick would stop working.</p>
<p>So is the philosophy something like "if <code>foo</code> is any old function, and if I'm defining a function <code>f : foo x -&gt; y</code>, then I might want to consider calling the function <code>foo.f</code>because then I can write <code>f.p</code> if <code>p : foo x</code>? What I don't get is that if I had just called it <code>f</code> then I could have written <code>f p</code> which is just as many characters as <code>f.p</code> anyway. </p>
<p>I guess I can understand that if <code>foo</code> is a structure and I wanted to define a <code>neg</code> on <code>foo x</code> then I would instinctively called it <code>foo.neg</code>. But I wouldn't do this for <code>continuous</code>. Is this evidence that <code>continuous</code> should be a structure? Are our naming conventions treating it like it is one?</p>
<p>Confused in London.</p>

#### [ Sebastian Ullrich (Feb 01 2019 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157342303):
<p>To spell it out, the full semantics of dot notation is, roughly, "if <code>e</code> is a <em>term</em> of type <code>t ...</code>, and there is a function <code>t.f</code>, then <code>e.f ...</code> is syntax sugar for <code>t.f ... e ...</code>, where <code>e</code> has been inserted as the argument for the first parameter of type <code>t ...</code>". <code>e</code> being a variable of a structure <code>s</code> and <code>s.f</code> being a projection is just a special case of that.</p>

#### [ Sebastian Ullrich (Feb 01 2019 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157342527):
<p>Note that the <em>term</em> <code>continuous_subtype_val</code> has type <code>continuous subtyp.val</code>. The type you gave is the type of <code>@continuous_subtype_val</code>! So dot notation doesn't think "oh, this is a function", but "oh, this is a <code>continuous</code>"</p>

#### [ Mario Carneiro (Feb 01 2019 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157342530):
<p>Originally, <code>continuous.comp</code> was called <code>continuous_comp</code>. It was renamed because it is "eligible" for projection notation like this</p>

#### [ Mario Carneiro (Feb 01 2019 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157342582):
<p>You can't just call it <code>comp</code> because that overlaps with a million other things</p>

#### [ Mario Carneiro (Feb 01 2019 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157342712):
<p>There is a danger in using non-structures with projection notation, because regular defs can be unfolded, and once they are unfolded they no longer have that name anymore (<code>continuous</code> in this case) so the projections won't find the namespace. In practice I haven't had too much issue with this unless you are solving some weird unification problem</p>

#### [ Mario Carneiro (Feb 01 2019 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157342733):
<p>and in that case it's not too bad to just say <code>continuous.comp ...</code></p>

#### [ Kevin Buzzard (Feb 01 2019 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157342952):
<p><code>continuous.comp</code> was "eligible" because it took <code>continuous f</code> as an input. It seems to me that the real coincidence is that <code>continuous_subtype_val</code> has type <code>continuous ...</code> and every other input can be inferred.</p>

#### [ Mario Carneiro (Feb 01 2019 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157342968):
<blockquote>
<p>If continuous_subtype_val had happened to just take one explicit argument, which in a parallel universe it could have done, I am assuming that this trick would stop working.</p>
</blockquote>
<p>No, it would be written <code>(continuous_subtype_val _).comp</code> in that case</p>

#### [ Mario Carneiro (Feb 01 2019 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157343048):
<p>it's not a coincidence that <code>continuous_subtype_val</code> returns a <code>continuous</code>; that's the whole point of the function, we are proving things are continuous. Possibly some hypotheses would be necessary but those can be dealt with as above</p>

#### [ Kevin Buzzard (Feb 01 2019 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157343077):
<p>Ok I think I now understand. Thanks to Sebastian and Mario as ever. Would I be right in thinking that the complete list of functions that aren't structures but which have an associated namespace is quite small? <code>continuous</code> being one. Or does this happen everywhere and I've just not noticed it yet (and this is the reason I underuse dot notation)?</p>

#### [ Mario Carneiro (Feb 01 2019 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157343078):
<p>You can basically always use <code>continuous.comp</code> with projection notation, because the first argument will be a <code>continuous</code></p>

#### [ Kevin Buzzard (Feb 01 2019 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157343128):
<p>Oh!</p>

#### [ Kevin Buzzard (Feb 01 2019 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157343148):
<p>So in fact it's utterly commonplace and this is why Patrick spotted it so quickly</p>

#### [ Kevin Buzzard (Feb 01 2019 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157343176):
<p>You basically never write <code>continuous.comp</code> at all!</p>

#### [ Kevin Buzzard (Feb 01 2019 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157343185):
<p>It does hamper readability though</p>

#### [ Mario Carneiro (Feb 01 2019 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157343186):
<p>it's a pretty simple and common trick, enough that I can't say how many times it's been used in mathlib. If a theorem about <code>foo</code> things has an argument of type <code>foo x</code>, you should consider calling it <code>foo.bar</code> instead of <code>foo_bar</code></p>

#### [ Kevin Buzzard (Feb 01 2019 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157343237):
<p>And now I understand why</p>

#### [ Mario Carneiro (Feb 01 2019 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157343238):
<p>Personally I like having <code>.comp</code> as a sort of infix operator. If you turn your head and squint it looks like the <code>∘</code></p>

#### [ Kevin Buzzard (Feb 01 2019 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157343241):
<p>It's to maximise obfuscation :-)</p>

#### [ Kenny Lau (Feb 01 2019 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157343249):
<p>I can read it perfectly without any problem</p>

#### [ Kevin Buzzard (Feb 01 2019 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157343257):
<p>You should have called it <code>continuous.o</code></p>

#### [ Kevin Buzzard (Feb 01 2019 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157343295):
<p>Wait</p>

#### [ Mario Carneiro (Feb 01 2019 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157343322):
<p>you are about to point out the order is wrong, I'm sure</p>

#### [ Kevin Buzzard (Feb 01 2019 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157343328):
<p>its inputs are in the...</p>

#### [ Kevin Buzzard (Feb 01 2019 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157343329):
<p>Yeah :-)</p>

#### [ Mario Carneiro (Feb 01 2019 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157343381):
<p>not sure there is any big reason for that</p>

#### [ Mario Carneiro (Feb 01 2019 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157343442):
<p>also not sure I care about it</p>

#### [ Mario Carneiro (Feb 01 2019 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157343490):
<p>I will let Scott have his hobby horse</p>

#### [ Johan Commelin (Feb 01 2019 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dot%20notation%20confusion/near/157344279):
<p>I guess we can still define <code>continuous.o</code> with arguments in the right order...</p>


{% endraw %}
