"""
Definition of views.
"""


from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django.db.models import F
from app.models import *
from .forms import *

from datetime import datetime



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )


def statistics(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    number_of_wrestlers = Wrestler.objects.all().count()
    number_of_events = Event.objects.all().count()
    number_of_matches = Match.objects.all().count()
    number_of_draws = Match.objects.filter(winner="Draw").count()
    number_of_wins_and_losses = number_of_matches - number_of_draws
    number_of_correct_predictions = Match.objects.filter(prediction = F('winner')).count()
    number_of_wrong_predictions = number_of_wins_and_losses - number_of_correct_predictions
    percentage_correct = 0
    if number_of_wins_and_losses > 0:
        percentage_correct = (((number_of_correct_predictions*1.0) / number_of_wins_and_losses)*100)

    return render(
        request,
        'app/statistics.html',
        {
            'title':'Statistics',
            'message':'Statistics About Your Predictions',
            'year':datetime.now().year,
            #'wrestlers': wrestlers,
            'count_wrestlers': number_of_wrestlers,
            'count_events': number_of_events,
            'count_matches': number_of_matches,
            'count_wins_and_losses': number_of_wins_and_losses,
            'count_draws': number_of_draws,
            'count_correct_predictions': number_of_correct_predictions,
            'count_wrong_predictions': number_of_wrong_predictions,
            'prediction_percentage': percentage_correct
        }
    )

def add_wrestler(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    add_form = AddWrestlerForm()
    succeeded = ""
    added = ""
    if request.method == 'POST':      
        add_form = AddWrestlerForm(request.POST)
        if add_form.is_valid():
            try:
                toAdd = add_form.cleaned_data['name']
                if Wrestler.objects.filter(name = toAdd).count() < 1:
                    added = Wrestler(name = toAdd)
                    added.save()
                    succeeded = toAdd + " was successfully added!"
                    added = "True"
                else:
                    succeeded = toAdd + " already exists."
            except Exception:
                succeeded = "Error processing request"
    list_of_wrestlers = Wrestler.objects.all()
    wrestlers = []
    for wrestler in list_of_wrestlers:
        wrestlers.append(wrestler.name)
    wrestlers.sort()
    return render(
        request,
        'app/add_wrestler.html',
        {
            'title':'Add Wrestlers',
            'message':'View, Add, Edit, or Delete Wrestlers',
            'year':datetime.now().year,
            'wrestlers': wrestlers,
            'add_form': add_form,
            'succeeded': succeeded,
        }
    )

def edit_wrestler(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    edit_form = EditWrestlerForm()
    succeeded = ""
    editted = ""
    if request.method == 'POST':      
       edit_form = EditWrestlerForm(request.POST)
       if edit_form.is_valid():
           try:
                change = edit_form.cleaned_data['new_name']
                old_name = edit_form.cleaned_data['old_name']
                old_obj = Wrestler.objects.filter(name = old_name)
                new_obj = Wrestler.objects.filter(name = change)
                if new_obj.count() < 1 and old_obj.count() > 0 :
                    toEdit = Wrestler.objects.get(name = old_name)
                    toEdit.name=change
                    toEdit.save()      
                    editted = "True"
                    succeeded = []
                    succeeded.append(str(old_name))
                    succeeded.append("successfully editted to")
                    succeeded.append(str(change))
                    succeeded = ' '.join(succeeded)
                elif new_count >= 1:
                    succeeded = change + " already exists."
                else:
                    succeeded = old_name + " doesn't exist."
           except Exception as E:
               print(E)
               succeeded = "Error processing request"

    list_of_wrestlers = Wrestler.objects.all()
    wrestlers = []
    for wrestler in list_of_wrestlers:
        wrestlers.append(wrestler.name)
    wrestlers.sort()
    return render(
        request,
        'app/edit_wrestler.html',
        {
            'title':'Edit Wrestler',
            'message':'View, Add, Edit, or Delete Wrestlers',
            'year':datetime.now().year,
            'wrestlers': wrestlers,
            'edit_form': edit_form,
            'succeeded': succeeded,
            'editted': editted,
        }
    )

def delete_wrestler(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    delete_form = DeleteWrestlerForm()
    if request.method == 'POST':      
        delete_form = DeleteWrestlerForm(request.POST)
        deleted = ""
        succeeded = ""
        if delete_form.is_valid():
            toDelete = delete_form.cleaned_data['name']
            toDelete_obj = Wrestler.objects.filter(name = toDelete)
            try:
                if toDelete_obj.count() > 0:
                    toDelete_obj.delete()
                    succeeded = toDelete + " was deleted!"
                    deleted = "True"
                else:
                    succeeded = toDelete + " already does not exist."
            except Exception:
                succeeded = "Error processing request"
                    

    list_of_wrestlers = Wrestler.objects.all()
    wrestlers = []
    for wrestler in list_of_wrestlers:
        wrestlers.append(wrestler.name)
    wrestlers.sort()
    return render(
        request,
        'app/delete_wrestler.html',
        {
            'title':'Delete Wrestlers',
            'message':'View, Add, Edit, or Delete Wrestlers',
            'year':datetime.now().year,
            'wrestlers': wrestlers,
            'delete_form': delete_form,
            'succeeded': succeeded,
            'deleted': deleted,
        }
    )

def view_wrestler(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    view_form = ViewWrestlerForm()
    toView = ""
    name = ""
    number_of_matches = 0
    number_wins_and_losses = 0
    number_of_wins = 0
    number_of_losses = 0
    number_of_draws = 0
    winning_percent = 0
    number_of_correct_predictions = 0
    prediction_percent = 0
    viewed = ""
    succeeded = ""
    if request.method == 'POST':      
        view_form = ViewWrestlerForm(request.POST)
        if view_form.is_valid():
            toView = view_form.cleaned_data['name']
            try:
                if Wrestler.objects.filter(name = toView).count() > 0:
                    obj = Wrestler.objects.get(name = toView)
                    id = obj.id
                    name = toView 
                    their_matches = Match_Wrestler_Results.objects.filter(wrestler_id_id=id)
                    number_of_matches = their_matches.count() 
                    number_of_wins = their_matches.filter(won = True).count()
                    number_of_losses = their_matches.filter(lost = True).count()
                    number_wins_and_losses = number_of_wins + number_of_losses
                    number_of_draws = their_matches.filter(draw = True).count()
                    if number_of_matches > 0:
                        winning_percent = ((number_of_wins*1.0)/number_of_matches)*100
                    number_of_correct_predictions = their_matches.filter(prediction=True).count()
                    if number_wins_and_losses > 0:
                        prediction_percent = ((number_of_correct_predictions*1.0)/number_wins_and_losses)*100
                    viewed = "True"
                else:
                    succeeded = toView + " No longer exists"
            except Exception:
                succeeded = "Error processing request"
    list_of_wrestlers = Wrestler.objects.all()
    wrestlers = []
    for wrestler in list_of_wrestlers:
        wrestlers.append(wrestler.name)
    wrestlers.sort()
    return render(
        request,
        'app/view_wrestler.html',
        {
            'title':'View Wrestler',
            'message':'View, Add, Edit, or Delete Wrestlers',
            'year':datetime.now().year,
            'wrestlers': wrestlers,
            'view_form': view_form,
            'to_view': toView,
            'name': name,
            'number_of_matches': number_of_matches,
            'number_of_wins': number_of_wins,
            'number_of_losses': number_of_losses,
            'number_of_draws': number_of_draws,
            'number_wins_and_losses': number_wins_and_losses,
            'winning_percent': winning_percent,
            'number_of_correct_predictions': number_of_correct_predictions,
            'prediction_percent': prediction_percent,
            'succeeded': succeeded,
            'viewed': viewed,
        }
    )




def select_event(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/select_event.html',
        {
            'title':'Select Event',
            'message':'View, Edit, or Delete Events',
            'year':datetime.now().year,
        }
    )

def add_event(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/add_event.html',
        {
            'title':'Add Event',
            'message':'Create and Add a New Event',
            'year':datetime.now().year,
        }
    )