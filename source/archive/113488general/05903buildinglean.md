---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/05903buildinglean.html
---

## [general](index.html)
### [building lean](05903buildinglean.html)

#### [Scott Morrison (Apr 04 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20lean/near/124608405):
I've just updated the OS X command line tools, I get a million warnings when trying to build Lean:
````
/Users/scott/projects/lean/lean/src/util/small_object_allocator.h:42:71: warning: 'operator delete' has a non-throwing exception specification but can still throw [-Wexceptions]
inline void operator delete(void *, lean::small_object_allocator &) { lean_unreachable(); }
 ^
/Users/scott/projects/lean/lean/src/util/debug.h:23:156: note: expanded from macro 'lean_unreachable'
#define lean_unreachable() { DEBUG_CODE({lean::notify_assertion_violation(__FILE__, __LINE__, "UNREACHABLE CODE WAS REACHED."); lean::invoke_debugger();}) throw lean::unreachable_reached(); }
 ^
/Users/scott/projects/lean/lean/src/util/small_object_allocator.h:42:13: note: deallocator has a implicit non-throwing exception specification
inline void operator delete(void *, lean::small_object_allocator &) { lean_unreachable(); }
 ^
/Users/scott/projects/lean/lean/src/util/small_object_allocator.h:43:73: warning: 'operator delete[]' has a non-throwing exception specification but can still throw [-Wexceptions]
inline void operator delete[](void *, lean::small_object_allocator &) { lean_unreachable(); }
 ^
/Users/scott/projects/lean/lean/src/util/debug.h:23:156: note: expanded from macro 'lean_unreachable'
#define lean_unreachable() { DEBUG_CODE({lean::notify_assertion_violation(__FILE__, __LINE__, "UNREACHABLE CODE WAS REACHED."); lean::invoke_debugger();}) throw lean::unreachable_reached(); }
 ^ 
````

#### [Scott Morrison (Apr 04 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20lean/near/124608407):
Presumably we want to switch off these warnings?

