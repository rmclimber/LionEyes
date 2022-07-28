# LionEyes

## Introduction
The genesis of this project was my sister's face-to-face encounter with a cougar
outside her home in the Sierra Nevada foothills. (The cougar was killing two of
her baby goats.) She was unhurt, but the cougar was never successfully found. 
I thought how convenient it would be if she had a system which would alert her
and her family (including a teenager and an infant) to the presence of a cougar 
on her property, allowing them to avoid contact and alert wildlife authorities
to the presence of the animal. As a newcomer to machine learning and software 
engineering, this seemed like a useful project to develop. 

In broad strokes, my plan is to create an end-to-end ML project using computer
vision to classify inputs from security and game cameras as containing (or not
containing) a mountain lion. (For the non-native English speakers, 'mountain
lion', 'cougar', and 'puma' are all synonyms and the colloquial terms for
*Puma concolor*.) 

Below, I outline the planned phases of the project. I will revise these as my
knowledge base expands. 

After completion of each phase, I also intend to write a short analysis of the
work: the approach taken, successes and failures, etc. 

## Phase 1: data acquisition and preparation (current phase)

### Phase 1.1: data source selection (complete)

For my data, I intend to use cougar observations from the citizen science
platform [iNaturalist](https://www.inaturalist.org/), which allows users 
worldwide to upload photographs and audio recordings of organisms in the wild. 
One can find observations from every macroscopic kingdom of life. The platform
has its own impressive image classification technology, and I commend it to the
biologically-interested reader[^1]. 

iNaturalist observations are available for download via the Global
Biodiversity Information Facility's [iNaturalist dataset](https://www.gbif.org/dataset/50c9509d-22c7-4a22-a47d-8c48425ef4a7).

### Phase 1.2: data acquisition (current phase)

Naturally, I need two types of data: images of cougars and images of
not-cougars. For the time being, my negative examples will primarily be other
medium-to-large mammals found locally: deer, foxes, bobcats, bears, and coyotes.

### Phase 1.3: data preparation

Unluckily for my purposes, the iNaturalist observations include not only images
of cougars, but images of cougar spoor: scat, tracks, etc. At this stage in the
project, I have little interest in scat classification, so I need to find a way
to tag all \~5k images as containing an animal or containing spoor. 

## Phase 2: building and training the model
## Phase 3: building a GUI for practical use
## Phase 4: adding video 
## Phase 5: adding live monitoring
## Phase 6: adding push notifications
## Phase 7: deployment to cloud
## Phase 8: add additional predators
## Resources
This project is only my second large project outside of academic coursework, so
my plan is to use it to explore every stage of using machine learning for
research and production. (Is this MLOPs? Maybe. I haven't figured it out yet.)
Here are some of the main resources I am using to learn how to do
everything:

- Géron's *Hands-On Machine Learning with Scikit-learn, Keras, and TensorFlow* from O'Reilly.
- Forsyth's *Computer Vision* from Pearson.
- Szeliski's *Computer Vision: Algorithms and Applications* from Springer.

## Citations
- iNaturalist contributors, iNaturalist (2022). iNaturalist Research-grade Observations. iNaturalist.org. Occurrence dataset https://doi.org/10.15468/ab3s5x accessed via GBIF.org on 2022-05-10.

[^1]: If you'd like to explore my own activity on iNaturalist, [here is my profile](https://www.inaturalist.org/people/tkatka).