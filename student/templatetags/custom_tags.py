from django import template
register = template.Library()
import datetime

@register.filter(name='stu_age')
def stu_age(value):
    age = datetime.date.today().year - value.year - ((datetime.date.today().month, datetime.date.today().day) <
(value.month, value.day))
    return age

register.filter('stu_age', stu_age)


@register.filter(name='short_text')
def short_text(value, arg):
    # if arg is first_name: return the first string before space
    if int(arg):
        text1= value.split("_")[arg]
        text2= value.split("_")[arg+1]
        return  text2 +"_"+ text1 + "... "
register.filter('short_text', short_text)



@register.filter(name='underless')
def underless(value):
    # if arg is first_name: return the first string before space
    text= value.replace("_",'')
    return  text
register.filter('underless', underless)

@register.filter(name='set_zeros')
def set_zeros(value, arg):
    if int(arg):
        text= value.zfill(arg)
        return  text
register.filter('set_zeros', set_zeros)