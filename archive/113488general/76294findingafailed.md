---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/76294findingafailed.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [finding a failed](https://leanprover-community.github.io/archive/113488general/76294findingafailed.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Keeley Hoek (Sep 10 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finding%20a%20failed/near/133643406):
<p>What's the easiest way to find where a "failed" was generated? I've been resorting to inserting trace statements in multiple files and now its just getting out of hand</p>

#### [ Keeley Hoek (Sep 10 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finding%20a%20failed/near/133643997):
<p>also, in the tactic monad, is there a way to get a stacktrace?</p>

#### [ Mario Carneiro (Sep 10 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finding%20a%20failed/near/133644045):
<p>There is the <code>vm</code> monad, which purports to be a debugger, but I don't know anyone who knows how to use it except possibly <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span></p>

#### [ Simon Hudon (Sep 10 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finding%20a%20failed/near/133671919):
<p>What I usually do is that, if I have a function with three lines I add the following until I find the error:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">my_fn</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">stmt1</span> <span class="bp">&lt;|&gt;</span> <span class="n">fail</span> <span class="s2">&quot;line A&quot;</span><span class="o">,</span>
   <span class="n">stmt2</span> <span class="bp">&lt;|&gt;</span> <span class="n">fail</span> <span class="s2">&quot;line B&quot;</span><span class="o">,</span>
   <span class="n">stmt3</span> <span class="bp">&lt;|&gt;</span> <span class="n">fail</span> <span class="s2">&quot;line C&quot;</span>
</pre></div>


<p>When I have found the function that fails, I repeat in that function.</p>

#### [ Sebastian Ullrich (Sep 10 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finding%20a%20failed/near/133673961):
<p>I've never used <code>vm</code> <span class="emoji emoji-1f605" title="sweat smile">:sweat_smile:</span> . I suppose it should be possible to write a <code>vm_monitor</code> that prints the stack trace whenever <code>failed</code> is called.</p>

#### [ Mario Carneiro (Sep 10 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finding%20a%20failed/near/133674025):
<p>who wrote it?</p>

#### [ Simon Hudon (Sep 10 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finding%20a%20failed/near/133683100):
<p>I had never used `vm_monitor and I gave it a try. Here's what I did:</p>
<div class="codehilite"><pre><span></span><span class="kn">set_option</span> <span class="n">debugger</span> <span class="n">true</span>

<span class="bp">@</span><span class="o">[</span><span class="n">vm_monitor</span><span class="o">]</span>
<span class="n">meta</span> <span class="n">def</span> <span class="n">my_mon</span> <span class="o">:</span> <span class="n">vm_monitor</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">init</span> <span class="o">:=</span> <span class="o">(),</span>
  <span class="n">step</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">do</span> <span class="n">vm</span><span class="bp">.</span><span class="n">curr_fn</span> <span class="bp">&gt;&gt;=</span> <span class="n">vm</span><span class="bp">.</span><span class="n">trace</span> <span class="o">}</span>

<span class="n">run_cmd</span> <span class="n">my_tactic</span>

<span class="kn">set_option</span> <span class="n">debugger</span> <span class="n">false</span>
</pre></div>


<p>It sets up a monitor that, before each instruction, prints the name of the enclosing function. It does not seem to be aware of failures but at least, you can figure out where the problem is by looking at the last printout</p>

#### [ Simon Hudon (Sep 10 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finding%20a%20failed/near/133684138):
<p>If you use the following instead, you can get an overview of the call nesting structure:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">vm_monitor</span><span class="o">]</span>
<span class="n">meta</span> <span class="n">def</span> <span class="n">my_mon</span> <span class="o">:</span> <span class="n">vm_monitor</span> <span class="o">(</span><span class="n">nat</span> <span class="bp">×</span> <span class="n">option</span> <span class="n">name</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">init</span> <span class="o">:=</span> <span class="o">(</span><span class="mi">0</span><span class="o">,</span> <span class="n">none</span><span class="o">),</span>
  <span class="n">step</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">fn</span><span class="o">,</span>
  <span class="n">do</span> <span class="n">fn&#39;</span> <span class="err">←</span> <span class="n">vm</span><span class="bp">.</span><span class="n">curr_fn</span><span class="o">,</span>
     <span class="n">n&#39;</span> <span class="err">←</span> <span class="n">vm</span><span class="bp">.</span><span class="n">call_stack_size</span><span class="o">,</span>
     <span class="n">when</span> <span class="o">(</span><span class="n">fn</span> <span class="bp">≠</span> <span class="o">(</span><span class="n">n&#39;</span><span class="o">,</span><span class="n">some</span> <span class="n">fn&#39;</span><span class="o">))</span> <span class="err">$</span> <span class="n">vm</span><span class="bp">.</span><span class="n">trace</span> <span class="err">$</span> <span class="o">(</span><span class="n">string</span><span class="bp">.</span><span class="n">join</span> <span class="err">$</span> <span class="n">list</span><span class="bp">.</span><span class="n">repeat</span> <span class="s2">&quot;| &quot;</span> <span class="n">n&#39;</span><span class="o">)</span> <span class="bp">++</span> <span class="n">to_string</span> <span class="n">fn&#39;</span><span class="o">,</span>
     <span class="n">pure</span> <span class="o">(</span><span class="n">n&#39;</span><span class="o">,</span><span class="n">fn&#39;</span><span class="o">)</span> <span class="o">}</span>
</pre></div>


{% endraw %}
