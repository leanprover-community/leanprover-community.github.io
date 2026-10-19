# Quickstart: The Module System

<style>
main img.diagram {
  /* Each module system svg is at the same absolute scale, so we scale them uniformly */
  --mod-figure-zoom: 0.27489;
  zoom: var(--mod-figure-zoom);
  /* undo the application of the zoom to the margin */
  margin-block: calc(1.5rem / var(--mod-figure-zoom));
  margin-inline: auto;
  display: block;
  max-width: 100%;
  height: auto;
}
main .diagram-group {
  width: fit-content;   /* only as wide as the widest image */
  max-width: 100%;
  margin-inline: auto;  /* center the group */
}
main .diagram-group img.diagram {
  margin-inline: 0;     /* left-align each image inside the group */
}

</style>

The module system provides a means of controlling how information may flow between modules.

Within modules, we can decide if information is `public`, and is thus seen by downstream modules, or if it is `private`, meaning that downstream modules are freed from the burden of loading this information.

Similarly, between modules, we can control whether or not a module's imports will be picked up transitively by downstream imports, via `public import`.

This provides various benefits:

- Cheaper builds: by refusing to load the private data of upstream modules (which would include e.g. large `theorem` proofs), and by pruning long chains of unnecessary transitive imports, we can load less data when building each module, saving on memory and other resources

- Faster rebuilds: changes made exclusively to a module's private data do not trigger rebuilds of downstream modules which import that module, since downstream modules only depend on public data, allowing us to reuse previous builds

- API control: making certain data private allows us to insist that downstream users use the API we want, and do not rely on "accidental" facts of the implementation. Likewise, we do not need to force internal `import` dependencies on downstream files if we only use them privately.

The module system also has us manage what code is available to execute at compile time through the `meta` keyword. This affects `syntax`, `macro`s, tactics, elaborators, attributes, and other compile-time affordances. Most code is not `meta`, and the guarantee that it will not be needed while compiling a file allows us to avoid costs associated with producing and loading the code.

A file is a "module file", i.e. participating in the module system, if and only if it has the `module` keyword at the top. Non-module files are allowed to import module files, but at the cost of loading both public and private information and following all imports transitively, eliminating the benefits of the module system from that point forward. Module files cannot import non-module files.

## Visibility

Each module has a `public` scope and a `private` scope.

<img src="img/module-system/vis-single-module-no-arrow.svg" alt="Two dots labeled 'public' and 'private' enclosed by a capsule-shape labeled 'A'." class="diagram"/>

The information in the `private` scope can use any information from the `public` scope, but the reverse is not true. We use an arrow to show information flowing from one scope to another.

<img src="img/module-system/vis-single-module-with-arrow.svg" alt="Two dots labeled 'public' and 'private' enclosed by a capsule-shape labeled 'A', with an arrow reaching down from the 'public' dot to the 'private' dot." class="diagram"/>

`import A` puts the **public** scope of `A` into the **private** scope of the current module.

<img src="img/module-system/vis-import.svg" alt="A diagram depicting an import by showing two module capsule diagrams A and B, with an arrow from A's public dot to B's private dot." class="diagram"/>

`public import A` puts the **public** scope of `A` into the **public** scope of the current module.

<img src="img/module-system/vis-public-import.svg" alt="A diagram depicting a public import by showing two module capsule diagrams A and B, with an arrow from A's public dot to B's public dot." class="diagram"/>

Note that both of these imports only access the public scope of `A`.

Module `B` receiving `A`'s public scope in its own public scope means that downstream imports of `B` (public or not) will also necessarily receive the public scope of `A` along with the public scope of `B`.

<div class="diagram-group">
<img src="img/module-system/vis-public-import-then-import.svg" alt="A diagram depicting an import following a public import by showing three module capsule diagrams in a row, with an arrow from A's public dot to B's public dot, and an arrow from B's public dot to C's private dot." class="diagram"/>
<img src="img/module-system/vis-public-import-then-public-import.svg" alt="A diagram depicting a public import following a public import by showing three module capsule diagrams in a row, with an arrow from A's public dot to B's public dot, and an arrow from B's public dot to C's public dot." class="diagram"/>
</div>

Information flows through the arrows in these diagrams transitively, meaning we can chain arrows together to infer new, composite arrows. In other words, the arrows in these diagrams may be composed.

As such, chains of public imports form transitive chains of dependencies.

<img src="img/module-system/vis-public-import-chain.svg" alt="A diagram depicting multiple public imports following each other, with arrows from the public dot of one module heading to the public dot of the next, forming a chain." class="diagram"/>

But what if `B` does *not* want to provide `A` to its importers? A non-public `import` "breaks the chain". Observe that `C` loads no data at all from `A`, regardless of whether it uses `import B` or `public import B`. This is how `B` is able to use data from `A` privately without forcing it on downstream consumers such as `C`.

<div class="diagram-group">
<img src="img/module-system/vis-import-then-import.svg" alt="A diagram depicting an import following another import by showing three module capsule diagrams in a row, with an arrow from A's public dot to B's private dot, and an arrow from B's public dot to C's private dot." class="diagram"/>
<img src="img/module-system/vis-import-then-public-import.svg" alt="A diagram depicting a public import following an import by showing three module capsule diagrams in a row, with an arrow from A's public dot to B's private dot, and an arrow from B's public dot to C's public dot." class="diagram"/>
</div>

This also enables us to skip rebuilding `C` when editing `A`. Since the resulting public scope of `B` will not be changed by any changes to `A`, the build of `C` will consider `C`'s dependencies to be up-to-date, and will thus skip building `C` and reuse the previous build results.

It is therefore generally good practice to make imports non-`public` if possible, and to only use `public import` where necessary or to deliberately provide access to API.

Both `public import A` and `import A` provide only `A`'s public scope, but what if you do need something from `A`'s private scope? As an escape hatch, `import all A` will request the private scope of `A` and put it in the target module's private scope.

Because arrows in the following diagram can be followed transitively, the public scope of `A` is *also* available in `B`'s private scope.

<img src="img/module-system/vis-import-all.svg" alt="A diagram depicting an import all by showing two module capsule diagrams A and B, with an arrow from A's private dot to B's private dot." class="diagram"/>

`import all` should be avoided if at all possible; the need for an imported module's private scope is generally a sign that either something is being done wrong in the current module, or that the public scope of the upstream module should be redesigned.

Note that `public import all` is not allowed. The private scope of a module cannot ever be lifted into the public scope through imports.

`public import A` and `import all A` (on separate lines) will import the public scope into the public scope and the private scope into the private scope.

<img src="img/module-system/vis-table-flags.svg" alt="A table of pairs of module capsule diagrams, showing an import (A's public dot connected to B's private dot); a public import (A's public dot connected to B's public dot); an import all (A's private dot connected to B's private dot); and a public import with an import all (A's public dot connected to B's public dot, and likewise for private dots)." class="diagram"/>

### Declarations

An ordinary constant has several pieces of data associated with it:

- `name : Name`
- `type : Expr`
- (optional) `value : Expr`
- (optional) `code : IR`

In some sense "the constant" is simply its name. Its type, value, and so on are merely data _associated_ with the constant.

Each constant has a _visibility_, i.e. which scope it is in (public or private).

The associated pieces of data may have different individual visibilities, and so may behave differently under imports. For example, if the constant is public but some data associated with it is private (say, its `value`), an `import` of the constant's module will only request the public data for the constant, thus completely forfeiting access to that private data.

Further, we may speak of working "at" a given visibility at different points in a module. This specifies which information we have available in the situation at hand (either just the public scope's information or both the public and private scopes' information).

As such, the notion of some information being "in scope" is not generally well-formed, as whether something is "in scope" will change depending on whatever our current working visibility is.

While a constant's current visibility depends on how it is imported (publicly or privately), it also has an _intrinsic_ visibility, namely which scope of its originating module it lives in. A constant may be made intrinsically public by using the `public` keyword (either on the declaration itself, e.g. `public def`, or via `public section`).

Otherwise, declarations are private by default, which encourages being deliberate about designing the public scope. (The `private` keyword is only useful in negating an enclosing `public section`.)

Different pieces of data associated with the constant behave differently with respect to visibility.

**`name`**: The intrinsic visibility is apparent in the `name`, since private constants are subject to mangling, and their name will have an autogenerated prefix like `_private.Foo.Bar.0.myFoo`, where `Foo.Bar` is the original module of a private `def myFoo`. Though the current visibility may be reduced from the intrinsic visibility depending on how the constant is imported, the name of a constant is immutable, and never changes no matter where or how it is imported.

**`type`**: The `type` of a constant always has the same visibility as the constant itself.

**`value`**: The `value` of a constant cannot have a greater visibility than the constant itself (it makes no sense to have a public value for a private constant, for example), but it may have a _lower_ visibility. In particular, the `type` of a constant may be public while the value is private.

In fact, having a private value is the default situation for a `public def`, and the _only_ situation for a `public theorem`. Note that the `value` of a `theorem` is just its proof, and `theorem` proofs are always private, since proof irrelevance means they will never be useful downstream (and so there is no reason to make downstream importers load them).

Recall that ordinary imports (i.e. `import` or `public import`, without `import all`) only import the public scope. As such, when importing a public constant with a private `value`, the `value` data will simply not be loaded downstream, and thus will be completely inaccessible.

#### `@[expose]`

However, `public` definitions may, if we so choose, have public `value`s as well. We may raise the intrinsic visibility of a `public` definition's `value` to `public` by attaching `@[expose]` to the definition. `@[expose]` is meaningless on a private constant, and Lean will reject it.

The main utility for having a `value` available is that it effectively provides Lean with a _rewrite rule_ that lets us _unfold_ the constant to that value during definitional equality checks. E.g., if Lean knows the value of `foo` to be given by `foo := 37`, then Lean may unfold `foo` in order to unify `foo + 1` with `37 + 1`.

Whether this unfolding is possible even in principle depends on whether the `value` data is available at the working visibility of the definitional equality check. As an example, if the `value` data is present but is private (i.e. no `@[expose]`), then Lean could unify `foo + 1` with `37 + 1` within a `public theorem`'s proof (a private location, where it can access private data) but not its type (a public location).

Note how, for a non-`@[expose]`d constant, this yields a significant difference between working in the module it was defined in and working in downstream modules. In the module in which a public non-`@[expose]`d constant is defined, the `value` data is present, but private. Even though it can't be used in public positions, we can still unfold the definition when proving public API theorems (since theorem proofs are private).

However, (ordinary) downstream modules never import the private scope, meaning that they cannot unfold the constant at *any* point, even in principle. The data is simply not there.

(The one exception is if the downstream modules use the discouraged `import all`, which would give them exactly that private data; note, even then, we would still only be able to unfold when working at the private visibility, since `import all` does not lift private data to the public scope.)

As such, `@[expose]` is required for being able to unfold constants downstream.

Note that `abbrev`s and `instance`s are definitions which are `@[expose]`d by default.

It is worth noting that Lean further restricts the unfolding of constants via their *transparency settings*, e.g. `@[reducible]`, `@[implicit_reducible]`, and so on. Transparency settings are subordinate to the module system; thus they are _only_ meaningful when unfolding is already possible. In the typical case, this means they only matter on `@[expose]`d definitions or else when working at private visibilities in the same file.

Technical note: typechecking down in the kernel always behaves as if it is at the private visibility. However, it still cannot unfold declarations whose values are not imported, as that data is not present.

To recap, the visibility of a constant's `value` depends on the kind of declaration creating it:

- `def`: the `value` is private by default, but can be made public via `@[expose]` (only) when the constant is also public
- `theorem`: the `value` is its proof, and is always private
- `abbrev`, `instance`: if public, the `value` is public by default (i.e., these commands attach `@[expose]`). Note: if Lean notices that a given `instance` has a `Prop` type, it will become a `theorem` with a private `value` behind the scenes.

Note that while `@[expose]` and `public` may be attached directly to the declaration, they may also be attached to `section` (e.g. `@[expose] public section`), which simply applies the modifiers to every declaration in the section. Within such sections these modifiers may also be individually negated with `@[no_expose]` and `private`.

## Phase (`meta` vs. runtime)

The `meta` keyword controls what happens to executable code associated with constants. Specifically, a constant's executable code may be either

1. available for execution during the elaboration of the current module, in which case we call it _meta_ code
2. or not, in which case we call it _runtime_ code.

This state ("meta" or "runtime") is called the _phase_ of the code.

Meta code cannot be referenced from runtime code, and vice versa.

Analogously to visibility, a constant's code has an *intrinsic* phase determined when the constant is created, and a *current* phase downstream determined by how it is imported.

By default, a constant's code is intrinsically runtime, unless it is a `meta def`. Many meta-related commands like `syntax`, `macro`, and `elab` necessarily produce `meta def`s behind the scenes without manual intervention, since their code must be executable during elaboration.

An ordinary, non-meta import preserves the phases of all code. Code which is already meta will remain meta and executable. Tactics and macros, for example, may be obtained and used by downstream modules via ordinary non-meta `import`s.

(In these diagrams, we use "IR" interchangeably with "code".)

<img src="img/module-system/phase-simple-non-meta.svg" alt="A pair of modules A and B each with a blue cell labeled 'meta IR' and a red cell labeled 'runtime IR'. A blue arrow leads from A's meta IR to B's meta IR, and a red arrow leads from A's runtime IR to B's runtime IR." class="diagram"/>

`meta import A` _lifts_ all of the runtime code reachable from `A` to the meta phase. That is, intrinsically runtime code from `A` is now in the meta phase in the importing module, and so we can use it in any meta code we write in our current module. Meta code from `A` is still imported under `meta import`, and stays meta.

(Arrow coloration only shows, redundantly, where the arrows end, to emphasize that runtime IR becomes available in the meta phase under `meta import`s.)

<img src="img/module-system/phase-simple-meta.svg" alt="A pair of modules A and B each with a blue cell labeled 'meta IR' and a red cell labeled 'runtime IR'. A blue arrow leads from A's meta IR to B's meta IR, and another blue arrow leads from A's runtime IR to B's meta IR." class="diagram"/>

In fact, having now seen both sorts of imports, we find that a `meta` modifier on an import only changes whether or not runtime IR is lifted to the meta phase, and does nothing else. Perhaps counterintuitively, its presence or absence does not change what happens to `meta` code from the imported module.

`public meta import A` behaves like a `public import` with the same runtime-to-meta phase lifting behavior as a `meta import`, but, due to how public imports chain transitively, will also provide that meta-lifted runtime code to downstream modules which import the current module.

The phase of an import *only* affects the phase of any code that is imported. `meta` import modifiers do not change which type-theoretic constants are imported or at what visibility (the latter of which is still determined by `public`). So, a `public meta import` also functions as a `public import` for the purpose of type-theoretic terms.

### Constants

As has been suggested, constants in Lean, separately from their role as terms in a type theory, are also _compiled_ into code (Lean IR). This code may then be compiled further to C code and then to machine code that runs natively. Or, instead, Lean IR may be executed directly by the Lean interpreter.

It is the interpreter that drives elaboration by executing parsers, elaborators, tactics, and so on. Whenever a constant appears in some piece of code the interpreter is executing, the interpreter must look up the code associated with the constant (preferring native machine code if available), and then execute the code it finds. If it cannot find the code, it errors.

**Meta code** is exactly code which the interpreter is able to successfully locate while elaborating a Lean file.

Since the phase of code specifies when that code must be available, the phase also determines where that code is stored behind the scenes (in order to be accessible downstream) and puts constraints on the phases of that code's references and how they are imported.

Specifically, the laws and constraints around the meta phase must ensure that any constant referenced by meta code will also, in turn, have locatable code, so that the interpreter never errors. I.e., Lean ensures that meta code only ever references meta code. Further, this must remain true downstream, so (as we will see in more detail) any references must be propagated to importers through transitive chains of imports.

Phase *only* pertains to executable code, and the `meta` keyword does not affect any aspects of a constant besides its code.

When a constant is used in executable code, it must have the same phase as the code it is used in.

However, note that the phases of constants used in proofs and types are ignored. This is because proofs and types are erased during compilation, and as such do not appear in the final executable code. Only dependencies which actually affect computation are checked for phase correctness.

Not all constants have code; `theorem`s produce no code, and `noncomputable def`s are permitted to not produce code. (Note: perhaps surprisingly, Lean does still attempt to compile `noncomputable def`s, and just silences failures.) As such, the phases of constants used by a `theorem` in both its type and its proof are ignored, and it may use both meta and runtime constants.

Since it would have no effect, Lean rejects the `meta` keyword on `theorem`s and other declarations that do not produce executable code. (Technical note: certain "code-like" declarations still accept `meta`, such as `structure`, even though they do not have code.)

#### `meta` visibility constraints

By and large, runtime code does not interact with the source constant's visibility. In contrast, any constant with intrinsically meta code has a complicated relationship to visibility which is different from that of runtime code.

Recall that a constant has a `name` (the constant itself), `code` (if computable), and a type-theoretic `type` and `value`. The `code` is produced by compiling the `value`, which turns a term of the type theory into Lean IR.

Despite this relationship between the `value` and `code`, the visibility rules surrounding a constant's meta code do _not_ behave similarly to those surrounding the `value` it was compiled from.

Instead, the `code` of a `public meta def` should be thought of as somehow "public" *itself*. This is because the code of a `public meta def` requires all of its transitive dependencies to both be in the meta phase and come from publicly-imported modules. This is how we ensure the interpreter is always able to find any referenced constant's code in the future, since the `public` import will preserve the availability of the referenced code downstream.

(Recall that, in contrast, whether the actual `value` is public is controlled by `@[expose]`, which has no effect on `code` whatsoever, meta or runtime. Code (both meta and runtime) also has an `@[expose]`-like notion to enable `@[inline]` and similar compilation features that rely on the availability of the code downstream, but this is a little-seen technical detail whose behavior is subject to change in the future, and we do not cover it here.)

Perhaps surprisingly (given our experience with visibility), a `public meta def` is allowed to use private `meta def`s from the same module—as long as _those_ `def`s, in turn, only have dependencies which are meta and come from publicly-imported modules.

This leads to situations such as

```lean4
module

meta import Bar -- privately meta imports `bar`

-- Succeeds
meta def foo := bar

-- Fails, due to `bar` in `foo` not being publicly imported
public meta def fooPublic := foo
```

The above example succeeds if we instead publicly import `bar` via `public meta import Bar`.

As such, the framing of the code from `public meta def`s being "public" doesn't quite work. Instead, we can conceptualize it this way: rather than saying that meta code is "public" or "private", we use the similar terms "presentable", meaning _valid to use downstream_, or "unpresentable".

However, rather than always being *declared* like `public` or `private` is, the presentability of code is _inferred_ on the basis of what the code references. By definition, we say that presentable code may only reference presentable code.

We also say that presentability is only a meaningful property of meta code. We consider all runtime code to just be runtime code.

A private `meta def`'s associated code may be presentable or unpresentable. However, a `public meta def`'s code is _required_ to be presentable. If a `public meta def` uses an unpresentable `meta def`, the compilation of that `public meta def` will error, and the error message will point to the private import which must be upgraded to `public` or `public meta` to make the code presentable.

<img src="img/module-system/phase-single-module-descr.svg" alt="A pair of blocks stacked vertically. The top one is blue and contains two blue dots labeled 'presentable meta IR' and 'unpresentable meta IR'. The bottom one is a red square containing a single red dot labeled 'runtime IR'." class="diagram"/>

Presentable code may be referenced by unpresentable code, but not vice versa.

<img src="img/module-system/phase-single-module-with-arrow.svg" alt="A pair of blocks stacked vertically. The top one is blue and contains two blue dots labeled 'presentable meta IR' and 'unpresentable meta IR'. The bottom one is a red square containing a single red dot labeled 'runtime IR'. A blue arrow goes down from the 'presentable meta IR' dot to the 'unpresentable meta IR' dot." class="diagram"/>

Note that there is no arrow either way between runtime IR and meta IR in the same module, since neither may use the other, as per the runtime/meta phase separation. Phase can only be changed at import boundaries (and only to lift runtime IR to meta IR).

(Technical note: to allow `public meta def`s to use private `meta def`s, the code from private `meta def`s is stored in the public `*.olean` behind the scenes, and their names are recorded in a special public location relevant only to the compiler and interpreter. Their types and values remain private as expected.)

Import visibility modifiers affect presentability analogously to the way they affect scopes: `public (meta) import A` imports all of the presentable code from `A` as presentable code in the target module; a `(meta) import` imports all of the presentable code from `A` as unpresentable.

Note: like visibility, if the same code is provided transitively in different ways from different imports, it has the maximum presentability among all different ways it is provided. For example, if `foo` is imported as unpresentable code due to `import A'` and as presentable code due to `public import A''`, it is presentable.

If code is imported both as runtime code and as meta code, it is available for use in both phases.

In the following diagrams, the arrows mean "(transitively) referenceable in".

As before, these arrows may be composed, and we show composite arrows in a lighter shade.

<img src="img/module-system/phase-table-flags.svg" alt="A table of four diagrams each depicting a pair of modules A and B with their meta and runtime IRs, for import, public import, meta import, and public meta import. In the non-meta import diagrams, a red arrow leads from A's runtime IR dot to B's runtime IR dot; in the meta import diagram, a blue arrow goes from A's runtime IR dot to B's unpresentable meta IR dot, whereas in the public meta import diagram, a blue arrow goes from A's runtime IR dot to B's presentable meta IR dot. In both the meta and non-meta non-public imports, a blue arrow goes from the presentable meta IR dot in A to the unpresentable meta IR dot in B. In both the meta and non-meta public imports, a blue arrow goes from the presentable meta IR dot in A to the presentable meta IR dot in B." class="diagram"/>

Observe that `(public) meta import A` lifts the runtime code from `A` (and its dependencies) to the meta phase, making it presentable or unpresentable depending on whether `public` is or isn't present, respectively. This is what we expect given our earlier discussion of `meta import`s.

However, even though runtime IR can be raised to the meta phase, importing can never lower meta IR down to runtime IR. Code in the meta phase is stuck there forever.

We also see that code which is already intrinsically meta (i.e. marked `meta` in the source file) is indeed still brought in as meta code under ordinary imports, and is unaffected by the presence of `meta` on the `import`.

We can now see that `public meta import`s indeed propagate the ability to interpret lifted runtime IR under non-meta downstream imports. This is why, if `B` in the diagram below defined tactics which used runtime code from `A`, it may be imported normally by `C` without breaking anything.

<img src="img/module-system/phase-public-meta-import-then-import.svg" alt="A public meta import followed by a regular import. We see that the arrows from A's presentable meta IR and A's runtime IR to B's presentable meta IR may be chained with the arrow from B's presentable meta IR to C's unpresentable meta IR." class="diagram"/>

However, `meta import`s break the chain, and runtime IR from `A` privately `meta import`ed by `B` is not loaded as meta IR in `C`.

<img src="img/module-system/phase-meta-import-then-import.svg" alt="A meta import followed by a regular import. We see that the arrows from A's presentable meta IR and A's runtime IR to B's unpresentable meta IR may not be chained with the arrow from B's presentable meta IR to C's unpresentable meta IR." class="diagram"/>
