#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="fido", breed="Corgi"):
        self.name =  name
        self.breed = breed

    def set_name(self, name):
        if(type(name) == str) and (0 < len(name) < 26):
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.") 
    def set_breed(self,breed):
        if (breed in APPROVED_BREEDS):
            self._breed = breed
        else:
            print('Breed must be in list of approved breeds.')
    def get_breed(self):
        return self._breed
    def get_name(self):
        return self._name
    name = property(get_name,set_name)
    breed = property(get_breed, set_breed)
