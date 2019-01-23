---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/65569Productmetaprogram.html
---

## Stream: [new members](index.html)
### Topic: [Product meta program](65569Productmetaprogram.html)

---

#### [Ken Roe (Jul 29 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130535258):
Here is a simple meta program to simplify a product expression.  It does not seem to match anything.  Can someone explain what is happening?

```lean
meta def simplifyProd : expr → expr
| (expr.app
    (expr.app
      (expr.app `(prod.fst) tt1a)
      tt1b)
     (expr.app
        (expr.app
          (expr.app 
            (expr.app `(prod.mk) tt1) tt2) a) b)) := a
| (expr.app a b) := expr.app (simplifyProd a) (simplifyProd b)
| (expr.lam v b t e) := expr.lam v b (simplifyProd t) (simplifyProd e)
| (expr.pi v b t e) := expr.pi v b (simplifyProd t) (simplifyProd e)
| x := x

theorem testit (f:ℕ) (s:ℕ) :
    (f,s).fst=f :=
begin
   do {
       t ← target,
       trace "Start",
       trace t.to_raw_fmt,
       tq ← some (simplifyProd t),
       trace tq.to_raw_fmt,
       change tq
   },
   refl
end
```

#### [Reid Barton (Jul 29 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130536744):
Well, I don't know, but replacing the first case with ``| `(prod.fst (prod.mk %%a %%b)) := a`` works.
Maybe something involving universe variables?

#### [Kevin Buzzard (Jul 29 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130536883):
@**Ken Roe** Just to let you know that probably nobody is reading the Lean bug reports. The developers are working on Lean 4 and anything that isn't obviously a serious issue in 3.4.1 which needs addressing (e.g. a proof of false) is very likely to be ignored.

#### [Ken Roe (Jul 29 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130540273):
Actually, `(prod.fst (prod.mk %%a %%b)) probably works but I'm trying to avoid quoting.  I doing pattern matching that is breaking apart \lambda expressions and I found that %%x inside a lambda lifts the variables (which I would like to avoid).  I've also been running into type checking issues.  If people are interested, I can post more cases illustrating more issues.

Right now, I'm pretty frustrated.  I'm trying to build a separation logic using Lean.  Right now, all paths to building the necessary tactics are blocked due to missing documentation or bugs.

#### [Patrick Massot (Jul 29 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130540874):
You should talk to Simon, he knows both tactics and separation logic in Lean

#### [Simon Hudon (Jul 29 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130540986):
If you want, I have started on a separation logic package: https://github.com/unitb/separation-logic. It might be easier to collaborate on it.

#### [Simon Hudon (Jul 29 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130541039):
So far, my tactics can handle a twenty-line proof of the list reversal program: https://github.com/unitb/separation-logic/blob/master/src/separation/examples.lean#L118-L137

#### [Ken Roe (Jul 29 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130541248):
Can someone send me a private message with Simon's contact information?  By the way, to illustrate another issue, I just added another case which causes simplifyProd to not compile.
```lean
meta def simplifyProd : expr → expr
| (expr.app
    (expr.app
      (expr.app `(prod.fst) tt1a)
      tt1b)
     (expr.app
        (expr.app
          (expr.app 
            (expr.app `(prod.mk) tt1) tt2) a) b)) := a
| `((λ x, (%%f) x) (%%z)) := `(%%f (%%z+1))
| (expr.app a b) := expr.app (simplifyProd a) (simplifyProd b)
| (expr.lam v b t e) := expr.lam v b (simplifyProd t) (simplifyProd e)
| (expr.pi v b t e) := expr.pi v b (simplifyProd t) (simplifyProd e)
| x := x

theorem testit (f:ℕ) (s:ℕ) :
    (f,s).fst=f :=
begin
   do {
       t ← target,
       trace "Start",
       trace t.to_raw_fmt,
       tq ← some (simplifyProd t),
       trace tq.to_raw_fmt,
       change tq
   },
   refl
end
```
  This case with the lambda gives the following error on the %%f:
```lean
function expected at
  _x_1
term has type
  ?m_1
```

#### [Patrick Massot (Jul 29 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130541265):
you can click on his name, right above your question

#### [Patrick Massot (Jul 29 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130541304):
I mean: right above in this thread

#### [Ken Roe (Jul 29 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130541312):
Never mind on the contact info--I just saw a message from Simon. 

I'm more than happy to collaborate on separation logic.  I did work on separation logic using Coq for my PhD.  You can check out my home page at www.cs.jhu.edu/~roe.  I'm working on porting my system to Lean.

#### [Simon Hudon (Jul 29 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130541412):
Cool thanks, that should be helpful. You can have a look at how far I got right here: https://leanprover.zulipchat.com/#narrow/stream/113489-new-members/subject/Product.20meta.20program/near/130540986

#### [Ken Roe (Jul 30 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130597942):
Actually, an ideal solution would be not to use `(prod.mk).   Is there an alternative that I can plug in without changing the surrounding text?  I would like to find a way of expression my product meta program without using any back quote annotations.  The motivation is that I actually have some more complex meta programs where I'm finding the back quote notation has semantics that is causing a number of problems.

#### [Simon Hudon (Jul 30 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130598427):
Can you show us that other program?

#### [Ken Roe (Jul 30 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130606073):
I'll put it up in a day or two.  The code isn't stand alone.  It is dependent on the infrastructure in my separation logic framework.  I need to put the work into a github repository and then post the critical meta functions.

#### [Ken Roe (Aug 06 2018 at 05:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Product%20meta%20program/near/130956238):
I've posted the source code that I have of my separation framework so far here: https://github.com/kendroe/pedantic2.  Some of my future questions will point to this repository.  I'm porting the Coq implementation.  Information on this implementation (and repository link) can be found here: http://www.cs.jhu.edu/~roe.

