# Merkle Tree

- **Course:** Data Structures
- **Module 4:** Hash Tables
- **Lecture #:** 47
- **URL:** https://www.coursera.org/learn/data-structures/lecture/sdreX/merkle-tree
- **Extracted:** 2026-06-20 21:42:10

---

Hi. In the previous video, we finally understood the basics of how blockchain works, and also the problem of how to prove to the lenders or to the writers that their transactions are all in the block chain, are in the diary. In this video, I'm going to show you one particular improvement in how this process works. To check that a transaction is recorded in the block, we saw that we need to send the whole chain of transactions inside the block hash values of the records of those transactions and the hash value column of those transactions.

We needed to compute the whole chain of hashes to check that everything is correct to make sure that our particular record is inside the block. It requires big O of n time for n transactions in the block. That can be inefficient if the number of transactions in the block is very big, and it also requires us to send a lot of information through the network to the writers so we need to improve it. Merkle tree is a data structure that allows to reduce this time to logarithmic from linear.

The Merkle tree works like this, in the bottom we have the data blocks transactions, for example, L1, L2, L3, and L4 and in this case we have just four transactions. First, each of the data blocks is hashed and we get these four hashes hash 00, hash 01, hash 10, hash 11. Why they are numbered this way is because the pairs of data blocks are considered together, and then we take the two hashes, hash 00 and hash 01, we concatenate them and compute hash of the concatenated string, and we get hash 0, and then we can get concatenate the hashes of the second pair, we compute the hash of the concatenated string and we get the hash 1, and now we concatenate these hashes again. We compute the hash, and we finally get the top hash of the block.

If we had not four but five transactions, there would be one more block here and it wouldn't have a pair, in this case, we would pair it with another block, which is the copy of itself, and produce one more block here. This one more block will be paired with another copy of itself, and produce one more block here. This block will be already merged with this block, and we will get top hash like this. If there is an odd number of blocks at some level then, the last block is paired with itself and produces a hash from a pair with its copy.

This process, of course, works in linear time, but the process of checking whether a data block is in the block of transactions or not can be done much faster. For example, you are the owner of the data block L2, and you want to check whether this data block is in the block chain block or not. First you can compute the hash of your block and get hash 01. Now, to proceed with the checking, you need to get hash of the paired block hash 00 and so we need to send you this hash 00.

Now you can concatenate your hash with the hash 00 and get hash 0, and you can check it against pair 0, which we can send to you. Now, to compute even more tableau hash, we also need to send you hash 1, the pair of your block. If you get this hash block you can combine these two hashes, concatenate them and get the top hash. If we send you the top hash, you can compare the resulting hash you got against this top hash and finally check that the hashes are equal.

In general, you won't need all the hash values from the block. You will need only one hash value that you don't know from each level of the Merkle tree. On the first level that has n data blocks and the second level that has n/2 data blocks and so on. The number of data blocks is divided by two every time we get one layer up.

The number of layers will be logarithmical, and you will need only one or two hashes from each of the levels to check against the hashes that you can compute yourself. You will need only a logarithmic number of hash values sent to you to check that everything is actually correct. This is a huge win against linear time. This is the diagram, one of the popular diagrams from the Internet of how the block chain works.

You see this chain of blocks which gets appended to the end and then you see that there is this last block that is going to be added to the block chain, and it is built using Merkle tree. The Merkle tree here is a binary tree where it has transactions, these transactions are paired, then they're concatenated to their hashes, and then these are paired, and hash is computed and they are concatenated, and then we get another hash and so on. This is actually how the block chain works in general and practice. Now you know that block chain is just a distributed diary which is very difficult to forge and which is a distributed database into which anyone can write, but it is a competitive process.

Basically, the one who came up with the right nonces first wins and writes his transactions. In case of cryptocurrencies, the system needs someone to mine those nonces, mine those blocks and those people are called miners and they are rewarded for their activity because if they're not rewarded, they won't do that. They are rewarded some money in return for creating needed hashes to add blocks to the block chain. Block chain basically uses hashing heavily to ensure its properties.

It hashes the records, it hashes the contents of the records with the previous hashes to make sure the forgery is too hard. It also uses hashing in the Merkle tree to check that the transaction is indeed in the block. It uses hashing on many steps of the process. Basically the whole protocol is based on the properties of different hash functions.

It also uses binary trees to improve the efficiency operations, Merkle trees and binary tree, and you can learn more about binary trees and efficient separations in binary trees right in the next module of this course. See you there.
