# coding=utf-8
# Copyright (c) 2020 Alibaba PAI team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import TYPE_CHECKING
from ..modelzoo.file_utils import _BaseLazyModule

_import_structure = {
    "sequence_classification.model": ["SequenceClassification", "SequenceMultiLabelClassification", "DistillatorySequenceClassification", "FewshotSequenceClassification", "CptFewshotSequenceClassification"],
    "sequence_labeling.model": ['SequenceLabeling'],
    "language_modeling.model": ['LanguageModeling'],
    "feature_vectorization.model": ['FeatureVectorization'],
    "text_match.model": ['TextMatch', 'TextMatchTwoTower', 'DistillatoryTextMatch', 'FewshotSingleTowerTextMatch', 'CptFewshotSingleTowerTextMatch'],
    "data_augmentation.model": ["DataAugmentation"],
    "geep_classification.model": ["GEEPClassification"],
    "multi_modal.model": ["MultiModal"],
    "text2image_generation.model": ["TextImageGeneration"],

    "sequence_classification.evaluator": ['SequenceClassificationEvaluator', 'SequenceMultiLabelClassificationEvaluator'],
    "sequence_labeling.evaluator": ['SequenceLabelingEvaluator'],
    "language_modeling.evaluator": ['LanguageModelingEvaluator'],
    "text_match.evaluator": ['TextMatchEvaluator'],
    "geep_classification.evaluator": ['GEEPClassificationEvaluator'],
    "multi_modal.evaluator": ['MultiModalEvaluator'],
    "text2image_generation.evaluator": ["TextImageGenerationEvaluator"],

    "sequence_classification.predictor": ['SequenceClassificationPredictor', 'FewshotSequenceClassificationPredictor', 'CptFewshotSequenceClassificationPredictor'],
    "sequence_labeling.predictor": ['SequenceLabelingPredictor'],
    "feature_vectorization.predictor": ['FeatureVectorizationPredictor'],
    "text_match.predictor": ['TextMatchPredictor', 'TextMatchTwoTowerPredictor', 'FewshotSingleTowerTextMatchPredictor', 'CptFewshotSingleTowerTextMatchPredictor'],
    "data_augmentation.predictor": ['DataAugmentationPredictor'],
    "geep_classification.predictor": ['GEEPClassificationPredictor'],
    "multi_modal.predictor": ['MultiModalPredictor'],
    "text2image_generation.predictor": ['TextImageGenerationPredictor'],

    "geep_classification.data": ['GEEPClassificationDataset'],
    "language_modeling.data": ['LanguageModelingDataset'],
    "multi_modal.data": ['MultiModalDataset'],
    "sequence_classification.data": ['ClassificationDataset', 'DistillatoryClassificationDataset', 'FewshotSequenceClassificationDataset'],
    "sequence_labeling.data": ['SequenceLabelingDataset', 'SequenceLabelingAutoDataset'],
    "text_match.data": ['TwoTowerDataset', 'SingleTowerDataset', 'DistillatorySingleTowerDataset', 'FewshotSingleTowerTextMatchDataset', 'SiameseDataset'],
    "text2image_generation.data": ['TextImageDataset'],
    "dataset": ['BaseDataset', 'GeneralDataset', 'load_dataset', 'list_datasets'],
    "api": ['get_application_dataset', 'get_application_model', 'get_application_model_for_evaluation', 'get_application_evaluator', 'get_application_predictor'],
}

if TYPE_CHECKING:
    from .sequence_classification.model import SequenceClassification, SequenceMultiLabelClassification, DistillatorySequenceClassification, FewshotSequenceClassification, CptFewshotSequenceClassification
    from .sequence_labeling.model import SequenceLabeling
    from .language_modeling.model import LanguageModeling
    from .feature_vectorization.model import FeatureVectorization
    from .text_match.model import TextMatch, TextMatchTwoTower, DistillatoryTextMatch, FewshotSingleTowerTextMatch, CptFewshotSingleTowerTextMatch
    from .data_augmentation.model import DataAugmentation
    from .geep_classification.model import GEEPClassification
    from .multi_modal.model import MultiModal
    from .text2image_generation.model import TextImageGeneration

    from .sequence_classification.evaluator import SequenceClassificationEvaluator, SequenceMultiLabelClassificationEvaluator
    from .sequence_labeling.evaluator import SequenceLabelingEvaluator
    from .language_modeling.evaluator import LanguageModelingEvaluator
    from .text_match.evaluator import TextMatchEvaluator
    from .geep_classification.evaluator import GEEPClassificationEvaluator
    from .multi_modal.evaluator import MultiModalEvaluator
    from .text2image_generation.evaluator import TextImageGenerationEvaluator

    from .sequence_classification.predictor import SequenceClassificationPredictor, FewshotSequenceClassificationPredictor, CptFewshotSequenceClassificationPredictor
    from .sequence_labeling.predictor import SequenceLabelingPredictor
    from .feature_vectorization.predictor import FeatureVectorizationPredictor
    from .text_match.predictor import TextMatchPredictor, TextMatchTwoTowerPredictor, FewshotSingleTowerTextMatchPredictor, CptFewshotSingleTowerTextMatchPredictor
    from .data_augmentation.predictor import DataAugmentationPredictor
    from .geep_classification.predictor import GEEPClassificationPredictor
    from .multi_modal.predictor import MultiModalPredictor
    from .text2image_generation.predictor import TextImageGenerationPredictor

    from .sequence_classification.data import ClassificationDataset, DistillatoryClassificationDataset, FewshotSequenceClassificationDataset
    from .sequence_labeling.data import SequenceLabelingDataset, SequenceLabelingAutoDataset
    from .language_modeling.data import LanguageModelingDataset
    from .text_match.data import TwoTowerDataset, SingleTowerDataset, DistillatorySingleTowerDataset, FewshotSingleTowerTextMatchDataset, SiameseDataset
    from .geep_classification.data import GEEPClassificationDataset
    from .multi_modal.data import MultiModalDataset
    from .text2image_generation.data import TextImageDataset

    from .dataset import BaseDataset, GeneralDataset
    from .dataset import load_dataset, list_datasets

    from .api import get_application_dataset, get_application_model, get_application_model_for_evaluation
    from .api import get_application_evaluator, get_application_predictor
    
    

else:
    import importlib
    import os
    import sys

    class _LazyModule(_BaseLazyModule):
        """
        Module class that surfaces all objects but only performs associated imports when the objects are requested.
        """

        __file__ = globals()["__file__"]
        __path__ = [os.path.dirname(__file__)]

        def _get_module(self, module_name: str):
            return importlib.import_module("." + module_name, self.__name__)

    sys.modules[__name__] = _LazyModule(__name__, _import_structure)
