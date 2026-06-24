# Julia's Diary

- **Course:** Data Structures
- **Module 4:** Hash Tables
- **Lecture #:** 44
- **URL:** https://www.coursera.org/learn/data-structures/lecture/DvaIb/julias-diary
- **Extracted:** 2026-06-20 21:41:39

---

Hi right in the beginning of this module, I've mentioned, Block Chain and the hype around Bitcoin and other cryptocurrencies are also around the Block Chain itself. And how it can change very different processes that we have currently in place. And I promised you to explain what is it based on. Actually, Block Chain is a very powerful technology, but we can use a simple story to gradually build it from the ground up.

And understand how those natural ideas led to the final solution, which is the Block Chain. And I'm going to use a story and this is going to be a story about Julia's Diary and Julia's Diary will explain to you what the Block Chain is. So at some point Julia started to keep a diary like this. First record had breakfast, second record went for a walk and so on and so forth.

And the record number 239 lent $100 to Daniel and record 240 watched some house of cards and she tried to keep the diary very diligently and to write down everything she did. And if she had an argument with anybody about what she did or did not do, she just took out her diary and pointed her finger to the corresponding record and there was nothing to left to argue about. So at some point Julia had an argument with Daniel regarding whether she gave him $100 or not. She didn't have her diary with her, but she promised to bring it the next day and show him the record which states that she actually lent him 100 dollars.

And in the evening Daniel afraid of having to return $100. He didn't have, he broke into Julia's room while she wasn't there and he forged the diary. He took the line 239 which said initially lend $100 to Daniel and he changed it to Watched Game of Thrones. So the next day Julia returned checked the diary, didn't find any record about lending Daniel $100.

So she apologized before him and forgot about it. 10 years later Daniel decided to confess everything to Julia because he had a lot of remorse and of course he was already able to return her $100 or whatever Julia forget forgave his friend. But she decided to enhance her diary so that it would be harder to forge like this. And she learned that it is possible to use hash functions to make short digest of arbitrary streams.

Just as we learned with you about polynomial family of hash functions that can convert any string into an integer. There are other hash functions like MD5 and for functions like MD5, they have one more useful property that it is extremely hard to find another string with exactly the same hash value. So basically although hash values have collisions for this string, it is extremely hard to find a collision intentionally and this is important to keep the integrity of the diary. So what she decided to do is to add a new column to your diary with the hash value.

And each hash value of each record will include two things first. The hash value of the content of the record. So the hash column at line I plus one will contain in some form hash value of the record itself. And also she's going to concatenate it with the hash value of the previous line.

And after consideration of these two stream to hash again. So the resulting hash contains information both about the current record and about the hash value of the previous record. And actually the hash value of the previous record contains information about everything that was before it and so on. So this is a way to encode a diary in such a way that is really hard to change something in it because if you change something, you have to change everything that was after it.

So this is an example, we assume that we have a special line number 0 with empty records and the harsh value of 0000. Now, if she has first record which is had breakfast and she has some hash function which when applied to this string, had breakfast returns 364 for example. Then we're going to concatenate this 364 with the four zeros from the previous line and we get 3640000. And we take hash of this string and it returns 2308.

And this is the hash value for the line number one. Now to compute the hash value for the line number two, we first take the hash value of the record, went for a walk and let's say hash value is 1782. Now we can culminated with the hash value of the previous line, which is 2308 and we have 17822308. Now we hash this again.

And let's say, we get the value 204, then this will be the hash value of the second line and so on. This can be computed for any existing diary starting from the first line and up to the end. And when you add a new line, you just compute the hash of the contents. You get the hash of the previous line, concatenate them, compute the hash of the result and write it down in the hash column.

So this can be done really quickly when you need to add a new record just around a simple program on your computer and gives you the unique hash value. So this way to forge any particular record in the diary, one would have to also forge all directors after it to fix the hash values. This is already harder and this is already good enough protection for lending small amounts of money to friends. Because either they won't understand that they need to forge more than one line, even if they try to do that or they will spend too much time to do that.

So it looks like it's already good enough. But learn in the next video what happened when Julia decided to actually open a bank and keep records of all the transactions using her diary.
