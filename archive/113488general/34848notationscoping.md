---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/34848notationscoping.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [notation scoping](https://leanprover-community.github.io/archive/113488general/34848notationscoping.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sebastian Ullrich (May 28 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127193572):
<p><a href="#narrow/stream/113488-general/subject/local.20notation.20for.20fin.20(n.2B1)/near/127041848" title="#narrow/stream/113488-general/subject/local.20notation.20for.20fin.20(n.2B1)/near/127041848">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/local.20notation.20for.20fin.20(n.2B1)/near/127041848</a></p>
<blockquote>
<p>This is exactly how lean 2 notation used to work. Why it changed, I don't know, and I'm not clear on whether to expect this to be different in lean 4.<br>
I think that lean 3 notation is not handled very well at all, this is why I avoid all notation overloading in mathlib</p>
</blockquote>
<p>Lean 2 used the notion of "metaclasses" to scope notations, coercions, and attributes declared in namespaces. To use them, you had <code>open</code> the namespace, either with an explicit list of metaclasses, or with all of them as the default. It was annoying and didn't make any sense for most of the metaclasses - except perhaps for notations and <code>classical.prop_decidable</code>. We completely removed metaclasses for Lean 3.<br>
I'm open to proposals for a notation (and macro) scoping system in Lean 4. A survey of designs in other systems would probably be a good first step.</p>

#### [ Andrew Ashworth (May 28 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127194432):
<p>Do people like the way Coq does it?</p>

#### [ Andrew Ashworth (May 28 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127194473):
<p>for reference:</p>
<blockquote>
<p>Interpretation scopes<br>
An interpretation scope is a set of notations for terms with their interpretation. Interpretation scopes provide a weak, purely syntactical form of notations overloading: the same notation, for instance the infix symbol + can be used to denote distinct definitions of the additive operator. Depending on which interpretation scopes is currently open, the interpretation is different. Interpretation scopes can include an interpretation for numerals and strings. However, this is only made possible at the Objective Caml level.</p>
<p>See Figure 12.1 for the syntax of notations including the possibility to declare them in a given scope. Here is a typical example which declares the notation for conjunction in the scope type_scope.</p>
<p>Notation “A /\ B” := (and A B) : type_scope.<br>
Note</p>
<p>A notation not defined in a scope is called a lonely notation.</p>
<p>Global interpretation rules for notations<br>
At any time, the interpretation of a notation for term is done within a stack of interpretation scopes and lonely notations. In case a notation has several interpretations, the actual interpretation is the one defined by (or in) the more recently declared (or open) lonely notation (or interpretation scope) which defines this notation. Typically if a given notation is defined in some scope scope but has also an interpretation not assigned to a scope, then, if scope is open before the lonely interpretation is declared, then the lonely interpretation is used (and this is the case even if the interpretation of the notation in scope is given after the lonely interpretation: otherwise said, only the order of lonely interpretations and opening of scopes matters, and not the declaration of interpretations within a scope).</p>
<p>The initial state of Coq declares three interpretation scopes and no lonely notations. These scopes, in opening order, are core_scope, type_scope and nat_scope.</p>
</blockquote>

#### [ Patrick Massot (May 28 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127194784):
<p>I'm a bit confused to see Coq mentioned here. I thought notations were one of the areas where Lean is clearly better than Coq. I can already tell you mathematicians wouldn't be pleased to see <code>a .+ b</code> or <code>%N</code> everywhere.</p>

#### [ Andrew Ashworth (May 28 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127194900):
<p>would be nice since we have leanpkg that there would be some idea of "package-scope". then my notations, type-class instances, &amp;such have precedence when inside my package.</p>

#### [ Andrew Ashworth (May 28 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127195085):
<blockquote>
<p>I'm a bit confused to see Coq mentioned here. I thought notations were one of the areas where Lean is clearly better than Coq. I can already tell you mathematicians wouldn't be pleased to see <code>a .+ b</code> or <code>%N</code> everywhere.</p>
</blockquote>
<p>It's not quite about <code>a .+ b</code>, but more how should lean handle cases where people use notation to mean different things. consider if one person wants <code>sin^2 x</code> to be <code>(sin x)^2</code>, but another person wants it to mean <code>sin (sin x)</code>. They define that notation in their own files and for whatever reason you end up importing both of them.  Which one should win?</p>

#### [ Sean Leather (May 28 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127195271):
<p>Or, for another example, about the interpretation of <code>[n]</code>: <code>fin (n+1)</code> or <code>list.cons n list.nil</code>.</p>

#### [ Sean Leather (May 28 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127195493):
<p>I'm not intimately familiar with the Coq notation given above, but it sounds complicated and confusing. I would like to see notation and non-notation name scopes be treated similarly and simply by <code>open</code>, probably more like of Agda. (But I'm sure my familiarity breeds bias.)</p>

#### [ Andrew Ashworth (May 28 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127195725):
<p>i think that would be fine too, but i'd also like restrictions on imported packages polluting the global namespace if that's an approach people like</p>

#### [ Sean Leather (May 28 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127195808):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> Maybe we're thinking from different sides of the same coin? It sounds you want a given global name-/notation-space with the ability to restrict it. I think I'd rather have an empty-by-default space with the ability to explicitly expand it using <code>open</code>.</p>

#### [ Sebastian Ullrich (May 28 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127196091):
<p>As a general comment, much of Coq's notation complexity seems to stem from the fact that it does not support notation overloading (i.e. overlapping notation disambiguated at elaboration time). Is that correct?</p>

#### [ Sebastian Ullrich (May 28 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127196092):
<p>I don't know what Agda's system is like.</p>

#### [ Sean Leather (May 28 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127196345):
<p>There are <a href="https://agda.readthedocs.io/en/latest/language/syntax-declarations.html" target="_blank" title="https://agda.readthedocs.io/en/latest/language/syntax-declarations.html">Agda syntax declarations</a>, but I was thinking mainly about the power and flexibility of Agda's <code>open</code> for modules. Since you can use nearly arbitrary Unicode naming structure (cf. mixfix parsing) in Agda, most of what is notation in Lean are names in Agda. Thus, they are treated by <code>open</code> in the same way as ASCII names are.</p>

#### [ Sean Leather (May 28 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127196429):
<p>One possibility is to give a <code>notation</code> declaration a name and support bringing notation into scope or excluding it from scope via the name.</p>

#### [ Sean Leather (May 28 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127196751):
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">list</span>
<span class="kn">notation</span> <span class="n">square_brackets</span> <span class="o">:</span> <span class="bp">`</span><span class="o">[</span><span class="bp">`</span> <span class="n">l</span><span class="o">:(</span><span class="n">foldr</span> <span class="bp">`</span><span class="o">,</span> <span class="bp">`</span> <span class="o">(</span><span class="n">h</span> <span class="n">t</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">cons</span> <span class="n">h</span> <span class="n">t</span><span class="o">)</span> <span class="n">list</span><span class="bp">.</span><span class="n">nil</span> <span class="bp">`</span><span class="o">]</span><span class="bp">`</span><span class="o">)</span> <span class="o">:=</span> <span class="n">l</span>
<span class="kn">end</span> <span class="n">list</span>

<span class="kn">section</span> <span class="n">list_with_brackets</span>
<span class="kn">open</span> <span class="n">list</span> <span class="c1">-- brings everything, including notation, into scope</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">list</span> <span class="n">nat</span> <span class="o">:=</span> <span class="o">[</span><span class="mi">1</span><span class="o">,</span> <span class="mi">2</span><span class="o">,</span> <span class="mi">3</span><span class="o">]</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">list</span> <span class="n">nat</span> <span class="o">:=</span> <span class="n">map</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="o">[</span><span class="mi">1</span><span class="o">,</span> <span class="mi">2</span><span class="o">,</span> <span class="mi">3</span><span class="o">]</span>
<span class="kn">end</span> <span class="n">list_with_brackets</span>

<span class="kn">section</span> <span class="n">list_without_open</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">list</span> <span class="n">nat</span> <span class="o">:=</span> <span class="n">list</span><span class="bp">.</span><span class="n">cons</span> <span class="mi">1</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">cons</span> <span class="mi">2</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">cons</span> <span class="mi">3</span> <span class="n">list</span><span class="bp">.</span><span class="n">nil</span><span class="o">))</span> <span class="c1">-- no brackets in scope</span>
<span class="kn">end</span> <span class="n">list_without_open</span>

<span class="kn">section</span> <span class="n">list_with_brackets_but_not_whole_namespace</span>
<span class="kn">open</span> <span class="n">list</span> <span class="o">(</span><span class="n">square_brackets</span><span class="o">)</span> <span class="c1">-- brings only notation into scope</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">list</span> <span class="n">nat</span> <span class="o">:=</span> <span class="o">[</span><span class="mi">1</span><span class="o">,</span> <span class="mi">2</span><span class="o">,</span> <span class="mi">3</span><span class="o">]</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">list</span> <span class="n">nat</span> <span class="o">:=</span> <span class="n">map</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="o">[</span><span class="mi">1</span><span class="o">,</span> <span class="mi">2</span><span class="o">,</span> <span class="mi">3</span><span class="o">]</span> <span class="c1">-- error: should be list.map</span>
<span class="kn">end</span> <span class="n">list_with_brackets_but_not_whole_namespace</span>
</pre></div>

#### [ Sebastian Ullrich (May 28 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127199647):
<blockquote>
<p>One possibility is to give a notation declaration a name and support bringing notation into scope or excluding it from scope via the name.</p>
</blockquote>
<p>I like that. Because we want to translate notations to macros in Lean 4, we have to give them _some_ name anyway.</p>

#### [ Sebastian Ullrich (May 28 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127199766):
<p>It's fun to think about what the standard declaration modifiers mean in that case:</p>
<ul>
<li><code>private</code> corresponds to <code>local</code></li>
<li><code>protected</code> is... interesting <span class="emoji emoji-1f604" title="smile">:smile:</span>  . Something like <code>persistent local</code>?</li>
<li><code>export</code> can be used for Coq's <code>Global</code></li>
</ul>

#### [ Sebastian Ullrich (May 28 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127199785):
<p>And of course <code>hide</code> hides any notation, global or not</p>

#### [ Mario Carneiro (May 28 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127199792):
<p>I don't understand how to use <code>hide</code></p>

#### [ Sebastian Ullrich (May 28 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127199797):
<p>You mean right now?</p>

#### [ Mario Carneiro (May 28 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127199805):
<p>when I have overloaded notations it's impossible to specify which to hide</p>

#### [ Mario Carneiro (May 28 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127199807):
<p>yes</p>

#### [ Sebastian Ullrich (May 28 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127199919):
<p><code>hide</code> currently only works for <code>open</code>ed or <code>export</code>ed names, I think. Perhaps that could be lifted. For specifying overloaded notations, you'd need to know their macro names. I'm not sure what the autogenerated names would look like, probably similar to <code>instance</code>.</p>

#### [ Sean Leather (May 28 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127200712):
<blockquote>
<p>Because we want to translate notations to macros in Lean 4, we have to give them _some_ name anyway.</p>
</blockquote>
<p>Oh, that's good. Can you generalize to make <code>infixl</code>/<code>infixr</code> a kind of notation and nameable, since it also affects how identifiers are parsed in a given scope?</p>

#### [ Sebastian Ullrich (May 28 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127200743):
<p>Sure, they are already implemented via <code>notation</code> in Lean 3 anyway</p>

#### [ Sean Leather (May 28 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127200794):
<p>Cool! And, while you're at it, point notation? In the same vein as we discussed in the past? <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Sebastian Ullrich (May 28 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127200799):
<p>Uh. Do you have a link? :)</p>

#### [ Sean Leather (May 28 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127200806):
<p>The namespace field projection stuff.</p>

#### [ Sean Leather (May 28 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127200811):
<p><a href="#narrow/stream/113488-general/topic/namespace.20field.20notation" title="#narrow/stream/113488-general/topic/namespace.20field.20notation">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace.20field.20notation</a></p>

#### [ Sean Leather (May 28 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127200862):
<p>Basically, I think you could consider field notation as a special notation that could become more flexible than right now.</p>

#### [ Sebastian Ullrich (May 28 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127201356):
<p>I haven't seen a very convincing example for generalizing projection notation outside of the original namespace yet. It may be simple to implement it yourself when the elaborator is implemented in Lean, but currently I'm not anticipating that to happen in the first version of Lean 4. On the other hand, we're definitely planning to rewrite the pretty printer in Lean, so adding dot notation support during that sound good to me.</p>

#### [ Sean Leather (May 28 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127201425):
<p>Dot-notation pretty-printing is a good step. But I don't think I'd want everything that could be pretty-printed with that notation to be done in that way. Do you?</p>

#### [ Sebastian Ullrich (May 28 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127201875):
<p>No, I think there should be an option with values "none/attributed/all"</p>

#### [ Sean Leather (May 28 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127201979):
<p>A global <code>set_option</code> option? I was thinking it would be preferable to decide for each identifier. What do each of the values mean?</p>

#### [ Sebastian Ullrich (May 28 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127202324):
<p>"none": never pretty-print projection notation<br>
"attributed": use on identifiers attributed with some new attribute<br>
"all": use where possible</p>

#### [ Sebastian Ullrich (May 28 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127202410):
<p>So I agree with you that there should be an attribute, but there should also be a quick way to turn it off completely</p>

#### [ Sean Leather (May 28 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20scoping/near/127202415):
<p>Sure, that sounds reasonable.</p>


{% endraw %}
