---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/58886partialorderformatrix.html
---

## Stream: [new members](index.html)
### Topic: [partial order for matrix](58886partialorderformatrix.html)

---


{% raw %}
#### [ Tobias Grosser (Sep 18 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134185883):
Dear all, as you know I just get up-to-speed on lean (and theorem proving) and don't do it fulltime for now. However, I picked as first toy-project to get started the extension of matrix as an instance of partial_order. (See https://github.com/tobig/lean-polyhedra/blob/master/src/polyhedra.lean)

#### [ Andrew Ashworth (Sep 18 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134185923):
Hi Tobias, you may want to post this in the #maths channel so people who are interested in this sort of stuff see it!

#### [ Andrew Ashworth (Sep 18 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186016):
or you may post in #general if this is a concrete matrix implementation meant for use in computation

#### [ Tobias Grosser (Sep 18 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186420):
Honestly, I don't even know how to post to the #maths channel. I see a "general" and a "new members" stream, but no "#maths" channel. I know streams and topics from https://zulipchat.com/help/about-streams-and-topics, but have no ideas of channels. I can obviously move this topic to the general stream if this helps. Would also post it to a math channel, if you can explain what a math channel is? Are you refering to "stream:general topic:#maths"?

#### [ Tobias Grosser (Sep 18 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186434):
I posted it in new members, as my questions are for now still very simple.

#### [ Reid Barton (Sep 18 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186514):
"Channel" means stream in this context I think.

#### [ Andrew Ashworth (Sep 18 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186540):
whew, yes, I forgot Zulip isn't IRC

#### [ Reid Barton (Sep 18 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186549):
#**maths**

#### [ Tobias Grosser (Sep 18 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186552):
OK, got it. Had to subscribe to #maths explicitly

#### [ Tobias Grosser (Sep 18 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186634):
My questions still remain simple. I mostly would like to know how to destruct an equality: https://github.com/tobig/lean-polyhedra/blob/master/src/polyhedra.lean#L51

#### [ Tobias Grosser (Sep 18 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186752):
I spend some time looking and will probably figure it out eventually, but maybe somebody has a pointer.

#### [ Reid Barton (Sep 18 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186772):
Don't you need to construct an equality?

#### [ Reid Barton (Sep 18 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186781):
I guess you mean: "destruct" the goal

#### [ Tobias Grosser (Sep 18 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186787):
Exactly.

#### [ Tobias Grosser (Sep 18 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186843):
I had the same problem with the <=, but there I could just "assume i" and lean would auto-destruct it.

#### [ Reid Barton (Sep 18 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186872):
I'm assuming your matrices are functions (of two variables), so the low-level way is to apply `funext` (twice)

#### [ Andrew Ashworth (Sep 18 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186888):
you will probably want `ext_iff ` in `ring_theory.matrix`

#### [ Andrew Ashworth (Sep 18 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134186956):
this will allow you to turn `M = N` into ` (∀ i j, M i j = N i j)`

#### [ Tobias Grosser (Sep 18 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134187198):
Right. ext_iff looks good. Now I need to figure out how to apply it.

#### [ Tobias Grosser (Sep 18 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134187201):
Reid's proposal also worked.

#### [ Tobias Grosser (Sep 18 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134187220):
But from there I would not know how to proceed.

#### [ Johan Commelin (Sep 18 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134187234):
Either `ext` or `rw ext_iff` probably works

#### [ Andrew Ashworth (Sep 18 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134187236):
indeed, `ext_iff` is defined using multiple `funext` applications

#### [ Tobias Grosser (Sep 18 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134187309):
Perfect. All works.

#### [ Tobias Grosser (Sep 18 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134187314):
So easy. I tried rw, but had missed a comma before. Thought I needed more magic.

#### [ Tobias Grosser (Sep 18 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134187329):
Thanks guys. This got me over a slow phase. Will finish my proofs and get back. Very nice community here.

#### [ Tobias Grosser (Sep 18 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134187979):
Just to report back, my proof went through and I know have the partial_order I wanted to define on matrix.

#### [ Kevin Buzzard (Sep 18 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134187985):
```lean
protected def matrix.le_antisymm [partial_order α] (a b: matrix n m α) :
a ≤ b → b ≤ a → a = b :=
begin
  assume h1: a ≤ b,
  assume h2: b ≤ a,
  apply funext, intro i, apply funext, intro j,
-- or   funext i,funext j,
-- or  ext i j,
  exact le_antisymm (h1 i j) (h2 i j),
end
```

#### [ Tobias Grosser (Sep 18 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134187996):
Ah, even better.

#### [ Tobias Grosser (Sep 18 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188004):
Thanks @**Kevin Buzzard**

#### [ Tobias Grosser (Sep 18 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188071):
@**Kevin Buzzard**, I used this for a proof on polyhedra. Would it make sense to add such defintions to your recent mathlib changes?

#### [ Mario Carneiro (Sep 18 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188081):
golfed:
```
protected lemma matrix.le_antisymm [partial_order α] (a b: matrix n m α)
  (h1 : a ≤ b) (h2 : b ≤ a) : a = b :=
by ext i j; exact le_antisymm (h1 i j) (h2 i j)
```

#### [ Mario Carneiro (Sep 18 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188096):
(also I don't have your definitions, so I had to guess if that's right)

#### [ Kevin Buzzard (Sep 18 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188203):
It would not surprise me if the Pi_instance tactic did this automatically, but it might not do.

#### [ Kenny Lau (Sep 18 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188206):
golfeded:
```lean
protected lemma matrix.le_antisymm [partial_order α] (a b: matrix n m α)
  (h1 : a ≤ b) (h2 : b ≤ a) : a = b :=
by ext i j; from le_antisymm (h1 i j) (h2 i j)
```

#### [ Tobias Grosser (Sep 18 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188431):
Nice, this lean golf.

#### [ Tobias Grosser (Sep 18 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188437):
The two solutions from Mario and Kenny don't work in my editor.

#### [ Tobias Grosser (Sep 18 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188444):
Need to replace "by" with "begin .. end"

#### [ Tobias Grosser (Sep 18 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188491):
Not yet sure why, but this proofs starts to look really nice. And you are all fast in golfing. ;-)

#### [ Tobias Grosser (Sep 18 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188689):
Got it, need a semicolon for 'by'.

#### [ Kevin Buzzard (Sep 18 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188751):
yes, `by` takes only one tactic, so you can either do `{tactic 1, tactic 2}` or `tactic 1;tactic 2`

#### [ Kevin Buzzard (Sep 18 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188801):
Did you notice that they both moved the hypotheses to the left of the colon? That's standard Lean style, so it seems; put as many hypotheses as possible on the left of the colon unless you can't do this for some reason (e.g. you're using the equation compiler).

#### [ Kevin Buzzard (Sep 18 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188858):
It makes your tactic proof two lines shorter at no extra cost

#### [ Tobias Grosser (Sep 18 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188885):
I noticed and changed my code, but lacked the explanation. Thanks for providing it.

#### [ Mario Carneiro (Sep 18 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188910):
basically, if the very first thing in your proof is a lambda/`intro`, you should probably shift your colon

#### [ Kevin Buzzard (Sep 18 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188921):
my partner does that for a living

#### [ Kevin Buzzard (Sep 18 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188934):
she's a colorectal surgeon

#### [ Mario Carneiro (Sep 18 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134188980):
I need an emoji for this

#### [ Tobias Grosser (Sep 18 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189102):
Meanwhile, things look a lot better: https://github.com/tobig/lean-polyhedra/blob/master/src/polyhedra.lean

#### [ Tobias Grosser (Sep 18 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189125):
In case you have more suggestions:

```
protected def matrix.le_trans [partial_order α] (a b c: matrix n m α)
  (h1 : a ≤ b) (h2 : b ≤ c) : a ≤ c :=
begin
  assume i: n,
  assume j: m,
  have h1l: a i j ≤ b i j, from h1 i j,
  have h2l: b i j ≤ c i j, from h2 i j,
  transitivity,
  apply h1l,
  apply h2l,
end
```

and

```
protected def matrix.le_refl [partial_order α] (A: matrix n m α) :
A ≤ A :=
begin
  assume i: n,
  assume j: m,
  refl
end
```

are also open for golfing. ;-)

#### [ Tobias Grosser (Sep 18 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189147):
I will golf myself a little browsing mathlib code.

#### [ Kenny Lau (Sep 18 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189154):
```lean
protected def matrix.le_trans [partial_order α] (a b c: matrix n m α)
  (h1 : a ≤ b) (h2 : b ≤ c) : a ≤ c :=
by intros i j; from le_trans (h1 i j) (h2 i j)

protected def matrix.le_refl [partial_order α] (A: matrix n m α) :
  A ≤ A :=
by intros i j; refl
```

#### [ Kenny Lau (Sep 18 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189245):
```lean
protected def matrix.le_trans [partial_order α] (a b c: matrix n m α)
  (h1 : a ≤ b) (h2 : b ≤ c) : a ≤ c :=
by intros i j; transitivity; solve_by_elim
```

#### [ Kenny Lau (Sep 18 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189264):
hmm the last one may not work

#### [ Tobias Grosser (Sep 18 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189409):
They all work.

#### [ Kevin Buzzard (Sep 18 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189412):
```lean
protected def matrix.le_refl [partial_order α] (A: matrix n m α) :
A ≤ A := λ i j, le_refl _
```

#### [ Tobias Grosser (Sep 18 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189417):
I learned a lot. So much fun.

#### [ Kevin Buzzard (Sep 18 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189468):
```lean
protected def matrix.le_refl [partial_order α] (A: matrix n m α) :
A ≤ A := λ_ _, le_refl _
```

#### [ Kevin Buzzard (Sep 18 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189479):
bad style (should be a space after the lambda)

#### [ Kevin Buzzard (Sep 18 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189493):
but I'm just trying to beat Kenny

#### [ Tobias Grosser (Sep 18 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189508):
Now I am unsure which ones to commit.

#### [ Kevin Buzzard (Sep 18 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189560):
`set_option profiler true` and see which one is quickest :-)

#### [ Tobias Grosser (Sep 18 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189566):
I feel the last ones are a little too tight. What's the stylistic preferred solution?

#### [ Kevin Buzzard (Sep 18 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189584):
```lean
protected def matrix.le_refl [partial_order α] (A: matrix n m α) :
A ≤ A := λ _ _, le_refl _
```
would probably be fine for mathlib I suspect

#### [ Chris Hughes (Sep 18 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189797):
Shouldn't all of this be `by pi_instance`?

#### [ Kevin Buzzard (Sep 18 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189804):
right

#### [ Kevin Buzzard (Sep 18 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189858):
but I don't know if they did partial orders and I didn't look.

#### [ Kenny Lau (Sep 18 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189876):
I believe they did

#### [ Kenny Lau (Sep 18 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189882):
though I too did not look

#### [ Kevin Buzzard (Sep 18 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134189931):
@**Tobias Grosser** The original matrix add_comm_group code was written by Ellen Arlt and I was rewriting it in a live Lean coding session with an audience of undergrads, and Chris pointed out that pi_instances just did everything immediately.

#### [ Tobias Grosser (Sep 18 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134190187):
Interesting. I don't know how to use pi_instance(s)

#### [ Tobias Grosser (Sep 18 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134190270):
If I just write pi_instance, I get "too many constructors" for the first two lemmas, and "failed" for the last.

#### [ Tobias Grosser (Sep 19 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134212318):
I made some good progress, but got stuck in type class resolution. I try to do dependent pattern matching in the following code:

```
#check matrix
universe v
def Gaussian_elimination {α : Type v} [ordered_ring α] :
   Π {x y : Type u}  [fintype x] [fintype y], matrix x y α →  α
| _ _ _ := 1
```

Unfortunately, I get the following error at location 'matrix':

```
polyhedra.lean:104:46: error

failed to synthesize type class instance for
α : Type v,
_inst_4 : ordered_ring α,
x y : Type u,
_inst_5 : fintype x,
_inst_6 : fintype y
⊢ fintype x
polyhedra.lean:104:46: error
```

#### [ Tobias Grosser (Sep 19 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134212376):
I modeled this according to https://leanprover.github.io/theorem_proving_in_lean/induction_and_recursion.html#dependent-pattern-matching, and therae the example on vector works without problems. In case anybody has some flyby ideas.

#### [ Mario Carneiro (Sep 19 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134213060):
`by exactI 1`

#### [ Tobias Grosser (Sep 19 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134213712):
Is this in reply to the type class issue?

#### [ Tobias Grosser (Sep 19 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134213766):
```lean
def Gaussian_elimination {α : Type v} [ordered_ring α] :
   Π {x y : Type u}  [fintype x] [fintype y], matrix x y α →  α
| _ _ _ := by exactI 1
```
does not work for me.

#### [ Tobias Grosser (Sep 19 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134213773):
I still get an error at 'matrix x y \a'

#### [ Tobias Grosser (Sep 19 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134213854):
I also don't see why I would add a tactics proof at a definition of a value. This seems to not make a lot of sense to me.

#### [ Kenny Lau (Sep 19 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134213905):
```lean
def Gaussian_elimination {α : Type v} [ordered_ring α] :
   Π {x y : Type u}  [fintype x] [fintype y], matrix x y α →  α
| _ _ _ _ _ := by exactI 1
```

#### [ Tobias Grosser (Sep 19 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134213986):
Thanks, now I know how to use syntax highlighting.

#### [ Tobias Grosser (Sep 19 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134213988):
But your code does not work either.

#### [ Tobias Grosser (Sep 19 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134213990):
I still get:
```
polyhedra.lean:108:46: error

failed to synthesize type class instance for
α : Type v,
_inst_4 : ordered_ring α,
x y : Type u,
_inst_5 : fintype x,
_inst_6 : fintype y
⊢ fintype x
```

#### [ Kenny Lau (Sep 19 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214030):
is that the whole error?

#### [ Kenny Lau (Sep 19 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214037):
oh, the error is in the type

#### [ Tobias Grosser (Sep 19 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214038):
I get it 4 times in a row at the same location.

#### [ Tobias Grosser (Sep 19 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214041):
Yes, something is broken. I just don't know how to interpret the error message.

#### [ Tobias Grosser (Sep 19 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214046):
It seems to derive fintype x, but I feel I provided all information.

#### [ Kenny Lau (Sep 19 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214050):
```lean
def Gaussian_elimination {α : Type v} [ordered_ring α] :
   Π {x y : Type u}  [hx : fintype x] [hy : fintype y], @matrix x y α hx hy _ →  α
| _ _ _ _ _ := by exactI 1
```

#### [ Kenny Lau (Sep 19 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214051):
something like that

#### [ Kenny Lau (Sep 19 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214055):
the order of the arguments may be wrong

#### [ Kenny Lau (Sep 19 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214096):
I don't see why you would need pattern matching

#### [ Kenny Lau (Sep 19 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214107):
```lean
def Gaussian_elimination {α : Type v} [ordered_ring α] {x y : Type u} [fintype x] [fintype y] :
  matrix x y α →  α
| _ := 1
```

#### [ Tobias Grosser (Sep 19 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214156):
The one without pattern matching works (I managed to write sth similar myself).

#### [ Tobias Grosser (Sep 19 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214161):
The @matrix one breaks with:

#### [ Tobias Grosser (Sep 19 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214168):
```
polyhedra.lean:192:57: error

type mismatch at application
  matrix x y
term
  α
has type
  Type v : Type (v+1)
but is expected to have type
  fintype x : Type u
```

#### [ Kenny Lau (Sep 19 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214176):
```lean
def Gaussian_elimination {α : Type v} [ordered_ring α] :
   Π {x y : Type u}  [hx : fintype x] [hy : fintype y], @matrix x y hx hy α _ → α
| _ _ _ _ _ := by exactI 1
```

#### [ Tobias Grosser (Sep 19 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214177):
I want to implement something similar to
```


Fixpoint Gaussian_elimination {m n} : 'M_(m, n) → 'M_m × 'M_n × nat :=
  match m, n with
  | _.+1, _.+1 ⇒ fun A : 'M_(1 + _, 1 + _) ⇒
    if [pick ij | A ij.1 ij.2 != 0] is Some (i, j) then
      let a := A i j in let A1 := xrow i 0 (xcol j 0 A) in
      let u := ursubmx A1 in let v := a^-1 *: dlsubmx A1 in
      let: (L, U, r) := Gaussian_elimination (drsubmx A1 - v ×m u) in
      (xrow i 0 (block_mx 1 0 v L), xcol j 0 (block_mx a%:M u 0 U), r.+1)
    else (1%:M, 1%:M, 0%N)
  | _, _ ⇒ fun _ ⇒ (1%:M, 1%:M, 0%N)
  end.
```

#### [ Tobias Grosser (Sep 19 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214224):
As implemented in mathcomp.

#### [ Tobias Grosser (Sep 19 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214229):
Need it to compute the matrix rank.

#### [ Tobias Grosser (Sep 19 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214302):
```
polyhedra.lean:196:57: error

function expected at
  matrix x y α
term has type
  Type (max u v)
```

for the last one.

#### [ Tobias Grosser (Sep 19 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214312):
Matrix is defined as `matrix : Π (m n : Type u_1) [_inst_1 : fintype m] [_inst_2 : fintype n], Type u_2 → Type (max u_1 u_2)`

#### [ Tobias Grosser (Sep 19 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214362):
This one works:
```lean

def Gaussian_elimination5 {α : Type v} [ordered_ring α] :
   Π {x y : Type u}  [hx : fintype x] [hy : fintype y], @matrix x y hx hy α → α
| _ _ _ _ _ := by exactI 1
```

#### [ Tobias Grosser (Sep 19 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214378):
Thanks.

#### [ Tobias Grosser (Sep 19 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214379):
Need to read up what all this stuff does.

#### [ Tobias Grosser (Sep 19 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214390):
I am especially surprised that I need to pass the hx, hy as parameters.

#### [ Kevin Buzzard (Sep 19 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214768):
I never answered your question about how to use `pi_instances`. It was used at some point in the code defining matrices, but this was in a branch of mathlib-community in code that got rewritten and then I think the branch was deleted? I couldn't find it anyway. In short, it's a tactic whereby if `f x` has a certain structure (e.g. that of an additive group) then`Pi x, f x` gets it too. For matrices over a ring it would immediately give them the structure of an additive commutative group by just guessing addition and zero and then figuring out the proofs itself. Of course it can't guess multiplication (if you asked it to, I guess it would guess pointwise multiplication of matrices).

#### [ Tobias Grosser (Sep 19 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134214936):
Thanks.

#### [ Tobias Grosser (Sep 19 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215050):
Ok, the last one for this morning:
```
def Gaussian_elimination5 {α : Type v} [ordered_ring α] {x y} [has_one x] [has_one y]:
   Π {x y}  [hx : fintype x] [hy : fintype y], @matrix x y hx hy α  → α
| (x+1) _ _ _ _ := by exactI 1
```

#### [ Tobias Grosser (Sep 19 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215121):
Gives me "equation compiler failed (use 'set_option trace.eqn_compiler.elim_match true' for additional details)".
Setting this option does not give me more details.

#### [ Kenny Lau (Sep 19 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215131):
1. you have two `x` and two `y`, which would cause much confusion, although it is not the source of the error

#### [ Tobias Grosser (Sep 19 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215133):
I wanted x to be both a fintype and a type with has_one.

#### [ Kenny Lau (Sep 19 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215140):
the source of the error is that the type of `(x+1)`, whatever it is, is not an inductive type with `_+1` as one of the constructors

#### [ Tobias Grosser (Sep 19 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215193):
 Right. It's a fintype.

#### [ Tobias Grosser (Sep 19 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215195):
I also want to make it to satisfy has_one.

#### [ Tobias Grosser (Sep 19 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215198):
That's why I added additional constraints.

#### [ Kenny Lau (Sep 19 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215204):
you have two `x` and two `y`. Lean treats those as separate objects.

#### [ Tobias Grosser (Sep 19 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215212):
Right, I lack the notation how to add more constraints on x.

#### [ Tobias Grosser (Sep 19 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215215):
I tried this one before:
```

def Gaussian_elimination5 {α : Type v} [ordered_ring α]  :
   Π {x y} [has_one x] [has_one y]  [hx : fintype x] [hy : fintype y], @matrix x y hx hy α  → α
| (x+1) _ _ _ _ := by exactI 1
```

#### [ Mario Carneiro (Sep 19 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215256):
`x` is not a number, it's a type

#### [ Kenny Lau (Sep 19 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215257):
I don't know what `x+1` is supposed to mean

#### [ Mario Carneiro (Sep 19 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215259):
This differs from the Coq development because matrices are not defined with indices in 1..n, they are drawn from an arbitrary finite type

#### [ Tobias Grosser (Sep 19 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215271):
Right.

#### [ Tobias Grosser (Sep 19 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215277):
I assumed I can fix this by defining my algorithm to only work if x and y are both finite _and_ satisfy has_one.

#### [ Mario Carneiro (Sep 19 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215317):
You could define your function on `matrix (fin m) (fin n) α` if you want to do induction on m and n

#### [ Mario Carneiro (Sep 19 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215322):
there is no problem with assuming your type has a one, but that doesn't license you to write `x+1`

#### [ Tobias Grosser (Sep 19 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215328):
That's what I tried ( I forgot that fin m exists, Johannes mentioned it at some point)

#### [ Mario Carneiro (Sep 19 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215331):
if `x` is a type containing a `1`, then `1 : x` is okay

#### [ Tobias Grosser (Sep 19 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215334):
```lean
def Gaussian_elimination5 {α : Type v} [ordered_ring α]  :
   Π {x y} [hx : fin x] [hy : fin y], @matrix x y hx hy α  → α
| (_+1) _ _ _ _ := by exactI 1
```

#### [ Tobias Grosser (Sep 19 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215411):
Now I am here. This works so far, but gives the error:
```
polyhedra.lean:201:46: error

maximum class-instance resolution depth has been reached (the limit can be increased by setting option 'class.instance_max_depth') (the class-instance resolution trace can be visualized by setting option 'trace.class_instances')
```

#### [ Mario Carneiro (Sep 19 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215418):
`fin` is not a typeclass, it is an actual type
```
def Gaussian_elimination5 {α : Type v} [ordered_ring α]  :
   Π (m n : ℕ), matrix (fin m) (fin n) α  → α
| (m+1) (n+1) := 1
```

#### [ Tobias Grosser (Sep 19 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215562):
Amazing: 
```lean
def Gaussian_elimination6 {α : Type v} [ordered_ring α]  :
   Π (m n), matrix (fin m) (fin n) α  → α
| (m+1) (n+1) A := A 0 0
| _ _ A := (0 : α)
```

#### [ Tobias Grosser (Sep 19 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134215623):
That type checks and does what I want. Thanks guys for getting me started.

#### [ Kevin Buzzard (Sep 19 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134216363):
`has_one` only means there's some term in your type called `1`. You need `has_add` too to make sense of `x + 1`.

#### [ Johan Commelin (Sep 19 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134216462):
Right, so you want `has_one Type` and `has_add Type` (-;

#### [ Tobias Grosser (Sep 19 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217164):
That's what I understand.

#### [ Tobias Grosser (Sep 19 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217168):
Now I don't understand how torequest such a type in a pattern match.

#### [ Tobias Grosser (Sep 19 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217171):
```lean
def Gaussian_elimination5 {α : Type v} [ordered_ring α] :
   Π {x y : Type u} [has_one x] [has_add x] [has_one y] [has_add y] [hx : fintype x] [hy : fintype y], @matrix x y hx hy α → α
| a b c d e f g h i := 
```

#### [ Tobias Grosser (Sep 19 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217173):
This is what I came up with.

#### [ Mario Carneiro (Sep 19 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217219):
you can't pattern match on types

#### [ Kevin Buzzard (Sep 19 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217222):
As a general rule you shouldn't need to name variables which are showing up in `[boxes like this]`

#### [ Kevin Buzzard (Sep 19 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217225):
The system is supposed to do that for you

#### [ Tobias Grosser (Sep 19 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217232):
I don't want to match  on types.

#### [ Tobias Grosser (Sep 19 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217236):
It seems I need to match on all the boxes for this to type check.

#### [ Tobias Grosser (Sep 19 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217239):
What I would like is something like

#### [ Kevin Buzzard (Sep 19 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217247):
You could move stuff to the left of the colon

#### [ Mario Carneiro (Sep 19 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217251):
this line is almost certainly not what you want

#### [ Kevin Buzzard (Sep 19 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217254):
the equation compiler only matches on stuff to the right of the colon

#### [ Kevin Buzzard (Sep 19 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217307):
and similarly in general you should be able to avoid using `@`

#### [ Kevin Buzzard (Sep 19 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217314):
because Lean is supposed to guess correctly

#### [ Mario Carneiro (Sep 19 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217326):
Also, in case it wasn't clear Johan's suggestion above was not serious

#### [ Mario Carneiro (Sep 19 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217332):
you don't actually want `has_add Type`

#### [ Mario Carneiro (Sep 19 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217339):
Perhaps you could explain what you are trying to do informally?

#### [ Kevin Buzzard (Sep 19 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217376):
You're more likely to want `has_add X` with `X : Type`

#### [ Mario Carneiro (Sep 19 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217383):
I'm not sure you want that either though, in this case

#### [ Kevin Buzzard (Sep 19 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217388):
On the other hand, I am pretty sure we want Gaussian Elimination

#### [ Tobias Grosser (Sep 19 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217402):
I want a function that takes a (matrix n m \a) and returns an alpha (for now)

#### [ Kevin Buzzard (Sep 19 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217403):
It's kind of a disgrace that we only just got matrices and that we still don't have differentiation of functions from R to R

#### [ Tobias Grosser (Sep 19 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217404):
I also want to do induction over n and m

#### [ Tobias Grosser (Sep 19 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217406):
So I looked at dependent type pattern matching

#### [ Kevin Buzzard (Sep 19 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217408):
@**Tobias Grosser** your two goals sound very achievable

#### [ Mario Carneiro (Sep 19 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217409):
In that case you should go with the version I stated with `fin m` and `fin n`

#### [ Tobias Grosser (Sep 19 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217410):
And my understanding is that I need to constrain n and m to satisfy has_add and has_one.

#### [ Kevin Buzzard (Sep 19 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217413):
if `fin n` makes sense

#### [ Kevin Buzzard (Sep 19 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217415):
then `n : nat`

#### [ Tobias Grosser (Sep 19 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217458):
Right. That one works perfectly.

#### [ Mario Carneiro (Sep 19 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217463):
`fin m` is a type, which already has a one and an add

#### [ Kevin Buzzard (Sep 19 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217464):
and `nat` already has a 1 and an +

#### [ Kevin Buzzard (Sep 19 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217467):
as does `fin n`

#### [ Tobias Grosser (Sep 19 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217472):
I have a variant that works

#### [ Kevin Buzzard (Sep 19 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217505):
feel free to post code

#### [ Tobias Grosser (Sep 19 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217506):
Which is:
```lean
def Gaussian_elimination6 {α : Type v} [ordered_ring α]  :
   Π (m n), matrix (fin m) (fin n) α  → α
| (m+1) (n+1) A := A 0 0
| _ _ A := (0 : α)
```

#### [ Tobias Grosser (Sep 19 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217554):
(I mean the pattern match, not the gaussian elimination yet)

#### [ Kevin Buzzard (Sep 19 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217556):
gotcha

#### [ Kevin Buzzard (Sep 19 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217558):
You use m and n to mean two different things

#### [ Kevin Buzzard (Sep 19 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217560):
you were doing this with x and y earlier

#### [ Kevin Buzzard (Sep 19 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217562):
I find it quite confusing

#### [ Mario Carneiro (Sep 19 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217563):
I think it was a bad idea to call the types `m` and `n` in the definition of `matrix`

#### [ Tobias Grosser (Sep 19 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217565):
I was asking for has_one has_add out of curiosity (and also it seemed it would be preferable)

#### [ Mario Carneiro (Sep 19 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217569):
we never use lowercase latin for types

#### [ Tobias Grosser (Sep 19 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217572):
```lean
def Gaussian_elimination6 {α : Type v} [ordered_ring α]  :
   Π (m n), matrix (fin m) (fin n) α  → α
| (x+1) (y+1) A := A 0 0
| _ _ A := (0 : α)
```

#### [ Kevin Buzzard (Sep 19 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217573):
The matching only matches stuff to the right of the colon, so you're writing "let m = m + 1".

#### [ Kevin Buzzard (Sep 19 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217618):
I used to do this in mathematics when I was younger -- "I have a quadratic equation x^2+bx+c=0 -- now let's complete the square by setting x=x+b/2"

#### [ Tobias Grosser (Sep 19 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217623):
I am aware that 'n' and 'm' in my original example mean different things.

#### [ Mario Carneiro (Sep 19 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217624):
where would you want to perform an addition, where you can't already?

#### [ Tobias Grosser (Sep 19 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217634):
All is good in this example.

#### [ Kevin Buzzard (Sep 19 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217638):
I never write that now because it's so easy to lose track of whether you're using the old x or the new x. Now I write "let y = x+b/2"

#### [ Tobias Grosser (Sep 19 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217639):
Things work fo rme.

#### [ Kevin Buzzard (Sep 19 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217663):
The only time I let "x=x+1" nowadays is in procedural programming when I actually want the old value to be forgotten forever

#### [ Mario Carneiro (Sep 19 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217710):
Here is a working version that doesn't use fin:
```
def Gaussian_elimination6 {α : Type v} [ordered_ring α] 
  (M N) [fintype M] [fintype N] : matrix M N α  → α
| A := A 0 0
```
But you can't do induction on `m : nat` in this case, since there is no `m`

#### [ Tobias Grosser (Sep 19 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217715):
Right.

#### [ Kevin Buzzard (Sep 19 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217716):
```quote
```lean
def Gaussian_elimination6 {α : Type v} [ordered_ring α]  :
   Π (m n), matrix (fin m) (fin n) α  → α
| (x+1) (y+1) A := A 0 0
| _ _ A := (0 : α)
```
```
Do you see that you're also using the fact that `fin (x+1)` has a zero here.

#### [ Kevin Buzzard (Sep 19 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217722):
Type class inference figured that out for you and let you use it

#### [ Tobias Grosser (Sep 19 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217730):
Yes.

#### [ Tobias Grosser (Sep 19 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217736):
That's why I had to write (0:\a) in the second match.

#### [ Tobias Grosser (Sep 19 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217741):
I think.

#### [ Kevin Buzzard (Sep 19 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217744):
`0` by itself means "the zero of something"

#### [ Tobias Grosser (Sep 19 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217745):
Because in that case it is not known that a zero exists.

#### [ Mario Carneiro (Sep 19 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217746):
Kevin means the `0` in `A 0 0`

#### [ Kevin Buzzard (Sep 19 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217751):
Lean was expecting something of type "fin (x+1)" and you wrote "0"

#### [ Tobias Grosser (Sep 19 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217798):
Right.

#### [ Kevin Buzzard (Sep 19 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217801):
and Lean figured "aah, this must be one of those types that has a zero, let me find an instance of has_zero (fin (x+1)) behind the scenes

#### [ Tobias Grosser (Sep 19 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217812):
I wrote
```lean
def Gaussian_elimination6 {α : Type v} [ordered_ring α]  :
   Π (m n), matrix (fin m) (fin n) α  → α
| (x+1) (y+1) A := A 0 0
| _ _ A := A 0 0 
```

#### [ Tobias Grosser (Sep 19 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217815):
Initially

#### [ Kevin Buzzard (Sep 19 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217828):
Lean's typeclass magic: `example (x : ℕ) : has_zero (fin (x+1)) := by apply_instance`

#### [ Kevin Buzzard (Sep 19 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217835):
your initial approach doesn't work becasue `fin 0` is the empty type and in particular has no zero

#### [ Tobias Grosser (Sep 19 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217838):
Right.

#### [ Tobias Grosser (Sep 19 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217841):
I understood this.

#### [ Tobias Grosser (Sep 19 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217843):
That's very interesting.

#### [ Kevin Buzzard (Sep 19 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217898):
`example : has_zero (fin 0) := by apply_instance -- "failed to generate instance" error`

#### [ Kevin Buzzard (Sep 19 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217911):
This black magic is related to the square bracket stuff and it took me a very long time before I got comfortable with it.

#### [ Tobias Grosser (Sep 19 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217914):
I see.

#### [ Kevin Buzzard (Sep 19 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217924):
In retrospect I wish that people had stressed earlier how basic notation like `0` and `+` worked in Lean

#### [ Tobias Grosser (Sep 19 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217927):
The only thing I do not understand is if it is possible to take Mario's stuff, but expose n and m without introducing 'fin n', but instead just use has_one and has_add.

#### [ Kevin Buzzard (Sep 19 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217928):
because it seems to me that this is a very good introduction to the type class system

#### [ Tobias Grosser (Sep 19 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217935):
I feel this should work, but seems to be far beyond my type_class capabilities.

#### [ Kevin Buzzard (Sep 19 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217937):
I'm afraid I'm not a computer scientist and I don't know what "expose" means

#### [ Tobias Grosser (Sep 19 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217970):
As I have a solution, that's not needed. But would be nice to understand this eventually.

#### [ Kevin Buzzard (Sep 19 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217983):
`matrix` eats something of type `fin n`

#### [ Kevin Buzzard (Sep 19 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217987):
so you have to give it something of type `fin n`

#### [ Mario Carneiro (Sep 19 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217989):
actually it eats a fintype

#### [ Tobias Grosser (Sep 19 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217992):
"expose" means pattern match on n and m to be able to do induction on n and m

#### [ Tobias Grosser (Sep 19 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134217994):
Right. I can pass it a fin n and all is good.

#### [ Kevin Buzzard (Sep 19 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218002):
wait, that's not even true any more

#### [ Tobias Grosser (Sep 19 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218005):
I was wondering if I could pass it a fintype x, where I know that x has_add and has_one.

#### [ Mario Carneiro (Sep 19 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218006):
any fintype has a cardinality, `fintype.card X`, and you can do induction on that

#### [ Kevin Buzzard (Sep 19 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218012):
sorry, I seem to be behind the times

#### [ Kevin Buzzard (Sep 19 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218023):
`#check @matrix -- matrix : Π (m n : Type u_1) [_inst_1 : fintype m] [_inst_2 : fintype n], Type u_2 → Type (max u_1 u_2)`

#### [ Mario Carneiro (Sep 19 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218026):
You don't usually need a one and an add on the index type

#### [ Mario Carneiro (Sep 19 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218035):
what is this needed for?

#### [ Tobias Grosser (Sep 19 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218072):
So how can I do induction over card? That's what I am trying to figure out.

#### [ Mario Carneiro (Sep 19 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218079):
It's a bit messy

#### [ Kevin Buzzard (Sep 19 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218084):
Do you want to prove things for matrices indexed by random finite types?

#### [ Tobias Grosser (Sep 19 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218085):
I just want to do induction on my dimensionality to do gaussion elimination.

#### [ Tobias Grosser (Sep 19 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218090):
No. If you tell me 'fin x' is enough, we are done.

#### [ Kevin Buzzard (Sep 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218103):
I guess this is a design decision

#### [ Tobias Grosser (Sep 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218104):
Just got curious about the type classes. Seems matlib likes to generalize things.

#### [ Tobias Grosser (Sep 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218111):
I am fine being in 'fin x'. That seems a lot less messy.

#### [ Kevin Buzzard (Sep 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218113):
Yes, if mathlib did Gaussian Elimination it would almost certainly do it for random types which are fintypes

#### [ Tobias Grosser (Sep 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218114):
Let's leave it at this for now.

#### [ Mario Carneiro (Sep 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218116):
```
def Gaussian_elimination6 {α : Type v} [ordered_ring α] 
  : ∀ (m n M N) [fintype M] [fintype N], fintype.card M = m → fintype.card N = n → matrix M N α  → α
| m n M N _ _ h1 h2 A := A 0 0
```
You will need some `@`'s in there, my typechecker isn't running

#### [ Kevin Buzzard (Sep 19 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218164):
If you do it like that then you can induct on m and n

#### [ Mario Carneiro (Sep 19 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218173):
More likely, I would just do it on `fin m` by induction and then use equivalence lemmas to transfer to the original fintype

#### [ Kevin Buzzard (Sep 19 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218187):
```lean
failed to synthesize type class instance for
α : Type v,
_inst_1 : ordered_ring α,
m : ?m_1,
n : ?m_2,
M : Type ?,
N : Type ?,
_inst_2 : fintype M,
_inst_3 : fintype N
⊢ fintype M
```

#### [ Kevin Buzzard (Sep 19 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218188):
boo

#### [ Mario Carneiro (Sep 19 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218189):
Or find a way to work with subsets of a fixed type of size `m`

#### [ Mario Carneiro (Sep 19 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218193):
you have to put a `by exactI` in there

#### [ Kevin Buzzard (Sep 19 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218199):
in the statement??

#### [ Mario Carneiro (Sep 19 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218200):
yeah

#### [ Mario Carneiro (Sep 19 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218244):
because there are typeclass args right of the colon

#### [ Mario Carneiro (Sep 19 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218249):
either that or use `@` a lot

#### [ Kenny Lau (Sep 19 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218261):
deja vu

#### [ Kevin Buzzard (Sep 19 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218284):
```lean
def Gaussian_elimination6 {α : Type v} [ordered_ring α]
  : ∀ (m n M N) [fintype M] [fintype N],
      by exactI fintype.card M = m → fintype.card N = n → matrix M N α  → α
| m n M N _ _ h1 h2 A := sorry
```

#### [ Kevin Buzzard (Sep 19 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218287):
eew

#### [ Kevin Buzzard (Sep 19 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218289):
soon to be not fixed in Lean 4

#### [ Kevin Buzzard (Sep 19 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218347):
that looks fine, not at all confusing for beginners

#### [ Mario Carneiro (Sep 19 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218357):
like I said, messy

#### [ Kevin Buzzard (Sep 19 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218362):
Isn't there some pre-rolled `fintype.induction_on`?

#### [ Mario Carneiro (Sep 19 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218371):
not to mention that this is not going to be a nice inductive proof since you have to build a recursive subtype

#### [ Mario Carneiro (Sep 19 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218392):
It's probably better to do induction over the finsets on a fixed type

#### [ Tobias Grosser (Sep 19 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218397):
Cool. At least it works.

#### [ Tobias Grosser (Sep 19 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218450):
I feel I can do induction by using x+1 and y+1
```lean
def Gaussian_elimination6 {α : Type v} [ordered_ring α]
  : ∀ (m n M N) [fintype M] [fintype N],
      by exactI fintype.card M = m → fintype.card N = n → matrix M N α  → α
| (x+1) (y+1) M N _ _ h1 h2 A := (0 : α)
| _ _ M N _ _ h1 h2 A := (0 : α)
```

#### [ Tobias Grosser (Sep 19 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218453):
Not sure what recursive subtypes mean.

#### [ Tobias Grosser (Sep 19 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218458):
I will start with the (fin n) stuff, which is sth I certainly understand.

#### [ Tobias Grosser (Sep 19 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218467):
If all works, I can see if I can generalize things.

#### [ Mario Carneiro (Sep 19 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218488):
when applying the induction hypothesis, you will need to build a type that contains one fewer element than the type you started with

#### [ Tobias Grosser (Sep 19 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218503):
I see. That's annoying. I will certainly stay with (fin n)

#### [ Tobias Grosser (Sep 19 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218568):
Thanks again. Now I learned quite a bit. Will need to read up on exactI in type definitions.

#### [ Sean Leather (Sep 19 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/partial%20order%20for%20matrix/near/134218604):
```quote
Will need to read up on exactI in type definitions.
```

Note that tactics are simply ways of generating code. They can appear in definitions or proofs. It's just that they are most useful in proofs.


{% endraw %}
