# Sprint Planning Meeting

* During this meeting the Product Owner and Development Team will agree to Sprint goals and negotiate which items from the Backlog will be committed to the Sprint Backlog
* **Product Backlog** contains everything we might ever work on, while the **Sprint Backlog** contains just the things we'll work on during one Sprint
* During this meeting, the team will come up with an initial list of tasks necessary to complete the committed PBIs
* According to Agile Project Management with Scrum (Schwaber 2004), only 60% of the tasks are likely to be identified during the Sprint Planning Meeting. Other tasks, such as unanticipated dependencies, will be discovered during Sprint Execution.
* **Sprint Planning Part 1**
   * Committing to Product Backlog Items (PBIs)
* **Sprint Planning Part 2**
   * Coming up with tasks. This is important for multi-team Scrum
* 30 days, or one calendar month is the longest allowable iteration, or Sprint, in Scrum
* In Scrum, teams attempts to build a potentially shippable product increment every Sprint.This requires every Sprint to have of analysis, design, implementation, testing, integration, and even deployment
* During Backlog Refinement, we divided the original epics into smaller user stories, representing thin vertical slices. We'll still have to work together during the Sprint more than traditional team
* A 30-day Sprint uses a 1-day timebox for the Sprint Planning Meeting.
   * How long should the Sprint Planning Meeting be for a two-week Sprint? 4 hours
* If you commit as a team to use Agile engineering practices consistently, you'll eventually be faster from a business perspective. Using craftsmanship to build innovatve product is not about how fast you type code
* The Team is responsible for committing to work in the Sprint Planning Meeting
* A Lean principle behind Scrum is to limit Work In Progress (WIP). Humans don't multitask efficiently. Too much Work in Progress actually slows things down
* How much work has been finished is better measure of progress
* In Sprint Retrospective Meeting we decided team members should wait until the last responsible moment to volunteer for tasks
* One Sprint are planned during a Sprint Planning Meeting. Once the Team has established a consistent velocity, the Product Owner can use this velocity to make longer range forecasts and release plans
* The Product Owner, Scrum Development Team, and Scrum Master must attend the Sprint Planning Meeting
* A Scrum Team attempt to do during its very first Sprint are to analyze, design, build, integrate, and test a potentially shippable product increment, even if its features are initially simple and small

### How can one Scrum team build a potentially shippable product increment within one Sprint?
* By agreeing to a smaller amount of feature scope at the Sprint Planning Meeting, allowing more time for integration, testing, and fixing during each Sprint
* By using modern software engineering approaches such as Test-Driven Development (TDD), continuous design, continuous integration, merciless refactoring
* By improved collaboration techniques
   * Pair programming
   * Working in a team room
   * Eliminating "over the wall" hands off
* By full-time allocation to one team, focusing on only one set of Sprint goals
* By checking code in multiple times per day, and reducing or eliminating branches in the version control system
* By organizing teams around features rather than architectural components

### To avoid technical debt, what should the team write down in their definition of done?
* All previous regression tests pass
* Regression tests for new functionality run automatically with every build
* Code has been written by pairs, or at least reviewed by other team members
* Duplicate code has been removed through refactoring
* Messy and poorly designed code has been cleaned up through refactoring
* Manual, exploratory testing has been conducted
* Checkout and build are fully reproducible, typically with one or two commands

#### Definition of DONE
* Properly tested
* Refactored
* Potentially shippable

### Do you agree the PBI will need some testing tasks?
Yes. If the team learns to use Test Driven Development (TDD), some of this will be handled implicitly and repeatabl. Manual exploratory testing is also important.

## Reference
* [Sprint Planning Meeting](https://www.collab.net/services/training/agile_e-learning#b3)