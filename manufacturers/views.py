from django.shortcuts import render, redirect

from .models import UtilityConsumption
from .forms import UtilityConsumptionForm

def utility(request):
    if request.method == 'POST':
        form = UtilityConsumptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('utility')
        
    else:
        form = UtilityConsumptionForm()
    return render(request, 'application/utility.html', {'form': form})
