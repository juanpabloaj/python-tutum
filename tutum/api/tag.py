import json as json_parser
import copy

from base import Taggable
from http import send_request
from exceptions import TutumApiError


class Tag(object):
    def __init__(self):
        self._tags = []
        self.tags = []

    def add(self, tagname):
        if isinstance(tagname, list):
            for t in tagname:
                self.tags.append({"name": t})
        else:
            self.tags.append({"name": tagname})

    @classmethod
    def create(cls, **kwargs):
        """Returns a new instance of the model (without saving it) with the attributes specified in ``kwargs``

        :returns: tag -- a new local instance of the Tag
        """
        return cls(**kwargs)

    def delete(self, tag):
        """Deletes the object in Tutum
        :returns: bool -- whether the operation was successful or not
        """
        if not self.endpoint:
            raise TutumApiError("You must initialize the tag object before performing this operation")

        if self.tags:
            raise TutumApiError("You must save the object before performing this operation")

        action = "DELETE"
        url = "/".join([self.endpoint, tag])
        send_request(action, url)
        if {"name": tag} in self.tags:
            self.tags.remove({"name": tag})
        for _tag in self._tags:
            if _tag.get('name', '') == tag:
                self._tags.remove(_tag)
        return True

    @classmethod
    def fetch(cls, taggable):
        """"Fetch a tag object given the taggable object

        :param pk: the Taggable object (usually service, node, nodecluster, etc.)
        :type pk: Taggable
        :returns: Tag -- the instance fetched from Tutum
        :raises: TutumApiError
        """
        if not isinstance(taggable, Taggable):
            raise TutumApiError("The object does not support tag")
        if not taggable._detail_uri:
            raise TutumApiError("You must save the taggable object before performing this operation")
        tag = cls()
        taggable.refresh()
        tag.endpoint = "/".join([taggable._detail_uri, "tags"])
        tags = []
        for _tag in taggable.tags:
            tagname = _tag.get("name", "")
            if tagname:
                tags.append({"name": tagname})
        tag._tags = copy.deepcopy(tags)
        return tag

    def list(self):
        """List all tags of a taggable object

        :returns: list -- a list of tags that match the query
        """
        if not self.endpoint:
            raise TutumApiError("You must initialize the tag object before performing this operation")
        json = send_request('GET', self.endpoint)
        if json:
            return json.get('objects', [])
        return []

    def save(self):
        if not self.endpoint:
            raise TutumApiError("You must initialize the tag object before performing this operation")

        json = send_request("POST", self.endpoint, data=json_parser.dumps(self.tags))
        if json:
            tags = []
            for _tag in json:
                tagname = _tag.get("name", "")
                if tagname:
                    tags.append({"name": tagname})
            self._tags = copy.deepcopy(tags)
            self.tags = []
            return True
        return False