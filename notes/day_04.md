# Day 4 — Python OOP & Clean Design

## Topics Covered

- Classes and objects
- Instance attributes vs class attributes
- Instance methods
- Class methods
- Static methods
- Composition vs inheritance
- SOLID principles
- Single Responsibility Principle (SRP)

## Classes and Objects

Reviewed how classes define the structure and behavior of objects.

An object contains:
- Data/state through attributes
- Behavior through methods

## Instance vs Class Attributes

Instance attributes belong to individual objects and can have different values for each object.

Class attributes belong to the class and are shared across instances unless overridden.

## Types of Methods

### Instance Method

Uses `self` and works with an individual object's state.

### Class Method

Uses `cls` and works with class-level state. It is defined using `@classmethod`.

### Static Method

Does not require access to instance or class state. It is defined using `@staticmethod`.

## Composition vs Inheritance

Reviewed the difference between:

**Inheritance:**  
An object "is a" type of another object.

**Composition:**  
An object "has a" relationship with another object.

Composition can often make software easier to change because components can be replaced without creating a deep inheritance hierarchy.

## SOLID — SRP

Introduced the Single Responsibility Principle:

> A class should have one primary responsibility and one reason to change.

The goal is to keep responsibilities focused rather than putting unrelated functionality into a single class.

## Practice

Implemented a `BankAccount` class with functionality for:

- Owner
- Balance
- Deposit
- Withdrawal
- Getting the current balance
- Basic validation

## DSA Review

Reviewed previously completed DSA problems rather than adding a new problem.

Problems completed so far:

1. Two Sum
2. Valid Parentheses
3. Contains Duplicate
4. Valid Anagram

## Key Learning

Day 4 helped me strengthen my understanding of Python OOP and start thinking about code organization and maintainability rather than only making code work.

I also learned that composition and focused responsibilities can make code easier to maintain and extend.

## Confidence

**Python OOP:** 3/5  
**Clean Design / SOLID:** 2/5

## Day Reflection

I understand the basic concepts of Python OOP better, especially the difference between instance and class behavior and the different types of methods.

SOLID and clean design are still relatively new to me, so I need more practical examples and coding practice before I become comfortable applying these principles naturally.

## Status

**Day 4 — Complete ✅**
