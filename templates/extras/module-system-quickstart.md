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
</style>

The module system provides a means of controlling how information may flow between modules.

Within modules, we can decide if information is `public`, and is thus seen by downstream modules, or if it is `private`, meaning that downstream modules are freed from the burden of loading this information.

Similarly, between modules, we can control whether or not a module's imports will be picked up transitively by downstream imports, via `public import`.

This provides various benefits:

- Cheaper builds: by refusing to load the private data of upstream modules (which would include e.g. large `theorem` proofs), and by pruning long chains of unnecessary transitive imports, we can load less data when building each module, saving on memory and other resources

- Faster rebuilds: changes made exclusively to a module's private data do not trigger rebuilds of downstream modules which import that module, since downstream modules only depend on public data, allowing us to reuse previous builds

- API control: making certain data private allows us to insist that downstream users use the API we want, and do not rely on "accidental" facts of the implementation. Likewise, we do not need to force internal `import` dependencies on downstream files if we only use them privately.


We also must manage what code is available to execute at compile time through the `meta` keyword. This affects `syntax`, `macro`s, tactics, elaborators, attributes, and other compile-time affordances.

A file is a "module file", i.e. participating in the module system, if and only if it has the `module` keyword at the top. Non-module files are allowed to import module files, but at the cost of loading both public and private information and following all imports transitively, eliminating the benefits of the module system from that point forward. Module files cannot import non-module files.

## Visibility

Each module has a `public` scope and a `private` scope.

<img src="img/module-system/vis-single-module-no-arrow.svg" alt="Two dots labeled 'public' and 'private' enclosed by a pill-shape labeled 'A'." class="diagram"/>

The information in the `private` scope can use any information from the `public` scope, but the reverse is not true.

<img src="img/module-system/vis-single-module-with-arrow.svg" alt="Two dots labeled 'public' and 'private' enclosed by a pill-shape labeled 'A', with an arrow reaching down from the 'public' dot to the 'private' dot." class="diagram"/>

`import A` puts the public scope of `A` into the _private_ scope of the current module.

`public import A` puts the public scope of `A` into the _public_ scope of the current module.

This also means that downstream imports of the current module, in receiving the current module's public scope, will also necessarily receive the public scope of `A` along with it.

<img src="img/module-system/vis-import-of-public-import.svg" alt="A diagram depicting an import following a public import by showing three module pill diagrams in a row, with an arrow from A's public dot to B's public dot, and an arrow from B's public dot to C's private dot." class="diagram"/>

(The arrows in these diagrams may be composed.)

Note that a `(public) import` following an `import` forms a "broken chain". Observe that `C` loads no data at all from `A`. This is how `B` is able to use data from `A` privately without forcing it on downstream consumers such as `C`.

<img src="img/module-system/vis-import-of-import.svg" alt="A diagram depicting an import following another import by showing three module pill diagrams in a row, with an arrow from A's public dot to B's private dot, and an arrow from B's public dot to C's private dot." class="diagram"/>

<img src="img/module-system/vis-public-import-of-import.svg" alt="A diagram depicting a public import following an import by showing three module pill diagrams in a row, with an arrow from A's public dot to B's private dot, and an arrow from B's public dot to C's public dot." class="diagram"/>

Typical `import`s, `public` or not, only request the public scope from the upstream module. The upstream private scope stays inaccessible unless you write `import all`, which should generally be avoided. (Even then, the upstream private scope can only be imported into the private scope; private data can never be made public.)

As an escape hatch, `import all A` will request the private scope of `A` as well as the public one, and put it in the target module's private scope. However, note that `public import all` is not allowed: the private scope of `A` cannot ever be lifted into the public scope. `public import A` and `import all A` (on separate lines) will import the public scope into the public scope and the private scope into the private scope.

<img src="img/module-system/vis-table-with-composites.svg" alt="A table of pairs of module pill diagrams, showing an import (A's public dot connected to B's private dot); a public import (A's public dot connected to B's public dot); an import all (A's private dot connected to B's private dot); and a public import with an import all (A's public dot connected to B's public dot, and likewise for private dots)." class="diagram"/>

### Declarations

An ordinary declaration has several pieces of data associated with it:

- `name : Name`
- `type : Expr`
- (optional) `value : Expr`
- (optional) `code : IR`

In some sense "the constant" is simply its name. Its type, value, and so on are merely data _associated_ with the constant.

Each constant has a _visibility_, i.e. which scope it is in (public or private).

The associated pieces of data may have different individual visibilities, and so may behave differently under imports. For example, if the constant is public but some data associated with it is private, an `import` of the constant's module will only request the public data for the constant, thus losing access to that private data.

Further, we may speak of working "at" a given visibility. This specifies which information we have available at that point (either just the public scope's information or both the public and private scopes' information).

While a constant's current visibility depends on how it is imported (publicly or privately), it also has an _intrinsic_ visibility, namely which scope of its originating module it lives in.

Note: this intrinsic visibility is apparent in the `name`: private constants are subject to mangling, and their name will have an autogenerated prefix like `_private.Foo.Bar.0.myFoo`, where `Foo.Bar` is the original module of `private def myFoo`. Though the actual visibility may change depending on how its imported, the name of a constant is immutable, and never changes no matter where or how it is imported.

The `type` of a constant always has the same visibility as the constant itself.

The `value` of a constant cannot have a greater visibility than the constant itself (it makes no sense to have a public value for a private constant, for example), but it may have a _narrower_ visibility. Namely, the `type` of a constant may be public while the value is private.

Having a private value is in fact the default situation for a `public def`, and the _only_ situation for a `public theorem`. (The `value` is the theorem's proof, and proofs are always private.)

When importing a public constant with a private `value` in an ordinary fashion (i.e. without `import all`), the `value` data will simply not be loaded downstream, and thus will be completely inaccessible.

#### `@[expose]`

However, `public` definitions may, if we so choose, have public `value`s as well. We may raise the intrinsic visibility of a `public` definition's `value` to `public` by attaching `@[expose]` to the definition.

Note that when the value of a constant is available at a given visibility, we also have a _rewrite rule_ that lets us _unfold_ the constant to its value during definitional equality checks. When exactly we are allowed to unfold an `@[expose]`d constant is controlled by the definition's transparency settings.

As such, `@[expose]` is required for unfolding. Conversely, without `@[expose]`, unfolding is not possible downstream even in principle under ordinary imports (since the necessary private `value` data is not available). Transparency settings (`@[reducible]`, `@[implicit_reducible` , and so on) are thus _only_ meaningful downstream on `@[expose]`d definitions. Otherwise, they only affect unfolding in private locations in the same file.

Note: even without `@[expose]`, the private `value` data of a definition is still available in the module in which it was created, but only in the private scope. This accordingly means that we may be able to unfold even a non-exposed definition in private locations in the module in which it was defined (such as proof bodies) without being able to unfold it at _any_ point downstream (unless we were to `import all`, which would give us exactly that private data; note, even then, we would still only be able to unfold it in private locations).

`abbrev`s and `instance`s are definitions which are `@[expose]`d by default.

To recap:

- `def`:
    - `type`: same visibility as overall constant
    - `value`: private by default, can be made public (when applicable) via `@[expose]`
- `theorem`:
    - `type`: same visibility as overall constant
    - `value` (i.e. proof): always private

## Phase (`meta` vs. runtime)

The `meta` keyword controls what happens to executable code. Specifically, executable code may be either available for execution during the elaboration of the current module, in which case we call it _meta_ code, or not, in which case we call it _runtime_ code. This state ("meta" or "runtime") is called the _phase_ of the code.

Meta code cannot be used in runtime code, and vice versa.

`meta import A` _lifts_ all of the runtime code reachable from `A` to the meta phase. That is, we are now able to use runtime code from `A` in meta code we write in our current module. (Meta code from `A` stays meta.)

`public meta import A` does the same, but also provides the same meta-lifted runtime code to downstream modules of the current module.

Note that any code from `A` which is _already_ intrinsically marked as meta will still be made available and remain meta under an ordinary import. For example, macros are intrinsically meta, and may be obtained by downstream modules via an ordinary non-meta `import`. I.e., intrinsically meta code is unaffected by `meta import`; the `meta` keyword on imports only lifts the phase of runtime code, and does nothing else.

The `meta` keyword _only_ affects the phase of executable code, and otherwise is ignored. So, a `public meta import` functions as a `public import` for the purpose of type-theoretic terms. As such, a `theorem` (which has no executable code) is totally insensitive to whether its dependencies are meta or runtime (both are accepted).

Because compilation erases proofs and types, this means that the phases of constants used by proofs and types even in definitions which _do_ produce compiled code are ignored when it comes to enforcing the phase distinction.

### Code

Declarations in Lean, separately from their role as terms in a type theory, are also _compiled_ into code (Lean IR), which may then either be compiled further to machine code, or may be executed directly by the Lean interpreter. As such, each constant is also associated to _code_.

A constant's code has a phase, i.e. may be either meta or runtime.

However, note that code has a complicated relationship to visibility. The meta code associated with a constant does _not_ behave similarly to the value of the constant, even though it comes from compiling the value. Instead, the `code` of a `public meta def` should be thought of as somehow "public" itself. (Recall that, in contrast, whether the actual `value` is public is controlled by `@[expose]`.) The code of a `public meta def` requires all of its transitive dependencies to be both meta and have publicly-imported modules.

Though, due to a module being publicly available to itself, a `public meta def` is allowed to use private `meta def`s from the same module—as long as _those_ `def`s, in turn, only have dependencies which are meta and have publicly-available originating modules. This leads to situations such as

```lean4
-- Succeeds
meta def foo := bar -- note: `bar` is privately `meta import`ed

-- Fails, due to `bar` in `foo` not being publicly imported
public meta def fooPublic := foo
```

The above example succeeds if we instead publicly import the module of `bar`.

We can conceptualize it this way: instead of saying that code is "public" or "private", we use the similar terms "presentable", meaning _valid to use downstream_, or "unpresentable".

Instead of being declared like `public` or `private` is, presentability is _inferred_ on the basis of what the code references. Presentable code may only reference presentable code.

Presentability is only a property of meta code; we say all runtime code is just runtime code.

(Note: code (both meta and runtime) also has an `@[expose]`\-like notion for code bodies to enable `@[inline]` and similar compilation features, but this is a little-seen technical detail whose behavior is subject to change in the future, and we do not cover it here.)

A private `meta def`'s associated code may be presentable or unpresentable; a `public meta def`'s code is _required_ to be presentable. If a `public meta def` uses an unpresentable `meta def`, compilation errors, and warns about the import responsible for it being unpresentable.

<img src="img/module-system/phase-single-module-descr.svg" alt="A pair of blocks stacked vertically. The top one is blue and contains two blue dots labelled 'presentable meta IR' and 'unpresentable meta IR'. The bottom one is a red square containing a single red dot labelled 'runtime IR'." class="diagram"/>

Presentable code may be referenced by unpresentable code, but not vice-versa.

<img src="img/module-system/phase-single-module-with-arrow.svg" alt="A pair of blocks stacked vertically. The top one is blue and contains two blue dots labelled 'presentable meta IR' and 'unpresentable meta IR'. The bottom one is a red square containing a single red dot labelled 'runtime IR'. A blue arrow goes down from the 'presentable meta IR' dot to the 'unpresentable meta IR' dot." class="diagram"/>

Presentability behaves analogously to visibility with respect to imports: `public (meta) import A` imports all of the presentable code from `A` as presentable code in the target module; a `(meta) import` imports all of the presentable code from A as unpresentable.

Note: if the same code is provided transitively in different ways from different imports, it has the maximum presentability among all different ways it is provided. For example, if `foo` is imported as unpresentable code due to `import A'` and as presentable code due to `public import A''`, it is presentable.

`(public) meta import A` lifts the runtime code from `A` (and its dependencies) to the meta phase, making it presentable or unpresentable depending on whether `public` is or isn't present, respectively.

Code that is already intrinsically `meta` (i.e. marked meta in the source file) is still brought in as meta code under ordinary imports, and is unaffected by the presence of `meta` on the `import`.

In the following diagram, the arrows mean "(transitively) referenceable in", and coloration only shows (redundantly) where the arrows end, to emphasize that runtime IR becomes available in the meta phase under `meta import`s. (These arrows may be composed.)

<img src="img/module-system/phase-table.svg" class="diagram"/>