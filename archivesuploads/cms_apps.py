from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register  # register the application
class ArchivesuploadsApphook(CMSApp):
    app_name = "archivesuploads"
    name = "Archivesuploads App"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["archivesuploads.urls"]
