from django import template

register = template.Library()

def cut(value,arg):

    """
    cuts out all values form arg in the string
    """

    return value.replace(arg,"")

def times_three(value):
    """
    multiplies value x3
    """

    return value*3

def cut_o(value):
    return value.replace("o","")



register.filter("cut",cut)
register.filter("times_three",times_three)
register.filter("cut_o",cut_o)
