---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/24816Isthereavariantofsimpthathandlesreversesimps.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Is there a variant of `simp` that handles reverse simps?](https://leanprover-community.github.io/archive/113489newmembers/24816Isthereavariantofsimpthathandlesreversesimps.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Nov 18 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Is%20there%20a%20variant%20of%20%60simp%60%20that%20handles%20reverse%20simps%3F/near/147897139):
<p>Is there a variant of <code>simp</code> so I can write things like <code>simp [←P, Q]</code> or <code>simp only [←P, Q]</code> where <code>P</code> and <code>Q</code> may or may not be <code>simp</code> lemmas?</p>

#### [ Kenny Lau (Nov 18 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Is%20there%20a%20variant%20of%20%60simp%60%20that%20handles%20reverse%20simps%3F/near/147897178):
<p>nope. you need to do <code>P.symm</code></p>

#### [ Mario Carneiro (Nov 18 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Is%20there%20a%20variant%20of%20%60simp%60%20that%20handles%20reverse%20simps%3F/near/147897184):
<p>and you alsso need to remove <code>P</code> if it is a simp lemma or it will go into a loop</p>

#### [ Chris Hughes (Nov 18 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Is%20there%20a%20variant%20of%20%60simp%60%20that%20handles%20reverse%20simps%3F/near/147897700):
<p>remove <code>P</code>, means do <code>simp [P.symm, -P]</code></p>

#### [ Mario Carneiro (Nov 18 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Is%20there%20a%20variant%20of%20%60simp%60%20that%20handles%20reverse%20simps%3F/near/147898210):
<p>maybe we should write <code>simp'</code>? I'm sure this isn't the last tweak we will want</p>


{% endraw %}
