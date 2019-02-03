---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/42731algebraonsubtypes.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [algebra on subtypes](https://leanprover-community.github.io/archive/116395maths/42731algebraonsubtypes.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Jul 19 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129923410):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> Simon has been working for us, and Mario promptly merged. You can update mathlib to at least c2f54ad03 and try to understand how to use the magic in <a href="https://gist.github.com/PatrickMassot/8afef3917a917300cf31c1396a895705" target="_blank" title="https://gist.github.com/PatrickMassot/8afef3917a917300cf31c1396a895705">https://gist.github.com/PatrickMassot/8afef3917a917300cf31c1396a895705</a></p>

#### [ Johan Commelin (Jul 19 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129926331):
<p>Looks interesting! I'm updating (-;</p>

#### [ Johan Commelin (Jul 19 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129926592):
<p>I really like where this is going! You give it the data (zero, addition, ...) and for the properties (assoc, comm, ...) you just tell Lean: look, follow your nose and you'll get there.</p>

#### [ Patrick Massot (Jul 19 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129926847):
<p>Indeed. This now really looks like what you would wrote on paper: explain why operations make sense and then write either nothing  or "algebraic axioms follow from the parent structure axiom"</p>

#### [ Patrick Massot (Jul 19 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129926851):
<p>And this will be reused a lot. Each algebraic structure need subtype instances</p>

#### [ Patrick Massot (Jul 19 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129926923):
<p>Note that <code>refine_struct</code> is an ongoing long-term collaboration effort using all available strengths: I do the whining and Simon does the coding. It started with the <code>pi_instance</code> tactic back in February I think</p>

#### [ Johan Commelin (Jul 19 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927028):
<p>Ok, so here are some explicit kudos to <span class="user-mention" data-user-id="110026">@Simon Hudon</span> <span class="emoji emoji-1f44d" title="thumbs up">:thumbs_up:</span> <span class="emoji emoji-1f389" title="tada">:tada:</span> <span class="emoji emoji-1f419" title="octopus">:octopus:</span> <span class="emoji emoji-1f370" title="cake">:cake:</span> <span class="emoji emoji-1f6e0" title="hammer and wrench">:hammer_and_wrench:</span> <span class="emoji emoji-1f4aa" title="muscle">:muscle:</span></p>

#### [ Johan Commelin (Jul 19 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927113):
<p>I do wonder, in how far is this overlapping with Scott's tactics? I don't fully understand what his <code>obviously</code> does, but it is also related to deriving obvious results from fields in structures and such, right?</p>

#### [ Mario Carneiro (Jul 19 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927179):
<p><code>obviously</code> is one of several "hammer" style tactics by scott</p>

#### [ Mario Carneiro (Jul 19 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927180):
<p>i.e. "throw every automation we have at the problem until it buckles"</p>

#### [ Mario Carneiro (Jul 19 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927242):
<p>I don't think <code>refine_struct</code> does anything like this</p>

#### [ Johan Commelin (Jul 19 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927259):
<p>Agreed, but vice versa? Would most of these goals buckle under <del>Thor's</del> Scott's hammer?</p>

#### [ Patrick Massot (Jul 19 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927315):
<p>No, <code>refine_struct</code> by itself carefully understand and name what Lean wants to be proved. Then specialized automation like <a href="https://github.com/leanprover/mathlib/blob/master/algebra/pi_instances.lean#L16" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/algebra/pi_instances.lean#L16">https://github.com/leanprover/mathlib/blob/master/algebra/pi_instances.lean#L16</a> or <a href="https://gist.github.com/PatrickMassot/8afef3917a917300cf31c1396a895705#file-subtypes-lean-L9" target="_blank" title="https://gist.github.com/PatrickMassot/8afef3917a917300cf31c1396a895705#file-subtypes-lean-L9">https://gist.github.com/PatrickMassot/8afef3917a917300cf31c1396a895705#file-subtypes-lean-L9</a> take over.</p>

#### [ Johan Commelin (Jul 19 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927370):
<p>Since Lean supports unicode, I think we really should have a tactic called <a href="https://en.wikipedia.org/wiki/Mj%C3%B6lnir" target="_blank" title="https://en.wikipedia.org/wiki/Mj%C3%B6lnir">Mjölnir</a>.</p>

#### [ Kevin Buzzard (Jul 19 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927543):
<p>You should propose a unicode character for that thing</p>

#### [ Patrick Massot (Jul 19 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927555):
<p>Let's ask google how to spell that in runes</p>

#### [ Patrick Massot (Jul 19 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927563):
<p>And then we can email Jasmin and give him one more incentive to bring us that hammer thing</p>

#### [ Patrick Massot (Jul 19 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927614):
<p>Looks like this could be our winner: <a href="https://static1.fjcdn.com/comments/Spelled+the+right+way+_47df3c7a85289a0912599c30d252cf08.jpg" target="_blank" title="https://static1.fjcdn.com/comments/Spelled+the+right+way+_47df3c7a85289a0912599c30d252cf08.jpg">https://static1.fjcdn.com/comments/Spelled+the+right+way+_47df3c7a85289a0912599c30d252cf08.jpg</a></p>
<div class="message_inline_image"><a href="https://static1.fjcdn.com/comments/Spelled+the+right+way+_47df3c7a85289a0912599c30d252cf08.jpg" target="_blank" title="https://static1.fjcdn.com/comments/Spelled+the+right+way+_47df3c7a85289a0912599c30d252cf08.jpg"><img src="https://static1.fjcdn.com/comments/Spelled+the+right+way+_47df3c7a85289a0912599c30d252cf08.jpg"></a></div>

#### [ Kenny Lau (Jul 19 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927691):
<blockquote>
<p>Let's ask google how to spell that in runes</p>
</blockquote>
<p>ᛗᛃᛟᛚᚾᛁᚱ</p>

#### [ Mario Carneiro (Jul 19 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927701):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="err">ᛗᛃᛟᛚᚾᛁᚱ</span> <span class="o">:=</span> <span class="k">by</span> <span class="err">ᛗᛃᛟᛚᚾᛁᚱ</span>
</pre></div>

#### [ Patrick Massot (Jul 19 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927730):
<p>Too bad: I tried <code>meta def ᛗᛃᛟᛚᚾᛁᚱ : tactic unit := sorry</code> but Lean complains <code>invalid declaration, identifier expected</code></p>

#### [ Patrick Massot (Jul 19 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927771):
<p>It seems we'll need some help from <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span></p>

#### [ Mario Carneiro (Jul 19 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927772):
<div class="codehilite"><pre><span></span>meta def «ᛗᛃᛟᛚᚾᛁᚱ» : tactic unit := sorry
</pre></div>

#### [ Sean Leather (Jul 19 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927808):
<p>Guillemets: how appropriate.</p>

#### [ Mario Carneiro (Jul 19 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927817):
<p>problem solved:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="err">«ᛗᛃᛟᛚᚾᛁᚱ»</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="kn">notation</span> <span class="bp">`</span><span class="err">ᛗᛃᛟᛚᚾᛁᚱ</span><span class="bp">`</span> <span class="o">:=</span> <span class="err">«ᛗᛃᛟᛚᚾᛁᚱ»</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span> <span class="k">by</span> <span class="err">ᛗᛃᛟᛚᚾᛁᚱ</span>
</pre></div>

#### [ Patrick Massot (Jul 19 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927870):
<p>This works! We're almost set. It only remains to whine long enough for someone to unsorry this</p>

#### [ Mario Carneiro (Jul 19 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927879):
<p>obviously <code>meta def «ᛗᛃᛟᛚᚾᛁᚱ» : tactic unit :=  by ᛗᛃᛟᛚᚾᛁᚱ</code></p>

#### [ Johan Commelin (Jul 19 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927891):
<p>I like your use of "obviously"</p>

#### [ Patrick Massot (Jul 19 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/algebra%20on%20subtypes/near/129927939):
<p>We shouldn't forget the PR to <a href="https://github.com/leanprover/vscode-lean/blob/master/translations.json" target="_blank" title="https://github.com/leanprover/vscode-lean/blob/master/translations.json">https://github.com/leanprover/vscode-lean/blob/master/translations.json</a></p>


{% endraw %}
