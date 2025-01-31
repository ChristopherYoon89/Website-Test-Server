from django.urls import path
from . import views
from blog_ger import views as blog_ger_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.home, name='blog-home'),
	path('blog/', views.BlogPostsView.as_view(), name='blog-posts-page'),
    path('blog/<slug>/', views.BlogDetailView.as_view(), name='blog-detail'),
	path('release-notes/', views.ReleaseNotesListView.as_view(), name="release-notes-page"),
	path('release-note/<slug>/', views.ReleaseNoteView.as_view(), name='release-note-detail'),
	path('solutions/', views.SolutionsPostsView.as_view(), name='solutions-page'),
	path('solutions/<slug>/', views.SolutionDetailView.as_view(), name='solution-detail'),
	path('about/', views.about, name='about-page'),
	path('imprint/', views.imprint, name='imprint'),
	path('jobs/', views.JobPostListView.as_view(), name='job-page'),
	path('apply/<slug>/', views.JobApplicationFormView.as_view(), name='application-form-page'),
	path('contact/', views.contactview, name='contact'),
	path('newsletter/', views.newsletterview, name='newsletter-page'),
	path('newsletter-unsubscribe/', views.newsletterunsubscribeview, name='newsletter-unsubscribe-page'),
	path('terms-and-conditions/', views.TermsView.as_view(), name='terms-page'),
	path('privacy-policy/', views.PrivacyPolicyView.as_view(), name='privacy-page'),
	path('accept-cookies/', views.accept_cookies, name='accept-cookies'),
	path('reject-cookies/', views.reject_cookies, name='reject-cookies'),
	path('keasbey-app/', views.KeasbeyAppProductView.as_view(), name='keasbey-app-product-page'),
	path('resources/', views.ResourcesView.as_view(), name='resources-page'),
	path('resources/<slug>/', views.ResourcesDetailView.as_view(), name='resources-detail-page'),

	path('de/', blog_ger_views.home_ger, name='blog-home-ger'),
	path('de/release-notes/', blog_ger_views.ReleaseNotesListGerView.as_view(), name='release-notes-page-ger'),
	path('de/release-note/<slug>/', blog_ger_views.ReleaseNoteGerView.as_view(), name='release-note-detail-ger'),
	path('de/loesungen/', blog_ger_views.SolutionsPostsGerView.as_view(), name='solutions-page-ger'),
	path('de/loesungen/<slug>/', blog_ger_views.SolutionDetailGerView.as_view(), name='solution-detail-ger'),
	path('de/blog/', blog_ger_views.BlogPostsGerView.as_view(), name='blog-posts-page-ger'),
	path('de/blog/<slug>/', blog_ger_views.BlogDetailGerView.as_view(), name='blog-detail-ger'),
	path('de/kontakt/', blog_ger_views.contactview_ger, name='contact-page-ger'),
	path('de/newsletter/', blog_ger_views.newsletterview_ger, name='newsletter-page-ger'),
	path('de/nutzungsbedingungen/', blog_ger_views.TermsGerView.as_view(), name='terms-page-ger'),
	path('de/datenschutz/', blog_ger_views.PrivacyPolicyGerView.as_view(), name='privacy-page-ger'),
	path('de/ueber-mich/', blog_ger_views.about_ger, name='about-page-ger'),
	path('de/impressum/', blog_ger_views.ImprintGerView.as_view(), name='imprint-page-ger'),
	path('de/jobs/', blog_ger_views.JobPostListGerView.as_view(), name='job-page-ger'),
	path('de/bewerben/<slug>/', blog_ger_views.JobApplicationFormGermanView.as_view(), name='application-form-page-ger'),
	path('de/keasbey-app/', blog_ger_views.KeasbeyAppProductGermanView.as_view(), name='keasbey-app-product-page-ger'),
	path('de/downloads/', blog_ger_views.ResourcesGerView.as_view(), name='resources-page-ger'),
	path('de/downloads/<slug>/', blog_ger_views.ResourcesDetailGerView.as_view(), name='resources-detail-page-ger'),
]


urlpatterns += staticfiles_urlpatterns()
