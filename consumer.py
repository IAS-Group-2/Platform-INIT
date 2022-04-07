from kafka_manager.KafkaInit import Producer,Consumer

consumer = Consumer('test_consumer')
print(consumer.consume())