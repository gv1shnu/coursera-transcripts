# CompletedWelcome to PostgreSQL!Video

- **Course:** Database Design Postgresql
- **Module 1:** Introduction to SQL
- **Lecture #:** 1
- **URL:** https://www.coursera.org/learn/database-design-postgresql/lecture/kNLrh/welcome-to-postgresql
- **Extracted:** 2026-06-22 20:16:19

---

Hello, and welcome to Postgres for Everybody. This is a course that I have dreamed of teaching for over a decade. You may have met me in another course, like Python for Everybody, Django for Everybody, or Web Applications for Everybody. You'll see in each of those courses, in all those courses, I have to teach SQL.

It turns out I teach basic SQL over and over again. It's like being a kindergarten teacher because I cannot go into the detail that I want because in each of those classes I have another topic to cover. So I have to teach you CRUD, Create, Read, Update, Delete, what's an index, what's a join, what's a foreign key. And then move on into whatever topic that is.

And a lot of you have told me over the years that you like the SQL part of the classes and that you wish that you could program more in SQL. And really, as I build online teaching and learning applications, the SQL part is almost the most creative part. Others are better at designing pretty user interfaces. But for me, the SQL is where the essence of applications and performance comes from.

And so there's just way so much more to learn and it's so much fun to work with. And so this is my moment where I now have a series of courses that can do nothing but databases, teach you as much as I want. I don't have to do anything but databases, and so that's really exciting to me. Now, you might ask why Postgres?

Why PostgreSQL? Here's the little elephant, that's the mascot of Postgres. Good open source projects need mascots. Here's the mascot from my Sakai project, the Sakaiger.

I've got the Postgres mascot and the Sakaiger and a Postgres mascot. So there you go. So why Postgres? I do like open source, but then you might say, why not MySQL?

And I'll just say this. I felt that way too. I used MySQL for a very, very long time. I love open source.

I build a lot of open-source software. The autograder that you're going to take this class, that actually is using MySQL. But here's the thing. It used to be in the beginning, it was easy to know what database was the right one to use.

You might use Oracle if you were in a corporate environment and your company had chosen Oracle. You might use MySQL if you were an open source environment and you insisted on giving folks free stuff. You might have used SQL Server, for example, if you are at an organization that is a Microsoft shop. And so it just seemed like based on sort of where you started, the answer was obvious.

And then a while back, Oracle purchased MySQL. Now they didn't purchase all of MySQL. MySQL is open source, but they purchased enough of the team building it so that Oracle owned the future destiny of MySQL. And so some of us got a little nervous because a lot of us had chosen MySQL just to avoid Oracle.

I don't want to go, I don't want to use Oracle, I don't want to pay every time I like install something. Now, what happened at that point was someone grabbed the open source copy, they made a copy of the open source MySQL and called it MariahDB. And the idea was, as MySQL would continue, then the open source people would keep releasing MariahDB. The problem was that also happened about the time, as we'll see later in Postgres for Everybody, the competitive environment for databases was increasingly challenging.

Challenges from NoSQL storage. The need to store JSON, something that classic relational databases hadn't really thought of much, but it turns out are very, very important. And relational databases sort of saw their grasp on the world slipping away as things like Mongo and Cassandra came out that were NoSQL databases. And so relational databases like SQL and Oracle and Postgres had to react.

And the problem was that MySQL 5 was pre all of this reaction and all this market concern. And so Oracle had to invest in MySQL to make it competitive with all these other products, and they ended up releasing a thing called MySQL 8. And the Mariah database community will have to see the extent to which they have kept up with MySQL 8, I believe it's Mariah 10. If enough of us open source people jump on Mariah, that'll work.

But the problem now is the MariahDB is a change, a small change, for MySQL folks. Maybe Mariah will be the answer. But Oracle, I mean Postgres, has become kind of like this interesting alternative because it's ruggedly, solidly open source. And you may or may not have heard that Amazon, when it first started in the late nineties, chose Oracle.

Why? Because it's what you did if you wanted a fast database and you didn't want to become a database company, which is not what Amazon wanted to become. And so they built a lot of stuff around the Oracle database. Well, the problem is that that cost them a lot of money and as Amazon got bigger and bigger and bigger their Oracle bill got bigger and bigger and bigger.

And that made Larry Ellison, the founder of Oracle, very, very rich. Rich so much to the point where the Iron Man character is based on Larry Ellison. And so Amazon spent a great deal of money to stop using Oracle, but instead use Postgres. And they've done that.

I believe they announced sometime back that there is no more Oracle used inside Amazon and it's all Postgres. And so this whole thing is making a lot of us, open source and otherwise, look at Postgres, and you should be looking at Postgres as well. I have taken a look at Postgres and I'm happy with what I see. The Oracle, the Postgres community is a very, very good open source community.

I'm a big fan. I'm jealous in many ways. They're big, they're talented. They have been doing this for 20 years and it is an advanced SQL database.

It's solid, it scales. Amazon bases its stuff on Postgres, and so it is time, I think, for us to take a really serious look at Postgres. So I'm happy that my first foray into advanced SQL is to introduce you to Postgres. So I hope that you will be as big a fan of Postgres as I am once this course is complete.
