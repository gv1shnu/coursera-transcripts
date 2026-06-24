# Blockchain

- **Course:** Data Structures
- **Module 4:** Hash Tables
- **Lecture #:** 46
- **URL:** https://www.coursera.org/learn/data-structures/lecture/EYerK/blockchain
- **Extracted:** 2026-06-20 21:42:00

---

Hi. After learning the story of Julia's Diary and Julia's Bank, we can actually understand the basics of how BlockChain works and more importantly, why does it work that way? So if you are actually keeping a bank, you need to not only make all the records about who borrowed wasn't who played back what. You also need to sometimes prove to your lenders that they did borrow something, and they did pay back something, and they need to make sure that you really kept all their transactions.

Not only the ones where they borrowed some money, but also the ones where they paid you back some money; so you need to prove to the lenders that every transaction is recorded and it is both inefficient and insecure to show them the whole diary or a whole page of the diary just to check that their particular transaction is recorded in the diary, because there could be other transactions on the same page and those other people, maybe they don't want their transactions to be seen by any other people. Also it is inefficient to show a whole page to just check one transaction. What can we do with that? Actually, we can use the same idea that works against forgery, instead of showing the diary itself in the records itself, show just the hashes of records and the hash value column basically.

You can mark the number of the record which should contain the lenders transaction. He knows exactly what is the text of his transaction; so they can compute the hash of his own transaction. Given the hashes of all the other transactions, he can check the chain rule that, if we get the hash of the previous column and the hash of the record in the second column, and you concatenate it that you get the hash value column of the second line and so on. He can find his record among those records; and if everything checks up with the hashes of the records and the hash value columns, then it means that his transactions is indeed in the diary or someone very powerful forged this transaction, but this is so hard to do that it is not economically viable for anyone, including the bank itself to forge this record.

Basically any lender given only the hashes of the records and the hash value column, check whether that transaction is in or not; so to do that, he just computes the chain of hashing and concatenation and hashing in for each line in the diary. Actually to avoid sending each lender hashes of the whole diary to check just one transaction, we can separate the whole dire into blocks of transactions corresponding to pages in a real physical diary. So just each lender can just check that his transaction is in a particular block. Maybe he can separately check that particular block is also in the whole diary.

We can group transactions by hundreds in one block and then check separately that the transaction is in the block and then the block isn't the direct because the amount of blocks will be 100 times smaller than the amount of transactions. It can be already feasible to send all the hashes of the blocks and not just all the hashes of all the transactions. This represents our diary as a chain of blocks, or a BlockChain, and that's the name. This is basically how BlockChain works, it groups all the transactions that need to be recorded in the distributed database, which is a diary and Julia's diary or everyone's diary of every transaction.

Actually those that have to be money transactions though, those can be any transactions. This is basically just a big diary where everybody can write to, this diary and everybody can make sure that their transaction is in. There are some rules on who writes a block when there is a conflict between two different writers who want to add their own block to the end of the diary. Those rules uniquely determine which version of the diary wins.

To actually write down and to make some transaction, you need to use some computing power. Typically, it becomes more and more hard to add new blocks to the end of the diary; because more and more people try to write their blocks to the end of the diary and system adjusts itself in such a way that approximately a one block in every 10 minutes is added to the end of the diary for example, in the case of Bitcoin, did this 10 minutes. Example could be different for other BlockChain implementations. But in general, typically there is some amount of time that is on average for adding one block.

This is capped by increasing or decreasing the difficulty of creating a block and adding it to the end by the system itself. Its difficulty, is of course controlled by the number of zeros under the hash that you need to have in the hash column or maybe those zeros could be not decimal but binary zeros, but those are all just details. You control the difficulty of creating a new block and made it so that on average, every block is added once in 10 minutes. BlockChain sense just diary, which is very hard to forge, and everybody can write to it only competitive basis, and everybody can check whether the transaction is in the diary or not.

Also there are some optimizations on top of what I've just told you. I'll tell you one of the interesting optimization in the next video.
