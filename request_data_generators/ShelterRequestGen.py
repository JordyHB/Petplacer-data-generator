from helpers.utils import load_file_into_mem

import os


class ShelterRequestGen:
    SHELTER_DATA_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the directory where your script is
    SHELTER_NAME_DIR = os.path.join(SHELTER_DATA_DIR, "..", "dummy_data_textfiles", "shelter", "sheltername")

    # place to store the data in memory
    shelter_name_data = {}

    def __init__(self):
        pass

    @classmethod
    def preload_data_into_mem(cls):
        cls.shelter_name_data["chunks_1"] = load_file_into_mem(os.path.join(cls.SHELTER_DATA_DIR, "chunk_1.txt"))
        cls.shelter_name_data["chunks_2"] = load_file_into_mem(os.path.join(cls.SHELTER_DATA_DIR, "chunk_2.txt"))
        cls.shelter_name_data["chunks_3"] = load_file_into_mem(os.path.join(cls.SHELTER_NAME_DIR, "chunk_3.txt"))
        print(cls.shelter_name_data)
