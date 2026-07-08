# span-basis-transforms — Intern Exercises

Two hands-on exercises that teach core linear algebra concepts (**span,
basis, and linear transformations**) as they apply to ML/AI, built entirely
**from scratch in plain Python** — no numpy, no scipy, no external linear
algebra packages of any kind. Every matrix operation, determinant, rank
computation, and transformation is implemented by hand so interns see the
mechanics, not just a library call.

## Summary Document

**Applied Linear Algebra Task Accomplishment**
Approach & Implementation Summary — Span, Basis, and Linear Transformations

📄 [View the full write-up (Google Docs)](https://docs.google.com/document/d/13TJB3aghU3XkdgnYtHwRTWDwi6jbblgE/edit?usp=sharing&ouid=110230718087497543028&rtpof=true&sd=true)

## Structure

```
.
├── src/
│   ├── linalg.py        # from-scratch linear algebra library (vectors, matrices,
│   │                     # determinant, rank/RREF, extended Euclid, transformation
│   │                     # matrix builders)
│   └── secret_box.py     # hidden composite transformation used by Task 2
│                         # (don't open until you've finished the notebook!)
│
├── task1_restricted_robot/
│   └── restricted_robot.ipynb     # Span & Basis
│
└── task2_mystery_black_box/
    └── mystery_black_box.ipynb    # Linear Transformations
```

## Task 1 — The Restricted Robot (Span & Basis)

Per the assignment: a grid-based AI agent restricted to integer multiples of
two move vectors — **Move A** = `(2, 1)` (2 forward, 1 right) and
**Move B** = `(1, -2)` (1 forward, 2 left). Interns determine which cells
are reachable by building up: span (continuous reachability) → basis
(is the move set linearly independent?) → integer lattice + determinant
magnitude (`|det| = 5` here, so only 1 in every 5 grid cells is actually
reachable, despite the move vectors being a full basis of R²) → a raw
`can_reach(target)` solver built on Cramer's rule with exact `Fraction`
arithmetic → visualizations of the reachable lattice.

## Task 2 — The Mystery Black Box (Linear Transformations)

Per the assignment: a black box reports `(1,0) -> (0,1)` and
`(0,1) -> (-1,0)`. Interns exploit the core fact that **a linear map is
fully determined by what it does to the standard basis vectors** — those
two reported outputs *are* the matrix's columns. The deduced matrix turns
out to be an exact 90-degree rotation. From there, interns implement raw
matrix-vector multiplication to verify the deduction on fresh points, then
**compound** the transformation (apply it repeatedly) to observe the
sequential effect: 90° → 180° → 270° → 360° (back to start), and confirm
that `k` repeated applications equals `M^k` computed via `matmul`.

## Getting started

```bash
git clone <this-repo-url>
cd span-basis-transforms
pip install matplotlib   # the only external dependency, used purely for plotting
jupyter notebook
```

Open either notebook under `task1_restricted_robot/` or
`task2_mystery_black_box/` and run the cells top to bottom. Each notebook
is self-contained and imports only `src/linalg.py` (and, for Task 2,
`src/secret_box.py`).

## Why "from scratch"?

The goal isn't to reinvent numpy — it's to make the *definitions* concrete:
what a determinant actually computes, what row-reduction actually does to
find rank, why a basis check is just a linear-independence check, and why
"the columns of a transformation matrix are the images of the basis
vectors" is not a fact to memorize but something you can derive and verify
yourself, one probe at a time.
