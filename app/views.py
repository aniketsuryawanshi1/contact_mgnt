from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .form import ProfileForm
from .models import Profile
from django.http import HttpResponse


def home(request):
   # Retrieving all the contacts from the database
    profiles = Profile.objects.all()
    context = {'profiles' : profiles}
    return render(request, 'home.html', context)

# This is a view for listing a single contact 

def contact_detail(request, id):
    # Querying a particular contact by its id 
    profile = Profile.objects.get(pk = id)
    context = {'profile' : profile}
    return render(request, 'contact-detail.html', context)

# This is view for adding contact
def add_contact(request):
    if request.method == 'POST':
        # Extracting data from the POST request
        data = request.POST
        # Extracting the image file
        photo = request.FILES.get('image-file')

        # Basic form validation (you might want to add more robust validation)
        if not data.get('name') or not data.get('email'):
            return HttpResponse('Error: Name and email are required fields.')

        try:
            # Creating and saving the contact
            profile = Profile.objects.create(
                name=data['name'],
                email=data['email'],
                photo=photo,
                gender=data.get('gender', ''),  # Optional field, handle it appropriately
                pnum=data.get('pnum', ''),  # Optional field, handle it appropriately
                job_role=data.get('job_role', '')  # Optional field, handle it appropriately
            )

            # Redirecting to the home page after successful addition
            return redirect('home')
        except Exception as e:
            # Handle any exception that might occur during profile creation
            return HttpResponse(f'Error: {str(e)}')

    return render(request, 'add-contact.html')




# This is a view for editing the contact's info
def edit_contact(request, id ):
    # getting a contact to be updated
    profile = Profile.objects.get(pk = id)

    # Populating the form with the contact's information 
    form = ProfileForm(request.POST, request.FILES, instance= profile)

    # checking if the form's data is valid
    if form.is_valid():
        # Saving data to the database
        form.save()
        # Redirecting to the home page
        return redirect('home')
    context = {'form' : form}
    return render(request, 'update-contact.html', context)

# This is view for deleting a contact 
def delete_contact(request,id):
    # Getting the contact to be deleted
    profile = Profile.objects.get(pk = id)

    # Checking if the method is POST
    if request.method == 'POST':
        # Delete the Contact
        profile.delete()

        # Return to home after success delete
        return redirect('home')
    context = {'profile' : profile}
    return render(request, 'delete-contact.html', context) 

 