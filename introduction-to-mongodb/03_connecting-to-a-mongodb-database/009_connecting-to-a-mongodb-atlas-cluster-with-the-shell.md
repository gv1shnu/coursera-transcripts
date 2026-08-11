# Connecting to a MongoDB Atlas Cluster with the Shell

- **Course:** Introduction To Mongodb
- **Module 3:** Connecting to a MongoDB Database
- **Lecture #:** 9
- **URL:** https://www.coursera.org/learn/introduction-to-mongodb/lecture/OHPaE/connecting-to-a-mongodb-atlas-cluster-with-the-shell
- **Extracted:** 2026-08-11 09:52:56

---

Welcome back, team. In this video, you'll learn to connect to your cluster via the MongoDB Shell using your application string. You'll also learn about the Node.js REPL that's used by the MongoDB Shell. To get started connecting to the MongoDB Shell, go ahead and log in to your Atlas account.

Once you've logged in, go ahead and navigate to the database tab. From here, we're going to want to connect to our cluster from our MongoDB Shell. First, go ahead and click on Connect. Then select the first option for connecting to the MongoDB Shell.

This will give us step by step instructions for connecting from the MongoDB Shell as well as the connection string. I'll go ahead and click on I have MongoDB installed because I do. From there, I'll go ahead and highlight and copy this connection string. Additionally, you can feel free to click the Copy button on the right hand side in order to copy this as well.

Once I've copied my connection string, we'll go ahead and switch back to our terminal. Let's go ahead and paste our connection string here. And then press Enter. This will then prompt me for my admin password.

Once I've correctly entered my password, I'll be then connected to my cluster. If you get an error about how the Mongosh command isn't found, you've likely not finished installing it on your machine. Once you've successfully logged in, you're going to get a prompt with several pieces of information. Including the Mongo Shell's log ID, the server that you're connected to, and the versions of MongoDB and the Mongo Shell that you're currently using.

Now that we've successfully connected to the MongoDB Shell, let's examine it in more detail. The MongoDB Shell is a Node.js REPL environment. This gives us access to JavaScript variables, functions, conditionals loops, and control flow statements inside of the shell. Let's go ahead and create a variable for an array of strings.

Here, I've created a greeting array that contains the strings hello, world and welcome. Pressing Enter will allow me to go ahead and store this greeting array as a variable for use for later. Notice that we don't receive any feedback in the shell when we do so. Next, we'll create another variable for a function that will loop over the array and print out each one of the elements.

Here, we've created the loop array variable as an arrow function expression. This function is going to take in an array variable, and for each element in the array, we're going to go ahead and use the for each method to console log each one of the elements. Pressing Enter again stores this loop array variable for later use as well. Now, let's go ahead and use our loop array function with our greeting array as the argument.

Here, I'm passing greeting array as the argument to the loop array method. Running this line allows me to console out each one of the elements within that array. As we can see, we can definitely leverage many of the elements from JavaScript in the Mongo Shell. Let's review what we've accomplished in this video.

First, we located the MongoDB Shell connection string. Then, we connected to the MongoDB Shell by using that connection string. Finally, we use the Node.js REPL environment to create JavaScript expressions within the MongoDB Shell.


<details><summary>Timestamped transcript</summary>

```
Welcome back, team. In this video, you'll learn to connect to your cluster via the MongoDB Shell using your application string. You'll also learn about the Node.js REPL that's used by the MongoDB Shell. To get started connecting to the MongoDB Shell, go ahead and log in to your Atlas account. Once you've logged in, go ahead and navigate to the database tab. From here, we're going to want to connect to our cluster from our MongoDB Shell. First, go ahead and click on Connect.
Then select the first option for connecting to the MongoDB Shell. This will give us step by step instructions for connecting from the MongoDB Shell as well as the connection string. I'll go ahead and click on I have MongoDB installed because I do. From there, I'll go ahead and highlight and copy this connection string. Additionally, you can feel free to click the Copy button on the right hand side in order to copy this as well. Once I've copied my connection string, we'll go ahead and switch back to our terminal. Let's go ahead and paste our connection string here.
And then press Enter. This will then prompt me for my admin password. Once I've correctly entered my password, I'll be then connected to my cluster. If you get an error about how the Mongosh command isn't found, you've likely not finished installing it on your machine. Once you've successfully logged in, you're going to get a prompt with several pieces of information. Including the Mongo Shell's log ID, the server that you're connected to, and the versions of MongoDB and the Mongo Shell that you're currently using. Now that we've successfully connected to the MongoDB Shell, let's examine it in more detail.
The MongoDB Shell is a Node.js REPL environment. This gives us access to JavaScript variables, functions, conditionals loops, and control flow statements inside of the shell. Let's go ahead and create a variable for an array of strings. Here, I've created a greeting array that contains the strings hello, world and welcome. Pressing Enter will allow me to go ahead and store this greeting array as a variable for use for later. Notice that we don't receive any feedback in the shell when we do so. Next, we'll create another variable for a function that will loop over the array and print out each one of the elements.
Here, we've created the loop array variable as an arrow function expression. This function is going to take in an array variable, and for each element in the array, we're going to go ahead and use the for each method to console log each one of the elements. Pressing Enter again stores this loop array variable for later use as well. Now, let's go ahead and use our loop array function with our greeting array as the argument. Here, I'm passing greeting array as the argument to the loop array method. Running this line allows me to console out each one of the elements within that array. As we can see, we can definitely leverage many of the elements from JavaScript in the Mongo Shell.
Let's review what we've accomplished in this video. First, we located the MongoDB Shell connection string. Then, we connected to the MongoDB Shell by using that connection string. Finally, we use the Node.js REPL environment to create JavaScript expressions within the MongoDB Shell.
```

</details>
