---
author: 'Patrick Massot'
category: 'Papers'
date: 2021-08-07 21:42:32 UTC+02:00
description: ''
has_math: true
link: ''
slug: eric-wiesers-scalar-action-paper
tags: ''
title: Eric Wieser's scalar action paper
type: text
---
Eric Wieser wrote a [paper about scalar actions in mathlib](https://easychair.org/publications/preprint/mC9X) for the 
[CICM 2021](https://cicm-conference.org/2021/) conference on intelligent computer
mathematics. 

Scalar actions are everywhere in mathematics. There are so many of
them that a given type can easily get several ones from different origins. For instance
$ℤ$ acts on itself by left multiplication but it also has the $ℤ$ scalar action
that every additive group has, by repeated addition or subtraction.
In general those multiple actions can be proven to be equal, but type class
inference needs definitional equality. So a great deal of care has been taken,
by Eric and others, when setting up the algebraic hierarchy in mathlib. 

The paper tells this fascinating story and is recommended for anyone interested
in multiple inheritance handling in Lean 3 type class system.
