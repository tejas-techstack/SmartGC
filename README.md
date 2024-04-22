# SmartGC
A smart garbage collector for C.

SmartGC is not exactly a garbage collector, the one main difference is that it does not 
run during the runtime of the code.

SmartGC pre-emptively decides when and where to clear up the memory in a c program.

There are 2 main advantages that SmartGC has over a dedicated GC Engine

	1. It does not cause any overhead, so runtime speeds are not affected at all
	2. It does not require the user to change any existing code, so it can work on any native C program

## How does Smart GC work?

	1. First using a python parser, we parse the ast to determine all the references to any identifier,
	   determine if it was allocated dynamically, and determines the last reference to it in the program
	   and returns the line number. It parses through the entire program as such and returns references, 
	   and its line number in the form of a json.
	2. Then another python script parses the json, determines where to free the memory and injects a free();
	   statement into the existing user code and returns a compilable c program that is now a memory safe 
           code.

## What are future prospects regarding this?
	
	1. The files and inputs have been hardcoded into the parsers, this needs to be changed to a variable input.
	2. Determination of a dynamically allocated pointer is a bit flawed and can cause issues, this 
	   will be resolved in future releases.
	3. As of the current version the references are stored as the variable name itself, which means that 
	   there can be issues regarding the same variable name being used in different scopes. This can be fixed 
	   by hashing the references to avoid clashes.
	4. Storing the line no might not be safe as multiple lines of code can be written in a single line, hence we 
	   we need to determine at which exact location the memory was freed and then clear it.
	5. Edge cases have not yet been tested, references used inside loops have been handled, but there are other 
	   cases, such as static, extern, register variables that may be dynamically allocated, multiple file structures
	   that share memory, and such cases have to be handled in the future.

## How to use SmartGC? 
(assuming that the git repo has been pulled)
	
First libclang dll needs to be installed
(For linux systems)
1. ``` sudo apt install libclang-dev ``` 
(As of 22/04/2024 this should install version 14 of the libclang dll required to run it)
```
pip install clang==14
```
This will install 

	 



