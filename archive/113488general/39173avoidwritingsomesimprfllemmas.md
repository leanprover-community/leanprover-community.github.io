---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39173avoidwritingsomesimprfllemmas.html
---

## Stream: [general](index.html)
### Topic: [avoid writing (some?) simp-rfl lemmas](39173avoidwritingsomesimprfllemmas.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 27 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/avoid%20writing%20%28some%3F%29%20simp-rfl%20lemmas/near/148623451):
I've brought this up before, but I'dd really hope that there is a way to get rid of blocks like this:
```lean
section simp

section
variables {X Y : comma L₂ R} {f : X ⟶ Y} {l : L₁ ⟹ L₂}
@[simp] lemma map_left_obj_left  : ((map_left R l).obj X).left  = X.left                := rfl
@[simp] lemma map_left_obj_right : ((map_left R l).obj X).right = X.right               := rfl
@[simp] lemma map_left_obj_hom   : ((map_left R l).obj X).hom   = l.app X.left ≫ X.hom := rfl
@[simp] lemma map_left_map_left  : ((map_left R l).map f).left  = f.left                := rfl
@[simp] lemma map_left_map_right : ((map_left R l).map f).right = f.right               := rfl
end

section
variables {X Y : comma L R₁} {f : X ⟶ Y} {r : R₁ ⟹ R₂}
@[simp] lemma map_right_obj_left  : ((map_right L r).obj X).left  = X.left                 := rfl
@[simp] lemma map_right_obj_right : ((map_right L r).obj X).right = X.right                := rfl
@[simp] lemma map_right_obj_hom   : ((map_right L r).obj X).hom   = X.hom ≫ r.app X.right := rfl
@[simp] lemma map_right_map_left  : ((map_right L r).map f).left  = f.left                 := rfl
@[simp] lemma map_right_map_right : ((map_right L r).map f).right = f.right                := rfl
end

end simp
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 27 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/avoid%20writing%20%28some%3F%29%20simp-rfl%20lemmas/near/148623511):
You define a new category, and afterwards you have to state pages of trivialities. There must be some structure to this, which we can abuse, so that automation just does this for us. Has there been any thought in this direction?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 27 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/avoid%20writing%20%28some%3F%29%20simp-rfl%20lemmas/near/148635044):
You can put `@[simp]` on the thing you defined (I guess `map_left`, `map_right`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 27 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/avoid%20writing%20%28some%3F%29%20simp-rfl%20lemmas/near/148635271):
Is that good practice? I thought it was some how considered evil, because it marked too much as `simp`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 27 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/avoid%20writing%20%28some%3F%29%20simp-rfl%20lemmas/near/148635344):
it's probably not what you want, because then it will unfold even when it is not being projected

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 27 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/avoid%20writing%20%28some%3F%29%20simp-rfl%20lemmas/near/148635439):
Aha, so I want `derive simp-projections`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 27 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/avoid%20writing%20%28some%3F%29%20simp-rfl%20lemmas/near/148635440):
Is that possible?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 27 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/avoid%20writing%20%28some%3F%29%20simp-rfl%20lemmas/near/148635603):
in theory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 27 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/avoid%20writing%20%28some%3F%29%20simp-rfl%20lemmas/near/148635672):
it gets complicated with nested structures, but you could inspect the definition for a structure instance and extract the parts

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 27 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/avoid%20writing%20%28some%3F%29%20simp-rfl%20lemmas/near/148635680):
this would basically be the same thing that the equation compiler does

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 27 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/avoid%20writing%20%28some%3F%29%20simp-rfl%20lemmas/near/148635832):
I see. I hope someone with a lot of tactic-fu will pop up and write something like this (-;


{% endraw %}
