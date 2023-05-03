# Understanding Mimicry in Butterflies from Images using Machine Learning

## Abstract

One of the central goals of evolutionary biology is to quantify the fine variation in adaptive traits, subject to natural selection, and to identify the causal genes. One system where natural selection can be characterized precisely are the tropical Heliconius butterflies. Two species, Heliconius erato and H. melpomene, both warn off predators with bold wing patterns and have evolved to resemble each other (mimicry). This thesis presents current work being done to expand machine learning (ML) algorithms to capture the biological mechanisms underlying mimicry in Heliconius butterflies. We apply an imageomics approach, which uses biology-guided ML to extract biological traits from images.

Traditionally, a common point of contact between biology and computer science is to use ML and computer vision to classify species. To go beyond species classification towards identifying biological traits that are common or different between mimic pairs requires restructuring ML models to consider biologically relevant information. We translate the biological question into computational abstractions in several ways.

First, we ask whether there is computationally detectable information from images in the similarity and difference of mimic pairs. Building upon previous work in this field, we use a convolutional neural network with triplet loss to create a latent embedding space, with different variations of the triplet chosen across species and co-mimic pairs. Pairwise comparisons across subspecies show that traditionally hypothesized co-mimics are significantly closer to each other in the embedding than are other subspecies pairs, providing a positive answer to our question.

Having identified the pattern elements central to mimicry, we leverage biological knowledge of wing pattern development to link phenotypic variation with specific genotypes. The need to place landmarks manually is a common limitation of biological morphometric studies: here, we automate this process using ML-morph, an algorithm for automated detection and landmarking of biological structures in images. Once we have the landmark-based transformations to superimpose images, color pattern variation in their expression can be studied using patternize, an R package that defines homology across specimens through fixed landmarks that correspond to fine anatomical features of butterfly wings. Using embedding space transformations on the representations of the color patterns obtained, as input to a Genome-Wide Association Studies (GWAS), the specific gene sequence can be associated with the corresponding color pattern variation, thereby connecting phenotype to genotype.

The big biological question of connecting phenotype to genotype shapes the future direction of this research. Future work could explore how to design a Convolutional Neural Network (CNN) to be able to automatically identify the gene sequence associated with phenotypic variation by using these values as a continuous class. This will result in the creation of new research directions in the emerging field of biological knowledge-guided machine learning.



## Cuthill dataset

- Code used for classification experiments on Cuthill dataset with all triplet constraints
- Custom 15 layer CNN + triplet loss
- Refer to metadata for files used within code
- 24 subspecies, 12 mimic pairs

## Jiggins dataset

- Code used for classification experiments on Jiggins dataset  
- ResNet50 + ArcFace Loss
- 18 subspecies, 9 mimic pairs 
- Also contains code used for classification experiments on Jiggins dataset using bird and butterfly acuity
- Refer to https://github.com/eleanorcaves/AcuityView to calculate acuity images
- Kingfisher acuity used for birds and Lepidoptera parthenos sylvia used
- Results on these experiments can be found in corresponding folders

## Landmarking

- Code for automating the placement of landmarks on the wings of butterflies 

- Refer to https://github.com/agporto/WingSeg for segmenting forewings and hindwings into quadrants

- Refer to https://github.com/agporto/ml-morph for file structure for using ml-morph code

- Further analysis landmark-wise and image-wise can be done using ml_morph_analysis_AP.ipynb
