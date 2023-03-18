from django.shortcuts import render

from tickets.forms import PnrForm
from tickets.utils import decoder

def decode_pnr(request):
    if request.method == 'POST':
        form = PnrForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            decode_pnr = decoder(code)

            return render(request, 'decoded_pnr.html', {'decoded_pnr': decode_pnr})
    else:
        form = PnrForm()
    return render(request, 'decode_pnr.html', {'form': form})