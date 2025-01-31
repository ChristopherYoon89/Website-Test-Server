from django.shortcuts import (
	render, 
	redirect,
    get_object_or_404,
)
from .models import (
	PostGerman, 
	ReleaseNotesGerman,
	JobPostGerman,
    SolutionGerman,
)
from django.views.generic import (
	TemplateView, 
	DetailView, 
	ListView,
	FormView,
)
from django.contrib import messages
from .forms import (
	ContactForm, 
	NewsletterForm, 
    JobApplicationGermanForm
)
from blog.models import Resource
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy



def home_ger(request):
    context = {
        'posts': PostGerman.objects.filter(publish_boolean=True).order_by('-date_posted')[:3],
        'release_notes': ReleaseNotesGerman.objects.filter(publish_boolean=True).order_by('-date_posted')[:3]  
    }
    return render(request, 'blog_ger/home_ger.html', context)



def about_ger(request):
    return render(request, 'blog_ger/about_ger.html', {'title': 'Über uns'})



class ReleaseNotesListGerView(ListView):
    model = ReleaseNotesGerman
    title = "Release Notes"
    template_name = "blog_ger/releasenoteslist_ger.html"
    context_object_name = "release_notes"
    ordering = ['-date_posted']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['release_notes'] = ReleaseNotesGerman.objects.filter(publish_boolean=True).order_by('-date_posted')
        return context



class ReleaseNoteGerView(DetailView):
    model = ReleaseNotesGerman
    title = "Release Note"
    template_name = "blog_ger/releasenotedetail_ger.html"
    context_object_name = "release_note"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        release_note = self.object
        context["all_release_notes"] = ReleaseNotesGerman.objects.filter(publish_boolean=True).exclude(pk=release_note.pk).order_by("-date_posted")[:3]
        return context
    


class BlogPostsGerView(ListView):
    model = PostGerman
    title = "Blog"
    template_name = "blog_ger/bloglist_ger.html"
    context_object_name = "blog_posts"
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_posts'] = PostGerman.objects.filter(publish_boolean=True).order_by('-date_posted')
        return context



class BlogDetailGerView(DetailView):
    model = PostGerman
    title = "Blog Post"
    template_name = 'blog_ger/blogdetail_ger.html'
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_post = self.object
        context["all_blog_posts"] = PostGerman.objects.filter(publish_boolean=True).exclude(pk=blog_post.pk).order_by("-date_posted")[:3]
        return context
    


class SolutionsPostsGerView(ListView):
    model = SolutionGerman
    title = "Solutions"
    template_name = "blog_ger/solutionslist_ger.html"
    context_object_name = "solution_posts"
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['solution_posts'] = SolutionGerman.objects.filter(publish_boolean=True).order_by('-date_posted')
        return context



class SolutionDetailGerView(DetailView):
    model = SolutionGerman
    title = "Solution"
    template_name = 'blog_ger/solutiondetail_ger.html'
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_release_notes"] = ReleaseNotesGerman.objects.filter(publish_boolean=True).order_by("-date_posted")[:3]
        return context 



def contactview_ger(request):
    if request.method == 'POST':
        l_form = ContactForm(request.POST)
        if l_form.is_valid():
            l_form.save()
            messages.success(request, f'Deine Anfrage wurde versendet!')
            return redirect('contact')
    else:
        l_form = ContactForm()

    context = {
        'l_form': l_form
    }

    return render(request, 'blog_ger/contact_ger.html', context)



def newsletterview_ger(request):
    if request.method == 'POST':
        n_form = NewsletterForm(request.POST)
        if n_form.is_valid():
            n_form.save()
            messages.success(request, f'Deine Email Adresse wurde in die Mailing-Liste aufgenommen!')
            return redirect('newsletter-page')
    else:
        n_form = NewsletterForm()

    context = {
        'n_form': n_form
    }
    return render(request, 'blog_ger/newsletter_ger.html', context)



class TermsGerView(TemplateView):
    '''
    View that renders the terms and condition page
    '''
    template_name = 'blog_ger/termsandconditions_ger.html'
    title = 'Nutzungsbedingungen'



class PrivacyPolicyGerView(TemplateView):
    '''
    View that renders the privacy policy page
    '''
    template_name = 'blog_ger/privacypolicy_ger.html'
    title = 'Datenschutz'
    


class ImprintGerView(TemplateView):
    '''
    View that renders the German imprint page
    '''
    template_name = 'blog_ger/imprint_ger.html'
    title = 'Impressum'
    

class JobPostListGerView(ListView):
    model = JobPostGerman
    title = "Jobs"
    template_name = "blog_ger/jobpostlist_ger.html"
    context_object_name = "jobposts"
    ordering = ['-date_posted']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobposts'] = JobPostGerman.objects.filter(publish_boolean=True).order_by('-date_posted')
        return context
    


class JobApplicationFormGermanView(SuccessMessageMixin, FormView):
    template_name = "blog_ger/jobapplication_ger.html"
    form_class = JobApplicationGermanForm
    success_url = reverse_lazy('job-page-ger')
    success_message = "Vielen Dank für deine Bewerbung!"

    def get_initial(self):
        # Add the job_post to the form's initial data
        job_post = get_object_or_404(JobPostGerman, slug=self.kwargs['slug'])
        return {'job_post': job_post}

    def form_valid(self, form):
        application = form.save()
        job_post = get_object_or_404(JobPostGerman, slug=self.kwargs['slug'])
        application = form.save(commit=False)
        application.jobpost = job_post
        application.save()

        #email = EmailMessage(
        #    subject = f"{application.subject}",
        #    body=f"Name: {application.name} \n Job Post: {job_post.title} \n Message: {application.message}",
        #    from_email = f"{application.email}",
        #    to=['yoondeveloping@outlook.com'],
        #)

        #email.attach(application.resume_upload.name, application.resume_upload.read(), 'application/pdf')
        #email.send()

        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    


class KeasbeyAppProductGermanView(TemplateView):
    '''
    View that renders the German Keasbey App product page
    '''
    template_name = 'blog_ger/productpagekeasbeyapp_ger.html'



class ResourcesGerView(ListView):
    '''
    View that renders the resources page
    '''
    model = Resource
    template_name = 'blog_ger/resourceslist_ger.html'
    context_object_name = 'resources'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class ResourcesDetailGerView(DetailView):
    '''
    View that renders the detail view of resources
    '''
    model = Resource 
    title = 'Resource'
    template_name = 'blog_ger/resourcesdetail_ger.html'
    context_object_name = 'resource'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context