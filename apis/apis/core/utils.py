import ast
from django.shortcuts import _get_queryset

def literal_eval_as_dict(data):
    try:
        return ast.literal_eval(data)
    except:
        return dict()

def get_object_or_None(klass, *args, **kwargs):
    queryset = _get_queryset(klass)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        raise None
