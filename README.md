# Vibe

A deep learning music platform

## Things to do

#### Backend
* Create backend dataflow to pull mp3 and metadata from spotify api to a local dir
* Run data collection on enough playlists to gather ~10k songs
* Convert all mp3s into spectograms and save them locally
* Train a deep convolutional autoencoder on spectograms to generate ml encodings
* Store encodings and metadata in DB (SQL/SPARK/etc.)
* Run basic clustering on only spotify metadata 
* Run clustering on only spectograms and combined to see best results

#### Frontend
* TBD


### Installing

Current backend environment setup

```
pip install spotipy
pip install keras
pip install tensorflow
```


## Running backend script

```
python3 data_collection.py
```



## Deployment

TBD



## Authors

* [**Ritwik Biswas**](https://github.com/ritwikbiswas)

* [**Trever Cullen**](https://github.com/iamttc)



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
