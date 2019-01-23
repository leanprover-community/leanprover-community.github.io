---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/63778coqwoes.html
---

## Stream: [general](index.html)
### Topic: [coq woes](63778coqwoes.html)

---


{% raw %}
#### [ Sean Leather (Apr 24 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125609345):
I'm stuck on trying to understand something in a Coq proof. Any experts on here who can spare a few minutes to help?

#### [ Sean Leather (Apr 24 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125609411):
The issue is partially at [`typ_open_types`](https://github.com/spl/formal_binders/blob/master/ML_Core_Infrastructure.v#L423-L431), which uses [`typ_body`](https://github.com/spl/formal_binders/blob/master/ML_Core_Definitions.v#L78-L81).

#### [ Sean Leather (Apr 24 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125609462):
There is an `exists` in `typ_body`, and I'm trying to figure out how it is used in the proof of `typ_open_types`.

#### [ Kevin Buzzard (Apr 24 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125609466):
Is there a coq chatroom like this one?

#### [ Kevin Buzzard (Apr 24 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125609469):
Of course I cannot help at all, I was just wondering.

#### [ Kevin Buzzard (Apr 24 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125609470):
There's certainly a mailing list, right?

#### [ Sean Leather (Apr 24 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125609474):
```quote
Is there a coq chatroom like this one?
```
No idea.

#### [ Sean Leather (Apr 24 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125609483):
```quote
There's certainly a mailing list, right?
```
I don't want to sign up for one if I don't have to. :wink:

#### [ Sean Leather (Apr 24 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125609486):
I'm trying to translate this into Lean.

#### [ Sean Leather (Apr 24 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125609531):
I've been doing fine so far, but this part has me a bit stuck.

#### [ Moses Schönfinkel (Apr 24 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610071):
You need to help me help you on this one, because it uses some non-standard stuff :). So from looking at the thing, your `typ_body` is now some `L` for which `K`. Then they do `pick_freshes`? What is that :)? And is `poses` some variation on `pose`?

#### [ Sean Leather (Apr 24 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610073):
```quote
You need to help me help you on this one, because it uses some non-standard stuff :).
```
Absolutely!

#### [ Sean Leather (Apr 24 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610085):
`pick_freshes` is a tactic.

#### [ Sean Leather (Apr 24 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610087):
`poses` is another tactic.

#### [ Moses Schönfinkel (Apr 24 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610088):
Ooh, now it's all clear then!

#### [ Sean Leather (Apr 24 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610089):
`LibTactic.v` I believe. I usually `grep` for it.

#### [ Moses Schönfinkel (Apr 24 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610091):
Alright, let's see :).

#### [ Sean Leather (Apr 24 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610139):
What does `introv [L K]` mean?

#### [ Moses Schönfinkel (Apr 24 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610141):
It destructs the existential into two parts.

#### [ Sean Leather (Apr 24 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610144):
Right, thought so.

#### [ Moses Schönfinkel (Apr 24 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610153):
Your `introv [L K] WT` basically first `intros T Us`.

#### [ Sean Leather (Apr 24 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610159):
And `rewrite*` and `apply*` just pull hypotheses from the context, right?

#### [ Moses Schönfinkel (Apr 24 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610161):
Yes.

#### [ Sean Leather (Apr 24 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610204):
... which makes it difficult to figure out what's getting used.

#### [ Moses Schönfinkel (Apr 24 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610205):
Btw, I don't think `LibTactics.v` has these `pick_freshes`. It might be coming from something home-baked there?

#### [ Moses Schönfinkel (Apr 24 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610209):
There's a `Metatheory` import there, whatever that is.

#### [ Sean Leather (Apr 24 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610210):
Oh, `pick_freshes` comes from `Metatheory_var.v` or `Metatheory_fresh.v`.

#### [ Sean Leather (Apr 24 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610220):
Err, or `Metatheory_Env.v`.

#### [ Sean Leather (Apr 24 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610277):
Correction: `ML_Core_Infrastructure.v`.

#### [ Sean Leather (Apr 24 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610293):
Also, I meant `Lib_Tactic.v` in this project.

#### [ Sean Leather (Apr 24 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610344):
[`pick_fresh` and `pick_freshes`](https://github.com/spl/formal_binders/blob/master/ML_Core_Infrastructure.v#L113-L117)

#### [ Sean Leather (Apr 24 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610349):
[`poses`](https://github.com/spl/formal_binders/blob/master/Lib_Tactic.v#L32-L33)

#### [ Sean Leather (Apr 24 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610420):
I think I get the gist of those. What I'm currently struggling with is what happens to the `L` and `K`. Do they get used and how?

#### [ Sean Leather (Apr 24 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610490):
Because `K` is a function, right? Something like this out of `typ_body`:

```coq
forall Xs, fresh L n Xs -> type (typ_open_vars T Xs)
```

#### [ Moses Schönfinkel (Apr 24 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610498):
`pick_fresh` and `poses` don't seem to do anything funny to them, so `rewrite* (@typ_substs_intro Xs). apply* typ_substs_types` so it's either of these two invocations.

#### [ Sean Leather (Apr 24 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610503):
I agree.

#### [ Moses Schönfinkel (Apr 24 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610509):
Yes, `K` is a function.

#### [ Sean Leather (Apr 24 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610548):
I think the culprit is [`typ_substs_intro`](https://github.com/spl/formal_binders/blob/master/ML_Core_Infrastructure.v#L380-L386).

#### [ Sean Leather (Apr 24 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610566):
```coq
Lemma typ_substs_intro : forall Xs Us T,
  fresh (typ_fv T \u typ_fv_list Us) (length Xs) Xs ->
  types (length Xs) Us ->
  (typ_open T Us) = typ_substs Xs Us (typ_open_vars T Xs).
```

#### [ Sean Leather (Apr 24 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610591):
(So sacrilege: pasting Coq onto a Lean forum...)

#### [ Moses Schönfinkel (Apr 24 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610674):
Right, so the last apply in the original proof is probably discharging one of the unresolved arguments of rewrites resulting from rewriting `typ_subst_intro`.

#### [ Sean Leather (Apr 24 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610679):
(BTW, it would be nice if I could run this. I tried, fixed a few things, but `coqc Lib_ListFacts.v` doesn't finish in several hours.)

#### [ Moses Schönfinkel (Apr 24 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610760):
Well that's the overarching problem of reading Coq. (Btw, even `rewrite*` is non-standard.)

#### [ Moses Schönfinkel (Apr 24 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610828):
Still, we rewrite `(typ_open T Us)` with `typ_subst Xs Us (typ_open_vars T Xs)`, we have `Xs Us T` from rewriting, there should be 2 new obligations, `fresh (...)` and `types ...`. Either of these may have been discharged by some form of `assumption` resulting from `rewrite*`, leaving the last one for the final `apply`.

#### [ Sean Leather (Apr 24 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610833):
So my confusion comes down to this (I think): when `typ_body` is destructed into `L` and `K` as `forall Xs, fresh L n Xs -> type (typ_open_vars T Xs)`, is `K` being used, and, if so, how does `fresh L n Xs ` get instantiated since nothing is known about `L`?

#### [ Moses Schönfinkel (Apr 24 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610946):
It doesn't necessarily need to be instantiated for `K` to still be used.

#### [ Moses Schönfinkel (Apr 24 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610966):
I don't think the `rewrite*` or `apply*` would go beyond defeq or some form of `assumption` (resulting from the `*` suffix).

#### [ Moses Schönfinkel (Apr 24 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611013):
You can still use `K` to discharge `Pi_Xs, _ -> _` which is what I think ends up happening.

#### [ Sean Leather (Apr 24 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611076):
`typ_subst_intro` expects `fresh (typ_fv T \u typ_fv_list Us) (length Xs) Xs`. Where does that come from?

#### [ Moses Schönfinkel (Apr 24 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611153):
It's probably either `Fr` or `Fr'`, resulting from `pick_freshes` and `assumption`'d from the `rewrite*` call.

#### [ Sean Leather (Apr 24 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611178):
Ah, right.

#### [ Moses Schönfinkel (Apr 24 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611236):
`apply* typ_substs_types` then most likely solves `types (length Xs) Us`

#### [ Moses Schönfinkel (Apr 24 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611248):
Can logically `K` and `L` help with that? let's see. So they basically map a "parameterized" fresh name to a parameterized type?

#### [ Moses Schönfinkel (Apr 24 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611293):
It is most likely the case that it's the very last tactic (`apply*`) that uses `K` in the `Pi` form.

#### [ Sean Leather (Apr 24 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611304):
```coq
rewrite* (@typ_substs_intro Xs). apply* typ_substs_types.
```

```coq
Lemma typ_substs_types : forall Xs Us T,
  types (length Xs) Us ->
  type T ->
  type (typ_substs Xs Us T).
```

#### [ Sean Leather (Apr 24 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611313):
```quote
You can still use `K` to discharge `Pi_Xs, _ -> _` which is what I think ends up happening.
```
I don't understand this.

#### [ Moses Schönfinkel (Apr 24 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611446):
It's as you said, there is no reasonable way to instantiate it. So we can just end up assuming the argument comes from someplace.

#### [ Moses Schönfinkel (Apr 24 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611464):
Aka. the goal transforming to `fresh L n Xs -> type (typ_open_vars T Xs)` (or `fresh L n Xs |- type (...)`)

#### [ Sean Leather (Apr 24 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611572):
I'm thinking it would help me to understand `poses`/`pose` better.

#### [ Sean Leather (Apr 24 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611630):
And to figure out where `Fr` comes from.

#### [ Moses Schönfinkel (Apr 24 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611637):
I think `Fr` and `Fr'` are related to the other hypothesis?

#### [ Moses Schönfinkel (Apr 24 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611647):
At least if `pick_freshes` doesn't ever mess with either `L` or `K`.

#### [ Moses Schönfinkel (Apr 24 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611652):
Which it doesn't seem to becasue its argument is a subterm of the other hypothesis (`length Us`).

#### [ Sean Leather (Apr 24 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611702):
```coq
Ltac pick_freshes_gen L n Y :=
  let Fr := fresh "Fr" in
  let L := beautify_fset L in
  (destruct (var_freshes L n) as [Y Fr]).
```

#### [ Sean Leather (Apr 24 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611708):
Does that introduce `Fr`? It's used by `pick_freshes`.

#### [ Sean Leather (Apr 24 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611730):
Oh, and I think `pick_freshes`/`pick_freshes_gen` might get `L` from the assumptions.

#### [ Sean Leather (Apr 24 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611776):
Via `gather_vars`.

#### [ Sean Leather (Apr 24 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611781):
```coq
Ltac gather_vars :=
  let A := gather_vars_with (fun x : vars => x) in
  let B := gather_vars_with (fun x : var => {{ x }}) in
  let C := gather_vars_with (fun x : env => dom x) in
  let D := gather_vars_with (fun x : trm => trm_fv x) in
  let E := gather_vars_with (fun x : typ => typ_fv x) in
  let F := gather_vars_with (fun x : list typ => typ_fv_list x) in
  let G := gather_vars_with (fun x : env => env_fv x) in
  let H := gather_vars_with (fun x : sch => sch_fv x) in
  constr:(A \u B \u C \u D \u E \u F \u G \u H).
```

#### [ Sean Leather (Apr 24 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611793):
I suppose the `gather_vars` tactic could also be getting something from `K`.

#### [ Sean Leather (Apr 24 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611916):
Right, so `Fr` comes from `pick_freshes` and includes `L` in the free variable finite set.

#### [ Moses Schönfinkel (Apr 24 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611959):
1) `pose` introduces `h := t : T`, a bit like `let` in lean. `poses` is their homebrew thing for transforming the introduced `h` into `h : T` without `t`.

#### [ Sean Leather (Apr 24 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612021):
I think the `K` obligation of `fresh L n Xs` *could* be satisfied by `Fr` by narrowing down the union of finite sets to extract only `L`.

#### [ Sean Leather (Apr 24 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612030):
... the finite set created by `gather_vars`, which scours the assumptions for variables.

#### [ Moses Schönfinkel (Apr 24 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612065):
Wouldn't that require something more magical than what `rewrite*` or `apply*` can do?

#### [ Sean Leather (Apr 24 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612079):
Yes.

#### [ Sean Leather (Apr 24 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612094):
There are other tactics that do that, but, to think of it, they're not being used here, are they?

#### [ Sean Leather (Apr 24 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612101):
Other homemade tactics, I mean.

#### [ Sean Leather (Apr 24 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612106):
So maybe I'm jumping ahead of myself.

#### [ Moses Schönfinkel (Apr 24 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612109):
Right, so here's the thing.

#### [ Moses Schönfinkel (Apr 24 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612151):
```lean
poses Fr' Fr.
rewrite (fresh_length _ _ _  Fr) in WT, Fr'.
rewrite* (@typ_substs_intro Xs). apply* typ_substs_types
```

#### [ Moses Schönfinkel (Apr 24 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612163):
The only non-standard one is `poses` which doesn't do much beyond `pose` (according to its definition).

#### [ Moses Schönfinkel (Apr 24 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612172):
`rewrite(*)` and `apply*` are standard in the sense that they cannot call anything magical.

#### [ Moses Schönfinkel (Apr 24 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612231):
The only remaining tactic is `pick_freshes (length Us) Xs` which can order you a pizza for what we know.

#### [ Sean Leather (Apr 24 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612251):
Well, I have a vague understanding of what `pick_freshes` does. It looks at *all* of the assumptions and picks out all the `vars` it can find, so that it can choose a free variable not in the resultant finite set of `vars`.

#### [ Sean Leather (Apr 24 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612268):
And, if I understand `fresh "Fr"` correctly, `pick_freshes` is creating the assumption `Fr`, which is later used by `poses`.

#### [ Moses Schönfinkel (Apr 24 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612351):
Right. Let's say you have `p : Prop`. `pose p` then introduces `P := p : Prop`. `poses p` also calls `clearbody P` which gives you `p, P : Prop` in the context.

#### [ Sean Leather (Apr 24 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612424):
```coq
rewrite (fresh_length _ _ _  Fr) in WT, Fr'.
```

```coq
Lemma fresh_length : forall xs L n, fresh L n xs -> n = length xs.
```

#### [ Moses Schönfinkel (Apr 24 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612474):
Right, this fully applies `fresh_length` so you have `n = length xs`, you make this rewrite in both `WT` and `Fr'`.

#### [ Sean Leather (Apr 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612482):
```coq
Definition list_for_n (A : Set) (P : A -> Prop) (n : nat) (L : list A) :=
  n = length L /\ list_forall P L.
```

```coq
 Definition types := list_for_n type.
```

#### [ Sean Leather (Apr 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612495):
That's where the rewritten `length` assumptions are used, I believe.

#### [ Sean Leather (Apr 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612499):
That = `types`.

#### [ Sean Leather (Apr 24 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612567):
As in here:

```coq
Lemma typ_substs_intro : forall Xs Us T,
  fresh (typ_fv T \u typ_fv_list Us) (length Xs) Xs ->
  types (length Xs) Us ->
  (typ_open T Us) = typ_substs Xs Us (typ_open_vars T Xs).
```

#### [ Moses Schönfinkel (Apr 24 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612582):
`types` is simple enough then, it's a filtered vector, conceptually

#### [ Moses Schönfinkel (Apr 24 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612705):
`typ_substs_types` however is `_ -> type (typ_substs Xs Us T)`, so there's no way for `apply*` to resolve `types` with it

#### [ Moses Schönfinkel (Apr 24 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612758):
So I was wrong wrt. what the last `apply*` pertains to it seems.

#### [ Sean Leather (Apr 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612814):
Yes, I think so. After `rewrite* (@typ_substs_intro ...)`, you get `type (typ_substs ...)` in the goal.

#### [ Moses Schönfinkel (Apr 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612824):
Right, so that one is magically discharged.

#### [ Sean Leather (Apr 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612829):
... which is fulfilled by `apply* typ_substs_types`

#### [ Sean Leather (Apr 24 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612906):
Are you sure there isn't more magic being done by `rewrite*` and/or `apply*`? Do those use the `Hint`s that are all over the place in this project?

#### [ Sean Leather (Apr 24 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612911):
```shell
$ git grep Hint | wc -l
     204
```

#### [ Sean Leather (Apr 24 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125613182):
@**Moses Schönfinkel** I have to go prepare lunch and feed my kid. Sorry. I'll be back on later. Feel free to leave any insightful and illuminating thoughts here for me to read upon my return. :smile:

#### [ Kevin Buzzard (Apr 24 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125613470):
I'm sure the moderators will have shut this thread down by then ;-)

#### [ Moses Schönfinkel (Apr 24 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125613746):
Can / should I migrate this to a separate stream? @**Kevin Buzzard**

#### [ Moses Schönfinkel (Apr 24 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125613761):
For example `maths` is this completely random topic that few here care about and has its own stream.. errrm :).

#### [ Kevin Buzzard (Apr 24 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125613807):
:-) I have no idea -- as I'm sure you are aware, I was not being remotely serious.

#### [ Moses Schönfinkel (Apr 24 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125613940):
@**Sean Leather** I'll take a closer look when I get home, I have some teaching to do

#### [ Sean Leather (Apr 24 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125615229):
Thanks. Lunch is over. I'll continue looking at it in the meantime, at least until the moderators or Kevin shut me down. If that happens, I'm sure I'll lose my mind, since I will no longer be able to voice my confusion publicly. :poop:

#### [ Sean Leather (Apr 24 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125616072):
Annotated:

```coq
Lemma typ_open_types : forall T Us,
  typ_body (length Us) T ->
```

`Definition typ_body n T := exists L, forall Xs, fresh L n Xs -> type (typ_open_vars T Xs).`


```coq
  types (length Us) Us ->
```

`Definition types := list_for_n type.`

`Definition list_for_n (A : Set) (P : A -> Prop) (n : nat) (L : list A) := n = length L /\ list_forall P L.`

```coq
  type (typ_open T Us).
Proof.
  introv [L K] WT.
```

`L : vars` (a.k.a. `FinSet`)

`K : forall Xs, fresh L n Xs -> type (typ_open_vars T Xs)`

```coq
  pick_freshes (length Us) Xs.
```

Creates an assumption named `Fr` defined as the union of all finite sets of variables in the context for some list. That is, I think `Fr : fresh L (length Us) Xs` because `destruct (var_freshes L n) as [Y Fr]` and `Lemma var_freshes : forall L n, { xs : list var | fresh L n xs }.`

```coq
  poses Fr' Fr.
```

Copies `Fr` to `Fr'`.

```coq
  rewrite (fresh_length _ _ _  Fr) in WT, Fr'.
```

`Lemma fresh_length : forall xs L n, fresh L n xs -> n = length xs.`

```coq
  rewrite* (@typ_substs_intro Xs).
```

`Lemma typ_substs_intro : forall Xs Us T,
  fresh (typ_fv T \u typ_fv_list Us) (length Xs) Xs ->
  types (length Xs) Us ->
  (typ_open T Us) = typ_substs Xs Us (typ_open_vars T Xs).`


```coq
  apply* typ_substs_types.
```

`Lemma typ_substs_types : forall Xs Us T,
  types (length Xs) Us ->
  type T ->
  type (typ_substs Xs Us T).`

```coq
Qed.
```

#### [ Sean Leather (Apr 24 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125616985):
See https://gist.github.com/spl/a204842b476cc46fb1b879ee2baedfbd for an easier-to-read and updated version of the above.

#### [ Sean Leather (Apr 24 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125617573):
Okay, I believe I have a better handle on what's going on.

#### [ Sean Leather (Apr 24 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125617576):
I've found where `L` and `K` are used.

#### [ Sean Leather (Apr 24 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125617617):
There is definitely more magic being applied here than meets the eye.

#### [ Sean Leather (Apr 24 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125617635):
I believe the `fresh` properties are being manipulated into their expected forms using the magic in `Metatheory_Fresh.v`.

#### [ Sean Leather (Apr 24 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125617695):
I couldn't explain the technical mechanism, but I believe it has to do with all the `Hint`s to get certain tactics to perform automagically.

#### [ Sean Leather (Apr 24 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125617702):
In particular, for `fresh`, it's:

```
Metatheory_Fresh.v:Hint Extern 1 (fresh _ _ _) => fresh_solve.
```

#### [ Sean Leather (Apr 24 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125617835):
Also, there's this dark magic underlying `pick_freshes`:

```coq
(** [gather_vars_with F] return the union of all the finite sets
  of variables [F x] where [x] is a variable from the context such that
  [F x] type checks. In other words [x] has to be of the type of the
  argument of [F]. The resulting union of sets does not contain any
  duplicated item. This tactic is an extreme piece of hacking necessary
  because the tactic language does not support a "fold" operation on
  the context. *)
```

#### [ Sean Leather (Apr 24 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125617855):
Used as so:

```coq
Ltac gather_vars :=
  let A := gather_vars_with (fun x : vars => x) in
  let B := gather_vars_with (fun x : var => {{ x }}) in
  let C := gather_vars_with (fun x : env => dom x) in
  let D := gather_vars_with (fun x : trm => trm_fv x) in
  let E := gather_vars_with (fun x : typ => typ_fv x) in
  let F := gather_vars_with (fun x : list typ => typ_fv_list x) in
  let G := gather_vars_with (fun x : env => env_fv x) in
  let H := gather_vars_with (fun x : sch => sch_fv x) in
  constr:(A \u B \u C \u D \u E \u F \u G \u H).
```

#### [ Sean Leather (Apr 24 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125617906):
And (it just clicked for me) that is how `typ_fv` and `typ_fv_list` are appearing.

#### [ Moses Schönfinkel (Apr 25 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125659086):
Sorry I didn't manage to get around to using my computer yesterday! :(

#### [ Sean Leather (Apr 25 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125659347):
I progressed a bit further, as you can see. I'm slightly better at systematically reverse engineering Coq proofs now. Thanks for that! :simple_smile:

#### [ Moses Schönfinkel (Apr 25 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125659582):
What a wonderful world this would be if you could run it :-\.

#### [ Sean Leather (Apr 25 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660053):
I've reverted to working on my Lean version of this proof. I have an idea of how to do the part of the `fresh` manipulation that is implemented with hidden dark magic in Coq, and I'm trying to work it out, in Lean, without magic.

#### [ Moses Schönfinkel (Apr 25 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660224):
You can also try Lean, with magic.

#### [ Sean Leather (Apr 25 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660234):
You mean, by writing tactics? I've avoided that so far, just so I can get a handle on how to do the proofs.

#### [ Moses Schönfinkel (Apr 25 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660331):
Yeah. I'm not entirely sure how useful learning it would be as of right now, given Lean 4 might (will?) change that.

#### [ Sean Leather (Apr 25 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660442):
That unknown future always seems to hang in the air, doesn't it? The possibility of change infects one's thoughts.

#### [ Sean Leather (Apr 25 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660520):
Apparently, Coq has changed a lot over the years, too. This project was supposed to work with 8.1, and now, with 8.8, it just compiles for more hours than I've been willing to wait.

#### [ Kevin Buzzard (Apr 25 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660564):
When mathematicians hear talks about the great things that have been achieved using computer proof checkers

#### [ Kevin Buzzard (Apr 25 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660567):
then the odd order theorem is always mentioned as one of the jewels in the crown

#### [ Kevin Buzzard (Apr 25 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660572):
(before Kepler it was _the_ jewel)

#### [ Kevin Buzzard (Apr 25 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660577):
and apparently that no longer compiles in Coq current

#### [ Kevin Buzzard (Apr 25 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660579):
so I have heard

#### [ Kevin Buzzard (Apr 25 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660584):
if either if you are in a position to formally verify this rumour I'd appreciate it

#### [ Sean Leather (Apr 25 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660643):
https://github.com/math-comp/odd-order is 8 days old. Maybe it's an update.

#### [ Sean Leather (Apr 25 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660693):
Anyway, that's what I got from the first page of a Google search. :simple_smile:

#### [ Johan Commelin (Apr 25 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660745):
Hmm, seems like it's working again.

#### [ Johan Commelin (Apr 25 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660750):
I heard this rumour on the ssreflect mailing list about a year ago

#### [ Johan Commelin (Apr 25 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660751):
Sounded pretty broken back then

#### [ Johan Commelin (Apr 25 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660763):
They were talking about distributing the proof with an old version of Coq inside a docker package. Just to make sure people could easily return to a version that compiles.

#### [ Johan Commelin (Apr 25 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660765):
All the better if it actually compiles with the latest release!

#### [ Sean Leather (Apr 25 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125661171):
```quote
They were talking about distributing the proof with an old version of Coq inside a docker package. Just to make sure people could easily return to a version that compiles.
```
I just discovered https://github.com/proofengineering/coq-docker

#### [ Sean Leather (Apr 25 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125663903):
Et voilà! I just figured out [how to install Coq 8.1](https://github.com/proofengineering/coq-docker/issues/1) and built the Coq project. :hatching_chick:

#### [ Kevin Buzzard (Apr 25 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125664059):
They occasionally prove false in Coq, right? And then of course things get patched. Do the patches extend back as far as things like 8.1? I know that this might all sound trivial to CS people but mathematicians, who are still in my view extremely skeptical about this formal proof verification thing, are not going to be too impressed by "proof of odd order theorem in a system which can also prove anything".

#### [ Kevin Buzzard (Apr 25 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125664078):
https://github.com/clarus/falso

#### [ Kevin Buzzard (Apr 25 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125664079):
8.1 < 8.4.6

#### [ Mario Carneiro (Apr 25 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125664080):
> which can also prove anything

only on tuesdays

#### [ Kevin Buzzard (Apr 25 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125664121):
only if you use a type with 256 constructors

#### [ Sean Leather (Apr 25 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125664193):
For my purpose, I'm just trying to figure out what some Coq proof does and translate that to Lean. So, since we *never* prove false in Lean, there shouldn't be any problem, right?

#### [ Kevin Buzzard (Apr 25 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125664204):
I guess so!

#### [ Sean Leather (Apr 25 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125665013):
Great. I can walk through the proof in CoqIde now. But it doesn't show the magic happening behind the scenes.

#### [ Sean Leather (Apr 25 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125665098):
Oh, but I can remove the `*` from `rewrite*` to see the subgoals. :light_bulb:

#### [ Moses Schönfinkel (Apr 25 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125667062):
@**Kevin Buzzard** Remember you also can't trust that pesky hardware Lean runs on!

#### [ Sean Leather (Apr 25 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125668364):
And... my Coq woes are over! I have successfully translated this particular Coq proof into Lean. :raised_hands:


{% endraw %}
