---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/75896syntaxsurprises.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [syntax surprises](https://leanprover-community.github.io/archive/113488general/75896syntaxsurprises.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sebastian Ullrich (Jun 19 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128299157):
<p>The Lean 4 parser only understands <code>prelude</code>, <code>import</code>, and <code>theory</code> so far, but I've already learned something surprising: <code>noncomputable theory</code> can be used anywhere in a file (also, multiple times)</p>

#### [ Sean Leather (Jun 19 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128299364):
<p>Can you elucidate on what is surprising about that?</p>

#### [ Sebastian Ullrich (Jun 19 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128299761):
<p>I assumed it only worked on the top of a file, since we usually use "theory" synonymously to "file".</p>

#### [ Sean Leather (Jun 19 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128300248):
<p>Ah, <code>theory</code>, not <code>theorem</code>: I missed that. I also didn't know <code>theory</code> was a keyword.</p>

#### [ Sean Leather (Jun 19 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128300366):
<p>I've only worked on computable theorems. Looking in the Lean 3 core library and mathlib, I see only <code>noncomputable theory</code> used. I don't see <code>theory</code> mentioned in the reference manual or TPIL. What purpose does <code>theory</code> serve?</p>

#### [ Sebastian Ullrich (Jun 19 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128300531):
<p><code>theory</code> is a command, like <code>theorem</code>. <code>noncomputable</code> is a modifier you can apply to either of them. The distinction doesn't really matter in Lean 3 since <code>theory</code> can only be used together with<code>noncomputable</code>, which marks the remainder of the file as noncomputable.</p>

#### [ Kenny Lau (Jun 19 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128300541):
<p>which marks the <em>appropriate</em> remainder of the file as noncomputable</p>

#### [ Sebastian Ullrich (Jun 19 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128300547):
<p>yes</p>

#### [ Kenny Lau (Jun 19 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128300549):
<p>computable functions remain computable</p>

#### [ Sebastian Ullrich (Jun 19 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128300685):
<p>Perhaps we'll want to generalize <code>theory</code> in Lean 4, though I'm not sure whether there are many sensible combinations. Say, using <code>private theory</code>, then negating it using a new keyword <code>public</code> on a few declarations.</p>

#### [ Kenny Lau (Jun 19 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128300690):
<p>lean -- java remade</p>

#### [ Reid Barton (Jun 19 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128304668):
<p>Oh funny, I've used <code>noncomputable theory</code> inside a section before and sort of expected it to be scoped, though there's no way I'd ever notice if it wasn't.</p>

#### [ Johannes Hölzl (Jun 19 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308056):
<p>wasn't there a Github issue the idea of introducing also <code>meta theory</code>?</p>

#### [ Johannes Hölzl (Jun 19 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308151):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> what about changing <code>theory</code> to be only allowed at the file header, but extend <code>section</code> and <code>namespace</code> to take <code>meta</code>, <code>noncomputable</code>, <code>private</code>, <code>protected</code>, <code>public</code> modifiers?</p>

#### [ Kenny Lau (Jun 19 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308168):
<p>how do you define file header?</p>

#### [ Kenny Lau (Jun 19 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308172):
<p>currently <code>import</code> must be at the beginning</p>

#### [ Sebastian Ullrich (Jun 19 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308179):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span>  Yes, that's my plan right now :)</p>

#### [ Sebastian Ullrich (Jun 19 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308183):
<p>Also, attributes on sections</p>

#### [ Johannes Hölzl (Jun 19 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308187):
<p>Nice!</p>

#### [ Sebastian Ullrich (Jun 19 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308276):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Right now I've defined it as <code>prelude? (import ...)* (noncomputable theory)?</code></p>

#### [ Kenny Lau (Jun 19 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308342):
<p>are you going to regex the whole file</p>

#### [ Sebastian Ullrich (Jun 19 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308362):
<p>Of course, everyone knows you solve all problems with regexes</p>

#### [ Kenny Lau (Jun 19 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308375):
<p>now you have 2...</p>

#### [ Johannes Hölzl (Jun 19 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308434):
<p>modulo whitespace / comments</p>

#### [ Sebastian Ullrich (Jun 19 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308458):
<p><code>repeat { all_goals { apply_regex } }</code></p>

#### [ Johannes Hölzl (Jun 19 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308841):
<p>another purpose of theory could be to set parameters, or execute an imported command, like <code>mathlib theory</code>. This would setup certain notation, options, namespaces, version checks etc. I guess this could be also solved using <code>run_cmd</code>, but <code>theory</code> is a nice syntax. Also, what about moving <code>prelude</code> to <code>prelude theory</code>?</p>

#### [ Sebastian Ullrich (Jun 19 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128309035):
<p><code>prelude</code> should logically come before <code>import</code> since it suppreses the default imports. We could move <code>theory</code> to the front instead, I'm not sure.</p>

#### [ Johannes Hölzl (Jun 19 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128309284):
<p>Okay, this makes sense.</p>

#### [ Sebastian Ullrich (Jun 19 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128309423):
<p>There shouldn't be any reason to restrict the modifiers applicable to <code>theory</code> in Lean 4, no. Though, in the examples so far, it sounded like applying something to <code>theory</code> or <code>section</code> simply distributes it to all contained declarations (even if, as Kenny pointed out, it will behave differently from e.g. an explicit <code>noncomputable</code>). Your <code>mathlib</code> example doesn't quite fit in that scheme.</p>

#### [ Mario Carneiro (Jun 19 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128311123):
<p>Will lean 4 allow for gathering the global file structure? For example: find the open section and namespace names; currently declared variables and parameters, notations and other <code>local</code> declarations; finding the "outline" of a given file, i.e. the tree of namespace and section blocks and the definitions in them</p>

#### [ Sebastian Ullrich (Jun 19 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128311421):
<p>You'll definitely get access to a concrete syntax tree of the entire file. You should also get access to more "dynamic" information like open namespaces (which could be influenced by a <code>run_cmd</code>), though it's less clear what that could look like</p>


{% endraw %}
