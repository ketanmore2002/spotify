from django.db import models



from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, GoogleDriveFilePermission

permission =  GoogleDriveFilePermission(
   GoogleDrivePermissionRole.READER,
   GoogleDrivePermissionType.USER,
   "moreketan2002@gmail.com"
)

gd_storage = GoogleDriveStorage(permissions=(permission, ))


# Define Google Drive Storage
gd_storage = GoogleDriveStorage()

# Create your models here.


class music (models.Model):

    title = models.CharField(max_length=300,null=True)
    video_id = models.CharField(max_length=300,null=True)
    song = models.FileField(upload_to ='songs',null=True,blank=True, storage=gd_storage)
    image = models.FileField(upload_to ='images',null=True,blank=True, storage=gd_storage)
    author = models.CharField(max_length=300,null=True)
    publish_date = models.CharField(max_length=300,null=True)
    length = models.CharField(max_length=300,null=True)
    thumbnail_url = models.CharField(max_length=300,null=True)    

    def __str__(self):

            return self.title