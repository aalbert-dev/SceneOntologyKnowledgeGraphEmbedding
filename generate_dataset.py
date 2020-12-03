import os.path
import sys
import json
import random
"""
@author Arjun Albert
@email  aalbert@mit.edu
@date   11/2/2020
@notes  Generate training, test, and validation datasets from
        Visual Genome scene ontology dataset for knowledge
        graph embedding for scene semantic understanding.
"""

"""
Convert a tuple representation of a head, relationship, tail triple into a string.
Returns the string representation of the triple.
"""
def get_triple_as_string(h, r, t):
    return h + "\t" +  r + "\t" + t + "\n"


"""
Checks if a relationship json object has the proper subject, object, predicate 
(relationship) fields required to form a head, relation, tail triple.
Returns true if the input json had proper fields, false otherwise.
"""
def check_valid_relationship(rel):
    if "subject" not in rel:
        return False
    if "predicate" not in rel:
        return False
    if "object" not in rel:
        return False
    return True


"""
Gets an objects name from each databases json object representation.
Returns the object name string regardless of database versions object.
"""
def get_object_name(obj):
    if "names" in obj:
        return obj["names"][0]
    if "name" in obj:
        return obj["name"]
    return None


"""
Gets a subjects name from each databases json subject representation.
Returns the subject name string regardless of database versions subject.
"""
def get_subject_name(sbj):
    if "names" in sbj:
        return sbj["names"][0]
    if "name" in sbj:
        return sbj["name"]
    return None


"""
Imports the json data from each of the visual genomes datasets.
Adds the relationships (h, r, t) for each dataset by scene to
the it's respective dataset.
"""
def import_datasets(set1, set2, set3):
    if set1:
        print("Importing dataset 1.")
        with open(os.path.join(sys.path[0], "scenes", "relationships_1.json"), 'r') as f:
            scenes = json.loads(f.read())
            for scene in scenes:
                scene_id = scene["image_id"]
                if scene_id not in dataset_1:
                    dataset_1[scene_id] = []
                relationships = scene["relationships"]
                for relationship in relationships:
                    if check_valid_relationship(relationship):
                        h = get_subject_name(relationship["subject"])
                        r = relationship["predicate"]
                        t = get_object_name(relationship["object"])
                        dataset_1[scene_id].append((h, r, t))

    if set2:
        print("Importing dataset 2.")
        with open(os.path.join(sys.path[0], "scenes", "relationships_1.json"), 'r') as f:
            scenes = json.loads(f.read())
            for scene in scenes:
                scene_id = scene["image_id"]
                if scene_id not in dataset_2:
                    dataset_2[scene_id] = []
                relationships = scene["relationships"]
                for relationship in relationships:
                    if check_valid_relationship(relationship):
                        h = get_subject_name(relationship["subject"])
                        r = relationship["predicate"]
                        t = get_object_name(relationship["object"])
                        dataset_2[scene_id].append((h, r, t))

    if set3:
        print("Importing dataset 3.")
        with open(os.path.join(sys.path[0], "scenes", "relationships_1.json"), 'r') as f:
            scenes = json.loads(f.read())
            for scene in scenes:
                scene_id = scene["image_id"]
                if scene_id not in dataset_3:
                    dataset_3[scene_id] = []
                relationships = scene["relationships"]
                for relationship in relationships:
                    if check_valid_relationship(relationship):
                        h = get_subject_name(relationship["subject"])
                        r = relationship["predicate"]
                        t = get_object_name(relationship["object"])
                        dataset_3[scene_id].append((h, r, t))


"""
Split the a relationship in a dataset randomly between training, test, and validation.
Returns the modified training, test, or validation datasets.
"""
def split_dataset(tr, te, va, rel):
    h, r, t = rel
    s = get_triple_as_string(h, r, t)
    i = random.randint(0, 2)
    if i == 0:
        tr += s
    elif i == 1:
        te += s
    else:
        va += s
    return tr, te, va


"""
Input training, test, validation data, and a dataset number to write to.
Write the training, test, and validation data to the proper directories.
"""
def write_datasets(tr, te, va, i):
    with open(os.path.join(sys.path[0], "pykg2vec", "scene_data_" + str(i), "ad_scene_relationships-train.txt"), 'w') as f:
        f.write(tr)
    with open(os.path.join(sys.path[0], "pykg2vec", "scene_data_" + str(i), "ad_scene_relationships-test.txt"), 'w') as f:
        f.write(te)
    with open(os.path.join(sys.path[0], "pykg2vec", "scene_data_" + str(i), "ad_scene_relationships-valid.txt"), 'w') as f:
        f.write(va)


"""
Label a relationships head and tail with an arbitrary prefix.
Return the new head and tail strings in the triple.
"""
def label_relationship(rel, pfx):
    h, r, t = rel
    return pfx + h, r, pfx + t


"""
Decide proper ratio to split training, test, and validation data into.
Also downsample the training data with ratio 1 : downsampling.
Gather triples from memory and then writeout each dataset.
Will overwrite previously filled out datasets with new datasets 
even if they are not included or are empty.
"""
def export_data_for_training(downsampling, testing_limit):
    print("Exporting datasets for training.")
    max_test = testing_limit
    keys = dataset_1.keys()
    train_1, test_1, valid_1 = "", "", ""
    relationship_count = 0
    for key in keys:
        for rel in dataset_1[key]:
            if relationship_count % downsampling == 0:
                c = random.randint(0, 10)
                h, r, t = rel
                s = get_triple_as_string(h, r, t)
                if c < 8:
                    train_1 += s
                elif c < 9:
                    if len(valid_1.split("\n")) < max_test:
                        valid_1 += s
                else:
                    if len(test_1.split("\n")) < max_test:
                        test_1 += s
            relationship_count += 1
    write_datasets(train_1, test_1, valid_1, 1)

    keys = dataset_2.keys()
    train_2, test_2, valid_2 = "", "", ""
    relationship_count = 0
    for key in keys:
        for rel in dataset_2[key]:
            if relationship_count % downsampling == 0:
                c = random.randint(0, 10)
                h, r, t = rel
                s = get_triple_as_string(h, r, t)
                if c < 8:
                    train_2 += s
                elif c < 9:
                    if len(valid_2.split("\n")) < max_test:
                        valid_2 += s
                else:
                    if len(test_2.split("\n")) < max_test:
                        test_2 += s
            relationship_count += 1
    write_datasets(train_2, test_2, valid_2, 2)

    keys = dataset_3.keys()
    train_3, test_3, valid_3 = "", "", ""
    relationship_count = 0
    for key in keys:
        for rel in dataset_3[key]:
            if relationship_count % downsampling == 0:
                c = random.randint(0, 10)
                h, r, t = rel
                s = get_triple_as_string(h, r, t)
                if c < 8:
                    train_3 += s
                elif c < 9:
                    if len(valid_3.split("\n")) < max_test:
                        valid_3 += s
                else:
                    if len(test_3.split("\n")) < max_test:
                        test_3 += s
            relationship_count += 1
    write_datasets(train_3, test_3, valid_3, 3)
    print("Done.")

# Store scene ontology relationships for each dataset
dataset_1 = {}
dataset_2 = {}
dataset_3 = {}

# Load dataset 1, dataset 2, dataset 3 into memory and format them
import_datasets(True, True, True)

# Export data downsampled by 100x for training, test, and validation
# Set a max length of 4000 relations each for testing and validation
export_data_for_training(50, 4000)
