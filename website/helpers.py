from QA_Web import settings
import os


def handle_bot_file_upload(module_name, file):
    local_file_path = os.path.join(settings.MODULE_UPLOAD_DESTINATION, module_name + '.py')

    with open(local_file_path, 'wb+') as local_file:
        for chunk in file.chunks():
            local_file.write(chunk)

    return True


def delete_local_file(module_name):
    local_file_path = os.path.join(settings.MODULE_UPLOAD_DESTINATION, module_name + '.py')
    os.remove(local_file_path)
    return True
