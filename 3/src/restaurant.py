import datetime
import random

class Worker:
    def __init__(self) -> None:
        self.is_available = True
        self.name = None
        self.open_time = None
    def __init__(self, is_available: bool, name: str) -> None:
        self.is_available = is_available
        self.name = name
        self.open_time = None

    def schedule(self, open_time: datetime.datetime):
        self.open_time = open_time

class WorkerDatabase:
    def __init__(self) -> None:
        self.workers = list[Worker]
    
    def add_worker(self, worker: Worker):
        self.workers.append(worker)

    def get_all_workers(self) -> list[Worker]:
        return self.workers

class Restaurant:
    OWNER = Worker(True, "OWNER")

    def __init__(self) -> None:
        self.worker_database = WorkerDatabase()
        self.worker_database.add_worker(Worker(True, "AAA"))
        self.worker_database.add_worker(Worker(True, "BBB"))
        self.worker_database.add_worker(Worker(False, "CCC"))
        self.worker_database.add_worker(Worker(True, "DDD"))
        self.emergency_worker_database = WorkerDatabase()
        self.emergency_worker_database.add_worker(Worker(True, "EEE"))
        self.emergency_worker_database.add_worker(Worker(True, "FFF"))
        self.emergency_worker_database.add_worker(Worker(False, "GGG"))
        self.emergency_worker_database.add_worker(Worker(True, "HHH"))

    def is_available(self, worker: Worker) -> bool:
        return worker.is_available
    
    def get_emergency_workers(self) -> list[Worker]:
        return self.emergency_worker_database.get_all_workers()

    def find_workers_available_for_time(self, open_time: datetime.datetime):
        workers = self.worker_database.get_all_workers()
        available_workers = [worker for worker in workers if self.is_available(worker)]
        if available_workers:   # 可能なワーカーがいればそれを返す
            return available_workers
        emergency_workers = [
            worker for worker in self.get_emergency_workers() if self.is_available(worker)
        ]
        if emergency_workers:
            return emergency_workers
        return list[self.OWNER]

    def schedule_restaurant_open(self, open_time: datetime.datetime, workers_needed: int):
        workers = self.find_workers_available_for_time(open_time)
        # x人のシフトに入れる従業員からworkers_needed人を選ぶために
        # random.sampleを使う
        for worker in random.sample(workers, workers_needed):
            worker.schedule(open_time)