# solid-principles
Code level implementation of the SOLID Principles for revision and study purposes.

The SOLID Principles is an acronym of five different design patterns to be applied on the
module level of software applications. Assembled by Robert Cecil Martin, the purpose of its implementation
is to achieve software structures that: "Tolerate change, are easy to understand, and 
are the basis of components that can be used in many software systems." (Martin, 2017)[¹]

Although the principles are directed to the mid-level components, it is important to
understand its implication on the code.
This repository is an attempt to summarize the practical description of this design principles
and to provide Python examples of its implementation. All the information here is based
on (Martin, 2017)[¹] (which the reading is very recommended). In fact, many of the scripts are only Python
implementations of examples provided in the book.

## Single Responsibility Principle (SRP)

SRP states that every module must have one, and only one, reason to change.
In other words, this can be defined as having only one group of stakeholder (actor).

For instance, if functions that concern different teams inside a company are defined inside the same
class, this bounds the actors together. The development team can modify a piece of code shared by both functions due to a
demand that came from one of the actors, the other actor will never know about this change and will continue
using the developed functions even if they do not work in the same way anymore.

Another good result of following the SRP is to decrease the chances of two different merges containing changes on the same
part of code, which can cause a huge headache. However, it is unlikely that you will never face merge conflicts with 
changes made by different branches and developers. If this happens even when following SRP, I would recommend the study
of the [rebase](https://git-scm.com/docs/git-rebase) method on git and that both developers should execute the rebase 
together at 4+ hands :).


[¹] MARTIN, R. C. _Clean Architecture: A Craftsman’s Guide to Software Structure and
Design._ [S.l.]: Prentice Hall, 2017.