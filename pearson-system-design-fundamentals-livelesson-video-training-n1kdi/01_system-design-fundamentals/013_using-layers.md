# Using Layers

- **Course:** Pearson System Design Fundamentals Livelesson Video Training
- **Module 1:** System Design Fundamentals
- **Lecture #:** 13
- **URL:** https://www.coursera.org/learn/pearson-system-design-fundamentals-livelesson-video-training-n1kdi/lecture/5I0pK/using-layers
- **Extracted:** 2026-06-20 11:03:03

---

The architecture, as I've learned so far, even for the stock trading system, was fairly loose and hand-wavy in nature. Put it in this box, put it in this box. You can actually be far more structured in it, and here's why. Fortunately, we're not designing houses or jumbo jets or laptops.

We are designing software systems. You can ask yourself the following question, are the typical areas of volatility in software systems? If the answer is yes, you can ask yourself another question, are the typical interaction between these typical areas of volatility? Now imagine you were to recognize those things.

You would bring that to bear on any software design problem you actually find. And as a result, you can actually be far more efficient doing the actual design. So what I'm going to show you now is a template or methodology for the common areas to encapsulate. Think of it as a good starting point for attacking software design.

These encapsulate the classic volatile areas of the system, and I'm also going to give you later on a whole series of runtime behaviors and pattern in the interactions. The approach I'm going to use uses layers. Layers encapsulate top-down, and inside the layers, you have services encapsulating things from each other. So in the abstract, it looks something like this.

You've got like a wedding cake, services, services, services, or layers, layers, layers. And each layer, layers encapsulation. Each layer encapsulates from the top what happens from underneath. And at the very bottom, we have some resources that the services consume.

Now, all cross-layer entities are services, and the reason we like to use services, even though that has nothing to do with the architecture, is because services provide these wonderful aspects of consistency, scalability, security, transaction, and so on.
