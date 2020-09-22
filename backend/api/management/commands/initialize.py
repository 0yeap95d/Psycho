from pathlib import Path
import pandas as pd
from django.core.management.base import BaseCommand
from backend import settings
from api import models


class Command(BaseCommand):
    help = "initialize database"
    DATA_DIR = Path(settings.BASE_DIR).parent.parent / "data"
    DATA_FILE = str(DATA_DIR / "dump.pkl")

    def _load_dataframes(self):
        try:
            data = pd.read_pickle(Command.DATA_FILE)
        except:
            print(f"[-] Reading {Command.DATA_FILE} failed")
            exit(1)
        return data

    def _initialize(self):
        """
        Sub PJT 1에서 만든 Dataframe을 이용하여 DB를 초기화합니다.
        """
        print("[*] Loading data...")
        dataframes = self._load_dataframes()

        print("[*] Initializing stores...")
        models.Store.objects.all().delete()
        stores = dataframes["stores"]
        stores_bulk = [
            models.Store(
                id=store.id,
                store_name=store.store_name,
                branch=store.branch,
                area=store.area,
                tel=store.tel,
                address=store.address,
                latitude=store.latitude,
                longitude=store.longitude,
                category=store.category,
            )
            for store in stores.itertuples()
        ]
        models.Store.objects.bulk_create(stores_bulk)

        print("[*] Initializing reviews...")
        models.Review.objects.all().delete()
        reviews = dataframes["reviews"]
        reviews_bulk = [
            models.Review(
                rid=review.rid,
                store=review.store,
                user=review.user,
                score=review.score,
                content=review.content,
                reg_time=review.reg_time,
            )
            for review in reviews.itertuples()
        ]
        models.Review.objects.bulk_create(reviews_bulk)

        print("[*] Initializing hotels...")
        models.Hotel.objects.all().delete()
        hotels = dataframes["hotels"]
        hotels_bulk = [
            models.Hotel(
                id=hotel.id,
                tel=hotel.tel,
                address1=hotel.address1,
                address2=hotel.address2,
                name=hotel.name,
                latitude=hotel.latitude,
                longitude=hotel.longitude,
            )
            for hotel in hotels.itertuples()
        ]
        models.Hotel.objects.bulk_create(hotels_bulk)

        print("[+] Done")

    def handle(self, *args, **kwargs):
        self._initialize()
