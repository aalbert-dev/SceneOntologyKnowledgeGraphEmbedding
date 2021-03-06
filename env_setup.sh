# author Arjun Albert
# email aalbert@mit.edu
echo "Starting setup."
mkdir ~/Desktop/ad_kge
cd ~/Desktop/ad_kge

read "Ctrl + C if you don't want to download py2kg env. Press [Enter] if you would like to continue."

conda create --name pykg2vec python=3.6
conda activate pykg2vec
conda install pytorch torchvision cudatoolkit=10.1 -c pytorch
conda install pytorch torchvision cpuonly -c pytorch
git clone https://github.com/Sujit-O/pykg2vec.git

read "Ctrl + C if you don't want to create dirs. Press [Enter] if you would like to continue."

cd pykg2vec
mkdir scene_data_1
mkdir scene_data_2
mkdir scene_data_3
touch scene_data_1/ad_scene_relationships-test.txt
touch scene_data_1/ad_scene_relationships-train.txt
touch scene_data_1/ad_scene_relationships-valid.txt
touch scene_data_2/ad_scene_relationships-test.txt
touch scene_data_2/ad_scene_relationships-train.txt
touch scene_data_2/ad_scene_relationships-valid.txt
touch scene_data_3/ad_scene_relationships-test.txt
touch scene_data_3/ad_scene_relationships-train.txt
touch scene_data_3/ad_scene_relationships-valid.txt
python setup.py install

echo "test install using: train TransE using benchmark dataset fb15k"
echo "Download the 3 datasets from: https://visualgenome.org/api/v0/api_home.html"
echo "Place them in a folder called: scenes"
echo "Remember: x for 1, 2, 3"
echo "Rename them: relationships_x.json"
echo "Structure should be as follows: 
/ad_kge/
    /pykg2vec/
        /scene_data_x/
            /ad_scene_relationships-test.txt
            /ad_scene_relationships-train.txt
            /ad_scene_relationships-valid.txt
    /scenes/
        /relationships_x.json"
read "Press [Enter] if you would like to continue."
echo "Then cd to ad_kge and run run_all_models.sh"
echo "This will build all the scene data and train four different knowledge graph embedding models on two sets of autonomous driving data."
