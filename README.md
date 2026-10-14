# Grid-World Q-Learning

An original tabular Q-learning notebook for navigating a 15×15 grid with terminal goal and quicksand states.

Chen Jiang’s Dartmouth graduate coursework.

University: Dartmouth College, Thayer School of Engineering  
Course: ENGS108 Applied Machine Learning, Assignment 5  
Year: Fall 2022  

## Implementation

Grid reward construction, legal state/action enumeration, greedy tie selection, epsilon-greedy exploration, per-episode Q-table learning, trajectory capture and visitation/reward plots.

## Technical approach

The original dictionary of four-action rows is preserved. Legal action identifiers index the current state row; the Bellman target uses the next state and zero future value at terminal transitions.

Episodes reset to the same start and terminate at goals/traps or an explicit cap. Seeded runs retain complete paths, allowing goals, failures and truncation to be counted separately.

## Run

Use Python 3.12: `python3 -m venv .venv`, then `.venv/bin/python -m pip install -r requirements.txt`. Open the original notebook from this directory, or run `.venv/bin/python -B verify_notebook.py` for schema validation, a fresh kernel, HTML/notebook artifacts in `.build/`, and regression tests.

## Checks and results

- All 15 code cells executed from a clean Python 3.12 kernel; four figures were generated.
- Four regression methods passed: legal-action IDs, terminal bootstrap, cap/repeatability and a deterministic small-goal task with invalid configuration cases.
- Seed 2026: 10,000 episodes yielded 9,938 goals, 61 traps and one truncation. Repeat clean-kernel stdout metrics were identical.

## 2026 maintenance

- Corrected boundary action indexing and next-state/terminal bootstrapping.
- Added seed, step cap, finite-table/configuration checks and small-grid-safe reward generation.
- Enabled saved inline plots and separated historical interpretations from measured execution counts.
- Added four deterministic learning regressions, pinned dependencies and a portable notebook verifier.

These changes are 2026 AI-assisted maintenance of the original student implementation.

## Usage notes

- The seed-specific counts are not a universal convergence guarantee.
- The environment is deterministic tabular grid-world, not a simulator or real robot.
- Grid rewards use [x,y] array indexing; heatmap rows correspond to x, rather than a physical Cartesian display.
