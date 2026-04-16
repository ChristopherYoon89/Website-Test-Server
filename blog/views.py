from typing import Any
from django.shortcuts import (
	render, 
	redirect,
    get_object_or_404,
)
from django.urls import reverse_lazy
from .models import (
	Post, 
    Solution,
	ReleaseNotes, 
	JobPost,
    NewsletterRequest,
    Resource,
)
from django.views.generic import (
	TemplateView, 
	DetailView,
	ListView,
    FormView,
)
from .forms import (
	ContactForm, 
	NewsletterForm,
    NewsletterUnsubscribeForm,
    JobApplicationForm,
)
from django.contrib.messages.views import SuccessMessageMixin
#from django.core.mail import EmailMessage



def home(request):
    context = {
        'posts': Post.objects.filter(publish_boolean=True).order_by('-date_posted')[:3],
        'release_notes': ReleaseNotes.objects.filter(publish_boolean=True).order_by('-date_posted')[:3]  
    }
    return render(request, 'blog/home.html', context)



def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})



def imprint(request):
    return render(request, 'blog/imprint.html', {'title': 'Imprint'})



class ReleaseNotesListView(ListView):
    model = ReleaseNotes
    title = "Release Notes"
    template_name = "blog/releasenoteslist.html"
    context_object_name = "release_notes"
    ordering = ['-date_posted']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['release_notes'] = ReleaseNotes.objects.filter(publish_boolean=True).order_by('-date_posted')
        return context
    


class ReleaseNoteView(DetailView):
    model = ReleaseNotes
    title = "Release Note"
    template_name = "blog/releasenotedetail.html"
    context_object_name = "release_note"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        release_note = self.object
        context["all_release_notes"] = ReleaseNotes.objects.filter(publish_boolean=True).exclude(pk=release_note.pk).order_by("-date_posted")[:3]
        return context



class BlogPostsView(ListView):
    model = Post
    title = "Blog"
    template_name = "blog/bloglist.html"
    context_object_name = "blog_posts"
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_posts'] = Post.objects.filter(publish_boolean=True).order_by('-date_posted')
        return context



class BlogDetailView(DetailView):
    model = Post 
    title = "Blog Post"
    template_name = 'blog/blogdetail.html'
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_post = self.object
        context["all_blog_posts"] = Post.objects.filter(publish_boolean=True).exclude(pk=blog_post.pk).order_by("-date_posted")[:3]
        return context
    


class SolutionsPostsView(ListView):
    model = Solution
    title = "Solutions"
    template_name = "blog/solutionslist.html"
    context_object_name = "solution_post"
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['solution_post'] = Solution.objects.filter(publish_boolean=True).order_by('-date_posted')
        return context
    


class SolutionDetailView(DetailView):
    model = Solution 
    title = "Solution"
    template_name = 'blog/solutiondetail.html'
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_release_notes"] = ReleaseNotes.objects.filter(publish_boolean=True).order_by("-date_posted")[:3]
        return context



def contactview(request):
    if request.method == 'POST':
        l_form = ContactForm(request.POST)
        if l_form.is_valid():
            l_form.save()
            return redirect('contact-redirect-page')
    else:
        l_form = ContactForm()

    context = {
        'l_form': l_form
    }

    return render(request, 'blog/contact.html', context)



def newsletterview(request):
    if request.method == 'POST':
        n_form = NewsletterForm(request.POST)
        if n_form.is_valid():
            n_form.save()
            return redirect('signup-completed-page')
    else:
        n_form = NewsletterForm()

    context = {
        'n_form': n_form
    }
    return render(request, 'blog/newsletter.html', context)



def newsletterunsubscribeview(request):
    if request.method == 'POST':
        n_form = NewsletterUnsubscribeForm(request.POST)
        if n_form.is_valid():
            n_form.save()
            email_to_remove = n_form.cleaned_data['email']
            newsletter_request = NewsletterRequest.objects.filter(email=email_to_remove)
            
            if newsletter_request:
                newsletter_request.delete()
                return redirect('newsletter-unsubscribe-completed-page')
            else:
                return redirect('newsletter-unsubscribe-page')
    else:
        n_form = NewsletterUnsubscribeForm()

    context = {
        'n_form': n_form
    }
    return render(request, 'blog/newsletterunsubscribe.html', context)



class TermsView(TemplateView):
    '''
    View that renders the terms and condition page
    '''
    template_name = 'blog/termsandconditions.html'



class PrivacyPolicyView(TemplateView):
    '''
    View that renders the privacy policy page
    '''
    template_name = 'blog/privacypolicy.html'



class ContactRedirectView(TemplateView):
    '''
    View the contact from is redirected to when message was sent
    '''
    template_name = "blog/contact_redirect.html"



class NewsletterRedirectView(TemplateView):
    '''
    View the newsletter form is redirected to when sign up was 
    completed
    '''
    template_name = 'blog/newsletter_redirect.html'



class NewsletterUnsubRedirectView(TemplateView):
    '''
    View the newsletter unsubscribe form is redirected to when sign up was 
    completed
    '''
    template_name = 'blog/newsletterunsubscribe_redirect.html'



class JobApplicationRedirectView(TemplateView):
    '''
    View the job application form is redirected to when user applies for a job
    '''
    template_name = 'blog/jobapplication_redirect.html'



def accept_cookies(request):
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie('accepted_cookies', 'true', max_age=365*24*60*60)
    return response



def reject_cookies(request):
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie('accepted_cookies', 'false', max_age=365*24*60*60)
    return response



class JobPostListView(ListView):
    model = JobPost
    title = "Job Posts"
    template_name = "blog/jobpostlist.html"
    context_object_name = "jobposts"
    ordering = ['-date_posted']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobposts'] = JobPost.objects.filter(publish_boolean=True).order_by('-date_posted')
        return context
    


class JobApplicationFormView(SuccessMessageMixin, FormView):
    template_name = "blog/jobapplication.html"
    form_class = JobApplicationForm
    success_url = reverse_lazy('job-applied-completed-page')

    def get_initial(self):
        # Add the job_post to the form's initial data
        job_post = get_object_or_404(JobPost, slug=self.kwargs['slug'])
        return {'job_post': job_post}

    def form_valid(self, form):
        application = form.save()
        job_post = get_object_or_404(JobPost, slug=self.kwargs['slug'])
        application = form.save(commit=False)
        application.jobpost = job_post
        application.save()

        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)



class ResourcesView(ListView):
    '''
    View that renders the resources page
    '''
    model = Resource
    template_name = 'blog/resourceslist.html'
    context_object_name = 'resources'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class ResourcesDetailView(DetailView):
    '''
    View that renders the detail view of resources
    '''
    model = Resource 
    title = 'Resource'
    template_name = 'blog/resourcesdetail.html'
    context_object_name = 'resource'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    
