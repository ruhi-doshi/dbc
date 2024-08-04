from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from smartcityapp.models import RaiseTicket
from django.contrib import messages

def dashboard(request):
    return render(request,'dashboard.html')
    '''if request.user.is_authenticated:
            return render(request,'dashboard.html')
    else:
        return redirect('/signin')'''

def signin(request):
    if request.user.is_authenticated:
            return redirect('/dashboard')
    else:
        if request.method=="POST": #if user has posted something
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username, password=password)
            if user is not None: #if user enters blank pass-only if its authenticated
                login(request,user)
                return redirect('/dashboard')
            else:
                return redirect('/signin')
        else:
            return render(request,"login.html") 
def signout(request):
     logout(request)
     return redirect('/signin')

def signup(request):
     if request.method=="POST":
           username=request.POST['username']
           email=request.POST['email']
           password=request.POST['password']
           if(username is not None and email is not None and password is not None):
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                login(request,user)
                return redirect('/')
           else:
                return redirect('/signup')
     else:
          return render(request,"signup.html")


def raisingcomplaintsection(request):
     return render (request,'raisingcomplaintsection.html')

def myarea(request):
     return render (request,'myarea.html')

def helpdesk(request):
     return render (request,'helpdesk.html')

def main(request):
          return render (request,'main.html')

def myticketssection(request):
     return render (request,'myticketssection.html')


def successfulticketsection(request):
     return render (request,'successfulticketsection.html')

def myticketssection(request):
     return render (request,'myticketssection.html')

def canceltickets(request):
     return render (request,'canceltickets.html')

def premium(request):
     return render (request,'premium.html')

def community(request):
     return render (request,'community.html')
          
def raiseticket(request):
    form = raisingticketform
    context = {'form':form}
    return render(request, 'signin/raisingcomplaintsection.html', context)

'''from pillow import Image
import io

# Saving an image
image = Image.open('path/to/image.jpg')
image_bytes = io.BytesIO()
image.save(image_bytes, format='JPEG')
image_data = image_bytes.getvalue()

your_model_instance = YourModel(description='Sample Image', image=image_data)
your_model_instance.save()

# Retrieving an image
retrieved_instance = YourModel.objects.get(id=1)
image_data = retrieved_instance.image
image = Image.open(io.BytesIO(image_data))
image.show()'''

def raiseticket(request):
     if request.method=="POST":
          if request.POST.get('title') and request.POST.get('location') and request.POST.get('description'):
               saverecord=RaiseTicket()
               saverecord.title=request.POST.get('title')
               saverecord.location=request.POST.get('location')
               saverecord.description=request.POST.get('description')
               saverecord.save()
               messages.success()
               return render(request,"successfullticketsection.html")
     else:
          return render(request,"dashboard.html")







'''
# views.py
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pandas as pd
import io
import base64
from django.http import JsonResponse

def generate_pothole_data(num_clusters, points_per_cluster, cluster_spread):
    np.random.seed(42)
    data = []
    for _ in range(num_clusters):
        cluster_center = np.random.uniform(low=[37.7, -122.5], high=[37.8, -122.4])
        cluster_points = cluster_center + cluster_spread * np.random.randn(points_per_cluster, 2)
        data.append(cluster_points)
    return np.vstack(data)

def cluster_view(request):
    num_clusters = 5
    points_per_cluster = 50
    cluster_spread = 0.01
    data = generate_pothole_data(num_clusters, points_per_cluster, cluster_spread)

    data = tf.constant(data, dtype=tf.float32)
    k = 5
    max_iters = 100
    tolerance = 1e-4

    centroids = tf.Variable(tf.gather(data, tf.random.shuffle(tf.range(tf.shape(data)[0]))[:k]))

    def assign_clusters(data, centroids):
        expanded_data = tf.expand_dims(data, 0)
        expanded_centroids = tf.expand_dims(centroids, 1)
        distances = tf.reduce_sum(tf.square(expanded_data - expanded_centroids), 2)
        return tf.argmin(distances, 0)

    def update_centroids(data, assignments, k):
        new_centroids = []
        for c in range(k):
            points_for_centroid = tf.boolean_mask(data, tf.equal(assignments, c))
            new_centroids.append(tf.reduce_mean(points_for_centroid, axis=0))
        return tf.stack(new_centroids)

    for i in range(max_iters):
        assignments = assign_clusters(data, centroids)
        new_centroids = update_centroids(data, assignments, k)
        centroid_shift = tf.reduce_sum(tf.square(new_centroids - centroids))
        centroids.assign(new_centroids)
        if centroid_shift < tolerance:
            break

    assignments = assignments.numpy()
    final_centroids = centroids.numpy()

    # Plotting
    plt.figure()
    plt.scatter(data[:, 0], data[:, 1], c=assignments, cmap='viridis', alpha=0.5)
    plt.scatter(final_centroids[:, 0], final_centroids[:, 1], s=300, c='red', marker='x')
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.title('Pothole Concentrations')

    # Convert plot to base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')

    return JsonResponse({'image': image_base64})'''
