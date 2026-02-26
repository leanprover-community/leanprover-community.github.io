# Maths in Lean: partial derivatives

Where are partial derivatives in Mathlib? There is only Fréchet derivative `fderiv` which might be surprising but it is sufficient to express all possible derivatives.

### Quick Answer

Given a function $$f : \mathbb{R}^n \to \mathbb{R}^m$$, how do you write $$\frac{\partial f}{\partial x_i}$$ in Lean?

Lean represents $$\mathbb{R}^n$$ as `EuclideanSpace ℝ (Fin n)`. You can express partial derivatives using the `fderiv` function and the basis vector `single i 1`:

```lean
import Mathlib

variable {n m : ℕ} (f : EuclideanSpace ℝ (Fin n) → EuclideanSpace ℝ (Fin m))
  (x : EuclideanSpace ℝ (Fin n)) (i : Fin n)

open EuclideanSpace
-- ∂f/∂xᵢ at x
#check fderiv ℝ f x (single i 1)
```

The `fderiv ℝ f x` expression gives the full Jacobian of `f`, which is a linear map $$L(\mathbb{R}^n, \mathbb{R}^m)$$. Evaluating this map on the basis vector $$e_i$$ (represented by `single i (1 : ℝ)`) gives the partial derivative.

### Longer Answer

There are two primary approaches to handling partial derivatives in Lean, depending on whether the input dimension is variable or fixed.

#### 1. Functions Over an n-Dimensional Space

If you work with a general function $$f : \mathbb{R}^n \to \mathbb{R}^m$$, use the approach described above with `fderiv` and `single`.

#### 2. Functions with Fixed Arguments

For functions with a known number of arguments, like $$f(x, y)$$, it's often better to define `f` as `ℝ → ℝ → EuclideanSpace ℝ (Fin m)` rather than `EuclideanSpace ℝ (Fin 2) → EuclideanSpace ℝ (Fin m)`. Here is how to compute partial derivatives with respect to each argument:

```lean
import Mathlib

variable {m : ℕ} (f : ℝ → ℝ → EuclideanSpace ℝ (Fin m)) (x y : ℝ)

open EuclideanSpace
-- ∂f/∂x at (x,y)
#check fderiv ℝ (fun x' => f x' y) x 1
-- ∂f/∂y at (x,y)
#check fderiv ℝ (fun y' => f x y') y 1
```

To actually prove anything about these derivatives you will need to state that `f` is differentiable in `x` and `y`. The ways to state differentiability of `f` in `(x,y)` are:
  - `(hf : Differentiable ℝ (fun (x,y) => f x y))`
  - `(hf : Differentiable ℝ (fun xy : ℝ×ℝ => f xy.1 xy.2)`
  - `(hf : Differentiable ℝ ↿f)`
They are syntactic variants of the same thing. Pick one you prefer writing. The first one does not work with `variable` though.

Requiring differentiability in `(x,y)` gives you differentiability in `x` and differentiability in `y`:
```lean
import Mathlib

variable {m : ℕ} (f : ℝ → ℝ → EuclideanSpace ℝ (Fin m)) (x y : ℝ)

example (hf : Differentiable ℝ ↿f) :
    Differentiable ℝ (fun x => f x y) := by fun_prop

example (hf : Differentiable ℝ (fun (x,y) => f x y)) :
    Differentiable ℝ (fun y => f x y) := by fun_prop
```

#### 3. Mixed Approach

When working with functions that mix fixed and variable dimensions (e.g., $$f(x, y)$$ where $$x \in \mathbb{R}^n$$ and $$y \in \mathbb{R}^m$$), you can apply `fderiv` to each argument separately:

```lean
import Mathlib

variable {n m k : ℕ} (f : EuclideanSpace ℝ (Fin n) → EuclideanSpace ℝ (Fin m) → EuclideanSpace ℝ (Fin k))
  (x y) (i : Fin n) (j : Fin m)

open EuclideanSpace
-- ∂f/∂xᵢ at (x,y)
#check fderiv ℝ (fun x' => f x' y) x (single i 1)
-- ∂f/∂yⱼ at (x,y)
#check fderiv ℝ (fun y' => f x y') y (single j 1)
```

### Special Cases

#### 1. When the Input is ℝ (`deriv`)

If the function's input is `ℝ`, you can use `deriv` as a simpler alternative to `fderiv`:

```lean
import Mathlib

variable {n : ℕ}
  (f : ℝ → EuclideanSpace ℝ (Fin n))
  (g : ℝ → ℝ → EuclideanSpace ℝ (Fin n))
  (x y : ℝ)

open EuclideanSpace
-- d f / d x at x
#check deriv f x
-- Equivalent to fderiv
example : deriv f x = fderiv ℝ f x 1 := by rfl
-- ∂ g / ∂ x at (x,y)
#check deriv (fun x' => g x' y) x
-- ∂ g / ∂ y at (x,y)
#check deriv (fun y' => g x y') y
```

#### 2. When the Output is ℝ (`gradient`)

If the function's output is `ℝ`, you may want the gradient (a vector of all partial derivatives). For this, use the `gradient` function:

```lean
import Mathlib

variable {n m : ℕ}
  (f : EuclideanSpace ℝ (Fin n) → ℝ)
  (g : EuclideanSpace ℝ (Fin n) → EuclideanSpace ℝ (Fin m) → ℝ)
  (x y)

open EuclideanSpace
-- ∇ₓ f at x
#check gradient f x
-- ∇ₓ g at (x,y)
#check gradient (fun x' => g x' y) x
-- ∇_y g at (x,y)
#check gradient (fun y' => g x y') y
```


### Writing all this is such a chore ...

I hear you! You can define custom notation:
```lean
import Mathlib

macro "ℝ[" n:term "]" : term => `(EuclideanSpace ℝ (Fin $n))
macro "∂[" i:term "]" : term => `(fun f x => fderiv ℝ f x (EuclideanSpace.single $i (1:ℝ)))

variable {m n k : ℕ} (f : ℝ[n] → ℝ[m] → ℝ[k]) (x : ℝ[n]) (y : ℝ[m])
   (i : Fin n) (j : Fin m)

-- `∂ f / ∂ xᵢ` at `(x,y)`
#check ∂[i] (f · y) x

-- `∂ f / ∂ yⱼ` at `(x,y)`
#check ∂[j] (f x ·) y
```
