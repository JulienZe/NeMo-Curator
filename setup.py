# Copyright (c) 2024, NVIDIA CORPORATION.  All rights reserved.
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

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='nemo_curator',
    version='0.2.0',
    description='Scalable Data Preprocessing Tool for '
    'Training Large Language Models',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/NVIDIA/NeMo-Curator',
    author='Joseph Jennings, Mostofa Patwary, Sandeep Subramanian, '
    'Shrimai Prabhumoye, Ayush Dattagupta, Vibhu Jawa, Jiwei Liu, Ryan Wolf',
    author_email='jjennings@nvidia.com, mpatwary@nvidia.com, '
    'rywolf@nvidia.com, sprabhumoye@nvidia.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[
        'dask[complete]>=2021.7.1',
        'distributed>=2021.7.1',
        'dask-mpi>=2021.11.0',
        'charset_normalizer>=3.1.0',
        'awscli>=1.22.55',
        'fasttext==0.9.2',
        'pycld2==0.41',
        'justext==3.0.0',
        'ftfy==6.1.1',
        'warcio==1.7.4',
        'zstandard==0.18.0',
        'in-place==0.5.0',
        'unidic-lite==1.0.8',
        'jieba==0.42.1',
        'comment_parser',
        'beautifulsoup4',
        'mwparserfromhell @ git+https://github.com/earwig/mwparserfromhell.git@0f89f44',
        'cudf-cu12==23.10.*',
        'dask-cudf-cu12==23.10.*',
        'cugraph-cu12==23.10.*',
        'dask-cuda==23.10.*',
        'spacy>=3.6.0, <4.0.0',
        'presidio-analyzer==2.2.351',
        'presidio-anonymizer==2.2.351',
        'usaddress==0.5.10',
        'nemo_toolkit[nlp]>=1.23.0'
    ],
    entry_points={
        'console_scripts': [
            'get_common_crawl_urls=nemo_curator.scripts.get_common_crawl_urls:console_script',
            'get_wikipedia_urls=nemo_curator.scripts.get_wikipedia_urls:console_script',
            'download_and_extract=nemo_curator.scripts.download_and_extract:console_script',
            'text_cleaning=nemo_curator.scripts.text_cleaning:console_script',
            'add_id=nemo_curator.scripts.add_id:console_script',
            'get_metadata_from_corpus=nemo_curator.get_metadata_from_corpus:console_script',
            'make_data_shards=nemo_curator.scripts.make_data_shards:console_script',
            'prepare_fasttext_training_data=nemo_curator.scripts.prepare_fasttext_training_data:console_script',
            'train_fasttext=nemo_curator.scripts.train_fasttext:console_script',
            'filter_documents=nemo_curator.scripts.filter_documents:console_script',
            'separate_by_metadata=nemo_curator.scripts.separate_by_metadata:console_script',
            'prepare_task_data=nemo_curator.scripts.prepare_task_data:console_script',
            'find_matching_ngrams=nemo_curator.scripts.find_matching_ngrams:console_script',
            'remove_matching_ngrams=nemo_curator.scripts.remove_matching_ngrams:console_script',
            'gpu_compute_minhashes=nemo_curator.scripts.compute_minhashes:console_script',
            'minhash_buckets=nemo_curator.scripts.minhash_lsh:console_script',
            'jaccard_map_buckets=nemo_curator.scripts.map_buckets:console_script',
            'jaccard_shuffle=nemo_curator.scripts.jaccard_shuffle:console_script',
            'jaccard_compute=nemo_curator.scripts.jaccard_compute:console_script',
            'gpu_connected_component=nemo_curator.scripts.connected_components:console_script',
            'write_deduped_result_with_text=nemo_curator.gpu_deduplication.write_deduped_result_with_text:console_script',
            'verify_all_pairs_jaccard=nemo_curator.gpu_deduplication.verify_all_pairs_jaccard:console_script',
            'gpu_exact_dups=nemo_curator.scripts.find_exact_duplicates:console_script',
            'prepare_fuzzy_ids=nemo_curator.gpu_deduplication.prepare_fuzzy_ids:console_script',
            'create_list_of_duplicate_ids=nemo_curator.gpu_deduplication.create_list_of_duplicate_ids:console_script',
            'remove_duplicates=nemo_curator.gpu_deduplication.remove_duplicates:console_script',
            'deidentify=nemo_curator.scripts.find_pii_and_deidentify:console_script',
            'generate_statistics=nemo_curator.distributed_data_classification.generate_statistics:console_script',
            'domain_classifier_inference=nemo_curator.distributed_data_classification.domain_classifier_inference:console_script',
            'quality_classifier_multiple_models_inference=nemo_curator.distributed_data_classification.quality_classifier_multiple_models_inference:console_script',
            'quality_classifier_inference=nemo_curator.distributed_data_classification.quality_classifier_inference:console_script',
            'verify_results=nemo_curator.distributed_data_classification.verify_results:console_script',
        ],
    },
)
