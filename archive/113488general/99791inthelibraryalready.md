---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99791inthelibraryalready.html
---

## Stream: [general](index.html)
### Topic: [in the library already?](99791inthelibraryalready.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 14 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/in%20the%20library%20already%3F/near/132078222):
Is this in the library somewhere?
```
def list.split_on_aux {α} [decidable_eq α] (a : α) : list α → list α → list (list α) 
| [] l       := [l.reverse]
| (h :: t) l := if h = a then
                  l.reverse :: (list.split_on_aux t [])
                else
                  list.split_on_aux t (h :: l)

def list.split_on {α} [decidable_eq α] (a : α) : list α → list (list α) 
| l := list.split_on_aux a l []
```


{% endraw %}
