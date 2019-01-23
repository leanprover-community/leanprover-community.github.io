---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/91947namespacedesignissuesvspedagogy.html
---

## Stream: [general](index.html)
### Topic: [namespace design issues vs. pedagogy](91947namespacedesignissuesvspedagogy.html)

---

#### [Kevin Sullivan (Aug 03 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20design%20issues%20vs.%20pedagogy/near/130837483):
The context for the following is an effort to use Lean in teaching a lower-level undergraduate course. Students are easily confused. I'm trying to use namespaces in the usual way so that we can recapitulate the definitions of built-in types, such as bool, without getting name conflicts. It "works", but in the course of figuring out the details, I noted some inconsistencies that I myself found confusing and that students are likely to find confusing, too. I comment the code. The key lines are marked AAA through EEE.

In the outer environment I define a type, bar, with constructors p and q, and open its namespace. This models the built-in type, bool, the namespace of which is open by default. Then I define a namespace, foo. Within foo, I define bar again, in the same way. Everything else occurs within the foo namespace.

Inconsistency #1: In the command "#check bar", on the line marked (AAA), bar is interpreted as referring to foo.bar (as the little equality claim proves); but if you issue the command "open bar" (BBB), bar is interpreted as referring to _root_.bar (so the open command has no effect, as the _root_.bar namespace is already open). The same identifier is thus interpreted in two different ways in the same environment. This is kind of confusing and will be hard to explain to new students in CS.

Inconsistency #2: If you now open foo.bar, then you end up with two definitions of the constructor p. Not unexpectedly, you get error messages flagging an "ambiguous interpretation" in both the command, "#check p", at line (CCC) and in the statement of a simple theorem on line (DDD). Uncomment those two lines to see the error. And yet, when p is used as an argument to a function (line EEE), no ambiguity is flagged; rather it's resolved in favor of foo.bar.p from the inner namespace. So once again the same
identifier is interpreted inconsistently in the same environment. Again, explaining that is p flagged as erroneous when used in the statement of a theorem or in a #check command but not when used as an argument to a function will tend to confuse my students.

Is there a compelling reason for these behaviors? If so, can you briefly explain? If not, perhaps they can be fixed in some near future version?


== the code ==

inductive bar : Type
| p : bar
| q : bar
open bar

#check bar
#check p

namespace foo

inductive bar : Type
| p : bar
| q : bar

#check bar -- bar here refers to foo.bar (AAA)
theorem t1 : bar = foo.bar := rfl
#check p -- as expected, p still refers to _root_.bar.p
theorem t2 : p = _root_.bar.p := rfl

open bar -- bar here refers to _root_.bar! (BBB)

#check bar -- bar still refers to foo.bar
theorem t3 : bar = foo.bar := rfl
#check p -- p still refers to _root_.bar.p
theorem t4 : p = _root_.bar.p := rfl

open foo.bar -- need to use qualified name to open namespace
#check bar -- bar still refers to foo.bar
theorem t5 : bar = foo.bar := rfl 
--#check p     -- p is now ambiguous (CCC)
--theorem t6 : p = _root_.bar.p := rfl    -- p is ambiguous (DDD)

def id(a: bar): bar := a

#check id p -- but in this expression, p is not ambiguous (EEE)

end foo

#### [Johan Commelin (Aug 03 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20design%20issues%20vs.%20pedagogy/near/130837541):
Kevin, you can use three backticks around your code to create a codeblock. If you write "lean" after the first set of backticks you get syntax highlighting! Like so
```
```lean
<your code>
-- nesting backticks is hard... somehow there are 4 backticks below. There should be only 3.
````
```

#### [Kevin Sullivan (Aug 03 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20design%20issues%20vs.%20pedagogy/near/130837550):
```quote
The context for the following is an effort to use Lean in teaching a lower-level undergraduate course. Students are easily confused. I'm trying to use namespaces in the usual way so that we can recapitulate the definitions of built-in types, such as bool, without getting name conflicts. It "works", but in the course of figuring out the details, I noted some inconsistencies that I myself found confusing and that students are likely to find confusing, too. I comment the code. The key lines are marked AAA through EEE.

In the outer environment I define a type, bar, with constructors p and q, and open its namespace. This models the built-in type, bool, the namespace of which is open by default. Then I define a namespace, foo. Within foo, I define bar again, in the same way. Everything else occurs within the foo namespace.

Inconsistency #1: In the command "#check bar", on the line marked (AAA), bar is interpreted as referring to foo.bar (as the little equality claim proves); but if you issue the command "open bar" (BBB), bar is interpreted as referring to _root_.bar (so the open command has no effect, as the _root_.bar namespace is already open). The same identifier is thus interpreted in two different ways in the same environment. This is kind of confusing and will be hard to explain to new students in CS.

Inconsistency #2: If you now open foo.bar, then you end up with two definitions of the constructor p. Not unexpectedly, you get error messages flagging an "ambiguous interpretation" in both the command, "#check p", at line (CCC) and in the statement of a simple theorem on line (DDD). Uncomment those two lines to see the error. And yet, when p is used as an argument to a function (line EEE), no ambiguity is flagged; rather it's resolved in favor of foo.bar.p from the inner namespace. So once again the same
identifier is interpreted inconsistently in the same environment. Again, explaining that is p flagged as erroneous when used in the statement of a theorem or in a #check command but not when used as an argument to a function will tend to confuse my students.

Is there a compelling reason for these behaviors? If so, can you briefly explain? If not, perhaps they can be fixed in some near future version?


== the code ==

inductive bar : Type
| p : bar
| q : bar
open bar

#check bar
#check p

namespace foo

inductive bar : Type
| p : bar
| q : bar

#check bar -- bar here refers to foo.bar (AAA)
theorem t1 : bar = foo.bar := rfl
#check p -- as expected, p still refers to _root_.bar.p
theorem t2 : p = _root_.bar.p := rfl

open bar -- bar here refers to _root_.bar! (BBB)

#check bar -- bar still refers to foo.bar
theorem t3 : bar = foo.bar := rfl
#check p -- p still refers to _root_.bar.p
theorem t4 : p = _root_.bar.p := rfl

open foo.bar -- need to use qualified name to open namespace
#check bar -- bar still refers to foo.bar
theorem t5 : bar = foo.bar := rfl 
--#check p     -- p is now ambiguous (CCC)
--theorem t6 : p = _root_.bar.p := rfl    -- p is ambiguous (DDD)

def id(a: bar): bar := a

#check id p -- but in this expression, p is not ambiguous (EEE)

end foo
```

Ok, I guess in case #2, type inference is resolving the type of p. What about the first inconsistency?

#### [Kevin Sullivan (Aug 03 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20design%20issues%20vs.%20pedagogy/near/130837633):
```quote
Kevin, you can use three backticks around your code to create a codeblock. If you write "lean" after the first set of backticks you get syntax highlighting! Like so
```
```lean
inductive bar : Type
| p : bar
| q : bar
open bar

#check bar
#check p

namespace foo

inductive bar : Type
| p : bar
| q : bar

#check bar -- bar here refers to foo.bar (AAA)
theorem t1 : bar = foo.bar := rfl
#check p -- as expected, p still refers to _root_.bar.p
theorem t2 : p = _root_.bar.p := rfl

open bar -- bar here refers to _root_.bar! (BBB)

#check bar -- bar still refers to foo.bar
theorem t3 : bar = foo.bar := rfl
#check p -- p still refers to _root_.bar.p
theorem t4 : p = _root_.bar.p := rfl

open foo.bar -- need to use qualified name to open namespace
#check bar -- bar still refers to foo.bar
theorem t5 : bar = foo.bar := rfl
--#check p     -- p is now ambiguous (CCC)
--theorem t6 : p = _root_.bar.p := rfl    -- p is ambiguous (DDD)

def id(a: bar): bar := a

#check id p -- but in this expression, p is not ambiguous (EEE)

end foo

#### [Simon Hudon (Aug 03 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20design%20issues%20vs.%20pedagogy/near/130839743):
I think the take away from AAA through CCC is that when you use `open` you must fully qualify the name that you use.

#### [Simon Hudon (Aug 03 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20design%20issues%20vs.%20pedagogy/near/130840086):
This might provide some more helpful details: https://leanprover.github.io/reference/other_commands.html#namespaces

#### [Kevin Buzzard (Aug 03 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20design%20issues%20vs.%20pedagogy/near/130850440):
I completely agree that this is confusing; I ran into this myself when trying to teach mathematicians how to build `nat` with its addition etc. I tried to do everything within a namespace but could never get everything to be as straightforward as I wanted. My solution in the end was to simply give up trying to build `my_namespace.nat` and as you can see at https://xenaproject.wordpress.com/2017/10/31/building-the-non-negative-integers-from-scratch/ I just called them `xnat` instead (x for xena). I was even super-paranoid and made them in a `xena` namespace. Now the trick is to make sure nobody opens `nat` :-) and then I found that my problems had gone away. Within the `xena` namespace I could define things like `add_assoc` and because of this pile of preventative measures I could be fairly confident that nobody would be trying to use the default `add_assoc` later on when proving `add_comm` or whatever for `xnat`. You might want to call my solution a workaround, but I took the practical viewpoint that it wasn't my job to teach people about namespaces -- they were mathematicians. You might be in a different situation of course.

#### [Kevin Buzzard (Aug 03 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20design%20issues%20vs.%20pedagogy/near/130850682):
PS if you start with
```lean
inductive bar : Type 7
| p : bar
| q : bar
open bar

#check bar
#check p

namespace foo

inductive bar : Type 4
| p : bar
| q : bar
```

then it's a little easier to figure out which `bar` is which when you're experimenting ;-)

