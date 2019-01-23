---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/77939AdventofCode.html
---

## Stream: [general](index.html)
### Topic: [Advent of Code](77939AdventofCode.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Dec 01 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150682850):
adventofcode.com in Lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 01 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150683859):
Does anyone know how to use Lean to read a file from disk, and get a `list int` if each line looks like an integer?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Dec 01 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150683922):
I just pasted into lean file! But that's a better idea!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 01 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150683931):
I thought about pasting, but I guess that's not a reasonable strategy if you want to do all 50 puzzles

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 01 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150683932):
And someone needs to write a IO monad howto anyway

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Dec 01 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150684498):
I completed it but I used `meta`. I feel dirty.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 01 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150684511):
Did you use IO?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Dec 01 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150684515):
nope

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 01 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150684561):
Would you know how to read from a file?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 01 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150684565):
```lean
import system.io data.buffer.parser data.int.basic
open tactic parser

def number : parser ℕ :=
string.to_nat <$> many_char1 (sat $ λ c,
  '0'.to_nat ≤ c.to_nat ∧ c.to_nat ≤ '9'.to_nat)

def signed_number : parser ℤ :=
ch '+' >> (int.of_nat <$> number) <|>
ch '-' >> ((λ x:ℕ, -x) <$> number)

run_cmd do
  s ← tactic.unsafe_run_io $ io.fs.read_file "dat.txt",
  sum.inr l ← return $ run (many (signed_number <* ch '\n')) s,
  trace l
```
```
[13,
 -(2+1),
 -(7+1),
 14,
 16,
 -(6+1),
 3,
 -(6+1),
 9,
 -(9+1),
 16,
...
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 01 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150684582):
maybe @**Sebastian Ullrich** knows the correct way to call IO from `run_cmd`, but `unsafe_run_io` works in a pinch

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Dec 01 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150684636):
I think you can use `#eval`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 01 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150684702):
oh, I should have used `to_string`, the output is much nicer
```lean
import system.io data.buffer.parser
open parser

def number : parser ℕ :=
string.to_nat <$> many_char1 (sat $ λ c,
  '0'.to_nat ≤ c.to_nat ∧ c.to_nat ≤ '9'.to_nat)

def signed_number : parser ℤ :=
ch '+' >> (int.of_nat <$> number) <|>
ch '-' >> ((λ x:ℕ, -x) <$> number)

#eval do
  s ← io.fs.read_file "dat.txt",
  sum.inr l ← return $ run (many (signed_number <* ch '\n')) s,
  trace (to_string l) (return ())
```
```
[13, -3, -8, 14, 16, -7, 3, -7, 9, -10, 16, 13, 12, 12, 4, 19, -2, -5, -15, -2, -13, -11, -13, -2, ...
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 01 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150684754):
For some reason the output or return value of the io is ignored, so I had to to a hack with `trace` to get it to print

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 01 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150684902):
Thanks Mario! It allowed to complete Day 1, adding only 15 characters to your code :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Dec 01 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150684972):
Did you do the second part?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 01 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150685393):
here's how I did the first part in lean:
```lean
#eval 0
+13
-3
-8
+14
+16
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 01 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150686187):
No, I decided I should stop distractions for a while. And also the question looked masochistic to do in functional rather than imperative language

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 01 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150686195):
Mario, was that all your input?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Dec 01 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150687782):
I had to use `#eval (0 : int)` since the first line of the input was negative.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 02 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150703402):
I solved it too. But my solution took 40 seconds to run

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 02 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150703410):
The first part, I mean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 02 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150703754):
Doing the second part in non-meta Lean seems pretty interesting

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 02 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150715253):
I think this is a good test case for the conventional programming capabilities of lean. Here's my solution for day 2 pt 1:
```lean
import system.io data.buffer.parser meta.rb_map data.list.basic
open parser

def letter : parser char :=
sat (λ c, 'a'.to_nat ≤ c.to_nat ∧ c.to_nat ≤ 'z'.to_nat)

def count1 {α lt} [decidable_rel lt] (c : rbmap α ℕ lt) (a : α) : rbmap α ℕ lt :=
c.insert a $ match c.find a with
| (some n) := n + 1
| none := 1
end

def get_counts (l : list char) : bool × bool :=
let m := list.foldl count1 (mk_rbmap char ℕ) l in
m.fold (λ c n ⟨r₁, r₂⟩, ⟨r₁ ∨ n = 2, r₂ ∨ n = 3⟩) (ff, ff)

#eval do
  s ← io.fs.read_file "dat.txt",
  sum.inr ls ← return $ run (many (many letter <* ch '\n')) s,
  let (l₁, l₂) := (ls.map get_counts).unzip,
  trace (to_string (l₁.count tt * l₂.count tt)) (return ())
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 02 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150715398):
@**Reid Barton**  As for doing the day 1 pt 2 in non-meta lean, it was obviously intended to have a solution with unbounded iteration, and it is possible to have such a program never halt on some inputs. With some significant additional work you can actually decide whether an input will halt (by looking at whether the numbers are all distinct mod the period), and so you could get a fully correct non-meta lean solution that way (which is even better than the naive algorithm because it will tell you when the infinite stream has no duplicates).

But if you just want the easy solution, the simplest approach is just to have a depth limiter, and increase it until you get the answer.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 03 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150794896):
To avoid spamming the chat I won't report daily, but I think I will take up this challenge. Follow along at https://github.com/digama0/advent-of-code (spoiler alert)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Dec 04 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150837825):
On part day 1 part 2, I believe you can show that the search terminates if two elements of your list are equal mod (answer to part 1). So I started coding up a non-meta algorithm but then I realized it would sap away my entire Saturday so I stopped.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 04 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150837987):
Did you see my solution?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 04 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150837992):
I did that algorithm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 04 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150838001):
and it did sap a good chunk of my day ;)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 04 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150838140):
you can actually do a bit better than producing a proof of well foundedness to run the search... when two values have the same mod the period, you find the least difference of divs, and that's where the search will terminate (so you can do the whole thing without actually running those passes)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Dec 04 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150838882):
Yeah that's how I was going to do it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Dec 04 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150839362):
@**Mario Carneiro** thanks for sharing your solutions. There are still lots of language/mathlib features I am neglecting! Eg `withtop`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Dec 04 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150841457):
Also @**Mario Carneiro**  in the parsers for numbers and letters you can use `sat $ char.is_lower` and `char.is_digit` instead of manually checking the char.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 04 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150841473):
oh, lovely

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 04 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Advent%20of%20Code/near/150841529):
I'm hoping that the conventional programming capabilities of lean will be boosted by these attempts

