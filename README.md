# Grid-World Q-Learning

## Overview

An original tabular Q-learning notebook for navigating a 15×15 grid with terminal goal and quicksand states.

## Original Context

Chen Jiang’s original reinforcement-learning exercise, retaining the tabular Bellman update, four movement actions, epsilon-greedy selection and grid reward experiment. The preserved pre-maintenance snapshot is `26df28c57a9e736dc03fe3b0b7535ed150fae5fc`;
its most recent original commit is dated 2022-11-02. This date describes Git evidence,
not necessarily the complete implementation period.

## What I Implemented

Grid reward construction, legal state/action enumeration, greedy tie selection, epsilon-greedy exploration, per-episode Q-table learning, trajectory capture and visitation/reward plots.

## Technical Approach

The original dictionary of four-action rows is preserved. Legal action identifiers index the current state row; the Bellman target uses the next state and zero future value at terminal transitions.

Episodes reset to the same start and terminate at goals/traps or an explicit cap. Seeded runs retain complete paths, allowing goals, failures and truncation to be counted separately.

## Build / Run

Use Python 3.12: `python3 -m venv .venv`, then `.venv/bin/python -m pip install -r requirements.txt`. Open the original notebook from this directory, or run `.venv/bin/python -B verify_notebook.py` for schema validation, a fresh kernel, HTML/notebook artifacts in `.build/`, and regression tests.

## Testing

- All 15 code cells executed from a clean Python 3.12 kernel; four figures were generated.
- Four regression methods passed: legal-action IDs, terminal bootstrap, cap/repeatability and a deterministic small-goal task with invalid configuration cases.
- Seed 2026: 10,000 episodes yielded 9,938 goals, 61 traps and one truncation. Repeat clean-kernel stdout metrics were identical.
- The final visitation/reward figure was visually inspected. Schema validation and portable execution passed. Evidence: RL_before_unit.log, RL_unit_final.log, reinforcement-learning_repeat_execution.json.

## 2026 Maintenance

- Corrected boundary action indexing and next-state/terminal bootstrapping.
- Added seed, step cap, finite-table/configuration checks and small-grid-safe reward generation.
- Enabled saved inline plots and separated historical interpretations from measured execution counts.
- Added four deterministic learning regressions, pinned dependencies and a portable notebook verifier.

The later work is AI-assisted maintenance, separate from the original implementation.
The exact original snapshot remains on `archive/handwritten-original`.
See [AI_PROJECT_REVIEW.md](AI_PROJECT_REVIEW.md) for a technical review.

## Known Limitations

- The seed-specific counts are not a universal convergence guarantee.
- The environment is deterministic tabular grid-world, not a simulator or real robot.
- Grid rewards use [x,y] array indexing; heatmap rows correspond to x, rather than a physical Cartesian display.
