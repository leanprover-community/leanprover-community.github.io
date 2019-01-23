---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/95664pedagogyvsdumpinginternalrepresentation.html
---

## Stream: [general](index.html)
### Topic: [pedagogy vs. "dumping internal representation"](95664pedagogyvsdumpinginternalrepresentation.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Sullivan (Aug 02 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pedagogy%20vs.%20%22dumping%20internal%20representation%22/near/130789249):
Here are five lines of code:, a short version of the Hello World of Lean, suitable as a first example for even new undergraduate students. The problem pedagogically is that  the result of  #eval is a cryptic message about no typeclass instance,  the dumping of an internal representation, and some #1s and other stuff. I understand what's going on here; the question is whether I can get Lean to show results in a readable form without defining typeclass instances. Coq's good in this regard, for example. How might I get the same effect in Lean. 

inductive day 
| monday: day
| tuesday: day

def id_day (d: day): day := d

#eval id_day day.monday

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 02 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pedagogy%20vs.%20%22dumping%20internal%20representation%22/near/130789325):
#reduce

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Sullivan (Aug 02 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pedagogy%20vs.%20%22dumping%20internal%20representation%22/near/130789982):
```quote
#reduce
```
Of course, thanks.


{% endraw %}
