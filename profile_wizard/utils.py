import os
from . import models
def update_filename(instance, filename):
    path = "upload/path/"

    format = instance.id + instance.user + instance.file_extension
    return os.path.join(path, format)
from django.db import models

import uuid
import os

def get_image_path(instance, filename):
    point_num = filename.find('.')
    return os.path.join('photos', "user%s" % str(instance.user.id), str(instance.user.id)+filename[point_num:])


#transaction_uuid     + instance.user
