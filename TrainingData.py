import datetime
from Sample import Sample
from Hyperparameter import Hyperparameter
from typing import List
class TrainingData:

    """
    A set of training data and testing data with methods to load and test the samples
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.uploaded = datetime.datetime
        self.tested = datetime.datetime
        self.training: List[Sample] = []
        self.testing: List[Sample] = []
        self.tuning: List[Hyperparameter] = []

    def load(
            self, 
            raw_data_source: Iterable[dict[str, str]]
    ) -> None:
        """Load and partition the raw data"""
        for n, row in enumerate(raw_data_source):
            """filter and extract data subsets (chp 6)"""
            """Create self.training and self.testing subsets"""
            self.uploaded = datetime.datetime.now(tz=datetime.timezone.utc)

    def test(
            self,
            parameter: Hyperparameter
    ) -> None:
        """Test this Hyperparameter Value"""
        parameter.test()
        self.tuning.append(parameter)
        self.tested = datetime.datetime.now(tz=datetime.timezone.utc)
        
    def classify(
            self,
            parameter: Hyperparameter,
            sample: Sample
            ) -> Sample:
        """Classify this sample"""
        classification = parameter.classify(sample)
        return sample
    