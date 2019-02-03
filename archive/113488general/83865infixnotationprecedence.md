---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83865infixnotationprecedence.html
---

## Stream: [general](index.html)
### Topic: [infix notation precedence](83865infixnotationprecedence.html)

---


{% raw %}
#### [ Sean Leather (Jun 07 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/infix%20notation%20precedence/near/127717979):
<p>I want something that is effectively equivalent to this:</p>
<div class="codehilite"><pre><span></span><span class="n">reserve</span> <span class="kn">infix</span> <span class="bp">`</span> <span class="n">d</span><span class="err">∉</span> <span class="bp">`</span><span class="o">:</span><span class="mi">51</span>
<span class="n">local</span> <span class="kn">notation</span> <span class="n">a</span> <span class="n">d</span><span class="err">∉</span> <span class="n">l</span> <span class="o">:=</span> <span class="n">blah</span> <span class="n">l</span> <span class="n">a</span>
</pre></div>


<p>However, I'm guessing it's not a good idea to use <code>reserve</code> here. I've tried several <code>notation</code> declarations (e.g. <code>notation a ` d∉ `:51 l</code> and <code>notation a ` d∉ `:51 l:0</code>), but I can't seem to get the precedence right. What's the correct way to specify the above without using <code>reserve</code>?</p>

#### [ Sebastian Ullrich (Jun 07 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/infix%20notation%20precedence/near/127718532):
<p>Why are you not using <code>local infix</code>?</p>

#### [ Sean Leather (Jun 07 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/infix%20notation%20precedence/near/127718663):
<p>Because then I would have to write:</p>
<div class="codehilite"><pre><span></span><span class="n">local</span> <span class="kn">infix</span> <span class="bp">`</span> <span class="n">d</span><span class="err">∉</span> <span class="bp">`</span><span class="o">:</span><span class="mi">51</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">l</span><span class="o">,</span> <span class="n">blah</span> <span class="n">l</span> <span class="n">a</span>
</pre></div>

#### [ Sebastian Ullrich (Jun 07 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/infix%20notation%20precedence/near/127718782):
<p>I see. The equivalent to <code>infix</code> should be </p>
<div class="codehilite"><pre><span></span>a ` d∉ `:51 l:51
</pre></div>

#### [ Sean Leather (Jun 07 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/infix%20notation%20precedence/near/127718930):
<p>Ah ha! Can you help me understand that?</p>

#### [ Sebastian Ullrich (Jun 07 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/infix%20notation%20precedence/near/127719540):
<p>The first <code>:51</code> sets the token's binding power, whereas the second one sets the right-binding power (rbp) the Pratt parser will use while parsing that expression. The parser will try to parse an expression until it encounters a token with bp &lt;= its rbp. The rbp used initially is 0.<br>
For example, on the input <code>a d∉ b d∉ c</code> (not that it makes much sense in your case), the parser will start with rbp 0, read the leading term <code>a</code>, read the token with bp &gt; 0, then recurse for the notation RHS using rbp 51. This recursive call will read the leading <code>b</code>, then stop at the token since 51 &lt;= 51, and return. The original parser call will accept it, since it uses rbp 0, and complete parsing the input. Thus the output is <code>(a d∉ b) d∉ c</code> because the parser for the first notation's RHS stopped after <code>b</code>.</p>

#### [ Sebastian Ullrich (Jun 07 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/infix%20notation%20precedence/near/127719638):
<p>If you use <code>infixr</code> instead and do <code>#print d∉</code>, you'll see that the RHS now has rbp 50 so that it will consume the <code>d∉</code> token</p>

#### [ Sean Leather (Jun 08 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/infix%20notation%20precedence/near/127757084):
<p>Thanks, <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span>!</p>


{% endraw %}
