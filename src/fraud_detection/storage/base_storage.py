from abc import ABC, abstractmethod


class BaseStorageService(ABC):
    # An abstract class that defines the data

    @abstractmethod
    def save_artifact(self, artifact, path):
        pass

    @abstractmethod
    def retrieve_artifact(self, artifact_name):
        pass



