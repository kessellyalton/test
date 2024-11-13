from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Main pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio_list, name='portfolio-list'),
    #path('portfolio/', views.portfolio, name='portfolio'),
    path('resources/', views.resources, name='resources'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
    path('inner-page/', views.inner_page, name='inner-page'),
    path('fnq/', views.fnq, name='fnq'),
    path('blog/', views.blog_list, name='blog'),

    # Blog and Portfolio details
    path('blog/<int:pk>/', views.blog_detail, name='blog-detail'),
    path('portfolio-details-app/', views.portfolio_details_app, name='portfolio-details-app'),
    path('portfolio-details-web/', views.portfolio_details_web, name='portfolio-details-web'),
    path('portfolio-details-card/', views.portfolio_details_card, name='portfolio-details-card'),
    path('portfolio-details-asc/', views.portfolio_details_asc, name='portfolio-details-asc'),
    path('portfolio-details-esp/', views.portfolio_details_esp, name='portfolio-details-esp'),
    path('portfolio-details-emergency/', views.portfolio_details_emergency, name='portfolio-details-emergency'),
    path('portfolio-details-train/', views.portfolio_details_train, name='portfolio-details-train'),
    path('portfolio-details-tech/', views.portfolio_details_tech, name='portfolio-details-tech'),
    path('portfolio-details-custom/', views.portfolio_details_custom, name='portfolio-details-custom'),
    path('portfolio/', views.portfolio_list, name='portfolio-list'),
    path('portfolio/<int:pk>/', views.portfolio_detail, name='portfolio-detail'),


    # Contact and Testimonials
    path('submit_form_1/', views.submit_form_1, name='submit_form_1'),
    path('thank_you/', views.thank_you, name='thank_you'),


    # Document Management (Upload/Download and Resume)
    path('resume/', views.resume_view, name='resume'),  # Main documents/resume page
    path('upload/', views.upload_resume, name='upload_resume'),
    path('download/<int:document_id>/', views.download_document, name='download_document'),
    path('upload_success/', views.upload_success, name='upload_success'),

    # Other sections
    path('press/', views.press_view, name='press'),
    path('dash/', views.dashboard_view, name='dash'),
    path('buy/', views.buy, name='buy'),

    # User Account and Item Management
    path('post-item/', views.post_item, name='post_item'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='mysite/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='mysite/logout.html'), name='logout'),

    # Directory and Search
    path('directory/', views.directory, name='directory'),
    path('school/', views.school, name='school'),
    path('business/', views.business, name='business'),
    path('hospital/', views.hospital, name='hospital'),
    path('recreation/', views.recreation, name='recreation'),
    path('resort/', views.resort, name='resort'),
    path('business_list/', views.business_list, name='business_list'),
    path('business/search/', views.business_search, name='business_search'),
    path('privy/', views.privy, name='privy'),
    path('terms/', views.terms, name='terms'),

    # Documents section with corrected 'resume' and 'documents' name conflict
    path('documents/', views.resume_view, name='documents'),
    path('category/<int:category_id>/', views.category_items, name='category_items'),
    path('item-list/', views.item_list, name='item_list'),
    path('newsletter_signup/', views.newsletter_signup, name='newsletter_signup'),
    path('blog/<int:post_id>/share/', views.post_share, name='post_share'),
    path('more', views.more, name='more'),
    path('testimonials/', views.testimonials_view, name='testimonials'),
    path('buy/category/<int:category_id>/', views.category_items, name='item_list_by_category'),
    path('documents/', views.pdf_list, name='pdf_list'),  # PDF list page
    path('documents/download/<int:pk>/', views.download_pdf, name='download_pdf'),
    path('category/<str:category>/', views.category_articles, name='category_articles'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    
    
    
]
