echo "Generating files for training."
python generate_dataset.py

echo "Got files for training."
ls pykg2vec/scene_data_1
ls pykg2vec/scene_data_2
ls pykg2vec/scene_data_3

echo "Starting TransE on dataset 1."
python ad_kge_train.py -mn TransE -ds ad_scene_relationships -dsp ~/Desktop/ad_kge/pykg2vec/pykg2vec/scene_data_1/
echo "Starting TransH on dataset 1."
python ad_kge_train.py -mn TransH -ds ad_scene_relationships -dsp ~/Desktop/ad_kge/pykg2vec/pykg2vec/scene_data_1/
echo "Starting Rescal on dataset 1."
python ad_kge_train.py -mn Rescal -ds ad_scene_relationships -dsp ~/Desktop/ad_kge/pykg2vec/pykg2vec/scene_data_1/
echo "Starting HoLE on dataset 1."
python ad_kge_train.py -mn HoLE -ds ad_scene_relationships -dsp ~/Desktop/ad_kge/pykg2vec/pykg2vec/scene_data_1/

echo "Starting TransE on dataset 2."
python ad_kge_train.py -mn TransE -ds ad_scene_relationships -dsp ~/Desktop/ad_kge/pykg2vec/pykg2vec/scene_data_2/
echo "Starting TransH on dataset 2."
python ad_kge_train.py -mn TransH -ds ad_scene_relationships -dsp ~/Desktop/ad_kge/pykg2vec/pykg2vec/scene_data_2/
echo "Starting Rescal on dataset 2."
python ad_kge_train.py -mn Rescal -ds ad_scene_relationships -dsp ~/Desktop/ad_kge/pykg2vec/pykg2vec/scene_data_2/
echo "Starting HoLE on dataset 2."
python ad_kge_train.py -mn HoLE -ds ad_scene_relationships -dsp ~/Desktop/ad_kge/pykg2vec/pykg2vec/scene_data_2/
echo "Done."
