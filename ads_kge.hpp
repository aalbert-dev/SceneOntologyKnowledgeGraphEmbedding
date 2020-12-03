#include "json/single_include/nlohmann/json.hpp"
#include <fstream>
#include <iostream>

/**
 * author   Arjun Albert
 * email    aalbert@mit.edu
 * date     11/26/2020
**/

// json namespace
using json = nlohmann::json;

// use the scene.json file as data
std::string scene_data_file_name = "scene.json";

// store all the scene descriptions
std::vector<std::string> descriptions;

// store the scene descriptions in ordered form
std::vector<std::vector<std::string>> multi_level_descriptions;

// store the scene entities as strings
std::vector<std::string> entities;

// store the scene relationships as strings
std::vector<std::string> relationships;

// define possible entity relations
std::string all_entities[] {"with", "before", "after", "none", "self"};


// define custom structure to hold entities and relations for an adjacency matrix graph representation knowledge graph embedding
struct labelledAdjacencyGraph{
    std::string name;
    std::vector<std::string> headers;
    std::vector<std::vector<std::string>> adjacency_matrix;
    std::vector<std::string> values;
};


/*
 * Add all relationships to relationship data structure.
 */
inline void define_relationships()
{
    for (std::string entity: all_entities){
        relationships.push_back(entity);
    }
}


/*
 * Get the level of an entity based on the order of the entity in the structure.
 * Returns the entity level or -1 if it does not exist in the structure. 
 */
inline int get_entity_level(std::string target_entity)
{
    int i = 0;
    for (i; i < descriptions.size(); i++){
        for (std::string entity: multi_level_descriptions[i]){
            if (target_entity.compare(entity) == 0){
                return i;
            }
        }
    }
    return -1;
}


/*
 * Find the relationship between two entities based on their level in the structure.
 * Also check if the entities are the same or not related. 
 * Returns the relationship between entity 1 and entity 2.
 */
inline std::string get_relationship(std::string entity_1, std::string entity_2)
{
    int entity_1_level = get_entity_level(entity_1);
    int entity_2_level = get_entity_level(entity_2);

    if (entity_1.compare(entity_2) == 0){
        return all_entities[4];
    }
    if (entity_1_level < 0 || entity_2_level < 0){
        return all_entities[3];
    }

    if (entity_1_level == entity_2_level){
        return all_entities[0];
    }else if (entity_1_level < entity_2_level){
        return all_entities[1];
    }else{
        return all_entities[2];
    }
}


/*
 * Calculate the adjacency matrix graph representation by finding the relationships between
 * every entity in the scene.
 * The adjacency matrix is a   
 */
inline std::vector<std::vector<std::string>> calculate_adjacency_matrix(){
    std::vector<std::vector<std::string>> adjacency_matrix;
    for (std::string s1: entities){
        std::vector<std::string> matrix_row;
        for (std::string s2: entities){
            std::string relation = get_relationship(s1, s2);
            matrix_row.push_back(relation);
        }
        adjacency_matrix.push_back(matrix_row);
    }
    return adjacency_matrix;
}


/*
 * Add entities and relations between entities to knowledge graph adjacency matrix representation using'
 * the defined labelledAdjacencyGraph structure.
 * Returns the labelledAdjacencyGraph with entities and relations. 
 */
inline labelledAdjacencyGraph form_knowledge_graph()
{
    labelledAdjacencyGraph non_embedded_knowledge_graph;
    non_embedded_knowledge_graph.name = "Non embedded";
    non_embedded_knowledge_graph.headers = entities;
    for (std::string value: all_entities){
        non_embedded_knowledge_graph.values.push_back(value);
    }
    non_embedded_knowledge_graph.adjacency_matrix = calculate_adjacency_matrix();
    return non_embedded_knowledge_graph;
}