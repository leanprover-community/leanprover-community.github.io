---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/04281matrices.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [matrices](https://leanprover-community.github.io/archive/113488general/04281matrices.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Andrew Ashworth (Apr 08 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/124777985):
<p>any of the coq experts out there know what the most complete linalg / tensor package is out there for theorem provers? I'd like to look into what's out there for computing with complex matrices. quaternions would be cool too</p>

#### [ Andrew Ashworth (Apr 08 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/124778185):
<p>the top referenced paper is this: <a href="http://www.math.ias.edu/~amortberg/papers/coqeal.pdf" target="_blank" title="http://www.math.ias.edu/~amortberg/papers/coqeal.pdf">http://www.math.ias.edu/~amortberg/papers/coqeal.pdf</a></p>

#### [ Yulia Zaplatina (Jul 13 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129593334):
<p>I am slightly stuck on the definition of a GL group,  has anyone defined matrices yet?</p>

#### [ Kenny Lau (Jul 13 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129593382):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> your year 2 student?</p>

#### [ Kevin Buzzard (Jul 13 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129593530):
<p><span class="user-mention" data-user-id="120469">@Ellen Arlt</span> wrote some very basic code for matrices -- defining not much more than addition and multiplication, but it might be enough to define GL. <span class="user-mention" data-user-id="119876">@Blair Shi</span> <span class="user-mention" data-user-id="119876">@Blair Shi</span> I should tell you about this too. I think that both of you might be thinking about linear algebra and more specifically finite-dimensional vector spaces. </p>
<p>Oh -- I found Ellen's code! <a href="https://github.com/kbuzzard/xena/blob/master/student_contributions/Ellen_Arlt_matrix_rings.lean" target="_blank" title="https://github.com/kbuzzard/xena/blob/master/student_contributions/Ellen_Arlt_matrix_rings.lean">https://github.com/kbuzzard/xena/blob/master/student_contributions/Ellen_Arlt_matrix_rings.lean</a> . She proves that square matrices form a ring. <span class="user-mention" data-user-id="110064">@Kenny Lau</span> presumably there is "units of a ring" somewhere?</p>

#### [ Kenny Lau (Jul 13 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129593729):
<p>yes</p>

#### [ Kenny Lau (Jul 13 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129593730):
<p><code>units \a</code></p>

#### [ Kenny Lau (Jul 13 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129593732):
<p>works for fake rings also</p>

#### [ Yulia Zaplatina (Jul 13 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129593733):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>  Thank you!</p>

#### [ Yulia Zaplatina (Jul 13 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129593868):
<p>Could we add <span class="user-mention" data-user-id="120469">@Ellen Arlt</span> 's code to mathlib so we don't have to define matrices every time?</p>

#### [ Blair Shi (Jul 13 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129594650):
<p>Wow, I think this might be useful for my vector space. Thank you for telling me about this.</p>

#### [ Kevin Buzzard (Jul 13 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129598579):
<p>I think it would be easier to just put it into our UROP repo. It's time to start a xenalib!</p>

#### [ Simon Hudon (Jul 13 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129602034):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> <span class="user-mention" data-user-id="120469">@Ellen Arlt</span> I suggest you remove the <code>ring</code> constraint in:</p>
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">R</span><span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="n">m</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">:=</span>  <span class="n">fin</span> <span class="n">n</span> <span class="bp">→</span><span class="o">(</span> <span class="n">fin</span> <span class="n">m</span> <span class="bp">→</span> <span class="n">R</span> <span class="o">)</span>
</pre></div>


<p>It makes it less useable in new and creative ways and it doesn't add any value: the ring assumption is really useful only for the operations and lemmas.</p>

#### [ Kevin Buzzard (Jul 13 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129604111):
<p>I'm busy today doing admin but I dumped ellen's code and Sean's comments on it here <a href="https://github.com/ImperialCollegeLondon/xena-UROP-2018/tree/master/src/xenalib" target="_blank" title="https://github.com/ImperialCollegeLondon/xena-UROP-2018/tree/master/src/xenalib">https://github.com/ImperialCollegeLondon/xena-UROP-2018/tree/master/src/xenalib</a></p>

#### [ Kevin Buzzard (Jul 13 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129604201):
<p><span class="user-mention" data-user-id="120736">@Yulia Zaplatina</span> if you pull the xena-UROP-2018 repo and open the folder in VS Code then you should be able to type stuff like <code>import xenalib/Ellen_Arlt_matrix_rings</code> and get her definitions. Someone should merge Sean's edits as well but I need to go and throw eggs at Trump</p>


{% endraw %}
