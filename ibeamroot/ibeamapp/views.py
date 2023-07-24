from django.shortcuts import render
from ibeamapp.utils import ibeam
   

def get_ibeam_form(request):
    if request.method == 'POST':
        sigma = float(request.POST['sigma'])
        force_applied = float(request.POST['force_applied'])
        beam_thick = float(request.POST['beam_thick'])
        num_distances = int(request.POST['num_distances'])
        distances = [float(request.POST[f'distance{i}']) \
                     for i in range(1, num_distances+1)]
        
        # using the ibeam() function to create the height, width
        # relationships
        ibeam_dict = ibeam(sigma, 
                           force_applied, 
                           beam_thick, 
                           distances)
        
        context = {'sigma': sigma, 'force_applied': force_applied,
                   'beam_thick': beam_thick, 'results': ibeam_dict}

        # Render the same template again
        return render(request, 'distance.html', context)
        
    else:
        return render(request, 'base.html')
