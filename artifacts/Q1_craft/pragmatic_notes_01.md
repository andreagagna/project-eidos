# The Pragmatic Programmer - Notes 01

## Preface

### What Makes a Pragmatic Programmer?

**Tip 1.** Care about your craft.

**Tip 2.** Think! About your work.

### Individual Pragmatism, Large Teams

*We who cut mere stones must always be envisioning cathedrals.*

Within the overall structure of a project there is always room for individuality and craftsmanship. One hundred years from now, our engineering may seem as archaic as the techniques used by medieval cathedral builders seem to today's civil engineers, while our craftsmanship will still be honored. 



## A Pragmatic Philosophy

What distinguishes Pragmatic Programmers is an attitude ,a style, a philosophy of approaching problems and their solutions.

Another key to success is that Pragmatic Programmers take responsibility for everything they do.

### Topic 1: It's Your Life

"Why can't you change it?"

Software developer must appear close to the top of any list of career where you have control.

**Tip 3.** You have agency.

### Topic 2: The Cat Ate My Source Code

One of the cornerstone of the pragmatic philosophy is the idea of taking responsibility for yourself and your actions in terms of your career advancement, your learning and education, your project, and your day-to-day work.

Be honest and direct. We must own up to our shortcomings---our ignorance and our mistakes.

#### Team Trust

Your team needs to be able to trust and rely on you.

Trust in a team is absolutely essential for creativity and collaboration.

#### Take Reponsibility

Responsibility is something you actively agree to. In addition to doing your own personal best, you must analyze the situation for risks that are beyond your control. You have the right *not* to take responsibility for an impossible situation, or one in which the risks are too great, or the ethical implications too sketchy.

When you *do* accept the responsibility for an outcome, you should expect to be held accountable for it. When you make a mistake (as we all do) or an error in judgment, admit it honestly and try to offer options.

**Tip 4.** Provide Options, Don't Make Lame Excuses.

Before you approach anyone, stop and listen to yourself.

Run through the conversation in your mind. Before you go and tell them bad news, is there anything else you can try? Sometimes, you just *know* what they are going to say, so save them the trouble.

Instead of excuses, provide options. Explain what *can* be done to salvage the situation. Examples:

- Explain the value of refactoring.
- Need to spend more time prototyping.
- Introduce better testing
- Need additional resources to complete this task.
- Need to spend more time with the users.
- Need to learn some techniques or technology in greater depth.

Don't be afraid to ask, or to admit that you need help.

#### Challenges

- How do you react when someone comes to you with a lame excuse? What do you think of them and their company as a result?
  *Answer*: I feel disappointed and slightly insulted. I feel that, if the company agrees with such behavior, I should probably get to a competitor.
- When you find yourself saying "I don't know" be sure to follow it up with "---but I'll find out."

### Topic 3: Software Entropy

The inexorable increase in *entropy* hits us hard.

When disorder increases in software, we call it "software rot." Some folks might call it by the more optimistic term "technical debt", with the implied notion that they'll pay it back someday. They probably won't.

Many factors can contribute to software rot. The most important one seems to be the psychology, or culture, at work on a project.

Broken window effect. Ignoring a clearly broken situation reinforces the ideas that perhaps *nothing* can be fixed, that no one cares, all is doomed; all negative thoughts which can spread among team members, creating a vicious spiral.

**Tip 5**. Don't Live With Broken Windows.

Don't leave "broken windows" (bad design, wrong decisions, or poor code) unrepaired. Fix each one as soon as it is discovered. If time is insufficient, *board it up*. Take *some* action to prevent further damage and to show that you're on top of the situation. Neglect *accelerates* the rot faster than any other factor.

You may be thinking that no one has the time to go around cleaning up all the broken glass of a project. If so, then you'd better plan on getting a dumpster, or moving to another neighborhood. Don't let entropy win.

#### First, Do No Harm

Don't cause collateral damage just because there's a crisis of some sort. One broken window is one too many.

#### Challenges

- Choose two or three broken windows and discuss with your colleagues what the problems are and what could be done to fix them.
- Can you tell when a window first get broken? What is your reaction? If it was the result of someone else's decision, or a management edict, what can you do about it?
  *Answer*. [To be added]

### Stone Soup and Boiled Frogs

[Stone soup story VS Boiled frog story.]

You may be in the situation where you know exactly what needs doing and how to do it. The entire system just appears before your eyes---you know it's right. But ask permission to tackle the whole thing and you'll be met with delays and blank stares. People will form committees, budgets will need approval, and things will get complicated. Everyone will guard their own resources. "Start-up fatigue."

Work out what you *can* reasonably ask for. Develop it well. Once you've got it, show people, and let them marvel. Then say "of course, it *would* be better if we added..." Pretend it's not important. Sit back and wait for them to start asking you to add the functionality you originally wanted. People find it easier to join an ongoing success. Show them a glimpse of the future and you'll get them to rally around.

**Tip 6.** Be a Catalyst for Change.

#### The Villagers' Side

It is often the accumulation of small things that breaks the morale and teams.

**Tip 7.** Remember the Big Picture.

The [boiled] frog's problem is different from the broken windows issue. In the Broken Window Theory, people lose the will to fight entropy because they perceive that no one else cares. The frog just doesn't notice the change.

Keep an eye on the big picture.

#### Challenges

- Can you determine whether you're making stone soup or frog soup when you try to catalyze change? Is the decision subjective or objective?
  *Answer*. [To be added]
- Exercise in *situational awareness*. Get in the habit of really looking and noticing your surroundings. Do the same for your project.

### Topic 5: Good Enough Software.

"Striving to better, oft we mar what's well", Shakespeare, King Lear 1.4.

Discipline yourself to write software that's good enough---good enough for your users, for future maintainers, for your own peace of mind. More productive and users are happier. Your programs are actually better for their shorter incubation.

"Good enough" does not imply sloppy or poorly produced code. Systems must meet their users' requirements to be successful, and meet basic performance, privacy, and security standards. Users should be given an opportunity to participate in the process of deciding when what you've produced is good enough for their needs.

#### Involve Your Users in the Trade-Off

The scope and quality of the system you produce should be discussed as part of that system's requirements.

**Tip 8.** Make Quality a Requirements Issue.

Many users would rather use software with some rough edges *today* than wait a year for the shiny version.

Give your users something to play with early, their feedback will often lead you to a better eventual solution.

#### Know When To Stop

Don't spoil a perfectly good program by over-embellishment and over-refinement. It may not be perfect. Don't worry: it could never be perfect.

#### Challenges

- Look at the software tools and operating systems that you use regularly. Can you find evidence that these organizations and/or developers are comfortable shipping software they know is not perfect? As a user, would you rather (1) wait for them to get all the bugs out, (2) have complex software and accept some bugs, or (3) opt for simpler software with fewer defects?
  *Answer*: Virtually all the softwares and OSs had bugs. The more complex the software and the least mature the company, the higher the rate. If bugs do not get in the way of activities and use, option (2) is definitely my choice.
- Consider the effect of modularization on the delivery of software. Will it take more or less time to get a tightly coupled monolithic block of software to the required quality compared with a system designed as very loosely coupled modules or microservices? What are the advantages and disadvantages of each approach.
  *Answer*: Loosely couples modules are much more parallelizable once contracts have been established. They also are naturally more flexible and customizable. The advantage of the monolithic software is that it provides the entire UX into a single (hopefully) coherent piece, while loosely coupled modules have to be assembled together via API and contracts.
- Can you think of popular software that suffers from *feature bloat*? That is, software contains far more features that you would ever use, each feature introducing more opportunity for bugs and security vulnerabilities, and making the features you *do* use harder to find and manage. Are you in danger of falling into this trap yourself?
  *Answer*: The old Outlook Desktop version is my stereotypical version of feature bloat. Currently, I am luckily not in a position to build anything that "ornate".

### Topic 6: Your Knowledge Portfolio

"An investment in knowledge always pays the best interest.", Benjamin Franklin.

Your knowledge and experience are your most important day-to-day professional assets.

Unfortunately, they are *expiring assets*. Changing market forces may render your experience obsolete or irrelevant. This can happen pretty quickly.

As the value of your knowledge declines, so does your value to your company or client.

How do you learn *how* to learn, and how do you know *what* to learn?

#### Knowledge Portfolio

Think of all the facts programmers know about computing, the application domains they work in, and all the experiences as their *knowledge portfolio*.

#### Building Your Portfolio

- *Invest regularly*: Even if it's just a small amount. The habit is as important as the sums.
- *Diversify*: The more *different* things you know, the more valuable you are. The more technology you are comfortable with, the better you will be able to adjust to change. Don't forget all the *other* skills you need, including those in non-technical areas.
- *Manage risk*:  Don't put all your technical eggs in one basket.
- *Buy low, sell high*: Learning an emerging technology before it becomes popular can be just as hard as finding an undervalued stock, but the payoff can be just as rewarding.
- *Review and rebalance*.

**Tip 9.** Invest Regularly in Your Knowledge Portfolio.

#### Goals

The best way to go about acquiring intellectual capital with which to fund your portfolio:

- Learn at least one new language every year.
- Read a technical book each month.
- Read nontechnical books, too. Computers are used by *people*, whose needs you are trying to satisfy.
- Take classes.
- Participate in local user groups and meetups.
- Experiment with different environments.
- Stay current.

#### Opportunities for Learning

Time is already in short supply. Plan ahead.

#### Critical Thinking

Thick *critically* about what you read and hear.

**Tip 10.** Critically Analyze What You Read and Hear.

- Ask the "Five Whys".
- Who does this benefit?
- What's the context?
- When or Where would this work? Don't stop with first-order thinking (*what will happen next*) , but use second-order thinking: *what will happen after that?*
- Why is this a problem?

#### Challenges

- Start learning a new language this week.
- Start reading a new book.
- Get out and talk with technology with people who aren't involved in your current project.

### Topic 7: Communicate

A good idea is an orphan without effective communication.

Developers communicate on many levels: spend hours in meetings, work with end users, communicate our intentions to a machine and document our thinking for future generations of developers, write proposals and memos, reports on status, suggest new approaches.

Treat English as just another programming language. Write natural language as you would write code: honor DRY principle, ETC, automation, and so on.

**Tip 11.** English is Just Another Programming Language.

#### Know Your Audience

Understand the needs, interests, and capabilities of your audience.

The trick is to gather feedback. Don't just wait for questions: ask for them. Continuously improve your knowledge of your audience as you communicate.

#### Know What You Want To Say

Plan what you want to say. Write an outline. Then ask yourself, "Does it communicate what I want to express to my audience in a way that works for them?" Refine it until it does.

#### Choose Your Moment

As part of understanding what your audience needs to hear, you need to work out what their priorities are. Make what you're saying relevant in time, as well as in content.

#### Choose a Style

Adjust the style of your delivery to suit your audience.

You are half of the communication transaction.

#### Make It Look Good

Your ideas are important. They deserve a good-looking vehicle to convey them to your audience.

Check the spelling!

#### Involve Your Audience

The documents we produce end up being less important than the process we go through to produce them. Involve your readers with early drafts of your document. Get their feedback, and pick their brains.

#### Be a Listener

There's one technique that you must use if you want people to listen to you: *listen to them*.

Encourage people to talk by asking questions. Turn every meeting into a dialog, and you'll make your point more effectively.

#### Get Back To People

Always respond to emails and voicemails, even if the response is simply "I'll get back to you later". Keeping people informed makes them far more forgiving of the occasional slip, and makes them feel that you haven't forgotten them.

**Tip 12.** It is Both What You Say and the Way You Say It.

#### Documentation

Pragmatic Programmers embrace documentation as an integral part of the overall development process. Writing documentation can be made easier by not duplicating effort or wasting time, and by keeping documentation close at hand---in the code itself. We want to apply *all* of our pragmatic principles to documentation as well as code.

**Tip 13.** Build Documentation In, Don't Bolt It On.

It's easy to produce good-looking documentation from the comments in the source code.

Restrict your non-API commenting to discussing why something is done, its purpose and its goal. The code already shows *how* it is done, commenting on this is redundant---and is a violation of the DRY principle.

Commenting source code gives you the perfect opportunity to document those elusive bits of a project that can't be documented anywhere else: engineering trade-offs, why decisions were made, what other alternatives were discarded, and so on.

#### Challenges

- Good books that contain sections on communications within teams: *The Mythical Man-Month: Essays on Software Engineering* and *Peopleware: Productive Projects and Teams*. In addition, *Dinosaur Brains: Dealing with All Those Impossible People at Work* discusses the emotional baggage we all bring to the work environment.
- The next time you have to give a presentation, or write a memo advocating some position, try working through the advice in this section before you start. Explicitly identify the audience and what you need to communicate. If appropriate, talk to your audience afterwards and see how accurate your assessment of their needs was.