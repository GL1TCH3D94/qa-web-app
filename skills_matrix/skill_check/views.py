from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.forms import modelform_factory
from .models import User, Skills

def skill(request, id):

    skill_list = []

    skills = get_object_or_404(Skills, pk=id)

    for skill in Skills.objects.all():
        if skills.get_user_name() == skill.get_user_name():
            skill_list.append(skill)


    return render(request, "skill_check/skill.html", {"skills": skill_list})

