from .models import *
from .forms import *

def header_context(request):
    legalfiles = LegalFiles.objects.all()
    lawyertp = LawyerType.objects.all()
    return {'legalfiles':legalfiles,'lawyertp':lawyertp}