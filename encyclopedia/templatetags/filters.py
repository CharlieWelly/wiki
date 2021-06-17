from django import template

register = template.Library()


@register.filter(name="add_class")
def add_class(form, arg):
    for field in form.fields.values():
        field.widget.attrs.update({"class": arg})
    return form


@register.filter(name="add_attr")
def add_attr(form, arg):
    """
    arg = "attr,value" without spacing brefore and after comma ,
    """
    arg = arg.split(",")
    attr = arg[0]
    value = arg[1]

    for field in form.fields.values():
        field.widget.attrs.update({attr: value})
    return form


def add_specific_attr(form, arg):
    """
    arg = "fieldname,attr,value" without spacing before and after comma ,
    """
    arg = arg.split(",")
    fieldname = arg[0]
    attr = arg[1]
    value = arg[2]

    form.fields[fieldname]
    pass
