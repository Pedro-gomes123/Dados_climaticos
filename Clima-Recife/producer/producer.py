from kafka import kafkaproducer
import json
from time import sleep
from enum import Enum
import os 

topic = 'app'

producer = kafkaproducer.kafkaProducer(bootstrap_servers='localhost:9092')