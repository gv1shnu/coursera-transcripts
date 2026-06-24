# Bruce Schneier - Cryptography, Hashing, and NIST

- **Course:** Intermediate Postgresql
- **Module 3:** Text in PostgreSQL
- **Lecture #:** 25
- **URL:** https://www.coursera.org/learn/intermediate-postgresql/lecture/NR3CH/bruce-schneier-cryptography-hashing-and-nist
- **Extracted:** 2026-06-22 20:28:28

---

[MUSIC] [MUSIC] One of the things we've learned from the Snowden documents is that cryptography, broadly applied, gives the NSA trouble, at least at scale. So the NSA does a lot of cryptanalysis and they break a lot of systems, but well designed, well implemented cryptography does stymie them. And it's important to understand how it does. Because if the NSA wanted to be in my computer, they'd be in my computer.

Done, period. No question about it. They would hack into my computer. And they have a lot of tools to do that.

If they are not in my computer, one of two things are true. One, it's against the law, and the NSA is following the law. And two, I'm not high enough on their priorities list. Now what cryptography does is it forces the attacker, whether the NSA or the Chinese government or cyber criminals or whoever, to have a priorities list.

And depending on their budget, they'll go down the priorities list, and the hope is you're not there, right? You are below their budget line. Without cryptography, an organization like the NSA can bulk collect data on everybody. With cryptography, they are forced to target.

And that's extraordinarily valuable, because it means the FBI will go after the criminals. The NSA will go after the agents of a foreign power. And the Chinese government will go after the US Government officials that rise to whatever level they want to spy on. The cyber criminals will just go after a few of us.

And the rest of us are protected. That makes cryptography a very important tool. Now, cryptography doesn't actually provide any security because cryptography is mathematics. When we say we trust the cryptography, what we're saying is we trust the mathematics and I think there's a lot of reason to say that.

I trust the mathematics. Everything I know about cryptography tells me the mathematics is good. Certainly there will be cryptographic advances, certainly some things will be broken in the future, but by and large, the math works. But math has no agency.

Math can't do anything. It's equations on a piece of paper. In order for math to do something, someone has to take that math and write code and embed that code in a program and embed that program in some bigger system and put that bigger system on a computer with an operating system, on a network with a user. And all of those things add insecurity.

When the NSA breaks cryptography, by and large, they don't break the mathematics. They break something else. They break the implementation, they break the software, they break the network, they break the hardware the software is running on. They do something somewhere else.

And again and again, we learned this lesson, that the math works, but putting stuff around it is much harder. Now there's an important corollary here, that complexity is the worst enemy of security. What these things do is they add complexity. The more complex you make your system, the less secure it's going to be because the more vulnerabilities you'll have, the more mistakes you'll make somewhere in that system.

And we learn again and again when we see analyses of voting systems, embedded systems, your cell phone, messaging systems, email systems, that it's always something around the crypto. Something that the designers, the implementers, the coders, the users, got wrong. And the simpler we can make systems, the more secure they are. So what NIST is doing is they're trying to build standards around as much as possible.

So they have a standard for a crypto algorithm. AES is the standard crypto algorithm. It was a public process where multiple groups submitted algorithms and the community as a whole picked a winner. It wasn't dictated on high.

There weren't secret criteria. The AES algorithm was the one that most of us thought should be AES. Actually, there were several we thought were good candidates. They picked one.

But there's a lot of trust in the process because there's a very public, open international process, right? SHA-3, the new secure hash standard, the same sort of process. Now it's really fun as a cryptographer to be involved in this process. I mean, I think of it is as a great crypto demolition derby.

We all put our algorithms in the ring, beat each other up, the last one left standing wins. It was kind of like that, you know. We would all publish papers analyzing each other and one of the ones left standing won. But that's just such a small part of what NIST does.

They have standards for random number generation, they have standards for key agreement, for different protocols. I mean, trying to standardize these components so the implementers make fewer mistakes. But still there's a lot that you can't standardize and those bigger pieces are where you're going to still find most of your vulnerabilities. I believe that's where the NSA finds most of vulnerabilities, that it's out there.

Recently, we learned about vulnerabilities in the key agreement protocols that are used to secure a lot of the VPNs and Internet connections, right? And if you look at where that vulnerability was, it's because of a shortcut that was made and copied that allowed for a massive pre-computation. The math worked great. If you want to make a standard worse, you make it super complex, and you're just building in vectors at that point.

And this is why the normal IETF process for Internet standards doesn't really work for security because those standards are compromises. Let's put in all the options and make everyone happy. Let's put in much flexibility as necessary to make the system as comprehensive as possible. That is sort of anti-cybersecurity Security needs as few options as possible.

As simple as possible. You don't want compromise. You want one group to win because that group has a self-contained vision. When you have a piece of this and a piece of that and a piece of that, there's going to be some interaction you didn't notice.

And that interaction will be the interaction that breaks your system. You didn't win AES, right? You were in it, you were in the demolition derby with your helmet on. Tell me a little bit about what it's like to be in the demolition derby toward the end and what it's like to sort of not win the demolition derby.

So AES was an interesting process. It started out with 64 algorithms, of which 56 met the submission criteria. Then NIST whittled it down to I think it was 15 or 16 and then the next round whittled it down to five and then chose one. So it's a constant winnowing process.

And Twofish, which was my submission, made it all the way into the top five. And those top five were all good algorithms. I mean, there was no bad algorithms there. And the arguments were more about security margin and implementability in hardware versus embedded systems versus constrained systems, eight-bit, 32-bit.

So we were making distinctions about how we thought it would be used and and to me, it came down to, I think, three algorithms, and I thought these were all good choices. Twofish was one. Rijndael, the eventual winner, was one. And actually, at this point I forget what the third is.

And what I said on my blog at the time is, you know, any of these three are good. And sure, it would been great to have been the winner. But there's a lot of value in NIST picking a non-US algorithm. And by picking an algorithm from Belgium, it said to the world that NIST is picking what they thought was the best and not trying to pick American.

So that was an important consideration I hadn't thought of at the time. So I can't fault NIST in this process it all. It would have been great to win. It actually was really fun to participate.

And, you know, I would do it again. And I participated in the SHA-3 competition, which again was picked by someone else won. My entry was called Skein. And you know these are lots of fun for cryptographers.

Also for students, because they give students a whole bunch of targets. One of the hard things, if you're a crypto student, is you have to break stuff. The only way you learn how to make things is by breaking things. It's back to that security mindset, right?

Anybody can create a security system that he can't break. So if you show up with a security system and say, I can't break this, my first question is, well, who are you? Why should I trust your attestation that you can't break it as something that's meaningful? What else have you broken?

And these competitions give a whole bunch of targets so students can start breaking things that haven't been broken before, get papers out of them, get publications, get cred in the field as someone who can break stuff and therefore, as someone who can design stuff. It's a source of new problems. It's a source of new targets, but this is what I said to start. Security is inherently adversarial, and that adversarial nature makes it different.

Unlike any other field in computer science, you go to a security conference, a crypto conference, and they are going to be papers of people who break each other's stuff and you have to get a thick skin. You have to understand that we are all learning. Now I produce a protocol and you break it, sure, I'm unhappy. But I've learned something, and so have you and so has everyone else.

And that knowledge is more important than my particular creation surviving. And you have to understand that and accept that. And that has to excite you. [MUSIC]
