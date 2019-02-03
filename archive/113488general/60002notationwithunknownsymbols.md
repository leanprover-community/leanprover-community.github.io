---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/60002notationwithunknownsymbols.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [notation with unknown symbols](https://leanprover-community.github.io/archive/113488general/60002notationwithunknownsymbols.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Apr 21 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496391):
<p>Is it possible to have notation using unknown symbols? Say I want a new notation for lambda abstraction (this is not my use case, I try to minimize). I try:</p>
<div class="codehilite"><pre><span></span><span class="kn">notation</span> <span class="bp">`</span><span class="n">mkfun</span><span class="bp">`</span> <span class="n">x</span> <span class="bp">`</span><span class="o">,</span><span class="bp">`</span> <span class="n">f</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">f</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">mkfun</span> <span class="n">x</span><span class="o">,</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span>
</pre></div>


<p>But it fails with <code>unknown identifier 'x'</code></p>

#### [ Gabriel Ebner (Apr 21 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496442):
<p>You might want to check out how the notation for ∃ is defined: <a href="https://github.com/leanprover/lean/blob/f59c2f0ef59fdc1833b6ead6adca721123bd7932/library/init/logic.lean#L532-L533" target="_blank" title="https://github.com/leanprover/lean/blob/f59c2f0ef59fdc1833b6ead6adca721123bd7932/library/init/logic.lean#L532-L533">https://github.com/leanprover/lean/blob/f59c2f0ef59fdc1833b6ead6adca721123bd7932/library/init/logic.lean#L532-L533</a></p>

#### [ Patrick Massot (Apr 21 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496451):
<p>Thanks, it looks promising</p>

#### [ Simon Hudon (Apr 21 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496452):
<p>It works with the <code>binder</code> / <code>binders</code> keywords and <code>scoped</code></p>

#### [ Patrick Massot (Apr 21 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496498):
<p>any chance this <code>r:(</code> thing is documented somewhere?</p>

#### [ Patrick Massot (Apr 21 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496503):
<p>oh, <code>binders</code> is also a special word here?</p>

#### [ Simon Hudon (Apr 21 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496504):
<p>Kevin and I had a long conversation about it on gitter. Let's see if I can find it again</p>

#### [ Simon Hudon (Apr 21 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496505):
<p>yes</p>

#### [ Simon Hudon (Apr 21 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496617):
<p><span class="emoji emoji-261d" title="point up">:point_up:</span> <a href="https://gitter.im/leanprover_public/Lobby?at=5a5691dd83152df26d570d0f" target="_blank" title="https://gitter.im/leanprover_public/Lobby?at=5a5691dd83152df26d570d0f">January 10, 2018 5:21 PM</a></p>

#### [ Simon Hudon (Apr 21 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496679):
<p>In short <code>r:(...)</code> gives a name to an expression that can be built in one of two ways:</p>
<ul>
<li><code>scoped</code></li>
<li><code>foldl</code> / <code>foldr</code></li>
</ul>
<p>In <code>r:(scoped p, ...)</code>, <code>p</code> is a bound variable that you can use in <code>...</code>. It will be replaced with a lambda abstraction</p>

#### [ Patrick Massot (Apr 21 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496781):
<p>It sorts of make sense, but not to the point where I could fix my <code>mkfun</code> example</p>

#### [ Patrick Massot (Apr 21 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496787):
<p>oh wait</p>

#### [ Patrick Massot (Apr 21 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496788):
<p>I can actually</p>

#### [ Patrick Massot (Apr 21 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496790):
<p><code>notation `mkfun` binders `,` r:(scoped f, f) := r</code> does work</p>

#### [ Simon Hudon (Apr 21 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496877):
<p>So, if I may ask, why are you making fun of lambda abstractions?</p>

#### [ Patrick Massot (Apr 21 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496885):
<p>I laughed. Do you also want an answer?</p>

#### [ Simon Hudon (Apr 21 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496887):
<p>Both are appreciated <span class="emoji emoji-1f606" title="laughing">:laughing:</span></p>

#### [ Patrick Massot (Apr 21 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496922):
<p>I'm trying to setup some notations for sums and products</p>

#### [ Patrick Massot (Apr 21 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496937):
<p>I would like to be able to write something like <code>def f := λ n, Sum_{0 ≤ i ≤ n} i^2</code></p>

#### [ Patrick Massot (Apr 21 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496938):
<p>I have no problem defining such a function</p>

#### [ Patrick Massot (Apr 21 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496939):
<p>Using <code>list.sum</code> and <code>list.range</code></p>

#### [ Patrick Massot (Apr 21 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496979):
<p>I have trouble setting up the notation</p>

#### [ Simon Hudon (Apr 21 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496981):
<p>Cool :) btw, would it be useful to you to have a notation for <code>classical.epsilon</code>: <code>ε x, 1 ≤ x ≤ 3</code>?</p>

#### [ Kenny Lau (Apr 21 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496982):
<p>not sure how easy it would be to implement it</p>

#### [ Kenny Lau (Apr 21 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496983):
<p>I mean, what are you going to produce when there is no such element</p>

#### [ Kenny Lau (Apr 21 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125496991):
<p>in classical Hilbert epsilon it is supposed to produce "whatever"</p>

#### [ Simon Hudon (Apr 21 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497039):
<p><code>classical.epsilon</code> already exists. It's only defined on nonempty types. When no such <code>x</code> exists, an arbitrary value is picked</p>

#### [ Kenny Lau (Apr 21 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497042):
<p>but then it is empty</p>

#### [ Kenny Lau (Apr 21 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497043):
<p>what is going to be the type of the output</p>

#### [ Simon Hudon (Apr 21 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497054):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Do you have a special provision for infinite sets in <code>Sum_{ ... }</code>?</p>

#### [ Patrick Massot (Apr 21 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497087):
<p>I was thinking about finite sums here</p>

#### [ Patrick Massot (Apr 21 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497102):
<p>Really I want to convert </p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">data</span><span class="bp">.</span><span class="n">list</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">open</span> <span class="n">list</span>
<span class="n">def</span> <span class="n">f</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">sum</span> <span class="o">(</span><span class="n">map</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="n">i</span><span class="bp">*</span><span class="n">i</span><span class="o">)</span> <span class="o">(</span><span class="n">range</span> <span class="n">n</span><span class="o">))</span>
</pre></div>


<p>to what I wrote earlier</p>

#### [ Patrick Massot (Apr 21 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497105):
<p>having a nice notation</p>

#### [ Patrick Massot (Apr 21 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497143):
<p>where the name of the bound variable i is not hard-wired in the notation</p>

#### [ Simon Hudon (Apr 21 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497161):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> here is the type of <code>epsilon</code>:</p>
<div class="codehilite"><pre><span></span><span class="n">noncomputable</span> <span class="n">def</span> <span class="n">epsilon</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">h</span> <span class="o">:</span> <span class="n">nonempty</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="o">:=</span>
</pre></div>

#### [ Kenny Lau (Apr 21 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497205):
<p>oh, I misinterpreted everything</p>

#### [ Simon Hudon (Apr 21 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497212):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> <br>
How about this as the underlying function:</p>
<div class="codehilite"><pre><span></span><span class="n">sum</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="bp">→</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">...</span>
</pre></div>


<p>Basically, the notation should be hardwired to fix an upper bound on the range</p>

#### [ Simon Hudon (Apr 21 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497251):
<p>but you still get to filter individual terms</p>

#### [ Patrick Massot (Apr 21 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497312):
<p>I don't really care about the underlying function. I want my notation with only the formula in term of i, not prefaced with a lambda</p>

#### [ Simon Hudon (Apr 21 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497355):
<p>One step at a time, young padawan, I'm getting there</p>

#### [ Patrick Massot (Apr 21 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497521):
<p>I'm making progress</p>
<div class="codehilite"><pre><span></span><span class="kn">notation</span> <span class="bp">`</span><span class="n">Sum_</span><span class="o">{</span><span class="bp">`</span> <span class="n">binders</span> <span class="bp">`≤`</span> <span class="n">n</span> <span class="bp">`</span><span class="o">}</span><span class="bp">`</span> <span class="n">r</span><span class="o">:(</span><span class="n">scoped</span> <span class="n">f</span><span class="o">,</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sum</span> <span class="o">(</span><span class="n">map</span> <span class="n">f</span> <span class="err">$</span> <span class="n">range</span> <span class="n">n</span><span class="o">)</span>
<span class="bp">#</span><span class="kn">eval</span> <span class="n">Sum_</span><span class="o">{</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">≤</span> <span class="mi">4</span><span class="o">}</span> <span class="n">i</span><span class="bp">*</span><span class="n">i</span>
</pre></div>

#### [ Simon Hudon (Apr 21 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497568):
<p>Not bad!</p>

#### [ Simon Hudon (Apr 21 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497597):
<p>I was trying:</p>
<div class="codehilite"><pre><span></span><span class="kn">notation</span> <span class="bp">`</span><span class="err">ΣΣ</span> <span class="bp">`</span> <span class="n">binder</span> <span class="bp">`</span> <span class="bp">|</span> <span class="bp">`</span> <span class="n">f</span><span class="o">:(</span><span class="n">scoped</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span><span class="o">)</span> <span class="bp">∧</span> <span class="n">ub</span><span class="o">:(</span><span class="n">scoped</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span><span class="o">)</span> <span class="bp">`</span> <span class="bp">≤</span> <span class="bp">`</span> <span class="n">n</span> <span class="bp">`</span><span class="o">,</span> <span class="bp">`</span> <span class="n">t</span><span class="o">:(</span><span class="n">scoped</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">sum&#39;</span> <span class="n">n</span> <span class="n">f</span> <span class="n">t</span>

<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="err">ΣΣ</span> <span class="n">x</span> <span class="bp">|</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">≤</span> <span class="mi">7</span><span class="o">,</span> <span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="bp">≤</span> <span class="mi">7</span> <span class="o">:=</span> <span class="bp">_</span>
</pre></div>


<p>But I think you're not allowed to use <code>scoped</code> so many times.</p>

#### [ Patrick Massot (Apr 21 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497617):
<p>I can even replace <code>(i : ℕ)</code> by <code>(i)</code> but not by <code>i</code></p>

#### [ Simon Hudon (Apr 21 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497623):
<p>Not <code>i</code>? What error does it give you?</p>

#### [ Patrick Massot (Apr 21 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497666):
<p>invalid expression</p>

#### [ Simon Hudon (Apr 21 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497675):
<p>That's intriguing. You may want to try giving precedences to the tokens: <code> ` ≤ `:0</code></p>

#### [ Simon Hudon (Apr 21 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497718):
<p>I'll catch up with you later. There an adorable 2 year old here who needs attention :)</p>

#### [ Patrick Massot (Apr 21 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497720):
<p>Too bad, I was hoping your nephew was also a Lean expert</p>

#### [ Patrick Massot (Apr 21 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497723):
<p>Have fun!</p>

#### [ Simon Hudon (Apr 21 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497729):
<p>He's more of an Idris kind of guy</p>

#### [ Patrick Massot (Apr 21 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497732):
<p><span class="emoji emoji-1f604" title="smile">:smile:</span></p>

#### [ Simon Hudon (Apr 21 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497733):
<p>His name is Idris but I assume that speaks to his parents preference of Idris over Agda and Lean</p>

#### [ Simon Hudon (Apr 21 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125497739):
<p>And not to the sexiness of Idris Elba <span class="emoji emoji-1f61c" title="stuck out tongue winking eye">:stuck_out_tongue_winking_eye:</span></p>

#### [ Patrick Massot (Apr 21 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125503970):
<p>Does anyone has a decidable predicate on nat at hand?</p>

#### [ Chris Hughes (Apr 21 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504018):
<p><code>pos</code></p>

#### [ Chris Hughes (Apr 21 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504019):
<p>Any predicate?</p>

#### [ Chris Hughes (Apr 21 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504060):
<p><code>(λ n : ℕ, true)</code> :-)</p>

#### [ Patrick Massot (Apr 21 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504061):
<p>Maybe somethin like even or odd exist somewhere and is decidable</p>

#### [ Patrick Massot (Apr 21 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504062):
<p>I need a decidable instance in the library</p>

#### [ Sebastian Ullrich (Apr 21 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504064):
<p>Fun fact: Idris has an <code>Elab</code> monad. Have you ever tried googling for "idris elab"?</p>

#### [ Reid Barton (Apr 21 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504071):
<p>there's <code>prime</code>, in <code>data.nat.prime</code></p>

#### [ Chris Hughes (Apr 21 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504072):
<p>even is decidable, if you define it as <code>n % 2 = 0</code></p>

#### [ Chris Hughes (Apr 21 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504117):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> I couldn't manage to use that instance to prove 3 is prime.</p>

#### [ Simon Hudon (Apr 21 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504118):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> I did some more experiment and I managed to define a syntax for <code>ΣΣ i, i ≥ 3 ∧ i &lt; 21 ∧ even i ▻ i^2</code> which guarantees that <code>i</code> is bounded. How do you like the notation? (I made the formula a bit ugly to demonstrate that the form is pretty flexible)</p>

#### [ Patrick Massot (Apr 21 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504165):
<p><code>#eval if nat.prime 3 then 1 else 0</code> does work here</p>

#### [ Patrick Massot (Apr 21 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504166):
<p>thanks</p>

#### [ Chris Hughes (Apr 21 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504217):
<p><code>example : 1 = if nat.prime 3 then (1 : ℕ) else (0 : ℕ) := rfl</code> doesn't work though unfortunately. It does work for 2 though</p>

#### [ Patrick Massot (Apr 21 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504502):
<p>My current achievements are at <a href="https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/bigop.lean" target="_blank" title="https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/bigop.lean">https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/bigop.lean</a></p>

#### [ Patrick Massot (Apr 21 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504503):
<p>I still has precedence issues</p>

#### [ Patrick Massot (Apr 21 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504508):
<p>But I'm already happy</p>

#### [ Patrick Massot (Apr 21 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504510):
<p>I have quite a lot of ways of computing 5!</p>

#### [ Patrick Massot (Apr 21 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504556):
<p>And I seems I was able to state a lemma about big product for an associative operator and apply it to addition in nat</p>

#### [ Patrick Massot (Apr 21 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504568):
<p>For those who didn't follow previous discussions, I'm going after <a href="http://hal.inria.fr/docs/00/33/11/93/PDF/main.pdf" target="_blank" title="http://hal.inria.fr/docs/00/33/11/93/PDF/main.pdf">http://hal.inria.fr/docs/00/33/11/93/PDF/main.pdf</a></p>

#### [ Simon Hudon (Apr 21 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504569):
<p>Nice!</p>

#### [ Simon Hudon (Apr 21 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504576):
<p>If you're interested, I've put my code here:</p>
<p><a href="https://gist.github.com/cipher1024/604d5ec28ceb29e80219ce6e69bb1ea4" target="_blank" title="https://gist.github.com/cipher1024/604d5ec28ceb29e80219ce6e69bb1ea4">https://gist.github.com/cipher1024/604d5ec28ceb29e80219ce6e69bb1ea4</a></p>

#### [ Mario Carneiro (Apr 21 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504617):
<p>Hopefully this will be resolved in lean 4 (<span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> vm replacements please) but right now you have to make a choice between VM efficient and kernel efficient. <code>decidable_prime_1</code> is kernel efficient and <code>decidable_prime</code> is VM efficient</p>

#### [ Mario Carneiro (Apr 21 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504622):
<p>the default one you get is <code>decidable_prime</code></p>

#### [ Patrick Massot (Apr 21 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504634):
<p><a href="https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/bigop.lean#L67" target="_blank" title="https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/bigop.lean#L67">https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/bigop.lean#L67</a> has no trouble suming primes numbers in <code>range 5</code></p>

#### [ Patrick Massot (Apr 21 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504637):
<p>That's scientific computing!</p>

#### [ Sebastian Ullrich (Apr 21 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504691):
<p>Lean 4 will use a simplifier on code to be compiled, which should also enable VM replacements</p>

#### [ Patrick Massot (Apr 21 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504928):
<p>What is the precedence voodoo I need to get rid of parentheses in  <a href="https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/bigop.lean#L71" target="_blank" title="https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/bigop.lean#L71">https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/bigop.lean#L71</a> ? I mean, everything on LHS of the equality is surrounded in parenthesis, otherwise it doesn't work. How to avoid that?</p>

#### [ Mario Carneiro (Apr 21 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504936):
<p>use a high precedence for left brackets and a low prec for right brackets</p>

#### [ Patrick Massot (Apr 21 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125504985):
<p>Which brackets?</p>

#### [ Chris Hughes (Apr 21 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125505203):
<p>There are alternatives characters for Pi and Sigma <code>\sum</code> and <code>\prod</code>.</p>

#### [ Patrick Massot (Apr 21 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125505208):
<p>I know, but they look weird in my VScode</p>

#### [ Patrick Massot (Apr 21 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125505209):
<p>too tall</p>

#### [ Patrick Massot (Apr 21 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125505213):
<p>But of course I like the semantic abbreviation</p>

#### [ Chris Hughes (Apr 21 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125505265):
<blockquote>
<p>too tall</p>
</blockquote>
<p>That's why they're called big operators.</p>

#### [ Mario Carneiro (Apr 21 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125505270):
<p><code>\sum</code> and <code>\Sigma</code> aren't the same</p>

#### [ Patrick Massot (Apr 21 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125505321):
<p>What do you mean?</p>

#### [ Patrick Massot (Apr 21 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125505322):
<p>Of course one is taller</p>

#### [ Patrick Massot (Apr 21 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125505323):
<p>But do you mean something else?</p>

#### [ Patrick Massot (Apr 21 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125505325):
<p>And of course we can give a different definition to different symbols</p>

#### [ Patrick Massot (Apr 21 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125506073):
<p>Oh, crap! My append lemma is not correct. Associativity is not enough, I really need a monoid.</p>

#### [ Patrick Massot (Apr 21 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125506130):
<p>Oh! I just used <code>rsimp</code> that <span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> explained earlier today!</p>

#### [ Patrick Massot (Apr 21 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125506170):
<p>No</p>

#### [ Patrick Massot (Apr 21 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20with%20unknown%20symbols/near/125506172):
<p>Actually Lean is hanging</p>


{% endraw %}
