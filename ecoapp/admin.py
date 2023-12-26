from django.contrib import admin
from ecoapp.models import Slides,Product,Category,Basket_card,Brend,NutritionValue,Header,Blog,HomeAbout,HomeIcons,Partners,Subject
from ckeditor.widgets import CKEditorWidget
from django.db import models

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Basket_card)
admin.site.register(Brend)
admin.site.register(NutritionValue)
admin.site.register(Header)
admin.site.register(Blog)
admin.site.register(HomeAbout)
admin.site.register(HomeIcons)
admin.site.register(Partners)
admin.site.register(Subject)
admin.site.register(Slides)

# class MyModelAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.TextField: {'widget': CKEditorWidget(config_name='default')},
#     }
#     exclude = ('content_without_ck','content','name','bottomcontent','sidename','sidecontent','bottomname')
# class MyTitleAdmin(admin.ModelAdmin):
#     exclude = ('title','content')
# class MyNameAdmin(admin.ModelAdmin):
#     exclude = ('name','content')
    
# class MyNameAdminVideo(admin.ModelAdmin):
#     exclude = ('name','content','coverimage')
# class MyOnlyNameAdmin(admin.ModelAdmin):
#     exclude = ('name','content','coverimage')
# class MyminiTitleAdmin(admin.ModelAdmin):
#     exclude = ('minititle','title','content','content2','contentbig')
# admin.site.register(HomeHeader,MyTitleAdmin)
# admin.site.register(HomeHeaderVideo,MyOnlyNameAdmin)
# admin.site.register(Article,MyNameAdmin)
# admin.site.register(Blog,MyModelAdmin)
# admin.site.register(Video,MyNameAdminVideo)
# admin.site.register(Photo,MyNameAdmin)
# admin.site.register(Tag)
# admin.site.register(Category)
# admin.site.register(Movie,MyOnlyNameAdmin)
# admin.site.register(About,MyminiTitleAdmin)
# admin.site.register(AllHeader,MyTitleAdmin)
# admin.site.register(Partners)
