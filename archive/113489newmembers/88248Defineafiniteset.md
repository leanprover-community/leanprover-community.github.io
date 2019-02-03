---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/88248Defineafiniteset.html
---

## Stream: [new members](index.html)
### Topic: [Define a finite set](88248Defineafiniteset.html)

---


{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Oct 15 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135797911):
<p>How do I define a finite set only giving information of its cardinality? I'd like to define something like this:</p>
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">S&#39;</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span>
<span class="bp">|</span> <span class="n">card</span> <span class="o">:</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="n">S&#39;</span> <span class="bp">=</span> <span class="mi">2</span>
</pre></div>


<p>(once again nonsense, but a sketch of what I want to define)</p>

#### [ Bryan Gin-ge Chen (Oct 15 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135797918):
<p><code>finset.range</code> ?</p>

#### [ Bryan Gin-ge Chen (Oct 15 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135797927):
<p>oh you want a fintype, then try <code>fin</code></p>

#### [ Kevin Buzzard (Oct 15 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135799298):
<p>Do you mean a finite type?</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 15 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135815346):
<p>You mean <code>def S' : Type := fin 2</code>? That does seem to work.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 15 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135815375):
<blockquote>
<p>Do you mean a finite type?</p>
</blockquote>
<p>Oh, right, set only refers to subsets. I forgot.</p>

#### [ Kenny Lau (Oct 15 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135815434):
<p>I don’t think we understood this question</p>

#### [ Kevin Buzzard (Oct 15 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135831206):
<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> <code>fin 2</code> is a type. There are exactly two distinct terms of that type. The terms are rather a mouthful to describe: </p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">2</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">dec_trivial</span><span class="bp">⟩</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">2</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">dec_trivial</span><span class="bp">⟩</span>
</pre></div>


<p>There's another type called <code>bool</code> which also has exactly two terms. Type <code>#check bool</code> and right-click on <code>bool</code>and select "go to definition" to see it. The definition is completely different to <code>fin</code>. The two terms of type <code>bool</code> are <code>tt</code> and <code>ff</code>. These types <code>bool</code> and <code>fin 2</code> are not <em>equal</em>, but there is a map from <code>bool</code> to <code>fin 2</code> which is a bijection, and which you can define using the equation compiler (pattern matching).</p>
<p>Exercise 1: <code>def f : bool → fin 2</code>. Define a function from <code>bool</code> to <code>fin 2</code> which you can prove (in maths, not in Lean) is a bijection.</p>
<p>Exercise 2: fill in the sorry.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span><span class="bp">.</span><span class="n">basic</span>

<span class="n">def</span> <span class="n">X</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">bool</span> <span class="err">$</span> <span class="n">fin</span> <span class="mi">2</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>Exercise 3: find the library function which turns <code>X</code> into a proof that <code>f</code> is a bijection. Hint: which namespace do you think that function would be in?</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">function</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">bijective</span> <span class="n">f</span> <span class="o">:=</span> <span class="bp">&lt;</span><span class="n">FILL</span> <span class="n">IN</span> <span class="n">FUNCTION</span> <span class="n">NAME</span><span class="bp">&gt;</span> <span class="n">X</span>
</pre></div>

#### [ Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135858585):
<blockquote>
<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> <code>fin 2</code> is a type. There are exactly two distinct terms of that type. The terms are rather a mouthful to describe: </p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">2</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">dec_trivial</span><span class="bp">⟩</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">2</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">dec_trivial</span><span class="bp">⟩</span>
</pre></div>


<p>There's another type called <code>bool</code> which also has exactly two terms. Type <code>#check bool</code> and right-click on <code>bool</code>and select "go to definition" to see it. The definition is completely different to <code>fin</code>. The two terms of type <code>bool</code> are <code>tt</code> and <code>ff</code>. These types <code>bool</code> and <code>fin 2</code> are not <em>equal</em>, but there is a map from <code>bool</code> to <code>fin 2</code> which is a bijection, and which you can define using the equation compiler (pattern matching).</p>
<p>Exercise 1: <code>def f : bool → fin 2</code>. Define a function from <code>bool</code> to <code>fin 2</code> which you can prove (in maths, not in Lean) is a bijection.</p>
<p>Exercise 2: fill in the sorry.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span><span class="bp">.</span><span class="n">basic</span>

<span class="n">def</span> <span class="n">X</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">bool</span> <span class="err">$</span> <span class="n">fin</span> <span class="mi">2</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>Exercise 3: find the library function which turns <code>X</code> into a proof that <code>f</code> is a bijection. Hint: which namespace do you think that function would be in?</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">function</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">bijective</span> <span class="n">f</span> <span class="o">:=</span> <span class="bp">&lt;</span><span class="n">FILL</span> <span class="n">IN</span> <span class="n">FUNCTION</span> <span class="n">NAME</span><span class="bp">&gt;</span> <span class="n">X</span>
</pre></div>


</blockquote>
<p>One more question: is there any way to use statements like "x is either the first element of fin 2 or the second element" directly without bijecting to bool?</p>

#### [ Kenny Lau (Oct 15 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135858626):
<p>by "use" do you mean "proof"?</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135858645):
<blockquote>
<p>by "use" do you mean "proof"?</p>
</blockquote>
<p>Either a proof or an existing lemma.</p>

#### [ Kenny Lau (Oct 15 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135858653):
<p>dec_trivial</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135858776):
<blockquote>
<p>dec_trivial</p>
</blockquote>
<p>Oh ok -- how would I actually denote "the first element of fin 2" and "the second element of fin 2" in such a statement? Just putting down the explicit form (like <code>⟨(0 : ℕ), dec_trivial⟩</code>) gives errors.</p>

#### [ Kenny Lau (Oct 15 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135858791):
<p>0 and 1</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135858861):
<blockquote>
<p>0 and 1</p>
</blockquote>
<p>Wait, don't I need to do x.val, y.val for that? or do just x and y also take the values 0 and 1? (where <code>x y : fin 2</code>). I was under the impression that <code>.val</code> indexes the elements as 0 and 1 but the elements themselves are left abstract.</p>

#### [ Kenny Lau (Oct 15 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135858962):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">2</span><span class="o">,</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">∨</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">dec_trivial</span>
</pre></div>

#### [ Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135859021):
<p>Oh ok -- what's the point of <code>x.val</code>, then?</p>

#### [ Kenny Lau (Oct 15 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135859126):
<p>that 0 is of type <code>fin 2</code></p>

#### [ Chris Hughes (Oct 15 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135859183):
<p>for any n, <code>fin (succ n)</code> has <code>0</code> defined on it in the obvious way, and any other numeral <code>x</code> is just <code>\&lt; x % succ n, proof\&gt;</code>. <code>val</code> is a function <code>fin n -&gt; nat</code>, so it's useful whenever you want to turn something of type <code>fin n</code> into something of type <code>nat</code>.</p>

#### [ Kenny Lau (Oct 15 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135859184):
<p>you can also write:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">2</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="n">val</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">∨</span> <span class="n">x</span><span class="bp">.</span><span class="n">val</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">dec_trivial</span>
</pre></div>

#### [ Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135859198):
<blockquote>
<p>for any n, <code>fin (succ n)</code> has <code>0</code> defined on it in the obvious way, and any other numeral <code>x</code> is just <code>\&lt; x % succ n, proof\&gt;</code>. <code>val</code> is a function <code>fin n -&gt; nat</code>, so it's useful whenever you want to turn something of type <code>fin n</code> into something of type <code>nat</code>.</p>
</blockquote>
<p>So it's like a coercion?</p>

#### [ Chris Hughes (Oct 15 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135859207):
<p>Yes.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135859412):
<p>Thanks. I was proving that if there are three elements in fin 2, two of them must be equal -- I was trying some insanely long (relative to the triviality of the statement) proof by contradiction, ordering the elements and showing that the largest of the three will be above fin.last. Now it's easy.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135859602):
<p>By the way, does dec_trivial behave differently in term mode and tactic mode? The statement <code>have H01 : ∀ s : fin 2, s = 0 ∨ s = 1 := dec_trivial</code> works, but <code>have H01 : ∀ s : fin 2, s = 0 ∨ s = 1, exact dec_trivial,</code> doesn't.</p>

#### [ Kenny Lau (Oct 15 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135859712):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">H01</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">s</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">2</span><span class="o">,</span> <span class="n">s</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">∨</span> <span class="n">s</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">,</span> <span class="k">from</span> <span class="n">dec_trivial</span><span class="o">,</span>
<span class="n">trivial</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">H01</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">s</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">2</span><span class="o">,</span> <span class="n">s</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">∨</span> <span class="n">s</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">,</span> <span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">,</span>
  <span class="n">trivial</span>
<span class="kn">end</span>
</pre></div>

#### [ Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135859931):
<p>Weird, that doesn't work for my theorem. I'll post my code, one second.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135860017):
<p>Or maybe it does.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135860103):
<p>Ok yeah it does.</p>

#### [ Chris Hughes (Oct 15 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135860131):
<p>If you <code>intro s</code> it won't work.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135860946):
<p>I found my problem -- I have <code>local attribute [instance] classical.prop_decidable</code> in my code, which seems to interfere with <code>dec_trivial</code>.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861021):
<p>How do I define the scope of a local attribute so it applies only to the theorem it is intended for?</p>

#### [ Kevin Buzzard (Oct 15 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861033):
<blockquote>
<p>I found my problem -- I have <code>local attribute [instance] classical.prop_decidable</code> in my code, which seems to interfere with <code>dec_trivial</code>.</p>
</blockquote>
<p>Remember when I suggested that <code>local attribute [instance, priority 0] classical.prop_decidable</code> was better? It's for this sort of reason.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861043):
<p>You did? Whoops, I missed it.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861114):
<p>Yep, that works. Thanks.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 15 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861127):
<p>But in a general scenario, is <code>section</code> the only way to define the scope of local things?</p>

#### [ Kevin Buzzard (Oct 15 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861487):
<p><code>example (a b c : bool) : a = b ∨ b = c ∨ c = a := by cases a;cases b;cases c;simp </code></p>

#### [ Kevin Buzzard (Oct 15 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861551):
<p>This trick wouldn't work with <code>fin 2</code> though. Although maybe <span class="user-mention" data-user-id="110087">@Scott Morrison</span>  was recently talking about a tactic which enabled you to do cases on <code>fin n</code> somehow...</p>

#### [ Kevin Buzzard (Oct 15 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861572):
<p>To make the trick work with <code>fin 2</code> you would have to define your own recursor.</p>

#### [ Kenny Lau (Oct 15 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861604):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">bool</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">∨</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">c</span> <span class="bp">∨</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">a</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">dec_trivial</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span><span class="o">,</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">∨</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">c</span> <span class="bp">∨</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">a</span><span class="o">)</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span>
</pre></div>

#### [ Kevin Buzzard (Oct 16 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861698):
<p>How do you do it for <code>fin 2</code>?</p>

#### [ Kevin Buzzard (Oct 16 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861765):
<p>I am surprised your code works -- I would have guessed that <code>dec_trivial</code> would have complained that it did not know the type of anything before you fed <code>a b c</code> to it</p>

#### [ Kenny Lau (Oct 16 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861771):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">bool</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">∨</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">c</span> <span class="bp">∨</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">match</span> <span class="n">a</span><span class="o">,</span> <span class="n">b</span><span class="o">,</span> <span class="n">c</span> <span class="k">with</span>
<span class="bp">|</span> <span class="n">ff</span><span class="o">,</span> <span class="n">ff</span><span class="o">,</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="n">tt</span><span class="o">,</span> <span class="n">tt</span><span class="o">,</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="n">ff</span><span class="o">,</span> <span class="bp">_</span><span class="o">,</span> <span class="n">ff</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="n">rfl</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">tt</span><span class="o">,</span> <span class="bp">_</span><span class="o">,</span> <span class="n">tt</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="n">rfl</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">_</span><span class="o">,</span> <span class="n">ff</span><span class="o">,</span> <span class="n">ff</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">rfl</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">_</span><span class="o">,</span> <span class="n">tt</span><span class="o">,</span> <span class="n">tt</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">rfl</span><span class="o">)</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Oct 16 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861778):
<blockquote>
<p>How do you do it for <code>fin 2</code>?</p>
</blockquote>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">2</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">∨</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">c</span> <span class="bp">∨</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">a</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">dec_trivial</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span><span class="o">,</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">∨</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">c</span> <span class="bp">∨</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">a</span><span class="o">)</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span>
</pre></div>

#### [ Mario Carneiro (Oct 16 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135861986):
<blockquote>
<p>I am surprised your code works -- I would have guessed that dec_trivial would have complained that it did not know the type of anything before you fed a b c to it</p>
</blockquote>
<p>That's what the type ascription is for</p>

#### [ Scott Morrison (Oct 16 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135862313):
<p>The tactic Kevin mentioned above is in the PR <a href="https://github.com/leanprover/mathlib/issues/352" target="_blank" title="https://github.com/leanprover/mathlib/issues/352">#352</a>.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135862416):
<blockquote>
<blockquote>
<p>I am surprised your code works -- I would have guessed that dec_trivial would have complained that it did not know the type of anything before you fed a b c to it</p>
</blockquote>
<p>That's what the type ascription is for</p>
</blockquote>
<p>Lean can't work out the types of <code>a b c</code> when it has to check that <code>dec_trivial</code> is a term of that type, in my model of how it works. It must decide to wait a bit longer and hope it gets lucky.</p>

#### [ Kenny Lau (Oct 16 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135862435):
<blockquote>
<p>The tactic Kevin mentioned above is in the PR <a href="https://github.com/leanprover/mathlib/issues/352" target="_blank" title="https://github.com/leanprover/mathlib/issues/352">#352</a>.</p>
</blockquote>
<p>yeah but it ain't merged</p>

#### [ Kevin Buzzard (Oct 16 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135862505):
<p>Interestingly, this fails:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">bool</span><span class="o">,</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">∨</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">c</span> <span class="bp">∨</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">a</span>
<span class="bp">|</span> <span class="n">ff</span><span class="o">,</span> <span class="n">ff</span><span class="o">,</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="n">tt</span><span class="o">,</span> <span class="n">tt</span><span class="o">,</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="n">ff</span><span class="o">,</span> <span class="bp">_</span><span class="o">,</span> <span class="n">ff</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="n">rfl</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">tt</span><span class="o">,</span> <span class="bp">_</span><span class="o">,</span> <span class="n">tt</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="n">rfl</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">_</span><span class="o">,</span> <span class="n">ff</span><span class="o">,</span> <span class="n">ff</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">rfl</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">_</span><span class="o">,</span> <span class="n">tt</span><span class="o">,</span> <span class="n">tt</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">rfl</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Oct 16 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135862521):
<p>aah it's the commas I guess</p>

#### [ Kevin Buzzard (Oct 16 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135862583):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">bool</span><span class="o">,</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">∨</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">c</span> <span class="bp">∨</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">a</span>
<span class="bp">|</span> <span class="n">ff</span> <span class="n">ff</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="n">tt</span> <span class="n">tt</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="n">ff</span> <span class="bp">_</span> <span class="n">ff</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="n">rfl</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">tt</span> <span class="bp">_</span> <span class="n">tt</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="n">rfl</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="n">ff</span> <span class="n">ff</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">rfl</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="n">tt</span> <span class="n">tt</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">rfl</span><span class="o">)</span>
</pre></div>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135911890):
<blockquote>
<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> <code>fin 2</code> is a type. There are exactly two distinct terms of that type. The terms are rather a mouthful to describe: </p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">2</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">dec_trivial</span><span class="bp">⟩</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">2</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">dec_trivial</span><span class="bp">⟩</span>
</pre></div>


<p>There's another type called <code>bool</code> which also has exactly two terms. Type <code>#check bool</code> and right-click on <code>bool</code>and select "go to definition" to see it. The definition is completely different to <code>fin</code>. The two terms of type <code>bool</code> are <code>tt</code> and <code>ff</code>. These types <code>bool</code> and <code>fin 2</code> are not <em>equal</em>, but there is a map from <code>bool</code> to <code>fin 2</code> which is a bijection, and which you can define using the equation compiler (pattern matching).</p>
<p>Exercise 1: <code>def f : bool → fin 2</code>. Define a function from <code>bool</code> to <code>fin 2</code> which you can prove (in maths, not in Lean) is a bijection.</p>
<p>Exercise 2: fill in the sorry.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span><span class="bp">.</span><span class="n">basic</span>

<span class="n">def</span> <span class="n">X</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">bool</span> <span class="err">$</span> <span class="n">fin</span> <span class="mi">2</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>Exercise 3: find the library function which turns <code>X</code> into a proof that <code>f</code> is a bijection. Hint: which namespace do you think that function would be in?</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">function</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">bijective</span> <span class="n">f</span> <span class="o">:=</span> <span class="bp">&lt;</span><span class="n">FILL</span> <span class="n">IN</span> <span class="n">FUNCTION</span> <span class="n">NAME</span><span class="bp">&gt;</span> <span class="n">X</span>
</pre></div>


</blockquote>
<p>Exercise 1 is easy, it's just </p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">f</span> <span class="o">:</span> <span class="n">bool</span> <span class="bp">→</span> <span class="n">fin</span> <span class="mi">2</span> <span class="o">:=</span> <span class="k">begin</span> <span class="n">intro</span> <span class="n">x</span><span class="o">,</span> <span class="n">cases</span> <span class="n">x</span><span class="o">,</span> <span class="n">exact</span> <span class="mi">0</span><span class="o">,</span> <span class="n">exact</span> <span class="mi">1</span><span class="o">,</span> <span class="kn">end</span>
</pre></div>


<p>But I have no clue as to how to even start exercise 2. Is there a library command that helps you prove the isomorphism?</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912162):
<p>Do you know how to build terms whose type is a structure using <code>{</code> <code>}</code>?</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912238):
<p>No, I'm not even sure what a structure is.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912269):
<p>A structure is just an inductive type which only has one constructor.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912280):
<p>So non-examples are things like <code>nat</code> and <code>bool</code>.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912327):
<p>But an example would be something like <code>and P Q</code>.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912357):
<p>Wait, can't <code>and P Q</code> be considered a pi type?</p>

#### [ Kenny Lau (Oct 16 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912372):
<p>it's a sigma type</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912377):
<p>Since it's a function of two propositions?</p>

#### [ Kenny Lau (Oct 16 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912382):
<p><code>and</code> is a pi type</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912396):
<p>Ok, sure, then how is it an inductive type? ("A structure is just an inductive type...")</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912411):
<p>There's only one way you can build a term of type <code>and P Q</code> -- you have to supply a proof of <code>P</code> and a proof of <code>Q</code>. So this gives us the possibility of having a second piece of notation for defining terms of type <code>and P Q</code> where we say we're making something of type <code>and P Q</code> and then just supply the proofs of <code>P</code> and <code>Q</code></p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912452):
<p>I said <code>and P Q</code> is an inductive type, not <code>and</code></p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912474):
<p>Oh ok sure, that makes sense.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912484):
<p>But I'm still not sure what that has to do with inductive types.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912493):
<p><code>example (P Q : Prop) : and P Q := {}</code></p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912521):
<p>If you type that, you get a red underline under the squiggly bracket -- this can't work currently, because we didn't supply proofs of P and Q. But the <code>{}</code> notation is clue to a new way of defining a term of type <code>and P Q</code></p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912580):
<p>And the error is interesting -- Lean complains that some fields are missing.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912589):
<p>I tried supplying the proofs, still doesn't work.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912602):
<p><code>example (P Q : Prop) (HP : P) (HQ : Q) : and P Q := {HP HQ}</code></p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912617):
<p>function expected at<br>
  HP<br>
term has type<br>
  P</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912634):
<p>You have to know how to supply them.</p>

#### [ Chris Hughes (Oct 16 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912641):
<p><code>example (P Q : Prop) (HP : P) (HQ : Q) : and P Q := { left := HP, right := HQ}</code> is the syntax I think.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912649):
<p>right</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912709):
<p>Oh ok, so it's just standard left and right in term mode.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912726):
<p>(But I don't know how to do exercise 2 in tactic mode either.)</p>

#### [ Reid Barton (Oct 16 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912735):
<p>It doesn't have anything to do with the <code>left</code> and <code>right</code> tactics if that's what you mean</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912753):
<p>Oh right, that's for <code>or</code> goals.</p>

#### [ Reid Barton (Oct 16 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912765):
<p>It's just that the fields of the structure <code>and P Q</code> happen to also be named <code>left</code> and <code>right</code> (I guess? I never knew this)</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912768):
<p>So you can start work on Q2 by doing this:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">X</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">bool</span> <span class="err">$</span> <span class="n">fin</span> <span class="mi">2</span> <span class="o">:=</span> <span class="o">{</span>
  <span class="n">to_fun</span> <span class="o">:=</span> <span class="n">f</span><span class="o">,</span>
  <span class="n">inv_fun</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">left_inv</span> <span class="o">:=</span> <span class="k">begin</span> <span class="n">sorry</span> <span class="kn">end</span><span class="o">,</span>
  <span class="n">right_inv</span> <span class="o">:=</span> <span class="k">begin</span> <span class="n">sorry</span> <span class="kn">end</span>
<span class="o">}</span>
</pre></div>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912786):
<p>Ah, I see.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912787):
<p>I figured out the fields by writing <code>... := {}</code> and then looking at the errors.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912841):
<p>I knew the fields from the definition, but I didn't know how to supply them.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912862):
<p>If you replace <code>inv_fun := sorry</code> with <code>inv_fun := _</code> and look at the error, you'll see that <code>inv_fun</code> is supposed to be the inverse map from <code>fin 2</code> back to <code>bool</code>. So you could define that outside, like you did with <code>f</code></p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135912885):
<p>The two remaining fields are the proofs that the compositions in both directions are the identity. Of course both proofs are "just unravel everything" but I think it's quite good fun trying to work out how to do this.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135913696):
<p>Ok, I'm defining <code>f_inv</code>, and I've gotten up to having <code>Hx01 : x = 0 ∨ x = 1</code>:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">f_inv</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">2</span> <span class="bp">→</span> <span class="n">bool</span> <span class="o">:=</span>
    <span class="k">begin</span>
        <span class="n">intro</span> <span class="n">x</span><span class="o">,</span>
        <span class="k">have</span> <span class="n">H01</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">s</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">2</span><span class="o">,</span> <span class="n">s</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">∨</span> <span class="n">s</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">,</span> <span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">,</span>
        <span class="k">have</span> <span class="n">Hx01</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">∨</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">,</span> <span class="n">exact</span> <span class="n">H01</span> <span class="n">x</span><span class="o">,</span>
        <span class="n">sorry</span><span class="o">,</span>
    <span class="kn">end</span>
</pre></div>


<p>But for some reason I can't do <code>cases Hx01</code>. I get <code>induction tactic failed, recursor 'or.dcases_on' can only eliminate into Prop</code> What's going on?</p>

#### [ Patrick Massot (Oct 16 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135913805):
<blockquote>
<p>I figured out the fields by writing <code>... := {}</code> and then looking at the errors.</p>
</blockquote>
<p>This is so September 2018...</p>

#### [ Patrick Massot (Oct 16 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135913874):
<p>Nowadays we type <code>{!}</code> and click on the light bulb (or Ctrl-.) and choose the relevant option from the menu (I don't have Lean to check right now)</p>

#### [ Kevin Buzzard (Oct 16 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135915076):
<p>I need to move with the times.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135915189):
<p>Abhi -- it's not a good idea to use tactics to define data. You can use tactics for the proof, but for the data you are better off using something like the equation compiler</p>

#### [ Kevin Buzzard (Oct 16 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135915333):
<p>But to answer your question about what's going on, the <code>cases</code> command runs the recursor for the type, and if you look at the definition of <code>or.rec</code> you'll see that it's only set up to spit out proofs, not data</p>

#### [ Kevin Buzzard (Oct 16 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135915359):
<p>I think I once knew a good reason for this</p>

#### [ Chris Hughes (Oct 16 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135915489):
<p>The iota reduction rule for <code>or</code>  would cause contradictions when both sides of the <code>or</code> were true if <code>or</code> could produce data.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135916915):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span>  Can you give an example?</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135917107):
<blockquote>
<p>Abhi -- it's not a good idea to use tactics to define data. You can use tactics for the proof, but for the data you are better off using something like the equation compiler</p>
</blockquote>
<p>I'm not sure how to. I mean, I tried to use the equation compiler to produce a definition for <code>f</code>, but all I could do is:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">f</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">bool</span><span class="o">):</span> <span class="n">fin</span> <span class="mi">2</span> <span class="o">:=</span>
    <span class="k">if</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">tt</span> <span class="k">then</span> <span class="mi">0</span> <span class="k">else</span> <span class="mi">1</span>
</pre></div>


<p>Which is only the value of <code>f</code>, not a function itself.</p>

#### [ Johan Commelin (Oct 16 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135917243):
<p>That did define a function <code>f</code>.</p>

#### [ Johan Commelin (Oct 16 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135917292):
<p>It is the same as</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">f</span> <span class="o">:</span> <span class="n">bool</span> <span class="bp">→</span> <span class="n">fin</span> <span class="mi">2</span> <span class="o">:=</span>
<span class="err">\</span><span class="n">lam</span> <span class="n">b</span><span class="o">,</span> <span class="k">if</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">tt</span> <span class="k">then</span> <span class="mi">0</span> <span class="k">else</span> <span class="mi">1</span>
</pre></div>

#### [ Chris Hughes (Oct 16 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135917376):
<p><code>def f (h : 1 = 1 ∨ 0 = 0) : ℕ := or.cases_on h (λ h, 0) (λ h, 1)</code>. The iota reduction rule says <code>f (or.inl rfl) = 0</code> and that <code>f (or.inr rfl) = 1)</code>, but since by proof irrelevance <code>or.inl rfl = or.inr rfl</code>, this would imply <code>0 = 1</code>, hence <code>or</code> cannot eliminate into data.</p>

#### [ Chris Hughes (Oct 16 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135917466):
<p>Here's your function defined using the equation compiler</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">f</span> <span class="o">:</span> <span class="n">bool</span> <span class="bp">→</span> <span class="n">fin</span> <span class="mi">2</span>
<span class="bp">|</span> <span class="n">tt</span> <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="n">ff</span> <span class="o">:=</span> <span class="mi">1</span>
</pre></div>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135917644):
<blockquote>
<p><code>def f (h : 1 = 1 ∨ 0 = 0) : ℕ := or.cases_on h (λ h, 0) (λ h, 1)</code>. The iota reduction rule says <code>f (or.inl rfl) = 0</code> and that <code>f (or.inr rfl) = 1)</code>, but since by proof irrelevance <code>or.inl rfl = or.inr rfl</code>, this would imply <code>0 = 1</code>, hence <code>or</code> cannot eliminate into data.</p>
</blockquote>
<p>Huh -- I thought <code>0 = 0</code> and <code>1 = 1</code> would just be treated as propositions (and indeed they are equivalent).</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135917806):
<blockquote>
<p>It is the same as</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">f</span> <span class="o">:</span> <span class="n">bool</span> <span class="bp">→</span> <span class="n">fin</span> <span class="mi">2</span> <span class="o">:=</span>
<span class="err">\</span><span class="n">lam</span> <span class="n">b</span><span class="o">,</span> <span class="k">if</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">tt</span> <span class="k">then</span> <span class="mi">0</span> <span class="k">else</span> <span class="mi">1</span>
</pre></div>


</blockquote>
<p>Thanks -- why doesn't <code>∀ b : bool</code> work in place of <code>λ b</code>?</p>

#### [ Kenny Lau (Oct 16 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135917850):
<p><code>(λ b,  proof) : (∀ b : bool, p b)</code></p>

#### [ Chris Hughes (Oct 16 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135917919):
<p>They are treated as propositions. That's why it's not possible to eliminate into data. If both sides of the <code>or</code> are true it breaks proof irrelevance, but without this iota reduction rule you can't compute with it.</p>

#### [ Johan Commelin (Oct 16 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135917928):
<p><code>\forall</code> is only for propositions.</p>

#### [ Chris Hughes (Oct 16 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135917973):
<p>It's only for types.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135921897):
<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> here are some comments on things you said whilst I was going home. </p>
<p>If <code>X</code> is an inductive type then it could well have been defined in something like the following way:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">X</span>
<span class="bp">|</span> <span class="n">c1</span> <span class="o">:</span> <span class="n">X</span>
<span class="bp">|</span> <span class="n">c2</span> <span class="o">:</span> <span class="n">X</span>
</pre></div>


<p>and then you can define functions <code>X-&gt;Y</code> using the equation compiler like this (I <code>open X</code> because <code>c1</code> is really called <code>X.c1</code> etc)</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">X</span>

<span class="n">def</span> <span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="n">c1</span> <span class="o">:=</span> <span class="mi">4</span>
<span class="bp">|</span> <span class="n">c2</span> <span class="o">:=</span> <span class="mi">6</span>
</pre></div>


<p>Note that the <code>|</code> symbols are being used in two different ways here -- first to define an inductive type, and secondly to define a function from the type. The equation compiler is quite powerful. It's trickier to get it to define the map from <code>fin 2</code>, but it's possible. The equation compiler is very smart.</p>
<p>You asked about <code>\forall b</code> instead of <code>lam b</code> -- one is the type, and one is the term. You use Pi to make Pi types (and forall is a special case of Pi, as are function types), and lam to make terms of type Pi. This is what Kenny's post was demonstrating. It took me some time to get my head around all this but it's easy really -- somehow I never read anything which explained it all in simple terms (which was what I needed this time last year). There are propositions called things like <code>P</code> and proofs called things like <code>H</code> or <code>HP</code>. Similarly there are function types (Pi types) called things like <code>X -&gt; Y</code> and then there are actual functions (the terms) called things like <code>lam x, x + 1</code>.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925018):
<p>Thanks. This works for exercise 2 (<code>left_inv</code> only -- presumably the same thing works for <code>right_inv</code>) :</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">norm_num</span>
<span class="c1">--set_option pp.notation false</span>

<span class="n">def</span> <span class="n">f</span> <span class="o">:</span> <span class="n">bool</span> <span class="bp">→</span> <span class="n">fin</span> <span class="mi">2</span>
    <span class="bp">|</span> <span class="n">tt</span> <span class="o">:=</span> <span class="mi">1</span>
    <span class="bp">|</span> <span class="n">ff</span> <span class="o">:=</span> <span class="mi">0</span>

<span class="n">def</span> <span class="n">f_inv</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">2</span> <span class="bp">→</span> <span class="n">bool</span> <span class="o">:=</span>
    <span class="bp">λ</span> <span class="n">k</span><span class="o">,</span> <span class="k">if</span> <span class="n">k</span> <span class="bp">=</span> <span class="mi">1</span> <span class="k">then</span> <span class="n">tt</span> <span class="k">else</span> <span class="n">ff</span>

<span class="n">def</span> <span class="n">X</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">bool</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">2</span><span class="o">)</span> <span class="o">:=</span> <span class="o">{</span>
  <span class="n">to_fun</span> <span class="o">:=</span> <span class="n">f</span><span class="o">,</span>
  <span class="n">inv_fun</span> <span class="o">:=</span> <span class="n">f_inv</span><span class="o">,</span>
  <span class="n">left_inv</span> <span class="o">:=</span> <span class="k">begin</span>
                <span class="n">rw</span> <span class="n">function</span><span class="bp">.</span><span class="n">left_inverse</span><span class="o">,</span>
                <span class="n">intro</span> <span class="n">x</span><span class="o">,</span> <span class="n">cases</span> <span class="n">x</span><span class="o">,</span>
                <span class="k">have</span> <span class="n">Hfff</span> <span class="o">:</span> <span class="n">f</span> <span class="n">ff</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">,</span> <span class="n">rw</span> <span class="n">f</span><span class="o">,</span>
                <span class="n">rw</span> <span class="n">Hfff</span><span class="o">,</span> <span class="n">rw</span> <span class="n">f_inv</span><span class="o">,</span> <span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">,</span>
                <span class="k">have</span> <span class="n">Hftt</span> <span class="o">:</span> <span class="n">f</span> <span class="n">tt</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">,</span> <span class="n">rw</span> <span class="n">f</span><span class="o">,</span>
                <span class="n">rw</span> <span class="n">Hftt</span><span class="o">,</span> <span class="n">rw</span> <span class="n">f_inv</span><span class="o">,</span> <span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">,</span>
              <span class="kn">end</span><span class="o">,</span>
  <span class="n">right_inv</span> <span class="o">:=</span> <span class="k">begin</span> <span class="n">sorry</span> <span class="kn">end</span>
<span class="o">}</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">function</span><span class="bp">.</span><span class="n">bijective</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">sorry</span> <span class="c1">--&lt;FILL IN FUNCTION NAME&gt; X</span>

<span class="bp">#</span><span class="kn">check</span> <span class="n">function</span><span class="bp">.</span><span class="n">bijective_iff_has_inverse</span>
</pre></div>


<p>Although <code>dec_trivial</code> did the job for me, I'm curious to know what exactly is the algorithm being tried by Lean at that point (in Lean notation, it's obvious mathematically), i.e. what could I replace <code>dec_trivial</code> with?</p>

#### [ Kevin Buzzard (Oct 16 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925157):
<p><code>right_inv</code> might be harder, the way you've set it up.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925232):
<div class="codehilite"><pre><span></span>  <span class="n">left_inv</span> <span class="o">:=</span> <span class="k">begin</span>
                <span class="n">intro</span> <span class="n">x</span><span class="o">,</span> <span class="n">cases</span> <span class="n">x</span><span class="o">,</span>
                <span class="k">have</span> <span class="n">Hfff</span> <span class="o">:</span> <span class="n">f</span> <span class="n">ff</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">,</span> <span class="n">rw</span> <span class="n">f</span><span class="o">,</span>
                <span class="n">rw</span> <span class="n">Hfff</span><span class="o">,</span> <span class="n">rw</span> <span class="n">f_inv</span><span class="o">,</span><span class="n">refl</span><span class="o">,</span>
                <span class="k">have</span> <span class="n">Hftt</span> <span class="o">:</span> <span class="n">f</span> <span class="n">tt</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">,</span> <span class="n">rw</span> <span class="n">f</span><span class="o">,</span>
                <span class="n">rw</span> <span class="n">Hftt</span><span class="o">,</span> <span class="n">rw</span> <span class="n">f_inv</span><span class="o">,</span> <span class="n">refl</span><span class="o">,</span>
              <span class="kn">end</span><span class="o">,</span>
</pre></div>

#### [ Kenny Lau (Oct 16 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925250):
<p>we should all wait until <code>fin_cases</code> is merged</p>

#### [ Kevin Buzzard (Oct 16 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925295):
<p>Your <code>rw</code> doesn't seem to do anything. Because your goal is definitionally equal to what the rw changed it into, you can just skip it. And both of your algorithms are <code>rfl</code> -- the left hand side equals the right hand side by definition.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925376):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> I just dealt with <code>n&gt;=2</code> using contradiction. Abhi is yet to run into this issue I think.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925548):
<p>Does <code>fin_cases</code> actually allow just doing cases on <code>fin n</code>? Does it break it up into the full <code>n</code> cases even if <code>n</code> is a thousand?</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925570):
<blockquote>
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> I just dealt with <code>n&gt;=2</code> using contradiction. Abhi is yet to run into this issue I think.</p>
</blockquote>
<p>Wait, which issue?</p>

#### [ Kevin Buzzard (Oct 16 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925651):
<p>His definition of <code>f_inv</code> is "k=1" and "all other cases" so he'll have to deal with k&gt;=2 at some point.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925662):
<div class="codehilite"><pre><span></span>  <span class="n">left_inv</span> <span class="o">:=</span> <span class="k">begin</span>
                <span class="n">intro</span> <span class="n">x</span><span class="o">,</span> <span class="n">cases</span> <span class="n">x</span><span class="bp">;</span><span class="n">refl</span>
              <span class="kn">end</span><span class="o">,</span>
</pre></div>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925812):
<p>I guess <code>refl</code> is more powerful than I thought.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925884):
<blockquote>
<p>His definition of <code>f_inv</code> is "k=1" and "all other cases" so he'll have to deal with k&gt;=2 at some point.</p>
</blockquote>
<p>I can just use exfalso and prove a contradiction using <code>2 &gt; fin.last</code>.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925975):
<p>In fact it seems just doing <code>cases x</code> gives a statement that says <code>x.val &lt; 2</code>.</p>

#### [ Kenny Lau (Oct 16 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925992):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">fintype</span>

<span class="n">noncomputable</span> <span class="n">def</span> <span class="n">X</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">bool</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">2</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">trunc</span><span class="bp">.</span><span class="n">out</span> <span class="o">(</span><span class="n">fintype</span><span class="bp">.</span><span class="n">equiv_fin</span> <span class="n">bool</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Oct 16 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135925998):
<p>:P</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926050):
<p>What??</p>

#### [ Kevin Buzzard (Oct 16 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926067):
<p>rofl what happened there?</p>

#### [ Mario Carneiro (Oct 16 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926096):
<p><code>fintype.card bool = 2</code></p>

#### [ Mario Carneiro (Oct 16 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926103):
<p>so <code>bool ~= fin 2</code></p>

#### [ Kenny Lau (Oct 16 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926145):
<p>trunc</p>

#### [ Kevin Buzzard (Oct 16 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926148):
<p>Oh, that's exactly what Abhi was asking if he could do earlier. <code>fintype.equiv_fin</code> is the general proof that a type which is known to have finitely many elements (say <code>n</code>) <code>equiv</code>s with <code>fin n</code></p>

#### [ Kenny Lau (Oct 16 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926152):
<p>still trunc</p>

#### [ Kevin Buzzard (Oct 16 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926170):
<p>Aah, but Kenny's proof is noncomputable :O</p>

#### [ Mario Carneiro (Oct 16 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926191):
<p>the funny part is it's not really, if you evaluate the proof you can eliminate the trunc</p>

#### [ Kenny Lau (Oct 16 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926198):
<p>how?</p>

#### [ Kenny Lau (Oct 16 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926204):
<p>wait, proof is irrelevant and can't be evaluated</p>

#### [ Mario Carneiro (Oct 16 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926215):
<p>false on both counts</p>

#### [ Mario Carneiro (Oct 16 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926232):
<p>it's not a proof, it's a trunc</p>

#### [ Mario Carneiro (Oct 16 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926236):
<p>and it can be evaluated</p>

#### [ Mario Carneiro (Oct 16 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926239):
<p>even if it was a proof</p>

#### [ Kenny Lau (Oct 16 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926242):
<p>how can I do it then</p>

#### [ Mario Carneiro (Oct 16 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926244):
<p>via <code>#reduce</code></p>

#### [ Kenny Lau (Oct 16 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926289):
<p>oh well then you can't make it a definition</p>

#### [ Kenny Lau (Oct 16 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926300):
<p>could you show us the code?</p>

#### [ Mario Carneiro (Oct 16 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926331):
<p>If you <code>#reduce</code> the proof that <code>trunc (bool ~= fin 2)</code> you will get something that starts <code>trunc.mk</code>... then you throw that away and keep the rest</p>

#### [ Kevin Buzzard (Oct 16 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926448):
<p>...or get a deterministic timeout</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926489):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">X</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">bool</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">2</span><span class="o">)</span> <span class="o">:=</span> <span class="o">{</span>
  <span class="n">to_fun</span> <span class="o">:=</span> <span class="n">f</span><span class="o">,</span>
  <span class="n">inv_fun</span> <span class="o">:=</span> <span class="n">f_inv</span><span class="o">,</span>
  <span class="n">left_inv</span> <span class="o">:=</span>  <span class="k">begin</span>
                 <span class="c1">--rw function.left_inverse,</span>
                 <span class="n">intro</span> <span class="n">x</span><span class="o">,</span> <span class="n">cases</span> <span class="n">x</span><span class="o">,</span>
                 <span class="k">have</span> <span class="n">Hfff</span> <span class="o">:</span> <span class="n">f</span> <span class="n">ff</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">,</span> <span class="n">rw</span> <span class="n">f</span><span class="o">,</span>
                 <span class="n">rw</span> <span class="n">Hfff</span><span class="o">,</span> <span class="n">rw</span> <span class="n">f_inv</span><span class="o">,</span> <span class="n">refl</span><span class="o">,</span>
                 <span class="k">have</span> <span class="n">Hftt</span> <span class="o">:</span> <span class="n">f</span> <span class="n">tt</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">,</span> <span class="n">rw</span> <span class="n">f</span><span class="o">,</span>
                 <span class="n">rw</span> <span class="n">Hftt</span><span class="o">,</span> <span class="n">rw</span> <span class="n">f_inv</span><span class="o">,</span> <span class="n">refl</span><span class="o">,</span>
               <span class="kn">end</span><span class="o">,</span>
  <span class="n">right_inv</span> <span class="o">:=</span> <span class="k">begin</span>
                 <span class="n">intro</span> <span class="n">x</span><span class="o">,</span>
                 <span class="k">have</span> <span class="n">H01</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">s</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">2</span><span class="o">,</span> <span class="n">s</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">∨</span> <span class="n">s</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">,</span> <span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">,</span>
                 <span class="k">have</span> <span class="n">x01</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">∨</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">,</span> <span class="n">exact</span> <span class="n">H01</span> <span class="n">x</span><span class="o">,</span>
                 <span class="n">cases</span> <span class="n">x01</span> <span class="k">with</span> <span class="n">x0</span> <span class="n">x1</span><span class="o">,</span>
                 <span class="c1">--case x0</span>
                    <span class="n">rw</span> <span class="n">x0</span><span class="o">,</span>
                    <span class="k">have</span> <span class="n">Hfarc0</span> <span class="o">:</span> <span class="n">f_inv</span> <span class="mi">0</span> <span class="bp">=</span> <span class="n">ff</span><span class="o">,</span> <span class="n">refl</span><span class="o">,</span>
                    <span class="n">rw</span> <span class="n">Hfarc0</span><span class="o">,</span> <span class="n">refl</span><span class="o">,</span>
                 <span class="c1">--case x1</span>
                    <span class="n">rw</span> <span class="n">x1</span><span class="o">,</span>
                    <span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">,</span>
               <span class="kn">end</span>
<span class="o">}</span>
</pre></div>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926558):
<p>What's <code>trunc.out</code>? Someone catch me up.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926607):
<p>it noncomputably removes the trunc.</p>

#### [ Kenny Lau (Oct 16 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926655):
<p>For a type <code>\a</code>, <code>trunc \a</code> is the type <code>\a</code> quotient by the equivalence relation that relates everything</p>

#### [ Kevin Buzzard (Oct 16 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926721):
<p>You can see the docstring for <code>trunc</code> by hovering over it. It's some weird CS thing.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926919):
<p>Ok, I'll need to read up a bit on that.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135926937):
<p>By the way, exercise 3 is just <code>equiv.bijective X</code> (or at least this works).</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135927027):
<p>Wait, could we also have used <code>finset.card_eq_of_bijective</code> to prove bijectivity then prove <code>equiv</code> from <code>equiv.of_bijective</code>?</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135927044):
<p>Oh wait that's for <code>finset</code>s.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135927279):
<blockquote>
<p>By the way, exercise 3 is just <code>equiv.bijective X</code> (or at least this works).</p>
</blockquote>
<p>Great! How did you find it? I found it by writing <code>bijective</code> and hitting ctrl-space and escape a few times.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135927496):
<blockquote>
<p>Great! How did you find it? I found it by writing <code>bijective</code> and hitting ctrl-space and escape a few times.</p>
</blockquote>
<p>Yep, same.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135927538):
<p>Although I didn't hit escape, just scrolled.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135927565):
<p>Sometimes in VS Code the first time I try ctrl-space I don't get all the options, so I instinctively cancel and try again before I start scrolling.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135927649):
<p>Yeah, I think sometimes it limits itself to a specific namespace or something.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135927702):
<p>Oh this <code>trunc</code> thing -- Lean is not keen on choosing a bijection between <code>bool</code> and <code>fin 2</code>but if you put an equivalence relation on the type of all choices, and the relation was "it's always true", then Lean will give you an element of the quotient type and this is well-defined! So Kenny's construction only shows that the type of <code>equiv</code>s is non-empty without producing an explicit element.</p>

#### [ Chris Hughes (Oct 16 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135929371):
<p>It's stronger than nonempty.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135929688):
<p>because it's data. But I am very hazy about what difference this makes, and even hazier about whether I care.</p>

#### [ Chris Hughes (Oct 16 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135930657):
<p>The definition of <code>equiv.fintype</code>, the thing that says <code>A</code> is finite implies <code>equiv A B</code> is finite uses <code>equiv_fin</code> and the lift condition is met because <code>fintype</code> is a <code>subsingleton</code>. This in turn means that determinant is computable.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135931288):
<p>They'll be pleased in M1M1 :-) I still have not got my head around how important computability is in my world.</p>

#### [ Chris Hughes (Oct 16 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135931427):
<p>I get the impression that it's nice to be able to easily prove <code>1+1=2</code> etc., but I never use computability on naturals on numbers bigger than about 4, and the same with most other computable objects.</p>

#### [ Chris Hughes (Oct 16 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135931731):
<p>Also Lean computable rarely means efficiently computable, so it's kind of useless.</p>

#### [ Kenny Lau (Oct 16 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135931843):
<p>David Helm once said that one of the reasons he likes modular forms is that this is one of the unique opportunities in pure maths where you get to see numbers bigger than 4</p>

#### [ Kevin Buzzard (Oct 16 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135931969):
<p>I once wrote an entire paper and then looked through it to find the biggest number in it, and it was 2</p>

#### [ Kevin Buzzard (Oct 16 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135931985):
<p>Maybe I'm less concerned about computability than I think</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135932585):
<blockquote>
<p>I once wrote an entire paper and then looked through it to find the biggest number in it, and it was 2</p>
</blockquote>
<p>I'm guessing reference and equation numbering don't count.</p>

#### [ Kevin Buzzard (Oct 17 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Define%20a%20finite%20set/near/135933569):
<p>I'm not sure I numbered any equations but I almost certainly numbered theorems (did you notice that here they name them instead?) and no I didn't count those numbers :-)</p>


{% endraw %}
