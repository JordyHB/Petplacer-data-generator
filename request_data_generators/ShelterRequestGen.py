import random
import requests
import concurrent.futures

from helpers.utils import *
from pathlib import Path


class ShelterRequestGen:
    # Get the absolute path of the project's root directory
    ROOT_DIR = Path(__file__).parent.parent.resolve()
    SHELTER_DATA_DIR = ROOT_DIR / "dummy_data_textfiles" / "shelter"
    SHELTER_NAME_DIR = SHELTER_DATA_DIR / "sheltername"

    def __init__(self, app_state):
        # reference to the app state
        self.app_state = app_state
        # place to store the data in memory
        self.shelter_name_data = None
        self.street_name_data = None
        self.city_data = None
        self.facilities_data = None
        self.description_data = None
        # keeps track of used shelter names
        self.used_shelter_names = set()

    def preload_data_into_mem(self):
        # Preloads the sheltername data
        self.shelter_name_data = {
            "chunks_1": load_file_into_mem(self.SHELTER_NAME_DIR / "chunk_1.txt"),
            "chunks_2": load_file_into_mem(self.SHELTER_NAME_DIR / "chunk_2.txt"),
            "chunks_3": load_file_into_mem(self.SHELTER_NAME_DIR / "chunk_3.txt"),
        }
        # preloads the streetname data
        self.street_name_data = load_file_into_mem(self.SHELTER_DATA_DIR / "streetnames.txt")
        # preloads the city data
        self.city_data = load_file_into_mem(self.SHELTER_DATA_DIR / "cities.txt")
        # preloads the facilities data
        self.facilities_data = load_file_into_mem(self.SHELTER_DATA_DIR / "facilities.txt")
        # preloads description data
        self.description_data = load_file_into_mem(self.SHELTER_DATA_DIR / "descriptions.txt")

    # TODO Website gen

    # TODO opening hours gen

    # TODO create facilities function

    def get_random_shelter_name(self):
        # keeps track of how large the set is before attempting to add something
        current_set_len = len(self.used_shelter_names)
        # creates a string with a random chunk from each list
        shelter_name = \
            f"{random.choice(self.shelter_name_data['chunks_1'])} " \
            f"{random.choice(self.shelter_name_data['chunks_2'])} " \
            f"{random.choice(self.shelter_name_data['chunks_3'])}"
        # attempts to add it to the set
        self.used_shelter_names.add(shelter_name)
        # Checks if it got successfully added, if so returns it
        if len(self.used_shelter_names) > current_set_len:
            return shelter_name
        # If not goes for another try at generating a unique name
        else:
            return self.get_random_shelter_name()

    def get_random_address(self):
        # Adds a number to a street
        random_street = random.choice(self.street_name_data)
        address = f"{random_street} {random.randint(1, 150)}"
        return address

    def build_request(self):
        request_dict = {}

        request_dict["shelterName"] = self.get_random_shelter_name()
        request_dict["phoneNumber"] = gen_dummy_phone_number()
        request_dict["email"] = gen_dummy_email(request_dict['shelterName'])
        request_dict["address"] = self.get_random_address()
        request_dict["city"] = random.choice(self.city_data)
        request_dict["postalCode"] = gen_dummy_postalcode()
        request_dict["description"] = random.choice(self.description_data)
        request_dict["website"] = "https://www.example.com"
        request_dict["facilities"] = "Facility 1, Facility 2, Facility 3"
        request_dict["openingHours"] = "Monday to Friday: 9am to 5pm"

        return request_dict

    def post_requests(self, amount_of_requests):
        with requests.Session() as session:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                # Submit all requests to the executor
                futures = [executor.submit(
                    session.post,
                    url=f"{self.app_state.base_url}/users/admin/shelters",
                    json=self.build_request(),
                    headers={
                        'Content-Type': 'application/json',
                        "Authorization": f"Bearer {self.app_state.token}"
                    }
                ) for _ in range(amount_of_requests)]

                # Wait for results and print them
                for future in concurrent.futures.as_completed(futures):
                    response = future.result()
                    print(response.status_code)
                    print(response.content)


