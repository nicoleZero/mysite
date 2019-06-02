from django.shortcuts import render

# Create your views here.
def testcase_manage(request):
	return render(request,"testcase.html")