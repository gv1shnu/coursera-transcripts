# C++ Assignment Project Structure

- **Course:** Introduction To Concurrent Programming
- **Module 3:** Earn credit towards a degree!
- **Lecture #:** 15
- **URL:** https://www.coursera.org/learn/introduction-to-concurrent-programming/lecture/MvOC4/c-assignment-project-structure
- **Extracted:** 2026-06-19 21:37:21

---

Now we're going to go over the structure of the project for this C++ assignment. Let's work in the browser. There are two assignment based files that you will need to know about, the assignment.h, the header file for the assignment. It contains a number of static variables and the function signatures for the four most important non-mean functions.

In the right tab is the main source code for the assignment, assignment.cpp. There are four non-mean functions of interest: executeTicketingSystemParticipation, runSimulation, getUsernameFromUserFile, and manageTicketingSystem. The runSimulationFunction executes a run on the assignment simulation based on the previously identified static variables in the header file. Within the run function, the first function that is called is the getUsernameFromUserFile, which retrieves the username value from the that UserFile.

Then based on a number of threads, the executeTicketingSystemParticipation call is executed on detached threads. Then lastly, the manageTicketingSystem manages how those independent threads interact with the ticketing system. Note, the goal of the manageTicketingSystem is to make sure the ticketing system works such that threads execute their work in the order that the tickets that they have pulled from the ticketing system. There are two support files required for the assignment, the first is the Makefile.

It contains the typical build, clean, run and all target. The other is the run.sh, which is very similar to the run.sh for Python 3 assignment, except that the arguments are passed without options or flags.
