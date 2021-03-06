import re

from .exceptions import TutumApiError, ObjectNotFound, NonUniqueIdentifier
from .container import Container
from .node import Node
from .nodecluster import NodeCluster
from .service import Service
from .stack import Stack
from .volume import Volume
from .volumegroup import VolumeGroup


def is_uuid4(identifier):
    uuid4_regexp = re.compile('^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}', re.I)
    match = uuid4_regexp.match(identifier)
    return bool(match)


class Utils:
    @staticmethod
    def fetch_by_resource_uri(uri):
        if not isinstance(uri, basestring):
            raise TutumApiError("Uri format is invalid")
        terms = uri.strip("/").split("/")
        if len(terms) < 2:
            raise TutumApiError("Uri format is invalid")

        id = terms[-1]
        resource_type = terms[-2]

        if resource_type.lower() == "container":
            return Container.fetch(id)
        elif resource_type.lower() == "node":
            return Node.fetch(id)
        elif resource_type.lower() == "nodecluster":
            return NodeCluster.fetch(id)
        elif resource_type.lower() == "service":
            return Service.fetch(id)
        elif resource_type.lower() == "stack":
            return Stack.fetch(id)
        elif resource_type.lower() == "volume":
            return Volume.fetch(id)
        elif resource_type.lower() == "volumegroup":
            return VolumeGroup.fetch(id)
        else:
            raise TutumApiError(
                "Unsupported resource type. Only support: container, node, nodecluster, service, stack, volume, volumegroup")


    @staticmethod
    def fetch_remote_container(identifier, raise_exceptions=True):
        try:
            if is_uuid4(identifier):
                try:
                    return Container.fetch(identifier)
                except Exception:
                    raise ObjectNotFound("Cannot find a container with the identifier '%s'" % identifier)
            else:
                objects_same_identifier = Container.list(uuid__startswith=identifier) or \
                                          Container.list(name=identifier)
                if len(objects_same_identifier) == 1:
                    uuid = objects_same_identifier[0].uuid
                    return Container.fetch(uuid)
                elif len(objects_same_identifier) == 0:
                    raise ObjectNotFound("Cannot find a container with the identifier '%s'" % identifier)
                raise NonUniqueIdentifier("More than one container has the same identifier, please use the long uuid")

        except (NonUniqueIdentifier, ObjectNotFound) as e:
            if not raise_exceptions:
                return e
            raise e

    @staticmethod
    def fetch_remote_service(identifier, raise_exceptions=True):
        try:
            if is_uuid4(identifier):
                try:
                    return Service.fetch(identifier)
                except Exception:
                    raise ObjectNotFound("Cannot find a service with the identifier '%s'" % identifier)
            else:
                objects_same_identifier = Service.list(uuid__startswith=identifier) or \
                                          Service.list(name=identifier)

                if len(objects_same_identifier) == 1:
                    uuid = objects_same_identifier[0].uuid
                    return Service.fetch(uuid)
                elif len(objects_same_identifier) == 0:
                    raise ObjectNotFound("Cannot find a service with the identifier '%s'" % identifier)
                raise NonUniqueIdentifier("More than one service has the same identifier, please use the long uuid")
        except (NonUniqueIdentifier, ObjectNotFound) as e:
            if not raise_exceptions:
                return e
            raise e

    @staticmethod
    def fetch_remote_stack(identifier, raise_exceptions=True):
        try:
            if is_uuid4(identifier):
                try:
                    return Stack.fetch(identifier)
                except Exception:
                    raise ObjectNotFound("Cannot find a stack with the identifier '%s'" % identifier)
            else:
                objects_same_identifier = Stack.list(uuid__startswith=identifier) or \
                                          Stack.list(name=identifier)
                if len(objects_same_identifier) == 1:
                    uuid = objects_same_identifier[0].uuid
                    return Stack.fetch(uuid)
                elif len(objects_same_identifier) == 0:
                    raise ObjectNotFound("Cannot find a stack with the identifier '%s'" % identifier)
                raise NonUniqueIdentifier("More than one stack has the same identifier, please use the long uuid")

        except (NonUniqueIdentifier, ObjectNotFound) as e:
            if not raise_exceptions:
                return e
            raise e

    @staticmethod
    def fetch_remote_volume(identifier, raise_exceptions=True):
        try:
            if is_uuid4(identifier):
                try:
                    return Volume.fetch(identifier)
                except Exception:
                    raise ObjectNotFound("Cannot find a volume with the identifier '%s'" % identifier)
            else:
                objects_same_identifier = Volume.list(uuid__startswith=identifier)
                if len(objects_same_identifier) == 1:
                    uuid = objects_same_identifier[0].uuid
                    return Volume.fetch(uuid)
                elif len(objects_same_identifier) == 0:
                    raise ObjectNotFound("Cannot find a volume with the identifier '%s'" % identifier)
                raise NonUniqueIdentifier("More than one volume has the same identifier, please use the long uuid")

        except (NonUniqueIdentifier, ObjectNotFound) as e:
            if not raise_exceptions:
                return e
            raise e

    @staticmethod
    def fetch_remote_volumegroup(identifier, raise_exceptions=True):
        try:
            if is_uuid4(identifier):
                try:
                    return VolumeGroup.fetch(identifier)
                except Exception:
                    raise ObjectNotFound("Cannot find a volume with the identifier '%s'" % identifier)
            else:
                objects_same_identifier = VolumeGroup.list(uuid__startswith=identifier) or \
                                          VolumeGroup.list(name=identifier)
                if len(objects_same_identifier) == 1:
                    uuid = objects_same_identifier[0].uuid
                    return VolumeGroup.fetch(uuid)
                elif len(objects_same_identifier) == 0:
                    raise ObjectNotFound("Cannot find a volume with the identifier '%s'" % identifier)
                raise NonUniqueIdentifier("More than one volume has the same identifier, please use the long uuid")

        except (NonUniqueIdentifier, ObjectNotFound) as e:
            if not raise_exceptions:
                return e
            raise e

    @staticmethod
    def fetch_remote_node(identifier, raise_exceptions=True):
        try:
            if is_uuid4(identifier):
                try:
                    return Node.fetch(identifier)
                except Exception:
                    raise ObjectNotFound("Cannot find a node with the identifier '%s'" % identifier)
            else:
                objects_same_identifier = Node.list(uuid__startswith=identifier)
                if len(objects_same_identifier) == 1:
                    uuid = objects_same_identifier[0].uuid
                    return Node.fetch(uuid)
                elif len(objects_same_identifier) == 0:
                    raise ObjectNotFound("Cannot find a node with the identifier '%s'" % identifier)
                raise NonUniqueIdentifier("More than one node has the same identifier, please use the long uuid")

        except (NonUniqueIdentifier, ObjectNotFound) as e:
            if not raise_exceptions:
                return e
            raise e

    @staticmethod
    def fetch_remote_nodecluster(identifier, raise_exceptions=True):
        try:
            if is_uuid4(identifier):
                try:
                    return NodeCluster.fetch(identifier)
                except Exception:
                    raise ObjectNotFound("Cannot find a node cluster with the identifier '%s'" % identifier)
            else:
                objects_same_identifier = NodeCluster.list(uuid__startswith=identifier) or \
                                          NodeCluster.list(name=identifier)
                if len(objects_same_identifier) == 1:
                    uuid = objects_same_identifier[0].uuid
                    return NodeCluster.fetch(uuid)
                elif len(objects_same_identifier) == 0:
                    raise ObjectNotFound("Cannot find a node cluster with the identifier '%s'" % identifier)
                raise NonUniqueIdentifier(
                    "More than one node cluster has the same identifier, please use the long uuid")

        except (NonUniqueIdentifier, ObjectNotFound) as e:
            if not raise_exceptions:
                return e
            raise e