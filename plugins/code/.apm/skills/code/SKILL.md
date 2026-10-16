---
name: code
description: Apply personal coding preferences when writing, refactoring, or reviewing code.
---

# Code

## Code Style

**Variable Naming:**
Prefer descriptive more verbose variable names over short or abbreviated names.

Bad => `var sc = new ShoppingCart();`
Good => `var shoppingCart = new Customer();`

## Design

 - Unless explicitly instructed, follow industry recognised best coding practices
 - SOLID principals
 - Clean code principals

## Testing

 - Use test-driven development when implementing changes
 - For new code, create a failing test with stub classes/methods first
 - For modifications to existing code. Find the test and modify it first to fail and then pass after your changes are impemented or create a new test which fails initially before implementing changes

## Comments

### Explanatory comments

Add these sparingly to help a reader understand the code where it is not self-explanatory or difficult to read or interpret. Use to document obscure choices or logic that would not be clear without an understanding of the reasoning when the code was implemented. 

Don't add comments for the sake of commenting or where the code should be self-documenting. Adding comments to explain code can be a sign or poorly written code. 

### Documentation comments

Some languages provide rich interfaces for documenting classes and functions etc. Follow the conventions and best practices of the language you're developing in when writing these type of comments. In C# for example, every public class and member should be documented.

## Workflow

 - Write failing tests
 - Implement the feature or change
 - Validate
  - Run tests
  - Run linting
  - Fix build warnings introduced by your code changes
 - Refactor
  - Look for and make improvements to your code. Consider improvements carefully and refactor if needed. Don't refactor for the sake of refactoring.
   - Can you make it easier to read by a human
   - Could it be better organised?
   - Could it be more modular or extensible for future changes?
   - Are the names of classes, interfaces, methods, variables etc appropriate?
