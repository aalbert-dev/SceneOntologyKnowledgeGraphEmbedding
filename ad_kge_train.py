import sys
from pykg2vec.utils.visualization import Visualization
from pykg2vec.data.kgcontroller import KnowledgeGraph
from pykg2vec.common import Importer, KGEArgParser
from pykg2vec.utils.trainer import Trainer
"""
@author Arjun Albert
@email  aalbert@mit.edu
@date   11/2/2020
@notes  Run designated model on autonomous driving scene
        ontology datasets. Designed for the visual genome
        dataset to run knowledge graph embeddings on for
        scene semantic understanding.
"""


"""
Get the knowledge graph and prepare the data for training.
Return the knowledge graph of the dataseted defined by commandline arguments.
"""
def get_knowledge_graph():
    knowledge_graph = KnowledgeGraph(dataset=args.dataset_name, custom_dataset_path=args.dataset_path)
    knowledge_graph.prepare_data()
    return knowledge_graph


"""
Get a model and model configuration.
Define the number of epochs we want to train for.
Return the model and model configuration objects.
"""
def get_model_and_config(ags):
    config_def, model_def = Importer().import_model_config(ags.model_name.lower())
    c = config_def(ags)
    config.epochs = 10
    m = model_def(**config.__dict__)
    return c, m


"""
Build and train the model on the datasets using the desired encoding.
Return the trained model and model configuration objects.
"""
def get_trained_model(c, m):
    trainer = Trainer(m, c)
    trainer.build_model()
    trainer.train_model()
    return c, m


"""
Publish the results as pdfs to the folder containing the datasets.
Also write the written test results to the same folder.
"""
def get_viz(c, m):
    viz = Visualization(model=m, config=c)
    viz.plot_train_result()
    viz.plot_test_result()


# Grab arguments from command line
args = KGEArgParser().get_args(sys.argv[1:])

# Get a knowledge graph from the desired arguments
knowlege_graph = get_knowledge_graph()

# Get a model and model configuration objects for the knowledge graph
config, model = get_model_and_config(args)

# Train the model using desired encoding
config, model = get_trained_model(config, model)

# Publish visualizations and write results
get_viz(config, model)
