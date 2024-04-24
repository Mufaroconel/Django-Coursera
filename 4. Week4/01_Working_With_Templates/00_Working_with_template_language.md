# Introduction to Django Template Language (DTL)

In this video tutorial, we will explore the Django Template Language (DTL), a powerful tool for separating presentation and application logic in web applications. By the end of this video, you'll understand how to effectively use DTL in your Django projects.

## What is DTL?

DTL is inspired by the popular Jinja2 template engine and shares many of its features. It helps developers adhere to the "Don't Repeat Yourself" (DRY) principle and adds a security layer by preventing template code from executing as Python code.

## Key Constructs of DTL

DTL consists of four main constructs that substitute for basic programming functionalities:

- **Variables**
  - Enclosed in double curly braces `{{ }}`.
  - Rendered by the template engine by evaluating the variable and replacing it with its result.
  - Example: `{{ restaurant_name }}` would display as "Welcome to Little Lemon restaurant".

- **Tags**
  - Created with curly braces and percentage symbols `{% %}`.
  - Control structures like `if` and `for` loops are common tags.
  - Example:
    - `if` tag checks conditions within the template, such as user login status.
    - `for` loop iterates over data, such as menu items in a list.

- **Filters**
  - Modify the values of variables.
  - Example: `{{ name|upper }}` converts `name` to uppercase.

- **Comments**
  - Use curly braces and percentage symbols `{% comment %} {% endcomment %}`.
  - Not rendered in the final output, used for in-template documentation.

## Practical Examples

1. **Using Variables**:
   - Display the name of a restaurant dynamically.

2. **Using Tags**:
   - Implement conditional rendering and loops for dynamic content, such as displaying different content based on user login status or looping through a list of menu items.

3. **Using Filters**:
   - Change display formats or modify data presentation, like converting text to uppercase or formatting dates.

4. **Using Comments**:
   - Document sections of the template for developer reference without affecting the rendered output.

## Conclusion

This tutorial covers the basics of working with DTL in Django. Understanding these constructs allows you to create dynamic and efficient web applications. For further learning, check the additional reading resources linked at the end of this lesson.

