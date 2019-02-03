---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/65569Productmetaprogram.html
---

## Stream: [new members](index.html)
### Topic: [Product meta program](65569Productmetaprogram.html)

---


{% raw %}
#### [ Ken Roe (Jul 29 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130535258):
<p>Here is a simple meta program to simplify a product expression.  It does not seem to match anything.  Can someone explain what is happening?</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">simplifyProd</span> <span class="o">:</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">expr</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">app</span>
    <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">app</span>
      <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">app</span> <span class="bp">`</span><span class="o">(</span><span class="n">prod</span><span class="bp">.</span><span class="n">fst</span><span class="o">)</span> <span class="n">tt1a</span><span class="o">)</span>
      <span class="n">tt1b</span><span class="o">)</span>
     <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">app</span>
        <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">app</span>
          <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">app</span>
            <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">app</span> <span class="bp">`</span><span class="o">(</span><span class="n">prod</span><span class="bp">.</span><span class="n">mk</span><span class="o">)</span> <span class="n">tt1</span><span class="o">)</span> <span class="n">tt2</span><span class="o">)</span> <span class="n">a</span><span class="o">)</span> <span class="n">b</span><span class="o">))</span> <span class="o">:=</span> <span class="n">a</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">app</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">:=</span> <span class="n">expr</span><span class="bp">.</span><span class="n">app</span> <span class="o">(</span><span class="n">simplifyProd</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">simplifyProd</span> <span class="n">b</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">lam</span> <span class="n">v</span> <span class="n">b</span> <span class="n">t</span> <span class="n">e</span><span class="o">)</span> <span class="o">:=</span> <span class="n">expr</span><span class="bp">.</span><span class="n">lam</span> <span class="n">v</span> <span class="n">b</span> <span class="o">(</span><span class="n">simplifyProd</span> <span class="n">t</span><span class="o">)</span> <span class="o">(</span><span class="n">simplifyProd</span> <span class="n">e</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">pi</span> <span class="n">v</span> <span class="n">b</span> <span class="n">t</span> <span class="n">e</span><span class="o">)</span> <span class="o">:=</span> <span class="n">expr</span><span class="bp">.</span><span class="n">pi</span> <span class="n">v</span> <span class="n">b</span> <span class="o">(</span><span class="n">simplifyProd</span> <span class="n">t</span><span class="o">)</span> <span class="o">(</span><span class="n">simplifyProd</span> <span class="n">e</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">x</span>

<span class="kn">theorem</span> <span class="n">testit</span> <span class="o">(</span><span class="n">f</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span>
    <span class="o">(</span><span class="n">f</span><span class="o">,</span><span class="n">s</span><span class="o">)</span><span class="bp">.</span><span class="n">fst</span><span class="bp">=</span><span class="n">f</span> <span class="o">:=</span>
<span class="k">begin</span>
   <span class="n">do</span> <span class="o">{</span>
       <span class="n">t</span> <span class="err">←</span> <span class="n">target</span><span class="o">,</span>
       <span class="n">trace</span> <span class="s2">&quot;Start&quot;</span><span class="o">,</span>
       <span class="n">trace</span> <span class="n">t</span><span class="bp">.</span><span class="n">to_raw_fmt</span><span class="o">,</span>
       <span class="n">tq</span> <span class="err">←</span> <span class="n">some</span> <span class="o">(</span><span class="n">simplifyProd</span> <span class="n">t</span><span class="o">),</span>
       <span class="n">trace</span> <span class="n">tq</span><span class="bp">.</span><span class="n">to_raw_fmt</span><span class="o">,</span>
       <span class="n">change</span> <span class="n">tq</span>
   <span class="o">},</span>
   <span class="n">refl</span>
<span class="kn">end</span>
</pre></div>

#### [ Reid Barton (Jul 29 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130536744):
<p>Well, I don't know, but replacing the first case with <code>| `(prod.fst (prod.mk %%a %%b)) := a</code> works.<br>
Maybe something involving universe variables?</p>

#### [ Kevin Buzzard (Jul 29 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130536883):
<p><span class="user-mention" data-user-id="121304">@Ken Roe</span> Just to let you know that probably nobody is reading the Lean bug reports. The developers are working on Lean 4 and anything that isn't obviously a serious issue in 3.4.1 which needs addressing (e.g. a proof of false) is very likely to be ignored.</p>

#### [ Ken Roe (Jul 29 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130540273):
<p>Actually, `(prod.fst (<a href="http://prod.mk" target="_blank" title="http://prod.mk">prod.mk</a> %%a %%b)) probably works but I'm trying to avoid quoting.  I doing pattern matching that is breaking apart \lambda expressions and I found that %%x inside a lambda lifts the variables (which I would like to avoid).  I've also been running into type checking issues.  If people are interested, I can post more cases illustrating more issues.</p>
<p>Right now, I'm pretty frustrated.  I'm trying to build a separation logic using Lean.  Right now, all paths to building the necessary tactics are blocked due to missing documentation or bugs.</p>

#### [ Patrick Massot (Jul 29 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130540874):
<p>You should talk to Simon, he knows both tactics and separation logic in Lean</p>

#### [ Simon Hudon (Jul 29 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130540986):
<p>If you want, I have started on a separation logic package: <a href="https://github.com/unitb/separation-logic" target="_blank" title="https://github.com/unitb/separation-logic">https://github.com/unitb/separation-logic</a>. It might be easier to collaborate on it.</p>

#### [ Simon Hudon (Jul 29 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130541039):
<p>So far, my tactics can handle a twenty-line proof of the list reversal program: <a href="https://github.com/unitb/separation-logic/blob/master/src/separation/examples.lean#L118-L137" target="_blank" title="https://github.com/unitb/separation-logic/blob/master/src/separation/examples.lean#L118-L137">https://github.com/unitb/separation-logic/blob/master/src/separation/examples.lean#L118-L137</a></p>

#### [ Ken Roe (Jul 29 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130541248):
<p>Can someone send me a private message with Simon's contact information?  By the way, to illustrate another issue, I just added another case which causes simplifyProd to not compile.</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">simplifyProd</span> <span class="o">:</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">expr</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">app</span>
    <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">app</span>
      <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">app</span> <span class="bp">`</span><span class="o">(</span><span class="n">prod</span><span class="bp">.</span><span class="n">fst</span><span class="o">)</span> <span class="n">tt1a</span><span class="o">)</span>
      <span class="n">tt1b</span><span class="o">)</span>
     <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">app</span>
        <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">app</span>
          <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">app</span>
            <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">app</span> <span class="bp">`</span><span class="o">(</span><span class="n">prod</span><span class="bp">.</span><span class="n">mk</span><span class="o">)</span> <span class="n">tt1</span><span class="o">)</span> <span class="n">tt2</span><span class="o">)</span> <span class="n">a</span><span class="o">)</span> <span class="n">b</span><span class="o">))</span> <span class="o">:=</span> <span class="n">a</span>
<span class="bp">|</span> <span class="bp">`</span><span class="o">((</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="o">(</span><span class="err">%%</span><span class="n">f</span><span class="o">)</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="err">%%</span><span class="n">z</span><span class="o">))</span> <span class="o">:=</span> <span class="bp">`</span><span class="o">(</span><span class="err">%%</span><span class="n">f</span> <span class="o">(</span><span class="err">%%</span><span class="n">z</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">app</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">:=</span> <span class="n">expr</span><span class="bp">.</span><span class="n">app</span> <span class="o">(</span><span class="n">simplifyProd</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">simplifyProd</span> <span class="n">b</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">lam</span> <span class="n">v</span> <span class="n">b</span> <span class="n">t</span> <span class="n">e</span><span class="o">)</span> <span class="o">:=</span> <span class="n">expr</span><span class="bp">.</span><span class="n">lam</span> <span class="n">v</span> <span class="n">b</span> <span class="o">(</span><span class="n">simplifyProd</span> <span class="n">t</span><span class="o">)</span> <span class="o">(</span><span class="n">simplifyProd</span> <span class="n">e</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">pi</span> <span class="n">v</span> <span class="n">b</span> <span class="n">t</span> <span class="n">e</span><span class="o">)</span> <span class="o">:=</span> <span class="n">expr</span><span class="bp">.</span><span class="n">pi</span> <span class="n">v</span> <span class="n">b</span> <span class="o">(</span><span class="n">simplifyProd</span> <span class="n">t</span><span class="o">)</span> <span class="o">(</span><span class="n">simplifyProd</span> <span class="n">e</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">x</span>

<span class="kn">theorem</span> <span class="n">testit</span> <span class="o">(</span><span class="n">f</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span>
    <span class="o">(</span><span class="n">f</span><span class="o">,</span><span class="n">s</span><span class="o">)</span><span class="bp">.</span><span class="n">fst</span><span class="bp">=</span><span class="n">f</span> <span class="o">:=</span>
<span class="k">begin</span>
   <span class="n">do</span> <span class="o">{</span>
       <span class="n">t</span> <span class="err">←</span> <span class="n">target</span><span class="o">,</span>
       <span class="n">trace</span> <span class="s2">&quot;Start&quot;</span><span class="o">,</span>
       <span class="n">trace</span> <span class="n">t</span><span class="bp">.</span><span class="n">to_raw_fmt</span><span class="o">,</span>
       <span class="n">tq</span> <span class="err">←</span> <span class="n">some</span> <span class="o">(</span><span class="n">simplifyProd</span> <span class="n">t</span><span class="o">),</span>
       <span class="n">trace</span> <span class="n">tq</span><span class="bp">.</span><span class="n">to_raw_fmt</span><span class="o">,</span>
       <span class="n">change</span> <span class="n">tq</span>
   <span class="o">},</span>
   <span class="n">refl</span>
<span class="kn">end</span>
</pre></div>


<p>This case with the lambda gives the following error on the %%f:</p>
<div class="codehilite"><pre><span></span><span class="n">function</span> <span class="n">expected</span> <span class="n">at</span>
  <span class="bp">_</span><span class="n">x_1</span>
<span class="n">term</span> <span class="n">has</span> <span class="n">type</span>
  <span class="err">?</span><span class="n">m_1</span>
</pre></div>

#### [ Patrick Massot (Jul 29 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130541265):
<p>you can click on his name, right above your question</p>

#### [ Patrick Massot (Jul 29 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130541304):
<p>I mean: right above in this thread</p>

#### [ Ken Roe (Jul 29 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130541312):
<p>Never mind on the contact info--I just saw a message from Simon. </p>
<p>I'm more than happy to collaborate on separation logic.  I did work on separation logic using Coq for my PhD.  You can check out my home page at <a href="http://www.cs.jhu.edu/~roe" target="_blank" title="http://www.cs.jhu.edu/~roe">www.cs.jhu.edu/~roe</a>.  I'm working on porting my system to Lean.</p>

#### [ Simon Hudon (Jul 29 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130541412):
<p>Cool thanks, that should be helpful. You can have a look at how far I got right here: <a href="#narrow/stream/113489-new-members/subject/Product.20meta.20program/near/130540986" title="#narrow/stream/113489-new-members/subject/Product.20meta.20program/near/130540986">https://leanprover.zulipchat.com/#narrow/stream/113489-new-members/subject/Product.20meta.20program/near/130540986</a></p>

#### [ Ken Roe (Jul 30 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130597942):
<p>Actually, an ideal solution would be not to use `(<a href="http://prod.mk" target="_blank" title="http://prod.mk">prod.mk</a>).   Is there an alternative that I can plug in without changing the surrounding text?  I would like to find a way of expression my product meta program without using any back quote annotations.  The motivation is that I actually have some more complex meta programs where I'm finding the back quote notation has semantics that is causing a number of problems.</p>

#### [ Simon Hudon (Jul 30 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130598427):
<p>Can you show us that other program?</p>

#### [ Ken Roe (Jul 30 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130606073):
<p>I'll put it up in a day or two.  The code isn't stand alone.  It is dependent on the infrastructure in my separation logic framework.  I need to put the work into a github repository and then post the critical meta functions.</p>

#### [ Ken Roe (Aug 06 2018 at 05:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130956238):
<p>I've posted the source code that I have of my separation framework so far here: <a href="https://github.com/kendroe/pedantic2" target="_blank" title="https://github.com/kendroe/pedantic2">https://github.com/kendroe/pedantic2</a>.  Some of my future questions will point to this repository.  I'm porting the Coq implementation.  Information on this implementation (and repository link) can be found here: <a href="http://www.cs.jhu.edu/~roe" target="_blank" title="http://www.cs.jhu.edu/~roe">http://www.cs.jhu.edu/~roe</a>.</p>


{% endraw %}
