from django import template

register = template.Library()


@register.filter(name="add_atr")
def add_atr(form, arg):
    """
    arg is a dictionary with:
        key is field's name
        value is an attribute dictionary with:
            key is css attribute
            value is value of the attribute

    example arg = {"field_name":{'class': 'field_class'}}
    """
    for field_name, attributes in arg:
        form.fields[field_name].widget.attrs.update(attributes)
    return form
