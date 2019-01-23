---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/97622inverseof.html
---

## Stream: [general](index.html)
### Topic: [inverse of $](97622inverseof.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186287):
is there an inverse of `$`? (the backwards pipe operator`<|`)  i.e. instead of `g (f x)` being written as `g $ f x` I'd like to write `f x <| g`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Brendan Zabarauskas (May 28 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186348):
I though `$` was backwards pipe? Do you mean you'd like to write `x |> f |> g`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Brendan Zabarauskas (May 28 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186357):
(big fan of directional composition/application operators at any rate)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186402):
er, maybe it's a forwards pipe? but yes, I'd like to reverse the order that function arguments appear

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186414):
in fact, I just googled and yeah, seems I have my directions mixed up, whoops

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Brendan Zabarauskas (May 28 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186455):
To be more precise, I'd also recommend saying 'apply' and 'application' rather than 'pipe', which is a little ambiguous.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186527):
short answer: no

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186532):
I believe that operator is used for `option.lhoare`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186590):
eughhh. `|>` and `<|` have been around for ages  to represent reverse and forward function application.... maybe I can steal them back after Lean 4 releases

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186593):
I think that `lhoare` and `rhoare` are surprisingly useless operators

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Brendan Zabarauskas (May 28 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186631):
what on earth is a `hoare`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186634):
I have never seen a use for them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186635):
as in tony

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Brendan Zabarauskas (May 28 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186636):
hoare logic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186637):
i don't have a problem with useless library files, but the problem is you can't unset global notation :(

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Brendan Zabarauskas (May 28 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186688):
Also a big fan of `>>` and `<<` for composition (as in F#, Elm), but those are often stolen by haskell-like langs for monady stuff. I just say use `*>` and `<*` from applicative instead.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186692):
looks like `lhoare` and `rhoare` are not used anywhere in core either

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186700):
`rhoare` is almost the same as `option.guard` but its logic is reversed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186748):
maybe I can get @**Sebastian Ullrich** to burninate it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186757):
for symmetry reasons I'd vote for that, `|>` and `<|` is more pleasant to look at than dollar signs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186798):
the dollar's not going anywhere though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186799):
and whatever arbitrary unicode symbol i would pick to replace `<|`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186804):
what about `<$`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186805):
yea, I know the dollar sign is one character and from haskell

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186808):
that is more obviously related to application

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186814):
I assume `<|` and `|>` have something to do with orelse

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186815):
and the hoare things are also orelsey

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186818):
`|>` and `<|` is ocaml notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186864):
does haskell have a `<|` equiv

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186876):
I assume that haskell has a meaning for every sequence of <= 3 punctuation chars

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186921):
I can get behind `<$` if `$` is sticking around

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186928):
But don't you want `$>` ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186929):
That seems more intuitive to me...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186971):
But then, I've never used OCaml

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186977):
as in `g (f x)` would be written `f x $> g`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186980):
Yes...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186981):
The `>` conveys in which way the arguments flow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127186985):
Just like in Bash...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 05:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187024):
if you write to a file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 05:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187027):
i can see that some might prefer that, i always thought of it as moving the top function instead of the arguments

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187035):
Ok, that also makes sense...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187036):
I was thinking `$` with a reversal, so a backward arrow to indicate that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187038):
oh, `<$` is taken...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187039):
`functor.map_const`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 05:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187078):
What about `$<` ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 05:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187082):
(No lean here, atm)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187083):
i prefer the bracket to be on the correct side of the dollar sign, haha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187089):
`$<` is clear

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187090):
yeah, that's why it's taken :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187135):
I guess `<$` is named similar to `<$>`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187190):
when lean 4 is released I will have to be very quick and reserve `|>` and `<|` as fast as possible in some large library most users install...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187229):
since it seems those might have a chance of being deleted anyway

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187243):
or maybe there's some unicode variant of the eq.subst triangle hanging around

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187284):
there is unicode for everything

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187288):
`◁ `?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187289):
= \lhd

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187299):
but mathematicians are also jockeying for these symbols

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 05:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187301):
this operator is so commonly used I'm boggled nobody has complained about it yet in this chat

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 05:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187302):
I hope in Lean 4 there will be a way to selectively import notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187344):
`import foo with bar as xyzzy`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187345):
Like in python

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187346):
am I really the first person to miss the dual of `$`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187347):
for CS things I prefer ascii because mathematicians won't lower themselves to use them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187354):
lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187355):
well, it is obviously redundant...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187411):
@**Andrew Ashworth** So plug a zero-width char in between, an create a keyboard shortcut to type the 3-char-combo. Or does VScode not render 0-width-chars with 0 width?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187414):
nooo

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187420):
Or use `local notation` to override the global stuff. I did that with `[n]`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187471):
Does Lean recognize 0-width space as whitespace?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187570):
i guess.. but when people do more actual programming, it's nice to write something like `[1..10] |> map f` (with the arrow the way Johan likes it)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 28 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187574):
I was going to say, isn't `|>` the flipped application?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 28 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187576):
But in lean, can't you write `[1..10].map f`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187619):
`[1..10]` might be some arbitrary expression that spans multiple lines

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187621):
```
def «te​st» := 1
#print «te​st»
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187625):
it doesn't like it as a space or as an identifier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187627):
also I've completely got the application directions mixed up in my head, if I could delete it all I would :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 28 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187636):
I don't really see what you gain over using parentheses or a variety of other options

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187639):
/me should prove `fermаt_lаst_theorem` in a couple lines, after importing https://github.com/formalabstracts/formalabstracts/blob/master/fabstract/Wiles_A_and_Taylor_R_FermatLast/fabstract.lean, and some other obscure libraries... :stuck_out_tongue_winking_eye:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 28 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187684):
The uses I know of for flipped application are when you have left-to-right type inference / overloading resolution (Haskell doesn't have this, Lean might, not sure) or you want the order of effects to be left-to-right (Haskell has `>>=`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187687):
No-one will notice that I used a Cyrillic `a` in `fermat`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 28 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187695):
And of course it can be a style thing. One can debate the merits of having more styles available versus having fewer styles available

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 28 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187696):
Just want to point out that I am a mathematician who loves ascii

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187790):
it is a little redundant, yes, you can argue field notation, `$`, and parens should be all you need, for me it's a stylistic issue v0v

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187801):
it's a bigger deal in F# because as you mentioned type checking is done left-to-right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187845):
but it enables you to build up nice looking data transformation definitions that look natural

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187851):
actually the type checking thing is a good point

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187891):
with no parentheses like you might need with Lean's field notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 06:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127187900):
```quote
actually the type checking thing is a good point
```
how so?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127188224):
hm, I'm having trouble coming up with an example of a difference from the order change

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 28 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127188228):
but in theory there should be some differences due to the parse order, which does matter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 28 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inverse%20of%20%24/near/127188235):
consider this F# snippet: 
```fsharp
let res = 
  [ 1 .. 10 ] 
  |> List.filter isEven
  |> List.map formatInt
```
writing this in Lean using field notation is a little cumbersome, and doesn't look as pretty


{% endraw %}
