#!/usr/bin/env python

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
class teacher(User):
    def __init__(self, first_name, last_name):
        super.__init__(self, first_name, last_name)
            
class student(User):
    def __init__(self, first_name, last_name):
        super.__init__(self, first_name, last_name)