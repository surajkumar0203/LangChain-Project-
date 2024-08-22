from django.shortcuts import render,redirect
from django.views import View
from myapp.form import InputForm
from myapp.langChain import askme_recipe

class index(View):
    def get(self,request):
        recipe_msg=request.session.get("is_recipe_msg", '')
        form=InputForm()
        return render(request,'index.html',{"form":form,'recipe_msg':recipe_msg})


    def post(self,request):
        form=InputForm(request.POST)
        if form.is_valid():
            msg=form.cleaned_data['inputBox']
            recipe_msg=askme_recipe(msg)
            request.session["is_recipe_msg"] = recipe_msg
        return redirect('/')