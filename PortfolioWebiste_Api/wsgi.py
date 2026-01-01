"""
WSGI config for PortfolioWebiste_Api project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PortfolioWebiste_Api.settings')

application = get_wsgi_application()

# Vercel အတွက် ဒီစာကြောင်းကို ထည့်ပေးရပါမယ်
app = application