# Python Decorators Examples

This repository contains a collection of Python decorator implementations, demonstrating both basic and advanced use cases of decorators in Python.

## Overview

The project is structured to showcase different types of decorators, from simple function modifications to complex behavioral patterns.

### Basic Decorators

1. **Basic Decorator Structure** 
   - Location: `decorators/basic/basic_decorator.py`
   - Demonstrates the fundamental structure of Python decorators
   - Shows a simple greeting implementation

2. **Logging Decorator**
   - Location: `decorators/basic/logging_decorator.py`
   - Tracks function calls, arguments, and return values
   - Useful for debugging and monitoring function execution

3. **Greeting Decorator**
   - Location: `decorators/basic/greeting_decorator.py`
   - Demonstrates string manipulation and function wrapping
   - Adds a greeting message to function returns

4. **Timing Decorator**
   - Location: `decorators/basic/timing_decorator.py`
   - Measures function execution time
   - Useful for performance monitoring and optimization

### Advanced Decorators

1. **Retry Decorator**
   - Location: `decorators/advanced/retry_decorator.py`
   - Implements automatic retry logic for failed operations
   - Features:
     - Configurable maximum retry attempts
     - Customizable delay between retries
     - Exception handling
   - Practical use case with database connections

2. **Rate Limiting Decorator**
   - Location: `decorators/advanced/function_rate_limits.py`
   - Implements function call rate limiting
   - Features:
     - Configurable maximum calls
     - Time period tracking
     - Prevents function execution when limit is exceeded

## Key Concepts Covered

1. Basic Decorator Structure
2. Function Wrapping
3. Decorator Parameters
4. Closure and Scope
5. Error Handling
6. Time-based Operations
7. State Management in Decorators


### Advanced Retry Decorator

## Learning Objectives

1. Understanding Python decorator syntax and structure
2. Implementing common decorator patterns
3. Handling decorator parameters
4. Managing state in decorators
5. Practical applications of decorators in real-world scenarios

## Best Practices Demonstrated

1. Proper function wrapping using `*args` and `**kwargs`
2. Maintaining function metadata
3. Clear documentation and commenting
4. Error handling and logging
5. Parameter validation

## Requirements

- Python 3.x
- No external dependencies for basic decorators
- SQLite3 for database-related examples

## Contributing

Feel free to contribute additional decorator examples or improvements to existing ones. Please follow the established code structure and include appropriate documentation.
