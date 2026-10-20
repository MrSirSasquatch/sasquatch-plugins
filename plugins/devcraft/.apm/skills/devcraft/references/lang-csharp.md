
# .NET C# (csharp) Coding Guidelines

Additional guidelines specific to C# coding

## Style Guide
 - Avoid multiple classes or class/interface definitions in the same file. Create separate files for all class/interface definitions
 - Effective use of whitespace around code in methods to logically separate related code lines or separate chunks of logic

## XML Comments

 - Add XML for all public classes and methods. Use inheritdoc where the docs should be inherited from a base class or interface
 - Don't write summaries which summarise the usage based on the current task. Write these summaries in a generic sense for the class or method could be called from anywhere.

## Validation and Linting

 - Code changes should be validated by compiling and running unit tests
 - All build warnings introduced by your changes MUST be resolved
 - `dotnet format` can be used to reformat code to adhere to the projects style rules