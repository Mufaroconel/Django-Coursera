# Template Language and Variable Interpolation

## Overview
In this guide, you will delve deeper into Django's templating language to understand how it's used to integrate dynamic data with HTML markup. You will also learn about the role of variables in rendering dynamic content in templates.

### Introduction to Django Template Engine
Modern web frameworks, including Django, use template systems that merge data sources with HTML to create dynamic web pages. Django templates are HTML scripts interspersed with DTL code, which the template engine uses to replace placeholders with actual data, rendering the final content to the user's browser.

### Django Template Language Components
Django Template Language includes three crucial components:
- **Variables**: Use to display dynamic data within templates.
- **Tags**: Provide logic and control structures within templates.
- **Filters**: Modify the output of variables for display.

## Template Variables
Variables are used within templates to insert dynamic data. For example, the `render()` function in Django allows you to pass context variables to templates, which are then rendered using curly braces syntax `{{ variable_name }}`.

### Example of Variable Usage
Given a URL like `http://localhost:8000/myapp/Novak`, a view function can pass the name 'Novak' as a variable to the template:

```python
def index(request, name):
    context = {'name': name}
    return render(request, 'index.html', context)
```

Inside `index.html`, the name would be displayed with:
```html
<h2>Welcome {{ name }}</h2>
```

## Template Tags
Tags are crucial for adding logic to templates. They are enclosed within `{% tag %}` symbols.

### Common Tags
- **{% if %}**: Allows conditional rendering based on Boolean expressions.
- **{% for %}**: Enables looping over data structures like lists or dictionaries.

### Example of Tags in Use
**Conditional Rendering:**
```django
{% if user == "admin" %}
    <h2>Welcome {{ user }}</h2>
{% else %}
    <h2>Welcome Guest. You don't have admin access</h2>
{% endif %}
```

**Looping Over Data:**
```django
<ul>
    {% for lang in langs %}
    <li>{{ lang }}</li>
    {% endfor %}
</ul>
```

## Template Filters
Filters are used to modify the display of variables. They are applied using the pipe symbol `|`.

### Common Filters
- **upper**: Converts a string to uppercase.
- **length**: Returns the length of a string or list.
- **title**: Converts a string to title case.

### Example of Filters
```django
{{ name|upper }}
{{ name|length }}
{{ "django template language"|title }}
```

## Conclusion
Understanding and utilizing Django's Template Language effectively allows you to create dynamic, data-driven web applications efficiently. This guide covers the fundamentals, but Django's documentation offers comprehensive details and examples for deeper exploration.
