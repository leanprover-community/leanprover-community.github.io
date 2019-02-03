---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/23324Understandingnotationdeclarations.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Understanding notation declarations](https://leanprover-community.github.io/archive/113488general/23324Understandingnotationdeclarations.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Brendan Seamas Murphy (Mar 04 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Understanding%20notation%20declarations/near/123248290):
<p>Hi all! I'm kind of confused about how notation works. I have a setup like this:</p>
<div class="codehilite"><pre><span></span><span class="kn">constant</span> <span class="n">SQL</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="kn">constant</span> <span class="n">groupBy</span> <span class="o">:</span> <span class="n">SQL</span> <span class="bp">→</span> <span class="n">SQL</span> <span class="bp">→</span> <span class="n">SQL</span> <span class="bp">→</span> <span class="n">SQL</span>

<span class="kn">notation</span> <span class="bp">`</span><span class="n">SELECT</span><span class="bp">`</span> <span class="bp">`*`</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">x</span>
<span class="kn">notation</span> <span class="bp">`</span><span class="n">FROM1</span><span class="bp">`</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">a</span>
<span class="kn">notation</span> <span class="bp">`</span><span class="n">SELECT</span><span class="bp">`</span> <span class="n">proj</span> <span class="bp">`</span><span class="n">FROM1</span><span class="bp">`</span><span class="o">:</span><span class="mi">1</span> <span class="n">a</span> <span class="bp">`</span><span class="n">GROUP</span><span class="bp">`</span> <span class="bp">`</span><span class="n">BY</span><span class="bp">`</span> <span class="n">v</span> <span class="o">:=</span> <span class="n">groupBy</span> <span class="n">proj</span> <span class="n">a</span> <span class="n">v</span>
</pre></div>


<p>And I can't write <code>SELECT a FROM1 b GROUP BY c</code>, I need to write <code>SELECT (a) FROM1 b GROUP BY c</code>. I also need the <code>:1</code> after <code>FROM1</code> to get it to parse at all, and I don't know why.</p>

#### [ Simon Hudon (Mar 04 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Understanding%20notation%20declarations/near/123250724):
<p>The <code>:1</code> is for precedence. If the parser meets <code>... x + y FROM1</code> the precedence tells Lean whether to keep reading to the right or to build the <code>x + y</code> expression some more with stuff on the left</p>


{% endraw %}
