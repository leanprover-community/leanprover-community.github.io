---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/61040CPDTParserinLean.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [CPDT Parser in Lean](https://leanprover-community.github.io/archive/113488general/61040CPDTParserinLean.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Jun 09 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127822804):
<p>My son got interested in parsers and I'm trying to understand them better by implementing the simple parser at the beginning of Certified Programming with Dependent Types. But actually I find making these inductive types quite hard -- in my area of expertise we don't really ever use complicated inductive structures like the ones showing up in these parsers. Here's an example of one I'm struggling with: in Coq it's</p>

#### [ Kevin Buzzard (Jun 09 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127822805):
<div class="codehilite"><pre><span></span>Fixpoint progDenote (p : prog) (s : stack) : option stack :=
match p with
| nil ⇒ Some s
| i :: p’ ⇒
match instrDenote i s with
| None ⇒ None
| Some s’ ⇒ progDenote p’ s’
end
end.
</pre></div>

#### [ Kevin Buzzard (Jun 09 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127822809):
<p><a href="http://adam.chlipala.net/cpdt/cpdt.pdf" target="_blank" title="http://adam.chlipala.net/cpdt/cpdt.pdf">http://adam.chlipala.net/cpdt/cpdt.pdf</a></p>

#### [ Kevin Buzzard (Jun 09 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127822814):
<p>page 21</p>

#### [ Kevin Buzzard (Jun 09 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127822933):
<p>I tried writing it by hand with <code>list.rec_on</code> (<code>prog := list instr</code>) but I seemed to end up knowing <code>progDenote p' s</code> rather than <code>progDenote p' s'</code>. Presumably this is the sort of thing the equation compiler can do for me somehow? Or is there some complicated issue which makes this definition problematic? I know very little about this sort of stuff beyond <code>rec</code>.</p>

#### [ Kevin Buzzard (Jun 09 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127822935):
<p>Oh I see now, I should somehow carry s around as a parameter</p>

#### [ Simon Hudon (Jun 09 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127822977):
<p>Do you also have the definition of <code>stack</code>?</p>

#### [ Kevin Buzzard (Jun 09 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823139):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">progDenote</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">prog</span><span class="o">)</span> <span class="o">:</span> <span class="n">stack</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">stack</span> <span class="o">:=</span>
<span class="n">list</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">p</span> <span class="n">some</span> <span class="err">$</span>
  <span class="bp">λ</span> <span class="n">i</span> <span class="n">p&#39;</span> <span class="n">pDp&#39;</span> <span class="n">s</span><span class="o">,</span><span class="n">option</span><span class="bp">.</span><span class="n">rec_on</span> <span class="o">(</span><span class="n">instrDenote</span> <span class="n">i</span> <span class="n">s</span><span class="o">)</span> <span class="n">none</span> <span class="n">pDp&#39;</span>
</pre></div>

#### [ Kevin Buzzard (Jun 09 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823140):
<p>So I can just do it in term mode</p>

#### [ Kevin Buzzard (Jun 09 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823192):
<p>I am slightly unnerved by how incomprehensible mine looks compared to Chlipata's</p>

#### [ Kevin Buzzard (Jun 09 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823199):
<p><code>definition stack := list ℕ</code></p>

#### [ Kevin Buzzard (Jun 09 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823252):
<p>you can plough through <a href="http://adam.chlipala.net/cpdt/html/Cpdt.StackMachine.html" target="_blank" title="http://adam.chlipala.net/cpdt/html/Cpdt.StackMachine.html">http://adam.chlipala.net/cpdt/html/Cpdt.StackMachine.html</a> to find these. I see my error now -- I should have been inducting on p before introducing s. These are subtleties I don't usually run into in my area of mathematics, you rarely induct on something other than nat</p>

#### [ Simon Hudon (Jun 09 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823257):
<p>You can also write it:</p>
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">progDenote</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">prog</span><span class="o">)</span> <span class="o">:</span> <span class="n">stack</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">stack</span>
 <span class="bp">|</span> <span class="o">[]</span> <span class="o">:=</span> <span class="bp">...</span>
 <span class="bp">|</span> <span class="o">(</span><span class="n">s</span> <span class="bp">::</span> <span class="n">ss</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">...</span>
</pre></div>

#### [ Simon Hudon (Jun 09 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823260):
<p>Which I find prettier than Coq</p>

#### [ Simon Hudon (Jun 09 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823364):
<p>Sorry, I should write:</p>
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">progDenote</span> <span class="o">:</span> <span class="n">prog</span>  <span class="bp">→</span> <span class="n">stack</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">stack</span>
 <span class="bp">|</span> <span class="o">[]</span> <span class="n">s</span> <span class="o">:=</span> <span class="n">some</span> <span class="n">s</span>
 <span class="bp">|</span> <span class="o">(</span><span class="n">p</span> <span class="bp">::</span> <span class="n">ps</span><span class="o">)</span> <span class="n">s</span> <span class="o">:=</span> <span class="n">instrDenote</span> <span class="n">p</span> <span class="n">s</span> <span class="bp">&gt;&gt;=</span> <span class="n">progDenote</span> <span class="n">ps</span>
</pre></div>

#### [ Kevin Buzzard (Jun 09 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823365):
<p>Oh thanks!</p>

#### [ Kevin Buzzard (Jun 09 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823369):
<p>I was just working on this myself but I'm not sure I would have hit upon that crazy smiley thing</p>

#### [ Simon Hudon (Jun 09 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823370):
<p>is <code>&gt;&gt;=</code> the smiley? :)</p>

#### [ Kevin Buzzard (Jun 09 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823419):
<p>I guess he looks pretty sad :-/</p>

#### [ Simon Hudon (Jun 09 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823468):
<p>Or angry? I see <code>&gt;&gt;</code> as eyebrows and <code>=</code> as a nose</p>

#### [ Kevin Buzzard (Jun 09 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823527):
<p>OK here's my effort:</p>

#### [ Kevin Buzzard (Jun 09 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823530):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">progDenote&#39;</span> <span class="o">:</span> <span class="n">prog</span> <span class="bp">→</span> <span class="n">stack</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">stack</span>
<span class="bp">|</span> <span class="o">([])</span> <span class="o">:=</span> <span class="n">some</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">i</span> <span class="bp">::</span> <span class="n">p&#39;</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">s</span><span class="o">,</span> <span class="k">match</span> <span class="o">(</span><span class="n">instrDenote</span> <span class="n">i</span> <span class="n">s</span><span class="o">)</span> <span class="k">with</span>
  <span class="bp">|</span> <span class="n">none</span> <span class="o">:=</span> <span class="n">none</span>
  <span class="bp">|</span> <span class="n">some</span> <span class="n">s&#39;</span> <span class="o">:=</span> <span class="n">progDenote&#39;</span> <span class="n">p&#39;</span> <span class="n">s&#39;</span>
  <span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Jun 09 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823537):
<p>So you are doing the match with this crazy smiley?</p>

#### [ Kevin Buzzard (Jun 09 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823571):
<p>I can see that your <code>progDenote ps</code> is my <code>progDenote p'</code> and then other than that I am sending <code>none</code> to <code>none</code> and <code>s'</code> to <code>s'</code>. You're exploiting this in some way?</p>

#### [ Kevin Buzzard (Jun 09 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823587):
<p>PS <span class="user-mention" data-user-id="110026">@Simon Hudon</span> I felt quite bad a week or so ago when I was trying to write some notation and didn't understand binding powers and was in a rush and you tried to explain them and I just said <code>just gimme the number!</code></p>

#### [ Simon Hudon (Jun 09 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823589):
<p>Yes, with option, <code>&gt;&gt;=</code> returns <code>none</code> if either of its parameters does</p>

#### [ Kevin Buzzard (Jun 09 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823590):
<p>It was partially because of that incident that I thought it was time to learn about parsers!</p>

#### [ Kevin Buzzard (Jun 09 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823635):
<p>Aah I see you're explictly utilising the fact that it's a monad?</p>

#### [ Simon Hudon (Jun 09 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823640):
<p>No worries, I got that you were in a rush. And I know I'd always prefer to get deeper into it. But thanks for coming back to it :)</p>

#### [ Simon Hudon (Jun 09 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823641):
<p>Exactly!</p>

#### [ Simon Hudon (Jun 09 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823688):
<p>In Coq, he'd have to do some work to bring that in but it's just there for us in Lean so it's good to get used to it</p>

#### [ Simon Hudon (Jun 09 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823993):
<p>The operators are a bit broken but in Haskell, I'd rather write <code>progDenote ps =&lt;&lt; instrDenote p s</code>. It's a bit like function application with monads (you apply <code>progDenote ps</code> to the result of <code>instrDenote p s</code>)</p>

#### [ Kevin Buzzard (Jun 09 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127824101):
<p>I have my compiler working now and I'd like to do some unit tests using <code>#eval</code>. This means as far as I can see that I have to go and define a bunch of <code>has_repr</code> instances.</p>

#### [ Kevin Buzzard (Jun 09 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127824102):
<p>Here's one:</p>

#### [ Kevin Buzzard (Jun 09 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127824110):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">binop</span>
<span class="bp">|</span> <span class="n">Plus</span> <span class="o">:</span> <span class="n">binop</span>
<span class="bp">|</span> <span class="n">Times</span> <span class="o">:</span> <span class="n">binop</span>

<span class="kn">open</span> <span class="n">binop</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_repr</span> <span class="n">binop</span> <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="n">b</span><span class="o">,</span> <span class="k">match</span> <span class="n">b</span> <span class="k">with</span>
    <span class="bp">|</span> <span class="n">Plus</span> <span class="o">:=</span> <span class="s2">&quot;add&quot;</span>
    <span class="bp">|</span> <span class="n">Times</span> <span class="o">:=</span> <span class="s2">&quot;mul&quot;</span>
    <span class="kn">end</span>
<span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (Jun 09 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127824112):
<p>I just wanted to write</p>

#### [ Kevin Buzzard (Jun 09 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127824115):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_repr</span> <span class="n">binop</span> <span class="o">:=</span> <span class="bp">⟨</span>
    <span class="bp">|</span> <span class="n">Plus</span> <span class="o">:=</span> <span class="s2">&quot;add&quot;</span>
    <span class="bp">|</span> <span class="n">Times</span> <span class="o">:=</span> <span class="s2">&quot;mul&quot;</span>
    <span class="kn">end</span>
<span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (Jun 09 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127824116):
<p>but that didn't work so I had to put all the match waffle in. Am I missing something?</p>

#### [ Simon Hudon (Jun 09 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127824169):
<p>No I think that's the way to do it. I was looking to see if it could be generated for you but I haven't found tactics for that</p>


{% endraw %}
