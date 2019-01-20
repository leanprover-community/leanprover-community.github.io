---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: LeanTogether2019/TeachingLeantomathematicians.html
---

## [Lean Together 2019](index.html)
### [Teaching Lean to mathematicians](TeachingLeantomathematicians.html)

#### Kevin Buzzard (Jan 11 2019 at 08:49):
I'm not at a pc right now (indeed I'm waiting for a 51 and am going to be a few minutes late) but I just mean defining a new tactic which strings together other tactics, it's trivial

#### Johan Commelin (Jan 11 2019 at 08:49):
@**David Holmes**  The problem is: tactics are just a certain kind of types. And now we have two versions of `ring`, living in different namespaces. One is a tactic, and the other is the typeclass that gives ring structure to a `R : Type`. (E.g. the ring structure on the reals). Without importing the tactic, it finds the other one, which confuses Lean, and gives you a cryptic error message.

#### David Holmes (Jan 11 2019 at 08:57):
It works, thanks Johan! Kevin, writing tactics to string together others sounds really neat, especially if its trivial :-).

#### Johan Commelin (Jan 11 2019 at 08:59):
If you want to know what `ring` does (up to "isomorphism of algorithms" :lol:), you should read Kevin's blogpost about it.

#### Rob Lewis (Jan 11 2019 at 09:13):
A small additional note: `by _` is equivalent to `begin _ end`, where `_` is a single tactic. So you can just write `by ring`, or `begin ring end`.

#### David Holmes (Jan 11 2019 at 17:34):
Hi Kevin, 
In the `complex' exercises, I made it up to and including 
``` 
theorem add_mul (a b c : ℂ) :
(a + b) * c = a * c + b * c := sorry
```
Will try the next ones later. The only thing I needed (other than what you provided) was the line 
```
import tactic.ring
```
and the tactic `by ring`. 

I wonder about more efficient ways to do some of this. I defined addition by 
```
definition add : ℂ → ℂ → ℂ 
| ⟨x1,y1⟩ ⟨x2,y2⟩ := ⟨x1 + x2, y1 + y2⟩
```
then needed things like 
```
lemma re_add (a b : ℂ) : 
re (a + b) = re a + re b:=
begin
have h : a + b = ⟨re(a+b), im(a+b) ⟩, rw eta, 
have ha : a = ⟨ re a, im a ⟩,rw eta, 
have hb : b = ⟨ re b, im b ⟩,rw eta,  
have H : a + b = ⟨re(a) + re(b), im(a+b) ⟩, rw ha, rw hb, 
unfold re, refl, rw H, refl, 
end
```
whose proof was harder than I expected. Then my proof of distributivity was 
```
theorem add_mul (a b c : ℂ) :
(a + b) * c = a * c + b * c := 
begin
apply ext, 
have Hrleft: re ((a+b) * c) = re(a + b)* re(c) - im(a + b) * im(c), 
apply re_mult,  
have Hrright : re(a * c + b * c) = re a * re c - im a * im c + re b * re c - im b * im c, 
have h1 : re(a*c) = re a * re c - im a * im c, apply re_mult, 
have h2 : re(b*c) = re b * re c - im b * im c, apply re_mult, 
rw [re_add], rw[h1], rw [h2], by ring, rw [Hrright], 
have H : re(a + b)* re(c) - im(a + b) * im(c) = re a * re c - im a * im c + re b * re c - im b * im c, 
rw [re_add], rw im_add, by ring, rw [Hrleft], rw H, -- now done with the real component
-- onto the imaginary part
have Hileft : im((a + b) * c) = re (a + b) * im c + re c * im (a + b), 
apply im_mult, 
have Hiright : im(a * c + b * c) = re a * im c + re c * im a + re b * im c + re c * im b, 
have h1 : im(a*c) = re a * im c + re c * im a, apply im_mult, 
have h2 : im(b*c) = re b * im c + re c * im b, apply im_mult, 
rw [im_add], rw[h1], rw [h2], by ring, rw [Hiright], 
have H : re(a + b)* im(c) + re(c) * im(a + b) = re a * im c + re b * im c + re c * im a + re c * im b, 
rw [re_add], rw im_add, by ring, rw [Hileft], rw H, by ring, 
end
```
(attached my code [complex.lean](/user_uploads/3121/W5bzU97AUkl2kyShuTAzZRbM/complex.lean) in case interesting/easier to read). Which was not really so bad, but doing this for every axiom would hurt a bit. 

These proof were all basically computations, so maybe tactic mode was not the best choice? But I am starting to like tactic mode quite a bit. 

I often felt I wanted to start a proof about a complex number `a` by saying 'write `a = x + iy`', but not sure if there is an analogue of that in Lean that functions as I would hope. Working around it got kind of messy, but perhaps that's life. 

[I'm putting this here (and not as a pm to Kevin) in case it is useful to other people, but I don't really know how the forum works so please let me know if I'm spamming!]

#### Kevin Buzzard (Jan 11 2019 at 18:01):
Posts like this are fine. Yes, there are better ways, but in my mind these struggles are interesting to go through once, just to make sure you understand what's going on.

https://github.com/leanprover/mathlib/blob/774e7fa39a8513c5c06e27c3e8bf4c124efd9db7/analysis/complex.lean

That was my effort at the time. I wrote a tactic called `crunch` which just did the ring theory I needed.

Defining structures and making them work properly is hard for mathematicians, because mathematicians don't instinctively think to define things like eta and ext.

#### Kevin Buzzard (Jan 12 2019 at 16:06):
```lean
theorem add_mul (a b c : ℂ) :
(a + b) * c = a * c + b * c := 
begin
  apply ext,
  { rw [re_add,re_mul,re_add,im_add,re_mul,re_mul],
    ring },
  { rw [im_add,im_mul,re_add,im_add,im_mul,im_mul],
    ring },
end
```
The `ring` tactic can solve a goal of the form `(re a + re b) * re c - (im a + im b) * im c = re a * re c - im a * im c + (re b * re c - im b * im c)` so we just apply the lemmas we know to turn it into a goal of this form. If the lemmas `re_add` etc are all tagged with the `simp` attribute then perhaps instead of the rewrite one could write `suffices : (re a + re b) * re c - blah blah blah, by simp`.

#### Kenny Lau (Jan 12 2019 at 16:27):
```lean
theorem add_mul (a b c : ℂ) : (a + b) * c = a * c + b * c :=
ext
  (show (_+_)*_-(_+_)*_=(_-_)+(_-_), by rw [add_mul, add_mul, add_sub_comm])
  (show (_+_)*_+(_+_)*_=(_+_)+(_+_), by rw [add_mul, add_mul, add_assoc, add_left_comm (b.1*_), ← add_assoc])
```

#### Bryan Gin-ge Chen (Jan 15 2019 at 01:18):
@**Kevin Buzzard** What's the new link for whatever was at http://wwwf.imperial.ac.uk/~buzzard/lean_together/source/leantogether.html ?

#### Kevin Buzzard (Jan 15 2019 at 09:10):
Sorry -- link fixed. I added some more (very sketchy) exercises and broke everything in the process.

#### David Holmes (Jan 18 2019 at 22:46):
Thanks Kevin, your proof is very nice - doing in 2 lines what took me 7. Also much easier to read! Moving on to the other cases seems more reasonable now.

#### David Holmes (Jan 18 2019 at 22:47):
Kenny, what you wrote looks very neat, but I can't get it to work. I guess i need to add `begin` and `end`, but then I get an error on the first `show`, saying `function expected at
  (λ (this : (?m_5 + ?m_6) * ?m_7 - (?m_10 + ?m_11) * ?m_12 = ?m_15 - ?m_16 + (?m_18 - ?m_19)), this) ?m_20
term has type
  (?m_5 + ?m_6) * ?m_7 - (?m_10 + ?m_11) * ?m_12 = ?m_15 - ?m_16 + (?m_18 - ?m_19)
`.
Any suggestions on what I'm doing wrong?

#### Kenny Lau (Jan 18 2019 at 22:49):
I think at that time I couldn't import mathlib so I made up my own complex numbers; the definition of multiplication may have been different (my proof relies heavily on definitional equalities)

#### Mario Carneiro (Jan 18 2019 at 22:56):
doesn't something like `by ext; ring` work?

#### Mario Carneiro (Jan 18 2019 at 23:00):
```lean
import data.complex.basic

attribute [extensionality] complex.ext

theorem add_mul' (a b c : ℂ) : (a + b) * c = a * c + b * c :=
by ext; simp; ring
```

#### David Holmes (Jan 18 2019 at 23:28):
Hi Mario, 
Thanks for the suggestion. I'm sure that works with the complex numbers in Lean, but this was part of an exercise to construct the complex numbers from the real numbers (so never used `import data.complex.basic`). I just get the usual `simplify tactic failed to simplify`. I think if some of my earlier lemmas had the simp attribute it might also work, but not yet sure how to go about that (and maybe it is not the goal of the exercise).

#### Mario Carneiro (Jan 19 2019 at 00:42):
You need simp lemmas for addition and multiplication

#### Mario Carneiro (Jan 19 2019 at 00:43):
```lean
@[simp] lemma add_re (z w : ℂ) : (z + w).re = z.re + w.re := rfl
@[simp] lemma add_im (z w : ℂ) : (z + w).im = z.im + w.im := rfl
@[simp] lemma mul_re (z w : ℂ) : (z * w).re = z.re * w.re - z.im * w.im := rfl
@[simp] lemma mul_im (z w : ℂ) : (z * w).im = z.re * w.im + z.im * w.re := rfl
```

#### Mario Carneiro (Jan 19 2019 at 00:44):
of course you can prove the theorem by `add_mul` since this is already proven in `data.complex.basic`, but if you are rewriting it on your own you want `complex.ext` and these re/im lemmas and then everything should follow by `ring` like I said

