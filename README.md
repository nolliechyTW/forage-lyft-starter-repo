# Back-End Engineering Virtual Experience Program
This repository contains the code for the Back-End Engineering Virtual Experience Program from Lyft. The program focused on various aspects of back-end engineering, including software architecture, refactoring, unit testing, and test-driven development.
## Criteria for Car Servicing
Whether or not a Lyft rental car should be serviced depends on two factors at the moment:
- The engine; and
- The battery. </br>

Each of the three types of engines has its own criteria for determining when it should be serviced. The same applies to each type of battery.

The current service criteria are as follows:

|               | Service criteria |
| ------------- | ------------- |
| Capulet Engine  | Once every 30,000 miles  |
| Willoughby Engine  | Once every 60,000 miles | 
| Sternman Engine | Only when the warning indicator is on | 
| Spindler Battery  | Once every 2 years | 
| Nubbin Battery | Once every 4 years | 

	
There are five car models in Lyft’s fleet, each with a different engine-battery combination. These are outlined below:

|Car| Engine |Battery |
| ------------- | ------------- |------------- |
| Calliope  | Capulet Engine  |Spindler Battery |
| Glissade | Willoughby Engine | Spindler Battery |
| Palindrome | Sternman Engine	 | Spindler Battery |
| Rorschach | Willoughby Engine | Nubbin Battery |
| Thovex| Capulet Engine | Nubbin Battery |

These service criteria will change somewhat frequently in the future, and new car models are bound to be added to the fleet. This is an important consideration throughout the program.

With this in mind, it’s very important that the component is extensible and easy to modify, so new service criteria can be added quickly and efficiently.

Tacking this functionality onto the current system would be difficult and messy - instead, you have been instructed to take the time to refactor the codebase prior to making the change. The first step of this process is to draft up a new (clean) system architecture that will allow for the seamless inclusion of the new functionality. Your task is to draft and submit a class diagram that maps out how the system will be reorganized

Engineers at Lyft take an immense amount of pride in their work, so pushing an untested component to production would be unthinkable!
So you need to also write unit tests for each of the battery and engine classes in the codebase.
Here are some important considerations for you to add your unit tests:

- You’ll need to replace the old test suite in the tests folder with your own series of unit tests.
- The old test suite should be broken (since you replaced all the classes it tests in the last step), but it should still serve as a handy template to speed you on your way.
- Note that you need only test concrete implementations of the engine and battery classes for this task. You may ignore testing on everything else.

In the last part, using the same codebase you’ve been working on throughout this program, your task is to add some new functionality.

Throughout this task, you should use a test-driven development workflow - write tests that check for the expected behavior, write code to satisfy those tests, rinse and repeat.

In adding new functionality, you will be making the following two changes:

1. Upgrade Spindler batteries
- First, modify the Spindler battery so it requires service after three years instead of two.
- Notice how easy it is to make this change - you only need to touch one line of code instead of several, and the place where that line of code lives should be immediately obvious.
- Consider what steps would have been required to make this change to the original system architecture, and how much more difficult it would have been, especially if you were new to working on the codebase.
2. Add tire servicing criteria
- There are two types of tires currently in use by the Lyft fleet - Carrigan tires and Octoprime tires.
- The new tire wear sensors produce an array of four numbers between 0 and 1 inclusive, representing how worn each of the tires are.
- This array will be passed to each function in the car factory class, to be used by your tire implementation.
- Carrigan tires should be serviced only when one or more of the values in the tire wear array is greater than or equal to 0.9.
- Octoprime tires should be serviced only when the sum of all values in the tire wear array is greater than or equal to 3.
- Think carefully about the cleanest way to implement the new tire service criteria, then modify the system to complete the change.

## Skills Learned
Throughout this program, I acquired the following skills:

1. Software Architecture: I learned how to design clean and efficient architectures for messy components, ensuring scalability and maintainability. This involved analyzing the existing system, identifying areas for improvement, and proposing a well-structured design.

2. Refactoring: I gained expertise in refactoring code to improve its readability, maintainability, and performance. I learned how to identify code smells, apply appropriate design patterns, and write clean, modular code.

3. Unit Testing: I became proficient in writing unit tests for the codebase, ensuring that individual components and functions work as expected. I learned how to use testing frameworks and techniques to verify the correctness of the code and identify potential bugs or regressions.

4. Object-Oriented Programming(OOP): Contains code examples and implementations showcasing the application of OOP principles. It includes classes, inheritance, and other OOP concepts relevant to the back-end engineering domain.

5. Test-Driven Development (TDD): I practiced the principles of TDD by writing tests before implementing new functionality. This approach helped me in designing clear requirements, improving code quality, and maintaining a robust test suite.

## Acknowledgements
I would like to express my gratitude to Lyft for providing this Back-End Engineering Virtual Experience Program, which has significantly enhanced my skills and knowledge in software architecture, refactoring, unit testing, and test-driven development.
