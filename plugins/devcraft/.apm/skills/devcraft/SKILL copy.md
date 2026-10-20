---
name: devcraft
description: 
---

## Planning

 - Gain context of the codebase before you implement changes.
 - Consider the impact of the changes on the codebase. 
 - Abstract your view of the implementation plan to a higher level than just the narrow task put forward to you. Consider how future changes to the codebase will build upon your completed solution. 
 - Use object-oriented paradigms to inform your implementation plan. Think about how the models, services, interfaces you're planning to add or change fit into best practices for domain driven design and OOP. 

## Writing Code

 - Keep changes simple and minimal.
 - Write code only for what the task requires. Resist the urge to add fluff and padding.
 - Strive for crisp, elegant minimalism in your implementations. Complex code made simple and written in fewer lines is always better. 
 - Writing simple and minimal code is not mutually exclusive with correctness or completeness. You must still meet all requirements of the task and ensure the solution works.


## Clean Code

### Naming things

 - Use meaningful names for all levels of the codebase including variables, methods, classes, namespaces, directories and project artifacts like project or solution files. 
 - Don't name variables after the domain concept they represent, name them specific to their instance
  - `var customerService = ` over `var service = `
  - `var twitterApiClient = ` over `var client = `
 - Always prefer full and verbose names over abbreviations or acronyms with the exception of established patters such as for loop variables
  - `var customer = ` over `var c = `

### Functions
 
 - A function should perform one coherent operation at a consistent level of abstraction.
 - Separate unrelated actions so callers can invoke one withint invoking the other.
 - Avoid long functions. Functions longer than 30 lines are at risk of being too complex and unmanagable. Long functions usually occur from incremental changes. Consider refactoring if a function has grown too large, even after adding just 1 additional line.
 - Avoid long parameter lists. Represent related inputs with a cohesive domain object or options type.
 - Do not bundle unrelated values into a parameter bag merely to shorten the signature.
 - Shorten functions by creating smaller functions with meaningful and intention revealing names.

## Classes

 - Give classes a single cohesive responsibility.
 - Protect a classes invariants using encapsulation
 - Expose a small public interface suited to callers of the class
 - Put domain rules with the class that owns them rather than making callers navigate object graphs and reconstruct those rules.

### Comments

These rules/guidelines apply to general code comments and not to C# XML comments or similar.

 - Use comments to preserve reasoning, constraints, and contracts that the code alone cannot communicate clearly.
 - Clean code should be self documenting. Comments explaining what the code does are almost never needed. Comments explaining why the code does what it does when this isn't clear from the code itself are acceptable.
 - Explain non-obvious ownership, side effects, units, ordering constraints, algorithms, and protocol requirements where callers or maintainers need them.
 - Keep comments and API documentation consistent with behavior. Update adjacent comments when behavior changes.
 - Do not use comments to excuse a known correctness defect instead of fixing it or explicitly defining the unsupported behavior.

### Exceptions

 - Handle failures at a boundary that can recover. Let failures propagate when a higher boundary owns that responsibility. 
 - Do not catch and handle exceptions simply to log the message. Again, leave this responsibility to a higher boundary
 - Do not swallow a failure, log and ignore it, or replace an unsuccessful operation with a success-like default.

## Code Smells

Avoid these coding anti-patterns and consider small targeted refactors for code you touch during task implementation.

During code review, these code smells should be flagged where they've been introduced or compounded with the changes made.

### Long Parameter Lists

Similar to primitive obsession, make sure a methods parameters are clear and safe to provide.

Long parameter lists are typically where 7 or more input parameters exist on a function or constructor.

The consequence of long parameter lists is a risk to a domain object which has not been encapsulated yet, confusion about parameter position for callers and a risk for incorrect properties to be provided during refactor operations or maintenance. 

### Data Clumps

Repeated groups of values may represent one concept with shared meaning, validation, or behavior. Establish that relationship before introducing a new type.

### Primitive Obsession

Primitive values are appropriate for simple interfaces. Use a domain type when a primitive or group of primitives conceals meaningful constraints, units, identity, or behavior that callers must repeatedly reconstruct.

Do not wrap every string, number, or boolean. Keep primitives when their meaning is obvious, constraints are trivial, and a type would add indirection without improving safety or clarity.