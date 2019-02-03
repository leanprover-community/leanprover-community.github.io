---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57914stringtactic.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [string -> tactic?](https://leanprover-community.github.io/archive/113488general/57914stringtactic.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Apr 06 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124695173):
<p>Is there a good way to take a string (e.g. "simp, exact p") and return the tactic that executes it in interactive mode?</p>

#### [ Scott Morrison (Apr 06 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124695190):
<p>(I have some "self-describing tactics", which can print as a message "what they did" in terms of built-in tactics, and I would like to automatic verify they are producing correct output.)</p>

#### [ Simon Hudon (Apr 06 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124696700):
<p>I think the best I could do is something of type <code>string -&gt; parser (tactic unit)</code></p>

#### [ Simon Hudon (Apr 06 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124696748):
<p>I don't know how to run that in a tactic though ... unless we're parsing the parameters to the tactic. Is that good enough?</p>

#### [ Scott Morrison (Apr 06 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124696754):
<p>Unfortunately not. I'm deep inside a tactic by now.</p>

#### [ Simon Hudon (Apr 06 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124696801):
<p>I think we'd need to plead with the developers to give us a <code>parser_state.mk</code> function</p>

#### [ Scott Morrison (Apr 06 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124697368):
<p>If I want to parse a <code>rw_rule</code>, followed by a <code>nat</code> (e.g. so I can write <code>some_tactic foo 1</code>, or <code>some_tactic ← foo 3</code>), what am I meant to do?</p>

#### [ Scott Morrison (Apr 06 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124697374):
<p>I've worked out that <code> (q : parse (rw_rule_p (parser.pexpr 0)))</code> will parse a single <code>rw_rule</code>.</p>

#### [ Simon Hudon (Apr 06 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124697618):
<p>Is the <code>rw_rule</code> fed by the user through a <code>begin ... end</code> block?</p>

#### [ Scott Morrison (Apr 06 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124697661):
<p>yes</p>

#### [ Scott Morrison (Apr 06 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124697669):
<p>I've decided that it's just as good to parse a list of rw_rules, and this seems to work out of the box.</p>

#### [ Scott Morrison (Apr 06 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124697683):
<p><code>(q : parse rw_rules) (n : ℕ) </code></p>

#### [ Simon Hudon (Apr 06 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124697689):
<p>Oh good then</p>

#### [ Simon Hudon (Apr 06 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124697744):
<p>I don't know if <code>n : ℕ </code> will work but if it doesn't, you can use <code>n : parse small_nat</code></p>

#### [ Scott Morrison (Apr 06 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124697755):
<p>Ah, I see, I just found <code>parse small_nat</code> in <code>conv</code>. Not bothering to use the parser for the nat seems okay.</p>

#### [ Simon Hudon (Apr 06 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124697809):
<p>Alright then :)</p>

#### [ Mario Carneiro (Apr 06 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124698444):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> knows the answer to this one. My first thought was either a <code>parser A -&gt; tactic A</code> lift, or the <code>with_input</code> function which is used to implement <code>format!</code>, but the first doesn't exist (you can make a parser from a tactic but not vice versa) and the second only works in the parser monad. There is no way to create a <code>parser_state</code> in lean that I can see (which corresponds to creating a C++ <code>parser</code> object), so I think parsing can only be done at parse time, not at tactic running time. (One <em>suuper</em> hacky way to maybe get this to work is to call <code>lean</code> using the <code>io</code> monad with a file that you create.)</p>

#### [ Sebastian Ullrich (Apr 06 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string%20-%3E%20tactic%3F/near/124707373):
<p>What Mario said</p>


{% endraw %}
