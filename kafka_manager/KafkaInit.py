from kafka import KafkaProducer
from kafka.errors import KafkaError
from kafka import KafkaConsumer
import config.config as config

class Producer:
    def __init__(self,topic):
        """
        Initialize the Kafka Producer
        topic : consumer's topic
        """
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers=[config.KAFKA_VM_IP+":"+config.KAFKA_VM_PORT])

    def send_message(self,message):
        try:
            self.producer.send(self.topic,message.encode('utf-8'))
            self.producer.flush()
        except KafkaError as e:
            print(e)

    def close(self):
        self.producer.close()

class Consumer:
    def __init__(self,topic):
        self.topic = topic
        self.consumer = KafkaConsumer(self.topic,bootstrap_servers=[config.KAFKA_VM_IP+":"+config.KAFKA_VM_PORT])

    def consume(self):
        data = []
        for message in self.consumer:
            data.append(message)
        return data
    
    def close(self):
        self.consumer.close()