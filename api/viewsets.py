from rest_framework import viewsets


class CreateListDestroyModelViewSet(viewsets.mixins.CreateModelMixin,
                                    viewsets.mixins.ListModelMixin,
                                    viewsets.mixins.DestroyModelMixin,
                                    viewsets.GenericViewSet):
    """
    A viewset that provides default `list()`, `create()`

    destroy() actions.

    """
    pass
