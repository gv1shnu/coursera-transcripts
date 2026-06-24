# Python 3 Assignment Project Structure

- **Course:** Introduction To Concurrent Programming
- **Module 3:** Earn credit towards a degree!
- **Lecture #:** 12
- **URL:** https://www.coursera.org/learn/introduction-to-concurrent-programming/lecture/JJmmL/python-3-assignment-project-structure
- **Extracted:** 2026-06-19 21:36:49

---

Now, we're going to go over the assignment project structure. Let's fire up the assignment in Coursera. Yet again, a lot of the structure, names of files will remain the same from the lab. You'll notice there have been some changes to the code PY file.

The new core object has variables for number of threads, user, name, file, the CLI argument, perse, username in the Coursera assignment part ID. The real user file and test username equality functions are used to verify submitted code, the parse arguments in this case, now part of code PY and not in example, Python file adds arguments for a number of threads, username, and part ID. The structure of the predefined classes and functions that are part of the assignment PY file should not be modified, but the non-login code should be filled out with any functional code that you need to implement a fully working ticketing system. The execute ticketing system participation is a function that is available to any code within the assignment at PY file.

It takes a ticket number, the current assignment part ID and a ticketing system object. It will perform any steps required to have numerous threads execute the critical code in the order that the tickets were pulled. The ticketing system should manage access to tickets to make sure that any number of threads can pull tickets and this is used in connection with the assignment class. Specifically, the managed ticketing system function of the assignment class is used to ensure that all threads execute their code in the order that they pulled tickets from the ticketing system.

The make file shown here is useful for making the assignment that PY file execute correctly. Run, make, clean, build to remove any compiled Python files and install any required Python packages. The last step you'll need to run is make run ARGS equals-N num_threads-U username-P part ID. You'll need to either set the environment variable for num threads, username, part ID, or just replace them in the make command example with values.

You should not need to modify our execute the code directly as there'll be abandoned in VS Code.
