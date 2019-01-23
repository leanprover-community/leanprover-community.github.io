---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/07463partialfunctionsagain.html
---

## Stream: [maths](index.html)
### Topic: [partial functions again](07463partialfunctionsagain.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 04 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133331307):
With the recent merges from my so-called differential topology repository to mathlib, the next target in this direction is the definition of derivatives (Fréchet derivative if you insist on this terminology). It is very easy to say that a function defined on a whole normed vector space is differentiable at some point a: https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/calculus.lean#L17 But of course we want derivatives of functions defined on a subset of a normed space, at least allowing an open set. I can clearly try to adapt the definition, but I'd be happy to read any advice.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 04 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133331524):
For instance, https://github.com/thalesant/formalabstracts/blob/riemann_hypothesis/folklore/complex.lean#L227 (in the holomorphic case, but this doesn't matter) define a function from a subset of a normed space to be differentiable at x if the subset is open and the extension by zero (which is defined everywhere) is differentiable at x. This is one option

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 04 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133333155):
I ran a quick sanity check on the definition from FAbstract (I wanted to see with my own eyes that division by zero works as intended).
```lean
import analysis.complex
import analysis.limits

open filter complex

def has_complex_derivative_at 
(f : ℂ → ℂ)
(f'z : ℂ) 
(z : ℂ) : Prop :=
let error_term (h : ℂ) : ℝ := 
    abs((f (z + h) - (f z + f'z * h))/h) in
(tendsto error_term (nhds (0 : ℂ)) (nhds (0:ℝ)))

lemma test : has_complex_derivative_at (λ z, z^2) 2 1 :=
begin
  dsimp only [has_complex_derivative_at],

  have :  (λ h : ℂ, abs (((1 + h) ^ 2 - (1 ^ 2 + 2 * h))/h)) = (λ h, abs(h^2/h)),
  by ext ; congr; ring,
  rw this,

  rw tendsto_nhds_of_metric,
  intros ε ε_pos,
  existsi [ε, ε_pos],
  intros x dx,
  by_cases h : x = 0,
  { simpa [h, ε_pos] },
  { rw [pow_two, mul_div_cancel x h],
    dsimp[dist] at dx ⊢,
    simpa using dx }
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 04 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133333260):
First I'm both amazed and ashamed that I wrote that so quickly without insulting my computer. But of course I'd be very happy to read a simpler proof. @**Rob Lewis** please feel free to explain that your Lean/Sage bridge allows to do this limit computation in one line.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 04 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133333813):
I can merge the last two lines in `simpa [dist] using dx`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 04 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133333948):
Anyway, this great success of division by zero makes me wonder whether I should define differentiability using  `∥f (a + h) - f a - L h∥/ ∥h∥`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 04 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334379):
Golfed as requested
```lean
lemma test : has_complex_derivative_at (λ z, z^2) 2 1 :=
have (λ h : ℂ, abs (((1 + h) ^ 2 - (1 ^ 2 + 2 * h)) / h)) = (λ h, abs (h ^ 2 / h)),
  by ext; congr; ring,
by simp only [has_complex_derivative_at, this, tendsto_nhds_of_metric];
  exact λ ε ε0, ⟨ε, ε0, λ x dx, if h : x = 0 then by simpa [h, ε0] 
  else by dsimp [dist] at *; simpa [pow_two, mul_div_cancel x h] using dx⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334501):
So 0/0 isn't 1? ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334514):
The applied mathematicians were lying to me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 04 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334544):
0/0 = 0 is actually really convenient for stating the definition of the derivative

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334553):
PS are we witnessing the first time Lean has ever differentiated a function here?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 04 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334564):
well, the chain rule was a derivative

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334572):
0/0 -- you got lucky :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334645):
Chris -- with the binomial theorem you can differentiate x^n and with Patrick's knowledge of filters he can prove differentiation is linear, and then we can differentiate polynomials!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334654):
we can differentiate polynomials just fine

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334657):
(hey, you teach Galois theory)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 04 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334701):
not formal derivatives, real derivatives

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334735):
But of course we need to differentiate `cos` too :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334784):
That will follow from C-linearity if someone can differentiate exp. Mario did you say there was a dirty trick for that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334838):
I guess step one is to get exp in mathlib...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 04 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334847):
yes, `1 + x <= exp x <= 1/(1-x)` proves `exp' 0 = 1` and then it's easy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 04 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335121):
Thanks Chris. I think it's exactly the same proof though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 04 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335145):
That is correct

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335163):
It's easy if you have the product rule, but Patrick doesn't believe in the product rule

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 04 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335170):
What?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335226):
The product rule is a low-dimensional coincidence

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335251):
```lean
lemma test : has_complex_derivative_at (λ z, z^2) 2 1 :=
tendsto_nhds_of_metric.2 $ λ ε hε, ⟨ε, hε, λ z hz,
if h : z = 0 then by simpa [h] else
by simp [pow_two, mul_add, add_mul, two_mul, dist];
rw [← complex.abs_mul z, ← complex.abs_div, mul_div_cancel _ h];
simpa [dist] using hz⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335477):
```lean
lemma test : has_complex_derivative_at (λ z, z^2) 2 1 :=
have H : ∀ z : ℂ, -1 + (-(2 * z) + (z + 1) ^ 2) = z * z,
  from λ _, by ring,
tendsto_nhds_of_metric.2 $ λ ε hε, ⟨ε, hε, λ z hz,
if h : z = 0 then by simpa [h] else
by simp [H, mul_div_cancel _ h, -complex.abs_div];
simpa [dist] using hz⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335582):
```lean
lemma test : has_complex_derivative_at (λ z, z^2) 2 1 :=
tendsto_nhds_of_metric.2 $ λ ε hε, ⟨ε, hε, λ z hz,
if h : z = 0 then by simpa [h] else by simp [pow_two,
mul_add, add_mul, two_mul, mul_div_cancel _ h,
-complex.abs_div]; simpa [dist] using hz⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335588):
finally 4 lines

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 04 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335659):
I think you broke the style guidelines with the last one.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335813):
```lean
lemma test : has_complex_derivative_at (λ z, z^2) 2 1 :=
tendsto_nhds_of_metric.2 $ λ ε hε, ⟨ε, hε, λ z hz,
if h : z = 0 then by simpa [h] else
by simp [pow_two, add_mul_self_eq, mul_div_cancel _ h, -complex.abs_div];
simpa [dist] using hz⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335883):
```lean
lemma test : has_complex_derivative_at (λ z, z^2) 2 1 :=
tendsto_nhds_of_metric.2 $ λ ε hε, ⟨ε, hε, λ z hz,
if h : z = 0 then by simpa [h] else
by simp [pow_two, add_mul_self_eq, -complex.abs_div];
simpa [mul_div_cancel _ h, dist] using hz⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335938):
Kenny this reminds me of Chris Ford's question "differentiate x^10*sin(x) five times"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335986):
for which my answer was "10 x^9*sin(x) + x^10*cos(x) every time"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133336000):
Why don't you prove the product rule one time instead?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 04 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133336022):
or prove that the derivative of `x^2` is `2x` and then prove `2*1=2`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133336364):
```lean
lemma test : has_complex_derivative_at (λ z, z^2) 2 1 :=
tendsto_nhds_of_metric.2 $ λ ε hε, ⟨ε, hε, λ z hz,
if h : z = 0 then by simpa [h] else trans_rel_right _
(by simp [dist, pow_two, add_mul_self_eq, mul_div_cancel _ h, -complex.abs_div]) hz⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133336621):
```lean
lemma test : has_complex_derivative_at (λ z, z^2) 2 1 :=
tendsto_nhds_of_metric.2 $ λ ε hε, ⟨ε, hε, λ z hz,
if h : z = 0 then by simpa [h] else by dsimp; rw [pow_two];
by simpa [dist, add_mul_self_eq, mul_div_cancel _ h, -complex.abs_div] using hz⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133337102):
```lean
lemma test : has_complex_derivative_at (λ z, z^2) 2 1 :=
tendsto_nhds_of_metric.2 $ λ ε hε, ⟨ε, hε, λ z hz,
by simp [pow_two, add_mul_self_eq, dist, -complex.abs_div] at *;
by_cases h : z = 0; [simpa [h], rwa mul_div_cancel _ h]⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133338281):
one of those proofs actually conformed to the guidelines!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133338317):
I don't understand the last one. What is this `[simpa [h], rwa mul_div_cancel _ h]`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133338330):
I mean, why is there a list of tactics?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133338383):
because there are two goals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133338398):
oh! The n'th term in the list acts on the n'th goal?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133338498):
```lean
example (p q : Prop) (hp : p) (hq : q) : p ∧ q :=
begin
  split;[exact hp,exact hq]
end

```

woo!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Sep 05 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133359026):
If you want to define differentiability in a rather broad setting, you certainly want it to contain differentiability on the left and on the right for 1-dimensional functions, and differentiability on manifolds with boundaries. The best setting for this is probably differentiability in the sense of Whitney, i.e., `f` is differentiable at `x` on `S` if there is a linear operator such that `f(y)-f(x) -L (y-x)/ ||y-x||` tends to `0` when `y`tends to `x`while remaining in `S`. This is certainly easy to define if you have a filter like `nhbds_within` (defined using `nhbds x` and `principal S` and the good filter operation (I never know in which direction they go)). This filter would also be useful to define continuity within `S`, as far as I can tell this is not in Lean?. 

With the big warning that the differential is not unique in general, if the tangent directions of `S` at `x` do not span the whole subspace. For uniquenss statement, you would probably want that `S` is a neighborhood of `x`, say.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 05 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133359631):
the good filter operation is infimum: `nhds_within a s := nhds a ⊓ principal s`


{% endraw %}
