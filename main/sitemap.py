from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return [
            'home',
            'about',
            'services',
            'python_automation',
            'rpa',
            'intelligent_document_processing',
            'chatbot',
            'industries',
            'manufacturing',
            'healthcare',
            'finance',
            'retail',
            'contact',
            'portfolio',
            'testimonials',
            'blog',
        ]

    def location(self, item):
        return reverse(item)
