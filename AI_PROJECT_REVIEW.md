# AI Project Review

## Project Summary

An original tabular Q-learning notebook for navigating a 15×15 grid with terminal goal and quicksand states.

Chen Jiang’s original reinforcement-learning exercise, retaining the tabular Bellman update, four movement actions, epsilon-greedy selection and grid reward experiment.

## Original Engineering Strengths

The original notebook makes the Markov decision process concrete: grid coordinates define states, explicit movement rules define legal actions, and the reward grid distinguishes ordinary, goal and trap transitions. The code exposes how those concepts meet in a tabular update.

Trajectories are retained separately from Q-values and displayed through visitation maps. This connects a learned value table to observable paths and gives an understandable way to inspect early and later behavior.

## Technical Highlights

The original dictionary of four-action rows is preserved. Legal action identifiers index the current state row; the Bellman target uses the next state and zero future value at terminal transitions.

Episodes reset to the same start and terminate at goals/traps or an explicit cap. Seeded runs retain complete paths, allowing goals, failures and truncation to be counted separately.

## 2026 Maintenance Improvements

- Corrected boundary action indexing and next-state/terminal bootstrapping.
- Added seed, step cap, finite-table/configuration checks and small-grid-safe reward generation.
- Enabled saved inline plots and separated historical interpretations from measured execution counts.
- Added four deterministic learning regressions, pinned dependencies and a portable notebook verifier.

The changes retain the project's original mechanisms and strengthen their execution
boundaries and verification contract. They do not substitute a new project concept.

## Verification

- All 15 code cells executed from a clean Python 3.12 kernel; four figures were generated.
- Four regression methods passed: legal-action IDs, terminal bootstrap, cap/repeatability and a deterministic small-goal task with invalid configuration cases.
- Seed 2026: 10,000 episodes yielded 9,938 goals, 61 traps and one truncation. Repeat clean-kernel stdout metrics were identical.
- The final visitation/reward figure was visually inspected. Schema validation and portable execution passed. Evidence: RL_before_unit.log, RL_unit_final.log, reinforcement-learning_repeat_execution.json.

Verification is limited to the commands and cases listed above; passing these checks is not a claim of universal correctness.

## Skills Demonstrated

MDP formulation, tabular Bellman updates, legal action/state indexing, epsilon-greedy exploration, terminal transitions, bounded experiments and trajectory-based validation.

## Engineering Assessment

The original exercise exposes the central learning mechanics and makes learned behavior inspectable through paths. The maintained version adds deterministic evidence for boundary and terminal behavior while retaining that educational approach.

## Maintenance Transparency

The original implementation is preserved in `archive/handwritten-original` at
`26df28c57a9e736dc03fe3b0b7535ed150fae5fc`. The reviewed maintained version contains a later AI-assisted engineering
maintenance pass focused on verification, robustness, testing, and documentation
while retaining the original project approach.
