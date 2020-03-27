
DATA_FOLDER = '/home/palonso/models/essentia_embeddings/musicnn_msd_lda/'  # set your data folder
config_preprocess = {
    'mtt_spec': {
        'identifier': 'mtt',                      # name for easy identification
        'audio_folder': '/home/jpons/audio/mtt/', # end it with / -> this is an absolute path!
        'n_machines': 1,                          # parallelizing this process through 'n_machines'
        'machine_i': 0,                           # id number of the machine which is running this script (from 0 to n_machines-1)
        'num_processing_units': 20,               # number of parallel processes in every machine
        'type': 'time-freq',                      # kind of audio representation: 'time-freq' (only recommended option)
        'spectrogram_type': 'mel',                # 'mel' (only option) - parameters below should change according to this type
        'resample_sr': 16000,                     # sampling rate (original or the one to be resampled)
        'hop': 256,                               # hop size of the STFT
        'n_fft': 512,                             # frame size (number of freq bins of the STFT)
        'n_mels': 96,                             # number of mel bands
        'index_file': 'index/mtt/index_mtt.tsv',  # list of audio representations to be computed
    },
    'msd_spec': {
        'identifier': 'msd',                      # name for easy identification
        'audio_folder': '/home/jpons/audio/MSD/millionsong-audio/mp3/', # end it with / -> this is an absolute path!
        'n_machines': 1,                          # parallelizing this process through 'n_machines'
        'machine_i': 0,                           # id number of the machine which is running this script (from 0 to n_machines-1)
        'num_processing_units': 20,               # number of parallel processes in every machine
        'type': 'time-freq',                      # kind of audio representation: 'time-freq' (only recommended option)
        'spectrogram_type': 'mel',                # 'mel' (only option) - parameters below should change according to this type
        'resample_sr': 16000,                     # sampling rate (original or the one to be resampled)
        'hop': 256,                               # hop size of the STFT
        'n_fft': 512,                             # frame size (number of freq bins of the STFT)
        'n_mels': 96,                             # number of mel bands
        'index_file': 'index/msd/index_msd.tsv',  # list of audio representations to be computed
    }
}

# DATASET = 'mtt'
DATASET = 'msd'

config_train = {
    'spec': {
        'name_run': '',
        # which data?
        'audio_representation_folder': 'audio_representation/'+DATASET+'__time-freq/',
        'gt_train': 'train_gt_'+DATASET+'.tsv',
        'gt_val': 'val_gt_'+DATASET+'.tsv',

        # input setup?
        'n_frames': 187,                          # length of the input (integer)
        'pre_processing': 'logC',                 # 'logEPS', 'logC' or None
        'pad_short': 'repeat-pad',                # 'zero-pad' or 'repeat-pad'
        'train_sampling': 'random',               # 'overlap_sampling' or 'random'. How to sample patches from the audio?
        'param_train_sampling': 1,                # if mode_sampling='overlap_sampling': param_sampling=hop_size
                                                  # if mode_sampling='random': param_sampling=number of samples
        # learning parameters?
        'model_number': 15,                       # number of the model as in models.py
        'load_model': None,                       # set to None or absolute path to the model
        'epochs': 120,                            # maximum number of epochs before stopping training
        'batch_size': 32,                         # batch size during training
        'weight_decay': 1e-5,                     # None or value for the regularization parameter
        'learning_rate': 0.001,                   # learning rate
        'optimizer': 'Adam',                      # 'SGD_clip', 'SGD', 'Adam'
        'patience': 75,                           # divide by two the learning rate after the number of 'patience' epochs (integer)
        'lambda': 1.0,                            # lambda for reversal gradient models
        'discriminator_dimensions': 12,
        'mfcc_max':  39.399,
        'mfcc_min': -26.740,
        # 'mfcc_max':  2.,
        # 'mfcc_min': -2.,
        'mfcc_headroom': 0.1,

        # experiment settings?
        'num_classes_dataset': 50,
        'val_batch_size': 32
    }
}
