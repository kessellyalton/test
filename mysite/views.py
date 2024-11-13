import logging
import os

from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import FileResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import EmailPostForm, ContactForm, UploadFileForm, PDFFileForm
from .models import Blog, Resume, PDFFile, Post, Item,  ItemCategory, Portfolio
from django.shortcuts import render, get_object_or_404


from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ItemForm
from .models import Business, BusinessCategory
from .models import Item
from .models import TeamMember
import requests

from .forms import ItemForm



from .models import Testimonial



logger = logging.getLogger(__name__)

from django.shortcuts import render, get_object_or_404, redirect
from django.http import FileResponse, HttpResponse
from .models import Resume  # Ensure Resume model includes a title and file field for storing documents
import os

def upload_resume(request):
    if request.method == 'POST':
        description = request.POST.get('description', '')
        file = request.FILES.get('resume')
        if file:
            Resume.objects.create(file=file, description=description)
            return redirect('upload_success')
    return render(request, 'mysite/upload.html')

def resume_view(request):
    documents = Resume.objects.all()  # Query all documents
    return render(request, 'mysite/resume.html', {'documents': documents})

def download_document(request, document_id):
    document = get_object_or_404(Resume, id=document_id)
    response = HttpResponse(document.file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{document.file.name}"'
    return response

def upload_success(request):
    return render(request, 'mysite/upload_success.html')
def download_resume(request):
    return render(request, 'mysite/download_resume.html')

def home(request):
    return render(request, 'mysite/home.html')
def about(request):
    return render(request, 'mysite/about.html')
def contact(request):
    return render(request, 'mysite/contact.html')
def portfolio(request):
    return render(request, 'mysite/portfolio_list.html')
def resources(request):
    return render(request, 'mysite/resources.html')
def services(request):
    return render(request, 'mysite/services.html')
def team(request):
    return render(request, 'mysite/team.html')
def portfolio_details(request):
    return render(request, 'mysite/portfolio-details.html')
def inner_page(request):
    return render(request, 'mysite/inner-page.html')
def fnq(request):
    return render(request, 'mysite/fnq.html')

def blog_list(request):
    posts = Blog.objects.all()
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)

    logger.info(f"Retrieved {page_obj.paginator.count} posts.")
    return render(request, 'mysite/blog.html', {'posts': page_obj})



def portfolio_details_app(request):
    return render(request, 'mysite/portfolio-details-app.html')
def portfolio_details_web(request):
    return render(request, 'mysite/portfolio-details-web.html')
def portfolio_details_card(request):
    return render(request, 'mysite/portfolio-details-card.html')
def portfolio_details_asc(request):
    return render(request, 'mysite/portfolio-details-asc.html')
def portfolio_details_esp(request):
    return render(request, 'mysite/portfolio-details-esp.html')
def portfolio_details_emergency(request):
    return render(request, 'mysite/portfolio-details-emergency.html')

def portfolio_details_train(request):
    return render(request, 'mysite/portfolio-details-train.html')
def portfolio_details_tech(request):
    return render(request, 'mysite/portfolio-details-tech.html')
def portfolio_details_custom(request):
    return render(request, 'mysite/portfolio-details-custom.html')

def terms(request):
    return render(request, 'mysite/terms.html')

def privy(request):
    return render(request, 'mysite/privy.html')





def dash(request):
    return render(request, 'mysite/dash.html')






def press_view(request):
    featured_post = Post.objects.filter(is_featured=True).first()
    top_stories = Post.objects.exclude(id=featured_post.id if featured_post else None)[:3]
    opinion_posts = Post.objects.filter(category='Opinion')[:4]

    sections = {
        'Tech': Post.objects.filter(category='Tech')[:3],
        'Business': Post.objects.filter(category='Business')[:3],
        'Health': Post.objects.filter(category='Health')[:3],
    }

    context = {
        'featured_post': featured_post,
        'top_stories': top_stories,
        'opinion_posts': opinion_posts,
        'sections': sections,
    }
    return render(request, 'mysite/press.html', context)

def post_share(request, post_id):
    post_1 = get_object_or_404(Blog, pk=post_id)
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post_1.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post_1.title}"
            message = f"Read {post_1.title} at {post_url}\n\n{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, settings.EMAIL_HOST_USER, [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'mysite/post_share.html', {'form': form, 'post': post_1, 'sent': sent})

def thank_you(request):
    return render(request, 'mysite/thank_you.html')

def blog_detail(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    return render(request, 'mysite/blog-detail.html', {'post': post})

def submit_form_1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        full_message = f"From: {name}\nEmail: {email}\n\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ['kessellyalton1@gmail.com'],
                fail_silently=False,
            )
            logger.info("Email sent successfully.")
            messages.success(request, "Your message has been sent successfully.")
            return redirect('thank_you')
        except Exception as e:
            messages.error(request, "There was an error sending your email. Please try again later.")
            logger.error(f"Error sending email: {e}")
    return render(request, 'mysite/contact.html')

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pdf_list')
    else:
        form = PDFFileForm()
    return render(request, 'upload_pdf.html', {'form': form})
def pdf_list(request):
    # Fetch all PDF files to display on the list page
    pdfs = PDFFile.objects.all()
    return render(request, 'mysite/pdf_list.html', {'pdfs': pdfs})

def download_pdf(request, pk):
    # Get PDF file or return 404 if not found
    pdf = get_object_or_404(PDFFile, pk=pk)
    response = HttpResponse(pdf.file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{pdf.file.name}"'
    return response
def dashboard_view(request):
    return render(request, 'mysite/dash.html')

def directory(request):
    return render(request, 'mysite/business_list.html')

def school(request):
    return render(request, 'mysite/upload.html')
def business(request):
    return render(request, 'mysite/upload1.html')

def hospital(request):
    return render(request, 'mysite/upload2.html')

def recreation(request):
    return render(request, 'mysite/upload3.html')
def resort(request):
    return render(request, 'mysite/upload4.html')

def documents(request):
    return render(request, 'mysite/upload.html')
def resume(request):
    return render(request, 'mysite/resume.html')

def more(request):
    return render(request, 'mysite/more.html')


def buy(request):
    # Retrieve the most recent 12 items to display on the main buy page
    items = Item.objects.all().order_by('-posted_on')[:12]
    # Retrieve all categories to display as category options in the template
    categories = ItemCategory.objects.all()

    # Pass both items and categories to the template
    return render(request, 'mysite/buy.html', {
        'items': items,
        'categories': categories
    })

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'mysite/item_detail.html', {'item': item})


# views.py



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'mysite/register.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')  # Redirect to login if not authenticated
def post_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.seller = request.user
            item.save()
            return redirect('buy')  # Redirect to the item list page after submission
    else:
        form = ItemForm()
    return render(request, 'mysite/post_item.html', {'form': form})




def business_list(request):
    categories = BusinessCategory.objects.all()
    businesses = Business.objects.all().order_by('-opened_on')[:8]
    return render(request, 'mysite/business_list.html', {'categories': categories, 'businesses': businesses})



def business_search(request):
    query = request.GET.get('query', '')
    results = Business.objects.filter(name__icontains=query)
    return render(request, 'mysite/business_search_results.html', {'query': query, 'results': results})




# Foursquare API key setup
FOURSQUARE_API_KEY = settings.FOURSQUARE_API_KEY  # Store your key in settings.py




FOURSQUARE_API_KEY = settings.FOURSQUARE_API_KEY

def business_search(request):
    query = request.GET.get('query', '')
    location = request.GET.get('location', 'Monrovia')

    # Categories based on Foursquare's standard categories
    categories = {
        "school": "4bf58dd8d48988d13b941735",
        "shop": "4bf58dd8d48988d1f2941735",
        "entertainment": "4d4b7104d754a06370d81259",
        "resort": "4bf58dd8d48988d1f8931735",
        "sports": "4bf58dd8d48988d1e8941735",
        "hospital": "4bf58dd8d48988d196941735",
        "business": "4d4b7105d754a06375d81259",
    }

    # Set up request parameters
    url = "https://api.foursquare.com/v3/places/search"
    headers = {
        "Accept": "application/json",
         "Authorization": f"Bearer {settings.FOURSQUARE_API_KEY}"
    }
    params = {
        "query": query,
        "ll": "6.3156,-10.8074",  # Coordinates for Monrovia, Liberia
        "radius": 10000,
        "categories": ','.join(categories.values()),
        "limit": 20
    }

    # API call and debugging
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raises HTTPError for 4xx or 5xx status codes
        data = response.json()
        results = data.get('results', [])
        if not results:
            print("No results found for query:", query, "with location:", location)
    except requests.exceptions.RequestException as e:
        print("API request error:", e)
        return HttpResponse("An error occurred while fetching data. Please try again later.")

    return render(request, 'mysite/business_search_results.html', {
        'query': query,
        'results': results,
        'location': location,
    })

print(f"Using API Key: {settings.FOURSQUARE_API_KEY}")





def category_items(request, category_id):
    # Get the category or return 404 if not found
    category = get_object_or_404(ItemCategory, id=category_id)
    # Filter items based on the selected category
    items = Item.objects.filter(category=category)
    return render(request, 'mysite/category_items.html', {'category': category, 'items': items})



def item_list(request):
    items = Item.objects.all()
    return render(request, 'mysite/item_list.html', {'items': items})


@login_required
def post_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.seller = request.user  # Ensure the seller is set
            item.save()
            return redirect('buy')  # Redirect to the page that shows items after submission
        else:
            print("Form is invalid:", form.errors)  # Debugging for form validation errors
    else:
        form = ItemForm()
    return render(request, 'mysite/post_item.html', {'form': form})


def newsletter_signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if email:
            # Here, add your code to save the email or perform any other action
            # For example: NewsletterSubscription.objects.create(email=email)

            # Add a success message
            messages.success(request, "Thank you for subscribing! Check your inbox for our next update.")
            return redirect('home')  # Redirect to the homepage or a thank-you page

    return render(request, 'mysite/newsletter_signup.html')







def portfolio_list(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'mysite/portfolio_list.html', {'portfolios': portfolios})

def portfolio_detail(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    return render(request, 'mysite/portfolio_detail.html', {'portfolio': portfolio})


# mysite/views.py


def team(request):
    team_members = TeamMember.objects.all()
    return render(request, 'mysite/team.html', {'team_members': team_members})



def testimonials_view(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'mysite/testimonials.html', {'testimonials': testimonials})


def item_detail(request, item_id):
    # Retrieve the item by its ID or return a 404 error if not found
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'mysite/item_detail.html', {'item': item})


def category_articles(request, category):
    posts = Post.objects.filter(category=category)
    return render(request, 'mysite/category_articles.html', {'posts': posts, 'category': category})

def article_detail(request, pk):
    article = get_object_or_404(Post, pk=pk)
    return render(request, 'mysite/article_detail.html', {'article': article})