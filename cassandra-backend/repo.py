from peewee import SqliteDatabase, Model, CharField, IntegerField, DateField, PrimaryKeyField, FloatField


db = SqliteDatabase('products.db')

class InternetPackages(Model):
    id = PrimaryKeyField()
    package_name = CharField()
    days_available = IntegerField()
    price = IntegerField()
    data_size_in_mb = IntegerField()
    vendor = CharField()
    number_of_purchases = IntegerField()
    price_per_mb = FloatField(null=True, default=price/data_size_in_mb)
    
    class Meta:
        database = db
        

if __name__ == "__main__":
    db.connect()
    db.create_tables([InternetPackages])
    
    InternetPackages.create(package_name='2.5gb daily', days_available=1, price=12600, data_size_in_mb=2500, vendor='Irancell', number_of_purchases=20)
    InternetPackages.create(package_name='750mb 3 days', days_available=3, price=9000, data_size_in_mb=750, vendor='Irancell', number_of_purchases=20)
    InternetPackages.create(package_name='5gb 7 days', days_available=7, price=24200, data_size_in_mb=5000, vendor='Irancell', number_of_purchases=20)
    InternetPackages.create(package_name='7gb 30 days', days_available=30, price=38000, data_size_in_mb=7000, vendor='Irancell', number_of_purchases=20)
    InternetPackages.create(package_name='10gb 60 days', days_available=60, price=48500, data_size_in_mb=10000, vendor='Irancell', number_of_purchases=20)
    InternetPackages.create(package_name='15gb 120 days', days_available=120, price=83500, data_size_in_mb=15000, vendor='Irancell', number_of_purchases=20)
    InternetPackages.create(package_name='4gb 7 days', days_available=7, price=21500, data_size_in_mb=4000, vendor='Irancell', number_of_purchases=20)
    InternetPackages.create(package_name='300mb 7 days', days_available=7, price=7400, data_size_in_mb=300, vendor='Irancell', number_of_purchases=20)
    InternetPackages.create(package_name='500mb daily', days_available=1, price=670, data_size_in_mb=500, vendor='Irancell', number_of_purchases=20)
    InternetPackages.create(package_name='4gb 7 days', days_available=7, price=6030, data_size_in_mb=4000, vendor='Irancell', number_of_purchases=20)
    InternetPackages.create(package_name='5gb 7 days', days_available=7, price=3350, data_size_in_mb=5000, vendor='Irancell', number_of_purchases=20)
    InternetPackages.create(package_name='7gb 7 days', days_available=7, price=10050, data_size_in_mb=7000, vendor='Irancell', number_of_purchases=20)