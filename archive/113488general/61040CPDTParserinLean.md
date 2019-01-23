---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/61040CPDTParserinLean.html
---

## Stream: [general](index.html)
### Topic: [CPDT Parser in Lean](61040CPDTParserinLean.html)

---


{% raw %}
#### [ Kevin Buzzard (Jun 09 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127822804):
My son got interested in parsers and I'm trying to understand them better by implementing the simple parser at the beginning of Certified Programming with Dependent Types. But actually I find making these inductive types quite hard -- in my area of expertise we don't really ever use complicated inductive structures like the ones showing up in these parsers. Here's an example of one I'm struggling with: in Coq it's

#### [ Kevin Buzzard (Jun 09 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127822805):
```
Fixpoint progDenote (p : prog) (s : stack) : option stack :=
match p with
| nil ⇒ Some s
| i :: p’ ⇒
match instrDenote i s with
| None ⇒ None
| Some s’ ⇒ progDenote p’ s’
end
end.
```

#### [ Kevin Buzzard (Jun 09 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127822809):
http://adam.chlipala.net/cpdt/cpdt.pdf

#### [ Kevin Buzzard (Jun 09 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127822814):
page 21

#### [ Kevin Buzzard (Jun 09 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127822933):
I tried writing it by hand with `list.rec_on` (`prog := list instr`) but I seemed to end up knowing `progDenote p' s` rather than `progDenote p' s'`. Presumably this is the sort of thing the equation compiler can do for me somehow? Or is there some complicated issue which makes this definition problematic? I know very little about this sort of stuff beyond `rec`.

#### [ Kevin Buzzard (Jun 09 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127822935):
Oh I see now, I should somehow carry s around as a parameter

#### [ Simon Hudon (Jun 09 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127822977):
Do you also have the definition of `stack`?

#### [ Kevin Buzzard (Jun 09 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823139):
```lean
definition progDenote (p : prog) : stack → option stack :=
list.rec_on p some $ 
  λ i p' pDp' s,option.rec_on (instrDenote i s) none pDp'
```

#### [ Kevin Buzzard (Jun 09 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823140):
So I can just do it in term mode

#### [ Kevin Buzzard (Jun 09 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823192):
I am slightly unnerved by how incomprehensible mine looks compared to Chlipata's

#### [ Kevin Buzzard (Jun 09 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823199):
`definition stack := list ℕ`

#### [ Kevin Buzzard (Jun 09 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823252):
you can plough through http://adam.chlipala.net/cpdt/html/Cpdt.StackMachine.html to find these. I see my error now -- I should have been inducting on p before introducing s. These are subtleties I don't usually run into in my area of mathematics, you rarely induct on something other than nat

#### [ Simon Hudon (Jun 09 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823257):
You can also write it:

```lean
definition progDenote (p : prog) : stack → option stack
 | [] := ...
 | (s :: ss) := ...
```

#### [ Simon Hudon (Jun 09 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823260):
Which I find prettier than Coq

#### [ Simon Hudon (Jun 09 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823364):
Sorry, I should write:

```lean
definition progDenote : prog  → stack → option stack
 | [] s := some s
 | (p :: ps) s := instrDenote p s >>= progDenote ps
```

#### [ Kevin Buzzard (Jun 09 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823365):
Oh thanks!

#### [ Kevin Buzzard (Jun 09 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823369):
I was just working on this myself but I'm not sure I would have hit upon that crazy smiley thing

#### [ Simon Hudon (Jun 09 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823370):
is `>>=` the smiley? :)

#### [ Kevin Buzzard (Jun 09 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823419):
I guess he looks pretty sad :-/

#### [ Simon Hudon (Jun 09 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823468):
Or angry? I see `>>` as eyebrows and `=` as a nose

#### [ Kevin Buzzard (Jun 09 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823527):
OK here's my effort:

#### [ Kevin Buzzard (Jun 09 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823530):
```lean
definition progDenote' : prog → stack → option stack
| ([]) := some
| (i :: p') := λ s, match (instrDenote i s) with
  | none := none
  | some s' := progDenote' p' s'  
  end  
```

#### [ Kevin Buzzard (Jun 09 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823537):
So you are doing the match with this crazy smiley?

#### [ Kevin Buzzard (Jun 09 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823571):
I can see that your `progDenote ps` is my `progDenote p'` and then other than that I am sending `none` to `none` and `s'` to `s'`. You're exploiting this in some way?

#### [ Kevin Buzzard (Jun 09 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823587):
PS @**Simon Hudon** I felt quite bad a week or so ago when I was trying to write some notation and didn't understand binding powers and was in a rush and you tried to explain them and I just said `just gimme the number!`

#### [ Simon Hudon (Jun 09 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823589):
Yes, with option, `>>=` returns `none` if either of its parameters does

#### [ Kevin Buzzard (Jun 09 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823590):
It was partially because of that incident that I thought it was time to learn about parsers!

#### [ Kevin Buzzard (Jun 09 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823635):
Aah I see you're explictly utilising the fact that it's a monad?

#### [ Simon Hudon (Jun 09 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823640):
No worries, I got that you were in a rush. And I know I'd always prefer to get deeper into it. But thanks for coming back to it :)

#### [ Simon Hudon (Jun 09 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823641):
Exactly!

#### [ Simon Hudon (Jun 09 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823688):
In Coq, he'd have to do some work to bring that in but it's just there for us in Lean so it's good to get used to it

#### [ Simon Hudon (Jun 09 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127823993):
The operators are a bit broken but in Haskell, I'd rather write `progDenote ps =<< instrDenote p s`. It's a bit like function application with monads (you apply `progDenote ps` to the result of `instrDenote p s`)

#### [ Kevin Buzzard (Jun 09 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127824101):
I have my compiler working now and I'd like to do some unit tests using `#eval`. This means as far as I can see that I have to go and define a bunch of `has_repr` instances.

#### [ Kevin Buzzard (Jun 09 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127824102):
Here's one:

#### [ Kevin Buzzard (Jun 09 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127824110):
```lean
inductive binop
| Plus : binop 
| Times : binop 

open binop 

instance : has_repr binop := ⟨λ b, match b with
    | Plus := "add"
    | Times := "mul" 
    end 
⟩
```

#### [ Kevin Buzzard (Jun 09 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127824112):
I just wanted to write

#### [ Kevin Buzzard (Jun 09 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127824115):
```lean
instance : has_repr binop := ⟨
    | Plus := "add"
    | Times := "mul" 
    end 
⟩
```

#### [ Kevin Buzzard (Jun 09 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127824116):
but that didn't work so I had to put all the match waffle in. Am I missing something?

#### [ Simon Hudon (Jun 09 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPDT%20Parser%20in%20Lean/near/127824169):
No I think that's the way to do it. I was looking to see if it could be generated for you but I haven't found tactics for that


{% endraw %}
