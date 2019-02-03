---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/08397Usingaddrightinj.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Using @add_right_inj](https://leanprover-community.github.io/archive/113489newmembers/08397Usingaddrightinj.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Oct 13 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135737105):
<p>How many parameters do I need to specify to use <code>←@add_right_inj</code>? I'm trying to understand how to use tactics with implicit parameters, but can't seem to get it right. I keep getting <code>failed to synthesize type class instance</code></p>

#### [ Chris Hughes (Oct 13 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135737389):
<p><code>rw ← add_right_inj x</code> should be good enough depending on the type that you're using. What type are the variables in your equality?</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 13 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135737744):
<blockquote>
<p><code>rw ← add_right_inj x</code> should be good enough depending on the type that you're using. What type are the variables in your equality?</p>
</blockquote>
<p>Yeah, that works, but I'm trying to understand how exactly the <code>@</code> syntax works. Do we not need to use it for things in normal parantheses?</p>

#### [ Chris Hughes (Oct 13 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135737946):
<p>No. <code>@</code> is for specifying the arguments in <code>{}</code> or <code>[]</code>, which are usually inferred, but sometimes Lean can't infer them so they have to be given explicitly. You can put underscores in place of arguments to you want to leave implicit, if you only want to give some of the implicit arguments explicitly.</p>

#### [ Kevin Buzzard (Oct 13 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135737951):
<p>Can you post a MWE with the error?</p>

#### [ Kevin Buzzard (Oct 13 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135738009):
<p>I gave a lecture on type class inference over the summer. Abhi if you log into Imperial's Panopto and search for Xena then you should be able to find all of them.</p>

#### [ Kevin Buzzard (Oct 13 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135738020):
<p>The rule of thumb is that you should not be using @ in general</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 13 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135738205):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">norm_num</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hrs</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">r</span> <span class="bp">=</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">r</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">rw</span> <span class="err">←</span><span class="bp">@</span><span class="n">add_right_inj</span> <span class="o">(</span><span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span><span class="o">)</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">r</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span><span class="o">)</span> <span class="mi">1</span><span class="o">,</span>
    <span class="n">sorry</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Abhimanyu Pallavi Sudhir (Oct 13 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135738266):
<p>(Something like that -- don't mind the sorry, I created the MWE from another project)</p>

#### [ Kenny Lau (Oct 13 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135738277):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">group</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hrs</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">r</span> <span class="bp">=</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">r</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">rw</span> <span class="err">←</span><span class="bp">@</span><span class="n">add_right_inj</span> <span class="bp">ℕ</span> <span class="bp">_</span> <span class="o">(</span><span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span><span class="o">)</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">r</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span><span class="o">)</span> <span class="mi">1</span><span class="o">,</span>
    <span class="n">sorry</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Oct 13 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135738280):
<p>If you do <code>#check @add_right_inj</code>, then you get <code>∀ {α : Type u_1} [_inst_1 : add_right_cancel_semigroup α] (a : α) {b c : α}, b + a = c + a ↔ b = c</code></p>

#### [ Kenny Lau (Oct 13 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135738281):
<p>so the first argument is the type</p>

#### [ Kevin Buzzard (Oct 13 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135740723):
<p>Here's a crash course in how it works. If you type <code>#check @add_right_inj</code> as Kenny says, you'll see the full definition of the function. Stuff in round brackets you are expected to supply (although if you are lazy you can write <code>_</code> which means "try to guess). Stuff in square brackets or curly brackets <code>{</code> <code>}</code> Lean is going to try to guess for you, so your first instinct should be to leave it out. If you leave that stuff out you just pretend it isn't there and don't use <code>@</code></p>

#### [ Kevin Buzzard (Oct 13 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135740796):
<p>Kenny wrote the output of the <code>#check</code> and you see that there's only one thing in round brackets, so it only wants the value of <code>a</code></p>

#### [ Kevin Buzzard (Oct 13 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135740853):
<p>So this works:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hrs</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">r</span> <span class="bp">=</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">r</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">rw</span> <span class="err">←</span><span class="n">add_right_inj</span> <span class="o">(</span><span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span><span class="o">),</span>
    <span class="n">sorry</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Oct 13 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135740891):
<p>although I'm not sure it's what you want, because <code> 2 * r - 4 * s * s - 4 * s</code> is parsed as <code> (2 * r - 4 * s * s) - 4 * s</code> so you might want to worry about the <code>4 * s</code> first.</p>

#### [ Kevin Buzzard (Oct 13 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135740967):
<p>But let's talk about this later. First let me show you how <code>@</code> works. With the <code>@</code> you need to supply _everything_, including the stuff which might not make much sense to you like the proof and all the data about the fact that the naturals are an additive right cancellative semigroup. Lean knows this already and without the @ it uses an algorithm called type class inference to find the proof in a database. That's what's going on with the square brackets.</p>

#### [ Kevin Buzzard (Oct 13 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135741043):
<p>The squiggly brackets -- Lean is saying "I'll guess these from the context". For example your goal was <code>2 * r - 4 * s * s - 4 * s = 1</code> just before the rewrite, so Lean can guess <code>b</code> and <code>c</code> because they must be the left and right hand side.  And once it's guessed them, it can guess <code>α</code> as well, because that's the type of <code>b</code> and <code>c</code></p>

#### [ Kevin Buzzard (Oct 13 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135741088):
<p>If you want to go with the @ you can try this:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hrs</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">r</span> <span class="bp">=</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">r</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">rw</span> <span class="err">←</span><span class="bp">@</span><span class="n">add_right_inj</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
    <span class="n">sorry</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>which says to Lean "OK I am using <code>@</code> so I am going to fill in everything myself...actually why don't you fill in those four things"</p>

#### [ Kevin Buzzard (Oct 13 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135741150):
<p>This works too:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hrs</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">r</span> <span class="bp">=</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">r</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">rw</span> <span class="err">←</span><span class="bp">@</span><span class="n">add_right_inj</span> <span class="bp">ℕ</span> <span class="bp">_</span> <span class="o">(</span><span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span><span class="o">)</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">r</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span><span class="o">)</span> <span class="mi">1</span><span class="o">,</span>
    <span class="n">sorry</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>and here I filled in the three squiggly bracket things but I didn't do the square bracket.</p>

#### [ Kevin Buzzard (Oct 13 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135741239):
<p>Finally here is the example with everything filled in, including the term which Lean can generate automatically:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hrs</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">r</span> <span class="bp">=</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">r</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="k">let</span> <span class="n">abcde</span> <span class="o">:</span> <span class="n">add_right_cancel_semigroup</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="c1">-- two goals now</span>
      <span class="n">apply_instance</span><span class="o">,</span> <span class="c1">-- the new one just got closed</span>
    <span class="n">rw</span> <span class="err">←</span><span class="bp">@</span><span class="n">add_right_inj</span> <span class="bp">ℕ</span> <span class="n">abcde</span> <span class="o">(</span><span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span><span class="o">)</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">r</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span><span class="o">)</span> <span class="mi">1</span><span class="o">,</span>
    <span class="n">sorry</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>The weird <code> apply_instance</code> line means "explicitly apply the type class inference machine to solve this goal". It's the explicit tactic which means "run the square bracket machine to produce the term of this type"</p>

#### [ Kevin Buzzard (Oct 13 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135741500):
<p>So that's the story of <code>@</code> in a nutshell. But what you might need advice on is how to solve your goal. If you let me cheat and work over the integers then here is the easiest way for a mathematician: </p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">ring</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hrs</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">r</span> <span class="bp">=</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">r</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">rw</span> <span class="n">Hrs</span><span class="o">,</span>
    <span class="n">ring</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>However subtraction on the naturals is not so well-behaved (did anyone point out to you that <code>2-3=0</code>? ) and <code>ring</code> can't handle it (the naturals aren't a ring, and ring isn't always so clever in the naturals case)</p>

#### [ Kevin Buzzard (Oct 13 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135741550):
<p>But something you have to learn about Lean is that almost every lemma you want is already there (e.g. <code>a+b=c -&gt; a=c-b</code> and all the variants will be there).</p>

#### [ Kevin Buzzard (Oct 13 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135741806):
<p>So here's a more low-level proof:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hrs</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">r</span> <span class="bp">=</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span>
<span class="mi">2</span> <span class="bp">*</span> <span class="n">r</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">nat</span><span class="bp">.</span><span class="n">sub_eq_of_eq_add</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">nat</span><span class="bp">.</span><span class="n">sub_eq_of_eq_add</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">Hrs</span><span class="o">,</span>
  <span class="n">simp</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Oct 13 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135741863):
<p>The strategy is to get rid of all the subtractions and then use simp, which is good at proving some equalities. Subtraction on naturals is a bit hairy though, that's why this was an effort. It would not surprise me if Kenny Chris or Mario could come up with a shorter proof.</p>

#### [ Chris Hughes (Oct 13 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135742263):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hrs</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">r</span> <span class="bp">=</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span>
  <span class="mi">2</span> <span class="bp">*</span> <span class="n">r</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">sub_sub</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">add_sub_cancel</span><span class="o">,</span> <span class="n">Hrs</span><span class="o">]</span>
</pre></div>

#### [ Kevin Buzzard (Oct 13 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135742323):
<p>How do you find a proof like that <span class="user-mention" data-user-id="110044">@Chris Hughes</span> ?</p>

#### [ Kevin Buzzard (Oct 13 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135742325):
<p>I was surprised <code>rw Hrs;ring</code> didn't work</p>

#### [ Chris Hughes (Oct 13 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135742640):
<p>First try to substitute in Hrs as quickly as possible. Then <code>simp</code>, look at the goal and see what else needs to be done.</p>

#### [ Kevin Buzzard (Oct 13 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135742694):
<p>I did that and got the horrible <code>1 + (4 * s + 4 * s * s) - 4 * s * s - 4 * s = 1</code></p>

#### [ Kevin Buzzard (Oct 13 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135742718):
<p><code>((1 + (4 * s + 4 * s * s)) - 4 * s * s) - 4 * s = 1</code></p>

#### [ Kenny Lau (Oct 13 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135744202):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span></p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hrs</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">r</span> <span class="bp">=</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span>
  <span class="mi">2</span> <span class="bp">*</span> <span class="n">r</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">sub_sub</span><span class="o">,</span> <span class="n">Hrs</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">add_sub_cancel_left</span><span class="o">]</span>
</pre></div>

#### [ Kevin Buzzard (Oct 13 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135744571):
<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> Kenny managed to do it in three rewrites; you can click around in the middle of his rewrite line to see what's going on.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 13 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135744726):
<p>Oh, I know how to do the proof -- I just wanted to learn about @, __inst, etc. Your crash course is helpful, thanks!</p>

#### [ Kevin Buzzard (Oct 13 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135746827):
<p>The weird <code>_inst_</code> variables are the ones which are generated by the type class inference machine</p>

#### [ Kevin Buzzard (Oct 13 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135747252):
<p>If you ever see the word "instance" in Lean code it just means "definition, and add it to the type class inference machine too"</p>

#### [ Kevin Buzzard (Oct 13 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20%40add_right_inj/near/135747304):
<p>So for example the construction of the ring structure on the integers will be defined as an instance rather than a definition, and then any lemmas about rings will automatically apply to the integers</p>


{% endraw %}
