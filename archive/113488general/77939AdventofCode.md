---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/77939AdventofCode.html
---

## Stream: [general](index.html)
### Topic: [Advent of Code](77939AdventofCode.html)

---


{% raw %}
#### [ Edward Ayers (Dec 01 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150682850):
<p><a href="http://adventofcode.com" target="_blank" title="http://adventofcode.com">adventofcode.com</a> in Lean?</p>

#### [ Patrick Massot (Dec 01 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150683859):
<p>Does anyone know how to use Lean to read a file from disk, and get a <code>list int</code> if each line looks like an integer?</p>

#### [ Edward Ayers (Dec 01 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150683922):
<p>I just pasted into lean file! But that's a better idea!</p>

#### [ Patrick Massot (Dec 01 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150683931):
<p>I thought about pasting, but I guess that's not a reasonable strategy if you want to do all 50 puzzles</p>

#### [ Patrick Massot (Dec 01 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150683932):
<p>And someone needs to write a IO monad howto anyway</p>

#### [ Edward Ayers (Dec 01 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150684498):
<p>I completed it but I used <code>meta</code>. I feel dirty.</p>

#### [ Patrick Massot (Dec 01 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150684511):
<p>Did you use IO?</p>

#### [ Edward Ayers (Dec 01 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150684515):
<p>nope</p>

#### [ Patrick Massot (Dec 01 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150684561):
<p>Would you know how to read from a file?</p>

#### [ Mario Carneiro (Dec 01 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150684565):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">system</span><span class="bp">.</span><span class="n">io</span> <span class="n">data</span><span class="bp">.</span><span class="n">buffer</span><span class="bp">.</span><span class="n">parser</span> <span class="n">data</span><span class="bp">.</span><span class="n">int</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">open</span> <span class="n">tactic</span> <span class="n">parser</span>

<span class="n">def</span> <span class="n">number</span> <span class="o">:</span> <span class="n">parser</span> <span class="bp">ℕ</span> <span class="o">:=</span>
<span class="n">string</span><span class="bp">.</span><span class="n">to_nat</span> <span class="bp">&lt;</span><span class="err">$</span><span class="bp">&gt;</span> <span class="n">many_char1</span> <span class="o">(</span><span class="n">sat</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">c</span><span class="o">,</span>
  <span class="err">&#39;</span><span class="mi">0</span><span class="err">&#39;</span><span class="bp">.</span><span class="n">to_nat</span> <span class="bp">≤</span> <span class="n">c</span><span class="bp">.</span><span class="n">to_nat</span> <span class="bp">∧</span> <span class="n">c</span><span class="bp">.</span><span class="n">to_nat</span> <span class="bp">≤</span> <span class="err">&#39;</span><span class="mi">9</span><span class="err">&#39;</span><span class="bp">.</span><span class="n">to_nat</span><span class="o">)</span>

<span class="n">def</span> <span class="n">signed_number</span> <span class="o">:</span> <span class="n">parser</span> <span class="bp">ℤ</span> <span class="o">:=</span>
<span class="n">ch</span> <span class="err">&#39;</span><span class="bp">+</span><span class="err">&#39;</span> <span class="bp">&gt;&gt;</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">of_nat</span> <span class="bp">&lt;</span><span class="err">$</span><span class="bp">&gt;</span> <span class="n">number</span><span class="o">)</span> <span class="bp">&lt;|&gt;</span>
<span class="n">ch</span> <span class="err">&#39;</span><span class="bp">-</span><span class="err">&#39;</span> <span class="bp">&gt;&gt;</span> <span class="o">((</span><span class="bp">λ</span> <span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">,</span> <span class="bp">-</span><span class="n">x</span><span class="o">)</span> <span class="bp">&lt;</span><span class="err">$</span><span class="bp">&gt;</span> <span class="n">number</span><span class="o">)</span>

<span class="n">run_cmd</span> <span class="n">do</span>
  <span class="n">s</span> <span class="err">←</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">unsafe_run_io</span> <span class="err">$</span> <span class="n">io</span><span class="bp">.</span><span class="n">fs</span><span class="bp">.</span><span class="n">read_file</span> <span class="s2">&quot;dat.txt&quot;</span><span class="o">,</span>
  <span class="n">sum</span><span class="bp">.</span><span class="n">inr</span> <span class="n">l</span> <span class="err">←</span> <span class="n">return</span> <span class="err">$</span> <span class="n">run</span> <span class="o">(</span><span class="n">many</span> <span class="o">(</span><span class="n">signed_number</span> <span class="bp">&lt;*</span> <span class="n">ch</span> <span class="err">&#39;\</span><span class="n">n&#39;</span><span class="o">))</span> <span class="n">s</span><span class="o">,</span>
  <span class="n">trace</span> <span class="n">l</span>
</pre></div>


<div class="codehilite"><pre><span></span>[13,
 -(2+1),
 -(7+1),
 14,
 16,
 -(6+1),
 3,
 -(6+1),
 9,
 -(9+1),
 16,
...
</pre></div>

#### [ Mario Carneiro (Dec 01 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150684582):
<p>maybe <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> knows the correct way to call IO from <code>run_cmd</code>, but <code>unsafe_run_io</code> works in a pinch</p>

#### [ Sebastian Ullrich (Dec 01 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150684636):
<p>I think you can use <code>#eval</code></p>

#### [ Mario Carneiro (Dec 01 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150684702):
<p>oh, I should have used <code>to_string</code>, the output is much nicer</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">system</span><span class="bp">.</span><span class="n">io</span> <span class="n">data</span><span class="bp">.</span><span class="n">buffer</span><span class="bp">.</span><span class="n">parser</span>
<span class="kn">open</span> <span class="n">parser</span>

<span class="n">def</span> <span class="n">number</span> <span class="o">:</span> <span class="n">parser</span> <span class="bp">ℕ</span> <span class="o">:=</span>
<span class="n">string</span><span class="bp">.</span><span class="n">to_nat</span> <span class="bp">&lt;</span><span class="err">$</span><span class="bp">&gt;</span> <span class="n">many_char1</span> <span class="o">(</span><span class="n">sat</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">c</span><span class="o">,</span>
  <span class="err">&#39;</span><span class="mi">0</span><span class="err">&#39;</span><span class="bp">.</span><span class="n">to_nat</span> <span class="bp">≤</span> <span class="n">c</span><span class="bp">.</span><span class="n">to_nat</span> <span class="bp">∧</span> <span class="n">c</span><span class="bp">.</span><span class="n">to_nat</span> <span class="bp">≤</span> <span class="err">&#39;</span><span class="mi">9</span><span class="err">&#39;</span><span class="bp">.</span><span class="n">to_nat</span><span class="o">)</span>

<span class="n">def</span> <span class="n">signed_number</span> <span class="o">:</span> <span class="n">parser</span> <span class="bp">ℤ</span> <span class="o">:=</span>
<span class="n">ch</span> <span class="err">&#39;</span><span class="bp">+</span><span class="err">&#39;</span> <span class="bp">&gt;&gt;</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">of_nat</span> <span class="bp">&lt;</span><span class="err">$</span><span class="bp">&gt;</span> <span class="n">number</span><span class="o">)</span> <span class="bp">&lt;|&gt;</span>
<span class="n">ch</span> <span class="err">&#39;</span><span class="bp">-</span><span class="err">&#39;</span> <span class="bp">&gt;&gt;</span> <span class="o">((</span><span class="bp">λ</span> <span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">,</span> <span class="bp">-</span><span class="n">x</span><span class="o">)</span> <span class="bp">&lt;</span><span class="err">$</span><span class="bp">&gt;</span> <span class="n">number</span><span class="o">)</span>

<span class="bp">#</span><span class="kn">eval</span> <span class="n">do</span>
  <span class="n">s</span> <span class="err">←</span> <span class="n">io</span><span class="bp">.</span><span class="n">fs</span><span class="bp">.</span><span class="n">read_file</span> <span class="s2">&quot;dat.txt&quot;</span><span class="o">,</span>
  <span class="n">sum</span><span class="bp">.</span><span class="n">inr</span> <span class="n">l</span> <span class="err">←</span> <span class="n">return</span> <span class="err">$</span> <span class="n">run</span> <span class="o">(</span><span class="n">many</span> <span class="o">(</span><span class="n">signed_number</span> <span class="bp">&lt;*</span> <span class="n">ch</span> <span class="err">&#39;\</span><span class="n">n&#39;</span><span class="o">))</span> <span class="n">s</span><span class="o">,</span>
  <span class="n">trace</span> <span class="o">(</span><span class="n">to_string</span> <span class="n">l</span><span class="o">)</span> <span class="o">(</span><span class="n">return</span> <span class="o">())</span>
</pre></div>


<div class="codehilite"><pre><span></span>[13, -3, -8, 14, 16, -7, 3, -7, 9, -10, 16, 13, 12, 12, 4, 19, -2, -5, -15, -2, -13, -11, -13, -2, ...
</pre></div>

#### [ Mario Carneiro (Dec 01 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150684754):
<p>For some reason the output or return value of the io is ignored, so I had to to a hack with <code>trace</code> to get it to print</p>

#### [ Patrick Massot (Dec 01 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150684902):
<p>Thanks Mario! It allowed to complete Day 1, adding only 15 characters to your code :)</p>

#### [ Edward Ayers (Dec 01 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150684972):
<p>Did you do the second part?</p>

#### [ Mario Carneiro (Dec 01 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150685393):
<p>here's how I did the first part in lean:</p>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">eval</span> <span class="mi">0</span>
<span class="bp">+</span><span class="mi">13</span>
<span class="bp">-</span><span class="mi">3</span>
<span class="bp">-</span><span class="mi">8</span>
<span class="bp">+</span><span class="mi">14</span>
<span class="bp">+</span><span class="mi">16</span>
</pre></div>

#### [ Patrick Massot (Dec 01 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150686187):
<p>No, I decided I should stop distractions for a while. And also the question looked masochistic to do in functional rather than imperative language</p>

#### [ Patrick Massot (Dec 01 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150686195):
<p>Mario, was that all your input?</p>

#### [ Bryan Gin-ge Chen (Dec 01 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150687782):
<p>I had to use <code>#eval (0 : int)</code> since the first line of the input was negative.</p>

#### [ Reid Barton (Dec 02 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150703402):
<p>I solved it too. But my solution took 40 seconds to run</p>

#### [ Reid Barton (Dec 02 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150703410):
<p>The first part, I mean</p>

#### [ Reid Barton (Dec 02 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150703754):
<p>Doing the second part in non-meta Lean seems pretty interesting</p>

#### [ Mario Carneiro (Dec 02 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150715253):
<p>I think this is a good test case for the conventional programming capabilities of lean. Here's my solution for day 2 pt 1:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">system</span><span class="bp">.</span><span class="n">io</span> <span class="n">data</span><span class="bp">.</span><span class="n">buffer</span><span class="bp">.</span><span class="n">parser</span> <span class="n">meta</span><span class="bp">.</span><span class="n">rb_map</span> <span class="n">data</span><span class="bp">.</span><span class="n">list</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">open</span> <span class="n">parser</span>

<span class="n">def</span> <span class="n">letter</span> <span class="o">:</span> <span class="n">parser</span> <span class="n">char</span> <span class="o">:=</span>
<span class="n">sat</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">c</span><span class="o">,</span> <span class="err">&#39;</span><span class="n">a&#39;</span><span class="bp">.</span><span class="n">to_nat</span> <span class="bp">≤</span> <span class="n">c</span><span class="bp">.</span><span class="n">to_nat</span> <span class="bp">∧</span> <span class="n">c</span><span class="bp">.</span><span class="n">to_nat</span> <span class="bp">≤</span> <span class="err">&#39;</span><span class="n">z&#39;</span><span class="bp">.</span><span class="n">to_nat</span><span class="o">)</span>

<span class="n">def</span> <span class="n">count1</span> <span class="o">{</span><span class="n">α</span> <span class="n">lt</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_rel</span> <span class="n">lt</span><span class="o">]</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="n">rbmap</span> <span class="n">α</span> <span class="bp">ℕ</span> <span class="n">lt</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">rbmap</span> <span class="n">α</span> <span class="bp">ℕ</span> <span class="n">lt</span> <span class="o">:=</span>
<span class="n">c</span><span class="bp">.</span><span class="n">insert</span> <span class="n">a</span> <span class="err">$</span> <span class="k">match</span> <span class="n">c</span><span class="bp">.</span><span class="n">find</span> <span class="n">a</span> <span class="k">with</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">some</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span>
<span class="bp">|</span> <span class="n">none</span> <span class="o">:=</span> <span class="mi">1</span>
<span class="kn">end</span>

<span class="n">def</span> <span class="n">get_counts</span> <span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">char</span><span class="o">)</span> <span class="o">:</span> <span class="n">bool</span> <span class="bp">×</span> <span class="n">bool</span> <span class="o">:=</span>
<span class="k">let</span> <span class="n">m</span> <span class="o">:=</span> <span class="n">list</span><span class="bp">.</span><span class="n">foldl</span> <span class="n">count1</span> <span class="o">(</span><span class="n">mk_rbmap</span> <span class="n">char</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="n">l</span> <span class="k">in</span>
<span class="n">m</span><span class="bp">.</span><span class="n">fold</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">c</span> <span class="n">n</span> <span class="bp">⟨</span><span class="n">r₁</span><span class="o">,</span> <span class="n">r₂</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">r₁</span> <span class="bp">∨</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">2</span><span class="o">,</span> <span class="n">r₂</span> <span class="bp">∨</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">3</span><span class="bp">⟩</span><span class="o">)</span> <span class="o">(</span><span class="n">ff</span><span class="o">,</span> <span class="n">ff</span><span class="o">)</span>

<span class="bp">#</span><span class="kn">eval</span> <span class="n">do</span>
  <span class="n">s</span> <span class="err">←</span> <span class="n">io</span><span class="bp">.</span><span class="n">fs</span><span class="bp">.</span><span class="n">read_file</span> <span class="s2">&quot;dat.txt&quot;</span><span class="o">,</span>
  <span class="n">sum</span><span class="bp">.</span><span class="n">inr</span> <span class="n">ls</span> <span class="err">←</span> <span class="n">return</span> <span class="err">$</span> <span class="n">run</span> <span class="o">(</span><span class="n">many</span> <span class="o">(</span><span class="n">many</span> <span class="n">letter</span> <span class="bp">&lt;*</span> <span class="n">ch</span> <span class="err">&#39;\</span><span class="n">n&#39;</span><span class="o">))</span> <span class="n">s</span><span class="o">,</span>
  <span class="k">let</span> <span class="o">(</span><span class="n">l₁</span><span class="o">,</span> <span class="n">l₂</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">ls</span><span class="bp">.</span><span class="n">map</span> <span class="n">get_counts</span><span class="o">)</span><span class="bp">.</span><span class="n">unzip</span><span class="o">,</span>
  <span class="n">trace</span> <span class="o">(</span><span class="n">to_string</span> <span class="o">(</span><span class="n">l₁</span><span class="bp">.</span><span class="n">count</span> <span class="n">tt</span> <span class="bp">*</span> <span class="n">l₂</span><span class="bp">.</span><span class="n">count</span> <span class="n">tt</span><span class="o">))</span> <span class="o">(</span><span class="n">return</span> <span class="o">())</span>
</pre></div>

#### [ Mario Carneiro (Dec 02 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150715398):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span>  As for doing the day 1 pt 2 in non-meta lean, it was obviously intended to have a solution with unbounded iteration, and it is possible to have such a program never halt on some inputs. With some significant additional work you can actually decide whether an input will halt (by looking at whether the numbers are all distinct mod the period), and so you could get a fully correct non-meta lean solution that way (which is even better than the naive algorithm because it will tell you when the infinite stream has no duplicates).</p>
<p>But if you just want the easy solution, the simplest approach is just to have a depth limiter, and increase it until you get the answer.</p>

#### [ Mario Carneiro (Dec 03 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150794896):
<p>To avoid spamming the chat I won't report daily, but I think I will take up this challenge. Follow along at <a href="https://github.com/digama0/advent-of-code" target="_blank" title="https://github.com/digama0/advent-of-code">https://github.com/digama0/advent-of-code</a> (spoiler alert)</p>

#### [ Edward Ayers (Dec 04 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150837825):
<p>On part day 1 part 2, I believe you can show that the search terminates if two elements of your list are equal mod (answer to part 1). So I started coding up a non-meta algorithm but then I realized it would sap away my entire Saturday so I stopped.</p>

#### [ Mario Carneiro (Dec 04 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150837987):
<p>Did you see my solution?</p>

#### [ Mario Carneiro (Dec 04 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150837992):
<p>I did that algorithm</p>

#### [ Mario Carneiro (Dec 04 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150838001):
<p>and it did sap a good chunk of my day ;)</p>

#### [ Mario Carneiro (Dec 04 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150838140):
<p>you can actually do a bit better than producing a proof of well foundedness to run the search... when two values have the same mod the period, you find the least difference of divs, and that's where the search will terminate (so you can do the whole thing without actually running those passes)</p>

#### [ Edward Ayers (Dec 04 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150838882):
<p>Yeah that's how I was going to do it.</p>

#### [ Edward Ayers (Dec 04 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150839362):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> thanks for sharing your solutions. There are still lots of language/mathlib features I am neglecting! Eg <code>withtop</code></p>

#### [ Edward Ayers (Dec 04 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150841457):
<p>Also <span class="user-mention" data-user-id="110049">@Mario Carneiro</span>  in the parsers for numbers and letters you can use <code>sat $ char.is_lower</code> and <code>char.is_digit</code> instead of manually checking the char.</p>

#### [ Mario Carneiro (Dec 04 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150841473):
<p>oh, lovely</p>

#### [ Mario Carneiro (Dec 04 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150841529):
<p>I'm hoping that the conventional programming capabilities of lean will be boosted by these attempts</p>


{% endraw %}
