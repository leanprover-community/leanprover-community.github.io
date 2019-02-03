---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/65987453irrationallean.html
---

## Stream: [PR reviews](index.html)
### Topic: [#453 irrational.lean](65987453irrationallean.html)

---


{% raw %}
#### [ Kevin Buzzard (Nov 01 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23453%20irrational.lean/near/136888753):
<p><span class="user-mention" data-user-id="132603">@Calle Sönne</span>  <span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span>  and <span class="user-mention" data-user-id="132889">@Jean Lo</span>  are all first year undergraduates at Imperial (who'd never used Lean 1 month ago) and this is joint work of theirs, subsequently tidied up by Chris and Kenny. The genesis of this project was some basic example sheet questions from my course, but it then it grew a bit. It feels to me like most of the things you'd ever want to know about irrational numbers, modulo theorems such as e or pi is irrational (the latter probably being hard to formalise).</p>

#### [ Mario Carneiro (Nov 04 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23453%20irrational.lean/near/137135207):
<p>I had a 'whaaaat' moment when I saw <a href="https://github.com/leanprover/mathlib/blob/9e888483c6532e4d3719a8b63696c14dc1b36040/data/rat.lean#L1045-L1046" target="_blank" title="https://github.com/leanprover/mathlib/blob/9e888483c6532e4d3719a8b63696c14dc1b36040/data/rat.lean#L1045-L1046"><code>rat.sqrt</code></a>. For fun, here's a plot of the behavior of this function:<br>
<a href="/user_uploads/3121/eM1mUm8wVIf29WCMLI8kN9ha/sqrt.png" target="_blank" title="sqrt.png">sqrt.png</a> <br>
I suspect it is dense in the top half-plane.</p>
<div class="message_inline_image"><a href="/user_uploads/3121/eM1mUm8wVIf29WCMLI8kN9ha/sqrt.png" target="_blank" title="sqrt.png"><img src="/user_uploads/3121/eM1mUm8wVIf29WCMLI8kN9ha/sqrt.png"></a></div>

#### [ Mario Carneiro (Nov 04 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23453%20irrational.lean/near/137135720):
<p>Correction: it's not dense in the top half-plane, and its closure is probably just the real square root function (plus countably many discrete points). Because the "jumps" away from the real square root function are smaller for better approximations, so there is a finite number of points which differ by more than <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>ϵ</mi></mrow><annotation encoding="application/x-tex">\epsilon</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">ϵ</span></span></span></span> from the real square root (on a bounded interval).</p>

#### [ Kenny Lau (Nov 05 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23453%20irrational.lean/near/146797600):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> <span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> <span class="user-mention" data-user-id="132889">@Jean Lo</span> <span class="user-mention" data-user-id="132603">@Calle Sönne</span> It has been merged</p>


{% endraw %}
