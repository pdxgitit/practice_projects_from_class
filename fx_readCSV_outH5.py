__author__ = 'Oliver'
import pandas as pd
import os


# filepaths stores all sub files with absolute path names
file_paths = []
base_dir = '/Users/Oliver/PyCharm/FX_app/data'
for folder, subs, files in os.walk(base_dir):
    for filename in files:
        if ".csv" in filename:
            file_paths.append(os.path.abspath(os.path.join(folder, filename)))

# loop through all .csv files and creat .h5 equivalents
for file_path in file_paths:
    h5_path = file_path[:-4] + ".h5"
    print ("Working on file at: {}").format(file_path)
    raw_input("Enter to start")

    # read into 10,000 rows per chunk, lazy generator, very fast
    file_reader = pd.read_csv(file_path, header=None, names=['Symbol', 'Date_time', 'Bid', 'Ask'],
                              index_col=['Date_time'], parse_dates=['Date_time'], chunksize=10000)

    # create  HDF5 with compression level 5 (0-9, 9 is extreme)
    h5_file = pd.HDFStore(h5_path, complevel=5, complib='blosc')

    # then write all records into hdf5 file
    # this will take a while ... but it emphasizes on re-usability across different IPython sessions
    i = 1
    for chunk in file_reader:
        h5_file.append('fx_tick_data', chunk, complevel=5, complib='blosc')
        print('Writing Chunk no.{}'.format(i))
        i += 1

    # check your hdf5 file, all 4,237,535 records are there
    print h5_file

    # close file IO
    h5_file.close()

# the advantage is that after you closing your current session,
# you can still read the file very quickly when you reopen another session

# reopen your IPython session
# data_h5 = '/media/Primary Disk/Jian_Python_Data_Storage.h5'
# h5_file = pd.HDFStore(data_h5)
#
# %time fx_df = h5_file['fx_tick_data']
# CPU times: user 1.93 s, sys: 439 ms, total: 2.37 s
# Wall time: 2.37 s
