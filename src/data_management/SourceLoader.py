import importlib
from multiprocessing.pool import ThreadPool
from src.data_management.database.Source import Source

loaded_sources = []
pool = ThreadPool()


def connect_to_source(source: Source) -> None:
    """ Creates worker for source script if not already existing """
    if source in loaded_sources:
        return
    script = importlib.import_module('scripts.default.' + source.script.rsplit('/')[0])
    pool.apply_async(script.run, args=(source.get_write_function,))


def terminate():
    pool.terminate()
    pool.join()
