from datetime import date


def get_age(instance):
    delta = date.today() - instance.dob
    return delta.days/365