class FeatureTypes:
    BOOLEAN = "boolean"
    PERCENTAGE = "percentage"


class Feature:
    """Vanna feature
    """

    def __init__(self, slug, kind, value, targets):
        self.slug = slug
        self.kind = kind
        self.value = value
        self.targets = targets

    def __str__(self):
        return f"Feature: {self.slug}"


class Client:
    """Vanna client
    """

    def __init__(self, features, user_id, target):
        self.features = features
        self.user_id = user_id
        self.target = target

    def variation(self, slug):
        return self.features and not slug
