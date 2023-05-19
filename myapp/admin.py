from django.contrib import admin
from myapp.models import log,feedback,nuser,Image,startup,suggestion,entrepreneur,Comment

# # Register your models here.
admin.site.register(log)
admin.site.register(feedback)

@admin.register(nuser)
class nuserAdmin(admin.ModelAdmin):
    list_display = ['userid','profilepic','bio','twitter','facebook','instagram','twitter','skills']
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id' , 'photo' ,'date' ,'caption','userid']

@admin.register(suggestion)
class suggestionAdmin(admin.ModelAdmin):
    list_display = ['to' , 'by' ,'date' ,'opinion']

@admin.register(entrepreneur)
class entrepreneurAdmin(admin.ModelAdmin):
    list_display = [ 'coverphoto','entrepreneurid','profilepic','startup','twitter','facebook','instagram','linkedin','about','form']

@admin.register(startup)
class startupAdmin(admin.ModelAdmin):
    list_display = [ 'coverphoto','startupid','profilepic','startupid','twitter','facebook','instagram','linkedin','about','startuplink','pitch','phoneno','form']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display =['id','comment' ,'date' ,'userid','post_id']