from __future__ import annotations

from typing import Callable


class KafkaIngestor:
    def __init__(self, bootstrap_servers: list[str], topic: str) -> None:
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic

    def produce(self, key: bytes, value: bytes) -> None:
        """Produce a message to Kafka. Implement actual Kafka producer in future."""
        raise NotImplementedError("Kafka producer integration is not yet implemented.")


class MQTTIngestor:
    def __init__(self, broker_url: str, topic: str) -> None:
        self.broker_url = broker_url
        self.topic = topic

    def publish(self, payload: bytes) -> None:
        """Publish a payload to MQTT. Implement actual MQTT client in future."""
        raise NotImplementedError("MQTT publisher integration is not yet implemented.")


class IngestionPipeline:
    def __init__(self, source: str, processor: Callable[[bytes], None]) -> None:
        self.source = source
        self.processor = processor

    def start(self) -> None:
        """Start ingestion from the configured source."""
        raise NotImplementedError("Ingestion pipeline implementation is pending.")
