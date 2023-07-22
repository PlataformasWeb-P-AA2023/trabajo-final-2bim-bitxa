from django import template

register = template.Library()

@register.filter
def get_attribute(object, attribute_name):
    return getattr(object, attribute_name)

@register.filter
def is_related_field(obj, field_name):
    """Check if a field name refers to a related field in the object."""
    try:
        return obj._meta.get_field(field_name).is_relation
    except Exception:
        return False

@register.filter
def get_related_field(value, arg):
    try:
        related_object = getattr(value, arg)
        return related_object.nombre if related_object else ""
    except Exception:
        return ""
