---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/06401DefininggraphsinLean.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Defining graphs in Lean](https://leanprover-community.github.io/archive/113488general/06401DefininggraphsinLean.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Hoang Le Truong (Jul 10 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129399957):
<p>I definite a function on the certain domain as follow</p>
<div class="codehilite"><pre><span></span>def V: set ℕ := {1,2,3,4}

def g [has_one V][has_add V](e:V× V ): ℕ :=
match  e  with
|(1,2) :=2
|(2,1) :=2
|_     :=0
end
</pre></div>


<p>I received the following  message</p>
<div class="codehilite"><pre><span></span>equation compiler failed (use &#39;set_option trace.eqn_compiler.elim_match true&#39; for additional details)
</pre></div>


<p>and</p>
<div class="codehilite"><pre><span></span>invalid function application in pattern, it cannot be reduced to a constructor (possible solution, mark term as inaccessible using &#39;.( )&#39;) 1
</pre></div>


<p>What is error?</p>

#### [ Kenny Lau (Jul 10 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400000):
<p><code>V</code> is not an inductive type.</p>

#### [ Kenny Lau (Jul 10 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400011):
<p>you can't match it</p>

#### [ Kenny Lau (Jul 10 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400050):
<p>you can't just "make it work" by using <code>[has_one V] [has_add V]</code></p>

#### [ Hoang Le Truong (Jul 10 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400103):
<p>I need make <code>V</code> as an inductive type, not is subset of <code>\N</code></p>

#### [ Kenny Lau (Jul 10 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400106):
<p>depends on your purpose</p>

#### [ Kenny Lau (Jul 10 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400108):
<p>I would just use if-then-else</p>

#### [ Hoang Le Truong (Jul 10 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400153):
<p>I need V is subset of <code>\N</code></p>

#### [ Hoang Le Truong (Jul 10 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400171):
<p>how are we use <code>V</code> is an inductive type and subset of <code>\N</code></p>

#### [ Johan Commelin (Jul 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400248):
<p><code>def g : V \times V \to nat := \lam x, if x.1 * x.2 = 2 then 2 else 0</code></p>

#### [ Johan Commelin (Jul 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400252):
<p>Something like that?</p>

#### [ Kenny Lau (Jul 10 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400260):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">def</span> <span class="n">V</span> <span class="o">:</span> <span class="err">\</span><span class="n">N</span> <span class="err">\</span><span class="n">to</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">one</span> <span class="o">:</span> <span class="mi">1</span> <span class="err">\</span><span class="n">to</span> <span class="n">V</span>
<span class="bp">|</span> <span class="n">two</span> <span class="o">:</span> <span class="mi">2</span> <span class="err">\</span><span class="n">to</span> <span class="n">V</span>
<span class="bp">|</span> <span class="n">three</span> <span class="o">:</span> <span class="mi">3</span> <span class="err">\</span><span class="n">to</span> <span class="n">V</span>
<span class="bp">|</span> <span class="n">four</span> <span class="o">:</span> <span class="mi">4</span> <span class="err">\</span><span class="n">to</span> <span class="n">V</span>
</pre></div>

#### [ Hoang Le Truong (Jul 10 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400408):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span>  It is ok but if I have function has domain is random and large. It is not good to make function when use <code>if - then-else</code></p>

#### [ Kenny Lau (Jul 10 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400426):
<p>maybe you should tell us what you want to do</p>

#### [ Hoang Le Truong (Jul 10 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400490):
<p>I want to make function with card V=100 and valued is random</p>

#### [ Kenny Lau (Jul 10 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400496):
<p>randomness doesn't exist</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400509):
<p>(in Lean)</p>

#### [ Kenny Lau (Jul 10 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400511):
<p>randomness doesn't exist, period</p>

#### [ Johan Commelin (Jul 10 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400514):
<p>What do you mean with "valued is random", do you mean that <code>V</code> is an arbitrary subset of <code>\N</code>?</p>

#### [ Kenny Lau (Jul 10 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400515):
<p>a random variable is neither random nor a variable</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400519):
<p>(I guess the quantum mechanics course is next year Kenny, right?)</p>

#### [ Hoang Le Truong (Jul 10 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400558):
<p>yes</p>

#### [ Kenny Lau (Jul 10 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400562):
<p>alright</p>

#### [ Johan Commelin (Jul 10 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400565):
<p>Kenny will <em>choose</em> not to follow QM...</p>

#### [ Kenny Lau (Jul 10 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400567):
<p>lol</p>

#### [ Johan Commelin (Jul 10 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400572):
<p>Hoang, ok, and what should your function do with <code>V</code>?</p>

#### [ Johan Commelin (Jul 10 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400584):
<p>You want a function <code>V \to \N</code>, is that right?</p>

#### [ Hoang Le Truong (Jul 10 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400588):
<p>yes is randomness doesn't exist<br>
I want find example function <code>g</code></p>

#### [ Hoang Le Truong (Jul 10 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400633):
<div class="codehilite"><pre><span></span>def G (e:ℕ× ℕ ): ℕ :=
match  e  with
|(1,2) :=2
|(2,1) :=2
|(1,3) :=2
|(3,1) :=2
|(2,4) :=1
|(4,2) :=1
|(3,4) :=1
|(4,3) :=1
|_     :=0
end
</pre></div>

#### [ Hoang Le Truong (Jul 10 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400641):
<p>it is ok but I want to certain domains <code>V</code></p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400649):
<p>Maybe you should define your function on all of nat x nat</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400650):
<p>and then just ignore its values on the elements you don't like</p>

#### [ Johan Commelin (Jul 10 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400651):
<p>Ok, so define the function on <code>\N \times \N</code>, and then restrict to <code>V</code></p>

#### [ Kenny Lau (Jul 10 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400652):
<p>i'll say it isn't even a function</p>

#### [ Johan Commelin (Jul 10 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400694):
<p>Kenny, did you read that translation of the article by Aristotle?</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400699):
<p>This is a standard trick in this game: for example the square root function in Lean is defined on all the reals, and returns the square root of x if x&gt;=0 but just returns something random if x &lt; 0</p>

#### [ Kenny Lau (Jul 10 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400701):
<p>what about it</p>

#### [ Johan Commelin (Jul 10 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400705):
<p>something <em>random</em> &lt;-- Kevin</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400706):
<p>you are just making noise Kenny, not contributing, that's what about it</p>

#### [ Hoang Le Truong (Jul 10 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400707):
<p>yes I want it</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400716):
<p>When I thought more like a mathematician, I really thought I wanted the square root function to be only defined on the non-negative reals</p>

#### [ Hoang Le Truong (Jul 10 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400720):
<p>I want same as <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Kenny Lau (Jul 10 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400727):
<p>I don't even know what function he wants to build. My understanding is that he wants some kind of a function defined on N x N, and then he just randomly gives some values in the two examples he gave us</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400729):
<p>but after building such a function myself, and then discovering how hard it was to use it, I started coming round to the methods which Mario and others were preaching.</p>

#### [ Kenny Lau (Jul 10 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400777):
<p>he wants an arbitrary function N x N -&gt; N, that's all I can make of it</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400779):
<p>right, so let's listen to him and find out more.</p>

#### [ Hoang Le Truong (Jul 10 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400846):
<p>In fact, I have function with certain properties. I want example from such function</p>

#### [ Kenny Lau (Jul 10 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400850):
<p>what properties?</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400904):
<p>What do you mean by "example"? You mean an example of the function, or example of a value, or example of a definition, or... ? When you say "I have function" -- you mean you have the definition of the function already? In Lean or on paper? Or you just have some properties which you want the function to satisfy?</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129400908):
<p>We are still trying to understand your question.</p>

#### [ Sean Leather (Jul 10 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129401005):
<p>I think one property of the function Hoang wants is the type: <code>ℕ × ℕ → ℕ</code>.</p>

#### [ Sean Leather (Jul 10 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129401126):
<p>Or perhaps the type should have subsets of <code>ℕ</code>?</p>

#### [ Sean Leather (Jul 10 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129401214):
<p><code>{ns : ℕ × ℕ // p ns} → ℕ</code> for some <code>p : ℕ × ℕ → Prop</code>?</p>

#### [ Hoang Le Truong (Jul 10 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402299):
<p>graph is connected</p>

#### [ Hoang Le Truong (Jul 10 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402300):
<p>I want check the definition of graph is correct</p>

#### [ Hoang Le Truong (Jul 10 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402301):
<p>I think g is graph</p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402359):
<p>What does this have to do with nat?</p>

#### [ Hoang Le Truong (Jul 10 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402375):
<div class="codehilite"><pre><span></span>variables {α : Type }
variable graph: α × α → ℕ
</pre></div>

#### [ Hoang Le Truong (Jul 10 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402387):
<p>I think function<code>graph</code> is graph</p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402388):
<p>Is alpha the vertices of the graph? What is nat doing there?</p>

#### [ Hoang Le Truong (Jul 10 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402393):
<p>yes</p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402404):
<p>What is a graph? For me it is vertices and edges, and there is no <code>ℕ</code></p>

#### [ Hoang Le Truong (Jul 10 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402418):
<div class="codehilite"><pre><span></span>def G (e:ℕ× ℕ ): ℕ :=
match  e  with
|(1,2) :=2
|(2,1) :=2
|(1,3) :=2
|(3,1) :=2
|(2,4) :=1
|(4,2) :=1
|(3,4) :=1
|(4,3) :=1
|_     :=0
end
</pre></div>

#### [ Hoang Le Truong (Jul 10 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402421):
<p>is example of graph</p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402426):
<p>What is a graph for you?</p>

#### [ Hoang Le Truong (Jul 10 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402490):
<p>vertices <code>def V: set ℕ := {1,2,3,4}</code></p>

#### [ Kenny Lau (Jul 10 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402507):
<p>so every graph is countable</p>

#### [ Hoang Le Truong (Jul 10 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402530):
<p>I do not know</p>

#### [ Hoang Le Truong (Jul 10 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402623):
<p>I have that definition of connected graph. I want check such definition in lean which I make is true or fail. I make an example of such definition</p>

#### [ Hoang Le Truong (Jul 10 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402765):
<p>I make example of graph</p>
<div class="codehilite"><pre><span></span>def G (e:ℕ× ℕ ): ℕ :=
match  e  with
|(1,2) :=2
|(2,1) :=2
|(1,3) :=2
|(3,1) :=2
|(2,4) :=1
|(4,2) :=1
|(3,4) :=1
|(4,3) :=1
|_     :=0
end
````
it is ok. but
</pre></div>


<p>def V: set ℕ := {1,2,3,4}</p>
<p>def G (e:V× V ): ℕ :=<br>
match  e  with<br>
|(1,2) :=2<br>
|(2,1) :=2<br>
|(1,3) :=2<br>
|(3,1) :=2<br>
|(2,4) :=1<br>
|(4,2) :=1<br>
|(3,4) :=1<br>
|(4,3) :=1<br>
|_     :=0<br>
end</p>
<div class="codehilite"><pre><span></span>is it not run
</pre></div>

#### [ Kevin Buzzard (Jul 10 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402771):
<p>Aah</p>

#### [ Mario Carneiro (Jul 10 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402779):
<p>this is the konigsberg graph?</p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402784):
<p>rofl</p>

#### [ Hoang Le Truong (Jul 10 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402787):
<p>yes</p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402792):
<p>even more rofl</p>

#### [ Mario Carneiro (Jul 10 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402799):
<p>I would use custom inductive types for all of it</p>

#### [ Hoang Le Truong (Jul 10 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402802):
<p>no</p>

#### [ Mario Carneiro (Jul 10 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402807):
<p><code>inductive vertices | north_shore | west_island | ...</code></p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402856):
<p><span class="user-mention" data-user-id="116065">@Hoang Le Truong</span> -- he is saying that you should make your own type called <code>graph</code></p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402862):
<p>and I would definitely agree with him</p>

#### [ Mario Carneiro (Jul 10 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402871):
<div class="codehilite"><pre><span></span>inductive edges : vertices -&gt; vertices -&gt; Type
| bridge1 : edges north_shore west_island
...
</pre></div>

#### [ Hoang Le Truong (Jul 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402877):
<p>yes I agree</p>

#### [ Mario Carneiro (Jul 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402888):
<p>It's self documenting and clear and unambiguous</p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402894):
<p>and then you could formalise what it means for a graph to be connected</p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402901):
<p>(for all vertices v1 and v2 there's a path from v1 to v2)</p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402905):
<p>and then you could prove it in this case just by a case by case check</p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402954):
<p>But for a big graph, it is not so clear that Lean is the tool for this.</p>

#### [ Mario Carneiro (Jul 10 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402959):
<p>This gets complicated for large graphs, but you will want to switch to a different encoding anyway in that case</p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402961):
<p>You might want to read about what algorithms are used to prove a graph is connected, and implement one of those, but probably you would not get good performance in comparison with a tool like python</p>

#### [ Mario Carneiro (Jul 10 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129402973):
<p>For fabs this is not a big problem</p>

#### [ Mario Carneiro (Jul 10 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403034):
<p>If you were, say, trying to work with the graphs in the four color theorem this kind of encoding is far too dense</p>

#### [ Hoang Le Truong (Jul 10 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403037):
<p>Yes I begin graph in general. after I restrict example</p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403038):
<p>Mario I'm surprised you haven't implemented graphs in mathlib. It's just the sort of thing a computer scientist would like to do, I would have thought.</p>

#### [ Mario Carneiro (Jul 10 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403046):
<p>The problem (which I have had also in metamath) is that "graph" means something different every time it is used</p>

#### [ Mario Carneiro (Jul 10 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403056):
<p>and the different theories are hard to fit in the same framework</p>

#### [ Mario Carneiro (Jul 10 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403064):
<p>even though everyone pretends it is easy</p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403220):
<p>I wondered if this was why. You need directed and undirected graphs, graphs where you're allowed/not allowed to have an edge from v to v, graphs where you are/are not allowed to have more than one edge from v to w, and that's before we've even started worrying about whether all graphs are finite etc</p>

#### [ Hoang Le Truong (Jul 10 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403293):
<p>Of course, I go this way.</p>

#### [ Hoang Le Truong (Jul 10 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403348):
<p>Now I work only the above graph <code>G</code></p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403361):
<p>So maybe one way of proceeding is that you decide exactly what is a graph for you, and then make your own type, and then make a term of that type corresponding to Koenigsberg, and make a general definition for connected, and then prove that Koenigsberg is connected.</p>

#### [ Mario Carneiro (Jul 10 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403368):
<p>And those "not allowed" things are not just constraints, they <em>change the encoding completely</em>, i.e. if there are no multiple edges you can have a relation instead of a set of edges with dom/cod; if it is undirected then maybe you want a function on <em>un</em>ordered pairs, if you have hyperedges then maybe each edge maps to a set of vertices which may or may not have size 2, ...</p>

#### [ Mario Carneiro (Jul 10 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403394):
<p>I agree that this is what Hoang should do, and it's what I did for Koenigsberg in Metamath</p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403442):
<p>I can now envisage a 2500-line graph.lean which carefully does every single possibility ;-)</p>

#### [ Mario Carneiro (Jul 10 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403446):
<p>just define things that make sense for undirected multigraphs</p>

#### [ Mario Carneiro (Jul 10 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403483):
<p>and forget about all the other crazy stuff until the next project</p>

#### [ Hoang Le Truong (Jul 10 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403495):
<p>I begin graph directed multiple degree have loop graph</p>

#### [ Hoang Le Truong (Jul 10 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129403637):
<p>After I restrict to undirected multiphaps<br>
Now I only work on a above <code>G</code>. I have two way to define <code>G</code>. I want to known what is good.</p>

#### [ Johan Commelin (Jul 10 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129405050):
<p>Hoang, that was a bit of an XY problem: <a href="https://mywiki.wooledge.org/XyProblem" target="_blank" title="https://mywiki.wooledge.org/XyProblem">https://mywiki.wooledge.org/XyProblem</a></p>

#### [ Johan Commelin (Jul 10 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129405067):
<p>I suggest you start a new topic titled "Defining graphs in Lean"</p>

#### [ Johan Commelin (Jul 10 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129405121):
<p>It would have helped a lot if you had mentioned the word "graph" in the first few posts. Instead of just "function with properties"</p>

#### [ Hoang Le Truong (Jul 10 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129405223):
<p>How to change "function on certain domain " to <code> Defining graphs in Lean</code></p>

#### [ Hoang Le Truong (Jul 10 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129405242):
<p>Ok I changed it</p>

#### [ Kevin Buzzard (Jul 10 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129405450):
<blockquote>
<p>I have two way to define <code>G</code>. I want to known what is good.</p>
</blockquote>
<p>I am a mathematician, and I find myself asking this question often in Lean. I think it is a very difficult and delicate question, and sometimes the computer scientist experts here answer things like "it depends on why you want this structure". My advice to you is to go ahead and formalise it in one way, and then post your actual working code and ask for comments.</p>

#### [ Hoang Le Truong (Jul 10 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129405782):
<p>I have two ways to define <code>G</code>. one is</p>
<div class="codehilite"><pre><span></span>inductive vertices
| a | b | c | d

def g (e:vertices× vertices ): ℕ :=
match  e  with
|(vertices.a,vertices.b) :=2
|(vertices.b,vertices.a) :=2
|(vertices.a,vertices.c) :=2
|(vertices.c,vertices.a) :=2
|(vertices.b,vertices.d) :=1
|(vertices.d,vertices.b) :=1
|(vertices.c,vertices.d) :=1
|(vertices.d,vertices.c) :=1
|_ :=0
end
</pre></div>


<p>and another is</p>
<div class="codehilite"><pre><span></span>def G (e:ℕ × ℕ  ): ℕ :=
match  e  with
|(1,2) :=2
|(2,1) :=2
|(1,3) :=2
|(3,1) :=2
|(2,4) :=1
|(4,2) :=1
|(3,4) :=1
|(4,3) :=1
|_     :=0
end
</pre></div>


<p>what is way in Lean good</p>

#### [ Johan Commelin (Jul 10 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129405788):
<p>No, that is not the definition of a graph</p>

#### [ Johan Commelin (Jul 10 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129405791):
<p>It is only 1 very specific example.</p>

#### [ Johan Commelin (Jul 10 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129405799):
<p>First you should decide if you want a general definition, or only the Koenigsberg example.</p>

#### [ Hoang Le Truong (Jul 10 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129405872):
<p>I want a general definition and after apply to example</p>

#### [ Johan Commelin (Jul 10 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129407364):
<p>So then, give a general definition, and not an example.</p>

#### [ Johan Commelin (Jul 10 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129407410):
<p>Can you first give a definition without using Lean? Just write down an informal definition here.</p>

#### [ Hoang Le Truong (Jul 10 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408167):
<p><code>An Euler walk in an undirected graph is a walk that uses each edge exactly once.</code></p>

#### [ Hoang Le Truong (Jul 10 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408413):
<p>this is a general definition. I formed it in Lean. Now I want to apply it to exactly example to check the definition Euler walk is correct or wrong in lean.</p>

#### [ Johan Commelin (Jul 10 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408432):
<p>How did you put that statement into Lean?</p>

#### [ Hoang Le Truong (Jul 10 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408443):
<p>yes</p>

#### [ Johan Commelin (Jul 10 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408449):
<p>Please show it to us.</p>

#### [ Johan Commelin (Jul 10 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408514):
<p>We can not help you with defining your Koenigsberg example if we don't know how you put "undirected graph" in Lean.</p>

#### [ Hoang Le Truong (Jul 10 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408661):
<p>```definition undirected_graph ( graph:α × α → ℕ  ): Prop := <br>
       ∀ u v:α, graph(u,v)=graph(v,u)</p>
<div class="codehilite"><pre><span></span>
</pre></div>

#### [ Hoang Le Truong (Jul 10 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408679):
<div class="codehilite"><pre><span></span>definition undirected_graph ( graph:α × α → ℕ  ): Prop :=
       ∀ u v:α, graph(u,v)=graph(v,u)
</pre></div>

#### [ Johan Commelin (Jul 10 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408771):
<p>Right, so for your example, you need the following ingredients: a type <code>alpha</code>, a function <code>alpha \times alpha \to nat</code> and a proof that your graph is undirected.</p>

#### [ Johan Commelin (Jul 10 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408782):
<p>There is no reason at all to take a subset of nat for alpha.</p>

#### [ Johan Commelin (Jul 10 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408796):
<p>You could define an inductive type for the four vertices.</p>

#### [ Johan Commelin (Jul 10 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408856):
<p>And it will allow you to define your function encoding the graph with matching.</p>

#### [ Johan Commelin (Jul 10 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129408944):
<p>Like Mario wrote above: <code>inductive vertices | north_shore | west_island | ... </code></p>

#### [ Hoang Le Truong (Jul 10 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129409001):
<p>Thank you for that. I understood</p>

#### [ Johan Commelin (Jul 10 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129409007):
<p>So, that is the same thing as your first method, except Mario's suggestion is more readable</p>

#### [ Johan Commelin (Jul 10 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129409014):
<p>(For people who have walked through Koenigsberg...; or those who looked at the map on Wikipedia...)</p>

#### [ Johan Commelin (Jul 10 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20graphs%20in%20Lean/near/129409133):
<p>Ok, so, afterwards you have to prove that the thing is undirected, and then you have to show us the formalisation of "Euler walk"</p>


{% endraw %}
