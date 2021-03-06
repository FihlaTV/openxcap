
"""Interface to the backend subsystem"""

__all__ = ['database', 'opensips']

from zope.interface import Interface


class StatusResponse(object):
    def __init__(self, code, etag=None, data=None, old_etag=None):
        self.code = code
        self.etag = etag
        self.data = data
        self.old_etag = old_etag

    @property
    def succeed(self):
        return 200 <= self.code <= 299

class StorageError(Exception): pass


class IStorage(Interface):
    """Storage interface. It defines the methods an XCAP storage class must implement."""

    def get_document(self, uri, check_etag):
        """Fetch an XCAP document.

        @param uri: an XCAP URI that contains the XCAP user and the document selector
        
        @param check_etag: a callable used to check the etag of the stored document

        @returns: a deferred that'll be fired when the document is fetched"""

    def put_document(self, uri, document, check_etag):
        """Insert or replace an XCAP document.
        
        @param uri: an XCAP URI that contains the XCAP user and the document selector
        
        @param document: the XCAP document
        
        @param check_etag: a callable used to check the etag of the stored document
        
        @returns: a deferred that'll be fired when the action was completed."""

    def delete_document(self, uri, check_etag):
        """Delete an XCAP document.
        
        @param uri: an XCAP URI that contains the XCAP user and the document selector
        
        @param check_etag: a callable used to check the etag of the document to be deleted
        """
