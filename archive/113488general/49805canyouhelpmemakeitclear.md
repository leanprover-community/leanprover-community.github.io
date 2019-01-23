---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/49805canyouhelpmemakeitclear.html
---

## Stream: [general](index.html)
### Topic: [can you help me make it clear](49805canyouhelpmemakeitclear.html)

---

#### [Truong Nguyen (Sep 10 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133665638):
I read the book about lean prover. There is some code like this:

```lean

def nat.dvd (m n: ℕ ): Prop := ∃ k, n = m * k 
instance : has_dvd nat := ⟨nat.dvd ⟩ 
theorem nat.dvd_refl (n: ℕ ) : n ∣ n := ⟨1, by simp ⟩ 

```
I don't know why this theorem can be proved by <1, simp>. What does number 1 mean?
Thank you for making it clear,

#### [Johan Commelin (Sep 10 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133665724):
You see the `k` on the first line?

#### [Johan Commelin (Sep 10 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133665742):
To prove `n | n`, you have to provide a `k`. And this proof provides `1`.

#### [Johan Commelin (Sep 10 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133665778):
Afterwards, you have to prove `n = m * k`. And in your theorem `m` is `n`, and you just provided `k` is `1`.

#### [Johan Commelin (Sep 10 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133665788):
The proof is then `by simp`.

#### [Truong Nguyen (Sep 10 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133665890):
Ok, thanks. I see it is trivial now.

#### [Truong Nguyen (Sep 10 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666052):
By the way, is there any other way. I mean how can we write the code clearer.

#### [Johan Commelin (Sep 10 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666084):
Yes. This is called tactic mode.

#### [Johan Commelin (Sep 10 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666101):
```lean
def nat.dvd (m n: ℕ ): Prop := ∃ k, n = m * k
instance : has_dvd nat := ⟨nat.dvd ⟩
theorem nat.dvd_refl (n: ℕ ) : n ∣ n :=
begin
  existsi 1,
  simp
end
```

#### [Truong Nguyen (Sep 10 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666288):
Oh, ok. How can we unfold the definition of "|", to make it appear like: 
```lean
\exists k, n = m * k

```

#### [Truong Nguyen (Sep 10 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666491):
I mean, to make it look like this:
``` lean
example (n: ℕ ): ∃ k, n = n * k := _
```

#### [Reid Barton (Sep 10 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666552):
Do you mean you want to change what the goal looks like, inside the tactic block?

#### [Truong Nguyen (Sep 10 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666565):
Oh, yes

#### [Reid Barton (Sep 10 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666643):
Two ways. One is that you can use `change` to change the goal to something definitionally equivalent, like
```lean
  change ∃ k, n = n * k,
```
Of course, that depends on knowing what the unfolded form should be

#### [Truong Nguyen (Sep 10 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666803):
WHat is the second way

#### [Reid Barton (Sep 10 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666817):
The other way is to use `unfold` or `dsimp` or related tactics to unfold the `∣` operation, but because it is notation in this case, you need to know the actual name of the operator, which is `has_dvd.dvd`

#### [Reid Barton (Sep 10 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666938):
Then `has_dvd` is a class, so you also need to unfold the actual instance for `nat`. If you start with
```lean
  unfold has_dvd.dvd,
```
then you'll see what the actual operation is in the goal window -- it's `nat.dvd`

#### [Truong Nguyen (Sep 10 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666955):
I tried this:
``` lean
theorem nat.dvd_refl (n: ℕ ) : n ∣ n := 
begin
unfold nat.dvd,
end
```
But, I got error

#### [Reid Barton (Sep 10 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133666979):
So then you can unfold both at once with
```lean
  unfold has_dvd.dvd nat.dvd,
```

#### [Reid Barton (Sep 10 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133667037):
Yep, because you have to unfold `has_dvd.dvd` first.
If you write `set_option pp.notation false` before your theorem, you can see what the notation really represents.

#### [Truong Nguyen (Sep 10 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133667112):
Oh, I made it works now.
It run fine
``` lean

theorem nat.dvd_refl (n: ℕ ) : n ∣ n := 
begin
unfold has_dvd.dvd nat.dvd,
end
```

#### [Mario Carneiro (Sep 10 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20you%20help%20me%20make%20it%20clear/near/133669697):
you can write `dsimp [(∣)]` too

