# Getting Real Quantum Computer Properties

- **Course:** Quantum Computing With Qiskit And Advanced Algorithms
- **Module 1:** Qiskit 101
- **Lecture #:** 9
- **URL:** https://www.coursera.org/learn/packt-quantum-computing-with-qiskit-and-advanced-algorithms-wils7/lecture/06Yeh/getting-real-quantum-computer-properties
- **Extracted:** 2026-06-22 15:20:45

---

Hi. Within this lecture, we're going to see how to get the real quantum computer properties and information, so that we can run our circuits on real quantum computers as well. So, it's a little bit detailed, but we're going to do this once, and you can use the same code for your other future circuits, or your other future works as well. So far we have only run this on the simulator, and it will be enough for our actually following lectures as well, but, of course, it's a good idea to know how to run this on a real quantum computer.

So, over here, in the quantum circuit composer, in fact, once we come over here and just do the quantum circuit that we want to do, we can just come back and get the API token that we want. So remember this API token that I've talked about, it's a way to connect your computer to your actual quantum computer, and without the API token, IBM computers won't know that you're requesting that queue or job to be executed, so you need to do that. So what I did was to copy that API token, and save it under a file called ibmapi.txt, in order not to show you my own API key, okay, and I'm going to open a new Python library or Python Notebook over here, and I'm just going to name the simulators and providers. So, I'm doing this in a separate Jupyter Notebook, as you can see, because I want to just give this notes to you in GitHub as well, and it will be available for you once you want to actually execute something on a real quantum machine and you can use the same code for every project that you will use.

So all you got to do is just say, IBMQ.save_account, okay. And over here you need to provide your own API token. You can just copy this from here and paste it with Control V or Command V on Mac, to here. I'm not going to do that, because I don't want you to just see my own API key, rather, I will just read it from the file that I have saved this, but you can just copy and paste the thing over there.

So I have stored it into some file called ibmapi.txt, and it's on the same folder as my simulator's and provider's Jupyter Notebook. So, what I can do, I can just read that file, and just let it take it from there. So again, you don't have to do this, you can just copy and paste API key here directly, but, I'm just going to open this by saying open("ibmapi.txt"), I'm going to say read only, okay. So remember, this is how we read the files, and I will just say read( ).

That's it. So once I execute that, it says that Credentials already present, because I have just run this, executed this command before, on my computer. Now, the Jupyter Notebook will know that I am going to request that thing, request that execution to the IBM Quantum computers with that API key. And, once you do that, you can run IBMQ.load_account, every time you open a new project, since you have said IBMQ.save_account, it shouldn't ask for your API key anymore, so it's very easy actually, you can just do this once, and it will be okay.

So, right now, I'm just going to use the Aer again to get the backends, okay. So, if you say Aer.backends, it will just display you the simulators. And, of course, simulators are very good in order to learn about this, but, if we want to use the real quantum computers, then, we're not going to go with this simulators every time. So as you can see, we have the QasmSimulator, the UnitarySimulator, StatevectorSimulator.

So these are all just simulators, we generally use QasmSimulator, because it gives us all the counts and all the possibilities that we want. For example, in the StatevectorSimulator, you get the results as state vectors like in the matrix form, and, if that's the case, if that's what you want to see, then you can use it, but this time, we're just going to go with the QasmSimulator, not this time, but generally. So, to get the actual quantum machines, all you got to just do is this provider = IBMQ.get_provider("ibm-q"), okay. So this will give you the providers, the real quantum computers that we should work with.

So if you just say provider.backends and hit Shift Enter, you can see all the available quantum machines that you can work on. So, of course, we can see the QasmSimulator here as well, but we can see the other quantum computers like melbourne, or athens, or santiago, or lima, and everything on this list. So, yours might be different from mine, because time to time they just change the real quantum computers. So sometimes they do maintenance, sometimes they do updates.

So, sometimes you cannot see everything that I'm seeing here right now, maybe you see something different, but you can just get the idea, you can just get some alternatives and work with them. But the real question is how to choose the thing over here, right? So, I don't know whether I want to go with the santiago or lima or belem. So if you remember, in the circuit composer, we have a pretty good way to choose them, because we have seen how many qubits they had, and also we have seen how many queues or how many jobs, they're executed, they're being executed on that particular moment.

So, we need to know this stuff, so that we can make an informed decision. So in order to get this stuff with code, we can just use the following. So I'm going to just say, for backend in provider.backends, remember this provider.backends give us a list, so I can just put it on our for loop, right? So, each backend will represent one quantum computer over here, like I'm inside of a list, and inside of that list there are quantum computers.

And I can try to reach the backend.properties in order to see the properties of that particular computer. So, as you can see, once I do that, it doesn't give me anything immediately, because it's being executed, as you can see. So let me try to print that and see if I can get something back. And this * means it's still being executed, okay.

So, we're going to have to wait a little bit for this to complete. And, of course, you can go to circuit composer and say, execute and run or set up and execute, in order to see this information yourselves from the circuit composer as well, but I believe it's a good idea to get this inside of the code as well. So that's why we are seeing this. As you can see, once I did the print(backend.properties), it gives us some properties, but it's in a form of a class inside of the Qiskit, so we need to be much more specific in order to get the properties that we want, because it's actually giving us some gibberish things over here.

So what I'm going to do, I'm going to delete this print over here. Rather than saying only backend.properties, let me go back one more time. I'm going to be much more specific, and I will just say try, because there are Nones over here. If I don't say try, there might be some exception, I can end up with a crash.

And I will get qubit_count, okay. So this will be len, so length of, okay, so this will be len, open the parenthesis, and inside of this parenthesis, you can specify what you want to get. So, I will just say backend.properties, like this, okay, .qubits. So that's it.

This will give us the qubit count. And except, if I don't get 1, then it means that it doesn't have any qubits, or we can just say qubit_count is "simulated". If it doesn't have any qubits, it means that it doesn't, it isn't actually a real quantum machine, it's a simulator. Now I'm just going to print this with a formatted way, open a curly brace over here, and I want to just print out the backend.name, okay, so this will give us the name of that particular computer, like ibmq_athens, ibmq_lima, and, then I will just come over here and hit Shift Enter to see if I get the real names.

Yeah, here you go. I believe we get the names, but not in a very structured way, I just want to get the names of this backend providers and the quantum machines. So I believe we need to open the parentheses over here. So it's not a property, it's a function, yeah, here you go.

Now we only get the names, yeah, great. Now, what I want to do over here is to put, like a colon or like a space, in order to just say, this has that many qubits, okay. So I'm just going to print out the qubit_count over here, so I can see how many qubits they have. So as you can see, the qasm_simulator is simulated, and the other ones, the rest of it has that many qubits.

So qubit_count is very important, because maybe I will create a circuit that has, maybe a 10 cubits, okay. In that case, I can only choose melbourne, for example. So, so far, so good. And, the last thing that we may want to get is the jobs or the queue that it currently has, right, so that we can make an informed decision as well.

So in order to get this, I can just say, come over here and open a new curly brace, and just say, this is another property that we may want to get. It's called backend.status, okay, and again, it's not a property, it's a function. So backend.status( ).pending_jobs. So if I do it like this, it's being executed right now, as you can see, it can take a while to give us that information.

So if you see * on the left hand side, it means that it's being executed, because it's requesting that from the Internet and it's getting back to us, and then it will be displayed to us. But after this, as you can see, now we are getting the pending jobs over here and also the qubit_counts. For example, in this melbourne, we have 142, in armonk we have 37, in lima, we only have 8. For example, lima is very good to go for us right now, it has very low number of pending jobs, and it has 5 qubits.

Since we're going to be using 2 qubits, I believe it's a way to go. And it will be different for you, right? So if you have, like less number of pending jobs, and if you have enough number of qubits over here, like appropriate number would be 2 or more, for you, then, you are good to go with that. Right now I'm going to go with the lima, but you're good to go with any other of these as well.

So, let's do that in the next lecture together.
